# oauth

A protocol that lets one service act on behalf of a user at another service, without sharing the user's password.

OAuth works by granting a token — a limited, revocable key — rather than handing over the master key. The grant is scoped: it says what the holder may do, with which service, for how long. When the grant is revoked, the token stops working.

The honest OAuth system keeps grants separate: one grant per module, one revocation per grant. When grants are shared across modules, removing one module can silently revoke another — the disconnect carries collateral damage the system did not name.

Links: [[disconnect]] [[module]] [[grant]]
