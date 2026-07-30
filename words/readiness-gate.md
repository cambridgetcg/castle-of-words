# readiness-gate

The consumer's test that a producer's release must pass before integration is claimed — the gate that turns two passing islands into a bridge.

A platform expansion is integrated only when the producer's exact release tree passes the consumer's readiness gate. Two test suites passing in isolation prove each island is solid, not that the bridge between them holds. The readiness gate is the integration test that exercises the producer's exact artifact against the consumer's exact expectations — and until it passes, the expansion is a plan, not a fact.

Links: [[ordered-release]] [[integration]] [[smoke-test]] [[deployment-gate]]
