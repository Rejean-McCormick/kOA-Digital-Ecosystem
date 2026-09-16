# Integration — Interaction Kernel

Interaction Kernel (IK) is the **target system-of-systems interoperability protocol/Profile layer** for cross-product interactions such as Konnaxion↔Orgo and ecosystem↔Da’at. IK is transport/protocol semantics, not a participant database or Kristal artifact store.

## Status boundary

Digital Ecosystem must distinguish:

```text
IK target cross-system architecture
≠
kOA-Linux canonical internal/component communication contracts
```

The current kOA-Linux snapshot already defines its own registered command/query/event/job/artifact/receipt/gateway patterns. IK must not be described as having replaced those contracts until kOA-Linux and the product owners explicitly publish adoption/mapping.

## Target use

Planned/mapped Profiles include:

- `governance.decision.execute/1.0.0`;
- `accountability.impact.publish/1.0.0`;
- Kristal build/artifact/revision/distribution Profiles through Da’at.

## Rules

- Konnaxion↔Orgo is direct by default; no forced Kristal hop.
- Da’at remains the anti-corruption/mapping boundary for IK-facing Kristal work.
- Profile admission does not imply Kristal validation/recognition.
- Source-owned artifacts remain source-owned; ArtifactRef/ExportManifest identify immutable boundary artifacts without moving the live database record.
- IK must not create a distributed transaction spanning product databases and Kristal; owners commit locally and reconcile durable cross-system effects asynchronously.
- Durable interactions preserve idempotency identity and reconciliation.

## Adoption claim

A product/platform may claim IK conformance only when its owning contracts and evidence identify the Profile/version and required behavior. General build/runtime qualification is not IK conformance evidence.
