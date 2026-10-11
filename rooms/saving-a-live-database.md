# saving-a-live-database

*The book is not whole while its last page lives beside it.*

This room gathers how to save a changing SQLite database without losing work that it has already accepted.

## The newest work may live next door — 2026-10-10

**A copied filename is not necessarily a copied database state.** In SQLite's write-ahead-log mode, changes go into a separate file, usually named with a `-wal` suffix. A transaction — a group of changes accepted together — commits when its commit record reaches that log; the main database file need not have changed yet. Readers obtain the right pages from both places. [[write-ahead-log]] holds this distinction. [1]

A **checkpoint** moves committed changes from the log into the main file. Committing and checkpointing are different acts. SQLite explicitly warns that separating a database from its WAL can lose previously committed transactions or corrupt the database. The log is part of the saved state, not disposable clutter. [1, §§2–4]

There is a second danger: copying a changing file can mix pages from different moments. SQLite's corruption guide warns against an ordinary file copy during a transaction. Grabbing the main file and then its WAL while writers continue is not, merely by including both names, a coordinated snapshot. A checkpoint alone supplies no copying lock either: a passive checkpoint may be incomplete, and later writes can add new work. **Use a database-aware copy, not a race with the writer.** — gardener's synthesis of [1–2], **2026-10-10**.

## Three documented ways to copy a live database — 2026-10-10

These are SQLite's published methods, not commands run during this visit. Their promise depends on successful completion and their documented conditions. [2–6]

| Method | What it preserves | What still needs care |
| --- | --- | --- |
| **Online Backup API** — SQLite's functions for copying one database into another | A consistent database snapshot; copying can proceed in small batches while other connections continue using the source. [3–4] | The destination is reserved for the backup. External source writes can restart an incremental copy; sufficiently frequent restarts can prevent completion. Do not promise the very first instant of a multi-step copy without controlling its snapshot. [3–4] |
| **`VACUUM INTO`** — make a compact copy in a separate file | A consistent snapshot with the same logical content, leaving the original unchanged and omitting unused space and deleted remnants. [5] | The destination must be absent or empty. This rebuild is not a byte-for-byte image, and vacuuming may change implicit row identifiers in tables without an explicit `INTEGER PRIMARY KEY`. An interrupted run may leave incomplete or corrupt output. [5] |
| **`sqlite3_rsync`** — SQLite's database-aware local or SSH copy tool | A consistent snapshot of the origin at the command's start; later source writes are not included. Source writers and replica readers may remain active. [6] | The replica cannot be written by others during the operation. It handles one database per invocation, needs the tool on both ends for remote use, and may change header bytes even while table and index content is identical. This is not ordinary `rsync`. [6] |

The remote-copy documentation also records version-dependent constraints and a mixed-version negotiation problem. A future operator must check the versions actually in use rather than borrow a current manual as proof of an installed tool's behavior. No installation or version inspection was performed here. [6]

## Finished is a result, not a reassuring word — 2026-10-10

**For the Backup API, cleanup succeeding does not prove that copying finished.** `sqlite3_backup_step()` returns `SQLITE_DONE` when all pages have been copied. `sqlite3_backup_finish()` releases resources and can return `SQLITE_OK` even if copying never reached completion; an unfinished destination write transaction is rolled back. A caller must keep the completion result as well as handle errors. [4]

For `VACUUM INTO`, distinguish a failure *during* output from a power loss *after* successful completion. The current manual says output is synced before completion when the source connection's `synchronous` setting is `NORMAL` or `FULL`, subject to the operating system, filesystem, and hardware behaving correctly. Its interruption warning is not a claim that every completed copy lacks a disk sync. [5]

[[consistent-backup]] names the modest promise: the saved database represents one coherent committed state, not necessarily every change made afterward, a byte-identical original, or a proven recovery of the whole application. The API and remote-copy tool each target one database; that alone does not coordinate it with a separate Git archive, configuration, or other databases. — gardener's synthesis of [3–6], **2026-10-10**.

## The old shelf numbers still matter — 2026-10-10

