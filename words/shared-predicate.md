# shared-predicate

A single yes-or-no condition that multiple parts of a system all check before acting — so a worker off-switch, a startup gate, and a request acceptor all agree on whether the system is running.

A global worker off-switch must gate startup, direct worker entry points, and request acceptance with one shared predicate. Fail closed when the queue is absent, and never present configuration flags as proof of runtime health.

Links: [[enforced-guarantee]] · [[honesty]]
