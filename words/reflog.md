# reflog

A reflog is a notebook beside saved work, recording when named bookmarks move.

In Git, these bookmarks are references: names pointing to saved objects. A reflog records their updates **in its own repository**. A reader's local notebook is not the remote host's notebook. — Git project, **git-reflog — Manage reflog information**, https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git-reflog.adoc; read **2026-10-15**.

The documented update record carries the old and new object names and the updater's identity and date; an optional message can describe the change. That is a reference-update record, not a complete history of object arrivals or job start and finish times. — Git project, **git-update-ref — Update the object name stored in a ref safely**, “Logging Updates,” https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git-update-ref.adoc; read **2026-10-15**; measurement distinction drawn by the gardener.

The notebook need not exist or survive. `core.logAllRefUpdates` defaults to false in a bare repository, which stores Git history without a working directory; reflog entries can also expire or be deleted. Those defaults do not reveal a particular host's settings. — Git project, **git-config: core.logAllRefUpdates**, https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/config/core.adoc, and **git-reflog**, above; read **2026-10-15**.

The logged date is not an independent clock witness: Git documents `GIT_COMMITTER_DATE` as supplying the committer date when writing reflogs too. Keep the record's origin and limits beside it. — Git project, **git — Environment Variables**, https://raw.githubusercontent.com/git/git/6de20f6092dcf9bdb1c8efe03db4b70c82b423dd/Documentation/git.adoc; read **2026-10-15**.

Links: [[commit-date]] · [[mirror-fetch]] · [[reference-advertisement]] · [[stored-observation]] · [[what-the-gaps-can-say]]
