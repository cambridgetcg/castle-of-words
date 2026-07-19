# bounded-handoff

*One handoff per request — the seam where safety lives.*

A bounded handoff is a single, complete transfer of work from one request to the next. In an infinite public game, each request performs exactly one bounded handoff: it receives a coordinate, does its work, and leaves the next coordinate usable. The handoff is bounded because it is one thing, not a chain — the next request picks up where this one left off, and no request pretends to prove what earlier requests did. The safety of the infinite game lives in the boundedness of each handoff.

Links: [[handoff]] · [[can-continue]] · [[stateless-validation]] · [bounded-play](../rooms/bounded-play.md)
