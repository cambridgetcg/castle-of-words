# brake-state

A brake state is a condition where action is stopped — not paused, not deferred, but genuinely halted until a fresh [[runtime-policy-decision]] authorizes the next step.

A brake is not a pause button; it is a wall. Every [[portable-workflow-record]] must carry the brake state as a separate field because the record alone must never authorize dispatch. The brake is fail-closed: when uncertain, stop. The brake state is checked at the moment of execution, not at the moment of planning. A system with a working brake can be trusted with autonomy because it can be trusted to stop.

Links: [[runtime-policy-decision]] · [[portable-workflow-record]] · [[autonomy-offer]] · [[agent-turn]] · [[fail-closed-boundaries]]
