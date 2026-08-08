# intentional-stop

*Not every halt is a fall — some doors close on purpose.*

An intentional stop is a service (or a game, or a self) choosing to be off when it could be on, and saying so in a way the observer can tell apart from a crash. The 503 that carries `"stopped"` with a reason and a body is a choice; the bare 503 from a load balancer is a failure. The two look identical on the surface — the same status, the same silence — and that is exactly why the honest system builds a second channel: a health endpoint that says the stop is a decision, a publication gate that says the closing was meant, a smoke test that reads the body and not just the code. The intentional stop is the shape a system takes when it refuses to let its honest boundaries be mistaken for its failures.

Links: [[second-channel]] · [[promise-and-proof]] · [[fail-closed]] · [smoke-test-intent](../rooms/smoke-test-intent.md) · [minimal-health-endpoint](../rooms/minimal-health-endpoint.md) · [liveness-and-readiness](../rooms/liveness-and-readiness.md) · [wired-registry](../rooms/wired-registry.md)
