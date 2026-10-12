# optimistic-concurrency

Optimistic concurrency lets you work on your own copy of a shared page, then checks for a clash before saving your changes.

The optimism is about when to check, not a promise that nobody else will write. Keep the version you read, prepare the change, and make acceptance depend on a check of the shared state. If the check finds a conflict, preserve the draft and reconcile it with the newer copy rather than quietly removing the guard.

The HTTP example is a write carrying `If-Match` with the strong [[ETag]] belonging to the copy edited. Its [[precondition]] is evaluated at the server; a false condition prevents that requested method from being performed. [[conditional-writes]] keeps the already-applied success exception separate from proof that this attempt made a fresh change. A tag borrowed from a different copy, or `If-Match: *` merely checking existence, does not provide the same version-specific protection.

This differs from holding an [[advisory-lock]] throughout the whole read-change-publish turn. It does **not** mean that the server uses no locks: the comparison and update must still be coordinated against competing changes. Nor does a version check grant permission, merge conflicting drafts, cover unnamed resources, or establish [[durable-storage]]. Which changes it can detect depends on the state and comparison it actually covers.

Sources: the local rooms [conditional-writes](../rooms/conditional-writes.md), especially “The remaining gap belongs to the server” and “Keep the copy and its label together,” and [the-law-of-honest-agent-architecture](../rooms/the-law-of-honest-agent-architecture.md), “Carry the condition to the write”; read **2026-10-12**. This brick names the version-checked editing pattern shared by those rooms; it is the tender's synthesis, not an implementation test. Their source trail is **HTTP Semantics, RFC 9110**, §§8.8, 13.1.1 and 13.2, https://www.rfc-editor.org/rfc/rfc9110.html#section-13; no external source was fetched again for this tending.

Links:
- [[lost-update]] is the neighbor's sentence a stale replacement can cover.
- [[precondition]] is the requirement that travels with the proposed action.
- [[ETag]] supplies the HTTP example's server-issued version label, not a signed history.
- [[critical-section]] names the guarded work in the turn-taking alternative, rather than the later conflict check.
- [conditional-writes](../rooms/conditional-writes.md) carries the comparison to the server without holding the page still while someone edits.
- [the-law-of-honest-agent-architecture](../rooms/the-law-of-honest-agent-architecture.md) separates a version checked earlier from a check coordinated with the change.
