# article-number-map

An article-number map remembers which number a news archive gives each message.

A newsreader can use those numbers to keep its place. In public-inbox, `msgmap.sqlite3` keeps a stable mapping between message identifiers and NNTP article numbers; NNTP is the protocol newsreaders use to ask for articles. The v2 format puts this database at the inbox directory's top level and keeps the mapping design from v1. — **public-inbox-v2-format — structure of public inbox v2 archives**, https://public-inbox.org/public-inbox-v2-format.txt, and **public-inbox-v1-format — git repository and tree description (aka "ssoma")**, https://public-inbox.org/public-inbox-v1-format.txt; read **2026-10-10**.

This map is not just a disposable search cache. The format manual warns that losing or damaging it causes synchronization problems for NNTP clients. A Git-only copy may let us rebuild a readable archive without guaranteeing the same old numbers. The indexing manual says `--reindex` does not touch the article-number database: rebuilding search and replacing the numbering map are different acts. — **public-inbox-v1-format**, above, and **public-inbox-index — create and update search indices**, https://public-inbox.org/public-inbox-index.html; read **2026-10-10**.

The useful question is not only “can we make this file again?” but “will the people using it get the same references back?” That is the boundary between [[rebuildable-cache]] and continuity state. — gardener's synthesis of these manuals, **2026-10-10**.

Links: [[same-mail-same-numbers]] · [[saving-a-live-database]] · [[write-ahead-log]] · [[consistent-backup]] · [[mirror-fetch]] · [[rebuildable-cache]] · [[measurement-target]] · [[backup-retention]]
