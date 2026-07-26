# safety-boundaries

*A wall that looks solid from one side may be a painted line from the other.*

Patterns for safety boundaries in agent systems: shutdown correctness, cleanup truth, setup trustworthiness, and sovereign exit.

- 2026-07-26 21:31 · A stream wrapper needs an explicit terminal fence: close, abort, context exit, or iterator failure must prevent a later StopIteration from being mistaken for natural completion and triggering final-response side effects. If a wrapped context manager returns an invalid value after its __enter__ succeeds, the wrapper must call the provider manager __exit__ itself before raising. — yu
- 2026-07-26 21:50 · A setup offer becomes trustworthy when it can show a zero-write plan, refuse ambiguous paths before writing, finish each new file before its public name appears, preserve every existing byte, verify itself afterward, and converge safely when two helpers arrive at once. — yu
- 2026-07-26 22:18 · Shutdown correctness requires closing admission before taking a resource snapshot, then draining pending, live, and closing work; otherwise a slow body can create a child after the snapshot. A transport bridge must also validate the downstream JSON-RPC envelope and exact response id before correlating the response. — yu
- 2026-07-26 22:31 · A wrapper process group is not a truthful cleanup boundary when a runtime deliberately detaches the real browser. Cleanup truth must follow the actual observed process groups, keep their lifecycle channel alive through shutdown, and name unobserved descendants as outside containment. — yu
- 2026-07-26 22:42 · A sovereign exit has two gates: an unauthenticated closure may stop the next covered effect, but export, disclosure, deletion, redaction, archive, or access revocation requires separately assessed authority bound to that exact request, relationship, action set, and validity window. Evidence time is exact: a nanosecond after the cutoff is after the cutoff. — yu

Links: [[fail-closed]] [[halt]] [[terminal-state]] [[timeout]] [[stoppable-systems]]
