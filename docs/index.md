# kOA Digital Ecosystem Documentation

This documentation defines the **system-of-systems boundary** for kOA. Product and platform repositories remain authoritative for their own state, contracts and implementation status.

## Current alignment baseline

- Kristal: `5.0.0-rc.1`, exact tag/commit/canonicalization pin.
- kOA-Linux: current supplied docs/contracts snapshot, including Release Set, Runtime Pack, Kristal Runtime and subsystem contracts.
- Koali Spaces: current supplied product/surface-layer snapshot.
- Interaction Kernel: selected distributed interoperability protocol/Profile layer with qualified Konnaxion↔Orgo adoption for two explicit Profile/version pairs; other adoption remains boundary-specific.

## Authority boundaries

- Konnaxion owns civic/public source state.
- Orgo owns workflow/work state.
- Kristal owns epistemic artifact semantics.
- kOA-Linux owns platform contracts and release-channel coordination.
- `kristal_runtime` owns local Runtime Pack verification/active-state/rollback records in kOA-Linux.
- kOA Node Agent owns narrow privileged node-local transitions assigned by its contract.
- Koali Spaces owns presentation composition and Space lifecycle, not business or epistemic authority.
- Interaction Kernel owns protocol/Profile semantics only when/where adopted; Konnaxion↔Orgo has qualified adoption for two Profile/version pairs, and IK is not a central service.

## Key distinctions

```text
Space activation                ≠ Runtime Pack activation
Release Set compatibility       ≠ Runtime Pack epistemic validation
kristal_runtime active state    ≠ kOA Node Agent privilege authority
IK target Profile               ≠ current kOA-Linux internal communication contract
compile                         ≠ validate ≠ recognize ≠ publish ≠ activate
```

## Control views

- [System map](1-Overview/index.md#system-map)
- [Authority map](2-Technical-Reference/10-system/authority-map.md)
- [Contract map](2-Technical-Reference/40-integration/contract-map.md)
- [Maturity map](status/current.md)

## Start here

- [Overview](1-Overview/index.md)
- [Components](1-Overview/Components.md)
- [Artifacts](1-Overview/Artifacts.md)
- [Lifecycle](1-Overview/Lifecycle.md)
- [Integration](1-Overview/Integration.md)
- [Koali Spaces integration](1-Overview/Integration-Koali-Spaces.md)
- [Kristal v5 integration](1-Overview/Integration-Kristal-v5.md)
- [Interaction Kernel integration](1-Overview/Integration-Interaction-Kernel.md)
- [Current maturity map](status/current.md)
- [Detailed alignment status](status/index.md)
