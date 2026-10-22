---
name: shape-goal-prompt
description: Turn rough requests or voice transcripts into a reusable, goal-driven prompt for a long-horizon agent through selective clarification, feedback, and observable success criteria.
---

# Shape a goal prompt

Produce a self-contained prompt that preserves the user's intent and gives an executor enough direction to pursue it. Refine the prompt with the user; do not perform the underlying task. Keep the structure repeatable while adapting its depth to the request.

## 1. Recover the current intent

Read the request, relevant supplied material, and the conversation before asking questions. Keep a compact working record of:

| Element | Capture when material |
|---|---|
| Purpose and outcomes | What should exist or change, for whom, and why |
| Deliverables | Artifacts, format, destination, audience, and required coverage |
| Boundaries | Scope, exclusions, required methods, permissions, time, cost, and other limits |
| Preferences | Priorities, tradeoffs, examples, and qualities to optimize |
| Context | Inputs, current state, authoritative sources, and dependencies |
| Uncertainty | Missing decisions, conflicts, proposed assumptions, and factual gaps |

Distinguish user-supplied requirements from assistant proposals and unresolved questions. Do not turn an inference into a fact by repeating it. Keep this record in context; show only what helps the user review the meaning.

For transcripts, remove fillers without deleting qualifications. Preserve speaker attribution, corrections, uncertainty in names or numbers, and whether an idea was suggested, rejected, quoted, or adopted. Do not treat every utterance as an instruction or infer consensus among speakers. Ask about an uncertain transcription only if it changes the work.

Apply later corrections to the affected items and remove superseded assumptions. Preserve unrelated settled requirements. Treat status questions and added constraints as steering; replace the objective only when the user actually changes or cancels it.

## 2. Clarify decisions that matter

If the request is already sufficient, draft directly. Do not manufacture interpretations or run an intake questionnaire.

When plausible readings imply materially different work, offer concrete interpretations: describe the result each would produce and the consequential difference. Invite the user to choose, combine, or correct them. Do not present wording variations as distinct options or make an arbitrary option count a goal.

Before asking a question, identify the decision its answer would change. Prioritize consequences for the outcome, scope, correctness, acceptance, authority, resources, or an expensive commitment. Ask the smallest useful batch; ask dependent questions after their prerequisite is resolved. Reuse answers already present.

Separate uncertainty about intent from missing factual knowledge. Consult supplied context when possible. Put ordinary task research into the executor's work rather than asking the user to do it or executing that research here. Ask about the user's intended use, preferences, private context, and decisions that only they can supply.

Offer a reasonable proposed default when it reduces effort, labeling it as a proposal. If the user is unsure or declines further questions, prepare a bounded draft with visible assumptions or delegated choices. Do not turn a refusal, off-topic reply, or silence into confirmation. If a premise or success condition is impossible, conflicting, or undefined, explain the concrete problem and offer workable revisions; agreement cannot make it valid.

## 3. Define success and useful freedom

Express one or more observable outcomes and connect each to suitable acceptance evidence. For each material criterion, identify **what must be true** and **how it can be checked**. Inspection, a demonstration, source traceability, an example, or a user-review rubric can be more appropriate than a metric.

Keep the deliverable the executor can verify distinct from an external effect it can only influence. If a numeric target matters, preserve its definition, baseline, measurement source, and time window where relevant. Leave unknowns explicit. Do not invent numbers, baselines, stakeholder agreement, or guaranteed improvements to make a goal look precise.

Separate mandatory constraints from preferences and suggested approaches. Preserve explicit tools, methods, exclusions, and process requirements even when an outcome-oriented formulation would otherwise leave methods open. Carry supplied permissions accurately; neither this skill nor the resulting prompt grants tools, access, persistence, or authority the executor lacks.

Allow the executor to choose and improve methods within the accepted scope and constraints. Make the priority among competing outcomes or preferences clear when it matters. Treat an enhancement that expands scope or relaxes a resource limit, permission boundary, or mandatory method as a proposal; do not silently adopt that change. Give open-ended optimization a practical stopping condition tied to acceptance and available resources; do not promise perfection or a global optimum.

## 4. Align through focused revision

Show a concise interpretation or draft as soon as it makes correction easier. Ask about unresolved consequential choices, then incorporate the answer into the current version. When useful, state the material change in one sentence; do not require the user to reread an unchanged specification.

Track agreement at the scope actually supported. A choice between interpretations, a correction, or a relevant answer can settle that decision without a separate approval ceremony. A narrow “yes” does not confirm unrelated assumptions. Explicit delegation settles who may choose; it does not establish the user's endorsement of the assistant's eventual choice.

Continue refining while an unsettled decision prevents a faithful, useful prompt and the user is participating. Stop asking when material decisions are supplied, settled, or delegated. Do not demand a final ritual confirmation. If the user requests a draft despite remaining uncertainty, deliver it with the consequential assumptions or open decisions visible and describe it accurately as provisional. Never claim agreement merely because no objection arrived.

## 5. Compile and check the handoff

Use the template below as an adaptive scaffold. Omit irrelevant sections, replace placeholders, and include sufficient context for a fresh executor. Do not rely on “as discussed,” hidden conversation history, or unprovided attachments. Preserve useful input references and state how missing inputs affect the work.

For long or interruptible work, add only the planning, progress records, checkpoints, and verification the task and actual environment warrant. If supported, specify a compact resumable record of the goal, latest constraints, decisions, artifact locations, completed work, evidence, remaining work, and next action. Do not promise durable memory or repeated sessions. Use checkpoints at meaningful decisions or integration boundaries, not fixed rituals.

```markdown
# Objective and outcomes
[What should exist or change; intended beneficiary/use; one or more outcomes.]

# Context and inputs
[Relevant current state and supplied material; source-of-truth references.]
[Material assumptions, unresolved facts, and delegated choices, labeled accurately.]

# Requirements and priorities
[Required scope, methods, exclusions, and resource limits.]
[Preferences and how to resolve consequential tradeoffs.]
[Available capabilities and authorization boundaries when relevant.]

# Acceptance and evidence
[For each material outcome: required observable condition and suitable check.]
[Distinguish verified deliverables from external effects requiring later measurement.]

# Working guidance
[Choose methods within the stated boundaries; preserve required procedures.]
[Resolve factual gaps using available sources; seek clarification for consequential
 unresolved intent or authority. Revise the approach when evidence warrants it.]
[For substantial work only: useful planning, continuity, and checkpoints supported
 by the environment. State a practical completion condition and genuine blockers.]

# Delivery
[Artifacts, format, destination, and detail level.]
[Report completion evidence, consequential decisions, and remaining limitations
 proportionately; distinguish completed work from proposals or unverified claims.]
```

Before delivering, check both fidelity and usefulness: does every material user requirement survive; have corrections displaced obsolete interpretations; are assumptions and open choices honest; can the acceptance conditions be checked; would the requested result serve the stated purpose? Remove unnecessary subgoals and unsupported capabilities. Ensure suggested improvements have not become mandatory requirements.

Return the copyable execution prompt, with a brief note about material unresolved assumptions if needed. If a consequential decision is still being elicited, present the useful draft and the focused question instead of declaring consensus. The prompt is the deliverable; do not claim its future task is complete or validated.

## Optional references

- Read [examples.md](references/examples.md) when concrete examples would help with ambiguous requests, feedback, transcripts, or acceptance criteria.
- Read [evidence.md](references/evidence.md) when explaining or adapting the workflow's research basis and limits. These sources inform the design; they do not validate this exact skill or promise improved execution.
