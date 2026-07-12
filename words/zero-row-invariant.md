# zero-row-invariant

A contract that says: when this route is status-only, the successful data response is removed from the schema.

A zero-row invariant encodes in the API contract what the rights boundary enforces at runtime. If a route cannot serve data because rights are unproven, the schema must not promise data — it must document the unauthenticated 503 and remove the 200 response shape. A schema that promises what the route cannot deliver is a schema that lies.

Links: [[fail-closed-route]] · [[public-api-reachability]] · [[canonical-schema-literal]]
