# Klassification — consolidated classification view

**Status:** conceptual navigation / derived classification  
**Normative for kOA:** NO  
**Technical authority:** owner repositories + Digital Ecosystem authority/contract maps  
**Lineage:** consolidated from the retired `Klassification` repository (`v0.2`, last reviewed 2026-06-09)

## Purpose

Klassification is retained as a **way to read, tag, navigate and teach** the kOA architecture. It is no longer an independent authority and it does not define technical contracts.

The current relationship is:

```text
owner repositories
    own internal state, schemas, product behavior and product contracts

kOA-Digital-Ecosystem / Technical Reference
    maps cross-system authority, boundaries, contracts and evidence

kOA Layer Model
    provides the current conceptual 0–13 layer model

Klassification
    adds optional coordinates, views, passage labels and topic-navigation lenses
```

## Authority rule

A Klassification label answers questions such as:

- where does this topic sit in the conceptual layer model?
- which reading/view is being used?
- which conceptual transition is being discussed?

It does **not** answer:

- who owns an authoritative state?
- which contract/version is active?
- whether an integration is qualified?
- whether a subsystem is admitted by a kOA-Linux profile?
- whether a release or Runtime Pack is active?

For those questions, use the technical maps and owner evidence.

## Current source of truth for the 0–13 layers

The current conceptual layer definitions are:

- [`../LAYER_MODEL.md`](../LAYER_MODEL.md)
- [`../LAYER_INDEX.md`](../LAYER_INDEX.md)
- [`../layers/`](../layers/)

These already carry forward the central 0–13 structure from Klassification while explicitly declaring themselves non-normative. The old `02_axe-maitre.md` is therefore historical, not a second live axis definition.

## Retained Klassification concepts

The following concepts remain useful as **optional conceptual metadata**:

- legacy macro-zones `A–F` and transversal `X`;
- legacy coordinate syntax `K-[Zone][Layer].[Function]-[View]-P[Passage]-[Object]`;
- translation views such as native, technical, governance, pedagogical, risk/audit, memory/archive, narrative and external/partner views;
- conceptual passage labels describing transitions between functions;
- topic atlas and pedagogical classification examples.

They are retained for navigation and migration. They are not identifiers for technical contracts.

## Retired authority claims

The standalone Klassification repository described several files as “Autorité principale”. Those claims are retired by this consolidation. In particular:

- `05_passages-et-contrats.md` no longer defines technical contracts;
- `06_invariants.md` no longer overrides current owner/platform/ecosystem invariants;
- `10_glossaire.md` no longer overrides current owner or Digital Ecosystem terminology;
- the old code index does not create runtime identifiers.

The complete old repository is preserved under [`../../../archive/Klassification-v0.2/`](../../../archive/Klassification-v0.2/).

## Known legacy inconsistencies

The archived Klassification source contains at least two internal inconsistencies that are deliberately **not silently resolved**:

1. `docs/05_passages-et-contrats.md` defines passages `P0` through `P8`, while `docs/08_index-des-codes.md` additionally lists `P9 — Mémoire → nouveau mandat`. This consolidation therefore does not canonize `P9`.
2. the retired macro-zone grouping `A–F/X` differs from the current Layer Model grouping described in `LAYER_INDEX.md`. Both are preserved as different conceptual groupings; the current Layer Model is the live conceptual reference.

See [`MIGRATION_MATRIX.md`](MIGRATION_MATRIX.md) for the file-by-file disposition.
