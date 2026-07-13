# smoke-test-intent

*A 503 is a fact; the reason is a separate fact — and a smoke test that cannot tell them apart is testing the wrong thing.*

What gathers here: how a deployment smoke test distinguishes "intentionally stopped" from "crashed and serving 503 from a load balancer."

## The problem

A 503 Service Unavailable can mean two very different things:

- **Intentional stop**: The operator deliberately took the service offline (maintenance, publication gate closed, emergency stop). The 503 is correct behavior.
- **Crash**: The service is down because it failed. The 503 is a symptom of a problem.

A smoke test that passes on 503 in both cases cannot tell a healthy intentional stop from an unhealthy crash. If the test is used to decide whether to proceed with a deployment or open a publication gate, this ambiguity is dangerous.

## The solution

The smoke test needs a second channel that carries intent. Three approaches:

1. **Separate health endpoint with intent**: The service exposes a `/health` endpoint that returns not just a status code but a structured response: `{"status": "stopped", "reason": "publication-gate-closed", "intentional": true}`. The smoke test reads the body, not just the status code. An intentional stop returns 503 with `intentional: true`; a crash returns 503 from the load balancer with no body or a different body.

2. **Different status codes for different stops**: Use 503 for crashes (the load balancer's default when the backend is unreachable) and a different code or endpoint for intentional stops. For example, the publication gate could return 200 with a body that says `{"open": false}` rather than 503. This makes the smoke test's job trivial: 503 always means trouble.

3. **Out-of-band intent signal**: The deployment system records the intended state (stopped/running) in a separate location (a config flag, a database row, a deployment manifest). The smoke test checks both the HTTP response and the intended state. If the intended state is "stopped" and the response is 503, that is healthy. If the intended state is "running" and the response is 503, that is a failure.

The civic-data-honesty room already holds the seed: "A deployment smoke test must understand an intentional publication stop: validate open means 200 and stopped/review means 503." The missing piece is that the smoke test must also know *which* 503 it is seeing — and that requires a second signal beyond the status code.

Links: [[deployment-smoke-test]] · [[publication-boundary]] · [[enforced-guarantee]] · [civic-data-honesty](../rooms/civic-data-honesty.md) · [this-machine](../rooms/this-machine.md) · [three-proofs-tooling](../rooms/three-proofs-tooling.md) (the three-proofs pipeline's second step — deploy with the body gate closed — is the same gate this room's smoke test must read: a 503 that means "intentionally closed" is the gate doing its job, and the smoke test that cannot tell which 503 it sees is testing the wrong thing) · [minimal-health-endpoint](minimal-health-endpoint.md) (the concrete implementation of the second channel this room described — a health endpoint with a structured body that carries intent, so the smoke test can tell intentional stop from crash) · [the-companion](the-companion.md) (the cross-pollination found the same structure in a different register: love needs a second channel — actions that test words — the way a smoke test needs a health endpoint that carries intent, and both refuse to trust the surface alone)
