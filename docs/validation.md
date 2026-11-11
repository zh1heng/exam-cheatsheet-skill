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
