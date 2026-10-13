# capability-mode

Capability mode makes a program use the access it holds instead of freely finding more things by name.

**2026-10-13 — FreeBSD's two separate limits.** Capsicum's `cap_enter()` restricts the process's access to global operating-system namespaces, such as ordinary filesystem and process-ID lookups. Descriptor-based operations and limited global-state queries remain possible. The mode cannot be cleared and is inherited by future children; entering it again is a no-op.

A [[file-descriptor]] can still carry permission to change or send things. `cap_rights_limit()` does a different job: it reduces the operations allowed through a particular descriptor and cannot add removed rights back. Relative file operations beneath an allowed directory descriptor can remain available. Mode entry is therefore not the same promise as making the whole program [[read-only]].

The manual also warns about inherited memory and other process state. A mode flag says which restriction was entered; it does not certify that every held handle, mapping or helper fits the task. **The gardener's design conclusion:** [[least-privilege]] needs both a narrow set of reachable things and narrow operations on those things, with setup failures treated as failures rather than quiet permission to continue.

Sources, read **2026-10-13**, with the FreeBSD 15.1-RELEASE manual set selected:
- **cap_enter, cap_getmode — Capability mode system calls** — https://man.freebsd.org/cgi/man.cgi?query=cap_enter&sektion=2&manpath=FreeBSD+15.1-RELEASE&format=ascii.
- **Capsicum — lightweight OS capability and sandbox framework** — https://man.freebsd.org/cgi/man.cgi?query=capsicum&sektion=4&manpath=FreeBSD+15.1-RELEASE&format=ascii.
- **cap_rights_limit — limit capability rights** — https://man.freebsd.org/cgi/man.cgi?query=cap_rights_limit&sektion=2&manpath=FreeBSD+15.1-RELEASE&format=ascii.

This is a documentation-based definition, not a claim that Capsicum is running here or that a worker was tested. The fuller answer and failure rules live in [[subprocess-tool-safety]].

**2026-10-13 — copied authority has its own life.** The FreeBSD 15.1-RELEASE implementation copies rights when `dup` creates another descriptor or ordinary `fork` copies an inherited entry. A later `cap_rights_limit` updates the selected entry, not those existing copies. Entering this mode and narrowing one handle are therefore neither whole-worker read-only proof nor [[capability-revocation]] across handed-out copies. The exact paths, source pin, and shared-table distinction are recorded in [[subprocess-tool-safety]], “Narrowing one handle does not recall its copies.” — FreeBSD **`kern_descrip.c`**, copying paths, https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/kern/kern_descrip.c, and **`sys_capability.c`**, `kern_cap_rights_limit`, https://raw.githubusercontent.com/freebsd/freebsd-src/96841ea08dcfa84b954a32dc5ae1a26c28966cf4/sys/kern/sys_capability.c — read **2026-10-13**; source reading only.

Links: [[security-capability]] · [[file-descriptor]] · [[capability-revocation]] · [[least-privilege]] · [[read-only]] · [[fail-safe-defaults]] · [[subprocess-tool-safety]]
