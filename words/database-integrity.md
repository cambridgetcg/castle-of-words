# database-integrity

Database integrity means the saved pieces fit together and obey the rules being checked.

SQLite separates several checks. `integrity_check` examines storage structure, table-to-index consistency, and certain declared rules; `quick_check` skips uniqueness and index-to-table consistency; `foreign_key_check` separately tests declared links between tables. The first two return an `ok` row when no covered error is found, while the last returns a row for each violation and none when there are no violations. Those meanings assume a supported check that completed without an execution error. — SQLite, **Pragma statements supported by SQLite**, sections **PRAGMA integrity_check**, https://www.sqlite.org/pragma.html#pragma_integrity_check; **PRAGMA quick_check**, https://www.sqlite.org/pragma.html#pragma_quick_check; and **PRAGMA foreign_key_check**, https://www.sqlite.org/pragma.html#pragma_foreign_key_check; read **2026-10-11**.

Passing these checks is not proof that the saved work is the intended work. They do not compare an archive's current message numbers with its earlier [[article-number-map]], establish how fresh a backup is, or show that a reading service works. Those are separate promises for a [[restore-test]]. [[checking-a-restored-map]] holds the limits and the distinction between a whole-database check and a table-only check. — gardener's synthesis of the check definitions and the public-inbox mapping contract sourced in that room, **2026-10-11**.

No database was opened or tested to write this definition.

Links: [[checking-a-restored-map]] · [[data-invariant]] · [[article-number-map]] · [[consistent-backup]] · [[restore-test]] · [[measurement-target]]
