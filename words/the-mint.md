# the mint

*A name is trustworthy only when the one who made it stands inside it.*

The part of a transaction identifier that says *who issued it* — so the value part can stay small, and the whole stays globally unique because issuers cannot collide with each other.

For a child: imagine every trader in the world could stamp numbers on parcels. If two traders stamp "17", the parcels are confused. But if each stamp begins with the trader's own initials — "ANNA-17", "BEA-17" — the number 17 can be reused safely, because the initials carry it apart. The mint is the initials.

In the UTI standard the mint is the issuer's LEI — the full 20 characters, deliberately, after an ISDA 2013 proposal to use only characters 7–16 was rejected for inviting collisions between different organisations. The mint is what moves uniqueness from the trade's own fields (which different feeds may spell differently) into the identifier's design (which one party controls). A reporter-id prepended to a fallback movement hash is the same shape in humbler dress. — *Source: Wikipedia, "Unique Transaction Identifier", https://en.wikipedia.org/wiki/Unique_Transaction_Identifier, and CPMI-IOSCO Technical Guidance, https://www.bis.org/cpmi/publ/d158.htm — read 2026-09-03.*

The castle's own shape is the same: the insight file is the mint of each insight's text; a room is the mint of the insights that gather in it. A mint never proves what is claimed inside it — only who stands behind the claim.

Links: [[movement-identity]] · [[end-to-end-identification]] · [[stable-identifier]] · [[identity]] · [[receipt]]
