# Shape Goal Prompt

Use this skill to turn a rough request, notes, or a transcript into a standalone assignment for an agent. It helps clarify consequential choices, preserve corrections, define observable outcomes, and bound useful optimization.

## Start

Load the `shape-goal-prompt` folder from the inner `shape-goal-prompt.zip` using your agent's supported skill-loading mechanism. Then invoke it with your request:

> Use $shape-goal-prompt to turn this into a reusable execution prompt: [your rough request].

You can answer its questions, choose or combine interpretations, correct the draft, or delegate a choice. If you want a provisional result without questions, say so. The skill should preserve consequential unknowns rather than fabricate agreement.

## Expected result

A copyable prompt containing the relevant parts of this repeatable structure:

1. Objective and outcomes
2. Context and inputs
3. Requirements and priorities
4. Acceptance and evidence
5. Working guidance
6. Delivery

Small requests can merge sections. Long tasks can add supported progress records and meaningful checkpoints. The skill does not create tools, persistent memory, permissions, or an execution environment.

## Package contents

- `shape-goal-prompt.zip`: runtime skill, examples, source notes, and interface metadata.
- `research-summary.md`: research synthesis and design limits.
- `evaluation/REPORT.md`: actual results, revisions, and limitations.
- `evaluation/`: raw prompt replies, anonymized grader inputs, both graders' judgments, original and revised candidates, frozen cases, dispatch records, downstream artifacts, and verification scripts.

After extracting the outer bundle, run `python3 evaluation/verify.py` to check package identity, frozen fixtures, transcript assembly, score totals, and downstream artifact checks. This reproduces checks on saved evidence; it does not rerun model generation or prove future performance.
