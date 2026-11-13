# Validation record

Date: 2026-11-11.

## Structural checks

- The skill-creator `quick_validate.py` validator accepted the skill's name, frontmatter and lack of unfinished scaffold markers.
- Local Markdown references and the agent metadata were checked for valid targets and consistent skill naming.
- The original graph example was checked by enumerating spanning trees: AB, BC, CD is the minimum-cost tree, with total cost 6.

## Behavioral checks

Before authoring, an independent agent received a synthetic request about a one-page bilingual sheet, difficult question aliases, MST versus shortest paths, uncertain hashing scope, and guided-only study history. Its response already distinguished source uncertainty, printing limits and independent mastery. This was not evidence of a failed baseline or a measured improvement from this skill.

After authoring, a fresh independent agent used the skill on a different synthetic case: a printed Java method-dispatch entry headed `04b Dispatch`, with only the instruction “看类型，找方法”, and a question asking `Which implementation runs?`. The user could not reprint and had only watched a guided example.

Observed response:

- Identified both the lookup problem and the missing distinction between reference and object types.
- Preserved `04b` and proposed a small annotation instead of a replacement sheet.
- Added the question's wording as an entry and explained compile-time accessibility/overload resolution versus runtime overriding.
- Correctly answered the supplied `Animal a = new Dog(); a.speak();` case using the supplied course facts.
- Kept the unseen overload question unverified; did not invent marks, print verification, or mastery.

The reviewer found no substantive error in this exercise. It suggested an optional more explicit no-reprint repair rule; the current instruction to respect scope and preserve printed versions already supported that behavior, so no additional universal requirement was added.

## Limits

These are structural checks and one post-authoring behavioral smoke test, not a statistical evaluation. There is no controlled proof that this skill improves outcomes over an unassisted model. No real exam score, timed student lookup, physical printing, PDF renderer, or every-client installation was tested. The examples use supplied or original material rather than uploading any private course source files.

## Follow-up: sources, constraints and feedback loop

The user subsequently requested explicit source priority (including teacher recordings/transcripts), single-sided constraints, independent question acceptance with a feedback loop, a 5pt minimum and visual hierarchy. A read-only baseline review of the initial skill found these were largely additional decisions the reviewer had to supply rather than explicit procedures. The follow-up adds focused references and connects them from the main skill.

An independent acceptance agent used the revised skill on a synthetic conflict case: current notice requires one A4 side, minimum 6pt and monochrome; old rules allow double-sided; a teacher transcript has uncertain negation and a separate clear MST answer requirement; candidate settings describe two pages, 6pt body, 4.8pt scripts and 90% print scale. No actual PDF or audio was supplied.

Observed audit correctly rejected exam-ready status, retained the uncertain exclusion as unresolved, extracted the clear teacher output requirement, applied current single-side/monochrome rules, and calculated effective sizes of 5.4pt and 4.32pt. It applied the official 6pt minimum over the project's 5pt floor, and did not claim rendering, listening or printing had occurred.

### Actual blind question trial and repair

A separate agent received only synthetic graph questions and a deliberately defective text sheet v0, without solutions or author hints. The sheet conflated connecting all sites with shortest paths and incorrectly allowed Dijkstra whenever no negative cycle exists.

- For the minimum cable network, the agent identified that the sheet's distance output did not answer the question; its own MST knowledge was necessary to supply the correct tree.
- For shortest paths, it produced correct distances but explicitly identified missing initialization, relaxation, selection and precondition guidance.
- For the negative-edge question, it reported the sheet's incorrect rule and provided a counterexample as outside-sheet knowledge.

The main author repaired this synthetic text candidate: separate question-language entries; Chinese decision criteria and executable Prim/Dijkstra steps; English answer patterns; required edges/tree/total output; nonnegative-edge condition; and a disconnected-graph stopping condition.

A fresh blind agent then attempted the three failed/incomplete cases plus the disconnected-graph variant using v1. It returned:

| Case | Verified outcome |
|---|---|
| Undirected cables AB=2, AC=3, BC=1, CD=2, AD=4, BD=8; minimum connected network | AB, BC, CD; tree A—B—C—D; total 5 |
| Same graph; shortest distances from A | A=0, B=2, C=3, D=4, with relaxation steps |
| Negative edge and no negative cycle; is Dijkstra guaranteed? | No, with the settled-distance reasoning supplied by v1 |
| Only AB=2 and CD=2 available | Disconnected; no spanning tree covering all four vertices |

The retest agent reported using only ordinary arithmetic/graph reading beyond the supplied sheet. The main author checked the outputs and reasoning. This demonstrates one text-only feedback-and-retest cycle, not a rendered sheet or a measured improvement in student performance.

### Language-role exercise

Using the new language reference and supplied fictional interview facts, an independent agent produced a `main flaw / useful information` entry: English question aliases for navigation, Chinese evidence-to-effect reasoning, and an English leading-question answer. It explained placeholders and avoided duplicating the whole Chinese explanation in English.

The same reviewer identified a real omission in the language reference's Prim example: graph preconditions and disconnected-graph termination were implicit. The author added both explicitly; the focused independent recheck confirmed the issue resolved while preserving the intended language roles. This is a content correction prompted by actual feedback, not a claim that a correct translation alone establishes understanding.

## 2026-11-12: initial delivery and @ code compression

A focused pre-change review found that scoped revisions already existed, but the skill did not explicitly separate early v1 delivery from final acceptance and had no @ expansion convention. The update adds both without relaxing basic correctness or known exam-format requirements.

A fresh agent used the revised skill to produce an actual text-only 0/1/2 sorting entry from supplied branches. It delivered v1 without postponing it for final acceptance, defined @SWAP locally, retained distinct pointer updates and explained the temporary variable. It then self-expanded both references and traced [2,0,1] through [1,0,2], [1,0,2], [0,1,2], ending with low=1, mid=2, high=1. The main author checked the expanded branches and trace against the supplied original behavior.

