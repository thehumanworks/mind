# Structured variant: source and consistency audit

## Result

**No high or medium issue found.** One low-severity example-completeness note is recorded below. This is a document/source audit, not a behavioral grade or evidence that the skill improves downstream execution.

## Scope and method

Read only `variants/structured/shape-goal-prompt/SKILL.md`, its two reference files, and the supplied research notes `requirements.md`, `long-horizon.md`, `clarification.md`, and `openai.md`. Compared source summaries, instructions, and examples for fidelity and internal consistency. No evaluation files, other variants, or package were inspected. No skill files were edited. No primary-source revisit was needed because no specific source claim conflicted with or materially exceeded the supplied research notes.

## Finding

**Low — the transcript example's preservation summary omits two explicit details.**

- Evidence: `references/examples.md:38` specifies a **leadership** brief **this week**. The preservation instruction at line 42 enumerates the private-brief objective, revised September source, and incident section, without explicitly retaining the audience or timing.
- Consistency basis: `SKILL.md:17–18,25,95` calls for preserving material audience, time limits, and transcript qualifications; `research/requirements.md:15–16,84` supports capturing these bounds and intended use.
- Impact: This is an incomplete teaching summary, not a demonstrated fact-changing final prompt. Nothing explicitly deletes the audience or deadline, so it does not rise to medium severity.
- Suggested adjustment: Include “for leadership this week” in the preservation sentence, leaving Thursday public publication unadopted. If reused outside the original conversation, preserve or resolve the calendar meaning of “this week” rather than inventing a date.

## Checks with no material issue

| Area | Evidence and conclusion |
|---|---|
| Research representation | `references/evidence.md:3,7–28,32` labels the workflow an engineering synthesis, distinguishes motivation from tested effects, and retains source limitations. Its summaries agree with the corresponding supplied research notes. No research-backed success guarantee or inflated independent-source count appears. |
| Invented rules or metrics | `SKILL.md:31–45,61,63` rejects arbitrary option counts, unnecessary intake, invented numbers, mandatory headings, and fixed checkpoint rituals. The adaptive workflow is a permissible operational synthesis, consistent with `research/requirements.md:82–98` and `research/long-horizon.md:93–120`. |
| Agreement and permission | `SKILL.md:39,47,55–57` distinguishes assumptions, local assent, delegation, and authority; it rejects silence as confirmation and final approval ceremonies. The local-agreement example at `references/examples.md:23–31` follows those rules. |
| Capabilities and completion | `SKILL.md:8,37,47,63,97` keeps the deliverable upstream, assigns ordinary task research to the executor, and avoids granting access or persistence. `references/examples.md:67,85` handles absent inputs and capabilities explicitly. This matches the limitations in `research/long-horizon.md:7,57,120` and `research/openai.md:8–10`. |
| Example fidelity | The backlog example retains the supplied export and customer-contact prohibition after the audience correction (`references/examples.md:13–19`). The clear-request prompt retains its word count, audience, source, required coverage, and prohibitions (`48–67`). The handbook and grant examples label proposed criteria or respect stated limits without fabricated performance targets (`71–85`). |

No finding requires a change before behavioral evaluation on source-fidelity grounds. The low-severity edit would improve the teaching example's completeness.
