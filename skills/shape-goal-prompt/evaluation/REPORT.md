# Shape Goal Prompt — evaluation report

**Release conclusion:** the revised skill produced faithful, usable prompts in the tested complete conversations, with no critical failures flagged by either grader. It improved the targeted early-clarification comparison with its parent, but **did not outperform the no-skill control on the held-out rubric**. Repetition in final prompts remains the main observed weakness.

The runtime is a ready-to-use instruction package, not a proven guarantee of better task execution. Its 1,147-word core is accompanied by optional examples, source notes, and interface metadata. No revision was made after held-out generation began.

## Results at a glance

Each rubric rating contains eight dimensions scored 0–2. The totals below combine two independent, fresh-context model graders. Higher is better. The maxima differ because the targeted comparison has three cases, while development and held-out each have six.

| Stage | Condition | Score | Critical failures flagged |
| --- | --- | ---: | ---: |
| Development | Compact candidate (q) | 188 / 192 | 0 |
| Development | Structured candidate (r) | 190 / 192 | 0 |
| Development | No-skill control (s) | 191 / 192 | 0 |
| Targeted first-turn comparison | Selected parent (w) | 84 / 96 | 0 |
| Targeted first-turn comparison | Revised skill (v) | 88 / 96 | 0 |
| Held-out complete conversations | Revised skill (t) | 187 / 192 | 0 |
| Held-out complete conversations | No-skill control (u) | 192 / 192 | 0 |

All four downstream executions passed their saved artifact checks: two tasks with skill-produced prompts and the same two tasks with control-produced prompts. These small checks do not establish an advantage for either condition.

## What was tested

There were **66 prompt-authoring replies**, **72 whole-transcript grader ratings**, and **four downstream execution artifacts**. Fourteen distinct scenario designs were used: six development, six held-out, and two transfer tasks. The three targeted regressions reuse development first turns and are not additional unseen scenarios.

| Stage | Conditions | Conversation instances | Prompt-authoring replies | Grader ratings |
| --- | ---: | ---: | ---: | ---: |
| Development | 3 | 18 | 36 | 36 |
| Held-out | 2 | 12 | 20 | 24 |
| Targeted first turns | 2 | 6 | 6 | 12 |
| Transfer prompt authoring | 2 | 4 | 4 | 0 |

The six development scenarios cover ambiguous onboarding, a prompt-only word limit, performance targets and output preservation, uncertain dictation, a row-preserving audit with embedded instructions, and unsupported causal claims. Follow-ups correct scope and distinguish aspirations from acceptance requirements.

The held-out scenarios cover volunteer-retention diagnosis and a proposed pilot, a long code migration with preserved behavior and strict checks, ambiguous dictated proposal details, a corrected image-comparison objective requiring user judgment, an exactly two-sentence translation prompt, and read-only ticket triage with source instructions treated as data.

The comparison measures fidelity, outcome clarity, acceptance evidence, clarification, feedback and agreement, handoff usability, proportionality, and bounded optimization. It does not award points merely for headings, elaborate procedures, more questions, or length. Critical failures are reported separately from ordinary deductions.

## Candidate selection and iteration

The frozen selection order was: fewest critical failures, then higher rubric score, then lower user burden and smaller runtime instructions if tied. The structured candidate was selected over the compact candidate, 190 to 188. The no-skill control was a comparison, not an installable candidate; its better development score is retained in the report.

The revision addressed actual development findings and the independent source audit:

- It directs the agent to resolve consequential intent before presenting an elaborate speculative prompt.
- It asks for each requirement to be stated once, with acceptance checks adding evidence rather than repeating the specification.
- It requires a proposed verification reference to establish the same original baseline. This addresses a development reply that could have substituted an expected-output fixture without proving equivalence to the original generator's bytes.
- It repairs the transcript teaching example's omitted audience and timing.
- It retains scoped agreement, explicit delegation, honest unknowns, user-imposed methods, and conditional continuity for long work.

The revision was frozen in local commit `e8e9301` before validation generation. Original candidates, all raw outputs, and hashes are retained. `selection-and-revision.md` records the decision in more detail. No unfavorable run was discarded or rerolled.

## What improved, and what did not

### Early clarification became more focused

In the fresh three-case comparison, the revised replies totalled **310 words**, compared with **1,579** for the selected parent: 89, 112, and 109 words versus 485, 542, and 552. The revision scored 88/96 against the parent's 84/96.

Both graders favored the revision's consequential clarification and proportionality. The parent tended to provide a full provisional execution workflow before resolving the main choice. One grader also flagged a premature assumption that successful onboarding ended at signup.

There is a real tradeoff: the concise replies leave the final handoff pending. Both graders deducted handoff points for that, and acceptance points where the success definition was still being elicited. The same eight-dimension rubric was retained; those deductions were not removed to favor the revision. This comparison evaluates first turns, so its aggregate is not directly comparable with the scores for completed dialogues.

### Complete handoffs remained accurate but sometimes repetitive

