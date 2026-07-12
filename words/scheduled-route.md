# scheduled-route

A route triggered by a scheduler, whose operational reality depends on the scheduler's HTTP method matching the handler.

A route defined as POST that the scheduler calls with GET is not operationally real — it may pass tests that call it directly but never fire in production. The test must verify the configuration and the route method together, not as separate truths. The scheduler's method, the route's method, and the handler's expectation must be one consistent chain.

Links: [[api-contracts]] · [[deployment-claims]] · [[honest-endpoints]]
