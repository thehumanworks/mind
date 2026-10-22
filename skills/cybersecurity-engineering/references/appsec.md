# Application security, dependencies, and remediation

Use this workflow for source review, scanner triage, dependency applicability, and security fixes. Establish intended security behavior before editing. Select applicable requirements from [OWASP ASVS](https://owasp.org/projects/asvs) and runtime procedures from [OWASP WSTG](https://owasp.org/projects/web-security-testing-guide); record the versions actually used.

## Investigate in increasing order of cost

1. Identify the exact commit, local modifications, built/deployed artifact, configuration, affected dependency resolution, and authorised execution environment. Read manifests, entry points, and security controls before broad searching.
2. Express the candidate as a boundary violation: actor, controlled input, protected resource, required privileges, reachable path, and observable consequence. List at least one benign explanation and evidence that would contradict a necessary condition.
3. Reuse existing scanner results. Trace relevant data and control flow using targeted text/AST/dataflow queries. Check whether validation or authorisation dominates every claimed path; account for alternate callers and representations.
4. Establish deployment applicability. Verify which artifact is deployed, who reaches it, and whether proxy, identity, feature, or network controls affect the claim. An “internal” code comment cannot establish network exposure.
5. Choose the cheapest discriminating test. Escalate from source/config inspection to focused tests, runtime reproduction, sanitizers, fuzzing, or bounded formal analysis only when the remaining question warrants it.
6. Record a disposition with evidence, coverage, and invalidation conditions. Search variants after establishing the root cause; avoid broad speculative expansion before validating the first candidate.

For dependencies, distinguish package identification, advisory/version match, dependency path, deployed presence, reachable vulnerable behavior, and local impact. A scanner match establishes a candidate, not exploitation. Retain advisory/database timestamp and ecosystem-specific version resolution. Run package-manager remediation in the permitted isolated environment because install/build hooks can execute code.

## Validate the actual target

Run the minimal reproducer against the affected revision/artifact with matching security-relevant configuration. Demonstrate the claimed violation using the least sensitive test data sufficient for the oracle. Preserve commands, inputs, outputs, and environment identity. Verify that failure is the security condition, not unrelated build, authentication, or connectivity failure.

If the build fails, record the failed attempt. Use an authorised matching CI artifact when available; prove its relationship to the affected source. A rewritten demonstration or mocked vulnerable service is supporting analysis, never a replacement for real-target reproduction.

Use instrumentation for the property it observes. For example, [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html) detects specified memory errors in instrumented executions; absence of a report does not establish complete memory safety. For fuzzing, retain harness, corpus, seed/reproduction input, engine/instrumentation version, duration, and coverage limitations. For symbolic/model checking, retain bounds, assumptions, environment models, and solver result; do not generalise a bounded result beyond those conditions.

## Remediate and verify independently

Keep vulnerability disposition separate from patch status. Write the security invariant and intended legitimate behavior. Make a minimal root-cause change in an authorised isolated checkout; preserve evidence of the vulnerable revision before changing it.

Require a verification matrix:

| Check | Required observation |
| --- | --- |
| Original condition, before fix | Reproducer reaches the vulnerable condition, or the alternative proof and missing baseline are explicit. |
| Original condition, after fix | Security boundary holds for the same test; rejection is safe and intentional. |
| Variants | Relevant alternate encodings, callers, privileges, states, and representations cannot bypass the change in the defined suite. |
| Legitimate behavior | Expected successful operations still work, including boundary cases. |
| Integration | Relevant build, ordinary tests, security regression tests, and deployment assumptions remain valid. |
| Independent review | Review the exact diff and evidence for bypasses, unrelated weakening, and a mistaken test oracle. |

A path-traversal fix illustrates the root-cause rule: rejecting one spelling of a parent-directory token can leave later decoding exploitable. Check containment at the final filesystem access boundary using semantics appropriate to the platform. A raw string-prefix test is insufficient; account for path-component boundaries, symlinks, alternate separators, and time-of-check/time-of-use races. Canonicalisation followed by an ordinary open can still race when an attacker can modify directories. Use suitable filesystem APIs or eliminate that capability, and test the stated threat model.

Report `fixed`, `still_vulnerable`, or `inconclusive` only for the exact patch and evidence. If the vulnerable baseline cannot be demonstrated and no sufficient alternative proof exists, report verification incomplete. A merged patch is not evidence of deployment; close deployed exposure only after checking the released artifact/configuration.
