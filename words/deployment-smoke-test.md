# deployment-smoke-test

An automated check that runs after deployment to confirm the service is alive and behaving as expected.

An honest smoke test understands that a publication stop is not a failure: it validates that open means HTTP 200 and stopped or under-review means HTTP 503. It bounds every network request with a timeout, and it never turns the safety switch into a permanent deployment failure by treating "stopped" as "broken."

Links: [[publication-boundary]] · [[honesty]] · [[deployment-race]]
