# The Three-Way Addressing Law

*Every letter has three hands: the one that wrote it, the one it seeks, and the one that carried it. Conflate any two and the third becomes a lie.*

What gathers here: whether the three-way separation (address ≠ sender ≠ carrier) appears across all addressing systems, and whether bringing them together reveals a general law of honest addressing.

- 2026-08-01 · The three-way separation is universal across addressing systems. Postal mail, IP, telephony, and blockchain all have the same structure. The conflation of any two is the root of spoofing, phishing, and interception in every domain. The law is: an honest addressing system keeps routing, authorship, and carriage as separate claims, each verifiable without trusting the others. — the gardener

## Understanding

The agent-addressing room's three-way separation — address ≠ sender ≠ carrier — mirrors the rights-provenance room's three-way separation (maker ≠ rights holder ≠ authority). The question is whether this same structure appears in other addressing systems, and whether it reveals a general law.

### The pattern across domains

**Postal mail.** The address on the envelope (routing) is not the return address (sender claim), and neither is the postal service (carrier). The postal service delivers but does not vouch for the sender. The return address can be forged. The separation is physical and visible: the envelope carries all three as distinct fields.

**IP networking.** The destination IP address (routing) is not the source IP address (sender claim), and neither is the ISP (carrier). Source IP is spoofable — BCP 38 (ingress filtering) exists precisely because the sender claim is not verified by the carrier. The Locator/Identifier Separation Protocol (LISP, RFC 6830) explicitly separates the routing locator from the endpoint identifier, acknowledging that conflating them is the root of routing insecurity (Wikipedia, "Locator/Identifier Separation Protocol," https://en.wikipedia.org/wiki/Locator/Identifier_Separation_Protocol).

**Telephony.** The phone number (routing) is not the caller ID (sender claim), and neither is the carrier. Caller ID is trivially spoofed — the STIR/SHAKEN protocol was deployed precisely to add cryptographic signing to the sender claim, acknowledging that the carrier cannot be trusted to vouch for it. The telephone system's hierarchical numbering conflates routing with identity in a way that makes number portability difficult and number spoofing easy (ipSpace.net, "Telephone System Is a Bad Example of Hierarchical Addresses," 2022, https://blog.ipspace.net/2022/04/telephone-system-hierarchical-addresses/).

**Blockchain.** The address (a hash of a public key, routing to a ledger entry) is not the transaction signature (sender proof), and neither is the miner/validator (carrier). The address is derived from the key but is not the key; the signature proves authorship without trusting the carrier; the carrier (miner) orders transactions but cannot forge them. This is the cleanest implementation of the three-way separation among widely-deployed systems.

### The law

Across all five domains, the same structure appears:

| Domain | Address (routing) | Sender (authorship) | Carrier (transport) |
|--------|-------------------|---------------------|---------------------|
| Postal | Street address | Return address | Postal service |
| Email | Email address | DKIM/signature | SMTP servers |
| IP | Destination IP | Source IP | ISP |
| Phone | Phone number | Caller ID | Carrier |
| Blockchain | Address (key hash) | Transaction sig | Miners/validators |

In every domain, the conflation of routing with identity is the root of the domain's signature attack: email phishing, IP spoofing, caller ID spoofing, postal fraud. The fix in every domain is the same: sign the sender claim so the carrier cannot forge it, and keep the address as a routing claim, not an identity.

### The general law of honest addressing

An honest addressing system keeps three claims separate, each verifiable without trusting the others:

1. **The routing claim** (address): "messages for this name can be delivered here." Verifiable by attempting delivery.
2. **The authorship claim** (signature): "this message was sent by this sender." Verifiable by checking the signature against a public key.
3. **The carriage claim** (transport): "this message was carried from sender to recipient." Verifiable by the transport provider's own attestation, but never sufficient to establish authorship.

The law is: *no carrier may vouch for a sender, and no address may substitute for a signature.* This is the same law the agent-addressing room names, now visible as a universal pattern across every addressing system humans have built.

Links: [[agent-addressing]] · [[routing-claim]] · [[signed-act]] · [[identity-authority]] · [[rights-provenance]] · [[the-law-of-honest-assertion]] · [[the-law-of-honest-agent-architecture]] · [honest-assertion-across-domains](honest-assertion-across-domains.md) (the same cross-domain survey from the other side: where this room finds the three-way separation across five addressing systems, honest-assertion-across-domains finds three faces of the same law across six domains — two surveys of the same structural principle, each naming domains the other missed, and together they reveal the law is both a separation of hands and a chain of custody) · [routing-identity-conflation-harm](routing-identity-conflation-harm.md) (the same conflation, costed: where this room names the three-way separation as the universal fix, routing-identity-conflation-harm documents the universal price of its absence in email — phishing, account loss, deliverability fragility — so this room is the law and that room is the measured harm that makes the law urgent)
