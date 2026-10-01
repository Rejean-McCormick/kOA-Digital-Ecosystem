# kOA Digital Ecosystem Documentation

This repository is the **cross-system architecture map** for kOA. It does not replace owner repositories.

## Current baseline

The current knowledge boundary is:

```text
EncyKlopedia acquisition
→ Da’at mapping
→ Kristal v6 knowledge/state canon
→ rebuildable UCKK / Univers-Cité projection
```

Current frozen contract identifiers:

- Kristal Standard `6.0.0` (`kristal.v6:jcs-rfc8785`);
- Referent Registry `kristal.referent-registry/1.0.0`;
- `encyklopedia.corpus-harvest-handoff/1.0.0`;
- IK `kristal.build.request/2.0.0` and `kristal.artifact.ready/2.0.0`;
- `uckk.univers-cite-projection/1.0.0`.

The v6 standard is pinned by manifest and core-contract digests rather than by a release-candidate Git identity.

## Authority boundaries

- Konnaxion owns civic/public source state.
- Orgo owns workflow/work state.
- EncyKlopedia owns acquisition evidence and source/provider resolution.
- Da’at owns the mapping/ACL boundary into Kristal.
- Kristal owns referent and epistemic artifact semantics.
- UCKK / Univers-Cité owns consumer projection and campus/learning state, not Kristal assertions.
- kOA-Linux owns platform contracts and release-channel coordination.
- `kristal_runtime` owns local Runtime Pack verification/active-state/rollback records.
- kOA Node Agent owns narrow privileged node-local transitions assigned by contract.
- Koali Spaces owns presentation composition and Space lifecycle.
- Interaction Kernel owns Profile/envelope semantics only where adopted.
- SemantiK Architect owns communication realization; its runtime orchestrator owns release sequencing only.

## Control views

- [System map](1-Overview/index.md)
- [Authority map](2-Technical-Reference/10-system/authority-map.md)
- [Contract map](2-Technical-Reference/40-integration/contract-map.md)
- [Knowledge acquisition/projection boundary](2-Technical-Reference/40-integration/knowledge-projection.md)
- [Current maturity map](status/current.md)
- [Conceptual Layer Model](3-Layer-Model/README.md)
- [Repository inventory](inventory/README.md)

## Start here

- [Overview](1-Overview/index.md)
- [Components](1-Overview/Components.md)
- [Artifacts](1-Overview/Artifacts.md)
- [Lifecycle](1-Overview/Lifecycle.md)
- [Integration](1-Overview/Integration.md)
- [Koali Spaces integration](1-Overview/Integration-Koali-Spaces.md)
- [Kristal v6 integration](1-Overview/Integration-Kristal-v6.md)
- [Interaction Kernel integration](1-Overview/Integration-Interaction-Kernel.md)
- [Current maturity map](status/current.md)

## Konstellation

[Contract, versions and responsibilities](2-Technical-Reference/40-integration/konstellation/index.md).
