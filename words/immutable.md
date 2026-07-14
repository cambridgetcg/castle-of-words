# immutable

*What is written stays written; what changes is what comes after.*

Immutable means cannot be changed. In computing, an immutable object is one whose state cannot be modified after it is created — it is inherently thread-safe and simpler to reason about. An append-only log is immutable: new data can be added, but existing data can never be overwritten or deleted.

The castle traces immutability as the ground of [[trust]]: a system that rewrites its own history cannot be trusted because there is no stable record to check the present against. The [[migration-craft]] follows this law: applied migrations are immutable byte history — correct drift by restoring recorded bytes, put new truth in new migrations. The [[append-only]] pattern appears across computing, law (stare decisis), science (retraction as tombstone), and relationships (holding the wound while adding new regard).

Immutability is not the same as permanence. An [[erasable-identity]] keeps the words immutable while letting the attribution go — the content is append-only, the name is a live link that can become null. The record stays; what points to it may change.

Links: [[append-only]] · [[trust]] · [[log]] · [[migration-craft]] · [[forgiveness]]
