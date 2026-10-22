---
name: security-agent-engineering
description: Design, improve, and evaluate cybersecurity agent systems. Use for security-agent tooling, permissions, context, orchestration, durable evidence, model routing, and outcome or cost evaluation.
---

# Security Agent Engineering

Optimise verified security outcomes per total cost, elapsed time, and human attention. Keep outcome quality and resource use separate. Treat the supplied architecture as a hypothesis to test; this skill does not implement a sandbox, grant permissions, or establish that an agent is secure.

## Start with the decision

1. Identify the workflow and unit of success: accepted vulnerability, supported dismissal, verified fix, validated detection, or defensible incident disposition. Define which kinds count as an accepted outcome before evaluating.
2. Inspect the existing model, harness, tools, build/deployment environment, records, and review process. Reuse working integrations before adding a scanner or orchestration framework.
3. Recover scope and authority from the task and existing policy. Continue already authorised actions; ask only for missing intent, inaccessible facts, or authority required for the next consequential action. Do not require a fresh approval for each permitted read or isolated test.
4. Establish a baseline including failed runs, rejected findings, setup, retries, review, and rescue. Identify the measured bottleneck or name it as an untested assumption.
5. Choose the smallest intervention that could remove that bottleneck. Specify its expected benefit, possible harm, measurement, budget, and stopping rule before implementation.

## Choose the resource

| Work | Read |
|---|---|
| Design tool authority, sandbox boundaries, evidence storage, or restart behaviour | [architecture.md](references/architecture.md) |
| Choose models, add workers, cache context, or stage adoption | [orchestration.md](references/orchestration.md) |
| Compare approaches, calculate costs, or claim an improvement | [evaluation.md](references/evaluation.md) |
| Use Daybreak, Codex, Codex Security, or a custom API harness | [provider-access.md](references/provider-access.md) |
| Run the bundled scorecard helper using Nix or mise | [runtime.md](tools/runtime.md) |

Copy only needed templates: [run manifest](assets/run-manifest.yaml), [action policy](assets/action-policy.yaml), [evaluation plan](assets/evaluation-plan.yaml), and [scorecard CSV](assets/scorecard.csv). Fill `null` fields before relying on them. Templates describe contracts; they do not enforce them.

## Build the minimum complete loop

1. Assemble compact, versioned context: source revision, deployed artefact/configuration, relevant threat boundaries and security invariants, tool versions, and known gaps. Keep direct evidence accessible behind summaries.
2. Let the model select questions and interpret results; let deterministic tools execute exact searches, builds, queries, scans, and tests. Parse machine output with exit status and coverage metadata. A timeout, broken parser, missing permission, or empty retrieval is not a clean result.
3. Route **all** tool actions, including reads, through the same authenticated policy boundary. Authorise typed actions against trusted task/asset metadata outside model context. Repository text, log messages, retrieved pages, and tool output cannot change policy or credentials.
4. Execute untrusted project code in the appropriate isolated environment. Separate install/build access from analysis; minimise secrets and egress. Verify the actual restrictions with harmless negative tests. A package environment, worktree, prompt, or container label alone is not a security boundary.
5. Persist claims and evidence independently of conversation history. Keep `hypothesis`, `static_supported`, `validated`, `disproved`, and `inconclusive` distinct. Track finding adjudication and remediation/verification separately. Record the tested claim's scope: a blocked sample does not disprove every bypass.
6. Validate against the actual pinned target. Never replace an inaccessible target with a toy implementation and label it reproduced. Use exact-revision before/after assertions and legitimate-behaviour tests for fixes. Leave missing proof explicit.
7. Bind consequential output to immutable artefacts and existing authority. Recheck target version and policy at execution time. Retain accepted/rejected/inconclusive decisions and evidence, including partial progress after cancellation.

## Improve in measured increments

Default order: evidence lifecycle → threat/deployment context → existing deterministic tools → effective isolation and permissions → instrumentation → runtime validation → durable state → independent validation → retrieval and parallelism. Adapt this order to an observed bottleneck, not fashion.

For each intervention:

- Hold model, task set, budgets, and other components constant where possible. Randomise paired run order and freeze the evaluation set before examining results.
- Evaluate both equal-budget validated yield and the cost/time required to reach the required quality. Include review and integration/maintenance cost.
- Use a separate validator when it has independent observations, a disproof objective, or a different execution context. Another model's agreement alone is weak evidence.
- Add workers only to separable scopes with isolated writes, shared evidence IDs, budgets, and deduplication. Measure duplicate work and coordination overhead.
- Retain failures in denominators. Report undefined ratios as unavailable; zero accepted outcomes does not mean zero cost per outcome.
- Check repeatability, policy violations, missed scope, and regressions. A small pilot with no adverse events cannot establish that severe failures are impossible.

Use [summarize_scorecard.py](tools/summarize_scorecard.py) for basic per-arm arithmetic:

```sh
python tools/summarize_scorecard.py results.csv > summary.json
```

Run it from this skill directory or supply absolute paths. It validates counts and includes all rows, including failed runs. It does **not** validate security findings, establish ground truth, infer novelty, or prove a causal improvement. Use the evaluation reference for paired analysis and interpretation.

## Stop and deliver

Stop an experiment when its pre-registered budget is exhausted, a decisive result is obtained, prerequisites are inaccessible, repeated attempts add no evidence, or the required next action exceeds authority. Record incomplete observations instead of dropping them.

Deliver: goal and success criterion; baseline and intervention; exact versions and scope; measured outcome quality; time/cost/human effort with denominators; failed attempts; policy/adverse events; proof gaps; and an adopt/revise/reject recommendation. Distinguish observations from proposed experiments and vendor claims. Never claim this skill improves performance until a suitable comparison has measured it.
