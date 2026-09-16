# Chesed — Konnaxion civic/public boundary

Konnaxion owns civic/public source state, deliberation, consultations, readings and finalized DecisionRecords inside its product domain.

## Responsibilities

- preserve source facts and derived readings as distinct objects;
- finalize civic/public DecisionRecords under Konnaxion/eThikos rules;
- emit cross-system requests/events through explicit adapters when implemented;
- consume external artifacts without taking ownership of their native semantics;
- keep local authorization/RBAC inside Konnaxion.

## Orgo boundary

Target flow:

```text
finalized DecisionRecord
→ adopted cross-system Profile/adapter
→ Orgo Signal / Workflow / Case / Tasks
```

Konnaxion does not create/update Orgo Task/Case rows directly.

## Kristal boundary

Konnaxion may consume or distribute Kristal artifacts under explicit use cases. It must preserve source status, validation, certainty, authority recognition and Reader Policy metadata.

## Runtime Pack activation

Konnaxion may own desired/application selection or product distribution intent. For kOA-Linux deployments, authoritative local Runtime Pack verification/active-state/activation+rollback receipts belong to `kristal_runtime`; kOA Node Agent performs a narrow privileged host transition only where required.
