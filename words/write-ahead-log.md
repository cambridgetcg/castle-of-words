# write-ahead-log

A write-ahead log keeps new changes beside a database before they are folded into its main file.

In SQLite's WAL mode, a transaction can be committed — accepted as a unit — by appending a commit record to the log without changing the main database file. Readers combine the appropriate pages from the main file and the log. A **checkpoint** later moves committed log content into the main file. Committed does not mean checkpointed. — SQLite, **Write-Ahead Logging**, §§2–2.2, https://www.sqlite.org/wal.html; read **2026-10-10**.

The file usually ends in `-wal`. It is part of the database's persistent state: separating it from the main file can lose accepted changes or corrupt the database. Copying both files at unrelated moments while they change is not a substitute for a coordinated backup. — SQLite, **Write-Ahead Logging**, §4, above, and **How To Corrupt An SQLite Database File**, §§1.2–1.4, https://www.sqlite.org/howtocorrupt.html; read **2026-10-10**; final sentence is the gardener's synthesis.

[[saving-a-live-database]] names the documented ways to make a consistent copy. This definition does not claim that any particular local database uses WAL; none was inspected.

Links: [[saving-a-live-database]] · [[consistent-backup]] · [[article-number-map]] · [[transaction-isolation]] · [[restore-test]]
