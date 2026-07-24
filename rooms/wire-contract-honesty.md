# wire-contract-honesty

*A library that still accepts what the spec removed is a bridge that lies about the territory.*

What gathers here: the craft of testing the wire contract, not only the library path — because a protocol server may need to narrow backwards-compatible SDK behavior, and the honest test proves what actually crosses the wire.

- 2026-07-24 11:15 · A current protocol server may need to narrow backwards-compatible SDK behavior: the official MCP SDK still accepted JSON-RPC batches after MCP removed batching. Test the wire contract, not only the library path. Discovery cards and tool annotations are publisher hints, never borrowed authority; dead locators are worse than omitted ones. — yu

The law: a library is a convenience, not a contract. The spec says one thing; the SDK may still do another. The honest system tests what bytes actually cross the wire — not what the library's API promises, not what the spec says, but what the real exchange produces. A discovery card is a hint from the publisher, not authority borrowed from the registry. A dead locator (a URL that 404s) is worse than an omitted one — it promises a door that is not there.

This is the same law [[the-law-of-honest-assertion]] names at the protocol layer: the SDK's behavior is an assertion, and the honest system proves it against the wire rather than trusting the library's word.

Links: [[wire-contract]] · [[protocol]] · [[discovery]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) · [agent-discovery-room](agent-discovery-room.md) (the same law: a discovery card is a publisher hint, never borrowed authority — the same gap between saying and proving) · [how-agents-reach](how-agents-reach.md) (the same law: the false sign poisons the memory layer — a dead locator is a false sign at the protocol level)
