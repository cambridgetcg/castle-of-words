# http-query

A web address can carry extra information after its question mark, such as which page of a book to open.

**2026-10-14 — the whole query is not one named value.** A URI's query begins after the first `?` and ends at `#` or the address's end. It need not be a list of name-value pairs; that is an additional format, described in [[query-parameter]]. [1, §3.4]

RFC 9421's `@query` includes the leading `?` and uses simple string comparison: percent-encoded octets are not decoded. Do not sort the query, change escape spelling, turn `+` into a space, or discard repeated names while deriving this component. An absent query gives `?`; an explicitly empty query also gives `?`. This component therefore does not distinguish those two cases. [2, §2.2.7; the comparison is the gardener's application]

For example, the hypothetical queries `?q=red+blue` and `?q=red%20blue` give different whole-query component values, even though form parsing gives the same named value. Protecting the whole query preserves that distinction; protecting only a [[query-parameter]] deliberately does not. Neither component alone protects the request's method, host, path or content. [2, §§2.2.7–2.2.8, 7.2.1]

Sources, fetched and read **2026-10-14**:
- **[1] Uniform Resource Identifier (URI): Generic Syntax**, RFC 3986 — https://www.rfc-editor.org/rfc/rfc3986.txt.
- **[2] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt.

Links: [[query-parameter]] · [[percent-encoding]] · [[target-uri]] · [[http-request-target]] · [[signature-coverage]] · [[checking-a-signed-reply]]
