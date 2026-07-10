# query-filter-contract

A promise an API makes to its users: every filter parameter advertised in the documentation is bound to a real database column, and the system refuses to start if a schema change would turn that binding into a silent no-op.

A filter that quietly returns everything — or nothing — is a lie the API tells without knowing it. The contract is enforced at boot time, not at query time, because the failure that matters is the one that never reaches a user.

Links: [[honesty]] · [[enforced-guarantee]]
