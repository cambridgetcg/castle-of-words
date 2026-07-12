# advisory-lock

A PostgreSQL lock that applications cooperate with — the database enforces the lock, but only if every query asks for it by name.

An advisory lock acquired inside the same READ COMMITTED statement as a capacity check can resume with the statement's old snapshot — the waiter sees the world as it was when the statement began, not as it is after the winner committed. The fix: acquire the transaction-level lock in one statement, then run the check-and-insert in a second statement, so the waiter sees the winner's committed row.

Links: [[read-committed]] · [[transaction-isolation]] · [[advisory-locks]]
