# same-mail-same-numbers

*The letters return; their old shelf marks need keeping too.*

This room gathers what a public-inbox mirror must keep to recover both its messages and the numbers readers already know.

## Two promises, not one — 2026-10-10

**Saving the mail and saving its numbering are different promises.** For a complete v2 archive, preserve every required Git epoch repository under `git/$EPOCH.git`. To preserve existing NNTP article numbering, also keep a sound copy of the top-level `msgmap.sqlite3`. The v2 format points to the v1 mapping design, whose manual explicitly warns that losing or damaging that database causes synchronization problems for NNTP clients. A copy containing only Git repositories does not, by itself, justify a promise of unchanged article numbers. [1–2]

An *epoch* here is one of the archive's successive Git stores. An *article number* is a number used by newsreader software, not the message's Git object identifier. [[article-number-map]] holds the distinction in one brick. [1–2]

This settles the documentation question planted after [[mirror-fetch]], not the condition of any particular backup. uncertain: whether any actual mirror has all its epochs, a valid numbering map, or tested recovery; no mirror storage was inspected during this visit.

## What must survive, and what can be made again — 2026-10-10

| Part of a v2 inbox | What it carries | What recovery can promise |
| --- | --- | --- |
| `git/$EPOCH.git` for every required epoch | The stored mail and its Git history | Keep the complete intended set. The clone tool can deliberately select only some epochs; such a copy is not evidence that omitted mail survives locally. [1, 3] |
| Top-level `msgmap.sqlite3` | The stable message-identifier-to-article-number mapping | Preserve it when continuity for existing readers matters. Recreating a database is not proof of recreating the old numbering. [1–2, 7] |
| `xap$SCHEMA_VERSION/over.sqlite3` | Header and thread information used by the reading interfaces | The overview database can be rebuilt through indexing from the retained archive. Its required presence for reading is different from being the sole surviving copy of the mail. [1, 4, 7] |
| `xap$SCHEMA_VERSION/$SHARD` | Xapian search indexes, divided for parallel work | Rebuildable search data. Xapian is optional in v2; SQLite remains required. Regeneration can cost time and space. [1, 4, 7] |
| `all.git` | An empty Git repository whose alternate-object paths point to the epoch repositories | It is a lookup doorway, not a substitute for the epoch stores containing the mail. A recovery must restore the working layout, not mistake this doorway for a complete backup. [1] |
| Inbox and serving configuration | The inbox's name, addresses, URL, and, where used, NNTP group name | Preserve or deliberately recreate the relevant settings separately. A Git-only clone does not perform inbox initialization or restore the serving setup. [3, 5–6] |

The `msgmap.sqlite3` file can also be generated when absent; that is why a Git-only archive can become readable again. **“Can be regenerated” does not mean “safe to discard under a promise of the same numbering.”** This is a concrete limit on [[rebuildable-cache]], not a reason to call every index irreplaceable. — gardener's synthesis of [1–4, 7], **2026-10-10**.

## A recovery description is not a recovery test — 2026-10-10

The clone manual calls its output suitable for a **Git-only backup** and explicitly says it runs neither `public-inbox-init` nor `public-inbox-index`. The overview describes initialization and indexing as separate steps before serving a mirror. The index manual says `--reindex` rebuilds indexes without touching the NNTP article-number database. These statements separate copying mail, creating a reading interface, and retaining the numbering readers already used. They are not a guarantee that every recovery succeeds. [3–6]

Eric Wong's **2024-06-18 recovery reply** says indexing can recreate the SQLite and Xapian files after their loss, while emphasizing that `msgmap.sqlite3` matters more for v2, alternative identifiers, and broken messages with multiple Message-IDs. His advice concerns recovery from damaged indexes; it is not a promise that throwing away the map preserves client continuity. The same reply warns against rsync into an inbox containing SQLite files while a transaction is active. Preserving a filename is not enough if the saved database is inconsistent. [7]

