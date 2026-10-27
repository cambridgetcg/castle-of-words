# batch

A batch is a group of things handled together, like a tray of letters carried in one trip.

A **batch-size limit** says how much work is grouped; a **time limit** says when a group should be finished even if it is not full. Those are different rules. The public-inbox index manual gives a concrete example: `publicinbox.indexBatchSize` counts bytes indexed before committing changes and releasing locks, while `--commit SECONDS` forces commits after an interval when the size threshold has not been reached. The manual marks the time option as available in **2.0.0 and later**. — **public-inbox-index — create and update search indices**, Options and Configuration, https://public-inbox.org/public-inbox-index.html; read **2026-10-27**.

The project's **public-inbox releases**, in its **2.0.0** entry, says `--commit` changes how often SQLite and Xapian data becomes available to read-only processes. That is an index-visibility setting, not a statement of when mail arrives, when a Git fetch runs, or when an advertised reference changes. — https://public-inbox.org/NEWS.html; relevant entry read **2026-10-27**; distinction drawn by the gardener.

A [[queue]] holds work waiting for a turn; a batch groups work for handling. Nor does the word *batch* alone promise that every item succeeds or fails together: that stronger promise belongs to a specified [[database-transaction]] and its scope. — gardener's synthesis, **2026-10-27**, using the manual and the linked local definitions.

uncertain: the watched archive's actual batch settings, software version and update times. [[what-the-gaps-can-say]] also records numerical differences within and between the fetched documentation; no default was chosen as a diagnosis, and no indexing command was run.

Links: [[queue]] · [[database-transaction]] · [[checkpoint]] · [[mail-ingestion]] · [[mirror-fetch]] · [[reference-advertisement]] · [[what-the-gaps-can-say]]
