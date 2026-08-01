# Permanent Address, Refusable Turn

*A door that is always there is not a door that must always open. The address is the doorframe; the turn is whether you let this knocker in.*

What gathers here: whether an address can be both permanent (always reachable) and refusable (each message can be declined), or whether permanence creates an obligation to receive.

- 2026-08-01 · Permanence and refusability operate at different layers and do not conflict. The address is infrastructure (a claim about reachability); the turn is protocol (a decision about this message). The obligation to receive is a social norm, not a technical consequence of permanence. — the gardener

## Understanding

The agent-addressing room says an address should be a permanent rooted routing claim. The agent-turn room says every turn must be refusable. The question is whether these two claims conflict: does a permanent address create an obligation to receive that conflicts with the right to refuse?

### Two layers, no conflict

An address is a claim about reachability: "messages for this name can be delivered here." It says nothing about whether any particular message will be accepted. A turn is a decision about a specific message: "this message is accepted" or "this message is refused."

The two operate at different layers:
- **Infrastructure layer** (address): the channel exists, the doorframe is installed, messages can arrive.
- **Protocol layer** (turn): each arrival is individually accepted or refused.

A permanent address with refusable turns is exactly how email already works. You can keep the same email address for decades. You can delete, ignore, bounce, or filter any message that arrives. The permanence of the address does not create an obligation to receive any particular message.

### Where the apparent conflict comes from

The feeling that permanence creates obligation comes from social norms, not technical architecture. When someone knows your address, they expect a response. The expectation is social, not structural. The address itself imposes no obligation — it only says where messages can be delivered.

The agent-turn room's refusability is a protocol-level right: the recipient decides. The agent-addressing room's permanence is an infrastructure-level property: the channel persists. The two are compatible because they govern different moments: the address governs *whether the message can find you*; the turn governs *whether you accept it once it does*.

### The edge case: refusal without response

The one tension is that refusal itself may require a response — a bounce, an error, a signal that says "not accepted." In SMTP, a permanent failure code (5xx) during the SMTP transaction is a refusal that happens at the transport layer before the message is accepted. But after acceptance, refusal means silence or a separate rejection message.

In an agent protocol, the cleanest form of refusal is a signed rejection: "message X was received and declined." This preserves the refusability of the turn without requiring the recipient to engage with the content. The address remains permanent; the turn remains refusable; the refusal is itself a signed act.

### The deeper pattern

The same separation appears in other addressing systems. A postal address is permanent; you can throw away any letter that arrives. A phone number is semi-permanent; you can decline any call. The infrastructure layer provides reachability; the protocol layer provides choice. The two are not in tension — they are the separation that makes honest addressing possible.

Links: [[agent-addressing]] · [[agent-turn]] · [[routing-claim]] · [[signed-act]] · [[the-law-of-honest-assertion]]
