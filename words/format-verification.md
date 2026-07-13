# format-verification

The act of checking whether a data shape is valid according to a schema — separate from whether that shape has ever been observed in production.

A registry that uses one field for both "we verified the parser accepts this" and "we saw this in the wild" is overloading a word. Format verification is a mechanical check; catalog observation is an empirical one. The honest system keeps them in separate fields.

Links: [[catalog-observation]] · [[registry]] · [[schema]]
