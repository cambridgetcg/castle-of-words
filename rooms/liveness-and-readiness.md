# Liveness and Readiness

*A pulse is not a diagnosis — the dashboard must name which signal it is showing.*

What gathers here: the craft of keeping liveness and readiness as separate contracts, so a process-alive check is never mistaken for database health.

---

- 2026-07-12 17:56 · Liveness and readiness are different contracts: a public process-alive endpoint must not be consumed as database health. Keep dependency probes authenticated, read-only, no-store, and make every dashboard name which signal it is showing. — yu

## Words

- [[liveness]] — is the process running? A yes/no answer, cheap and public.
- [[readiness]] — can the process serve traffic? A deeper check that may probe dependencies.
- [[health-endpoint]] — an HTTP endpoint that reports a service's state

## Links

[[minimal-health-endpoint]] · [[smoke-test-intent]] · [[honest-endpoints]] · [[fail-closed-boundaries]] · [[the-law-of-honest-assertion]] · [minimal-health-endpoint](minimal-health-endpoint.md) (the concrete form of the separate-contracts craft: this room names liveness and readiness as two contracts that must not be fused, and the minimal health endpoint builds the JSON body whose status and gate state carry them apart — both refuse to let the pulse be read as the diagnosis) · [smoke-test-intent](smoke-test-intent.md) (the second channel this room's dashboard needs: a pulse that cannot tell an intentional stop from a crash is the liveness-readiness fusion this room warns against, and the smoke test that reads a structured body for intent is the same separation made operational)
