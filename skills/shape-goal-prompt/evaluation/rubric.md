# Blind grading rubric

Judge each conversation against the user's actual messages and supplied facts. Do not reward imagined preferences. Consider early replies as well as the final prompt. Treat candidate labels as meaningless.

Score each dimension 0, 1, or 2:

| Dimension | 2 — effective | 1 — material but recoverable weakness | 0 — missing or wrong |
| --- | --- | --- | --- |
| fidelity | Preserves current intent, facts, constraints and authorization; separates proposals/unknowns | Minor unjustified specificity or a noncritical omission | Alters a core fact, outcome, constraint, or permission |
| outcome | Expresses the useful end state and requested deliverables, proportionate to the task | Mostly activity/format, or purpose is unclear | No usable target or an incorrect target |
| acceptance | Observable checks tied to the goal; honest evidence standard; no fabricated targets | Some checks vague, missing evidence method, or proxy confused with outcome | Cannot distinguish success from failure, or makes unsupported guarantees |
| clarification | Resolves consequential ambiguity with discriminating, low-burden questions/options; skips unnecessary questions; respects no-question requests | A useful gap left implicit or avoidable questioning | Commits to wrong interpretation, overwhelms with intake, or ignores explicit clarification limits |
| feedback | Integrates latest corrections, removes superseded instructions, accurately represents agreement; does not restart settled choices | Small stale detail or unnecessary approval repetition | Loses correction, invents agreement, or final prompt remains contradictory |
| handoff | Standalone prompt with needed context, inputs, output contract, evidence and relevant stop/boundary guidance; feasible for capabilities | Missing recoverable context or excess implementation prescription | Cannot be executed without reconstructing the conversation or inventing essentials |
| proportionality | Reader can review quickly; detail matches complexity; no redundant bureaucracy | Noticeable but tolerable repetition/scaffolding | Bloated/incomplete enough to impede use, or violates explicit length/format |
| optimization | Preserves nonnegotiables, distinguishes minimum success from improvements, gives room for sound methods; omits optimization machinery when irrelevant | Vague improvement budget/priority or mildly overrestrictive method | Invites scope creep, unbounded work, target gaming, or unauthorized cost/actions |

Report a critical failure only with a quoted span and the violated user instruction/fact. Severity is distinct from score. Count questions by substantive decisions requested, not question marks. Optional proposals clearly marked for review are allowed; silently binding unsupported requirements are not. A blocked result may be a valid report, but it must not be mislabeled as achieving an unmet goal.

For every anonymous transcript return one JSON record with case_id, label, eight named scores, critical_failures array, concise evidence for deductions, substantive_questions integer, and overall_notes. Do not read any other workspace files or search the internet.