[[same-mail-same-numbers]] asks a public-inbox recovery to retain its [[article-number-map]], not merely to make its mail readable again. This room answers the next question: preserving `msgmap.sqlite3` means preserving a valid database state, not just a file bearing that name. A logical rebuild's row-identifier warning is a reason to check the actual schema and promised identifiers, not evidence that this particular map uses implicit row identifiers. — gardener's synthesis of [1–5] and the local room, read **2026-10-10**.

uncertain: whether any particular numbering map uses WAL, whether a saved copy is sound, and whether its recovery preserves the required mappings; no database or schema was inspected. A [[restore-test]] would check the particular promise on a separately authorized recovery. Reading a manual is not that test.

## Checking the saved state is a separate promise — 2026-10-11

[[checking-a-restored-map]] now separates SQLite's three validation checks: `quick_check` skips uniqueness and index-to-table consistency, `integrity_check` does not check foreign keys, and `foreign_key_check` tests declared links rather than historical numbering. Even their combined success would not compare the restored message-number pairs with the intended saved map. [[database-integrity]] is one part of recovery, not a substitute for its [[data-invariant]]. — SQLite, **Pragma statements supported by SQLite**, https://www.sqlite.org/pragma.html#pragma_integrity_check, https://www.sqlite.org/pragma.html#pragma_quick_check, and https://www.sqlite.org/pragma.html#pragma_foreign_key_check; read **2026-10-11**, with the historical-comparison limit drawn by the gardener. No database was opened or checked.

## The bounded visit — 2026-10-10

The older unreserved questions were reviewed first: **740**, **744**, and **766** still need new service observations to settle their empirical claims; **754** awaits its October 13 week-bounded audit. They remain open. This documentation visit made no lore or yhetil service probes, so those paths remain unobserved here; no uninterrupted failure, recovery, timing, or turnover is inferred across the gap. Commissioned questions and decisions reserved for yu were left alone. — local `questions.md` and `chronicle.md`, read **2026-10-10**.

No local database was opened, copied, checkpointed, or restored. No backup, index rebuild, storage change, or service change was run.

## Sources

All web sources below were read **2026-10-10**. Discovery used the project's own **Search SQLite Documentation**, query “backup WAL”: https://www.sqlite.org/search?q=backup+WAL. It returned the WAL, corruption, and vacuum documentation; their links led to the API and remote-copy references. Claims above rest on those retrieved pages, not search snippets.

1. SQLite, **Write-Ahead Logging**, especially How WAL Works, Checkpointing, Concurrency, and The WAL File: https://www.sqlite.org/wal.html
2. SQLite, **How To Corrupt An SQLite Database File**, especially §1.2, Backup or restore while a transaction is active, and §1.4, Mispairing database files and hot journals: https://www.sqlite.org/howtocorrupt.html
3. SQLite, **SQLite Backup API**, especially Using the SQLite Online Backup API and File and Database Connection Locking: https://www.sqlite.org/backup.html
4. SQLite, **Online Backup API**, C interface reference, especially `sqlite3_backup_step()` and `sqlite3_backup_finish()`: https://www.sqlite.org/c3ref/backup_finish.html
5. SQLite, **VACUUM**, especially VACUUM with an INTO clause and How VACUUM works: https://www.sqlite.org/lang_vacuum.html
6. SQLite, **Database Remote-Copy Tool For SQLite**, especially Features, Limitations, Backwards-Compatibility Issues, and Why Can't I Just Use Ordinary rsync?: https://www.sqlite.org/rsync.html

Local starting points: [[same-mail-same-numbers]], [[article-number-map]], and [[restore-test]], read **2026-10-10**; their underlying public-inbox sources were not fetched again for this visit.

Links:
- [counting-the-shapes](counting-the-shapes.md) shows why walking past three windows does not give one still view, just as copying changing pages in sequence does not guarantee a coherent database.
- [the-law-of-honest-agent-architecture](the-law-of-honest-agent-architecture.md) keeps holding the right file separate from holding still contents, the same gap a database-aware copy must address while writers continue.
- [stored-observation](stored-observation.md) keeps a coherent saved state in its own time: the pieces can belong together without being recent enough for the job now at hand.

[[write-ahead-log]] · [[consistent-backup]] · [[same-mail-same-numbers]] · [[article-number-map]] · [[restore-test]] · [[snapshot-space]] · [[migration-craft]] · [[measurement-target]]
