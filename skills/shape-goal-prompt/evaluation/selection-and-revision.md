# Selection and revision — recorded before validation generation

## Selection under the frozen protocol

| Condition | Rubric total | Critical failures |
| --- | ---: | ---: |
| Structured candidate (r) | 190 / 192 | 0 |
| Compact candidate (q) | 188 / 192 | 0 |
| Direct-instruction control (s) | 191 / 192 | 0 |

Select **structured (r)** as the parent: the candidates tie on critical failures, and r has the higher rubric total. The control is not a candidate for installation. These results do not establish that either skill improves on the control.

Two independent, blinded graders assessed all six complete dialogues in each condition. Judge 1 deducted one proportionality point from r and four from q for repeated requirements. Judge 2 deducted one acceptance point from r: an alternative expected-output reference was not explicitly established as equivalent to the user's original-output baseline. The judges disagreed on these local issues; retain both judgments, not just their sum.

Across 12 replies per condition, q used 5,203 words, r 4,784, and s 3,454. Length alone is not a failure. The observed repetition deductions and the user's context-switching needs justify removing needless restatement rather than imposing a word quota.

## Revision decisions

1. Lead with core rules and use a consequence-based clarification table. Preserve the parent's distinction between user intent and ordinary factual research. When purpose remains unsettled, prefer a compact interpretation and focused question before a speculative full template. This addresses unnecessary scaffolding without requiring a fixed question count.
2. State each requirement once and use acceptance checks to verify it, rather than repeating it across the template. Retain a full standalone final handoff; do not repeat it on every partial correction. This addresses the development proportionality deduction.
3. Add an explicit requirement-to-evidence rule: a replacement reference must establish the same agreed baseline. Add an illustration derived from the observed development case. This addresses the original-output preservation gap, rather than introducing a task-specific benchmark script.
4. Repair the independent source audit's incomplete transcript summary by retaining the leadership audience and “this week” timing without inventing a calendar date.
5. Add the already-researched official reasoning and goal-specification sources to the parent's evidence notes. Preserve the caveat that runtime capability is not created by instructions. These sources were researched before development, not selected to rationalize scores.
6. Keep scope-specific agreement, corrections, bounded improvements, actual permissions, and conditional long-task continuity. Add an explicit prohibition on requesting private chain-of-thought and on claiming to have heard audio when only text was available.

Original candidates remain unchanged. The revised skill and examples will be hash-frozen before validation. A targeted comparison with the parent uses three previously seen first-turn requests to check the effect on early clarification; it is a regression test, not held-out evidence. The six held-out dialogues remain untouched and are not used to revise this version.

## Expected evidence, not an assumed result

Check that the revision preserves fidelity and acceptance while reducing unnecessary first-turn scaffolding. It may tie or lose to the control. Report all runs, grader disagreement, word counts, and downstream handoff results; do not infer multi-hour reliability from prompt-only tests.
