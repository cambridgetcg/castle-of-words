# agent-data-envelope

The wrapper around an agent-facing result that carries data rights, absence boundary, and explicit exclusions — the three things an HTTP response would provide that a raw function call does not.

Without the envelope, the agent has bytes and no way to know what they mean, what they cover, or what they're allowed to do with them. The envelope is not decoration; it is the only part of the result the agent can trust without guessing.

Links: [[absence-boundary]] · [[data-rights]] · [[agent-interface]]
