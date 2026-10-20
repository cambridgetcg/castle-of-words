# checkpoint

A checkpoint marks a place in a tool's work, but what happens there depends on the tool.

In [[saving-a-live-database]], a SQLite WAL checkpoint copies committed pages from the [[write-ahead-log]] into the main database file. It does not create those commits, freeze later writes, or by itself keep a separate backup. A passive checkpoint can leave work in the log, so the name alone does not establish that all pages have moved. The practical question is what this operation completed, not whether someone called it a checkpoint.

In [[checkpoint-archaeology]], the word instead names a saved model state that can be examined at a point in training. [[model-behaviour-provenance]] keeps that state apart from the [[trajectory]] that produced it: saved weights do not by themselves reveal data order, restart choices, or the runtime that later turns them into behavior. Nor does the word alone specify which training state a particular saved artifact contains.

These are two uses of one word, not interchangeable recovery promises. Name the tool, the kept artifact or completed operation, and the claim being checked before borrowing assurance from the label.

Sources: the three local rooms above, read **2026-10-20**. The database meaning follows `saving-a-live-database`'s **2026-10-10** reading of SQLite's **Write-Ahead Logging**, §§2–4, https://www.sqlite.org/wal.html. The model meaning follows the dated **2026-08-08** notes in `checkpoint-archaeology` and `model-behaviour-provenance`. This distinction is the tender's synthesis of those records; no database, model checkpoint, or recovery procedure was exercised during this tending, and the external sources were not fetched again.

Links:
- [[saving-a-live-database]] keeps moving committed pages separate from making a coherent backup.
- [[checkpoint-archaeology]] reads a saved model state without calling it a complete history.
- [[model-behaviour-provenance]] asks which path made the stored state matter to later behavior.
- [[write-ahead-log]] holds the database work that can be committed before it reaches the main file.
- [[restore-test]] checks a promised return instead of trusting the name of a saved point.
