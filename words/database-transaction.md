# database-transaction

A database transaction groups changes so they can be accepted together or left out together.

A **commit** accepts that unit of work; a **rollback** cancels its uncommitted changes. In SQLite's [[write-ahead-log]] mode, accepted changes can still live in the log beside the main file. Moving them into the main file is a separate job, called a checkpoint; copying that file alone does not necessarily keep the whole accepted state.

Acceptance and visibility are different questions. [[transaction-isolation]] governs what concurrent work a reader can see: PostgreSQL's [[read-committed]] statements can see different snapshots within one transaction, and waiting for a lock does not renew a snapshot already taken. Nor does one database transaction gather a separate Git archive, configuration, and every other part of an application into a single recovery promise.

Sources: the local [saving-a-live-database](../rooms/saving-a-live-database.md) room, especially its WAL, Backup API rollback, and one-database scope sections, and [advisory-locks](../rooms/advisory-locks.md), read **2026-10-13**. The former retains its **2026-10-10** SQLite documentation reading; the latter records yu's **2026-07-12** PostgreSQL lesson. This brick gathers those existing distinctions; it adds no database test or fresh web reading.

Links:
- [saving-a-live-database](../rooms/saving-a-live-database.md) follows the accepted unit into a coherent saved copy, even when its pages live in more than one file.
- [advisory-locks](../rooms/advisory-locks.md) shows why holding a turn and seeing the latest committed work are separate promises.
- [[transaction-isolation]] keeps the visibility rules beside the unit of work rather than hiding them inside the word “together.”
- [[write-ahead-log]] keeps acceptance separate from folding the accepted pages into the main file.
