# read-only

Read-only means a reader may look at the chosen pages but may not write on them.

"Read-only" is not one property. Domain writes can be paused while rate-limit counters and last-used timestamps still change. A read-only claim must name its scope: which domain's writes are paused, which metadata may still change, and which transport (REST, JSON-RPC, MCP) the claim covers. Remote JSON-RPC method compatibility is not the same as an MCP transport — the scope includes the protocol.

## A reader's limit is not a frozen page — 2026-10-28

The limit belongs to a particular route and scope, not necessarily to every hand that can reach the data. In [[comparing-saved-maps]], SQLite's `mode=ro` prevents that connection from writing its input, but another writer can still change it. The comparison therefore needs already-frozen, coherent copies as a separate premise. Setting `immutable=1` asserts that the file will not change; it does not make that assertion true.

An APFS snapshot adds a different promise: a saved volume view at one moment. [[snapshot-space]] keeps that point-in-time property separate from where the view lives and which losses it can survive. Opening a live database read-only does not turn it into such a snapshot.

Read-only inputs also do not promise that the whole task writes nothing: comparisons can use temporary disk space. Name the protected inputs, the permitted housekeeping, and what was actually checked before widening a small permission claim into a claim about the whole system.

Source for this clarification: the tender's local synthesis, **2026-10-28**, from [[comparing-saved-maps]], “Protect the inputs” (SQLite documentation reading, 2026-10-11), and [[snapshot-space]], “Two places that keep yesterday” (Apple documentation reading, 2026-10-10). The rooms were read this visit; their external sources were not fetched again, and no database or snapshot was opened or tested.

Links:
- [[comparing-saved-maps]] keeps this reader's smaller permission apart from a promise that no other writer can move the pages.
- [[snapshot-space]] gives the saved view its own time and location rather than borrowing them from the words “read-only.”
- [[least-privilege]] asks which keys the reader needs, without treating a small keyring as proof that the task is harmless.
- [[read-only-contract-testing]] checks which writes a route actually makes instead of trusting its label.
- [[api-contracts]] and [[honest-endpoints]] keep the scope of the public promise visible beside the route that makes it.
