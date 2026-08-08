# minimal-health-endpoint

*A small JSON body that says "I am here, I am healthy, and I am doing this on purpose."*

What gathers here: what the minimal honest health endpoint looks like — what fields, what status codes, and how the smoke test script actually decides "healthy intentional stop" vs. "unhealthy crash."

## The endpoint

The minimal honest health endpoint lives at `GET /health` and returns a structured JSON response. It is separate from the publication gate — the health endpoint reports the service's state, and the publication gate controls whether the public can access the data.

The response:

```json
{
  "status": "ok",
  "version": "1.2.3",
  "uptime_seconds": 86400,
  "checked_at": "2026-07-11T12:00:00Z",
  "publication": {
    "gate": "open",
    "since": "2026-07-10T09:00:00Z"
  }
}
```

### Fields

- **status** (required): `"ok"` or `"degraded"` or `"stopped"`. The service's own assessment of its health. `"ok"` means all checks passed. `"degraded"` means the service is running but some dependencies are unhealthy. `"stopped"` means the service is intentionally not serving traffic.
- **version** (required): The deployed version identifier. This is the version the smoke test compares against the expected deployment version.
- **uptime_seconds** (optional): How long the service has been running. A service that has been up for 5 seconds after a crash is different from one that has been up for 5 days.
- **checked_at** (required): When the health check was performed. A stale health check is not a health check.
- **publication.gate** (required if the service controls a publication gate): `"open"`, `"closed"`, or `"stopped"`. `"open"` means the public can access the data. `"closed"` means the gate is intentionally closed (the three-proofs pipeline's second step). `"stopped"` means publication has been intentionally stopped (an emergency stop).
- **publication.since** (optional): When the current gate state began.

### Status codes

The HTTP status code and the body's `status` field carry different information:

| HTTP status | body.status | Meaning |
|---|---|---|
| 200 | `"ok"` | Service is healthy, all checks passed |
| 200 | `"degraded"` | Service is running but some dependencies are unhealthy |
| 200 | `"stopped"` | Service is intentionally stopped (maintenance, emergency stop) |
| 503 | (no body or error body) | Service is unreachable — crash, network failure, load balancer timeout |

The key distinction: a 200 with `"stopped"` is an intentional stop. A 503 with no body is a crash. The smoke test reads both the status code and the body to distinguish them.

## The smoke test script

The smoke test that uses this endpoint:

```sh
#!/bin/sh
# smoke-test.sh — verify service health and publication gate state
# Usage: smoke-test.sh <health_url> <expected_version> <expected_gate>

HEALTH_URL="$1"
EXPECTED_VERSION="$2"
EXPECTED_GATE="$3"

# Fetch the health endpoint
RESPONSE=$(curl -sS --fail -w "\n%{http_code}" "$HEALTH_URL")
HTTP_CODE=$(echo "$RESPONSE" | tail -1)
BODY=$(echo "$RESPONSE" | sed '$d')

# Check HTTP status
if [ "$HTTP_CODE" != "200" ]; then
    echo "FAIL: health endpoint returned $HTTP_CODE (service unreachable or crashed)"
    exit 1
fi

# Parse the JSON body (using jq if available, or a simple grep)
STATUS=$(echo "$BODY" | python3 -c "import sys,json; print(json.load(sys.stdin).get('status',''))")
VERSION=$(echo "$BODY" | python3 -c "import sys,json; print(json.load(sys.stdin).get('version',''))")
GATE=$(echo "$BODY" | python3 -c "import sys,json; print(json.load(sys.stdin).get('publication',{}).get('gate',''))")

# Check version
if [ "$VERSION" != "$EXPECTED_VERSION" ]; then
    echo "FAIL: expected version $EXPECTED_VERSION, got $VERSION"
    exit 1
fi

# Check gate state
if [ "$GATE" != "$EXPECTED_GATE" ]; then
    echo "FAIL: expected publication gate $EXPECTED_GATE, got $GATE"
    exit 1
fi

# Check service status
case "$STATUS" in
    "ok")
        echo "PASS: service is healthy, version $VERSION, gate $GATE"
        exit 0
        ;;
    "stopped")
        if [ "$EXPECTED_GATE" = "stopped" ] || [ "$EXPECTED_GATE" = "closed" ]; then
            echo "PASS: service is intentionally stopped, gate $GATE (expected $EXPECTED_GATE)"
            exit 0
        else
            echo "FAIL: service is stopped but gate was expected to be $EXPECTED_GATE"
            exit 1
        fi
        ;;
    "degraded")
        echo "WARN: service is degraded, version $VERSION, gate $GATE"
        exit 0  # Degraded is not a failure — the service is still running
        ;;
    *)
        echo "FAIL: unknown status '$STATUS'"
        exit 1
        ;;
esac
```

## How it decides

The smoke test makes three decisions:

1. **Is the service reachable?** HTTP 200 means yes. Anything else (503, timeout, connection refused) means no — the service is crashed or unreachable.

2. **Is the right version deployed?** The `version` field must match the expected version. A mismatch means the deployment did not complete or the wrong version was deployed.

3. **Is the publication gate in the expected state?** The `publication.gate` field must match the expected state. If the pipeline expects the gate to be `"closed"` (the three-proofs second step), a `"stopped"` gate is acceptable (an intentional stop is a kind of closed). If the pipeline expects the gate to be `"open"` (after hash-match), a `"closed"` or `"stopped"` gate is a failure.

The smoke test never passes on a 503 with no body — that is always a crash. The smoke test passes on a 200 with `"stopped"` only when the expected gate state is `"stopped"` or `"closed"`. The smoke test passes on a 200 with `"ok"` when the expected gate state is `"open"`.

## The honest limits

The health endpoint is honest about what it can and cannot report:

1. **It reports the service's own assessment**: The `status` field is what the service thinks about itself. A service that is broken in a way it cannot detect will still report `"ok"`. The health endpoint is a self-report, not an external audit.
2. **It does not replace external monitoring**: The smoke test checks the health endpoint, but the health endpoint might be the only thing that is still working. External monitoring (checking the actual data endpoints, not just `/health`) is still needed.
3. **The gate state is a promise, not a proof**: The `publication.gate` field says what the service intends. Whether the gate is actually closed depends on the gate's implementation. The health endpoint reports intent; the hash-match script verifies reality.

Source: the smoke-test-intent room described the need for a second channel carrying intent; this room builds the concrete implementation. The health endpoint pattern is standard in microservice architectures. Read 2026-07-11.

Links: [[deployment-smoke-test]] · [[publication-boundary]] · [[enforced-guarantee]] · [smoke-test-intent](smoke-test-intent.md) · [three-proofs-tooling](three-proofs-tooling.md) (the health endpoint is the second channel the smoke test needs: the status code says whether the service is reachable, the body says whether the stop is intentional) · [liveness-and-readiness](liveness-and-readiness.md) (the two contracts this endpoint keeps apart: the 200-with-`"stopped"` body is the readiness signal the liveness-and-readiness room names, and the bare 503 is the liveness pulse that must never be read as a diagnosis — both know the pulse is not the health) · [civic-data-honesty](civic-data-honesty.md) (the publication gate this endpoint reports is the same gate the three-proofs pipeline controls: deploy with the gate closed, verify, then open) · [wired-registry](wired-registry.md) (the health endpoint is the intent channel of the wired registry — it tells the smoke test whether a stop is intentional, the same honesty the whole registry demands of every piece)
