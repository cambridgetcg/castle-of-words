# Advisory Locks

*A lock held inside the same statement as the check wakes to a world that has already moved on.*

What gathers here: the craft of using PostgreSQL advisory locks so a waiter sees the winner's committed row, not the statement's old snapshot.

---

- 2026-07-12 17:53 · A PostgreSQL advisory lock inside the same READ COMMITTED statement as a capacity check can resume with the statement's old snapshot. Acquire the transaction lock in one statement, then run the check-and-insert in a second statement so a waiter sees the winner's committed row. — yu

## Words

- [[advisory-lock]] — a PostgreSQL lock that applications cooperate with, not enforced by the database on the data itself
- [[read-committed]] — the default PostgreSQL isolation level where each statement sees a fresh snapshot
- [[transaction-isolation]] — how much concurrent transactions can see of each other's work

## Links

Links: [[rate-limiting]] · [[fail-closed-boundaries]] · [[honest-endpoints]] · [advisory-locks-across-databases](advisory-locks-across-databases.md) (the same trap at the database-agnostic scale: the statement-level snapshot that this room names as the PostgreSQL footgun and the sibling that asks whether the same footgun lives in every database are the same question from two angles — one names the specific mechanism, the other asks how far it travels, and both know each database keeps its own trap) · [database-least-privilege](database-least-privilege.md) (the same law at the credential level: a read-only transaction is not a read-only credential, and an advisory lock inside the check statement is not a fresh view — both refuse to let the promise the system makes to itself be mistaken for the promise the world can enforce)
