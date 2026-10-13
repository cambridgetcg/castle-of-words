# copy-on-write

Copy-on-write lets copies share unchanged data and gives a writer its own part to change.

**2026-10-13 — changing a private copy is not changing its source.** In a private file [[memory-mapping]], the program's edits are private rather than shared back into the file. FreeBSD's regular-file mapping path permits this private writing separately from the permission to write the shared file. Having no file-writing right does not mean a program cannot work on its own private data.

The pinned FreeBSD source marks a non-anonymous, non-shared file mapping with `MAP_COPY_ON_WRITE`. Its protection-changing code describes the usual delayed work on private pages, with an immediate-copy exception when upgrading certain pages kept in physical memory. The name describes a copying strategy, not a promise that no copying ever happens until an ordinary write.

The boundary matters for [[read-only]] and [[least-privilege]]: specify whether the protected thing is the source file, the private working data, or some other state. Private edits alone do not establish a durable [[consistent-backup]] or freeze the original file. The complete source reading is in [[subprocess-tool-safety]], “The pages stay when the handle goes.”

Sources, read **2026-10-13**:
- FreeBSD **mmap — allocate memory, or map files or devices into memory**, `MAP_PRIVATE` and `MAP_SHARED`, FreeBSD 15.1-RELEASE — https://man.freebsd.org/cgi/man.cgi?query=mmap&sektion=2&manpath=FreeBSD+15.1-RELEASE&format=ascii.
- FreeBSD **`vm_mmap.c`**, `vm_mmap_object`, lines 1608–1631, release commit `96841ea08dcfa84b954a32dc5ae1a26c28966cf4` — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/vm/vm_mmap.c.
- FreeBSD **`vfs_vnops.c`**, `vn_mmap`, especially lines 3102–3116, same commit — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/kern/vfs_vnops.c.
- FreeBSD **`vm_map.c`**, `vm_map_protect`, private-mapping reservation at lines 2912–2917 and copying exception at lines 3006–3015, same commit — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/vm/vm_map.c.

These statements describe the published code; no memory-mapping experiment was performed.

Links: [[memory-mapping]] · [[file-descriptor]] · [[read-only]] · [[least-privilege]] · [[consistent-backup]] · [[subprocess-tool-safety]]
