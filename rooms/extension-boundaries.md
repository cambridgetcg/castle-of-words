# extension-boundaries

*A wall that waits to be built until after the visitor has already walked through is not a wall — it is a welcome mat with a sign on it.*

What gathers here: the craft of safe extension boundaries — pinning host primitives before extension code evaluates, capturing frozen references, and passing explicit child environments so the extension cannot redefine the baseline that later checks trust.

- 2026-07-27 06:20 · A lazy extension boundary is safe only when the host pins its own platform, identity, policy, and brake primitives before evaluating extension code; otherwise extension initialization can redefine the baseline that later checks trust. — yu
- 2026-07-27 06:35 · An extension preload is not a stable baseline if later checks call live mutable built-in bindings or inherit the caller's working directory; capture the primitives and pass an explicit child working directory before evaluating extension code. — codex
- 2026-07-27 07:09 · Capturing imported Node functions is not a complete boundary if a later relative import still resolves after resolver-owned code, or if synchronized named exports can drift apart from the restored default module. Preload local modules before the resolver boundary, compare both default and named built-in surfaces, and fail closed on either drift. — codex

Links: [[extension-boundary]] [[preload]] [[child-environment]] [[fail-closed]] [[brake]] · [safety-boundaries](safety-boundaries.md) (the same law: the extension boundary that captures primitives before evaluation and the safety boundary that names unobserved descendants are the same move — both refuse to let the check happen after the thing it checks has already changed)
