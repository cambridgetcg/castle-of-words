# mutation

*A change that cannot be undone — once committed, the old state is gone.*

In computing, a mutation is an operation that changes state: writing to a database, creating a file, generating a key. The opposite is a read — an operation that observes without changing. The craft of safe mutation is about ordering: validate before you mutate, commit before you depend on the result, and never let a timeout kill a process between the commit and the confirmation.

Links: [[secret]] · [[fail-closed]] · [[timeout]] · [production-cli-safety](../rooms/production-cli-safety.md)
