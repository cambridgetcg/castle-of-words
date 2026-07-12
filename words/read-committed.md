# read-committed

The default PostgreSQL isolation level where each statement sees a fresh snapshot of committed data.

READ COMMITTED means a statement sees all rows committed before it began — but a long-running statement within a transaction may see a stale snapshot if it started before another transaction committed. This is the trap that advisory-lock describes: the lock is held, but the snapshot is old.

Links: [[advisory-lock]] · [[transaction-isolation]] · [[advisory-locks]]
