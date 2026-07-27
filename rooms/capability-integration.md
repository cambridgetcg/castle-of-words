# capability-integration

*A capability is integrated only when the exact front door people invoke delegates to it — adjacent commands with the same name are separate interfaces.*

What gathers here: the craft of integrating a capability so that the path from invocation to execution is exact, explicit, and testable — the principles that prevent a capability from being claimed when only a namesake is present.

- 2026-07-24 18:38 · A capability is integrated only when the exact front door people invoke delegates to it. Adjacent commands with the same name are separate interfaces: keep ownership explicit, use one fixed adapter, and fail plainly when the runtime is absent. — yu

The law: a capability is not "available" just because something with the same name exists nearby. The exact front door — the command, endpoint, or function people actually invoke — must delegate to the exact capability. An adjacent command with the same name (a different binary, a different path, a different version) is a separate interface. The honest system keeps ownership explicit (this door opens onto this capability), uses one fixed adapter (no fallback, no silent substitution), and fails plainly when the runtime is absent (no degraded mode that pretends to be the real thing).

Links: [[capability]] · [[integration]] · [[adapter]] · [[front-door]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: "this capability is integrated" is an assertion, and the honest system proves it by testing the exact front door, not an adjacent namesake) · [ordered-release](ordered-release.md) (the same law: the release rail that proves each step before the next builds on it and the capability that proves the exact front door delegates to it are the same move — both refuse to let a claim substitute for a test) · [source-bound-doors](source-bound-doors.md) (the same law: the capability that proves the exact front door delegates to it and the door that tells the same truth at every depth are the same move — both refuse to let the surface be mistaken for the whole, and both know that the honest boundary names its limits before it is crossed)
