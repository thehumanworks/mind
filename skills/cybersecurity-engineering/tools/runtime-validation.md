# Runtime and formal validation tools

Read [index.md](index.md). Install only after identifying the property, harness and target runtime. A tool environment must preserve the relevant target semantics.

## Clang, sanitizers and libFuzzer

**Nix:** inspect the locked input for `clang` and the relevant LLVM/compiler-rt packages, add the supported compiler to the tooling flake, and verify `clang --version`. Verify the required sanitizer runtime links on that platform before a long run.

**mise:** reuse the target project's existing compiler when valid. Otherwise obtain a versioned toolchain through [LLVM's official setup guidance](https://llvm.org/docs/GettingStarted.html) and releases, retain its digest, and use its exact executable under `mise exec`. Do not invent a universal mise LLVM backend: compiler, SDK and runtime support are platform-specific.

- Linux: use matching compiler and sanitizer runtime packages for the distribution, or a supported LLVM release/build.
- macOS: install Xcode command-line tools when required; use an LLVM distribution that contains the needed fuzzer/sanitizer runtimes. Apple Clang and upstream LLVM installations are distinct.
- Native Windows: use LLVM's Windows toolchain and required MSVC/Windows SDK environment. Test the specific sanitizer configuration; use WSL2 only for tests whose Linux behaviour answers the intended question.

For an existing compatible C++ harness:

```sh
clang++ -O1 -g -fno-omit-frame-pointer -fsanitize=address,undefined harness.cc -o harness
clang++ -O1 -g -fsanitize=fuzzer,address fuzz_target.cc -o fuzz_target
```

These are compiler-flag examples, not standalone tests. Link with the compiler driver; retain harness code, corpus, seed, time limit, compiler version and flags. [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html) and [libFuzzer](https://llvm.org/docs/LibFuzzer.html) describe runtime requirements and supported configurations. A clean bounded run is coverage evidence, not a universal proof.

## OSS-Fuzz-compatible workflows

OSS-Fuzz is an integration/service workflow, not a single binary installed by mise or Nix. Use its [project setup guide](https://google.github.io/oss-fuzz/getting-started/new-project-guide/) and an approved container runtime. Retain an exact [OSS-Fuzz repository](https://github.com/google/oss-fuzz) revision and image digests; build the project harness with the supplied helper for that revision. Nix/mise can supply Git and Python, but they do not supply the container daemon or authorise access to its socket.

Do not upload private sources, samples or crash inputs to an external service merely to run a local harness. A locally compiled libFuzzer target can be the smaller appropriate tool.

## KLEE

Use the [upstream getting-started routes](https://klee-se.org/getting-started/). The documented [Nix package](https://klee-se.org/nix/) targets **x86-64 Linux**. Resolve it from the locked input and keep its expected LLVM version together with KLEE and its solver.

```sh
nix-shell -p klee --run 'klee --version'
```

The command above is a channel-based bootstrap; use the locked flake route for a reproducible investigation. For macOS or Windows/mise workflows, prefer a dedicated compatible Linux worker or the [upstream container](https://klee-se.org/docker/), pinned by digest after confirming architecture support. Follow upstream source-build instructions if native support is needed; do not assume the generic host Clang creates compatible LLVM bitcode.

Record symbolic inputs, environment/libc models, solver, explored/completed paths, timeouts and unsupported operations. A solver timeout or incomplete exploration is inconclusive, not a successful proof.

## CBMC

The [official download page](https://www.cprover.org/cbmc/) documents Linux packages, Windows x64 MSI and macOS/Homebrew. Choose the current package appropriate to the host; older distribution packages can differ substantially in defaults.

- **Nix:** resolve `cbmc` against the locked input; use it only if the package is available and supported.
- **mise on Linux/macOS/Windows:** keep the downloaded OS package or release installed through its supported route and invoke its exact `cbmc` executable under `mise exec`. No custom installer backend is needed. Native Windows requires the documented Visual Studio command environment.
- **Fallback:** use the official source build or an authorised compatible host rather than disabling unsupported-platform checks.

Smoke check with `cbmc --version`. Verify only a stated property with explicit assumptions and unwind bounds; retain the harness, command, solver result and counterexamples. Check unwinding assertions before claiming loops were fully covered. State whether the result is bounded, whether external functions were modelled, and which environmental behaviour is excluded.
