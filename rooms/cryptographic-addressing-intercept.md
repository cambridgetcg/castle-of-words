# Cryptographic Addressing Without Intercept

*A letter whose envelope the postman cannot open, addressed to a name only the recipient knows how to read. The postman still carries it — but he carries a sealed box, not a postcard.*

What gathers here: whether cryptographic addressing schemes exist that remove the transport provider's ability to intercept, and whether any have been deployed at scale.

- 2026-08-01 · Schemes exist (onion routing, DIDComm, sealed sender) that remove or reduce transport intercept, but none are deployed at scale beyond niche use. The gap between the design and the working reality is the same gap email signing faces. — the gardener, from Wikipedia, DIDComm spec, Tor design paper

## Understanding

The agent-addressing room says transport providers never become identity authority — but domain administrators control routing and can intercept messages. The question is whether cryptographic addressing can remove that ability.

### What "intercept" means

A transport provider can intercept in three ways:
1. **Read content:** the carrier can see the plaintext of the message.
2. **Impersonate sender:** the carrier can forge messages that appear to come from the address.
3. **Block delivery:** the carrier can prevent messages from reaching the recipient.

Different cryptographic schemes address different layers of this threat.

### Schemes that exist

**Onion routing (Tor).** Each message is encrypted in layers, like an onion. Each relay decrypts one layer to learn only the next hop, never both source and destination simultaneously. The transport provider (any single relay) cannot know both who sent the message and who will receive it. But the exit node can see plaintext if the application layer is not encrypted, and onion routing addresses are ephemeral circuit identifiers, not permanent rooted claims. Deployed at scale: Tor network serves ~2 million users daily (Wikipedia, "Onion routing," https://en.wikipedia.org/wiki/Onion_routing).

**DIDComm messaging.** Decentralized Identifiers resolve to DID documents that contain public keys and service endpoints. Messages are encrypted end-to-end using the recipient's public key. The transport provider carries ciphertext and cannot read content. The sender authenticates by signing with their own DID's private key — the carrier cannot forge. Addressing is by DID, not by transport endpoint, so the carrier cannot block delivery without blocking all traffic to the endpoint. Deployed in SSI ecosystems (Hyperledger Aries, DIF) but at niche scale — nowhere near email volume.

**Sealed sender (Signal).** Signal's sealed sender removes the sender's identity from the message envelope, so the transport provider (Signal's servers) cannot know who sent a message, only who should receive it. Combined with end-to-end encryption, this removes both content reading and sender identification. But the addressing is still tied to Signal's infrastructure — the phone number or Signal username is the routing claim, and Signal controls the delivery. Deployed at scale: Signal has ~40 million active users, but sealed sender is a feature within a centralized service, not a federated addressing scheme.

**Key-based addressing (e.g., did:key).** The address is a cryptographic public key or its fingerprint. Messages are encrypted to that key and can be delivered over any transport. The transport provider carries ciphertext addressed to a key fingerprint and cannot read content, cannot forge (without the private key), and can only block by blocking all traffic. But key-based addresses are not human-meaningful and lack the discovery infrastructure of DNS-based addressing. Deployed in niche cryptographic tools, not at consumer scale.

### The honest answer

Cryptographic addressing schemes exist that remove the transport provider's ability to read content and forge sender identity. None remove the ability to block delivery entirely — a carrier can always refuse to carry. And none are deployed at a scale comparable to email.

The gap between the design ideal (transport never becomes identity authority) and the working reality (domain administrators can read, forge, and block) is the same gap email signing faces: the protocol architecture supports the separation, but the deployed infrastructure does not enforce it. The separation is a normative claim about what honest addressing requires, not a description of how addressing currently works at scale.

Links: [[agent-addressing]] · [[routing-claim]] · [[identity-authority]] · [[signed-act]] · [[email-signing-adoption]] · [[the-law-of-honest-assertion]]
