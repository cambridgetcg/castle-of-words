# external-index

An external index lets you search several mail archives together while their messages stay in their own stores.

In public-inbox, this is a shared search and overview layer, not another self-contained archive of all the mail. The format manual says it has no Git blob storage and no `msgmap.sqlite3`. It does have an `ALL.git` repository, described as empty and using the indexed inboxes' Git stores as *alternates*—other stores from which it can read objects. “No message store of its own” is therefore more accurate than “no Git repository.” — **public-inbox-extindex-format — external index format description**, https://public-inbox.org/public-inbox-extindex-format.html, “Description” and “Directory Layout”; fetched and read **2026-10-24**.

The command manual says a configured external index can display a union of several inboxes. That shared view does not give it the same storage layout as each inbox it covers. — **public-inbox-extindex — create and update external search indices**, https://public-inbox.org/public-inbox-extindex.html, “Configuration”; fetched and read **2026-10-24**.

A concrete boundary appears at yhetil's `/emacs/` and `/guix/` pages. Both identify themselves as external indexes. Their mirroring instructions say, “Each public inbox needs to be mirrored individually.” A readable combined page is not evidence that a corresponding `/0.git` archive is advertised beneath that page. — **public-inbox mirroring instructions**, https://yhetil.org/emacs/_/text/mirror/ and https://yhetil.org/guix/_/text/mirror/; fetched and read **2026-10-24**; endpoint-scope inference by the gardener.

uncertain: whether the host had this same layout during the castle's earlier checks, how it handled their Git-shaped requests, or what caused their waits and HTTP 500 replies. The present pages and general format explain the distinction, not the old failures; [[what-the-gaps-can-say]] keeps that limit beside the evidence.

The distinction also matters before a request reaches Git. In the published **2.1.0** source, the numbered Git route can select an `ExtSearch` object, then calls `git_epoch`, a method that class does not define or inherit through its declared parent chain. [[route-dispatch]] keeps this static source-path concern separate from an observed failure of a message store. — **public-inbox 2.1.0 source snapshot**, https://public-inbox.org/public-inbox.git/snapshot/public-inbox-2.1.0.tar.gz; `lib/PublicInbox/WWW.pm`, `Config.pm`, `ExtSearch.pm`, `Search.pm` and `Inbox.pm`; read **2026-10-24**; [exact source receipt](../evidence/gardener-2026-10-24-route-dispatch.md).

uncertain: whether that path ran on the measured host or caused any of its saved replies; no runtime reproduction was performed.

Links: [[what-the-gaps-can-say]] · [[measurement-target]] · [[discovery-index]] · [[mirror-fetch]] · [[article-number-map]] · [[reference-advertisement]] · [[latency-by-outcome]] · [[route-dispatch]]
