# time-based-state

*Memory that changes what it remembers is not memory — it is action.*

A read endpoint should project time-based state in memory, never persist it as a side effect. When a read changes the thing it reads, the read is a write wearing a different verb. The honest system keeps GET pure: it returns what is true now, and leaves no trace of having been asked.

Links: [[side-effect]] · [[read]] · [[write]] · [[purity]] · [safe-api-design](safe-api-design.md)
