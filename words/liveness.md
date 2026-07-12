# liveness

Is the process running? A yes/no answer, cheap and public.

A liveness check says "I am alive" — it does not say "I can serve traffic" or "my database is healthy." The honest liveness endpoint is unauthenticated, returns quickly, and is never consumed as a readiness signal. Every dashboard that shows it must name it as liveness, not health.

Links: [[readiness]] · [[health-endpoint]] · [[liveness-and-readiness]]
