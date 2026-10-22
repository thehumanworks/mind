---
name: shape-goal-prompt
description: Turn rough requests or transcripts into goal-driven agent prompts. Use when asked to clarify intent, agree scope, or refine a reusable execution prompt.
---

# Shape a goal-driven prompt

Turn the user's request into a clear, reusable assignment: the outcome, its limits, and the evidence that would show it succeeded. Produce the prompt; execute the underlying task only when separately requested.

## Core rules

- Preserve the user's purpose, facts, constraints and corrections. Keep confirmed requirements distinct from assumptions, proposed improvements and unresolved choices.
- Define **what should be true when finished**, not just activities. Make success observable without inventing numbers, baselines, deadlines or guarantees.
- Ask only when the answer could materially change the work. Offer distinct interpretations when they are easier to choose than an open question.
- Give a concrete draft as soon as it is useful. Let the user correct it; do not turn clarification into an intake form.
- Give the executor room to choose methods inside the agreed limits. Better results must still serve the same goal.

## 1. Understand and clarify

Read the whole request and relevant prior feedback. Extract the intended use, outcomes, deliverables, sources, constraints and unknowns. From transcripts, retain self-corrections, speaker distinctions and uncertainty; tentative or quoted remarks are not automatically decisions. Do not claim to have heard audio when only text is available.

Use this decision rule:

| Situation | Response |
| --- | --- |
| Meaning and success are clear | Draft directly; skip questions whose answers would not change the result. |
| Plausible readings imply different outcomes | Show the consequential alternatives and ask which fits; recommend one only with a stated basis. |
| Missing preference, constraint or authority changes the result | Ask a focused question, explaining the choice it resolves. |
| Missing fact can be established from available sources | Use authorized context when practical, or make inspection an executor dependency; do not ask the user to guess. |
| User cannot answer or declines questions | Produce the useful provisional prompt, label consequential unknowns, and give a safe route for resolving them. |

Challenge a conflicting, infeasible or unsupported premise in plain language, then propose a useful achievable version. Do not silently replace the user's objective. If the core purpose is unclear, resolve that before elaborating its implementation.

## 2. Define success and useful optimization

For each goal, connect **desired result → acceptance condition → evidence**. Use a test, comparison, inspection, source check or human review that fits the task. Include the relevant data, baseline and measurement conditions for numerical claims; leave unknown values unresolved or assign measurement as an initial task.

Keep these separate:

- **Required result:** the deliverable and mandatory conditions.
- **Desired impact:** a real-world effect the artifact may influence but cannot guarantee.
- **Optional improvement:** something that advances the goal within authorized time, cost and scope.

For subjective quality, seek examples or observable review criteria. Do not manufacture a quality score. Mark new acceptance criteria as proposals until adopted. Define how to compare worthwhile improvements and when to stop; never lower the target, discard inconvenient evidence or relax a constraint to claim success.

## 3. Write the execution prompt

Use the same field order for repeatability; merge sections or omit irrelevant ones for small tasks. Respect a user-supplied format or length. Read [the template and examples](references/template-and-examples.md) when a fuller pattern helps.

1. **Goal:** intended outcome and why it matters; include the audience or beneficiary when relevant.
2. **Context and inputs:** authoritative material, starting state, dependencies and consequential assumptions.
3. **Deliverables:** what must exist, with required format, destination and coverage.
4. **Acceptance:** goal-linked conditions and the evidence used to check them.
5. **Constraints and latitude:** mandatory limits, real exclusions, preferences, allowed decisions and actual permissions.
6. **Work and finish:** proportional execution/verification guidance, optimization bounds, when to ask, and completion versus a blocked report.

Write a standalone prompt addressed to the executor. Include needed context or exact accessible references; avoid “as discussed.” Identify unavailable inputs without pretending they have been inspected. Distinguish source material from governing instructions. Do not invent tools, access, persistent memory or authority.

For long or interruptible work, add only what is useful and supported: a revisable plan, checks at meaningful milestones, and a compact progress record with current goals, decisions, artifacts, evidence, blockers and next action. Let evidence guide method changes. Request concise decisions and evidence, not private chain-of-thought. Do not prescribe fixed sprints, compulsory subagents or repeated tests for trivial work.

## 4. Refine and agree

Lead with the intended outcome or the decision that needs the user's attention. Show only consequential assumptions and questions alongside the draft.

On feedback, update the affected goals, criteria and constraints together. Remove superseded instructions and retain unrelated settled choices. Briefly name material changes when useful. A status question is not a new goal.

Use **Draft** while consequential choices remain; **Ready for review** when a coherent prompt awaits the user's judgment; **Agreed** only when the user has actually accepted the relevant scope. An answer to one question is not blanket approval. Respect an instruction to finalize or proceed with delegated judgment without asking again; disclose remaining assumptions rather than inventing agreement.

Deliver one clean current prompt after agreement. Keep optional improvements visibly separate from commitments. Agreement on wording does not itself authorize executing the task.

## Final check

- Does the prompt preserve the latest intent, important constraints and accepted corrections?
- Can the executor distinguish success, incomplete evidence and a real blocker?
- Are requirements grounded, assumptions visible and optional improvements bounded?
- Can a new agent use it without reconstructing the conversation?
- Did each question and instruction earn its place?

## Sources

This workflow is a practical synthesis, not a universally validated prompt formula. Read [source notes](references/sources.md) for support and limitations.

- [NASA: stakeholder expectations](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/) and [good requirements](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/).
- [Horvitz: mixed-initiative interfaces](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/) and [Clark/Brennan: grounding](https://web.stanford.edu/~clark/1990s/Clark%2C%20H.H.%20_%20Brennan%2C%20S.E.%20_Grounding%20in%20communication_%201991.pdf).
- [IN3: intention understanding](https://aclanthology.org/2024.acl-long.61/) and [multi-turn instruction failures](https://arxiv.org/html/2505.06120v1).
- [OpenAI: reasoning prompts](https://developers.openai.com/api/docs/guides/reasoning-best-practices), [goal contracts](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) and [proportional skills](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).
- [Anthropic: context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) and [long-running harnesses](https://www.anthropic.com/research/harness-design-long-running-apps).
