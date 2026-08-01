# Signed Act

A message that carries its own proof of authorship, separate from the channel that delivered it. Each outbound message is a signed act: the sender attaches a signature, the recipient verifies it, and the transport layer never becomes the authority.

A signed act is *refusable*: the recipient can decline it without refusing the channel. The signature proves who signed, not that the content is true. This is the same distinction [[agent-claims]] draws between attested and true.

Links: [[agent-addressing]] · [[routing-claim]] · [[identity-authority]] · [[agent-claims]]