On held-out conversations, both graders gave the revised skill full marks on fidelity, outcomes, acceptance, clarification, feedback, handoff, and bounded optimization. All five point deductions were in proportionality: repeated requirements across objectives, requirements, acceptance, working guidance, and delivery.

Both graders flagged the final volunteer-retention prompt and the provisional proposal prompt. One also flagged ticket triage. These were usable but longer to review than necessary. The control received full marks on this small set.

Across all ten held-out replies, the revision used **4,081 words**, compared with the control's **3,724**. Shorter openings did not translate into shorter complete conversations. The final volunteer-retention prompt alone used 930 words. Do not describe this release as universally more concise or superior to ordinary prompting.

The user-specified format checks passed: all three development D2 replies stayed under 120 words, and both held-out H5 replies contained exactly two sentences. Saved outputs and the narrowly applicable checks are in `format-checks.json`.

### Downstream handoff checks passed in both conditions

Fresh executors received only the unedited generated prompt and the task's source files, plus an administrative instruction identifying the output path. They did not receive the original user request, expected answer, or rubric.

| Task | Skill prompt | Control prompt | Evidence checked |
| --- | --- | --- | --- |
| Invoice CSV audit | Pass | Pass | Exact header, five rows in order, calculations, duplicate flags, missing payment, valid negative credit |
| Decisions extraction | Pass | Pass | Valid JSON, only adopted actions, corrected due date, null unknowns, retained open questions |

The CSV artifacts exactly match the expected rows. Both JSON artifacts contain the same correct adopted actions and open questions. The root agent also inspected their meaning; this was not human calibration. Source-file hashes remained unchanged. The result checks do not constitute an audit of every possible tool interaction or external side effect.

## Research and source review

The workflow combines requirements engineering, clarification and grounding research, human–AI interaction guidance, and official agent guidance. The runtime source notes map design choices to primary sources and distinguish normative advice, historical systems, trained interaction models, and practitioner experiments. None validates this exact prompt format.

Independent candidate and revision audits found no high or medium source or consistency issues. A low-severity display-description note remains: “agreed, testable agent prompts” describes the intended outcome, while the actual workflow also permits provisional drafts. The core explicitly forbids false agreement. See `source-audit-disposition.md` and `audits/`.

## Method and limitations

1. **Small, synthetic sample.** User follow-ups were scripted, not generated by an adaptive person responding to each question. The tests directly assess incorporation of feedback; they are weaker evidence about which question a real user would find easiest or most valuable.
2. **Same model family.** Generators and graders used fresh threads and inherited the platform's configured default, with no explicit model overrides. Exact model snapshot, sampling parameters, and seeds were not exposed. Model judgments have not been calibrated with a human.
3. **Batching.** Each generator handled labeled independent conversations within one thread. A separate thread per scenario would provide stronger isolation. Graders saw randomized anonymous labels, but recognizable response styles can still reveal differences.
4. **Development staging correction.** Future-turn files were initially copied into run folders during setup. They were removed during first-turn generation; subsequent files were staged only at dispatch. Generators were instructed to read the assigned turn, and no future-turn content was supplied in their messages. There is no evidence of advance reading, but access was instruction-constrained rather than security-isolated, and complete tool traces were not captured.
5. **One extra held-out review.** The revised-skill generator delegated a review of H1, H3, and H4 first-turn clarification to a helper restricted to its assigned inputs and skill. The control did not. The run was retained and disclosed. Both generators then received the same no-further-delegation instruction; later runs prohibited delegation. This extra review is a comparison confound and prevents attributing any advantage solely to the skill.
6. **Held-out means unused for revision.** The response generators had not seen those cases, and the revision was frozen before their generation. The root author created the cases and therefore knew their contents. No change was made in response to held-out deductions.
7. **No statistical or long-horizon claim.** One trial per condition and near-ceiling scores do not establish a reliable performance difference. The execution tasks are small. No multi-hour task, real speech recognition, context-compaction recovery, multi-model portability, or real user satisfaction was tested.

These limitations are why the release is presented as a researched, tested workflow with known tradeoffs, rather than a proven improvement over the underlying agent.

## Reproduce the saved checks

Extract the outer bundle and run:

```bash
python3 evaluation/verify.py
```

The standard-library verifier checks the file manifest, frozen protocol and candidates, exact delivered runtime identity, metadata and local links, transcript anonymization against raw replies, rubric totals, explicit user format limits, unedited transfer prompts and source inputs, and saved downstream outputs. It does not rerun model generation or authenticate the external sources.

Raw replies are under `development/`, `holdout/`, `regression/`, and `transfer/`. Each grader's input, label key, and scores are under `grading/`. Transfer anonymization views were generated for inspection but were not model-graded; transfer outcomes were checked directly. Dispatch records and `generation-runs.json` document the actual conditions and setup corrections.

Automatic installation into the protected Skills directory remains blocked by the earlier automatic approval-review rejection. The installable ZIP is provided without bypassing that restriction; no installation is claimed.
