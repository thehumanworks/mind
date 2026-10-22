# Source and dependency analysis

Read [index.md](index.md) before installation. Commands containing `/absolute/...` require your own paths. Run actual scans only in the authorised environment. Choose one existing SAST engine before installing another.

## Semgrep CE

From the trusted mise tooling directory:

```sh
mise use python@3.12 uv pipx:semgrep
mise exec -- semgrep --version
```

Lock the resulting configuration using [mise.md](mise.md). For Nix, resolve `semgrep` against the locked input and add the confirmed package as described in [nix.md](nix.md). If unavailable, use `uv tool install semgrep==VERSION` with the Python/uv supplied by Nix; replace `VERSION` with a reviewed release, and record that this Python environment has its own dependency-resolution inputs.

The [official CE guide](https://docs.semgrep.dev/getting-started/quickstart-ce) provides Linux/macOS installation and labels native Windows **beta**. Set `$env:PYTHONUTF8 = '1'` for the current PowerShell session before a native Windows run. WSL2 is a Linux alternative. Use a locally retained, reviewed rule set:

```sh
mise exec -- semgrep scan --config /absolute/rules --metrics=off --disable-version-check --json --output /absolute/evidence/semgrep.json /absolute/target
```

The [CLI reference](https://docs.semgrep.dev/cli-reference) documents JSON/SARIF, metrics and exit-code semantics. Capture stderr and exit status too. Review skipped paths, parser errors, timeouts, ignore files and rule coverage; an empty findings array alone is not a clean scan. Disabling metrics is not a network sandbox. CE and commercial inter-file analysis have different capabilities.

## OSV-Scanner V2

```sh
mise use aqua:google/osv-scanner
mise exec -- osv-scanner --version
```

For Nix, search `osv-scanner` in the locked input and use the confirmed package if supported. Otherwise follow the [official installation page](https://google.github.io/osv-scanner/installation/) to download a matching Linux/macOS/Windows release and verify its SLSA provenance. This avoids silently depending on a new Go toolchain. Native Windows also has the documented `winget install Google.OSVScanner` route.

```sh
mise exec -- osv-scanner scan source -r /absolute/target --format json --output-file /absolute/evidence/osv.json
```

Record extracted manifests, resolved package identities, configuration/ignores, advisory-query time and output. See [V2 usage](https://google.github.io/osv-scanner/usage/). Networked resolution and matching may disclose package metadata; use the documented offline mode with a pre-fetched, dated database when required. Do not turn a dependency match into a demonstrated attack path. The `fix` workflow can invoke package-manager behaviour and must remain separately authorised and isolated.

## CodeQL

Use GitHub's [bundle setup guide](https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/scan-from-the-command-line/set-up-codeql-cli), then:

1. Check that the repository/use case is permitted by the current CodeQL terms and organisational licence.
2. Select a release in [github/codeql-action](https://github.com/github/codeql-action/releases). Download the **platform bundle**, including compatible queries and libraries: `linux64`, `linux-arm64`, `osx64` or `win64`. Prefer `.tar.zst`; use the provided `.tar.gz` alternative if the extractor lacks Zstandard support.
3. Verify release identity/provenance as available, retain its digest, and extract into a versioned directory outside the target repository. Put its `codeql` directory on the process PATH.
4. Run `codeql version` and `codeql resolve packs`.

macOS Apple Silicon currently requires Rosetta 2 and Xcode command-line tools. Non-glibc Linux, including Alpine/musl, is unsupported. Native Windows uses its own bundle; WSL2 uses the Linux bundle.

**mise:** its `codeql` registry entry currently installs CLI binaries, which does not satisfy the recommended compatible-bundle setup by itself. Keep the verified full bundle external and run its executable within the mise-managed project build environment.

**Nix:** use a compatible packaged bundle only after checking its contents and platform. Otherwise run the official bundle in an authorised supported host environment; a Nix shell does not repair every binary-loader incompatibility.

Follow the selected language's extraction/build instructions. Retain database creation command, source commit, build logs, query-pack versions and SARIF. Inspect extraction failures before accepting results. Database creation may execute the project's build scripts. A CodeQL database is analysis evidence, not proof of production reachability.

## SBOM and structured interchange

Keep the team's existing SBOM producer and record its version, input artefact digest and selected CycloneDX/SPDX schema version. SARIF, CycloneDX, SPDX, STIX and TAXII are not interchangeable scanner installations. Validate against the chosen schema, preserve original tool records, and avoid converting scanner severity into local risk without deployment evidence.
