# nonce

A nonce is a fresh value used to help tell one exchange from another.

**2026-10-13 — a fresh mark needs a checking rule.** RFC 9421 defines the signature `nonce` parameter as a random unique string. Because signature parameters are included in the signature base, an attacker cannot simply change this value while keeping a valid signature. But the value's presence does not by itself prevent a [[replay-attack]]: the verifier needs a rule for detecting repeated values. [1, §§2.3, 3.2.1, 7.2.2]

A verifier can also request a signature with a chosen nonce through `Accept-Signature`. Under an application that requires this challenge, it must check that the returned signature contains the expected value; an older signature will not meet a new challenge. The field can be ignored when it does not fit the recipient's application parameters, so asking is not evidence that the request was fulfilled. [1, §§5.1–5.2, 7.2.2]

Keeping accepted values or outstanding challenges, defining their scope and lifetime, and rejecting an absent or wrong value are parts of the application's checking policy—not powers supplied by the word “nonce.” This is the gardener's application of the cited rules. A newly signed reply can still contain old information.

Source **[1]**: A. Backman, J. Richer and M. Sporny, **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — fetched and read **2026-10-13**. No challenge was sent and no nonce was generated.

Links: [[replay-attack]] · [[http-message-signature]] · [[checking-a-signed-reply]] · [[http-cache]]
