# Selection addendum before holdout generation

The development comparison reached a ceiling: both graders gave all three conditions 72/72. The prespecified tie-break selected the lean structure (689 words versus 1173). This did not establish a behavioral advantage over the no-added-skill control.

An independent source/self-consistency audit then identified factual drift in the drafts' own before/after examples: the lean version added an unmentioned pending release check; the operational version added an unmentioned migration blocker; both cache examples added mechanism or guarantees absent from their starting text. These are correctness defects in the instruction artifacts even though they did not surface in the six development responses.

Before any holdout generation, the release rule is clarified: do not ship a known fact-changing illustration merely because behavioral scores tie. Preserve the selected lean structure, repair the examples, make the three requested structural frameworks explicit, and keep source mapping separate. Compare the repaired candidate with the predecessor and control on the unchanged holdout set. Accept the repair only if it fixes the source-audit defects without new decision-critical failures. If behavior remains tied, report the improvement as instruction correctness, not proven response-quality improvement.

This is a disclosed amendment to the original instruction to retain a predecessor when a revision does not improve held-out behavior. It resolves a known source-fidelity defect before seeing heldout results; it does not change the behavioral rubric or cases.

Also add four targeted regression requests for rewriting under factual constraints. These are explicitly development-derived regression checks, not a second held-out set. Freeze them before response generation and preserve all results.
