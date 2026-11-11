# First-version design

Requested outcome: extract a successful exam-cheatsheet workflow into a reusable skill and place the project on the user's GitHub account.

Approach chosen as an implementation default: a portable Markdown skill with references, an original example, and a Chinese README. A standalone upload-and-render application would require a separate interface and document-processing implementation; that is outside this first version.

Inputs: current course scope and sheet rules, lecture material, representative questions, an existing sheet where applicable, and student language preferences.

Outputs: a sheet or requested audit, sources and verification notes, and editable/rendered artifacts when supported by the host environment.

Core behavior: question wording leads to visible entries, conditional decisions, executable steps and exam answers. Verify actual lookup and use separately from content inclusion. Preserve existing printed versions and avoid inferring exam probabilities or mastery.

Repository contents are reusable instructions and original examples. They do not include course source files or private student records. No standalone renderer, account integration, or automatic tutoring system is included.

Validation: validate skill metadata and references; check example arithmetic and algorithm trace; run an independent behavioral exercise with synthetic source facts; report limited scope honestly. No course marks, future exam outcomes, student lookup speed, or physical print quality are claimed.
