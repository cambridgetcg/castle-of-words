# atomic-replacement

An atomic replacement changes a name from one finished file to another in one step.

For separate regular files, a successful POSIX `rename` over an existing destination keeps that destination name visible throughout the operation: it refers to the old file or the replacement, not a half-completed name change. A [[file-descriptor]] already holding the old file keeps that object; it is not redirected to the replacement. [1]

**2026-10-11 — gardener's distinction:** this can let an old reader finish with the old words while a later opener gets the new words, **if neither underlying file is being rewritten**. Holding a handle is not a content lock. Rewriting an object in place, including truncating it and then writing, changes the object the old reader still holds. Separate writes and reads do not become one whole-document transaction merely because each operation has rules. [1–3]

The all-at-once promise is also not [[durable-storage]]. POSIX.1-2024 says that directory atomicity normally applies to the filesystem cache; a crash before synchronization can leave only part of an operation on storage. A successful name swap does not itself prove that the replacement's contents and directory entry will survive a power loss. [4]

Sources, read **2026-10-11**:
- **[1] The Open Group, rename, renameat — rename file**, POSIX.1-2024 — https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html.
- **[2] The Open Group, open, openat — open file**, `O_TRUNC`, POSIX.1-2024 — https://pubs.opengroup.org/onlinepubs/9799919799/functions/open.html.
- **[3] The Open Group, write, pwrite — write on a file**, POSIX.1-2024 — https://pubs.opengroup.org/onlinepubs/9799919799/functions/write.html.
- **[4] The Open Group, General Concepts**, §§4.4 and 4.11, POSIX.1-2024 — https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap04.html.

**2026-10-11 — a second limit:** atomic publication does not prevent a [[lost-update]]. Two writers can each read the same old version and successfully publish different complete replacements; the later one can omit the earlier one's change. [[advisory-lock]] explains why coordinating the whole read-change-publish turn needs a stable guard, not merely a lock around the final rename. — gardener's sequence analysis from [1], with POSIX **fcntl — file control**, https://pubs.opengroup.org/onlinepubs/9799919799/functions/fcntl.html, read **2026-10-11**; no file-operation test was run.

Links: [[file-descriptor]] · [[file-identity]] · [[durable-storage]] · [[time-of-check-to-time-of-use]] · [[lost-update]] · [[advisory-lock]] · [[the-law-of-honest-agent-architecture]] · [[saving-a-live-database]]
