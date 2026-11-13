"""Synthetic contract tests; no course material or student-performance claims."""
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from audit_harness import evaluate


def fixture():
    def question(qid, kind=None):
        q = {
            "id": qid, "family": "explain", "source": "synthetic prompt " + qid,
            "source_resolved": True, "rubric_basis": "derived",
            "rubric_locator": "synthetic expected answer fixed before attempt",
            "expected_region": "R1",
            "units": [{"id": str(i), "weight": 1, "critical": i == 0}
                      for i in range(10)],
            "attempt": {
                "candidate_sha256": "a" * 64, "agent_id": "solver",
                "answer": "Complete synthetic answer", "correct": True,
                "reviewer_id": "reviewer", "review_evidence": "checked against rubric",
                "first_region": "R1", "whole_sheet_search": False,
                "lookup_path": ["T1"], "navigation_evidence": "question cue led to R1/T1",
                "units": [{"id": str(i), "correct": True, "supported_by": ["T1"],
                           "support_evidence": "T1 rule plus input substitution",
                           "external_knowledge": ""} for i in range(10)]}}
        if kind:
            q["variant_kind"] = kind
        return q
    return {
        "schema_version": 1, "candidate_sha256": "a" * 64, "author_id": "author",
        "expected_ids": ["Q1"], "entries": {"T1": {"region": "R1"}},
        "questions": [question("Q1")],
        "variants": [question("V1", "transfer"), question("V2", "boundary")],
        "layout": {"regions": [{"id": "R1", "title": "Explain", "question_types": ["explain"]}],
                   "chosen_sequence": ["R1"], "rationale": "Group by answer task",
                   "order_sources": [], "disclosure": "No exam-order evidence; task-based grouping.",
                   "visual_verified": True, "visual_evidence": "synthetic render review"}}