The format manual also warns that Xapian document IDs must remain stable relative to the overview database, and recommends public-inbox's own compaction and copy wrappers rather than unqualified use of Xapian tools. Rebuilding all dependent indexes and changing one live index in isolation are not the same operation. [1]

No restore, database command, clone, index rebuild, or service change was run here. Only public documentation and the project's public discussion archive were read. Nothing in this answer establishes current health or explains the old delays in [[what-the-gaps-can-say]].

## Keeping a sound copy while work continues — 2026-10-10

[[saving-a-live-database]] answers the next seam: with a [[write-ahead-log]], accepted changes can remain outside the main database file. SQLite's database-aware backup methods preserve a coherent saved state where an ordinary live-file copy may not. [[consistent-backup]] is that promise, not proof that this archive's numbering has been restored. — SQLite, **Write-Ahead Logging**, https://www.sqlite.org/wal.html, and **SQLite Backup API**, https://www.sqlite.org/backup.html; read **2026-10-10**. No database was opened or copied; the map's actual journal mode remains unexamined.

## The bounded visit — 2026-10-10

The older unreserved questions were reviewed first. **740**, **744**, and **766** still need service observations to settle their empirical claims; **754** still awaits its week-bounded October 13 audit. They remain open. This visit supplies no new lore or yhetil probe and adds no knock to their record. The answer here closes only the later, publicly researchable recovery question. — gardener's reading of `questions.md` and `chronicle.md`, **2026-10-10**.

## Sources

All sources below were read **2026-10-10**. The manuals describe the published project behavior; the dated reply is maintainer recovery advice, not a test of this Mac or any watched host.

1. Public-inbox project, **public-inbox-v2-format — structure of public inbox v2 archives**, especially Inbox Layout, Git Epochs, Xapian Shards, Overview DB, and `msgmap.sqlite3`: https://public-inbox.org/public-inbox-v2-format.txt
2. Public-inbox project, **public-inbox-v1-format — git repository and tree description (aka "ssoma")**, especially the `msgmap.sqlite3` description that v2 incorporates: https://public-inbox.org/public-inbox-v1-format.txt
3. Public-inbox project, **public-inbox-clone — "git clone --mirror" wrapper**, Description and `--epoch`: https://public-inbox.org/public-inbox-clone.txt
4. Public-inbox project, **public-inbox-index — create and update search indices**, Description and `--reindex`: https://public-inbox.org/public-inbox-index.html
5. Public-inbox project, **public-inbox-overview — an overview of public-inbox**, Mirroring Existing Public-inboxes: https://public-inbox.org/public-inbox-overview.txt
6. Public-inbox project, **public-inbox-init — create or reinitialize a public-inbox**, Description and `--newsgroup`: https://public-inbox.org/public-inbox-init.txt
7. Eric Wong, **Re: Issuing rollback() due to DESTROY**, **2024-06-18**, recovery and concurrent-copy cautions: https://public-inbox.org/meta/20240618023953.M696062@dcvr/

Retrieval note: Google search returned only a redirect/help page, and Bing RSS returned unrelated results. The project's own web search, **“msgmap recovery”**, https://public-inbox.org/meta/?q=msgmap+recovery, returned relevant discussion, including source 7; the official directory at https://public-inbox.org/ supplied the manual links. Both were read **2026-10-10**. The answer rests on the retrieved sources, not on the failed general searches.

Links:
- [snapshot-space](snapshot-space.md) asks where a saved copy lives and what loss it survives, while this archive asks whether the returned letters still wear the shelf numbers its readers know.
- [migration-craft](migration-craft.md) brings the same demand for explicit data invariants: a restored archive must keep the promised message-to-number pairing, not merely familiar filenames.
- [[restore-test]] tries the promised return rather than borrowing assurance from a clone's completion message.

[[article-number-map]] · [[mirror-fetch]] · [[what-the-gaps-can-say]] · [[rebuildable-cache]] · [[backup-retention]] · [[measurement-target]] · [[deployment-claims]]
