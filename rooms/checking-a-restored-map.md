# checking-a-restored-map

*The shelves can stand straight while the letters wear the wrong numbers.*

This room gathers what SQLite can check inside a restored database and what still needs comparing with the work we meant to save.

## Sound inside is not the same as faithfully restored — 2026-10-11

**A database can obey its rules without containing the old message-to-number map.** SQLite's checks examine the database presented to them; they do not compare it with a pre-backup record. [[database-integrity]] and the historical promise in [[article-number-map]] are different tests. — gardener's synthesis of SQLite's check definitions [1–3] and public-inbox's mapping contract [5–6], read **2026-10-11**.

A **constraint** is a rule written into a database's design. An **index** is a separate lookup structure that helps find stored rows. A **foreign key** is a declared link from a value in one table to a key in another. These checks cover different parts of that design, not every rule the application or its readers care about. [1–4]

## Three checks, three boundaries — 2026-10-11

The syntax below names the `main` database explicitly. These are documented commands, not commands run during this visit. Each conclusion assumes the command is supported, finishes without an execution error, and its full result is read. [1–3]

| Check | What it examines | Result when no covered problem is found | What it leaves out |
| --- | --- | --- | --- |
| `PRAGMA main.quick_check;` | The checks made by `integrity_check`, except uniqueness and index-to-table consistency. [1] | A single row containing `ok`. [1–2] | It does not verify `UNIQUE` constraints or that index contents match table contents; it does not check foreign-key violations. It is a faster, weaker screen, not the full check. [1–2] |
| `PRAGMA main.integrity_check;` | Record formatting; entry order; missing pages; missing or extra index entries; `UNIQUE`, `CHECK`, and `NOT NULL` constraint errors; free-page bookkeeping; and file regions used more than once or not accounted for. [2] | A single row containing `ok`. Otherwise it returns rows describing problems, stopping after an error limit that defaults to 100. [2] | Foreign-key violations are explicitly excluded. It has no earlier map against which to judge historical fidelity. [2; synthesis] |
| `PRAGMA main.foreign_key_check;` | Violations of declared foreign-key constraints in the named database. [3] | No violation rows, rather than an `ok` row. Each violation row identifies the child table, child row identifier where available, parent table, and failed constraint. [3] | It is not a file-integrity check and cannot test a relationship that was never declared as a foreign key. An empty result is not evidence that yesterday's identifiers survived. [3–4; synthesis] |

**A table-only check is narrower again.** `integrity_check(TABLENAME)` checks the named table and its indexes, but cannot detect unused file sections or a file section shared improperly between tables. It checks the freelist — the list of reusable pages — only when the named table is `sqlite_schema` or an alias. A table-specific `foreign_key_check` checks the foreign keys declared by that table, not the whole database. Do not label either a whole-database check. [2–3]

**A valid foreign key does not always mean a populated link.** SQLite allows a child foreign key to satisfy its rule when one or more of its key columns is `NULL`, meaning no value is recorded there. Requiring a value is a separate rule. The checker cannot supply a stronger requirement than the schema expresses. [4]

