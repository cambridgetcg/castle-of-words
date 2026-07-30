# registrable-site

A domain boundary that the browser treats as a separate site for cookie and SameSite trust purposes — a public-suffix boundary or a distinct registrable domain per ownership epoch, so that changing the hostname actually isolates the new owner from the old one's cookies and trust.

A hostname change alone does not make a clean break. Sibling subdomains under the same registrable domain can share parent-domain cookies, and SameSite trust flows through the registrable domain boundary. A safe ownership bridge needs either a public-suffix boundary (a different TLD or a PSL-listed suffix) or a distinct registrable site per epoch, plus exact Host-to-epoch binding so the resolver knows which host belongs to which owner.

Links: [[ownership-epoch]] [[adversarial-naming]] [[key-bound-identity]]
