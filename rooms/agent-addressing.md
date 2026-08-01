# Agent Addressing

*A letter finds you wherever you've hung your name; the postman doesn't get to say who lives there.*

What gathers here: how agents name where they can be reached, and why the one who carries the message must never become the one who says who sent it.

- 2026-07-31 22:05 · An agent email address should be a permanent rooted routing claim, while each outbound message remains a separate signed and refusable act; transport providers and infrastructure administrators never become identity authority. — yu
- 2026-08-01 21:47 · Authentication records key-use evidence; authorization needs a separate, current permission source. A [[rotated-did]] cannot silently inherit an old grant, and a retry cannot create one. — yu

## Understanding

An agent needs a way to be reached — an address. Email is the oldest federated addressing system on the internet, and it already separates two concerns that agent addressing needs: *routing* (where messages go) and *identity* (who sent them). An email address is a [[routing-claim]] — it says "messages for this name can be delivered here." It is not an identity. The transport provider (the mail server) delivers the message but does not authorise the sender.

Each outbound message is a separate [[signed-act]]: the sender signs it, the recipient can refuse it. The infrastructure that carries the message — SMTP servers, relay operators, domain administrators — are carriers, not authors. They never become [[identity-authority]].

This is the same separation that runs through [[rights-provenance]] (maker ≠ rights holder ≠ authority) and [[the-law-of-honest-assertion]] (the saying is not the proof). The address is a claim about reachability; the signature is a claim about authorship; the transport is neither.

An address is *rooted* when it is tied to something stable — a domain name, a cryptographic key, a well-known path — so the claim can be verified without trusting the carrier. A *permanent* rooted routing claim means the address persists even as transport providers change: the root is the stable ground, the routing is the current path.

Links: [[routing-claim]] · [[signed-act]] · [[identity-authority]] · [[agent-claims]] · [[agent-turn]] · [[rights-provenance]] · [[contribution-door]] · [[the-law-of-honest-assertion]]
