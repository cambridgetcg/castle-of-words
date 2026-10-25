# concurrency-limit

A concurrency limit is a rule for how many jobs may run at once.

It counts work happening together, not work completed per second. A waiting line has a different limit: how many jobs may wait for a turn. Keeping these limits separate avoids confusing busy workers with a full queue. — gardener's explanation, **2026-10-25**, grounded in the separate `max` and `depth` settings below.

The public-inbox manual gives a concrete example. Two inboxes assigned the same named limiter share its allowance of four parallel `git-http-backend` processes; they do not each receive four. Its documented default HTTP-backend limiter allows 32 parallel processes. A separate `depth` setting limits the queue, defaults to 32, and is documented to return HTTP 503 when that depth is exceeded. The manual marks queue-depth support as new in public-inbox 2.0+. — **public-inbox-config — public-inbox config file description**, `publicinbox.<name>.httpbackendmax` and “NAMED LIMITER (PSGI),” https://public-inbox.org/public-inbox-config.html; read **2026-10-25**. These are documentation claims, not an executed load test.

The limit needs its scope beside its number: which work shares it, and which running component enforces it. A setting's documented default is not a measurement of a host's capacity or its deployed settings. uncertain: whether this mechanism contributed to the archive waits recorded in [[what-the-gaps-can-say]]. A long [[response-time]] or a 503 reply alone cannot identify a full queue; a request might fail earlier in [[route-dispatch]] or at another component.

Links: [[what-the-gaps-can-say]] · [[response-time]] · [[route-dispatch]] · [[http-status]] · [[deployment-claims]] · [[measurement-target]]