This was an independent exercise of the skill, followed by the drafting agent's self-check of its candidate; it was not a second blind solver's final acceptance of that candidate. The agent correctly distinguished those claims and did not claim PDF, font-size or print verification. Structural validation and Markdown reference checks also passed. No executable macro preprocessor or actual sheet layout was added or tested.

## 2026-11-12: exhaustive acceptance and evidence-ledger harness

The skill now requires exhaustive in-scope question attempts by additional independent agents, question-type regions, order-evidence disclosure when fewer than two independent applicable sources exist, and at least 90% weighted sheet support for each complete correct answer. Template contributions form a union of answer units; critical unsupported units still fail. Transfer and boundary variants test stated applicability without claiming universal generality.

A read-only baseline agent identified absent percentage/denominator/combination rules, absent order-evidence disclosure and a gap in unseen transfer testing. The update adds a state/evidence contract and the standard-library `audit_harness.py` checker. It does not launch agents, grade answers semantically, render PDFs or independently discover source questions.

Validation performed on the revised source and installed skill:

- 20 synthetic unit/CLI tests passed, including the exact 90% boundary, weighted template unions, external critical knowledge, wrong answer units, missing/duplicate/extra IDs, candidate hashes, separate role identifiers, transfer/boundary requirements, explicit cross-region navigation links, duplicate/conflicting order evidence and numerical edge cases.
- An independent reviewer reproduced an output hard-link overwrite vulnerability and ambiguous row-based statistics. These were repaired; the reviewer retested hard links to both input files, rejected extreme weights without malformed reports, verified expected-ID statistics and rejected invalid navigation/relabelled variant records. No blocking issue remained in that review.
- Both skill frontmatter validations passed; 26 local Markdown link targets resolved; all six changed/added installed skill files matched the source checkout byte-for-byte.

These tests use synthetic evidence ledgers, not real exam questions. They establish checker behavior and recorded-evidence gates, not rubric validity, genuine actor independence, comprehensive source discovery, unseen-variant quality, measured student lookup speed, real PDF layout or a 90% score on any course examination. Those semantic and physical checks remain explicit execution duties.


## 2026-11-13: representative-by-family acceptance

This update supersedes the preceding exhaustive-default policy. The installed skill and checkout now default to full source classification with actual attempts only for a representative set, retaining distinctions that change methods, preconditions, boundaries, outputs or template combinations. Exhaustive per-question acceptance and its unchanged JSON checker are opt-in only. Layout-only edits do not trigger content re-solving; content repairs retest affected representatives and shared dependencies.

A bounded read-only policy scenario was run before and after the edit using one additional agent (`/root/check_sampling_rule`). Scenario: 120 questions comprising 100 data-only linear-search repetitions, 10 new-array reversal questions and 10 in-place reversal questions, followed by a font-size-only edit. Before the change, the agent applied the existing exhaustive rule to all 120 questions. After re-reading the revised instructions, it selected three base representatives when no other consequential distinctions exist, adding cases only for uncovered important boundaries; it kept the other 117 as classified but untested. It correctly limited font edits to final rendering/effective font size/affected navigation checks, did not invoke the legacy JSON checker by default, and retained exhaustive mode when expressly requested.

This was a small before/after interpretation check using the same reviewer, not a fresh blinded evaluation, real course acceptance, measured token saving, or evidence that three questions suffice for any real course. No course questions were solved and no sheet acceptance was rerun.

Both source and installed skill passed quick_validate.py with Python UTF-8 mode. The four edited skill documents match byte-for-byte; 17 local Markdown links within the skill resolve. Existing layout/font requirements were checked unchanged. The strict JSON checker and its tests were not modified or rerun in this documentation-only change. Previous historical validation records remain intact.


## 2026-11-13: Cheatsheet Master naming and publication checks

Renamed the skill directory and frontmatter to `cheatsheet-master`, display title to `Cheatsheet Master`, and invocation to `$cheatsheet-master`. Updated README references and added a GitHub installation example and old-name migration note. Repository URL remains unchanged. Source checkout and installed copy contain the same 11 non-cache skill files; old skill directories are absent.

Before publication, both quick validators passed in UTF-8 mode, all 29 local Markdown links in the repository resolved, and the existing strict ledger checker passed its 20 synthetic unit/CLI tests from the renamed path. Name/display/default-prompt consistency and `git diff --check` passed. These checks do not constitute a new exam-sheet audit or measured quota savings.


## 2026-11-13: GitHub-distributed Codex plugin 1.0.0

Added root `plugin.json`, a matching `.codex-plugin/plugin.json` compatibility manifest, and `.agents/plugins/marketplace.json` for `zh1heng-study-tools`. The marketplace resolves `cheatsheet-master` from the repository root. The plugin packages the existing skill without MCP services, connections or hooks. README documents source registration, desktop installation, optional CLI installation, updating and standalone-skill fallback.

On codex-cli 0.167.0-alpha.4.1, a clean isolated CODEX_HOME and a package-only copy were used to run marketplace add, available-plugin listing, plugin add and installed-plugin listing. All exited successfully; the installed listing reported `cheatsheet-master@zh1heng-study-tools`, version `1.0.0`, installed and enabled. All 11 non-cache skill files in the installation matched the source. Portable/compatibility metadata and local links were checked for consistency. No actual user plugin configuration was changed.

This verifies local CLI discovery and installation, not every client version or the desktop UI. No exam-sheet generation or expensive representative/full-question acceptance was rerun. The repository is a custom GitHub marketplace, not a listing in the universal public plugin directory.
