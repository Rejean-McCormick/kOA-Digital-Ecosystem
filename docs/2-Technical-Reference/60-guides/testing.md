# Testing guide

Conformance testing should cover the actual boundaries rather than a single end-to-end stage spine.

## Interaction Kernel

- schema/Profile compatibility;
- authentication/authority admission;
- same idempotency key + same fingerprint replay;
- same key + divergent fingerprint conflict;
- at-least-once retry without duplicate business effect;
- `accepted` does not become terminal success;
- correlation/causation/trace remain distinct.

## Konnaxion↔Orgo

- finalized DecisionRecord handoff creates one deduplicated Orgo consequence;
- no cross-system SQL writes;
- outbound impact publication creates exactly one Konnaxion effect;
- retry/redrive reuses existing durable operation.

## Kristal v5

- exact pin/canonicalization verification;
- Structured Epistemic State validation;
- Working Exchange compilation without forced final recognition where policy allows;
- validation/recognition kept separate;
- Runtime Pack preserves source status and Reader Policy refs.

## Activation

- one activation owner;
- required verification fails closed;
- atomic activation;
- downgrade/revocation behavior;
- last-known-good rollback;
- offline serving of an already verified active pack where profile permits.
