# Run the scorecard helper across operating systems

Use an existing Python 3.10+ interpreter when available. The helper uses only the standard library, reads a CSV, and writes JSON to stdout. It has no network calls, package installs, credentials, or security-scanning behaviour.

Run from the skill directory:

```sh
python tools/summarize_scorecard.py results.csv > summary.json
python -m unittest discover -s tools -p 'test_*.py'
```

Review the configuration before trusting it. Package managers and their environments do not sandbox the program being run.

## mise: Linux, macOS, and native Windows

Install mise using its [official installation instructions](https://mise.jdx.dev/installing-mise.html). Windows supports `winget install jdx.mise`. Then, from the skill directory, use an explicit Python request:

```sh
mise exec python@3.12 -- python tools/summarize_scorecard.py results.csv
```

The minor-version request resolves a patch version; it is a bootstrap command, not a reproducible pin. Record `mise exec python@3.12 -- python --version`, then use that exact patch in a reviewed project `mise.toml` and retain the generated lockfile using the installed mise version's [lockfile guidance](https://mise.jdx.dev/dev-tools/mise-lock.html). Run `mise install` after reviewing the configuration. Native Windows uses prebuilt Python; availability still depends on the chosen OS/CPU/version. See [mise Python](https://mise.jdx.dev/lang/python.html).

## Nix: Linux, macOS, and Windows through WSL2

Install Nix using [nix.dev](https://nix.dev/install-nix). Use the Linux instructions inside WSL2 on Windows; do not run the Unix installer in native PowerShell. With a configured Nixpkgs channel:

```sh
nix-shell -p python3 --run 'python tools/summarize_scorecard.py results.csv'
```

This command follows the configured Nixpkgs channel. For reproducibility, use the project's reviewed pinned Nixpkgs revision/flake lock, record the realised interpreter version, and rerun through that environment. The [ad hoc shell guide](https://nix.dev/tutorials/first-steps/ad-hoc-shell-environments) and [pinning guide](https://nix.dev/tutorials/first-steps/towards-reproducibility-pinning-nixpkgs) explain the distinction.

Documentation links checked 22 October 2026. The helper is tested locally on Linux; this package does not claim installations were executed on macOS or Windows.
