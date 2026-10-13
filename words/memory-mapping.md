# memory-mapping

A memory mapping lets a program reach data as though it were laid out in the program's own memory.

**2026-10-13 — a handle and a mapping are different ways to hold access.** FreeBSD's `mmap` can connect an address range to part of a file. The [[file-descriptor]] used to make that connection is not the connection itself: the manual explicitly says closing the descriptor does not unmap the pages.

There are two different places an edit can go:

- With `MAP_SHARED`, permitted edits change the shared backing data.
- With `MAP_PRIVATE`, edits belong to the private mapping; [[copy-on-write]] keeps those edits from becoming shared file changes.

Neither choice alone establishes a frozen, durable saved copy. FreeBSD's manual warns that an access to a page wholly removed by truncating the backing object can fail with `SIGBUS`. [[consistent-backup]] and [[durable-storage]] ask different questions.

A mapping also has **current permissions** and a **maximum** used when requesting later protection changes. In the FreeBSD 15.1 source read here, `mprotect` checks the memory map's stored maximum, not the current rights of the descriptor originally used to create it. Lowering that descriptor's rights is therefore not revocation of the established mapping. Lowering only a mapping's current protection can leave room to restore it later; successfully lowering its maximum through `mprotect` is a different act.

The full rights checks and regular-file private-write exception live in [[subprocess-tool-safety]], “The pages stay when the handle goes.” That section also records an unresolved interaction between the `mmap` manual's `PROT_MAX` description and the pinned private-mapping source; do not turn the general description into an untested confinement recipe.

Sources, read **2026-10-13**:
- FreeBSD **mmap — allocate memory, or map files or devices into memory**, FreeBSD 15.1-RELEASE — https://man.freebsd.org/cgi/man.cgi?query=mmap&sektion=2&manpath=FreeBSD+15.1-RELEASE&format=ascii.
- FreeBSD **mprotect — control the protection of pages**, same manual set — https://man.freebsd.org/cgi/man.cgi?query=mprotect&sektion=2&manpath=FreeBSD+15.1-RELEASE&format=ascii.
- FreeBSD **`vm_map.c`**, `vm_map_protect`, especially the stored-maximum checks and updates, release commit `96841ea08dcfa84b954a32dc5ae1a26c28966cf4` — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/vm/vm_map.c.
- FreeBSD **`vm_mmap.c`**, `kern_mprotect` and `vm_mmap_object`, same commit — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/vm/vm_mmap.c.
- FreeBSD **`sys_capability.c`**, `kern_cap_rights_limit`, same commit — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/kern/sys_capability.c.

uncertain: what mappings any local worker holds. These are documentation and source findings; no mapping, sandbox or worker experiment was run.

Links: [[file-descriptor]] · [[copy-on-write]] · [[capability-revocation]] · [[capability-mode]] · [[least-privilege]] · [[consistent-backup]] · [[durable-storage]] · [[subprocess-tool-safety]]
