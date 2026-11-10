# kOA Digital Ecosystem Documentation

The central documentation is organized around the **intended final system**, not around prior implementation generations. The source repositories remain the owners of their code, exact contracts and releases.

## Final-system entry point

- **[Cumulative functional architecture (24 chains)](target/functional-chains/README.md)** — complete destination model, dependencies, 53-repository coverage and acceptance scenarios

- [Architecture, responsibilities and end-state ownership](target/architecture.md)
- [End-to-end target journeys](target/journeys.md)
- [26 target cross-owner boundaries](target/BOUNDARIES.md)
- [53-repository role catalogue](target/PORTFOLIO.md) (machine-readable [source](target/portfolio.v1.json))
- [Cross-repository code alignment instructions](target/CODE_ALIGNMENT_INSTRUCTIONS.md)
- [Implementation evidence and qualification](status/current.md)

The target architecture deliberately distinguishes **design** from **observed implementation**, **independent qualification** and **actual runtime deployment**. Current owner READMEs describe Framework v11, Kit v4, Skope-integrated EncyK acquisition and an EncyKlopedia read-only product; the retained older v6/IK/UCKK knowledge contracts are available for compatibility reference, not the organizing architecture.

- [GitHub Wiki export and synchronization](wiki/README.md) — generated reader pages, controlled publish process

- [Consolidated owner-branch delivery evidence (9 November 2026)](integration/2026-11-09-branch-consolidation.md) — delivered files, source status and missing branch 05
- [Cross-owner handoff matrix](integration/2026-11-09-overlay-handoffs.md) — bilateral work remaining

## Technical compatibility references (not target design)

The [frozen v6 knowledge-contract set](2-Technical-Reference/40-integration/knowledge-projection-contract-set.json) and [v10 coordination ledger](2-Technical-Reference/40-integration/kristal-v10-alignment/README.md) remain available because some implementation and tests still depend on their exact IDs. **Do not** infer that the old EncyKlopedia acquisition role describes the final EncyKlopedia product.

## Wiki synchronization

The GitHub Wiki is a secondary navigation surface. The [2026-10-27 wiki reconciliation notes](status/wiki-synchronization-2026-10-27.md) identify the source status, historical baselines, correction scope and remaining verification gates. Current status, owner authority and integration profiles are maintained in this repository, not inferred from a wiki date.

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

## First-priority Konnaxion + Orgo deployment profile

The selected **VPS Linux / Docker / Capsule Agent** profile is tracked in [Tandem VPS coordination](2-Technical-Reference/40-integration/tandem-vps-capsule-agent/README.md). This is a C0 decision record with G0–G8 admission gates, **not** proof of deployment or permission to activate.

## Current owner-contract coordination (2026-10-08)

The pinned Kristal v6 projection above remains the **frozen historical lane**. For the newer EncyKlopedia→Médiathèque source handoff and Kristal v9 identity / GitHub v10 read and publication lane, see [C0 orchestration coordination](2-Technical-Reference/40-integration/orchestration-c0/README.md). These newer integrations are documented as **pending qualification** until owner evidence establishes them.

## Newer Kristal v10 alignment and Konstellation fleet navigation

The [v10 alignment pages](2-Technical-Reference/40-integration/kristal-v10-alignment/README.md) document owner responsibilities, current snapshot gaps, the proposed My Kristals navigation, and nonpublication gates. The historical v6 baseline above remains unchanged by design.
