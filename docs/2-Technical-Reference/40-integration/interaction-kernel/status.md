# Interaction Kernel adoption status

Interaction Kernel is adopted **per boundary and profile version**. It is not a universal replacement for product/platform contracts.

## Qualified boundary

Konnaxion↔Orgo is qualified for:

- `governance.decision.execute/1.0.0`;
- `accountability.impact.publish/1.0.0`.

The demonstrated behavior includes DecisionRecord delivery, Orgo Signal/Workflow/Case/Task execution, durable impact publication, idempotent replay and divergent replay rejection. See [`../orgo-konnaxion/index.md`](../orgo-konnaxion/index.md).

## Frozen knowledge profiles

The knowledge acquisition/projection contract set references:

- `kristal.build.request/1.1.0`;
- `kristal.artifact.ready/1.1.0`.

These are explicit boundary contracts; they do not make IK owner of source acquisition, Kristal state or UCKK projection state.

## Additional adoption

Any other boundary claiming IK conformance must publish the Profile ID/version, authority mapping, idempotency/authentication/receipt behavior and boundary-specific evidence.
