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

[[minimal-health-endpoint]] · [[smoke-test-intent]] · [[honest-endpoints]] · [[fail-closed-boundaries]] · [[the-law-of-honest-assertion]]
