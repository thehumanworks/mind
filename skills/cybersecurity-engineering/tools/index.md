# Provision the tools needed for the next test

Documentation checked: **2026-10-22**. Resolve and record versions when adopting a recipe; these files do not assert that every package was installed or tested on every OS.

1. Reuse the project's working build, tests, SAST, SCA and telemetry clients first.
2. Choose **[mise](mise.md)** for project-local tool selection on macOS, Linux or Windows, or **[Nix](nix.md)** for a pinned development environment on macOS, Linux or Windows through WSL2.
3. Add only the capability needed: **[source/dependency analysis](source-analysis.md)**, **[runtime/formal validation](runtime-validation.md)**, or **[binary/detection analysis](binary-and-detection.md)**.
4. Before installing, inspect the configuration and upstream publisher, select a version, check OS/CPU/libc support and licence applicability, and retain the lockfile or download digest. Provision in a trusted tooling directory, outside the repository being investigated.
5. Run the tool's version/help check, then a known positive and negative fixture when relying on its results. Record the actual executable, version, rule/query/database revision and exit status. Separate tool failure, empty results and a completed negative test.

## Platform routes

| Host | Nix | mise | Material constraints |
| --- | --- | --- | --- |
| Linux x86-64 | Native | Native | CodeQL needs glibc. KLEE's documented Nix recipe targets x86-64 Linux. |
| Linux ARM64 | Native baseline | Native baseline | Check each release's ARM64 artefacts; do not silently substitute an x86 binary. |
| macOS Intel / Apple Silicon | Native baseline | Native baseline | Some analysis tools need Xcode tools, Rosetta or their own JDK. Treat these as separate prerequisites. |
| Windows x64 | Use Linux Nix inside WSL2 | Native PowerShell | Semgrep currently labels native Windows beta. Use a Linux environment for Linux-specific harnesses. |
| Windows ARM64 | WSL2 Linux ARM64 baseline | Check individual tool artefacts | Native Windows support does not imply ARM64 support. Use a documented compatible worker when an artefact is unavailable. |

The checked baseline manifests provide Python, ripgrep, jq and uv; Nix also provides Git. The Python scripts bundled with this skill use the standard library and do not require scanners or cloud accounts.

## Provisioning is separate from execution containment

A Nix development shell or mise environment selects software; it does **not**, by itself, confine commands, remove host credentials, restrict egress, or make malware safe to run. Use the harness's independently enforced execution policy. Installing a package can itself execute build or installation code.

Keep scanner configuration, rule packs, evidence and credentials outside attacker-writable repository paths. Do not trust a repository's mise tasks, shell hooks, Nix expressions, build scripts, package-manager hooks or scanner exclusions merely because a file has a familiar name. Avoid automatically trusting an entire directory tree.

For direct downloads, use the vendor's exact release asset, verify published provenance/signatures where available, and record a SHA-256 digest. A digest computed only after an unverified download records identity; it does not establish publisher authenticity. Do not replace missing checksums with invented values or bypass a mismatch.

## Scope of installation guidance

| Capability | Included route |
| --- | --- |
| Git / ripgrep / jq / Python / uv | Core Nix and mise manifests; native Git prerequisite for mise |
| CodeQL / Semgrep CE / OSV-Scanner | Source analysis guide |
| Clang sanitizers / libFuzzer / OSS-Fuzz / KLEE / CBMC | Runtime validation guide |
| Ghidra / YARA-X / Sigma CLI | Binary and detection guide |
| SIEM / EDR / cloud / IAM clients | Reuse the organisation's documented, authorised client or typed API; obtain its installation and API docs for the selected vendor. No generic connector or credentials are bundled. |
| SARIF / SBOM / STIX / TAXII | Formats or protocols, not programs to install. Use existing producers; add a validator or converter only for an identified interoperability need. |

If a platform cannot run a tool, record that limitation and use an authorised compatible worker. Preserve target OS, runtime and dependency semantics when moving validation; a successful Linux simulation does not establish Windows production behaviour.
