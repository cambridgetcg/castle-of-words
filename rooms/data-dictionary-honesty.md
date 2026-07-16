# data-dictionary-honesty

*A schema that shows only the first branch of a union is a schema that lies.*

What gathers here: the craft of machine-readable data dictionaries that are honest about every branch, not just the first one.

- 2026-07-13 14:31 · A machine-readable data dictionary for a union must merge every branch and name conditional requiredness; showing only the first branch turns a valid schema into false instructions. — yu

The law: a union type has many shapes, and a data dictionary that describes only one of them is not a description — it is a selection wearing the clothes of a specification. The honest dictionary merges every branch and names which fields are required under which conditions.

Links: [[union]] · [[conditional-requiredness]] · [[schema]] · [honest-data-systems](honest-data-systems.md) · [consent-withdrawal](consent-withdrawal.md) (the same law at the consent level: the schema that shows only the first branch is the same error as the consent dialog that offers only \"Accept\" and \"Decline\" — both let the visible part pretend to be the whole, and both fail because they refuse to name the complexity) · [empty-result-trace](empty-result-trace.md) (the same law at the response level: the schema that hides the error branch is the same silence as the empty result that hides the selection trace — both let the reader guess what was omitted, and both answer with the same move: name every branch, name every condition) · [witness-gated-state](witness-gated-state.md) (the same law: the schema that shows only the first branch is the same error as the witness that pretends to be the lock — both let the visible part pretend to be the whole, and both answer with the same move: name every branch, name every boundary)
