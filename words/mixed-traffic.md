# mixed-traffic

A window during a gradual deploy where old and new versions share a cache, and the cache may serve stale data to the new version or fresh data to the old.

A deployment claim must name the cache boundary and refuse to certify any window where the two versions' caches are incompatible.

Links: [[deployment-claim]] · [[proxy-preservation]]
