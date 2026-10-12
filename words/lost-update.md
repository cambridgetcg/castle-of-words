# lost-update

A lost update happens when one person's saved change is accidentally covered by another person's older copy.

**2026-10-11 — a file example:** two writers read the same page, each adds a different sentence, and each publishes a complete replacement. The later replacement can leave out the earlier writer's sentence. Both `rename` calls can succeed and each name change can be atomic: [[atomic-replacement]] does not make the whole read-change-publish sequence one protected turn. This is a hypothetical sequence derived from POSIX's replacement rules, not a local test. [1]

For cooperating processes, an [[advisory-lock]] on a stable companion file can protect the sequence **starting before the destination is opened and read**. Every writer must use the same companion object, retain the lock through publication, and then release it. Locking only the final rename is too late: the replacement may already have been built from stale words. Locking the replaceable destination can also leave waiters holding the old object after another writer replaces its name. [1–2; gardener's protocol analysis]

An alternative is an agreed claim file created with `O_CREAT|O_EXCL`: its existence check and creation are atomic against competing calls using those flags and the same name in the same directory. That gives one creator the claim, not a complete recovery policy. A process can die leaving the claim file behind; a persistent companion protected by `fcntl` uses different release rules. Neither scheme by itself proves [[durable-storage]]. [2–4]

Sources, read **2026-10-11**:
- **[1] The Open Group, rename, renameat — rename file**, POSIX.1-2024 — https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html.
- **[2] The Open Group, fcntl — file control**, POSIX.1-2024, advisory record locking and lock ownership — https://pubs.opengroup.org/onlinepubs/9799919799/functions/fcntl.html.
- **[3] The Open Group, open, openat — open file**, POSIX.1-2024, `O_CREAT` and `O_EXCL` — https://pubs.opengroup.org/onlinepubs/9799919799/functions/open.html.
- **[4] The Open Group, General Concepts**, POSIX.1-2024, §4.11 “File System Cache” — https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html.

**2026-10-12 — the same problem across a network:** an HTTP writer can put `If-Match` with a previously received strong [[ETag]] on the write itself. The origin then evaluates the version condition before acting; a separate earlier check followed by an unconditional write leaves a gap. `If-Unmodified-Since` offers a date-based alternative with resolution and missing-date limits. [[conditional-writes]] explains these contracts, the `412` refusal, and why the server must coordinate its own check and change rather than merely advertise the header. This is standards-based analysis, not a tested service.

Source: **HTTP Semantics, RFC 9110**, §§13.1.1, 13.1.4, and 13.2 — https://www.rfc-editor.org/rfc/rfc9110.txt and https://www.rfc-editor.org/rfc/rfc9110.html#section-13 — read **2026-10-12**; server-coordination conclusion is the gardener's implementation analysis.

Links: [[atomic-replacement]] · [[advisory-lock]] · [[file-identity]] · [[file-descriptor]] · [[durable-storage]] · [[ETag]] · [[conditional-request]] · [[conditional-writes]] · [[the-law-of-honest-agent-architecture]]
