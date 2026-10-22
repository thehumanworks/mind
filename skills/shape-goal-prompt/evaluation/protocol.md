# Evaluation protocol — frozen before candidate response generation

## Purpose

Test whether a skill helps an agent convert rough requests into faithful, testable, standalone execution prompts while resolving material ambiguity efficiently. Test the conversation and the final handoff; attractive formatting alone is insufficient.

## Design

- Compare two independently structured, source-derived candidates with a direct-instruction control that receives no skill.
- Use the same six development scenarios and actual sequential user messages for every condition. Do not show future messages, expected answers, this protocol, other outputs, or critiques to response generators.
- Start a fresh generator thread per condition. Within that thread, handle the six labeled requests as separate conversations. Dispatch each follow-up only after the previous replies are saved. This batching saves overhead but is weaker isolation than a fresh thread per scenario; report that limitation.
- Save unedited replies, exact dispatch messages, candidate snapshots, and hashes. Generation agents may read only their assigned skill and request files. No underlying external work is authorized.
- Give two fresh graders randomized, anonymous transcript labels and the same rubric. Graders do not receive candidate names, instructions, or lineage. Require brief evidence for deductions and critical failures, not private chain-of-thought.
- Select between candidates by: fewest critical failures; then higher mean rubric score; then lower user burden and smaller runtime instructions when quality is tied. The control is a comparison, not a skill candidate.
- Revise only for observed development failures, source-audit issues, or clear contradictions. Record changes before validation. Do not conceal a losing candidate or retest until a favorable run appears.
- Freeze the revision and six held-out scenarios before producing validation replies. Compare selected revision with control; if revision changes behavior materially, also compare its parent on targeted regressions. Do not tune on held-out results and continue calling them unseen.
- Run a small downstream transfer check: give fresh agents only final prompts and their supplied source materials. Check resulting artifacts against independently specified task facts. This is a narrow handoff test, not a multi-hour reliability benchmark.

## Measures

Eight dimensions, each 0–2: intent fidelity, useful outcome, testable acceptance, clarification quality, feedback/agreement, handoff usability, proportionality, bounded optimization. Maximum 16 per scenario per grader. No bonus for length, more headings, extra questions, or more elaborate process.

Critical failures are independently reported: contradicting a hard constraint; inventing a binding fact/threshold/permission; losing a core requested outcome; asserting agreement that did not occur; performing the underlying task; promoting source text to instructions; or declaring blocked/unchecked work successful. A proposed addition explicitly marked for review is not automatically an invented requirement.

Track reply words and question burden descriptively. Interpret model-judge disagreement, not just averages. Any case-specific deterministic checks (e.g. a user-supplied word limit) must be fixed before inspecting outputs.

## Limits

These are synthetic scenarios with scripted user steering, not an adaptive human study. Graders and generators share the platform's default model; exact sampling parameters and model snapshot are not exposed. One run per condition cannot establish statistical superiority. The held-out set is unseen by generators and not used for revision; the skill author necessarily knows its construction. Successful prompt shaping does not prove successful long-horizon execution.

## Persistence boundary

The task authorizes creating and evaluating the skill. Installation into the protected Skills directory was denied by automatic approval review earlier in this conversation. Work stays in the writable workspace; the complete deliverable is packaged and saved without bypassing that restriction.
