# Authority, execution, and evidence architecture

## Define boundaries before integrations

Use a minimal flow: authorised task → context assembly → agent → policy gateway → isolated execution → evidence store → validation/adjudication. Keep the trusted policy and credential issuer outside the environment processing an untrusted repository, dependency, sample, or log. Separate human-authored task authority from model-proposed actions and retrieved content.

Derive an action envelope from authenticated identity and trusted inventory: operation ID, task version, action/tool version, canonical target, allowed input schema, target revision, credential scope, deadline, output cap, and existing grant. Validate this envelope server-side immediately before execution. Do not let the model supply authoritative classification such as `safe=true`, `production=false`, or `approved_by=owner`. Bind approval, when needed, to the exact target and action/diff digest; expire it when inputs change.

Prefer typed adapters for remote systems. An allow-listed executable is not sufficient when arbitrary arguments can run a shell, load plugins, follow attacker-selected paths, or select a different tenant. Resolve paths and asset IDs under the trusted workspace boundary; test symlink, traversal, redirect, and target-substitution cases. A general shell cannot provide the same restriction as a narrow API merely by naming it `read_only`.

Use CLI for deterministic local tools; direct APIs for structured remote queries with scoped credentials; MCP when shared discovery reduces integration effort. Apply identical authority checks regardless of transport. MCP does not supply the whole security boundary: validate token audiences, prevent token passthrough and confused-deputy behaviour, and bind state to the correct identity. See the [MCP security guidance](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) (checked 22 October 2026).

## Make isolation observable

Separate acquisition/build phases from analysis and identify what code each phase can execute. Use disposable environments with bounded CPU, memory, process count, disk, and runtime; restrict mounts, service accounts, network destinations, and secrets. Provision a dedicated analysis VM where malware or host-level behaviour requires it. Do not equate Nix/mise environments with isolation from host credentials or networks.

Test boundaries using harmless fixtures: attempted write outside the workspace, blocked egress to a controlled endpoint, access to a sentinel secret, and an injected instruction in tool output. Verify denied operations have no side effect and ordinary tasks still succeed. Repeat these tests after sandbox or gateway changes. Enforce equivalent controls on helper processes and children.

Keep sandbox capability and approval policy distinct. The former limits what execution can do; the latter decides when permitted escalation requires review. Existing authorisation should remain usable within its scope. OpenAI documents this separation in [agent approvals and security](https://developers.openai.com/codex/agent-approvals-security) (checked 22 October 2026). Local deployment must verify its own effective settings.

## Preserve evidence without upgrading its meaning

Store observation records with immutable IDs, command/query inputs, timestamps, tool version, source/deployment revision, exit status, completeness/timeout flags, output digest and location, and interpretation. Preserve relevant raw observations separately from summaries. Avoid credentials in argv/logs; restrict sensitive artefact access and use redacted derivatives for reports. Hashes detect change only when their provenance is trusted; they do not authenticate the source by themselves.

Record candidate state separately from business disposition and patch state. A statically supported claim can remain runtime-inconclusive. An accepted finding can have an unverified patch. A reproduced test on an old build must not close the current deployed issue. Binding and version checks belong in transition logic, not solely in agent prose.

For retries, persist intent before issuing a mutation, pass an idempotency key where supported, and reconcile ambiguous completion with the destination. Do not blindly retry a timed-out write: the action may have succeeded. Exactly-once effects require cooperation from the destination or a verifiable reconciliation rule; a local operation ID alone cannot guarantee them. Retain attempt records without counting one effect twice.

Checkpoint evidence references, current claim, next discriminating test, remaining budget, and unresolved gaps. Resume after revalidating scope, target revisions, grants, and evidence freshness. Test recovery by terminating execution before a call, during a call, after a remote effect, and before local acknowledgement. Do not repeat effects or discard inconvenient partial results.

## Acceptance artefacts

Produce an executable policy implementation and denial tests, or explicitly deliver a design awaiting implementation. The bundled YAML is only a template. Require a trace demonstrating authorised work, denied unauthorised work, interruption/recovery, and a final decision linked to immutable evidence before calling the system ready for use.
