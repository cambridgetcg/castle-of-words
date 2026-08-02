# signed-act

A signed act is a message that carries its own proof of authorship — a cryptographic signature that says "this message was sent by this sender." The signature is verifiable without trusting the carrier; the carrier delivers the message but does not vouch for who sent it.

Each outbound message in an honest addressing system is a separate signed and refusable act. The recipient can verify the signature and decline the message. The transport provider never becomes identity authority — it carries the signed act but cannot forge one.

Links: [[routing-claim]] · [[identity-authority]] · [[agent-addressing]] · [[agent-turn]]