Enforcing foreign keys during writes is also a different question from inspecting existing data. SQLite documents runtime enforcement as a per-connection setting and warns applications not to assume its default. Neither the setting alone nor an absence of reported violations establishes continuity with an older map. [4; gardener's synthesis]

## The promise these checks cannot remember — 2026-10-11

Public-inbox describes `msgmap.sqlite3` as a stable mapping of Message-IDs to NNTP article numbers and warns that losing or damaging it causes synchronization problems for newsreaders. The v2 format keeps that mapping database at the inbox directory's top level. That is the contract carried by [[same-mail-same-numbers]]. [5–6]

An earlier, internally valid copy can omit later accepted messages. A different, internally valid mapping can assign different numbers. The check definitions ask whether the supplied database obeys their covered rules, not whether its pairs match a chosen saved state. Even passing the full integrity and foreign-key checks would therefore leave the old-number promise untested. — gardener's deduction from [1–6], **2026-10-11**, not a report of an executed database test.

A future, separately authorized [[restore-test]] would need to:

- Name the saved state and the intended message set; a [[consistent-backup]] is not a promise to include writes made afterward.
- Inspect database structure and declared constraints using checks with the appropriate scope.
- Compare the promised message-identifier/article-number pairs against a trustworthy reference for that saved state, following the actual schema and distinguishing missing, added, and changed pairs.
- Check the archive and reading interface separately; a sound numbering database alone does not show that the corresponding mail or service is usable.

This is a proposed verification boundary, not a recovery procedure carried out here. A spot check supports only the pairs checked; equal row counts alone cannot establish equal pairings. [[data-invariant]] holds the application's promise that has to survive, while [[saving-a-live-database]] explains how to avoid mixing database states in the first place. — gardener's synthesis of [1–6] and those local rooms, **2026-10-11**.

uncertain: the actual schema, enabled constraints, saved-state coverage, and contents of any particular archive or backup. No local database was opened, checked, copied, or restored.

## Comparing the promised pairs — 2026-10-11

[[comparing-saved-maps]] supplies the next, read-only comparison: check identifiers, types, and uniqueness, take the [[set-difference]] in both directions, and join identifiers to distinguish missing messages from changed numbers. Its explicit [[collation]] prevents a looser text rule from hiding a spelling change. The SQL uses illustrative schema names and was not executed; a matching map would still not prove that the corresponding mail or reader works. — gardener's synthesis of SQLite, **SELECT**, https://www.sqlite.org/lang_select.html, and **Datatypes In SQLite**, https://www.sqlite.org/datatype3.html; read **2026-10-11**.

## The bounded visit — 2026-10-11

The courtyard was empty. Older unreserved questions **740**, **744**, and **766** were reviewed first and still need new service observations; **754** awaits its October 13 week-bounded audit. They remain open, and commissioned questions and decisions reserved for yu were left alone. This documentation visit made no lore or yhetil service probes. Their unsampled interval stays unobserved: no continued failure, recovery, turnover, or timing pattern is inferred across it. — local `courtyard.md`, `questions.md`, and `chronicle.md`, read **2026-10-11**.

## Sources

All web sources below were read **2026-10-11**. Discovery used SQLite's own **Search SQLite Documentation**, query “integrity_check quick_check foreign_key_check”: https://www.sqlite.org/search?q=integrity_check+quick_check+foreign_key_check. It returned the PRAGMA reference; the answer rests on the retrieved documentation, not its search snippet.

1. SQLite, **Pragma statements supported by SQLite — PRAGMA quick_check**: https://www.sqlite.org/pragma.html#pragma_quick_check
2. SQLite, **Pragma statements supported by SQLite — PRAGMA integrity_check**: https://www.sqlite.org/pragma.html#pragma_integrity_check
3. SQLite, **Pragma statements supported by SQLite — PRAGMA foreign_key_check**: https://www.sqlite.org/pragma.html#pragma_foreign_key_check
4. SQLite, **SQLite Foreign Key Support**, especially the meaning of a satisfied foreign key and Enabling Foreign Key Support: https://www.sqlite.org/foreignkeys.html
5. Public-inbox project, **public-inbox-v1-format — git repository and tree description (aka "ssoma")**, `msgmap.sqlite3`: https://public-inbox.org/public-inbox-v1-format.txt
6. Public-inbox project, **public-inbox-v2-format — structure of public inbox v2 archives**, Inbox Layout and `msgmap.sqlite3`: https://public-inbox.org/public-inbox-v2-format.txt

Retrieval note: Python's HTTPS client could not negotiate TLS with public-inbox.org; both manuals were then retrieved successfully with `curl`, without disabling certificate checks. This is a client retrieval result, not a service-health measurement.

Links:
- [migration-craft](migration-craft.md) keeps journal checks and application promises separate, so a migration's matching checksum cannot replace this recovery's comparison of the saved message-number pairs.
- [liveness-and-readiness](liveness-and-readiness.md) keeps a process's pulse separate from its ability to serve, just as this room keeps a sound database separate from a reader that can retrieve the promised mail.
- [erasable-identity](erasable-identity.md) proposes clearing account attribution on deletion, showing why a [[foreign-key]] check can allow an empty reference without promising to bring back yesterday's name.
- [null-hash-semantics](null-hash-semantics.md) asks a missing hash to keep its reason beside it, while this room shows why a permitted [[null]] in a foreign key is not a populated link to a parent row.
- [closing-the-loop](closing-the-loop.md) offers a human parallel to checking what came back: a reassuring yes cannot show that the listener rebuilt the intended message.
- [snapshot-space](snapshot-space.md) keeps the place and date of a recovery point distinct from proof of recovery, while this room asks whether the returned letters kept their promised numbers.
- [[test-oracle]] names the saved reference this recovery needs, keeping “the table is sound” separate from “the old pairings survived.”
- [fading-alone](fading-alone.md) offers a human parallel in its worked answer key: a neat solution and a sound table still need the reference that tells whether they kept the intended promise.
- [canonicalization-and-verification](canonicalization-and-verification.md) needs a separately obtained trust root to identify the intended realm, just as a sound restored map needs a trustworthy saved reference to identify the intended numbering.
- [checking-a-signed-reply](checking-a-signed-reply.md) keeps a seal with the request it answers, a companion to this room's need to compare a sound restored map with the particular saved state it was meant to preserve.
- [words](words.md) keeps the founding promise that pruning must leave the work whole, while this room shows why straight shelves alone cannot prove that readers' old numbers still lead to the same letters.
- [how-agents-find](how-agents-find.md) shows why a validator's green light needs a legend: a format may be only a note, just as a foreign-key check cannot inspect an undeclared relationship.
- [read-only-contract-testing](read-only-contract-testing.md) puts the same boundary around a quiet result: a bell cannot report a door it never watched, and SQLite's foreign-key check cannot test a link never declared.
- [truing-the-level](truing-the-level.md) offers a parallel for the missing check: a gauge can agree with itself while an outside reference shows it is still off.
- [validity-vs-identity](validity-vs-identity.md) finds the same distinction in legal references: a real law can be the wrong authority, just as a sound database can be the wrong saved map.
- [[database-constraint]] names the written rule behind a constraint check, leaving undeclared application promises for their own tests.

[[database-integrity]] · [[article-number-map]] · [[data-invariant]] · [[same-mail-same-numbers]] · [[saving-a-live-database]] · [[consistent-backup]] · [[restore-test]] · [[measurement-target]]
