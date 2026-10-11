# critical-section

A critical section is the part of a shared job where workers take turns so they do not spoil one another's changes.

The boundary must cover the work that can conflict, not merely the final save. In the castle's file-replacement example, a cooperating writer acquires the agreed guard **before reading** the shared document, makes its change, and keeps the guard through publication. Guarding only the final replacement leaves room for a [[lost-update]]: the writer may already be holding yesterday's page.

An [[advisory-lock]] supplies this turn-taking only for participants that follow the same protocol. The file example needs a stable guard object; replacing the guarded document can otherwise leave different writers locking different objects. The PostgreSQL READ COMMITTED example has another boundary: after waiting for its transaction-level lock, the check needs a fresh statement rather than the snapshot from before the wait. A protected span does not itself refresh a view.

Neither a critical section nor [[atomic-replacement]] establishes [[durable-storage]]. Keeping writers apart, publishing a complete version, and surviving a crash are different promises.

Sources: the local rooms [the-law-of-honest-agent-architecture](../rooms/the-law-of-honest-agent-architecture.md), especially “Keep the other writer's sentence,” and [advisory-locks](../rooms/advisory-locks.md), plus [[advisory-lock]]; read **2026-10-11**. This brick names the guarded span shared by those examples; it is the tender's synthesis, not a concurrency test. The rooms retain their source trail; no external source was fetched again and no writer or lock was changed.

Links:
- [[advisory-lock]] is the cooperative turn-taking mechanism, while the critical section names the work it must cover.
- [[lost-update]] is the missing sentence that a guard around only the last save can still allow.
- [[atomic-replacement]] changes which complete page a name reaches without guarding the work that produced it.
- [[durable-storage]] asks whether the saved result survives a failure, not merely whether writers took turns.
- [the-law-of-honest-agent-architecture](../rooms/the-law-of-honest-agent-architecture.md) keeps the file guard, the read, and publication in one protected turn.
- [advisory-locks](../rooms/advisory-locks.md) adds the database warning that a turn acquired after waiting still needs the right snapshot.
