# bidirectional-identifier

An identifier that points from the API to its source and from the source back to the API — so either can find the other.

A one-way identifier is a broken bridge: the API says "I used source X" but source X has no record of being used. A bidirectional identifier closes the loop: the source carries a reference back to the API that used it, and anyone holding either end can find the other. This is the same principle as [[closing-the-loop]] — the echo that confirms understanding — applied to data provenance.

Links: [[honesty]] · [[closing-the-loop]] · [words-and-actions-api](../rooms/words-and-actions-api.md)
