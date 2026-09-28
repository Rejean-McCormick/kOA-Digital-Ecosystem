# Ecosystem contract map

**Status:** current ecosystem-level reference map

This page maps important **cross-owner boundaries**. It does not duplicate owner contracts.

## Contract map

| Boundary | Producer | Contract / profile | Consumer | Authority preserved | Current state |
|---|---|---|---|---|---|
| Civic decision → governed work | Konnaxion / eThikos | `governance.decision.execute/1.0.0` via IK | Orgo | Konnaxion owns DecisionRecord; Orgo owns resulting work state | **QUALIFIED** integrated local runtime |
| Durable work impact → civic/accountability state | Orgo | `accountability.impact.publish/1.0.0` via IK | Konnaxion | Orgo owns delivery state; Konnaxion owns accepted impact/accountability state | **QUALIFIED**, including replay protections |
| Acquired corpus evidence → epistemic build | EncyKlopedia | `encyklopedia.corpus-harvest-handoff/1.0.0` + IK `kristal.build.request/1.1.0` | Da’at → Kristal | EncyKlopedia owns acquisition evidence; Kristal owns resulting epistemic artifacts | **Frozen contract baseline** |
| Operational owner snapshot → epistemic artifact | Orgo / Konnaxion / other owner | source-owned immutable export + provenance; Da’at mapping | Da’at → Kristal | Source owner retains live state; Kristal owns mapped epistemic artifact | **Selective / owner-specific** |
| Kristal artifact → Univers-Cité projection | Kristal / Da’at | IK `kristal.artifact.ready/1.1.0` + `uckk.univers-cite-projection/1.0.0` | UCKK / Univers-Cité | Kristal owns epistemic state; UCKK owns rebuildable presentation/projection state | **Frozen contract baseline** |
| Kristal artifact → deployable knowledge runtime | Kristal | Runtime Pack semantics / source artifact status | kOA-Linux knowledge channel / Release Set | Kristal owns epistemic semantics; platform owns admission/compatibility | **Specified; release identity must be pinned per artifact** |
| Admitted Runtime Pack → active runtime state | kOA-Linux platform coordination | kOA-Linux artifact/release contracts | `kristal_runtime` | `kristal_runtime` owns verification/active-state/receipts | platform contract |
| Required privileged host transition | `kristal_runtime` / authorized platform flow | kOA-Linux node-local authorized operation | kOA Node Agent | Node Agent performs only the narrow privileged transition | platform-internal |
| Product surface → global presentation | owner application | Koali integration manifest + admitted descriptors | Koali Spaces | Application keeps business authority; Koali owns presentation state | owner-specific |
| kOA local publication → online UCKK | kOA Mediatheque + Publication Gateway | kOA-Linux UCKK publication package/receipt contracts | UCKK Publication Bridge / Moodle | kOA retains local source; UCKK owns accepted remote object | platform contract |
| online UCKK learning material → private local kOA | UCKK | kOA-Linux UCKK import package/receipt contracts | UCKK Import Bridge → kOA Mediatheque | UCKK provenance preserved; accepted local copy gets local authority | platform contract |
| Konnaxion reading → UCKK Assembly context | Konnaxion | optional UCKK/Konnaxion reading contract | UCKK / Moodle | Konnaxion owns reading semantics; UCKK owns Assembly decision/permissions | documented optional boundary |
| Federated authentication → local identity | OIDC IdP | OIDC profile | participating apps | IdP owns credentials/assertion; app owns local authorization | deployment-specific |

## Frozen knowledge-contract set

The current cross-repository knowledge baseline is machine-readable in [`knowledge-projection-contract-set.json`](./knowledge-projection-contract-set.json). Human-readable ownership and release caveats are in [`knowledge-projection.md`](./knowledge-projection.md).

## Qualified Konnaxion ↔ Orgo path

```text
Konnaxion DecisionRecord
    → governance.decision.execute/1.0.0
    → Orgo Signal / Workflow / Case / Task
    → accountability.impact.publish/1.0.0
    → Konnaxion impact/accountability state
```

Required semantics include owner-local mutation, durable delivery, stable idempotency keys, terminal receipt handling, idempotent replay and divergent replay rejection. See [`orgo-konnaxion/index.md`](./orgo-konnaxion/index.md).

## Contract discipline

- Never infer a contract from repository proximity or shared UI.
- Pin explicit versions for conformance claims.
- Do not turn a candidate release tag into an immutable release claim until its commit is resolved.
- A projection/read model is not a second authoritative owner.
