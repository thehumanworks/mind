# Select standards by the decision they improve

Load a framework only when it provides a requirement, test procedure, vocabulary, evidence format, or operational decision needed by the task. Pin the document/schema version actually used. Check official release status before implementing an integration; drafts, schemas, identifiers, and backend support change independently.

## Apply the smallest useful set

| Need | Primary source | Use it to produce | Avoid |
| --- | --- | --- | --- |
| Testable application-security requirements | [OWASP ASVS](https://owasp.org/projects/asvs) | Applicable requirement → product invariant → test/evidence mapping. | Declaring compliance from scanner coverage or mapping every requirement indiscriminately. |
| Repeatable web-runtime checks | [OWASP WSTG](https://owasp.org/projects/web-security-testing-guide) | A scoped runtime test plan with observed results and exclusions. | Treating a checklist as permission to test new systems. |
| Root-cause classification | [MITRE CWE](https://cwe.mitre.org/) | The most specific supported weakness and rationale; a query for related variants. | Selecting a more severe category than the evidence supports. |
| Relevant attack mechanisms | [MITRE CAPEC](https://capec.mitre.org/about/index.html) | Candidate mechanisms and prerequisites for authorised tests. | Confusing a described attack pattern with a validated local attack path. |
| Threat-informed hunts and defensive controls | [MITRE ATT&CK](https://attack.mitre.org/) and [D3FEND](https://d3fend.mitre.org/) | Behavior → required telemetry → tested analytic or defensive control. | Reporting percentage-of-framework coverage without a defined observable scope. |
| Technical vulnerability severity | [FIRST CVSS](https://www.first.org/cvss/) | Versioned vector, stated assumptions, and applicable threat/environment information. | Treating a base score as the complete business risk or inventing unavailable metrics. |
| Exploitation probability | [FIRST EPSS](https://www.first.org/epss/) | Dated probability signal for exploitation in the next 30 days, combined with local context. | Treating a low score as proof of safety or a local compromise probability. |
| Known exploitation | [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Dated known-exploitation status as one prioritisation input. | Treating absence from the catalogue as proof of no exploitation. |
| Secure-development lifecycle | [NIST SSDF](https://csrc.nist.gov/projects/ssdf) | Root-cause prevention, ownership, regression controls, and follow-up work. | Adding framework prose that changes no engineering action. |
| Incident response and improvement | [NIST SP 800-61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Investigation, response, recovery, and lessons connected to organisational risk management. | Using a governance framework as evidence that a specific incident hypothesis is true. |
| Scanner interchange | [OASIS SARIF](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html) | Portable locations, rule IDs, fingerprints, provenance, and scanner results. | Treating valid JSON/schema conformance as validated exploitability. |
| Component inventory | [CycloneDX](https://cyclonedx.org/specification/overview/) or [SPDX](https://spdx.dev/use/specifications/) | Artifact-bound component/dependency inventory with generator and schema versions. | Treating source-manifest inventory as proof of what is deployed. |
| Portable detection | [Sigma](https://sigmahq.io/docs/digging-deeper/pipelines.html) | Rule plus pinned target conversion and replay evidence. | Equating portable syntax with identical backend behavior. |
| Inter-system threat intelligence | [OASIS STIX/TAXII](https://oasis-open.github.io/cti-documentation/) | CTI objects and exchange contracts when interoperability is required. | Building an elaborate interchange layer for a single internal candidate log. |

## Turn mappings into evidence

Record requirement/technique ID, version, applicability rationale, local invariant, procedure/query, evidence IDs, result, limitations, and owner. Permit `not_applicable` only with a reason; distinguish `not_tested`, `inconclusive`, and `passed`. A finding can map to multiple requirements without becoming multiple unique vulnerabilities.

For prioritisation, combine local exposure, reachable behavior, asset value, consequences, compensating controls, and remediation risk with relevant external signals. Keep the inputs visible. Do not collapse incompatible signals into an unexplained composite score. Revisit the decision when advisories, deployment, exploit evidence, or control effectiveness changes.

For format integrations, validate against an explicitly selected supported schema, retain original producer output, and test representative imports/exports. Treat conversion losses as evidence gaps. Normalise identity for deduplication while preserving distinct affected configurations and assets.

Sources checked on 22 October 2026. These references define useful concepts and interfaces; the selection and completion rules above are engineering guidance derived from the supplied report, not a claim of certification or universal performance improvement.
