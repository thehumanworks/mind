# Cloud, identity, binary, and malware work

Use only the relevant workflow below. Keep the execution environment and permissions appropriate to the target. A general development environment is not automatically suitable for untrusted binaries or production identity changes.

## Cloud and identity: establish the effective path

1. Bind the task to exact accounts/tenants, projects, resource IDs, environments, regions, and authorised action classes. Retain the authority source and expiry; preserve any organisation-required signed scope. Do not introduce new approval ceremony when existing authority covers the work.
2. Collect immutable or version-identified snapshots of relevant IaC, live resource configuration, identity policies, trust relationships, network paths, service controls, and audit events. Compare desired state with observed state; neither alone establishes the other.
3. Express the attack-path hypothesis as principal → permitted action → resource or delegated identity → protected asset. Identify prerequisites at each edge, including conditions, explicit denies, inheritance, permission boundaries, organisational policies, and service-specific controls where applicable.
4. Query effective permissions or a policy simulator using the provider's documented semantics. Record simulator assumptions and missing policy types. A simulated allow is evidence about the model; it is not proof that the action succeeded against the live service.
5. Check exposure and reachability separately from permission. A public endpoint can still require strong authorisation; a private network position can still permit a privileged misuse path. Preserve contradictory evidence.
6. Validate only the minimal authorised condition in a suitable test environment. Avoid using production mutation as a shortcut for demonstrating a speculative path. If available evidence cannot resolve the route, report the specific gap.

For remediation, specify the security invariant, exact identities/resources, proposed configuration diff, dependencies, expected legitimate operations, blast radius, recovery plan, and rollback trigger. Test denied and allowed behaviors against the intended effective policy. Follow current authorisation for production changes; having write credentials does not expand task scope.

After any authorised change, retain before/after snapshots and audit operation IDs. Verify effective state, security effect, and necessary service behavior. Account for propagation delays and cached sessions. Reconcile IaC to prevent a later deploy undoing the fix. Keep “proposal prepared,” “change applied,” and “effect verified” distinct.

## Binaries and malware: separate representation from behavior

Identify the sample by digest, acquisition source, timestamp, file type, and relevant architecture. Store originals read-only in approved restricted storage. Work on disposable copies. Do not upload samples, extracted secrets, or proprietary firmware to external analysis services without appropriate authority.

Start with static triage: metadata, signatures, imports, sections, strings, control/data flow, and embedded configuration. Use [Ghidra](https://github.com/NationalSecurityAgency/ghidra) for reverse-engineering representations and retain tool/project/script versions. Treat decompiler output as an interpretation; verify decisive claims against instructions, actual control flow, or observations. A suspicious string or imported API is a lead, not proof of executed behavior.

Execute only in an approved disposable analysis environment suited to the sample's OS/architecture and threat. Remove organisational credentials, shared mounts, clipboard integration, and implicit production access. Default network access off; if network behavior matters, use controlled emulation or explicitly authorised egress to designated test services. Verify isolation outside the agent. A container alone does not establish sufficient containment for every sample.

Retain snapshot identity, instrumentation, environment changes, inputs, process/file/network observations, and captured artifacts. Distinguish observed behavior from predicted capability. Nonexecution can reflect incompatibility, missing triggers, or anti-analysis behavior; it does not establish benignness. Avoid unsupported actor attribution.

Use [YARA-X](https://virustotal.github.io/yara-x/docs/) rules for repeatable pattern-based detection. Test positive samples and representative benign negatives; record rule/runtime versions, module dependencies, and false matches. A rule match establishes its pattern condition, not the complete behavior or provenance of the file.

Conclude with observed behaviors, supported capabilities, uncertainties, defensive implications, and retained evidence. Keep dynamic observations tied to the tested environment; do not generalise one sample or sandbox run to a malware family without supporting evidence.
