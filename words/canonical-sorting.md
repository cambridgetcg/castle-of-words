# canonical-sorting

Canonical sorting is putting things in one fixed, agreed order — by key, by hash, by number — so that the same collection always produces the same output.

It exists so that anyone, anywhere, can compare two outputs byte for byte and know they mean the same thing. That is its gift: stability, diffability, verifiability — the same reason [canonicalization-and-verification](../rooms/canonicalization-and-verification.md) signs canonical forms rather than friendly ones.

But canonical order is a presentation order, not a meaning. Once rows are sorted, position carries no information about which role each row was playing. Any meaning that lived in the pre-sort arrangement must be bound to the items *before* the sort — a role name attached to its row — or the sorted output silently reassigns it. The sort is honest about order and must never be asked to carry identity.

Links: [[return-graph]] · [the-display-is-not-the-thing](../rooms/the-display-is-not-the-thing.md) · [canonicalization-and-verification](../rooms/canonicalization-and-verification.md) · [canonical-wire-action](../rooms/canonical-wire-action.md)
