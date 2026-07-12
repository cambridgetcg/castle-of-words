# fail-closed

A system that denies access when it cannot confirm permission, rather than granting by default.

The opposite of fail-open. A fail-closed gate says "no" when its own machinery is uncertain — the database is unreachable, the secret is missing, the check times out. This is the safer default for security boundaries, but it means the system's availability depends on its dependencies. The craft is knowing which gates must be fail-closed (authentication, authorization) and which may be fail-open (analytics, non-critical features).

Links: [[rate-limiting]] · [[route-guard]] · [[fail-closed-boundaries]]
