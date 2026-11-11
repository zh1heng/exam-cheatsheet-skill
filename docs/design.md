# First-version design

Requested outcome: extract a successful exam-cheatsheet workflow into a reusable skill and place the project on the user's GitHub account.

Approach chosen as an implementation default: a portable Markdown skill with references, an original example, and a Chinese README. A standalone upload-and-render application would require a separate interface and document-processing implementation; that is outside this first version.

Inputs: current course scope and sheet rules, lecture material, representative questions, an existing sheet where applicable, and student language preferences.

Outputs: a sheet or requested audit, sources and verification notes, and editable/rendered artifacts when supported by the host environment.

Core behavior: question wording leads to visible entries, conditional decisions, executable steps and exam answers. Verify actual lookup and use separately from content inclusion. Preserve existing printed versions and avoid inferring exam probabilities or mastery.

Follow-up requirements: apply a claim-specific course-source hierarchy including teacher recordings/transcripts; establish single-sided versus double-sided permission explicitly; use independent question attempts and a bounded feedback/repair/retest loop; enforce a minimum effective printed text size of 5pt (or a larger official minimum); distinguish major headings, reasoning, answer templates and evidenced priorities through typography, colors and backgrounds that remain legible in grayscale.

Language design: allocate question-language aliases to recognition, the student's strongest language to reasoning and executable steps, and the required answer language to terminology and answer patterns. Avoid full-paragraph bilingual duplication; preserve code and mathematical notation and test the bridges between these roles.

Repository contents are reusable instructions and original examples. They do not include course source files or private student records. No standalone renderer, account integration, or automatic tutoring system is included.

Validation: validate skill metadata and references; check example arithmetic and algorithm trace; run an independent behavioral exercise with synthetic source facts; report limited scope honestly. No course marks, future exam outcomes, student lookup speed, or physical print quality are claimed.
