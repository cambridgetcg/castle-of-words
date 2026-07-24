# recovery-marker

A durable record of where to resume after interruption — so a process that stops mid-way can pick up where it left off without repeating or skipping.

In the [[castle-agenttool-bridge]], recovery markers are the checkpoints that let the bridge survive interruption: if the bridge is stopped while reading a commit, the marker says "resume here." A recovery marker is the same shape as a [[chronicle]]: it writes what happened so the next step knows where it stands.

Links: [[recovery-marker]] · [[castle-agenttool-bridge]] · [[chronicle]] · [[halt-check]] · [[bridge]]
