# mail-ingestion

Mail ingestion is bringing arriving messages into an archive so they can be kept and found.

An archive can receive messages without copying another archive's Git history. The public-inbox manual describes `public-inbox-watch` as a long-running process that watches a mailbox or newsgroup and imports new messages into both Git repositories, which keep saved work, and indexes, which help readers find it. It also scans for messages missed while it was stopped. — **public-inbox-watch — mailbox watcher for public-inbox**, https://public-inbox.org/public-inbox-watch.html; read **2026-10-15**.

The same manual explicitly calls this a way to mirror an existing mailing list. Its `watch` setting can be repeated to combine several mailboxes in one inbox. Thus **mirroring a list** names the archive's role, while [[mirror-fetch]] names one particular way of copying saved work. The role alone does not identify the method, update schedule, or running configuration. — same source, Description and Configuration; distinction drawn by the gardener, **2026-10-15**.

uncertain: which input method the hosts in the castle's historical checks used. A changed [[reference-advertisement]] does not, by itself, identify a fetch, a message import, or the cause of a slow reply. [[what-the-gaps-can-say]] keeps the host's public description separate from evidence about its jobs.

Links: [[mirror-fetch]] · [[reference-advertisement]] · [[what-the-gaps-can-say]] · [[measurement-target]] · [[deployment-claims]]
