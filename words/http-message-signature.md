# http-message-signature

An HTTP message signature is a mark checked with a cryptographic key to protect chosen parts of a web request or reply.

**2026-10-13 — chosen parts, not an automatic seal over everything.** RFC 9421 constructs a signature base from named message components and signature parameters. The verifier must rebuild that base from the received message and its proper context, use an allowed algorithm and a key trusted for that context, and enforce the application's required coverage. A valid mark made with an attacker's own key is not an acceptable answer from the expected server. [1, §§1.4, 2.5, 3.2, 7.3.4]

Covering [[content-digest]] protects the field's value; the recipient must still check that value against the actual content. Uncovered fields can change without breaking the signature. A response can cover parts of its triggering request using the `req` parameter, but request binding and protection against [[replay-attack|replay]] need explicit application rules. [[checking-a-signed-reply]] holds the full distinction. [1, §§2.4, 7.2.1–7.2.2, 7.2.8]

The mechanism permits both public/private-key signatures and shared-secret authentication codes. With a shared secret, a verifier can also create a valid mark; it is not exclusive proof that the other party made it. A signature supplies no confidentiality and does not replace TLS. [1, §§7.1.2, 7.3.3]

Source **[1]**: A. Backman, J. Richer and M. Sporny, **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — fetched and read **2026-10-13**. No keys or signatures were generated, loaded into a verifier, or tested.

Links: [[content-digest]] · [[repr-digest]] · [[nonce]] · [[replay-attack]] · [[agent-claims]] · [[checking-a-signed-reply]]
