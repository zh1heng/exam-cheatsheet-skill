"""Evidence-ledger gate checker, not an answer grader or autonomous agent runner.

Usage: python audit_harness.py audit.json --sheet candidate.pdf --output report.json
Exit 0: recorded gates pass; 1: incomplete/failed gates; 2: malformed input.
See references/acceptance-harness.md for the contract and semantic review duties.
"""
import argparse
from collections import Counter
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def unique(values):
    return len(values) == len(set(values))


def finite_positive(value):
    try:
        return type(value) in (int, float, Decimal) and math.isfinite(value) and value > 0
    except OverflowError:
        return False


def evaluate(data):
    errors = []
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    candidate = data.get("candidate_sha256", "")
    if len(candidate) != 64 or any(c not in "0123456789abcdef" for c in candidate):
        errors.append("candidate_sha256 must be a lowercase SHA-256")
    author = data.get("author_id")
    if not nonempty(author):
        errors.append("author_id required")
    expected = data["expected_ids"]
    questions = data["questions"]
    variants = data["variants"]
    entries = data["entries"]
    layout = data["layout"]
    regions = [r["id"] for r in layout["regions"]]
    if not regions or not unique(regions):
        errors.append("nonempty unique region IDs required")
    for region in layout["regions"]:
        if not nonempty(region.get("title")) or not region.get("question_types"):
            errors.append("each region needs visible title and question types")
    for eid, entry in entries.items():
        if entry["region"] not in regions:
            errors.append("unknown region for entry " + eid)
        if not set(entry.get("links", [])).issubset(entries):
            errors.append("unknown cross-reference for entry " + eid)
    sequence = layout["chosen_sequence"]
    if not unique(sequence) or set(sequence) != set(regions):
        errors.append("chosen_sequence must contain each region exactly once")
    if not nonempty(layout.get("rationale")):
        errors.append("layout rationale required")
    if layout.get("visual_verified") is not True or not nonempty(layout.get("visual_evidence")):
        errors.append("final visual review evidence required")

    sources = layout["order_sources"]
    evidence = []
    for source in sources:
        if source.get("applicable") is True:
            if (source.get("kind") not in {"paper", "mock", "teacher"}
                    or not nonempty(source.get("locator"))
                    or not nonempty(source.get("independence_key"))
                    or not source.get("sequence")
                    or not set(source["sequence"]).issubset(regions)):
                errors.append("invalid applicable order source " + str(source.get("id")))
            else:
                evidence.append(source)
    evidence_count = len({s["independence_key"] for s in evidence})
    # Conservative: differing or partial sequences require an explicit explanation.
    order_conflict = any(s["sequence"] != sequence for s in evidence)
    if (evidence_count < 2 or order_conflict) and not nonempty(layout.get("disclosure")):
        errors.append("order evidence below 2 or differs: user disclosure required")

    ids = [q["id"] for q in questions]
    all_ids = ids + [q["id"] for q in variants]
    missing = sorted(set(expected) - set(ids))
    extra = sorted(set(ids) - set(expected))
    duplicates = sorted(k for k, count in Counter(all_ids).items() if count > 1)
    if not expected or not unique(expected) or missing or extra or duplicates:
        errors.append("inventory is empty, duplicated, missing or has extra IDs")

    def score(q):
        issues = []
        qid = q["id"]
        if not nonempty(q.get("family")) or not nonempty(q.get("source")):
            issues.append("family and source required")
        resolved = q.get("source_resolved") is True
        if not resolved:
            return {"id": qid, "family": q.get("family"), "status": "SOURCE_UNRESOLVED",
                    "support_percent": None, "supported_weight": 0, "total_weight": None,
                    "passed": False, "issues": ["unresolved question source"], "navigation_passed": False}
        if q.get("rubric_basis") not in {"official", "derived"} or not nonempty(q.get("rubric_locator")):
            issues.append("official or explicitly derived rubric evidence required")
        rubric = q["units"]
        if not rubric or not unique([u["id"] for u in rubric]):
            issues.append("nonempty unique rubric units required")
        weights_ok = all(finite_positive(u.get("weight")) and type(u.get("critical")) is bool for u in rubric)
        if weights_ok:
            weights_ok = finite_positive(sum(Decimal(str(u["weight"])) for u in rubric))
        if not weights_ok:
            issues.append("positive finite weights and boolean critical flags required")
        attempt = q.get("attempt", {})
        if attempt.get("candidate_sha256") != candidate:
            issues.append("attempt uses different candidate")
        solver, reviewer = attempt.get("agent_id"), attempt.get("reviewer_id")
        if not nonempty(solver) or solver == author:
            issues.append("additional independent solver required")
        if not nonempty(reviewer) or reviewer == solver or not nonempty(attempt.get("review_evidence")):
            issues.append("separate correctness review required")
        if not nonempty(attempt.get("answer")) or attempt.get("correct") is not True:
            issues.append("complete correct answer required")
        attempted_units = attempt.get("units", [])
        unit_ids = [u["id"] for u in attempted_units]
        if not unique(unit_ids) or set(unit_ids) != {u["id"] for u in rubric}:
            issues.append("attempt unit IDs must match rubric exactly")
        by_id = {u["id"]: u for u in attempted_units}
        used_templates = set()
        supported = total = Decimal(0)
        for unit in rubric:
            record = by_id.get(unit["id"], {})
            if record.get("correct") is not True:
                issues.append("incorrect or unverified answer unit: " + unit["id"])
            refs = record.get("supported_by", [])
            if not isinstance(refs, list) or not all(isinstance(r, str) and r in entries for r in refs):
                issues.append("unknown or malformed template references")
                refs = []
            used_templates.update(refs)
            supported_here = (bool(refs) and record.get("correct") is True
                              and nonempty(record.get("support_evidence"))
                              and record.get("external_knowledge") == "")
            if unit.get("critical") and not supported_here:
                issues.append("critical unit unsupported: " + unit["id"])
            if weights_ok:
                total += Decimal(str(unit["weight"]))
                if supported_here:
                    supported += Decimal(str(unit["weight"]))  # Union of templates; never sum template percentages.
        percentage = float(100 * supported / total) if total else None
        path = attempt.get("lookup_path", [])
        valid_path = isinstance(path, list) and bool(path) and all(isinstance(e, str) and e in entries for e in path)
        if valid_path:
            valid_path = (entries[path[0]]["region"] == attempt.get("first_region")
                          and used_templates.issubset(path)
                          and all(entries[a]["region"] == entries[b]["region"] or b in entries[a].get("links", [])
                                  for a, b in zip(path, path[1:])))
        navigation = (valid_path and nonempty(attempt.get("navigation_evidence"))
                      and q.get("expected_region") in regions
                      and attempt.get("first_region") == q.get("expected_region")
                      and attempt.get("whole_sheet_search") is False)
        if not navigation:
            issues.append("first-region lookup failed or required whole-sheet scan")
        if percentage is None or supported < Decimal("0.9") * total:
            issues.append("sheet support below 90 percent")
        passed = not issues
        return {"id": qid, "family": q.get("family"), "status": "SUPPORTED" if passed else "PARTIAL" if supported else "UNSUPPORTED",
                "support_percent": percentage, "supported_weight": float(supported), "total_weight": float(total),
                "passed": passed, "navigation_passed": navigation, "issues": issues}

    results = [score(q) for q in questions]
    variant_results = [dict(score(q), variant_kind=q.get("variant_kind")) for q in variants]
    variant_sources = [q.get("source") for q in variants]
    if (not unique(variant_sources)
            or set(variant_sources) & {q.get("source") for q in questions}):
        errors.append("variants need distinct prompt references, not relabelled original questions")
    families = {q.get("family") for q in questions}
    for family in families:
        passed_kinds = {r["variant_kind"] for r in variant_results if r["family"] == family and r["passed"]}
        if not {"transfer", "boundary"}.issubset(passed_kinds):
            errors.append("family needs passed transfer and boundary variants: " + str(family))
    if any(r["family"] not in families or r["variant_kind"] not in {"transfer", "boundary"}
           for r in variant_results):
        errors.append("variant family or kind not in declared scope")
    if any(not r["passed"] for r in results + variant_results):
        errors.append("one or more question/variant gates failed")
    canonical = {}
    for row in results:
        if row["id"] in expected and row["id"] not in canonical:
            canonical[row["id"]] = row
    canonical_results = list(canonical.values())
    total = sum(Decimal(str(r["total_weight"] or 0)) for r in canonical_results)
    supported = sum(Decimal(str(r["supported_weight"])) for r in canonical_results)
    unresolved = sum(r["status"] == "SOURCE_UNRESOLVED" for r in canonical_results)
    family_reports = {}
    for family in sorted({r["family"] for r in canonical_results}, key=str):
        rows = [r for r in canonical_results if r["family"] == family]
        family_total = sum(Decimal(str(r["total_weight"] or 0)) for r in rows)
        family_supported = sum(Decimal(str(r["supported_weight"])) for r in rows)
        family_reports[family] = {
            "question_count": len(rows), "passed_count": sum(r["passed"] for r in rows),
            "pass_percent_of_returned_questions": 100 * sum(r["passed"] for r in rows) / len(rows),
            "scope": "unique returned expected IDs only; missing IDs have no verified family assignment",
            "weighted_support_percent_resolved_only": float(100 * family_supported / family_total) if family_total else None,
            "unresolved_count": sum(r["status"] == "SOURCE_UNRESOLVED" for r in rows),
            "failed_ids": [r["id"] for r in rows if not r["passed"]]}
    # Only expected IDs earn pass credit; missing IDs stay in the denominator.
    pass_ids = {r["id"] for r in canonical_results if r["passed"]}
    return {"accepted": not errors, "errors": errors, "candidate_sha256": candidate,
            "expected_count": len(expected), "processed_count": len(set(ids)),
            "unresolved_count": unresolved, "missing_ids": missing, "extra_ids": extra,
            "duplicate_ids": duplicates, "order_evidence_count": evidence_count,
            "order_conflict_or_difference": order_conflict,
            "weighted_support_percent_resolved_only": float(100 * supported / total) if total else None,
            "per_question_pass_count": len(pass_ids),
            "question_pass_percent": 100 * len(pass_ids) / len(set(expected)) if expected else None,
            "first_region_success_count": sum(r["navigation_passed"] for r in canonical_results),
            "families": family_reports, "questions": results, "variants": variant_results,
            "limitation": "Checks recorded evidence and arithmetic. Humans/agents must verify complete source inventory, frozen rubric, actor independence, actual template bridges, genuinely unseen meaningful variants and visual quality. Distinct prompt references alone do not prove generality. Family percentages cover returned IDs only. Not an exam-score prediction."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    parser.add_argument("--sheet", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        if (args.output.resolve() in {args.audit.resolve(), args.sheet.resolve()}
                or (args.output.exists() and any(args.output.samefile(p) for p in (args.audit, args.sheet)))):
            raise ValueError("output must not overwrite input files")
        data = json.loads(args.audit.read_text(encoding="utf-8-sig"))
        actual_hash = hashlib.sha256(args.sheet.read_bytes()).hexdigest()
        report = evaluate(data)
        if actual_hash != data["candidate_sha256"]:
            report["errors"].append("actual sheet hash differs from candidate")
            report["accepted"] = False
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
        print(json.dumps({"accepted": report["accepted"], "errors": report["errors"]}, ensure_ascii=False))
        return 0 if report["accepted"] else 1
    except (OSError, ValueError, KeyError, TypeError, AttributeError, OverflowError) as exc:
        print(json.dumps({"accepted": False, "input_error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
