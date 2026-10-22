# Investigations, threat hunting, and detection engineering

Use this workflow for alerts, incident analysis, and detection changes. Reuse authorised read access and established response authority. Separate evidence collection from decisions that disable identities, contain hosts, alter production rules, or trigger automated response.

## Establish competing explanations

Translate an alert into a falsifiable question and a bounded scope: affected identities/assets, relevant event types, time window, timezone, and observed consequence. Include plausible benign and attribution explanations. For unusual secret enumeration, consider credential compromise, a new inventory job, a scanner configuration change, and mistaken identity attribution.

Map each explanation to discriminating evidence: authentication/session chain, token issuance, source workload, deployment events, resource-access records, historical activity, peer behavior, and endpoint observations. Start with inexpensive high-information queries. Do not demand the user manually supply logs that available authorised integrations can retrieve.

## Query and correlate defensibly

Retain exact query text, backend/schema version, source/index, filters, tenant, time bounds, timezone, pagination, event IDs, and retrieval time. Track event occurrence time separately from ingestion/observation time. Record clock skew, delayed ingestion, sampling, retention, duplicate events, access restrictions, and unavailable sources.

Check query success and complete pagination before interpreting zero matches. Verify critical field mappings and use a known event as a positive control when feasible. An empty query on a source that does not record the action is no evidence of absence. Expand the window deliberately when causality or ingestion delay requires it; do not silently change the question.

Resolve principals with stable IDs and identity history rather than display names alone. Keep observed facts distinct from inferred causality. A deployment shortly before an alert supports a benign explanation but does not by itself establish it; correlate the workload identity, token/session chain, expected API sequence, and authorised deployment records. Keep contradictions visible.

Produce a timeline with source references and uncertainty. Distinguish confirmed scope from potentially affected scope. Avoid attribution beyond the available evidence. Use [NIST incident-response guidance](https://csrc.nist.gov/pubs/sp/800/61/r3/final) to connect investigation, containment, recovery, and lessons; do not infer incident authority from the ability to query telemetry.

## Turn a hypothesis into a tested detection

1. State the behavior, relevant threat model, required telemetry, minimum fields, expected normal cases, and operational response. Use [MITRE ATT&CK](https://attack.mitre.org/) to select relevant behavior hypotheses, not to manufacture a coverage percentage.
2. Draft the analytic and record rule identity, version, exceptions, aggregation/window semantics, and deployment destination. Keep benign exceptions narrow and tied to evidence; excluding an entire privileged identity can hide compromised use of that identity.
3. Compile the exact target-backend query. For Sigma, pin both backend and processing pipeline because [pipelines transform fields, log streams, and other semantics](https://sigmahq.io/docs/digging-deeper/pipelines.html).
4. Replay against known positive cases and representative negatives; separate tuning data from held-out evaluation data where possible. Preserve replay inputs, expected labels, resulting matches, deduplication, and analyst adjudication.
5. Measure match volume, false-positive review burden, known-positive detection, latency, data gaps, and any resulting automated actions. Do not claim recall when the set of true events is unknown. A rule compiling successfully is not a detection-quality result.
6. Review the change's operational consequences. Use an authorised observation-only rollout or controlled deployment with rollback/disable criteria. Promotion authority for a detection is separate from authority to automate containment.

If no positive corpus exists, say so. Use explicitly labelled simulations to test parsing and mechanics, while retaining the gap in real-world detection validation. Do not claim the simulation recreates the original incident.

## Finish with a defensible disposition

Deliver the alert/incident disposition, evidence-supported timeline and scope, competing explanations resolved or outstanding, telemetry gaps, and exact evidence links. For detections, include the deployable rule/query, backend/pipeline versions, test corpus and results, expected review volume, rollout status, and residual blind spots.

For containment proposals, specify the exact resources, preconditions, expected effect, blast radius, recovery path, and authority required by the existing policy. Continue within already-granted authority; ask only when the next consequential action lies outside it. Feed confirmed lessons into the threat model, runbook, and detection tests.
