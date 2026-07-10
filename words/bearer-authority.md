# bearer-authority

A bearer token is a key that opens every door the project owns — whoever holds it acts as the project, not as a named person or a specific device.

In AgentTool, the bearer proves project-wide root authority, never identity-bound or device-scoped credential. Device names are operational labels only; per-agent self scope comes from whether the bearer's project owns the addressed identity. A bearer proves project authority, not DID authorship — holding the key says you can act for the project, not that you wrote the content. This distinction matters because ciphertext at rest does not imply runtime opacity: a truthful agent platform must describe authority, storage, processing custody, and signature proof as separate boundaries, then pin those words to executable routes and tests.

Links: [[continuity-boundary]] · [[wake]] · [[ledger]]