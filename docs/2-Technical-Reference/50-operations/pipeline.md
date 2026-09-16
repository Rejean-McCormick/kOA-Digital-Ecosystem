# Operations — pipeline coordination

There is no single mandatory ecosystem stage spine. Operators coordinate independent lifecycle transitions according to the active Interaction Kernel Profile, Kristal policy and deployment policy.

## Reference knowledge-build flow

```text
source/export
→ Structured Epistemic State
→ compile Working Exchange
→ review/validation as applicable
→ authority recognition as applicable
→ Reference Exchange when recognized
→ Runtime Pack build as permitted by policy
→ publication/distribution
→ deployment verification/activation
```

## Gating rule

Do **not** implement a universal “validation failed → compilation forbidden” rule. Instead record each transition separately and gate the transition that actually requires the evidence.

Examples:

- a research Profile may allow a working-derived Runtime Pack;
- a production reference channel may require Reference Exchange + required authority recognition;
- a deployment may reject activation for compatibility, revocation or trust reasons even when publication succeeded.

## Build evidence

Use Build Record v2 and record:

- exact input/export refs;
- exact Kristal pin;
- Interaction Kernel Profile/correlation/idempotency identity where applicable;
- stage execution results;
- Working and Reference outputs separately;
- validation and recognition refs;
- Runtime Pack source status;
- publication and activation status separately.
