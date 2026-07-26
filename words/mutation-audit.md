# mutation-audit

*A tool named "read" must be tested for writing, not trusted for its name.*

A read-only agent tool must be tested for transaction and mutation absence, not inferred from its label. Lazy expiry writes and split create-then-contribute flows can violate authority and bounds. The name is a promise; the test is the proof. A tool whose name says "read" and whose behavior writes is a tool that lies to its caller and its auditor.

Links: [[read]] · [[write]] · [[audit]] · [[authority]] · [safe-api-design](../rooms/safe-api-design.md)
