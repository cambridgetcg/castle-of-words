# exact-byte-vector

A sequence of bytes that carries its own decode rule, encoded-octet length, and digest — so two things that look the same but have different bytes are never mistaken for equal evidence.

Visually equal JSON is not equal evidence. An editor-added newline is a different artifact. The exact-byte vector refuses to let the surface appearance be mistaken for the underlying truth.

Links: [[digest]] [[receipt]] [[checksum]] · [verification-receipts](../rooms/verification-receipts.md) (the receipt that names what it does not prove and the vector that refuses to let surface match be mistaken for byte match are the same move)
