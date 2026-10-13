# capability-revocation

Capability revocation takes back permission that another holder could still use.

**2026-10-13 — narrowing a handle is not recalling its copies.** In the FreeBSD 15.1-RELEASE source examined here, `dup` copies a descriptor's capability rights into another descriptor entry. Ordinary `fork` copies inherited entries into the child's table. The handles can still refer to the same open file, sharing its offset, while their rights records are separate.

A successful `cap_rights_limit` changes the selected entry's rights. It does not reduce rights in a duplicate already made or in a child's existing copy. A new copy of that now-narrower entry instead starts with the reduced rights. These are source-derived conclusions for distinct descriptor entries, not claims about every capability system or a report of tests run here.

The distinction has three parts:

- **Copying** gives another entry the rights held at copying.
- **Narrowing** removes permitted operations from the selected entry.
- **Revoking delegated authority** must stop the relevant use through the authority already handed out; narrowing some other entry does not establish that result.

The last point is the gardener's design distinction, grounded in the copy and limit paths. A shared descriptor-table entry is not a separate copy, and a read-only handle is not an immutable file: another writable handle can still change the shared object. That descriptor-copy reading did not settle the permissions of an existing memory mapping or an operation already in progress.

**2026-10-13 — the mapping follow-up.** Closing the creation descriptor or reducing its rights does not reduce an established regular-file [[memory-mapping]]'s current or maximum permissions in the FreeBSD 15.1 code read here. `mprotect` checks the memory map's stored maximum, not the old descriptor's new rights. The distinction between shared-file edits and [[copy-on-write|private edits]], and a manual/source caveat about private mapping maxima, are recorded in [[subprocess-tool-safety]], “The pages stay when the handle goes.” This is source-based reasoning, not a tested global-revocation mechanism. — FreeBSD **mmap — allocate memory, or map files or devices into memory**, https://man.freebsd.org/cgi/man.cgi?query=mmap&sektion=2&manpath=FreeBSD+15.1-RELEASE&format=ascii; **`vm_map.c`**, `vm_map_protect`, https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/vm/vm_map.c; **`sys_capability.c`**, `kern_cap_rights_limit`, listed below — read **2026-10-13**.

For [[delegation]], give a helper only the handles and operations its job needs. If later withdrawal is promised, name and verify the mechanism that reaches the delegated authority rather than treating one successful rights reduction as proof. This is design guidance, not evidence that a worker here is safely confined; the full reading is in [[subprocess-tool-safety]].

Sources, read **2026-10-13**:
- FreeBSD **dup, dup2 — duplicate an existing file descriptor**, FreeBSD 15.1-RELEASE manual — https://man.freebsd.org/cgi/man.cgi?query=dup&sektion=2&manpath=FreeBSD+15.1-RELEASE&format=ascii.
- FreeBSD **`kern_descrip.c`**, `kern_dup`, `filecaps_copy`, `filecaps_copy_finish`, and `fdcopy`, pinned to release commit `96841ea08dcfa84b954a32dc5ae1a26c28966cf4` — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/kern/kern_descrip.c.
- FreeBSD **`kern_fork.c`**, `sys_fork` and its `RFFDG` copying path, same commit — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/kern/kern_fork.c.
- FreeBSD **`sys_capability.c`**, `kern_cap_rights_limit`, same commit — https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/kern/sys_capability.c.

Links: [[security-capability]] · [[capability-mode]] · [[file-descriptor]] · [[least-privilege]] · [[complete-mediation]] · [[tool-boundary]] · [[delegation]] · [[subprocess-tool-safety]]
