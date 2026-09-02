# Advisory Locks Across Databases

*A trap that lives in one database's snapshot may not live in another's — but each has its own.*

What gathers here: whether the advisory-locks trap (a lock inside the same READ COMMITTED statement as a capacity check waking to a stale snapshot) is PostgreSQL-specific or shared across databases.

---

## PostgreSQL: the statement-level snapshot

PostgreSQL's READ COMMITTED isolation level takes a new snapshot at the start of *each statement* within a transaction (PostgreSQL docs, "Transaction Isolation", https://www.postgresql.org/docs/current/transaction-iso.html, read 2026-07-12). This means a lock acquired inside a statement that also reads a capacity value may see a stale snapshot — the lock was acquired, but the read that follows sees data from before the lock was granted. The trap is real and PostgreSQL-specific.

## MySQL: the transaction-level snapshot

MySQL's default REPEATABLE READ isolation level takes a snapshot at the start of the *first read statement* in a transaction and holds it for all subsequent consistent reads (MySQL docs, "InnoDB Transaction Isolation Levels", https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html, read 2026-07-12). This means a lock acquired mid-transaction does not see a stale snapshot — the snapshot was fixed before the lock. The PostgreSQL trap does not exist in MySQL's REPEATABLE READ. However, MySQL's READ COMMITTED (not the default) behaves similarly to PostgreSQL's, so the trap *could* exist there if explicitly configured.

## SQLite: the single-writer model

SQLite in WAL mode uses snapshot isolation: a read transaction sees an unchanging snapshot from the moment it started (SQLite docs, "Isolation In SQLite", https://www.sqlite.org/isolation.html, read 2026-07-12). There is no isolation between operations on the same database connection — they all see each other's changes immediately. The PostgreSQL trap does not exist in SQLite because there is no statement-level snapshot to go stale; the single-writer model means the lock and the read are serialized.

## The answer

The statement-level snapshot trap is PostgreSQL-specific. MySQL's default REPEATABLE READ avoids it by fixing the snapshot at transaction start. SQLite avoids it by having no statement-level isolation at all. Each database has its own footgun — the craft is knowing which one you are holding.

## Words

- [[advisory-lock]] — a lock that the application requests by name, not tied to a specific row or table
- [[transaction-isolation]] — the degree to which concurrent transactions see each other's changes
- [[read-committed]] — an isolation level where each statement sees a fresh snapshot

## Links

[[advisory-locks]] · [[fail-closed-boundaries]] · [[rate-limiting]] · [database-least-privilege](database-least-privilege.md) (the two halves of the same rule: the grant says what the credential is allowed to touch, and the lock inside the snapshot says what the statement is allowed to know — a privilege boundary and a time boundary, and an honest database holds both)
