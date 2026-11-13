---
name: cheatsheet-master
description: Use when a student wants to create, audit, or revise an exam reference sheet or cheatsheet from course materials, especially when page space is limited or existing notes are difficult to locate and apply to questions.
---

# Cheatsheet Master

Build a sheet students can navigate from question wording and use to produce an answer. Treat coverage, findability, usability, print quality, and mastery as separate claims.

## Establish the task

Read any course-specific study instructions and the current sheet before editing. Recover current scope, exclusions, permitted sheet format, source files, language preferences, and requested changes. Reuse information already available; ask only for missing constraints that materially affect the result. If an official rule is unavailable, label the assumption rather than inventing permission.

Before selecting content, read [source-priority.md](references/source-priority.md). Extract dated teacher statements from recordings/transcripts about scope, corrections, emphasis, and answer requirements, retaining timestamps and transcription uncertainty. Resolve authority and applicability rather than blindly preferring a newer file. Record paper size, sheet count, permitted sides, typed/handwritten rules, and any font/color restrictions: **one sheet does not establish permission for two sides**.

Keep the workflow within the request: an audit need not trigger a redesign; making a sheet need not trigger tutoring. Respect a student's chosen question pool. For a new sheet, use current course materials to establish coverage and questions to establish how knowledge is applied.

## Deliver a first version, then personalize

Default to producing a usable **v1 draft** from available course evidence and known user preferences. Do not postpone it for a long preference interview, exhaustive personalization, or all final acceptance rounds. Apply known exam constraints, check essential content and the rendered layout when generating a document, and disclose specific unknowns and pending checks. Share the actual draft, not merely a proposed structure; do not label it final or independently accepted before those checks occur.

Use the user's subsequent requests and observed difficulties to make scoped v2/v3 revisions. Preserve the previous usable/printed version and stable entry IDs. Record what changed and why; recheck affected content and layout. User-directed revision can continue after an internal review round limit; that limit does not cap the lifetime of the sheet. Keep an established working version instead of restarting the whole design for each preference.

## Build from questions

1. Inventory current topics and sources. Distinguish verified current instructions, original questions, teacher answers, inferred answer advice, and generated examples. Preserve precise source locators in a companion audit; never invent marks or an official rubric.
2. Group questions by exam question type, then by method and consequential conditions. Prefer the supported exam/mock/teacher-stated order for the main sheet regions; map question cues to a primary page/column region and stable entry IDs, with explicit cross-region links for combined answers. Count independent applicable order sources, not duplicate copies or mere topic-scope statements. If fewer than two exist, explicitly tell the user the evidence count and the actual chosen ordering and its basis. Explain conflicting evidence too; do not promise the next exam's order. Classify the full in-scope question inventory, but solve representative questions per method/condition/output family. Merge data-only repetitions in the attempt set; retain consequential variants and make a coverage decision for unrepresented current topics. See [peer-review-and-layout.md](references/peer-review-and-layout.md) for selection and navigation checks.
3. Use recognizable question words as visible headings or aliases with stable IDs. Add a reasoning bridge for scenarios that do not name the concept. Do not require the student to know the answer before locating the entry.
4. Write each entry as **trigger → decision criteria → steps → required output → answer pattern → trap**. Allocate languages by function: question-language aliases for recognition, the student's strongest language for decisions/steps, and exam-answer language for precise terms and usable sentences. Preserve code and mathematical notation. Avoid duplicating whole paragraphs through translation. Explain placeholders and conditions. Read [language-design.md](references/language-design.md) when building multilingual entries and [entry-and-audit.md](references/entry-and-audit.md) for the entry format and audit.
5. Allocate space by current scope, task diversity, likely lookup difficulty, and the student's priorities. Historical occurrence is descriptive, not an exam probability. Flag the tradeoff if a requested allocation crowds out confirmed topics; respect the user's final choice. Compress duplicate explanations before shrinking text.
6. Repeated identical code may use visible `@NAME` shared snippets to save space. Define every reference on the permitted sheet, explain literal in-place expansion and any explicit parameters, and verify expansion preserves the original code. Keep differing conditions/control flow explicit. Read [code-shorthand.md](references/code-shorthand.md) when using this notation; it is sheet shorthand, not automatically valid submitted code.

Use [the original worked example](examples/keyword-to-answer.md) when a concrete illustration would help. Adapt its structure, not its topic choices or language assumptions.

## Verify and iterate

