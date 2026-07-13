# migration-byte-history

A database migration, once applied, is a permanent record of the exact bytes that changed the database — not a suggestion, not a plan, but history that cannot be unwritten.

When a migration runs, it writes bytes to the database. Those bytes are now part of the database's story. You can add new migrations that change things further, but you cannot erase what the first migration did. Treating applied migrations as immutable byte history means: never edit a migration that has already run, never pretend a drift didn't happen, and always put corrections in new migrations that build on the recorded past.

Links: [[database-drift]] · [[journal-checksum]] · [[immutable-correction]]
