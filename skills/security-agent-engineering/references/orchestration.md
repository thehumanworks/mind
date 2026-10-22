# Context, routing, orchestration, and adoption

## Spend context on decisions

Discover repository structure, lockfiles, build instructions, routes, IaC, and available telemetry before asking the user. Ask about intended security/business behaviour, authority, and unavailable facts that could change a material decision. Reuse task-level answers; do not repeat permission requests already settled by the task.

Construct a small fact set with source URI/ID, revision or time range, retrieval time, scope, and invalidation condition. Mark inferred facts and contradictions. Prefer current deployment/IAM records over a repository comment about exposure. Resolve contradiction rather than averaging confidence. Keep sensitive source records out of prompts when a minimised structured observation suffices.

Start with manifests and service/entry-point boundaries, then narrow text/AST/dataflow queries. Introduce indexing when repeated traversal costs justify its maintenance. Cache source facts and deterministic analysis by all relevant inputs: commit plus dirty diff, tool/rule version, extraction settings, build flags, lockfile/SBOM, generated inputs, and configuration. Include image/config/deploy identifiers for runtime conclusions and telemetry source/time-window for incident conclusions. Invalidate on relevant change; treat cached model conclusions as leads to recheck.

## Route work by evidence needs

Use deterministic transformations for parsing, joins, deduplication, metrics, and queries with known semantics. Try a lower-cost capable model on bounded extraction/classification; use stronger reasoning when cross-component uncertainty dominates. Measure the resulting error/review cost. Record actual model ID, settings, access tier and surface, tool capabilities, and harness revision. Provider access changes can alter willingness without improving correctness; evaluate both separately.

Separate a validator when it receives exact evidence/revisions and tries to refute the claim, recreates execution independently, or applies a distinct oracle. A second opinion sharing all upstream assumptions is correlated evidence. Preserve uncertainty when validators disagree; choose a discriminating observation rather than a majority vote.

## Parallelise only separable work

Partition by independent services, hypotheses, binaries, or telemetry windows. Give each worker its scope, inputs, deadline, budget, expected output schema, evidence location, and authority. Use separate worktrees/workspaces for mutations. Retain one owner for final adjudication and patch integration. Cap combined model/compute spend and rate-limited service calls; worker count alone is not a budget.

Deduplicate candidates by root cause, affected boundary, revisions, and prerequisites, preserving distinct consequences and variant evidence. Share validated observations, not instructions copied out of untrusted content. Stop a worker on validation, disproof within a stated scope, unavailable prerequisites, budget exhaustion, or no new material evidence. Stop the team when marginal yield fails the agreed criterion, not merely when all contexts are full.

Use transactional leases or equivalent ownership for shared work queues. Handle at-least-once delivery with idempotent claims/results and explicit mutation reconciliation. Never permit two workers to write the same branch concurrently. Record coordination, duplicate work, and validator effort as costs.

## Adopt in observable stages

| Stage | Permitted progression | Evidence required to progress |
|---|---|---|
| Baseline | Instrument the current human/tool workflow | Representative outcome, cost, review, rescue and adverse-event denominators |
| Shadow | Read/query and produce internal evidence | Useful validated yield and acceptable review burden; no automatic production effect |
| Validation assistant | Investigate existing findings in isolation | Traceable dispositions, honest inconclusive cases, demonstrated recovery |
| Remediation assistant | Prepare isolated changes and reviewable diffs | Before/after security assertion, legitimate behaviour, regression checks, authority-bound publishing |
| Scaled coverage | Add workers/indexing only to measured bottlenecks | Equal-budget or fixed-quality improvement; controlled duplication and rate limits |
| Bounded autonomy | Automate an explicitly pre-authorised action class | Deterministic preconditions, blast-radius limits, audit/recovery, and risk-specific validation |

Treat this sequence as a decision aid, not an extra approval process imposed on an already authorised task. Do not silently promote proposal authority to production mutation. Verify rollback feasibility: restoring configuration may not reverse credential exposure, disclosure, lost data, or an external notification.

Record why each added component earns its operating cost. Prefer revising a weak evidence loop over adding agents to repeat weak conclusions.
