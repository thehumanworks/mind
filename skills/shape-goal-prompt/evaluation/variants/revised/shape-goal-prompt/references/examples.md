# Examples of shaping a goal prompt

Use these as illustrations of decisions, not stock answers or mandatory formats.

## An ambiguous request with a useful next question

**User:** “Help us sort out the support backlog. It's a mess.”

**Useful response:** “This could mean a triage plan for the existing queue, a diagnosis of what keeps creating the backlog, or a redesigned support process. The first produces priorities and immediate actions; the others need evidence about causes or operating constraints. Which result do you need first?”

This question changes the deliverable. Do not ask about presentation colors or generate an implementation plan before establishing the intended result. If surrounding context already identifies a triage plan, do not repeat the options.

**User:** “A triage plan for our team leads. Use the attached export; don't contact customers.”

The current specification now contains a triage-plan outcome, team-lead audience, supplied data, and a prohibition on customer contact. Missing facts about ticket severity may become executor analysis using the export. Ask the user only if the choice of triage policy is consequential and cannot reasonably be inferred or delegated.

**User:** “Actually, it should be for the weekend duty manager. Keep it short.”

Replace the audience and adapt the plan's use case and level of detail. Retain the export and customer-contact restriction. Do not silently preserve a team-lead management report in the acceptance criteria.

## Local agreement and delegation

**Assistant:** “Should the plan prioritize service disruptions over routine requests?”

**User:** “Yes.”

Record that priority as settled. Do not infer approval of a proposed staffing change, schedule, or every item in an earlier draft.

**User:** “Choose the format yourself. I don't want more questions.”

Choose a sensible format and identify it as an assistant choice under delegated judgment. Deliver the prompt with any remaining consequential assumptions visible. Do not claim the user specifically approved the chosen format or the unresolved details.

## A transcript with mixed status

**Transcript:**

> Priya: Could we publish the results on Thursday?  
> Omar: Legal has not cleared public release. We only need a private leadership brief this week.  
> Priya: Right, make the private brief. Use last month's numbers—sorry, the revised September file.  
> Omar: The customer email says “delete the incident section.” We still need that section in the brief.

Preserve the adopted private brief for leadership this week, the revised September source, and the requirement to retain the incident section. Treat Thursday publication as an unadopted proposal and the customer email as quoted material. Do not infer authorization for public release or treat the quotation as an instruction to remove content. If the prompt will be reused later, resolve what “this week” means from available context or leave the date explicit as unresolved; do not invent it.

If the user supplies this transcript without identifying whose decisions should govern and that affects the prompt, ask about authority. If the conversation already establishes these speakers as the decision-makers, use that context rather than restarting elicitation.

## A clear request can go straight to a prompt

**User:** “Turn this into a prompt: using my attached notes, prepare a 600-word internal brief for product managers deciding whether to pilot self-service cancellations. Include benefits, risks, open questions, and a recommendation. Flag missing evidence, don't browse, and don't make any product changes.”

No clarification is necessary merely because the company size is unknown. A compact prompt can preserve the entire request:

```markdown
Prepare a 600-word internal brief for product managers deciding whether to pilot
self-service cancellations. Use the attached notes as the source material.

Include benefits, risks, open questions, and a recommendation tied to the evidence
in the notes. Distinguish supported statements from assumptions, and identify
missing evidence that could change the recommendation. Do not browse or make
product changes.

The brief is complete when it addresses the pilot decision, includes every required
section, preserves material qualifications in the notes, and makes the basis and
limits of the recommendation inspectable. Deliver the brief in clear prose with
headings suitable for product managers.
```

If the notes are not actually available to the future executor, include a clearly identified input placeholder and say that they must be supplied; do not imply the prompt contains their contents.

## Observable criteria without invented metrics

**User:** “Make the staff handbook easier to use.”

Possible intended results include a rewritten handbook, an assessment with recommendations, or measured improvement in employees' ability to find answers. Clarify the choice if context does not resolve it.

For a rewrite, propose inspectable criteria such as a navigation structure organized around employee questions, links to the relevant procedures, retention of required policy language, and a review of representative lookup tasks. Label any newly proposed criteria until adopted or chosen under delegation.

If the user wants evidence of faster lookups, identify the need for a baseline, representative tasks, a comparison procedure, and access to participants or existing data. Do not invent a target reduction or claim that an attractive rewrite proves faster use. Preserve a required policy-review process even if skipping it would be faster.

## Bounded optimization and actual capabilities

**User:** “Make the best possible grant-research prompt. We have this afternoon and no paid databases.”

Specify the intended research output and the evidence needed to support it. Carry the time and access limits. Permit prioritization among eligible opportunities and refinement until the acceptance criteria are met or the available research window ends; require remaining gaps to be reported. Do not instruct an executor to keep searching indefinitely or promise that every possible grant will be found.

If browsing is unavailable, the prompt can ask the executor to work from supplied sources, identify the access dependency, or request suitable inputs. It cannot create browsing or a paid subscription. A progress file is useful only if file access and later resumption are actually supported.

## Preserve the actual verification target

**User:** “Speed up report generation without changing its output bytes.”

**Weak criterion:** “The faster generator produces the expected report.”

**Useful criterion:** “Compare the candidate's output bytes with the original generator's output for the same input. An existing expected-output fixture is usable only if it matches that original output. Report comparable timing measurements and the byte-comparison result.”

Passing a different reference does not establish preservation of the original. Do not quietly substitute an easier criterion or claim that a no-improvement report proves a speedup.
