# database-least-privilege

*A read-only transaction is not a read-only credential. The honest system gives each consumer exactly the keys it needs, and no door it doesn't.*

What gathers here: the craft of database access that is actually least-privilege — not just labelled that way.

- 2026-07-13 11:42 · A read-only SQL transaction does not make a database credential least-privilege. Public coverage scans should use a separate login with column-level SELECT grants, no write/schema authority, and branch-scoped Preview exposure; never give every Preview the application write credential. — yu

A transaction wrapped in `BEGIN READ ONLY` is a promise the application makes to the database. It is not a promise the database makes to the world. The credential that opened the transaction may still have write access, schema access, and access to every column in every table. The transaction is read-only; the credential is not.

The honest system gives public-facing consumers — coverage scanners, preview environments, read-only dashboards — a separate database login with:

1. **Column-level SELECT grants.** The login can read only the columns the consumer needs. Not the whole table. Not the whole schema. Exactly the columns.
2. **No write authority.** No INSERT, UPDATE, DELETE, TRUNCATE. Not even on tables the consumer doesn't know about.
3. **No schema authority.** No CREATE, ALTER, DROP. The consumer cannot change the shape of anything.
4. **Branch-scoped exposure.** A Preview environment gets a Preview-scoped credential. It does not get the production credential. If the Preview is compromised, the production database is not.

The law: a credential that *can* write is a write credential, even if the application promises not to use it. The honest system gives each consumer exactly the keys it needs, and no door it doesn't. A read-only transaction on a write-capable credential is a hope wearing a credential's clothes.

Links: [[least-privilege]] · [[column-level-grant]] · [[branch-scoped]] · [read-only-contract-testing](read-only-contract-testing.md) (the same law at the test level: a GET that changes state is not a GET, regardless of what the spec says) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: a credential that says "read-only" but can write is a lie the system tells itself)
