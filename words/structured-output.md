# structured-output

*A message that arrives already wearing its labels, so the reader never has to guess.*

Structured output is text whose parts are named by a shape both sides agreed on — JSON keys, a fixed schema — instead of prose a reader must parse by feel. A scheduler that can speak either way tells its operator the result in prose (fine for one pair of eyes) but owes a *public* observer the structured form: the observer's job is to read it byte-for-byte, and prose forces guessing. With the structured form, the reader either recognises the shape or it does not — and when it does not, the honest reader falls back on [[fail-closed]]: deny, keep nothing, pass nothing on.

The pair to it: free text carried in a strictly delimited block — marked at both ends so a reader can cut the whole block out and retain none of its bytes. A block whose delimiters are loose is a block whose contents leak.

Links: [[fail-closed]] · [[second-channel]] · [smoke-test-intent](../rooms/smoke-test-intent.md) · [[diagnostic-block]]
