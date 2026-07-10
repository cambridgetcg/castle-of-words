# deployment-race

The brief window during a machine handoff when routing has not yet settled and a smoke test can hit the superseded release instead of the new one.

Confirm the active machine version, then repeat publication-state probes after routing settles before declaring a gate open or closed. The race is short but real — a green endpoint is not the same as a deployed service.

Links: [[publication-boundary]] · [[honesty]]
