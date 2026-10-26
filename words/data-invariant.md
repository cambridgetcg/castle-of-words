# data-invariant

A rule the data must keep when it changes.

The rule belongs to a named system and must say when it holds. An application might require every order to identify an existing customer, or a recovery might promise that messages keep their saved article numbers. State the promise, then check the resulting data; a matching migration journal cannot perform that check for us.

A [[database-constraint]] can express some of these rules, not every application promise. SQLite permits a [[foreign-key]] to satisfy its rule when one or more child-key columns is [[null]]; requiring a populated reference is a separate condition. Even a sound database with valid declared links can contain the wrong historical message-number pairs.

Scope correction — **2026-10-26**: the earlier examples made every foreign key sound like a populated link and every balance sound necessarily nonnegative; those are not universal rules. This clarification uses the local [checking-a-restored-map](../rooms/checking-a-restored-map.md) and [migration-craft](../rooms/migration-craft.md), read on this date; the former records SQLite's foreign-key rules and the latter separates journal checks from data promises. Their external sources were not fetched again, and no database was tested.

Links:
- [checking-a-restored-map](../rooms/checking-a-restored-map.md) shows why sound shelves still need a check that each letter kept its promised number.
- [migration-craft](../rooms/migration-craft.md) keeps the journal's byte history and the resulting data's promises as separate checks.
- [[journal-checksum]] · [[migration-byte-history]] · [[zero-row-invariant]]
