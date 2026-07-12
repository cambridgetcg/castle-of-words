# commit-reveal-limits

*A server can prove it wrote down what you sent — but it cannot prove it chose fairly among strangers.*

What gathers here: the craft of understanding what a server-generated commit/reveal receipt actually proves, and where independent evidence must begin.

- 2026-07-11 23:24 · A server-generated commit/reveal receipt proves recorded consistency, not unbiased selection; independent evidence begins only when entropy or a commitment is witnessed outside the server's control. — yu

The distinction, plainly:

A commit/reveal protocol has two steps: the server commits to a value (publishes a hash), then later reveals it (publishes the value that matches the hash). The receipt proves the server did not change the value after committing — that is **recorded consistency**.

What it does not prove is that the server chose the value fairly among all possible values — that is **unbiased selection**. A server can commit to a hash, wait to see what others reveal, then reveal a value that benefits itself — and the receipt will still verify. The consistency is real; the fairness is not.

Independent evidence begins only when the entropy (the randomness that produced the value) or the commitment itself is witnessed by someone outside the server's control — a second server, a public blockchain, a trusted third party. Until then, the receipt is a proof of honesty about the past, not a proof of fairness about the choice.

Links: [[commit-reveal]] · [[recorded-consistency]] · [[unbiased-selection]] · [[entropy]] · [verifiable-encryption-claim](verifiable-encryption-claim.md) (the same law: a field named "ciphertext" describes an intended protocol, not evidence; a commit/reveal receipt describes an intended fairness, not evidence of it) · [the-truth-chain](the-truth-chain.md) (the truth-chain's append-only ledger proves recorded consistency; the commit/reveal limit is the same boundary — what was written is true, how it was chosen is not) · [deployment-claims](deployment-claims.md) (the same law: a commit/reveal receipt proves recorded consistency but not unbiased selection, and a deployment claim proves intent but not execution — both name the exact point where the binding to independent evidence stops) · [honest-feedback-receipt](honest-feedback-receipt.md) (the same law: a feedback receipt proves the report was stored, and a commit/reveal receipt proves the value was recorded — both prove what was written down, and neither proves what was fair or what will happen next)
