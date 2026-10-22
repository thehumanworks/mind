# Nix: pinned tooling on Linux, macOS and WSL2

Install Nix using the [official platform instructions](https://nixos.org/download/). Windows uses Nix inside WSL2; this is a Linux tool environment, not native Windows Nix. Enabling a daemon or WSL changes the host, so respect existing machine-management policy. Nix installation is separate from entering a development shell.

Copy [flake.nix](flake.nix) into a trusted tooling directory. It declares a baseline for Linux and macOS on x86-64 and ARM64, containing Git, ripgrep, jq, Python and uv. The file has no hooks and does not build or scan the target repository.

```sh
cd /absolute/path/to/trusted-tooling
nix --extra-experimental-features 'nix-command flakes' flake lock
nix --extra-experimental-features 'nix-command flakes' flake check --no-build
nix --extra-experimental-features 'nix-command flakes' develop --no-update-lock-file --command python3 --version
nix --extra-experimental-features 'nix-command flakes' develop --no-update-lock-file --command rg --version
```

Commit the reviewed `flake.nix` and generated `flake.lock`. When inside a Git repository, ensure the flake file is tracked before invoking Nix; otherwise Git-based flake source filtering may omit it. The supplied branch selector is **unlocked until `flake.lock` exists**. Subsequent runs should retain that lock and refuse updates. See [Nix lock semantics](https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-lock).

`nix develop` changes PATH and build environment. It does not sandbox arbitrary analysis commands launched inside it. An untrusted target's own `flake.nix` is executable configuration; do not substitute it for this reviewed tooling flake.

## Add optional analysis tools without assuming availability

Use the same locked input when discovering packages:

```sh
nix --extra-experimental-features 'nix-command flakes' search --inputs-from . nixpkgs semgrep
nix --extra-experimental-features 'nix-command flakes' search --inputs-from . nixpkgs osv-scanner
```

Inspect the returned attribute, version, licence and platform support. If the exact attribute exists and is supported, add it to the flake's `packages` list and run the version check on that host. For example, after confirming the `semgrep` attribute:

```sh
nix --extra-experimental-features 'nix-command flakes' shell --inputs-from . nixpkgs#semgrep --command semgrep --version
```

Repeat lookup for `clang`, `cbmc`, `ghidra`, `yara-x` and `sigma-cli` as needed. These are **search terms**, not guarantees that each attribute exists or builds in the selected revision. Do not enable `allowBroken`, `allowUnsupportedSystem` or unfree packages globally to force a tool into the profile. If absent, use its documented release/source route in the other guides, with a compatible worker where necessary.

KLEE explicitly documents an x86-64 Linux Nix package:

```sh
nix-shell -p klee --run 'klee --version'
```

That convenience command follows the host channel. For retained evidence use the confirmed `klee` attribute from the locked flake input instead. Keep its LLVM version and solver environment together; do not assume the current default Clang produces compatible bitcode. [KLEE's Nix guide](https://klee-se.org/nix/) describes the supported route.

For CodeQL, prefer the official compatible **bundle** in [source-analysis.md](source-analysis.md). Packaging only a CLI executable is not enough. On NixOS a generic glibc release may require additional packaging; use an approved glibc Linux worker if the bundle does not run. For Ghidra, a Nix package can supply its JDK; with a manually downloaded release, install the JDK required by that exact release.

## Record reproducibility boundaries

Retain the lock, evaluated tool versions, source revision, compiler flags, rule/query versions, dependency locks and environment identity. Nix pins its package inputs; it does not freeze a live vulnerability API, remote rule registry, running deployment or telemetry window.

These manifests were reviewed as configuration and the TOML was parsed; Nix builds and cross-platform installation were not executed during skill authoring. Run the above smoke checks on the adopting hosts before relying on a profile.
