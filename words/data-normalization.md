# data-normalization

Transforming data so public operations do not depend on private values.

When a sensitive field controls row order or page selection, the normalization step extracts the public-facing sort and filter criteria before the private source is contacted. The query that shapes the public view never sees the private value.

Links: [[sensitive-field]] · [[sensitive-data]] · [[representation-audit]]
