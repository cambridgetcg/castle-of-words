# route-guard

A piece of code that sits between the incoming request and the handler, checking whether the caller may proceed.

A route guard runs before the handler parses the body or touches the database. The honest guard rejects early — before identity is parsed, before service modules are imported — so a malformed or unauthorized request never reaches code that could leak information. Testing a guard with an unreadable Request proves it rejects at the boundary, not after inspection.

Links: [[fail-closed]] · [[fail-closed-boundaries]] · [[honest-endpoints]]
