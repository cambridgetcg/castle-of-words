# null-hash-semantics

*A null hash is a silence where a fact should be — and silence is always ambiguous.*

What gathers here: whether a manifest that lists a file with a null hash should distinguish "never published" from "published and then deleted."

## The ambiguity

A manifest entry with a null hash is a statement that says "this file has no hash." But the reason matters:

- **Never published**: The file was planned but never released. The null means "not yet."
- **Published and deleted**: The file was once available but has been removed. The null means "no longer."
- **Hash unavailable**: The file exists but the hash could not be computed (corruption, access error). The null means "unknown."

A consumer of the manifest cannot tell which of these is true from a null hash alone. If the consumer is a mirror that already has a copy of the file, "never published" means "keep your copy, it's fine" while "published and deleted" means "your copy is stale, stop serving it." The two states demand opposite actions.

## The solution

The manifest should distinguish the states explicitly. Three approaches:

1. **Separate status field**: Add a `status` field with values like `published`, `unpublished`, `deleted`, `pending`. The hash is present only when `status` is `published`. This is the cleanest approach — the status carries the semantics, the hash carries the verification.

2. **Explicit null reasons**: Use a structured null — `{"hash": null, "reason": "never-published"}` or `{"hash": null, "reason": "deleted"}`. This keeps the hash field but adds the missing information.

3. **Absence vs. explicit null**: Never-published files are simply absent from the manifest. Deleted files appear with a tombstone entry (a record that says "this file was here and is now gone"). This is the approach most version control systems use.

The verification-hash insight already says to "report null when bytes are unavailable." The missing piece is that null needs a reason. The honest manifest says not just "no hash" but "no hash because..."

Links: [[verification-hash]] [[open-data]] [[honesty]] · [open-data-checksums](../rooms/open-data-checksums.md) · [signing-key-bootstrapping](../rooms/signing-key-bootstrapping.md) (the manifest whose null hash this room reads is the same manifest whose signing key that room must trust — a null hash is a silence in a document whose authorship must be verified, and the two questions are the same question asked of the manifest's body and its signature: what does this document actually say, and who actually said it) · [verification-receipts](../rooms/verification-receipts.md) (the same law at the receipt level: the null hash that names which silence it is and the receipt that names every limit it does not carry are the same move — both refuse to let an absent value be promoted into a present one, and both know the honest manifest says not just "no proof" but "no proof because…") · [transparency-graph-audit](../rooms/transparency-graph-audit.md) (the null hash's ambiguity — never published, deleted, or unavailable — is the same honesty-of-absence the graph audit demands: what is not said is as load-bearing as what is, and the refusal to distinguish is the same silence that makes a graph manufacture influence by joining what should stay apart)
