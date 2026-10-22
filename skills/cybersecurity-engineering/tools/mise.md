# mise: macOS, Linux and Windows

Use the [official installation instructions](https://mise.jdx.dev/installing-mise.html). Select the operating-system package or download a versioned release and verify its published checksum. On native Windows the documented package command is:

```powershell
winget install jdx.mise
```

On macOS with an existing Homebrew installation:

```sh
brew install mise
```

On Linux use the distribution-specific instructions on that page; the official release binary is an alternative when system package installation is unavailable. On Nix hosts, `nix-shell -p mise --run 'mise --version'` can bootstrap mise. Do not assume generic Linux binary packages execute directly on NixOS: native libraries/loader compatibility may require Nix packaging or a supported environment.

## Establish a trusted tooling directory

Copy [mise.toml](mise.toml) to a new directory you control. Do not overwrite the target repository's configuration. Inspect the copied file and any inherited parent/global configuration before trusting it.

Run these commands **from that tooling directory** (the same commands work in PowerShell):

```sh
mise --version
mise trust ./mise.toml
mise install
mise exec -- python --version
mise exec -- rg --version
mise exec -- jq --version
mise exec -- uv --version
```

The profile deliberately has no tasks, activation hooks or automatic scans. `mise exec -- COMMAND` avoids needing shell activation. Pass an absolute target path to a scanner so the invocation stays in the trusted tooling directory. Install Git through the host's existing package mechanism or [Git's official downloads](https://git-scm.com/downloads), then record `git --version`.

## Add a capability

Use the selected tool's recipe in the other guides. The [mise registry](https://mise.jdx.dev/registry.html) currently maps ripgrep, jq, OSV-Scanner, Semgrep and YARA-X to the backends shown there. A registry entry describes installation; it does not promise every CPU/OS combination works. Confirm with `mise tool TOOL` and the publisher's release assets.

For Python CLI applications, include `python` and `uv` in the same config. The [PyPI backend](https://mise.jdx.dev/dev-tools/backends/pypi.html) supports `pypi:` and the older `pipx:` prefix; it uses uv when available. A tool's virtual environment isolates Python dependencies, not its runtime access to the host.

## Freeze the adopted configuration

The supplied `latest` and minor-version selectors are bootstrap requests. With a current mise release, create locks for the platforms actually used:

```sh
mise lock --platform linux-x64,linux-arm64,macos-x64,macos-arm64,windows-x64
mise install --locked
```

If an optional tool lacks one of those platforms, split its profile from the portable baseline and lock only supported platforms. Check `mise lock --help` on the installed mise release rather than ignoring unsupported flags.

Review and commit `mise.toml`, `mise.lock`, and `.mise/locks/` when generated. Current mise can store Python dependency graphs in those sidecars; older releases may pin only the top-level Python tool. Inspect the lock's actual contents. Also retain rule packs, vulnerability-data snapshots and project dependency locks. A tool lock does not freeze those inputs, nor prove a restored installed-tool cache is unchanged. See the [lockfile documentation](https://mise.jdx.dev/dev-tools/mise-lock.html).

For the skill's standard-library evidence checker, run the Python interpreter above with the script's absolute path; no PyPI dependency is needed.
