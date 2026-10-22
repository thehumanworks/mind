# Execution prompt template and examples

Use the fields that change the work. Bracketed text is a placeholder, never a supplied fact. Remove empty sections in a ready prompt; retain material missing inputs explicitly in a provisional one.

## Reusable template

```markdown
# [Task]

## Goal
[Create or change what, for whom, to support which use or decision.]

## Context and inputs
[Relevant facts and accessible sources. What has not been supplied or verified.]
[Consequential assumptions, clearly labeled.]

## Deliverables
[Required artifacts, coverage and format.]

## Acceptance
| Goal | Condition | Evidence/check |
| --- | --- | --- |
| [Outcome] | [Observable result] | [Test, measurement, inspection or review] |

## Constraints and latitude
[Hard limits and authorized actions. Required methods, if any.]
[Preferences and priority when tradeoffs matter.]
[Permitted improvements and their bounds.]

## Work and finish
[Choose the approach; inspect necessary inputs before committing to implementation.]
[For substantial work: useful checkpoints and supported progress preservation.]
[Check the result against acceptance; repair relevant failures within the limits.]
[Finish with artifacts, evidence, residual uncertainty and unmet conditions.]
[Ask or stop when a specified decision, resource limit or blocker prevents progress.]
```

The following examples are original applications of the cited principles, not quotations or empirical results.

## Missing measurement

**Request:** “Make our dashboard much faster. Do not change its content.”

**Weak:** “Cut load time by 40% and reach 99% user satisfaction.”

**Useful draft:** “Improve the dashboard's load time while preserving its content. Establish a repeatable baseline and identify the main delays. Report comparable before/after measurements and any remaining limitations.”

**Focused clarification:** “Which user flow or page should be faster?” Propose a threshold only if a pass/fail target is needed and there is a defensible basis; label it as proposed.

## Ambiguous purpose

**Request:** “Sort out our knowledge base.”

**Useful response:** “Do you want easier navigation through existing articles, or a review of gaps and outdated guidance? Those lead to different deliverables. I can draft either, or combine them if both are in scope.”

Do not assume the user wants a replacement platform or a rewrite of all content.

## Feedback that changes one decision

**Earlier:** “Compare five suppliers. Favor low cost. Use only their public product pages.”

**Correction:** “Make reliability the priority; cost still matters.”

**Current prompt:** “Compare five suppliers using only their public product pages. Prioritize reliability, with cost as a secondary consideration. Distinguish published reliability claims from independently demonstrated reliability; mark evidence gaps.”

The new priority replaces the earlier one. The count and source boundary remain intact. Do not manufacture independent evidence that the source restriction prevents obtaining.

## Small task

**Request:** “Prompt an agent to shorten this announcement to 150 words for customers. Keep every date unchanged.”

**Prompt:** “Shorten the supplied announcement to at most 150 words for customers. Preserve every date exactly and retain the main message. Return only the revised announcement. Before returning it, check the word count and compare all dates with the source.”

No milestone plan, persistent state, questionnaire or invented style score is needed.
