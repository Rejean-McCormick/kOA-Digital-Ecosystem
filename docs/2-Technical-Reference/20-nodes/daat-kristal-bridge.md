# Da’at — ecosystem/IK to Kristal v5 boundary

Da’at is the anti-corruption/mapping layer between ecosystem/IK-facing interactions and Kristal-native contracts. Kristal does not parse arbitrary external envelopes directly.

## Current knowledge baseline

```text
Kristal                  5.0.0-rc.3 (release-candidate contract baseline)
Referent Registry        1.0.0
knowledge-model bundle   sha256:07fe0527ab29a4b40870efdd0c9e0c67c91de919e5428047245b2a2c04f8ea98
```

The supplied rc.3 release metadata has an unresolved commit SHA. Da’at must therefore distinguish a frozen contract baseline from an immutable published release claim. Existing downstream locks remain scope-specific until explicitly updated.

## Responsibilities

- validate the declared external/IK profile and exact contract version;
- map immutable source-owned exports/evidence into Kristal-native inputs;
- preserve source identity, provenance, referent-candidate status and epistemic labels;
- invoke Kristal-native contracts/tools;
- validate produced artifacts against the applicable contract set;
- return receipts/events with Kristal-owned ArtifactRefs;
- preserve Working/Reference status, validation/recognition metadata and Reader Policy references.

## Non-responsibilities

Da’at does not:

- make acquisition evidence epistemically valid merely by mapping it;
- add ecosystem-only fields to Kristal core schemas;
- collapse compilation, validation and recognition into one gate;
- interpret a signature as epistemic recognition;
- own physical Runtime Pack activation;
- read/write another product's live operational database as part of Kristal compilation;
- maintain bidirectional authority synchronization;
- treat derived query/projection stores as authoritative state.

See [`../40-integration/knowledge-projection.md`](../40-integration/knowledge-projection.md).
