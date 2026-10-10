# relative-reference

A relative reference is an address that needs another address to show where it leads.

The starting address is called the **base URI**. `guide.md` beside a document at `https://example.org/docs/llms.txt` leads to `https://example.org/docs/guide.md`; `/guide.md` leads to `https://example.org/guide.md`. The label on a Markdown link is not this base and does not determine the destination.

These are worked examples, computed with Python's `urllib.parse.urljoin` on **2026-10-10**, not pages fetched from those example addresses.

RFC 3986 §5.1 describes how to establish the base. When no embedded or enclosing base applies, use the address that actually retrieved the document; after redirects, that means the final retrieval address. A copied relative link without its base can lose its meaning. The llms.txt v2 proposal uses Markdown links but does not supply a separate relative-reference resolution algorithm.

Sources, read **2026-10-10**:
- T. Berners-Lee, R. Fielding and L. Masinter, **Uniform Resource Identifier (URI): Generic Syntax**, RFC 3986 §§5.1 and 5.4 — https://www.rfc-editor.org/rfc/rfc3986.txt.
- Jeremy Howard, **The /llms.txt file, v2**, “Format” — https://llmstxt.org/index.md.

Links: [[discovery-index]] · [[how-agents-find]] · [[false-doors]]
