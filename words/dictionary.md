# dictionary

A dictionary lets a program find a value by its name, like choosing a drawer by its label.

Here the word means a keyed lookup structure, not a book of definitions. Under the structure's chosen equality rule, one key selects one value; that value can itself be a list. The name alone does not tell us the ordering rule or what happens when the same key arrives twice.

An ordered list of name/value pairs can keep repeated names. In [[decoding-query-names]], the form parser returns that list rather than a one-value-per-name dictionary. [[checking-a-signed-reply]] gives the example `q=one&%71=two`: both parsed names are `q`, and choosing just one value hides the repetition that prevents selection of that name as an RFC 9421 query component.

Converting a list therefore needs an explicit rule: reject unwanted repetition, or preserve the values and any order or context the job needs. Silently keeping the first or last value is a [[lossy-transformation]], not proof that the input was unique. A dictionary whose values are lists can retain repeated values, but it does not automatically preserve every distinction in the original record.

Sources: [[decoding-query-names]], “Read the pieces in order” and “The value used must still be the value protected,” and [[checking-a-signed-reply]], the query-name discussion beside `q=one&%71=two`; local rooms read **2026-10-26**, carrying their dated WHATWG form-parser and RFC 9421 readings. This is a definition and connection drawn from those rooms, not a new parser or verifier test.

Links:
- [[decoding-query-names]] keeps every parsed pair on the table before an application's naming rule can fold several entries into one drawer.
- [[checking-a-signed-reply]] needs to see the repeated name before deciding whether its value can enter the signed input.
- [[deterministic-json-standards]] starts with duplicate-free object keys, a condition that silent overwriting cannot prove about the original input.
