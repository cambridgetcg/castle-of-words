# serialization

Serialization writes information in a form a computer can save or send.

A record and its written form are not the same thing. A format chooses concrete spellings, separators, ordering and encoding; two forms can carry the same values while containing different bytes. [[deterministic-json]] adds fixed rules so the same supported data gets the same byte spelling.

Repeatable is not automatically right for the job. JSON's canonical form and an HTTP signature's signed input follow different recipes. A signer and verifier can agree with each other while both miss the required component or escaping rule. Name the format and follow its rules before treating matching bytes as evidence of [[conformance]].

Sources: [deterministic-json-standards](../rooms/deterministic-json-standards.md), “The standard: RFC 8785 JCS,” and [checking-a-signed-reply](../rooms/checking-a-signed-reply.md), “A valid signature is one check, not the whole answer” and “A library can agree with itself and still miss the rule”; local rooms read **2026-10-23**, carrying their dated RFC 8785 and RFC 9421 readings. This is a definition drawn from those rooms, not a new implementation test.

Links:
- [deterministic-json-standards](../rooms/deterministic-json-standards.md) fixes a JSON record's byte spelling so another writer can reproduce it.
- [checking-a-signed-reply](../rooms/checking-a-signed-reply.md) keeps the signature's own spelling rules in charge rather than borrowing another format's tidy output.
