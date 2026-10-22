# Compact candidate: source and consistency audit

**Date:** 21 October 2026  
**Scope:** All three files in `variants/compact/shape-goal-prompt/`; the four research memos; relevant primary-source passages reopened independently. No other candidate or evaluation material was inspected. This is a source/consistency review, not evidence of execution performance. The candidate was not edited.

## Disposition

No high- or medium-severity source-fidelity or internal-consistency defect found. One low-severity example correction is warranted.

### Low — An example silently narrows dashboard performance to load time

- **Passage:** `references/template-and-examples.md:42` requests “Make our dashboard much faster. Do not change its content.” The “Useful draft” at line 46 specifies “Improve the dashboard's load time.” The question at line 48 asks which flow or page should improve.
- **Why this matters:** A dashboard can be slow during loading, filtering, refresh, or other interactions. Selecting load time changes which work and evidence count as success; selecting a page does not resolve that distinction. “Useful draft” makes the commitment provisional, so this is limited in severity, but the assumption remains unmarked.
- **Evidence:** The candidate's own `SKILL.md:12` requires separating confirmed requirements from assumptions, and lines 26–28 distinguish consequential interpretations. NASA's [requirements guidance](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) supports explicit assumptions and traceability to the need; it does not justify choosing this particular performance target.
- **Proposed correction:** Use “Improve the dashboard's responsiveness while preserving its content,” and ask “Which operation feels slow: initial loading, filtering, refreshing, or something else?” Alternatively, explicitly mark load time as a provisional interpretation. Preserve the repeatable baseline and comparable measurements.

## Source fidelity

The source table correctly describes the workflow as engineering synthesis, including its field order, status labels, and decision rules (`references/sources.md:3`; `SKILL.md:81`). No inspected claim presents the skill as an experimentally validated universal formula.

- **Requirements and goals:** [NASA stakeholder expectations](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/), [requirements](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/), [validation](https://www.nasa.gov/reference/5-4-product-validation/), and [van Lamsweerde](https://webperso.info.ucl.ac.be/~avl/files/RE01.pdf) support the mapped ingredients. The candidate appropriately distinguishes institutional/conceptual guidance from LLM experiments.
- **Clarification and repair:** [Horvitz](https://erichorvitz.com/chi99horvitz.pdf), [Clark/Brennan](https://web.stanford.edu/~clark/1990s/Clark%2C%20H.H.%20_%20Brennan%2C%20S.E.%20_Grounding%20in%20communication_%201991.pdf), [IN3](https://aclanthology.org/2024.acl-long.61.pdf), and [Laban et al.](https://arxiv.org/html/2505.06120v1) support the stated practices. The notes preserve the human-communication analogy, trained-system/simulation limitations, and historical-model limits. Microsoft's Horvitz PDF failed to fetch; the author's copy was inspected successfully.
- **Prompt and long-work guidance:** The [OpenAI reasoning guide](https://developers.openai.com/api/docs/guides/reasoning-best-practices), [Goals guide](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex), [skills article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), [Anthropic context article](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), and [harness experiments](https://www.anthropic.com/research/harness-design-long-running-apps) support the stated ingredients. The candidate correctly avoids transferring runtime features, fixed sprints, compulsory subagents, or capability promises into a generic prompt.

## Consistency and examples: no correction required

- Concise output is expressly permitted: draft directly when clear (line 26), merge or omit sections for small tasks (line 48), and use proportional checks (lines 55 and 59). This is permission in the text, not a measured performance result.
- Arbitrary metrics and invented agreement are expressly barred (lines 13, 36, 44 and 67). Delegated judgment does not require another confirmation (line 67). “After agreement” at line 69 should be read with that explicit exception, not as a compulsory signoff loop.
- Prompt drafting and task execution are explicitly separated (lines 8 and 69); access, tools, persistence, and authority must not be invented (line 57).
- The supplier example's evidence-gap instruction is reasonable evidence hygiene; it does not require independently verified evidence that the source boundary prevents obtaining.
- The small-task example's “to 150 words” becoming “at most 150 words” is an ambiguous colloquial interpretation, not a confirmed material defect. Making the illustrative request itself say “at most 150 words” would remove the ambiguity without adding a clarification step. “Retain the main message” and a concise output format are reasonable operational defaults.
- Baselines, checks, draft status, acceptance fields, and compact progress records are clearly proposed operational methods, not facts or requirements falsely attributed to research.

No source-driven rewrite is needed. Apply the dashboard example correction only to a subsequent revision if the current candidate is frozen.

