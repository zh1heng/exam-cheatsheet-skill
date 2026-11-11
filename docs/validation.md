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
