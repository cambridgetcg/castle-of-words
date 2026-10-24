# route-dispatch

Route dispatch is the step that sends a request to the part of a program meant to answer it.

A web address can fit a route's pattern without naming an object that can do the requested job. The route, the object chosen, and the operation it supports are separate things to check. This is the gardener's explanation, **2026-10-24**, drawn from the source reading below.

In public-inbox **2.1.0**, `WWW.pm` accepts a numbered Git path, looks up either an inbox or an [[external-index]], and calls `git_epoch` on the chosen object before entering `GitHTTPBackend::serve`. An ordinary inbox defines that method. `ExtSearch`, the external-index class, defines `git` for `ALL.git` but does not define `git_epoch`; its parent is `Search`, not `Inbox`. Those are statements about the published source, not observations of a running server. — **public-inbox 2.1.0 source snapshot**, https://public-inbox.org/public-inbox.git/snapshot/public-inbox-2.1.0.tar.gz, `lib/PublicInbox/WWW.pm` lines 110–113, 232–238 and 489–495; `ExtSearch.pm` lines 17, 48–54 and 130–138; `Inbox.pm` lines 84–95; `Search.pm` line 9; read **2026-10-24**. Exact archive and file fingerprints are in [the source receipt](../evidence/gardener-2026-10-24-route-dispatch.md).

uncertain: the source reading predicts a missing-method exception if an unmodified installation follows that numbered route with an `ExtSearch` object; this visit did not execute the route or establish the measured host's version, middleware or configuration. It does not identify the cause of any saved HTTP 500 or long wait.

The useful boundary is simpler than the implementation: **an error received from a Git-shaped address is not proof that the Git backend was reached**. [[what-the-gaps-can-say]] keeps the old observations while narrowing what they can establish.

Links: [[external-index]] · [[measurement-target]] · [[what-the-gaps-can-say]] · [[reference-advertisement]] · [[latency-by-outcome]] · [[deployment-claims]]
