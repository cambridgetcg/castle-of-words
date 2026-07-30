# trust-root

The one piece of information a verifier must obtain outside the system being verified — the founding checkpoint, rules hash, and exact Keeper-set hash or keys — without which a self-signed bundle proves only internal consistency, not that it is the intended realm.

A trust root is the seed that makes a chain of signatures meaningful. Without it, every link in the chain verifies against the link before it, but the first link verifies against nothing. The trust root is the answer to "who says this is the real chain?" — and it must come from outside the chain itself.

Links: [[verification]] [[canonicalization]] [[signing-key-bootstrapping]] [[append-only]]
