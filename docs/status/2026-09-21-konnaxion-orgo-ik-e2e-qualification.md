# Konnaxion ↔ Orgo Interaction Kernel E2E qualification — 2026-09-21

This dated report records the successful end-to-end qualification of the selected Interaction Kernel boundary between Konnaxion/eThikos and Orgo.

## Result

**QUALIFIED — local integrated runtime evidence captured on 2026-09-21.**

The following two Profile/version pairs were exercised together through the owning product runtimes:

- `governance.decision.execute/1.0.0` — Konnaxion/eThikos → Orgo;
- `accountability.impact.publish/1.0.0` — Orgo → Konnaxion.

This closes the previously open direct Konnaxion/eThikos → Orgo handoff gap for the tested Profile versions. It does **not** claim universal IK adoption by every kOA subsystem, nor production-environment qualification.

## Qualified path

```text
Konnaxion / eThikos
DecisionRecord CLOSED
        ↓ publish
DecisionRecord PUBLISHED + canonical SHA-256 artifact
        ↓
InteractionEmission
        ↓ durable Celery delivery
governance.decision.execute/1.0.0
        ↓ authenticated IK admission
Orgo Signal
        ↓ outbox / worker
Published WorkflowVersion
        ↓
Case
        ↓
Task
        ↓
IntegrationOperation(provider = konnaxion)
        ↓ durable worker delivery
accountability.impact.publish/1.0.0
        ↓ authenticated Konnaxion ingress
OrgoImpactPublication
```

No shared mutable database write is part of this path. Each product commits its own state and crosses the boundary through authenticated, idempotent interactions.

## Observed qualification evidence

The successful run produced the following concrete runtime evidence:

```text
Konnaxion emission: delivered (attempts=1)
Orgo Signal: PROCESSED
Orgo impact operation: SUCCEEDED
Konnaxion impact publication confirmed
Replay idempotency confirmed: 1 Signal, 1 impact
Divergent replay conflict confirmed
KONNAXION <-> ORGO IK E2E PASS
```

Observed entity identifiers from the qualification run:

```text
DecisionRecord : 2
Signal         : 1a70fe31-491f-4a99-8e6e-ef4124a186cd
Case           : ade6f975-86cd-4f57-86cb-dd6e96fe6cfa
Task           : b4703346-a886-4364-ae40-4f7fb2aaee53
Impact op      : 9169d94b-6bf1-4b8e-bd42-45215005fa7f
Impact row     : 1
```

These identifiers are evidence from one run, not reusable contract identifiers.

## Idempotency and conflict behavior

The qualification explicitly exercised both required replay cases.

### Same key + same semantic interaction

The same interaction was replayed using the same idempotency identity and equivalent semantic payload.

Result:

```text
accepted replay
1 Signal total
1 Konnaxion impact total
```

No duplicate business effect was created.

### Same key + divergent semantic interaction

The same idempotency identity was reused with a different semantic interaction.

Result:

```text
HTTP 409
IK_IDEMPOTENCY_CONFLICT
```

The boundary therefore fails closed on divergent replay rather than silently accepting a conflicting business effect.

## Runtime ownership confirmed

The qualification confirms the intended ownership split:

- Konnaxion/eThikos owns `DecisionRecord`, publication state, `InteractionEmission`, and inbound impact persistence.
- Orgo owns IK admission into `Signal`, workflow/version resolution, `Case`, `Task`, `IntegrationOperation`, and its outbox/worker execution mechanics.
- Konnaxion Worlds and Orgo Worlds are not product-runtime owners for this interaction path.
- UCKK is not a mandatory relay for Konnaxion → Orgo decision execution.

## Defects closed during qualification

The runtime qualification exposed and closed several integration defects before the final PASS:

1. stale Konnaxion IK package export after contract rename;
2. invalid use of outer-class status constants inside `DecisionRecord.Meta` constraints;
3. PostgreSQL `FOR UPDATE` combined with nullable `select_related()` joins in decision publication;
4. local runtime propagation/security/scoping needed for the two product workers to communicate through the configured IK endpoints;
5. local PostgreSQL credential drift in the existing Orgo development volume.

The final run was executed after these issues were corrected.

## Qualification scope and limits

This report proves the selected application-level IK boundary in the tested local integrated runtime. It does not by itself prove:

- production TLS, certificate rotation, or production secret-management behavior;
- load, soak, failover, or multi-node high-availability characteristics;
- kOA-Linux system-image or Release Set qualification;
- IK adoption by unrelated subsystem boundaries;
- Kristal/Da’at IK Profile conformance.

Those remain separate owner-specific qualification concerns.

## Evidence authority

Product implementation remains authoritative in the owning repositories:

- Konnaxion owns the decision/publication and inbound impact behavior;
- Orgo owns Signal/Workflow/Case/Task/IntegrationOperation behavior.

This Digital Ecosystem document is the canonical **cross-product qualification record** for the demonstrated interaction. kOA-Linux may reference this result as integration evidence but must not duplicate it as a competing product authority.

## Related documentation

- `../2-Technical-Reference/40-integration/orgo-konnaxion/index.md`
- `../2-Technical-Reference/40-integration/interaction-kernel/status.md`
- `../2-Technical-Reference/90-reference/adr/adr-0007-konnaxion-ethikos-decision-authority.md`
- `../2-Technical-Reference/90-reference/adr/adr-0010-interaction-kernel-boundary.md`
