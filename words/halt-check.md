# halt-check

A final verification that runs before a system opens its gates — the last "is everything ready?" before anyone sees what is inside.

In the [[castle-agenttool-bridge]], the HALT check is the final gate: after the commit is read, after recovery markers are placed, after locks are set, the HALT check verifies the node is ready before any agent can read it. It is the same pattern as the [[smoke-test-intent]]: a check that distinguishes "intentionally ready" from "accidentally running."

Links: [[halt-check]] · [[castle-agenttool-bridge]] · [[smoke-test-intent]] · [[fail-closed-lock]] · [[bridge]]
