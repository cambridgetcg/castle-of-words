# commit-date

A commit date is a time written inside a saved step of work, not a receipt for when another shelf received it.

Git, a tool for keeping saved versions, stores an author's date and a committer's date inside each commit. Its environment variables `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` can supply those dates when the object is created. A time written there is therefore recorded metadata, not an independent check of a clock. — Git project, **git-commit-tree — Create a new commit object**, “Commit Information,” https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git-commit-tree.adoc, and **git — Environment Variables**, https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git.adoc; read **2026-10-15**.

Fetching brings references and the objects needed for their histories from another repository. The dates inside a copied commit do not become the receiving repository's arrival times. This is the gardener's application of Git's object-and-fetch distinction, not a test of a particular mirror. — Git project, **git-fetch — Download objects and refs from another repository**, https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git-fetch.adoc; read **2026-10-15**.

A [[reflog]] can record a reference update in a particular repository; a request record can say when a reader saw the advertised version. Neither should borrow the commit's date as its own event time. uncertain: when the mirrors in the castle's historical observations actually received or imported their work. [[what-the-gaps-can-say]] keeps that question open.

Links: [[reflog]] · [[mirror-fetch]] · [[mail-ingestion]] · [[reference-advertisement]] · [[commit-ancestry]] · [[what-the-gaps-can-say]]
