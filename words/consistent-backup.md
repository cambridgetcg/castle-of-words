# consistent-backup

A consistent backup keeps pieces of saved work that belong together, rather than mixing incompatible moments.

For one SQLite database, this means a coherent committed state. SQLite documents its Online Backup API, `VACUUM INTO`, and `sqlite3_rsync` as ways to obtain such a copy from a live database. They differ in how the snapshot is taken and what physical details are preserved; they are not interchangeable promises of byte identity. — SQLite, **How To Corrupt An SQLite Database File**, §1.2, https://www.sqlite.org/howtocorrupt.html; **SQLite Backup API**, https://www.sqlite.org/backup.html; **VACUUM**, https://www.sqlite.org/lang_vacuum.html; **Database Remote-Copy Tool For SQLite**, https://www.sqlite.org/rsync.html; all read **2026-10-10**.

Consistency is not freshness forever. Nor does a coherent copy of one database prove that a separate archive and its configuration match it, that every later change was included, or that a restore has succeeded. Name the saved state and the application's needed relationships, then test the promised return. — gardener's synthesis of those sources and [[restore-test]], **2026-10-10**.

[[saving-a-live-database]] holds the concrete limits, including why successful API cleanup is not proof that the copying completed. No backup or restore was performed to write this definition.

Links: [[saving-a-live-database]] · [[write-ahead-log]] · [[restore-test]] · [[same-mail-same-numbers]] · [[article-number-map]] · [[measurement-target]]
