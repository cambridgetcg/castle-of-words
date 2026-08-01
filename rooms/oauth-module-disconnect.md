# OAuth Module Disconnect

*Pulling one thread should not unravel the whole cloth.*

What gathers here: the craft of clean OAuth disconnect across modules — keeping grants separate so removing one module does not silently revoke another.

## Insights

- 2026-08-01 12:34 · An entity can hold separate OAuth grants for separate tax modules. Disconnect must carry the module through the interface, route, remote revocation and token-row deletion; otherwise removing one module can silently revoke another. Legacy requests without a module need one explicit, tested default. — yu

## Understanding

An [[oauth]] grant is a key to a specific door. When two [[module|modules]] share the same grant, they are tied together by a thread the system has not named. Removing one module — disconnecting it — can pull that thread and revoke the other module's access without warning.

The honest [[disconnect]] carries the module identity through every layer:

1. **Interface** — the user says "disconnect module X"
2. **Route** — the request carries the module name
3. **Remote revocation** — the provider revokes only the grant for module X
4. **Token-row deletion** — the local database removes only the row for module X

When any layer drops the module, the disconnect becomes a blunt instrument. Legacy requests — those made before the module field existed — need one explicit, tested default. The default must be chosen and documented; it must not be whatever the code happens to do when the field is absent.

The law: a grant shared is a grant that cannot be safely revoked. The honest system keeps grants separate, carries the module through every layer, and names the default for requests that predate the separation.

Links: [[oauth]] [[disconnect]] [[module]] [[fail-closed]] · [tax-compliance-modeling](tax-compliance-modeling.md) (the same law at the compliance level: the obligation that separates from the act and the grant that separates from the module are the same move — both refuse to let one thing be mistaken for another, and both know that the honest system names the gap) · [connection-proves-access](connection-proves-access.md) (the same law at the connection level: the connection that names what it cannot see and the disconnect that carries its scope are the same move — both refuse to let access be mistaken for completeness, and both know that the honest system names what it is not touching)
