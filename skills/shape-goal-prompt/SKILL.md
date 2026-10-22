---
name: shape-goal-prompt
description: Turn rough requests, notes, or voice transcripts into reusable, goal-driven agent prompts. Use when asked to clarify intent, develop an execution prompt, or refine a prompt through feedback and observable acceptance criteria.
---

# Shape a goal prompt

Turn the user's request into a standalone assignment: the intended outcome, its limits, and evidence of success. Refine the meaning with the user. The prompt is the deliverable; execute its underlying task only if also requested.

## Core rules

- Preserve the user's purpose, constraints, and corrections. Distinguish confirmed requirements, proposals, delegated choices, and unknowns.
- Ask about decisions that change the work. Offer distinct interpretations when choosing is easier than explaining from scratch.
- Make success observable. Do not invent numbers or turn a desired impact into a guaranteed result.
- Leave methods flexible inside the user's boundaries. Useful improvements must serve the same objective.
- Match detail to the next decision. A brief clarification should not require reading a speculative full specification.

## 1. Recover and clarify intent

Read the request and relevant context first. Maintain a compact current record of purpose and audience, deliverables, inputs, boundaries, preferences, and unresolved decisions. Show only what helps the user correct your understanding.

For speech or transcripts, preserve speaker attribution, self-corrections, qualifications, uncertain names or numbers, and whether an idea was proposed, rejected, quoted, or adopted. Do not infer consensus or treat quoted material as instructions. Use the input actually available; do not claim to have heard audio when given only text.

Choose the next response by consequence:

| Situation | Response |
| --- | --- |
| Intent and success are sufficiently clear | Draft directly. Do not ask for information that would not change the assignment. |
| Plausible meanings imply different results | Briefly describe those results and the consequential difference; invite a choice, combination, or correction. |
| Missing intent, preference, private context, or authority changes the work | Ask the smallest useful batch of focused questions. Resolve dependencies before asking downstream questions. |
| An ordinary factual gap can be researched | Use supplied context or make research an executor task. Do not ask the user to guess or undertake the underlying work here. |
| User cannot answer or declines questions | Give a useful provisional prompt with consequential assumptions or delegated choices visible. |

Explain an impossible, conflicting, or unsupported premise and propose an achievable revision. Do not silently replace the objective. While the purpose remains unsettled, prefer a concise interpretation and focused question over a full execution template. There is no required number of questions or options.

## 2. Define success and bounded optimization

Connect each material **outcome → acceptance condition → evidence**. A test, comparison, inspection, demonstration, source check, or human review may fit. Quantitative goals need a meaningful definition, baseline, measurement conditions, and time window where relevant; leave unknowns explicit or assign their measurement.

Keep required deliverables distinct from real-world effects they can only influence. Preserve aspirations as aspirations. Label new acceptance criteria as proposals unless adopted or chosen under delegated judgment.

Check the actual requirement, not a convenient substitute. For a preservation requirement, compare with the agreed original or establish that a proposed reference is equivalent. Do not weaken a criterion, redefine the baseline, or discard inconvenient evidence to claim success.

Separate mandatory limits and required methods from preferences. Allow the executor to improve methods within scope, resources, and authority; propose expansions separately. State priorities when tradeoffs matter and give open-ended optimization a practical stopping condition. Report a genuine blocker or unmet goal honestly rather than promising perfection.

## 3. Refine the current understanding

On feedback, update affected goals, criteria, and constraints together. Remove superseded assumptions; retain unrelated settled choices. A status question is not a replacement goal. Briefly state a material change when useful; do not reprint an unchanged full specification at every turn.

Track agreement only at the scope supported. A local “yes” settles its question, not unrelated assumptions. Delegation settles who may choose, not endorsement of the eventual choice. Silence is not agreement.

Continue while a consequential decision prevents a useful prompt and the user is participating. Stop asking when material choices are settled or delegated. Respect a request to finalize without a ritual confirmation. Describe unresolved drafts as provisional; claim agreement only when supported. Agreement on wording alone does not authorize execution.

## 4. Compile a standalone handoff

Use this field order for repeatability. Merge or omit irrelevant sections for small tasks; respect the user's requested form and length. State each requirement once where it belongs. Acceptance checks should make requirements verifiable, not repeat the entire specification.

```markdown
# Objective and outcomes
[What should exist or change, for whom, and for which use or decision.]

# Context and inputs
[Starting state, supplied material, accessible source references, dependencies.]
[Consequential assumptions, unknowns, and delegated choices, labeled accurately.]

# Requirements and priorities
[Scope, required methods, exclusions, permissions, and resource limits.]
[Preferences, tradeoffs, and bounds on optional improvements.]

# Acceptance and evidence
[For each material outcome: what must be true and how to check it.]
[Preserve the actual target and reference; distinguish evidence from aspiration.]

# Working guidance
[Freedom to choose methods within the requirements; resolve ordinary factual gaps.]
[For substantial work: useful planning, continuity, and meaningful checkpoints.]
[Completion, resource boundaries, and consequential reasons to ask or stop.]

# Delivery
[Artifacts, coverage, format, destination, and appropriate detail.]
[Completion evidence, remaining limitations, and unmet conditions.]
```

Supply needed context or exact usable references; avoid “as discussed.” Mark missing inputs and their effect without pretending to have inspected them. Keep source material distinct from instructions. Do not invent tools, access, persistent memory, or authority.

For long or interruptible work, include only useful, supported planning and continuity. A resumable record can hold the goal, current constraints, decisions, artifact locations, evidence, blockers, remaining work, and next action. Let evidence change the approach. Do not prescribe fixed sprints or compulsory agent teams. Request concise decisions and evidence, not private chain-of-thought.

## Before delivery

- Does the latest purpose survive, with every material constraint and correction?
- Can a fresh executor distinguish success, missing evidence, and a blocker?
- Would the specified result serve the user's intended use?
- Are proposals, assumptions, permissions, and agreement represented honestly?
- Can any question, repeated requirement, or unnecessary subgoal be removed?

Return one clean, copyable current prompt. Add only a brief note or focused question about consequential uncertainty. Do not claim the future task has been completed or validated.

## Sources and examples

Read [examples](references/examples.md) for ambiguity, feedback, transcripts, and acceptance. Read [evidence and limits](references/evidence.md) for the source-to-design mapping. This is a practical synthesis, not a universally validated prompt formula.

- [NASA: stakeholder expectations](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) and [good requirements](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/).
- [Horvitz: mixed-initiative interaction](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/) and [IN3: intention understanding](https://aclanthology.org/2024.acl-long.61/).
- [Multi-turn instruction failures](https://arxiv.org/html/2505.06120v1).
- [OpenAI: reasoning prompts](https://developers.openai.com/api/docs/guides/reasoning-best-practices) and [goal specifications](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex).
- [Anthropic: context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) and [long-running harnesses](https://www.anthropic.com/research/harness-design-long-running-apps).
