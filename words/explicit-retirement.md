# explicit-retirement

A declaration that a data node's life is over — not a deletion, but a named end that says "this was here, and now it is done."

In the [[castle-agenttool-bridge]], explicit retirement is the counterpart to the [[tombstone-in-manifest]]: you cannot delete from an append-only record, but you can append a marker that says the node is retired. Retirement is not erasure — the record remains — but it is an honest signal that the bridge no longer carries this node forward.

Links: [[explicit-retirement]] · [[castle-agenttool-bridge]] · [[tombstone-in-manifest]] · [[whole-collection-withdrawal]] · [[bridge]]
