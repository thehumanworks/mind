# Binary analysis and detection tooling

Read [index.md](index.md). These tools process untrusted samples/rules; keep them in the analysis environment and retain sample and rule hashes.

## Ghidra

Follow the [official Ghidra installation instructions](https://github.com/NationalSecurityAgency/ghidra#install). Download the versioned multi-platform release ZIP from the repository's Releases assets, not a source-code archive, verify its identity, and extract into a new directory. Use `ghidraRun` on macOS/Linux or `ghidraRun.bat` on Windows. Use the release's `support/analyzeHeadless` launcher for automation.

The upstream README checked on 2026-10-22 specifies a **64-bit JDK 25**. Follow the documentation included with the exact Ghidra release you adopt; older releases may require a different JDK.

**mise:** provision the matching JDK using the [Java backend](https://mise.jdx.dev/lang/java.html), then launch the downloaded Ghidra release in that environment. For a release requiring JDK 25:

```sh
mise use java@temurin-25
mise exec -- java -version
```

Lock the resolved JDK as in [mise.md](mise.md). On native Windows use the `.bat` launchers. On ARM hosts confirm the release's native helper support, or use an authorised compatible worker.

**Nix:** search for `ghidra` in the pinned input, inspect its JDK/runtime dependencies, and add the confirmed package only when supported. A packaged JDK must match the release; do not force a generic system Java onto it.

Record release/build, JDK, processor/language selection, analysis settings and scripts. Treat decompiler output as a derived representation. Installing Ghidra is not permission to execute a sample.

## YARA-X

The [official installation guide](https://virustotal.github.io/yara-x/docs/intro/installation/) provides Linux, macOS and Windows release binaries. Current mise registry support permits:

```sh
mise use github:VirusTotal/yara-x
mise exec -- yr --version
```

Lock the selected release. If automatic asset selection does not support the architecture, download and verify the exact upstream release manually. For Nix, search `yara-x` in the pinned input and use the supported result; otherwise use the official release/source procedure on a compatible host. Do not substitute classic YARA without checking rule/module compatibility.

The executable is **`yr`**, not `yara-x`. A local file scan takes the form:

```sh
yr scan /absolute/rules/example.yar /absolute/samples
```

See [YARA-X CLI commands](https://virustotal.github.io/yara-x/docs/cli/commands/). Retain sample hashes, rule revision, compiler warnings and match output. Evaluate against known positive and benign samples. A signature match is not a full behavioural finding.

## Sigma CLI

Sigma is a rule format; `sigma-cli` is its Python converter. Install it using the mise Python/uv environment:

```sh
mise use python@3.12 uv pipx:sigma-cli
mise exec -- sigma --help
```

Nix can supply Python and uv; resolve `sigma-cli` if present in the pinned package set, or install the reviewed Python release in a separate environment with `uv tool install sigma-cli==VERSION`. Replace `VERSION` with a selected release, retain dependency pins and do not mutate the immutable Nix store.

Select the actual SIEM backend and mapping pipeline. The [Sigma guide](https://sigmahq.io/docs/guide/getting-started.html) documents backend installation and conversion. Avoid `sigma plugin install` into an immutable or locked environment. For a mise-managed installation, declare a backend package in the same Python tool environment using the PyPI backend's `with` option, then re-lock; for example:

```toml
[tools]
python = "3.12"
uv = "latest"
"pipx:sigma-cli" = { version = "latest", with = ["pysigma-backend-splunk"] }
```

This is an example for an organisation using Splunk, not a default backend for all users. Pin the CLI, backend and pipeline together. Check supported options with `sigma convert --help`, compile for the target backend, then replay representative positive and negative telemetry. YAML validity or successful conversion alone does not establish a useful detection.

## Telemetry connectors

There is no universal SIEM/EDR/IAM download. Reuse the organisation's existing client or typed API and its vendor instructions. With mise or Nix, pin only the applicable client/runtime; keep credentials out of the manifest. Preserve query text, paging/completeness, immutable event IDs, source time zone, time window and ingestion delay. Production rule promotion and containment use the existing action policy.
