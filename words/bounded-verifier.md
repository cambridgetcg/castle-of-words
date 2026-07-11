# bounded-verifier

A checker that knows its own limit — it will verify up to N pages or M items, and if the job is bigger than that, it fails closed rather than pretending to have checked everything.

For a civic API, a self-consistent hash chain is not enough to make release history append-only. The verifier must serialize deployments, capture the cache-revalidated live prefix, compare it with the candidate artifact before mutation, and verify it again afterward — and fail closed when it reaches its page limit.

Links: [[enforced-guarantee]] · [[three-proofs-release]] · [[honesty]]
