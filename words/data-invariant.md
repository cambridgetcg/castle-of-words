# data-invariant

A condition that must always be true in the data, no matter what operations have run.

An invariant is a promise the data makes about itself: every order has a customer, no balance is negative, every foreign key points to a real row. After a migration runs, the invariants must still hold. Verifying them is the last gate before claiming a deployment succeeded — if an invariant is broken, the deployment is not done, no matter what the migration journal says.

Links: [[journal-checksum]] · [[migration-byte-history]] · [[zero-row-invariant]]
