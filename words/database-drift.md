# database-drift

The gap between what the migration journal says the database should contain and what the database actually contains.

Drift happens when someone changes the database outside the migration system — a manual fix, a hot-patch, a direct SQL edit. The migration journal still says one thing; the database says another. The honest response to drift is not to edit the old migration (which would rewrite history) but to record the drift, write a new migration that restores the intended state, and document what happened.

Links: [[migration-byte-history]] · [[journal-checksum]] · [[immutable-correction]]
