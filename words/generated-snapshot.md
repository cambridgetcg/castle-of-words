# generated-snapshot

A self-contained, committed artifact of generated code — like an OpenAPI spec or JSON Schema — that is checked for drift before tests run, so the served bytes and the committed contract can never silently disagree.

The generated snapshot is the contract's one source of truth. It is committed to version control, checked for drift in CI (does the generator still produce the same bytes?), and compiled independently at runtime. The release smoke test asserts against the snapshot, not against whatever the generator happened to produce last.

Links: [[api-contract]] · [[smoke-test]] · [[deployment-gate]]
