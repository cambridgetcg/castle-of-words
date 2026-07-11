# observation-vs-inference

An observation reports what was measured or seen ("the endpoint returned 503"). An inference draws a conclusion from it ("the service is unhealthy"). The two must be kept separate because an observation can be true while the inference is false — the 503 might be an intentional stop, not a crash. Fusing them is the most common way an honest system lies.

Links: [[testimony]] · [agent-feedback-path](../rooms/agent-feedback-path.md) · [smoke-test-intent](../rooms/smoke-test-intent.md)
