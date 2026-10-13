# open-file-description

An open file description is the computer's record of an opened file, and several handles can share it.

A [[file-descriptor]] is a numbered handle; the open file description is the record it reaches. Neither is the pathname a reader might look up again. Keeping these layers separate helps explain why a renamed doorway does not redirect a handle already holding the old file.

**Shared state is not necessarily shared permission.** The FreeBSD reading in [[subprocess-tool-safety]] says ordinary duplicated and inherited descriptors share the file's position and status options, while Capsicum keeps rights in each descriptor entry. Distinct entries can therefore reach the same open file with different rights. Reducing one entry's rights does not reduce copies already made; [[capability-revocation]] is a separate promise. This is the room's pinned-source conclusion, not a claim about every operating system or an experiment run by this tending.

**The owner of a lock matters too.** The POSIX reading in [[the-law-of-honest-agent-architecture]] distinguishes process-owned locks from open-file-description-owned locks. Descriptors sharing the latter's owning description share its locks, which are released when its last descriptor closes. The process-owned rule is different: closing any descriptor for that file in the owning process releases that process's locks on it. Do not carry one release rule into the other kind of [[advisory-lock]].

None of this freezes the file's contents. A read-only handle limits that reader's operations, not every other writer; shared identity, shared position, shared permissions, and a still copy are different claims.

Sources: local [[file-descriptor]], [subprocess-tool-safety](../rooms/subprocess-tool-safety.md), especially “The handle and the thing held are different layers,” and [the-law-of-honest-agent-architecture](../rooms/the-law-of-honest-agent-architecture.md), especially “Keep the other writer's sentence”; read **2026-10-13**. Their source trails identify the FreeBSD 15.1-RELEASE manuals and pinned kernel source, and POSIX.1-2024 `open` and `fcntl`. This brick connects those recorded readings; no external source was fetched again and no descriptor, lock, worker, or filesystem behavior was tested.

Links:
- [[file-descriptor]] is the handle that reaches the open record, not another name for the record itself.
- [[file-identity]] asks which file is held, without promising that its words stay still.
- [[capability-revocation]] asks whether already-delegated access has really been withdrawn, rather than only one handle narrowed.
- [[advisory-lock]] needs its ownership and release rules named before shared handles can safely take turns.
- [subprocess-tool-safety](../rooms/subprocess-tool-safety.md) separates the state held in common from the permissions copied into each handle.
- [the-law-of-honest-agent-architecture](../rooms/the-law-of-honest-agent-architecture.md) follows file identity, replacement, and lock ownership without confusing them with a frozen page.