class HarnessTests(unittest.TestCase):
    def test_all_gates_pass(self):
        self.assertTrue(evaluate(fixture())["accepted"])

    def test_exact_90_passes_but_below_90_does_not(self):
        data = fixture()
        units = data["questions"][0]["attempt"]["units"]
        units[-1]["supported_by"] = []
        report = evaluate(data)
        self.assertEqual(report["questions"][0]["support_percent"], 90)
        self.assertTrue(report["accepted"])
        units[-2]["supported_by"] = []
        self.assertFalse(evaluate(data)["accepted"])

    def test_combined_templates_count_each_unit_once(self):
        data = fixture()
        data["entries"]["T2"] = {"region": "R1"}
        data["questions"][0]["attempt"]["lookup_path"].append("T2")
        for i, unit in enumerate(data["questions"][0]["attempt"]["units"]):
            unit["supported_by"] = (["T1"] if i < 6 else []) + (["T2"] if 3 <= i < 8 else [])
        self.assertEqual(evaluate(data)["questions"][0]["support_percent"], 80)

    def test_critical_external_knowledge_fails_at_90(self):
        data = fixture()
        data["questions"][0]["attempt"]["units"][0]["external_knowledge"] = "unstated precondition"
        report = evaluate(data)
        self.assertEqual(report["questions"][0]["support_percent"], 90)
        self.assertFalse(report["accepted"])

    def test_weights_determine_ratio(self):
        data = fixture()
        data["questions"][0]["units"][0]["weight"] = 9
        data["questions"][0]["attempt"]["units"][0]["supported_by"] = []
        self.assertEqual(evaluate(data)["questions"][0]["support_percent"], 50)

    def test_missing_duplicate_and_extra_ids_fail(self):
        for mutation in (lambda d: d["expected_ids"].append("Q2"),
                         lambda d: d["questions"].append(copy.deepcopy(d["questions"][0])),
                         lambda d: d["expected_ids"].clear()):
            data = fixture()
            mutation(data)
            self.assertFalse(evaluate(data)["accepted"])

    def test_unresolved_is_not_answered(self):
        data = fixture()
        data["questions"][0]["source_resolved"] = False
        report = evaluate(data)
        self.assertEqual(report["questions"][0]["status"], "SOURCE_UNRESOLVED")
        self.assertFalse(report["accepted"])

    def test_stale_self_review_and_missing_unit_fail(self):
        for key, value in (("candidate_sha256", "b" * 64), ("agent_id", "author"),
                           ("reviewer_id", "solver"), ("answer", ""), ("correct", False)):
            data = fixture()
            data["questions"][0]["attempt"][key] = value
            self.assertFalse(evaluate(data)["accepted"], key)
        data = fixture()
        data["questions"][0]["attempt"]["units"].pop()
        self.assertFalse(evaluate(data)["accepted"])

    def test_unseen_family_variants_required(self):
        data = fixture()
        data["variants"].pop()
        self.assertFalse(evaluate(data)["accepted"])

    def test_first_region_and_whole_sheet_scan_fail(self):
        for key, value in (("first_region", "R2"), ("whole_sheet_search", True)):
            data = fixture()
            data["questions"][0]["attempt"][key] = value
            self.assertFalse(evaluate(data)["accepted"])

    def test_duplicate_order_sources_do_not_avoid_disclosure(self):
        data = fixture()
        source = {"id": "S1", "independence_key": "mock1", "kind": "mock",
                  "locator": "mock1 p1", "applicable": True, "sequence": ["R1"]}
        data["layout"]["order_sources"] = [source, dict(source, id="S2")]
        data["layout"]["disclosure"] = ""
        report = evaluate(data)
        self.assertEqual(report["order_evidence_count"], 1)
        self.assertFalse(report["accepted"])

    def test_conflicting_evidence_requires_disclosure(self):
        data = fixture()
        data["layout"]["regions"].append({"id": "R2", "title": "Code", "question_types": ["code"]})
        data["layout"]["chosen_sequence"].append("R2")
        data["layout"]["order_sources"] = [
            {"id": str(i), "independence_key": str(i), "kind": "paper", "locator": "p1",
             "applicable": True, "sequence": seq}
            for i, seq in enumerate((["R1", "R2"], ["R2", "R1"]))]
        data["layout"]["disclosure"] = ""
        self.assertFalse(evaluate(data)["accepted"])

    def test_invalid_weight_and_unknown_template_fail(self):
        for value in (0, -1, True, float("nan")):
            data = fixture()
            data["questions"][0]["units"][0]["weight"] = value
            self.assertFalse(evaluate(data)["accepted"])
        data = fixture()
        data["questions"][0]["attempt"]["units"][0]["supported_by"] = ["missing"]
        self.assertFalse(evaluate(data)["accepted"])

    def test_wrong_noncritical_answer_unit_cannot_pass_at_90(self):
        data = fixture()
        data["questions"][0]["attempt"]["units"][-1]["correct"] = False
        self.assertFalse(evaluate(data)["accepted"])

    def test_family_statistics_keep_question_denominator(self):
        data = fixture()
        report = evaluate(data)
        self.assertEqual(report["families"]["explain"]["question_count"], 1)
        self.assertEqual(report["families"]["explain"]["pass_percent_of_returned_questions"], 100)
        self.assertEqual(report["question_pass_percent"], 100)

    def test_decimal_weights_exact_90_and_overflow_rejected(self):
        data = fixture()
        for unit in data["questions"][0]["units"]:
            unit["weight"] = 0.1
        data["questions"][0]["attempt"]["units"][-1]["supported_by"] = []
        self.assertTrue(evaluate(data)["accepted"])
        for value in (10 ** 400, 1e308):
            data = fixture()
            for unit in data["questions"][0]["units"]:
                unit["weight"] = value
            self.assertFalse(evaluate(data)["accepted"])

    def test_cli_checks_hash_and_does_not_overwrite_hardlinked_input(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            sheet = root / "candidate.txt"
            sheet.write_bytes(b"synthetic sheet")
            data = fixture()
            digest = hashlib.sha256(sheet.read_bytes()).hexdigest()
            data["candidate_sha256"] = digest
            for q in data["questions"] + data["variants"]:
                q["attempt"]["candidate_sha256"] = digest
            audit = root / "audit.json"
            audit.write_text(json.dumps(data), encoding="utf-8")
            output = root / "report.json"
            command = [sys.executable, "-X", "utf8", str(Path(__file__).with_name("audit_harness.py")),
                       str(audit), "--sheet", str(sheet), "--output", str(output)]
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
            sheet.write_bytes(b"changed sheet")
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
            self.assertFalse(json.loads(output.read_text(encoding="utf-8"))["accepted"])
            linked = root / "linked.txt"
            try:
                os.link(sheet, linked)
            except OSError as exc:
                self.skipTest(str(exc))
            command[-1] = str(linked)
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 2)
            self.assertEqual(sheet.read_bytes(), b"changed sheet")

    def test_duplicate_records_cannot_inflate_navigation_statistics(self):
        data = fixture()
        data["questions"].append(copy.deepcopy(data["questions"][0]))
        report = evaluate(data)
        self.assertEqual(report["first_region_success_count"], 1)
        self.assertEqual(report["families"]["explain"]["question_count"], 1)

    def test_cross_region_requires_actual_link_and_lookup_path(self):
        data = fixture()
        data["layout"]["regions"].append({"id": "R2", "title": "Other", "question_types": ["other"]})
        data["layout"]["chosen_sequence"].append("R2")
        data["entries"]["T1"]["region"] = "R2"
        self.assertFalse(evaluate(data)["accepted"])
        data["entries"]["INDEX"] = {"region": "R1", "links": ["T1"]}
        for q in data["questions"] + data["variants"]:
            q["attempt"]["lookup_path"] = ["INDEX", "T1"]
        self.assertTrue(evaluate(data)["accepted"])

    def test_original_question_cannot_be_relabelled_as_variant(self):
        data = fixture()
        data["variants"][0]["source"] = data["questions"][0]["source"]
        self.assertFalse(evaluate(data)["accepted"])


if __name__ == "__main__":
    unittest.main()
