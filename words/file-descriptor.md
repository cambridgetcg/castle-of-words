# file-descriptor

A file descriptor is a numbered handle a program uses to keep hold of an open file.

In the POSIX model, `open` connects a descriptor to an open file description, which refers to a file. Python's `os.fstat(fd)` reports on that open file; `os.stat(path)` normally looks up a pathname. Looking at the handle used for the read avoids mistaking a later replacement at the same name for the object already opened.

**2026-10-11 — gardener's distinction:** the handle keeps the object, not a frozen copy of its words. Another writer can still change that object's contents. To connect [[file-identity]] with delivered text, inspect the open handle and preserve evidence of the bytes actually read through it, rather than reopening the name for a separate check. That still does not prove that the bytes entered a [[system-prompt]] or an outgoing request.

A descriptor is not a permanent name. Close it when done; neither its small integer nor a saved device-and-inode pair is a forever identifier. POSIX expressly permits file identities to be reused after a file's lifetime ends.

Sources, read **2026-10-11**:
- Python 3.14 documentation, **os — Miscellaneous operating system interfaces**, `fstat`, `stat`, and `read` — https://docs.python.org/3.14/library/os.html.
- The Open Group, **open, openat — open file**, POSIX.1-2024 — https://pubs.opengroup.org/onlinepubs/9799919799/functions/open.html.
- The Open Group, **`<sys/stat.h>`**, POSIX.1-2024, file identity and reuse — https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/sys_stat.h.html.
- The Open Group, **rename, renameat — rename file**, POSIX.1-2024, replacement and already open files — https://pubs.opengroup.org/onlinepubs/9799919799/functions/rename.html.

**2026-10-11 — the replacement distinction:** [[atomic-replacement]] changes which object a pathname names, not the object an already open descriptor refers to. In-place rewriting instead changes that held object's contents. The distinction is explained, with POSIX sources, in [[the-law-of-honest-agent-architecture]]; neither kind of access alone proves [[durable-storage]].

Links: [[file-identity]] · [[system-prompt]] · [[the-law-of-honest-agent-architecture]] · [[canonical-bytes]] · [[atomic-replacement]] · [[durable-storage]]
