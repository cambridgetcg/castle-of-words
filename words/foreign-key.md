# foreign-key

A foreign key is a table rule that checks whether a reference points to a key the database knows.

The reference uses one or more columns, and its target is a key in a table, not proof of a person's real-world identity. In the SQLite rules recorded in [[checking-a-restored-map]], a child reference with a null key column can satisfy the foreign-key rule without naming a parent row. Requiring a filled-in reference is a separate [[database-constraint]]. A clean check can therefore leave a blank place on the page.

Declaring the rule, enforcing it during writes, and checking stored rows are separate acts. SQLite's `foreign_key_check` examines declared relationships; it does not compare the data with yesterday's saved map. A valid reference can point to a different permitted row, so [[database-integrity]] does not by itself establish historical fidelity.

[[erasable-identity]] proposes clearing account attribution when an account is deleted. That is a chosen deletion policy, not something every foreign key does. Clearing the reference does not establish that retained text or other identifiers are anonymous; the empty link says less than the whole privacy claim.

Sources: [[checking-a-restored-map]], especially “Three checks, three boundaries,” and [[erasable-identity]], read locally **2026-10-21**. The SQLite claims follow the first room's cited **SQLite Foreign Key Support**, https://www.sqlite.org/foreignkeys.html, and **PRAGMA foreign_key_check**, https://www.sqlite.org/pragma.html#pragma_foreign_key_check, read there **2026-10-11**. This brick distills the local notes; no web source was fetched again and no database or deletion policy was tested.

Links:
- [[database-constraint]] names the wider family of rules a table is asked to keep.
- [[null]] marks the empty place without explaining how it became empty.
- [checking-a-restored-map](../rooms/checking-a-restored-map.md) keeps a valid relationship separate from the old relationship we meant to recover.
- [erasable-identity](../rooms/erasable-identity.md) separates kept words from attribution that its proposed deletion policy clears.
