# runtime-policy-decision

A runtime-policy decision is a choice made at the exact moment of execution — not pre-authorized, not inherited from a stored plan — that binds the terms under which an action may proceed.

A portable workflow record can describe what should happen, but only a live runtime-policy decision can authorize it to happen. The decision binds five things: exact terms (what is being asked), provider grant (what the provider is authorized to do), customer data permission (what data may be used), exact action approval (this specific action, not a category), and [[brake-state]] (whether the system is stopped). The decision is current by definition — it is made now, not stored from before.

Links: [[portable-workflow-record]] · [[brake-state]] · [[autonomy-offer]] · [[agent-turn]]
