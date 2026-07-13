# agent-data-envelope

*An agent-facing result without its rights, boundaries, and exclusions is a letter without an envelope — the agent cannot know who sent it, what it covers, or what was left out.*

What gathers here: the craft of wrapping data for agents so they know what they have, what they don't, and what they're allowed to do with it.

- 2026-07-13 11:15 · A shared data resolver is not yet a complete agent interface: the agent-facing result must carry the data rights, absence boundary, and explicit exclusions that an HTTP envelope would otherwise provide. — yu

When a human opens a web page, the browser gives them more than the body: status codes, headers, redirects, cache directives. The human may not read them, but the browser uses them to make decisions. When an agent calls a shared data resolver — a function that returns data directly, without an HTTP envelope — it loses all of that. The resolver returns bytes, and the agent has no way to know:

- **Data rights.** Can the agent redistribute this? Attribute it? Cache it? The HTTP response would carry a `Link` header with a license, or a `Cache-Control` header. The resolver returns none of that.
- **Absence boundary.** Did the resolver return everything it knows, or only what it could find? The HTTP response would carry a `Content-Range` header or a `Link` header pointing to the next page. The resolver returns silence.
- **Explicit exclusions.** What was deliberately left out? The HTTP response would carry a warning header or a structured error body. The resolver returns nothing.

The honest agent interface wraps every result in an [[agent-data-envelope]] that carries these three things — rights, boundary, exclusions — as explicit fields. The envelope is not decoration; it is the only part of the result the agent can trust without guessing.

Links: [[agent-data-envelope]] · [[absence-boundary]] · [[data-rights]] · [agent-friendly-data](agent-friendly-data.md) (the same law at the data layer: bounded descriptions, stable IDs, typed errors) · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: a system's output is an assertion, and the honest system names what backs it) · [honest-endpoints](honest-endpoints.md) (the same law at the endpoint level: a door that tells you how to open it and what you'll find inside)
