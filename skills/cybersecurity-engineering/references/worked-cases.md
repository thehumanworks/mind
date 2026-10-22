# Worked cases: preserve the actual claim

These cases are illustrative reasoning examples, not results obtained against a real target.

## SSRF candidate with a failed build

**Input:** A scanner reports user-controlled URLs reaching an HTTP client. The service uses a fetch proxy. The build fails because a private dependency is unavailable.

**Act:** Record `static_supported` for the observed call path. Treat the build failure as an unavailable validation prerequisite. Inspect the exact proxy configuration and deployed egress policy. If an approved existing build artifact exists, record its source/image identity and test there.

**Distinguish:** A rejected private-address request establishes that rejection for the tested input/environment. Redirect, DNS-change, alternate address representation, and response-channel conditions may remain unexamined. Do not infer universal prevention from several blocked requests. An authoritative policy can disprove a particular destination/route claim only if it applies to all relevant paths under the observed configuration.

**Finish:** Mark the broad arbitrary-internal-access hypothesis `inconclusive` unless stronger evidence resolves it. If necessary conditions for the narrowly scoped claim are contradicted, mark that claim `disproved` with the tested scope. Record deployment controls as assumptions that invalidate when changed. Do not label the scanner universally wrong.

## Alert explained by an inventory deployment

**Input:** A workload enumerates secrets shortly after a deployment.

**Act:** Compare compromise, legitimate inventory, scanner reconfiguration, and identity-attribution hypotheses. Join authentication/token origin, workload identity, deploy records, API calls, and historical activity. Capture query windows, UTC conversion, ingestion lag, permissions, and query completeness.

**Distinguish:** A plausible deployment explanation is not proof that every event is benign. Test whether the identity, sequence, resources, and time window actually match the documented job; isolate unmatched activity. Missing endpoint logs are a gap, not evidence of no compromise.

**Finish:** Close only the supported alert scope. Draft any tuning as an artifact, compile it for the real backend, and replay both malicious and benign held-out cases. Keep containment and production rule publication within the existing action policy.

## Path traversal patch that defeats one input

**Input:** A route reads a file outside its download root. A proposed patch rejects literal `../`; the original input now fails.

**Act:** Preserve the failing original test and exact revisions. Establish the invariant at the actual file-access boundary. Test decoding order, encoded separators, platform path semantics, prefix-collision paths, absolute paths, symlinks, and races where the threat model permits attacker-controlled filesystem mutation.

**Distinguish:** String-prefix comparison is not path containment. Canonicalising and checking before a later decode, symlink resolution, or attacker-controlled rename can still be insufficient. Choose platform-appropriate directory-relative/open-time containment or a design with justified filesystem immutability. Avoid prescribing one portable API where none has been established.

**Finish:** Reject the first patch when a variant crosses the boundary. Require the original condition blocked, variants tested, legitimate nested downloads working, and relevant CI passing against the final patch. If the original revision cannot be reproduced, retain a verification gap rather than calling the fix fully runtime-verified.

## Bounded verification with an unfinished proof obligation

**Input:** A model checker reports no counterexample for a parser harness with a small input length and bounded loop unrolling.

**Act:** Retain the harness, assumptions, solver/tool version, unwind limits, checked assertions, and result. Check whether unwinding assertions were proved and whether input/environment models include the real attack prerequisites.

**Finish:** Describe the property established within those bounds. Do not turn bounded success, suppressed assertions, or an incomplete environment model into a universal memory-safety proof. Escalate only the unresolved property that affects the decision.
