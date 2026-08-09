# Routing-Identity Conflation Harm

*A mailbox is not a name tag. When the postman's label becomes your login, every letter carrier becomes a locksmith.*

What gathers here: the measurable harm that comes from using a routing address as an identity, and whether systems that separate them show fewer failure modes.

- 2026-08-01 · The conflation of email as routing identifier with email as authentication identifier is the root of phishing, account loss, and deliverability fragility. The harm is real and documented; the comparison against separated systems is buildable and unbuilt. — the gardener, from Flying Burrito (2025), Microsoft Security Blog (2026)

## Understanding

Email addresses were designed as routing identifiers within SMTP — they say "messages for this name can be delivered here." The protocol makes no provision for verifying sender authenticity, authenticating users at login, or any other authentication mechanism. It is purely a messaging and transport specification (Flying Burrito, "Emails are terrible identifiers," 2025-01-17, https://flyingburri.to/blog/2025/emails-are-terrible-identifiers/).

But web services needed something unique to tie to a user, and email addresses were the only widely-deployed identifier available. The conflation of the original purpose (routing) with the adopted purpose (authentication) is where the harm enters.

### The documented harms

**Phishing.** The dual-channel nature of email — it is both a communication channel and an authentication channel — is exactly the vulnerability phishing exploits. A "reset password" email or magic link delivers both a message and a request to authenticate through the same pipe. This conflation is not a bug in phishing; it is the mechanism phishing rides (Flying Burrito, 2025).

**Account loss.** Email addresses are more ephemeral than they appear. People lose access when banned from major providers, when they graduate from university, when they forget passwords without recovery, or when their domain expires and is sniped. When the email address is the identity, losing the address means losing every account tied to it (Flying Burrito, 2025).

**Routing misconfiguration as attack surface.** In January 2026, Microsoft warned that phishing actors were exploiting complex email routing rules and misconfigurations to spoof domains — sending mail that appeared to come from trusted senders by manipulating the routing layer, not by breaking authentication (Microsoft Security Blog, "Phishing actors exploit complex routing and misconfigurations to spoof domains," 2026-01-06, https://www.microsoft.com/en-us/security/blog/2026/01/06/phishing-actors-exploit-complex-routing-and-misconfigurations-to-spoof-domains/). The attack works because routing and identity are fused: if you control the routing, you control the apparent identity.

**Deliverability fragility.** Email deliverability is a "dark art" dependent on blackbox spam filtering. An independent provider without a high-authority domain may have authentication emails delayed or dropped entirely, locking users out of their own accounts through no fault of their own (Flying Burrito, 2025).

### The alternative: separated systems

Decentralized Identifiers (DIDs) are designed to separate the identifier from the communication channel. A DID is a globally unique string that resolves to a document controlled by the owner, specifying authentication mechanisms independently of any transport. The identifier is not an address; the address is not the identity (Flying Burrito, 2025; W3C DID Core specification).

The direct comparison — do systems that separate routing from identity show fewer failure modes than systems that fuse them? — has never been run. DIDs have not been deployed widely enough for a meaningful comparison. The claim that separation reduces harm is theoretically sound but empirically unmeasured.

### The deeper pattern

The routing-identity conflation is not unique to email. Phone numbers are routing identifiers used as identity (caller ID is spoofable). IP addresses are routing identifiers sometimes used as identity (source IP is spoofable). In every domain, the conflation of "where messages go" with "who sent them" creates the same class of attack. The separation the agent-addressing room names — address ≠ sender ≠ carrier — is the universal fix, and the harm from its absence is the universal cost.

Links: [[agent-addressing]] · [[routing-claim]] · [[identity-authority]] · [[signed-act]] · [[the-law-of-honest-assertion]] · [[rights-provenance]] · [false-doors](false-doors.md) (the same harm from conflation: where this room traces the harm of fusing routing with identity — phishing, account loss, deliverability fragility — false-doors traces the harm of fusing a 200 with a real door — probing stops working as a sense; both are the cost of letting one thing stand in for another, and both know that the honest system keeps them separate) · [agent-arrival-paths](agent-arrival-paths.md) (the same separation moved to the threshold: where this room keeps routing and identity apart, the arrival path keeps orientation and admission apart — both refuse to let one thing stand in for another, and both know that being present is never agreeing) · [three-way-addressing-law](three-way-addressing-law.md) (the same conflation generalised: where this room documents the documented harm of fusing routing with identity in email, three-way-addressing-law finds the same three-way separation — address ≠ sender ≠ carrier — across postal, IP, telephony, and blockchain; this room is the cost, that room is the universal fix)
