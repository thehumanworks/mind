# Evaluate validated outcomes and total cost

## Register the experiment

Define workflow, in-scope units, security outcome types, adjudication rules, quality floor, minimum worthwhile improvement, critical regressions, budget, and stopping rule before running. Define an accepted outcome narrowly enough that one intervention cannot inflate it by splitting findings or counting tool calls. Keep supported dismissals, vulnerabilities, detections, and fixes as separate classes even when a portfolio metric combines them with declared weights.

Compare the existing human/tool process and a simple agent baseline. Add one intervention at a time: threat context, deterministic tools, runtime validation, state machine, durable evidence, independent validator, retrieval, then workers. Where refusals are a bottleneck and access allows it, compare the same explicit model with standard versus approved cyber access. Hold all other variables fixed; record unavoidable differences.

Use paired tasks and randomise run order. Include positive cases, negative cases, ambiguous/unbuildable cases, malicious instructions in retrieved content, malformed output, stale context, and recovery after partial mutation. Mix withheld historical internal tasks, recent prospective tasks, and seeded cases. Keep public benchmark results separate from local production evidence. Hide final conclusions and patches from the agent; prevent leakage through history, caches, worker messages, or retrieval.

Use independent/blinded adjudication when feasible. Specify adjudicator disagreements and how they are resolved. Freeze task exclusions prospectively. Include all initiated runs and costs; a failed environment setup is an outcome of the system under evaluation, not an excuse to drop the task.

## Report metrics with denominators

| Metric | Denominator and interpretation |
|---|---|
| Useful-finding precision | Accepted actionable findings / all findings presented for review, including unresolved cases; also show accepted/rejected/inconclusive counts |
| Ground-truth recall | Validated known issues found / all known in-scope issues, only where the ground-truth denominator is defensible |
| Novel yield | Unique accepted issues new to the organisation / predefined scoped units; deduplicate against existing backlog and across workers/repeats |
| Fix correctness | Fixes closing the security condition and preserving required behaviour / all proposed fixes reviewed |
| Review burden | Reviewer minutes on rejected and inconclusive findings / tasks, and / accepted findings; retain total review minutes too |
| Human attention | Reviewer + operator + unscheduled rescue minutes / task and / accepted outcome |
| Total cost | Model + tool + compute + allocated integration/maintenance + human cost, in one declared currency and costing period |
| Run success and rescue | Terminal success without unscheduled rescue / all initiated runs; rescued runs / all initiated runs |
| Time | Intake-to-supported-disposition and acceptance-to-verified-resolution; report median/tail and separate censored/incomplete tasks |
| Repeatability | Equivalent material disposition/evidence across repeated tasks; do not score prose similarity |
| Adverse effects | Policy violations, unauthorised actions, regressions, exposure, or incidents / runs and, where useful, actions |
| Coverage | Actually examined applicable units / predefined applicable scope; state unexamined surfaces and telemetry gaps |

Report a ratio with a zero denominator as `null`/unavailable and show its counts. Do not substitute zero or infinity. Unknown ground truth is not zero ground truth. No findings does not establish full recall or absence of vulnerabilities. Averages of per-run ratios can mislead; distinguish pooled rates from task-weighted rates.

Use both comparisons: **fixed budget**, measuring validated yield at equal total resources; and **fixed quality**, measuring resources needed to satisfy the agreed quality floor. A faster agent may consume more total compute, while a costly validator may save scarce reviewer time. Disclose both effects.

## Interpret uncertainty

Choose sample size using baseline rates and the minimum worthwhile change; there is no universal sufficient count. Use paired differences and uncertainty intervals. Bootstrap at the task/organisation cluster level when repetitions are correlated, not at individual finding level as if independent. Declare censoring and timeout treatment. For repeated models on one task, report within-task variability separately from variation across tasks.

Do not infer causality from an unpaired aggregate with changing models, datasets, or budgets. Do not infer rare-event safety from observing zero violations in a small sample. Retain adversarial denial tests and deterministic controls as separate evidence. Vendor metrics and the supplied report's research figures motivate hypotheses; they are not results of this skill.

Adopt when the pre-registered condition is met: accepted-outcome quality and adverse-event performance remain acceptable and a material yield, time, cost, or attention improvement justifies other trade-offs. Reject or revise when gains disappear after including failed runs, review, repeated/duplicate findings, or integration costs.

## Bundled arithmetic helper

Use `tools/summarize_scorecard.py` with `assets/scorecard.csv`. Record one row for every initiated run, including failed/cancelled runs, with final observation time. Use the same `task_id` across arms; use a unique `run_id` per execution. Costs must use one currency. `accepted_outcomes` follows the declared experiment definition; it may include justified dismissals, so it need not equal `accepted_findings`. Counts must reflect adjudication, not model confidence.

All monetary/time fields are required, including explicitly justified zero allocations. `ground_truth_total` and `ground_truth_validated` may both be blank when unknown. `run_status` is `complete`, `inconclusive`, `failed`, or `cancelled`; `rescued` is `0` or `1`. Finding dispositions must sum to findings presented. The helper returns per-arm totals, pooled rates, and observed-run duration median/p95. These duration statistics include failed/cancelled run durations and therefore are **not** time-to-validated-result estimates. It refuses empty datasets, invalid numbers, impossible counts, or duplicate run IDs.

The helper does not check task pairing, deduplicate findings, estimate recall for incomplete ground truth, calculate confidence intervals, or test statistical significance. Inspect the task table and apply the experiment plan before concluding an improvement.
