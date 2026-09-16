# Integration — External systems

External systems integrate through explicit adapters/contracts, source-owned exports/references and adopted cross-system Profiles where applicable. Shared mutable state is not an integration contract.

## Safe entry patterns

- command: explicit intent to the owning receiver;
- query: read/projection without ownership transfer;
- event: fact already committed by the publisher;
- artifact: immutable/versioned content with identity/integrity/provenance;
- durable external effect: idempotency + retry/outbox + terminal reconciliation.

## kOA-Linux artifact boundary

When an external artifact is adopted by kOA-Linux, use the registered artifact class/release channel and Release Set compatibility rules. Runtime Pack local verification/active state belongs to `kristal_runtime`; privileged node operations use kOA Node Agent only where required.

## Koali

External/product applications may contribute presentation surfaces to Koali Spaces through its admission/registration contracts. Presentation registration or Space activation does not grant product, policy or host authority.
