# Communication skill evaluation protocol

Frozen before response generation: 2026-10-21.

## Aim

Compare two source-derived skill variants with a no-added-skill control. Select the better variant, revise only on observed development failures, and test the revision on previously unused cases. Treat this as a small model-based evaluation, not proof of improved human decision speed.

## Design

- Development set: D1–D6; six independent tasks covering a simple answer, partial completion, a choice, a nontechnical explanation, uncertain progress, and a procedure.
- Holdout set: H1–H6; kept out of response-generation prompts until the final candidate is frozen.
- Conditions: no added skill; a lean source-derived skill; an operational source-derived skill. Use fresh subagent threads with no inherited conversation, same inherited model/settings, and no expected answers.
- Give response generators only the assigned skill (if any), the raw requests and facts, and their output destination. Do not show rubric, other outputs, critique, or variant identity beyond its task path. Treat each case independently.
- Shuffle/anonymize conditions for graders. Give graders raw cases, responses and rubric, but no candidate text, version lineage, or preferred winner.
- Preserve exact skill snapshots, prompts, outputs, scores and hashes. Do not silently overwrite an evaluated candidate. A revision gets a new snapshot.

## Rubric

Score each dimension 0 (fails), 1 (partial), or 2 (meets):
1. Answer first: the opening supplies the answer/status/recommendation or immediate task purpose.
2. Decision completeness: preserve facts, limits and uncertainty required for this user's decision.
3. Actionability: the reader can identify the actual next step/decision, with conditions before actions; no invented work or request.
4. Audience fit: explain unfamiliar terms for the stated audience; retain precise detail for experts; follow requested format/depth.
5. Scanability: group related information and use formatting only when it helps retrieval.
6. Economy: remove redundancy, generic framing and irrelevant detail without losing meaning.

A critical failure is a factual distortion or omission that changes the release/decision/safety conclusion, fabricated execution/evidence, violated explicit output constraint, or lost prerequisite that makes the stated procedure unsafe. Record the exact offending passage and missing fact. No numerical sentence/word target is a communication rule; word counts are descriptive only.

## Selection

First minimize critical failures. Then compare rubric totals. Break ties by shorter skill text, then shorter responses if equally complete. Keep the no-added-skill control as a comparison, not a deployable source-grounded skill. Reject changes that add unsupported rules, fixed length quotas, or degrade decision-critical completeness. If a revision does not improve held-out performance, retain the predecessor and report that result.

Use independent grading plus a factual audit of borderline critical failures. Disclose disagreements rather than altering the rubric to favor a version. Report raw counts/totals, not statistically significant claims. Holdout observations must not be used to tune a candidate subsequently labeled held-out; any later change requires new cases.

