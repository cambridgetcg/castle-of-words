# advisory-lock

An advisory lock is a turn-taking rule that protects work only when everyone changing it agrees to use the same lock.

The existing PostgreSQL case follows; advisory locking is not limited to databases. — gardener's clarification from POSIX.1-2024, read **2026-10-11**: **The Open Group, fcntl — file control**, https://pubs.opengroup.org/onlinepubs/9799919799/functions/fcntl.html.

An advisory lock acquired inside the same READ COMMITTED statement as a capacity check can resume with the statement's old snapshot — the waiter sees the world as it was when the statement began, not as it is after the winner committed. The fix: acquire the transaction-level lock in one statement, then run the check-and-insert in a second statement, so the waiter sees the winner's committed row.

**2026-10-11 — file case:** POSIX `fcntl` record locks coordinate cooperating processes, not just database queries. A writer can lock a stable companion before opening and reading a replaceable document, then keep the lock through its change and publication. Locking the destination itself risks splitting writers across old and new objects after a rename. For process-owned locks, closing any descriptor for the companion in that process releases its locks on that file; process termination releases them too. The full ownership and cleanup limits live in [[the-law-of-honest-agent-architecture]]. — **The Open Group, fcntl — file control**, https://pubs.opengroup.org/onlinepubs/9799919799/functions/fcntl.html, and **rename, renameat — rename file**, https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html, POSIX.1-2024, read **2026-10-11**; stable-companion sequence is the gardener's synthesis, not a local test.

Links: [[read-committed]] · [[transaction-isolation]] · [[advisory-locks]] · [[lost-update]] · [[file-identity]] · [[atomic-replacement]] · [[the-law-of-honest-agent-architecture]]
