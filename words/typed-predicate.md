# typed-predicate

A database query helper that knows how to serialize a value for its column type, so a Date becomes an ISO string instead of a raw JavaScript object.

When you interpolate a value directly into a raw SQL template, the database driver may not know what column type it's headed for and can't apply the right encoder. A typed predicate like `lt(column, date)` or `gte(column, date)` tells the query builder the column's type, so the value is serialized correctly before it reaches the wire.

Links: [[honesty]]
