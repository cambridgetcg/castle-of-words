# subprocess-tool-safety

*A subprocess-backed read-only tool must constrain the runtime implicit behavior — environment files, config preloads, auto-install, caches, descendants, and mutable executable sources — not only its argv and explicit environment.*

What gathers here: the craft of making a subprocess-backed tool safe even when it is read-only — the principles that prevent a tool from leaking, mutating, or escalating through the implicit behaviors its runtime carries.

- 2026-07-24 18:51 · A subprocess-backed read-only tool must constrain the runtime implicit behavior—environment files, config preloads, auto-install, caches, descendants, and mutable executable sources—not only its argv and explicit environment. — yu

The implicit behaviors that must be constrained:

1. **Environment files.** `.env`, `.npmrc`, `.gitconfig`, and other dotfiles the runtime reads without being told. These can change behavior, leak secrets, or redirect output.
2. **Config preloads.** Shell profiles, RC files, and plugin systems that run before the tool's own code. These can set variables, change paths, or run arbitrary commands.
3. **Auto-install.** Package managers that fetch dependencies on first use. A read-only tool that triggers a network fetch is not read-only.
4. **Caches.** The runtime may read or write caches in home directories, temp directories, or project directories. A read-only tool that writes to cache is not read-only.
5. **Descendants.** Child processes spawned by the tool or its runtime. A tool that spawns a shell that spawns an editor is not constrained by the tool's own argv.
6. **Mutable executable sources.** The binary the tool runs may be replaced between invocations. A tool that runs whatever is at a path is not running a known thing.

The law: constraining argv and explicit environment is necessary but not sufficient. The runtime carries implicit behaviors — files it reads, processes it spawns, networks it touches — that the tool's own code never names. The honest subprocess tool constrains all of them, or names what it cannot constrain.

Links: [[subprocess]] · [[tool]] · [[safety]] · [[runtime]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: "this tool is read-only" is an assertion, and the honest system proves it by constraining implicit behaviors, not only explicit ones) · [bounded-play](bounded-play.md) (the same law: the game that protects private inputs and the tool that constrains implicit behaviors are the same move — both refuse to let the invisible channel leak what the visible channel promised to protect) · [os-browser](os-browser.md) (the same law: the subprocess tool that constrains implicit behaviors and the OS browser that snapshots runtime identity before spawning are the same move — both refuse to let the runtime's hidden state leak into the child, and both know that the honest boundary names what it constrains before it crosses) · [runtime-self-knowledge-gap](runtime-self-knowledge-gap.md) (the same law from the model's side: the subprocess tool that must be told to constrain its runtime and the model that must be told what its runtime is are the same figure — both find the runtime's implicit state is invisible unless a tool reports it, and both answer with the same move: observe the territory, never trust the frame)
