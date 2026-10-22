# Sources and maintenance

## Origin and applicability

This skill converts the user-supplied report **Making Cybersecurity AI Agents More Effective and Efficient**, dated 22 October 2026, into an operational workflow. The report is the supplied synthesis; its embedded `turn...` citation identifiers are not portable bibliographic references and are intentionally not copied into the skill.

Preserve the report's useful engineering decisions: evidence-based dispositions, current threat context, deterministic tools, authority outside the model, realistic validation, durable artifacts, root-cause fixes, and measured cost/quality. Treat those procedures as engineering guidance requiring local application; the skill is not an empirical demonstration of improvement.

Do not reuse the report's benchmark percentages as guarantees or acceptance thresholds. Different benchmarks measure willingness, reproduction, repair, or live engagement performance; denominators and target distributions differ. For a numeric claim, retrieve the actual paper, dataset/version, model/harness settings, and limitations first. A report-supplied claim is not independently verified merely because this skill repeats its motivation.

## Primary source routes

Use the applicable workflow's linked sources and [tool provisioning index](../tools/index.md) for exact supported interfaces and installation paths. Useful primary anchors are:

- [NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final): incident response within cybersecurity risk management; final publication April 2025.
- [OWASP ASVS](https://asvs.owasp.org/): versioned testable security requirements. Cite the requirement's version as well as its identifier.
- [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/): choose versioned test procedures appropriate to the actual exposed surface.
- [FIRST CVSS](https://www.first.org/cvss/), [EPSS](https://www.first.org/epss/), and [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog): distinct severity, exploitation-probability, and known-exploitation inputs; combine with local exposure and impact.

Source review date: 22 October 2026. Follow live official documentation for current packages, platform support, model access, API controls, licences, and standard releases. Retain the consulted URL, date, and actual version in the run manifest. If current documentation cannot be retrieved, say which operational detail is unverified.

## Version-sensitive provider details

Keep the workflow harness-neutral. Daybreak access, a model's technical ability, Codex execution, and Codex Security orchestration are separate concepts. Do not infer access or capabilities from a model alias, a saved preference, or another product's entitlement. Before provider-specific work, verify actual organisation/project/workspace eligibility, selected model, effective per-request settings, product surface, and data policy using current official documentation. Record observed configuration without credentials.

The companion `$security-agent-engineering` skill contains the provider verification checklist and system evaluation workflow. No provider feature is necessary to use this skill's evidence process.

## Update when evidence changes

Recheck installation recipes after upstream releases or platform changes. Invalidate security conclusions on source, lockfile/SBOM, build flags, runtime image, deployment/IAM/network controls, or relevant telemetry-window changes. Re-run only checks needed to resolve the changed assumption. Maintain failures and inconclusive outcomes alongside successful results.
