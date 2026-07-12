# readiness

Can the process serve traffic? A deeper check that may probe dependencies.

A readiness check says "I am ready to handle requests" — it may check the database, the cache, the upstream services. The honest readiness endpoint is authenticated (dependency state is not public), read-only, and marked no-store. It is never confused with liveness.

Links: [[liveness]] · [[health-endpoint]] · [[liveness-and-readiness]]
