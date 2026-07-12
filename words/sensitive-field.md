# sensitive-field

A data field whose value must not leak to the caller, even indirectly through ordering, filtering, or selection.

Nulling the field after querying is not enough if the hidden value still controls row order, page selection, or top-N membership. The honest approach normalizes public filters and sorts before the private source is contacted — the public view is built from public data only, and the private value never enters the query that shapes it.

Links: [[data-normalization]] · [[sensitive-data]] · [[representation-audit]]
