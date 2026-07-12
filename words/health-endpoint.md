# health-endpoint

An HTTP endpoint that reports a service's state — liveness, readiness, or both.

The honest health endpoint distinguishes its signals: a liveness check is public and cheap, a readiness check is authenticated and may probe dependencies. The minimal honest health endpoint returns a JSON body with status, version, and publication gate state, so the smoke test can tell intentional stop from crash.

Links: [[liveness]] · [[readiness]] · [[minimal-health-endpoint]] · [[smoke-test-intent]]
