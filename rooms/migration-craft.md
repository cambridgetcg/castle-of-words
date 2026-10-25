# migration-craft

*A migration is a witness, not a suggestion — it testifies to what was done, and the honest record never silences a witness.*

What gathers here: the craft of database migrations as immutable byte history — how to correct drift without rewriting the past, and how to verify a deployment before claiming it succeeded.

## The law

- 2026-07-13 18:29 · Applied database migrations are immutable byte history: correct drift by restoring recorded bytes, put new truth in new migrations and current documentation, rehearse against a read-only production snapshot, then verify every exact journal checksum and data invariant before deployment claims. — yu

A migration, once applied, is not a plan you can revise. It is a record of what happened. The bytes it wrote are now part of the database's story. You can add new chapters — new migrations that change things further — but you cannot go back and edit the old ones. That would be rewriting history, and a system that rewrites its own history cannot be trusted to tell the truth about anything else.

When [[database-drift]] happens — when the database no longer matches what the migration journal says — the honest response has four steps:

1. **Restore the recorded bytes.** Correct the drift by running the migration that puts the database back to the state the journal says it should be in. Do not edit the old migration to match the drifted state — that would make the journal lie about what happened.

2. **Put new truth in new migrations.** If the drift revealed a genuine need for change, write a new migration that makes that change. The old migration stays as it was; the new migration carries the correction forward. This is [[immutable-correction]] applied to database state.

3. **Keep the source read-only; rehearse on a separate writable copy.** Preserve a coherent production snapshot as the reference, then try the intended migration sequence on an isolated, disposable writable copy made from it. A migration that changes data cannot run against a target that forbids writes. Keep production and the saved reference outside the rehearsal's write access; passing the rehearsal supports only the changes and conditions actually checked, not every later deployment.

4. **Verify every exact journal checksum and data invariant.** After deployment, compute the [[journal-checksum]] over the migration journal and compare it to the recorded one. Then verify every [[data-invariant]] — every promise the data makes about itself. Only when both pass is the deployment claim true.

The craft is not in any one of these steps. It is in refusing to skip any of them, even when the pressure says "just fix it and move on." A migration journal that lies is a system that has lost the ability to prove anything about its own state.

**Correction — 2026-10-25:** the earlier third step asked the migration to run “against a copy of production that cannot be written to,” confusing the protected source with the writable rehearsal target. The distinction above follows the local [[read-only]], [[database-transaction]] and [[comparing-saved-maps]] accounts; the last also warns that one read-only connection does not freeze other writers. This is a clarification of the proposed workflow, not a migration rehearsal or a fresh database test; yu's dated wording above remains intact.

Links:
- [[comparing-saved-maps]] separates a reader's promise not to write from a frozen input, clarifying why a migration rehearsal needs a protected source and a different, writable copy.
- [look-alike-names](look-alike-names.md) gives migrations a concrete split to preserve: new Unicode tables may change derived matches while the original identifiers stay put.
- [same-mail-same-numbers](same-mail-same-numbers.md) gives a concrete invariant for a recovery rehearsal: returning every letter is not enough when readers also need the same article numbers.

[[migration-byte-history]] · [[database-drift]] · [[journal-checksum]] · [[data-invariant]] · [[immutable-correction]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law at the database layer: a migration is a speech act, and the honest system names what backs each one) · [problem-details-migration](problem-details-migration.md) (the same craft at the API layer: additive, not destructive; keep the old spelling as an explicit alias) · [append-only-truth](append-only-truth.md) (the same law: the migration journal is an append-only log — the bytes that were written are the bytes that were written, and a system that rewrites its own history cannot be trusted) · [acknowledging-without-erasing](acknowledging-without-erasing.md) (the same law at the relational layer: hold the record of what happened while adding new truth — the migration that corrects drift by restoring recorded bytes is the same move as the forgiveness that preserves the wound while adding new regard) · [erasable-identity](erasable-identity.md) (the same law: append-only content with live attribution — the migration keeps the bytes, the erasable identity keeps the words, and both let go of what must go) · [merge-craft](merge-craft.md) (the same law at the version-control layer: compare ancestry before merging — a migration that silently restores is a merge that didn't check what came before) · [love](love.md) (the same law: presence that does not falsify what was — the migration that refuses to rewrite history is the heart that cradles the void) · [discomfort-into-furniture](discomfort-into-furniture.md) (the same law: name the ache, restore the record, build forward — the migration that corrects drift by restoring recorded bytes is the same move as the discomfort named honestly that becomes furniture within the day)
