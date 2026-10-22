# Provider and access configuration

**Source check: 22 October 2026.** Keep product-specific settings here rather than freezing model lists in the core workflow. Recheck documentation and the installed client before integrating or changing access.

The official [Daybreak overview](https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview) describes Blue and Red as access tiers for authorised cybersecurity work. Treat access tier, model capability, harness, and security product as separate choices. Reduced refusal does not prove better reasoning or validated outcomes. The [Codex Security documentation](https://developers.openai.com/codex/security) describes a security workflow; do not attribute that orchestration to an API model alone.

## Verify the actual execution path

1. Identify the surface: account/workspace product, CLI/SDK, security product, or custom API integration. Inspect installed version and config schema before writing flags or request fields.
2. Read the current provider eligibility/onboarding page. Confirm the selected organisation, project/workspace, credentials and model are approved for the intended workflow. Do not infer entitlement in one surface from entitlement in another.
3. Prefer a documented explicit model identifier. Verify aliases and deprecations live; do not copy historical names from the report as configuration. For the Responses API, consult the [current model/program selection guide](https://developers.openai.com/api/docs/guides/daybreak). Organisation approval tier and the request’s `access_programs.cyber` value are distinct: some eligible models require Red approval while the supported request value remains `daybreak_blue`. Match the documented value to the model, and inspect returned programme/model metadata where available; selecting a value does not grant access.
4. Inspect the actual outbound request or trusted request metadata with credentials redacted. Record requested model, resolved model when available, access-programme setting, client version, project/workspace identifier and response/request ID. Label unobservable fields `unknown`; a saved preference is not proof of propagation.
5. Verify effective sandbox, network, approval and data-control settings independently. Access tier does not grant system authority, alter the user's scope, or establish data-retention/residency guarantees. Consult [OpenAI data controls](https://platform.openai.com/docs/guides/your-data) for applicable API arrangements rather than inferring them from cyber access.
6. Run a harmless in-scope canary through the real integration. Check request acceptance, tool execution boundaries, logging redaction, and failure behaviour. Do not probe advanced capabilities merely to discover entitlement.

When account-specific information is inaccessible, complete provider-agnostic design and record integration as unverified. Ask only for the missing account/authority decision needed to proceed. Do not claim to have activated Daybreak or installed Codex Security through a documentation-only deliverable.

## Distinguish authority from model selection

Read [agent approvals and security](https://developers.openai.com/codex/agent-approvals-security) for the selected runtime. Sandbox capability and approval decisions are separate. Existing grants apply within their approved scope; changing a model or access tier cannot expand that scope. Managed organisation policy still applies.

Use the provider configuration as a recorded experimental variable. Compare the same task, evidence gates and tools. Measure accepted outcomes, review burden, failure/rescue rates, and cost in addition to refusals. Reverify this reference when documentation, client version, model routing, workspace/project, or contractual data settings change.
