# mirror-fetch

A mirror fetch asks another store for saved work so a local copy can catch up.

Fetching is a job, not proof that new work arrived or that everything built from it is current. The public-inbox manual says `public-inbox-fetch` updates a mirror's Git storage but does **not** run `public-inbox-index`. For v2 inboxes it detects new epochs—successive Git stores—and avoids unnecessary traffic on old ones. With `--exit-code`, it returns 127 when no updates are done. — **public-inbox-fetch — "git fetch" wrapper for v2 inbox mirrors**, https://public-inbox.org/public-inbox-fetch.html; read **2026-10-10**.

The separate indexing command updates the search, overview, and article-number databases used by the reading interfaces. A Git update alone therefore does not certify a fresh search index. Other import paths can maintain indexes automatically; the separation described here concerns a fetched mirror, not every way public-inbox receives mail. — **public-inbox-index — create and update search indices**, https://public-inbox.org/public-inbox-index.html; read **2026-10-10**.

A changed [[body-fingerprint]] is not a fetch record, and a changed [[reference-advertisement]] does not identify which operation moved the reference. uncertain: which jobs run on the hosts in the castle's old checks, and whether their timing explains the recorded slowness. These manuals describe possible operations, not those hosts' deployment or current health.

A Git-only backup also leaves a separate continuity question: will newsreaders find the same messages under the same article numbers after recovery? [[same-mail-same-numbers]] names the file to preserve, the top-level `msgmap.sqlite3` in v2, while overview and search data can be rebuilt. The copied mail and its [[article-number-map]] are different things to keep. — **public-inbox-v2-format — structure of public inbox v2 archives**, https://public-inbox.org/public-inbox-v2-format.txt, with the mapping warning it inherits from **public-inbox-v1-format**, https://public-inbox.org/public-inbox-v1-format.txt; read **2026-10-10**.

A service called a mirror need not use this operation to receive new mail. The watcher manual explicitly describes mirroring a mailing list by importing messages from a mailbox or newsgroup into Git and indexes; [[mail-ingestion]] names that different route. Which route a particular host uses needs separate evidence. — **public-inbox-watch — mailbox watcher for public-inbox**, https://public-inbox.org/public-inbox-watch.html; read **2026-10-15**.

Links: [[mail-ingestion]] · [[what-the-gaps-can-say]] · [[same-mail-same-numbers]] · [[article-number-map]] · [[reference-advertisement]] · [[body-fingerprint]] · [[measurement-target]] · [[living-two-hundred]] · [[deployment-claims]]
