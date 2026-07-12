# transaction-isolation

How much concurrent transactions can see of each other's uncommitted work.

The four standard levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable) trade consistency against concurrency. The trap in advisory-locks is that even Read Committed — the default — can show a stale snapshot to a waiter who acquired a lock inside the same statement as the check.

Links: [[read-committed]] · [[advisory-lock]] · [[advisory-locks]]
