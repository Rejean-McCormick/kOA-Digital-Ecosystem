# Ecosystem contract map

**Status:** ecosystem-level reference map  
**As of:** 2026-09-21

This page maps the important **cross-owner boundaries**. It does not duplicate the contracts owned by the participating repositories.

## Contract map

| Boundary | Producer | Contract / profile | Consumer | Authority preserved | Current evidence |
|---|---|---|---|---|---|
| Civic decision → governed work | Konnaxion / eThikos | `governance.decision.execute/1.0.0` via IK | Orgo | Konnaxion owns the finalized `DecisionRecord`; Orgo owns resulting Signal/Workflow/Case/Task state | **QUALIFIED 2026-09-21** in integrated local runtime |
| Durable work impact → civic/accountability state | Orgo | `accountability.impact.publish/1.0.0` via IK | Konnaxion | Orgo owns `IntegrationOperation`/delivery state; Konnaxion owns accepted impact/accountability state | **QUALIFIED 2026-09-21**, including idempotent replay and divergent replay rejection |
| Operational source state → epistemic artifact | Orgo / Konnaxion / other owner | Source-owned immutable snapshot/export + digest/revision; Da’at mapping to Kristal-native contract | Da’at → Kristal | Source owner retains live operational authority; Kristal owns resulting epistemic artifact | **Target/selective**; Da’at→Kristal v5 conformance remains separate owner work |
| Kristal artifact → deployable knowledge runtime | Kristal | Runtime Pack semantics / source artifact status | kOA-Linux knowledge channel / Release Set | Kristal owns epistemic semantics; platform owns admission/release compatibility | Kristal v5 profile is pinned; ecosystem conformance rules documented |
| Admitted Runtime Pack → active runtime state | kOA-Linux platform coordination | kOA-Linux canonical artifact/release contracts | `kristal_runtime` | `kristal_runtime` owns verification/compatibility/active-state/receipts | Platform contract; **not an IK replacement claim** |
| Required privileged host transition | `kristal_runtime` / authorized platform flow | kOA-Linux node-local authorized operation | kOA Node Agent | Node Agent performs only the narrow privileged transition | Platform-internal contract; owner-specific qualification |
| Product surface → global presentation | Owner application | Koali integration manifest + admitted surface/runtime descriptors | Koali Spaces | Application keeps business/domain authority; Koali owns shell/routing/presentation state | Konnaxion pilot evidence exists; broader app integration remains system-specific |
| Federated authentication → local application identity | OIDC IdP | OIDC profile / explicit identifiers | Konnaxion, Orgo, other participating apps | IdP owns credentials/assertion; application owns local account/authorization | Normative kOA identity profile; deployment-specific provider evidence is separate |

## Qualified Konnaxion ↔ Orgo path

```text
Konnaxion / eThikos
DecisionRecord CLOSED
        ↓ publish
DecisionRecord PUBLISHED
        ↓
InteractionEmission
        ↓
governance.decision.execute/1.0.0
        ↓
Orgo Signal → WorkflowVersion → Case → Task
        ↓
IntegrationOperation + durable delivery
        ↓
accountability.impact.publish/1.0.0
        ↓
Konnaxion-owned impact/accountability state
```

For the qualified Profile versions, semantically identical replay is idempotent and divergent reuse of the same idempotency identity is rejected.

## Contract classification

Use these labels consistently in ecosystem documentation:

- **Qualified** — executable boundary-specific evidence exists for the stated version/profile and scope.
- **Implemented** — owner implementation exists, but complete cross-owner qualification is not claimed here.
- **Target / selective** — architecture/profile is selected, but adoption or conformance is not yet proven for the full boundary.
- **Platform-internal** — kOA-Linux canonical component contract; do not relabel as IK unless the platform explicitly adopts an IK mapping.

## Boundary invariants

```text
no shared mutable database writes
no implicit distributed transaction
receiver mutates only receiver-owned state
accepted != succeeded
profile adoption is explicit and versioned
qualification is boundary-specific
```

## Evidence and owner references

- [`orgo-konnaxion/index.md`](./orgo-konnaxion/index.md)
- [`interaction-kernel/status.md`](./interaction-kernel/status.md)
- [`kristal-v5/conformance.md`](./kristal-v5/conformance.md)
- [`koali-spaces/index.md`](./koali-spaces/index.md)
- [`identity-oidc/principles.md`](./identity-oidc/principles.md)
- [`../../status/2026-09-21-konnaxion-orgo-ik-e2e-qualification.md`](../../status/2026-09-21-konnaxion-orgo-ik-e2e-qualification.md)
- [`../10-system/authority-map.md`](../10-system/authority-map.md)
