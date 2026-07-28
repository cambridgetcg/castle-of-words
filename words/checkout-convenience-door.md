# checkout-convenience-door

A checkout-convenience door is a door that lets code from a repository checkout execute — a convenience for developers who want to run without a full build pipeline.

The door is honest only when it names that checkout code executes (not a reviewed release), keeps byte receipts separate from provenance, and validates the entire test suite before starting outside code. Without these, the convenience door becomes a back door: code that was never reviewed, never built, and never verified runs with the same trust as a production release.

Links: [[receipt]] [[provenance]] [[fail-closed]] [[safety-boundaries]]