Default to **full classification, representative actual attempts**, not exhaustive solving. Read [peer-review-and-layout.md](references/peer-review-and-layout.md). Map each identifiable in-scope question to a family defined by method, consequential conditions, and required output. Select one substantive original question per family, plus only the additional cases needed to exercise materially different decisions, boundaries, output forms, or template combinations. Different data or story names alone do not require another attempt. Do not select only easy examples or classify everything under broad labels such as “Java”.

Keep a compact classification/selection table with source IDs, family, representative IDs, selection reasons, and untested or unresolved members. Do not write answers or detailed rubrics for every unselected member. Prefer existing unseen questions for necessary transfer/boundary checks; generate a variant only when an important distinction is absent. There is no automatic quota of two generated variants per sheet entry.

For the selected set, use one additional independent solver by default, in compact batches; the author separately reviews correctness and sheet support. Give the solver only assigned questions and the candidate sheet, not answers or author lookup routes. Each selected answer must be complete and correct, have at least 90% weighted support for its necessary answer units, and have all critical conditions/steps supported. Fix official or labelled derived units before inspecting performance; record template combinations, actual lookup path and outside knowledge concisely. Shared rubrics can be reused within the same applicable family. The 90% threshold applies to tested questions, never automatically to all classified members. If independent tools are unavailable or declined, disclose the missing independent check rather than inventing it.

After a repair, retest failed representatives and cases affected by changed entries or shared dependencies. Preserve prior results for demonstrably unchanged content, recording their original version and why they still apply; do not relabel old attempts as newly performed on the latest file. Layout-only edits need current rendering and affected navigation checks, not another round of content solving. Keep the initial selected count visible, avoid unbounded case expansion, and stop at user resource limits or at most two targeted repair rounds with unresolved work disclosed.

Report classification coverage, representative attempts, necessary variants, carried-forward evidence, unresolved families and layout separately. “Representative-question acceptance passed” is allowed when those checks pass; “all original questions independently passed” is not. Assistant attempts do not establish student speed or mastery. Use [acceptance-harness.md](references/acceptance-harness.md) and its strict JSON checker only when the user explicitly requests exhaustive per-question acceptance; do not build that heavy ledger for ordinary representative checks.

For procedural questions, include the intermediate states the question requests. A memorized final formula or algorithm name is insufficient when a trace, tree, proof, or code is required. Put long demonstrations in a companion guide if sheet space is limited.

For PDF/DOCX output, use available document tools and render every final page. Inspect page count/size, clipping, column collisions, symbols, diagrams, code, contrast, and consistency with the editable source. Record actual font sizes. If rendering or printing is unavailable, report that limitation; do not claim visual or physical verification.

Use **5 pt as the minimum effective printed size**, not a target for every element; obey a larger official minimum. Include code, labels, footnotes and mathematical scripts in the check, accounting for export transformations and intended print scaling. Do not silently go below the floor to fit. Use larger, visually distinct major headings with consistent colors/background bands; distinguish keyword entries, reasoning, answer templates and evidenced priorities with both styling and text. Recheck grayscale legibility. Follow the detailed layout gates in [peer-review-and-layout.md](references/peer-review-and-layout.md).

For space-limited sheets, default to starting directly with question-type regions and topic entries: omit a large document title and repeated navigation/instruction paragraphs; put source and usage notes in the companion record. Give question-type regions distinguishable, consistent heading bands and text labels so users can search one region first; use selective red text only with clear semantics distinct from warning markers. Make topic headings prominent; give answer templates a distinct light fill, visible border, and short text label. Separate three columns with two continuous black vertical rules in the gutters on every page (for other multi-column layouts, separate adjacent columns). Verify these features on the actual-size color and grayscale renders, with no text touching the rules. Explicit user styling and official exam restrictions override these defaults; preserve existing content and stable entry IDs during a layout-only edit.

Preserve a usable old/printed version and stable IDs unless replacement or renumbering is requested. For a targeted repair, change the relevant content and recheck layout; do not silently redesign the whole sheet.

## Deliver

Provide the requested sheet, editable source when generated, and concise source/verification notes outside the cramped sheet. State unresolved scope, unverified answers, and layout or print limits. Track practice only if requested, distinguishing guided, attempted, corrected, and independently verified work. Do not infer new mastery from delivery or acknowledgement.

Publication of the reusable method does not authorize uploading private course materials, student records, or other source files. Keep examples original or appropriately licensed and publish only the requested project contents.
