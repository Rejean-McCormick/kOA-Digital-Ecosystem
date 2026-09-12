# kOA Documentation

The repository uses three documentation layers with different purposes.

## Current status

For the latest implementation/validation state, start with [`status/index.md`](status/index.md). Status pages are descriptive snapshots; ADRs and technical contracts remain authoritative.

## 1. Overview

`1-Overview/` is the readable entry point for the ecosystem: lifecycle, components, artifacts, operations, integrations, glossary, and FAQ. It explains the system without duplicating schema-level contracts.

Start with: [`1-Overview/index.md`](1-Overview/index.md)

## 2. Technical Reference

`2-Technical-Reference/` is the implementation-oriented reference for architecture, node responsibilities, kOA-native artifacts and schemas, integrations, operations, guides, and ADRs.

Start with: [`2-Technical-Reference/index.md`](2-Technical-Reference/index.md)

## 3. Layer Model

`3-Layer-Model/` is the conceptual model that explains how kOA turns meaning into knowledge, decision, action, memory, and future capacity. It does not replace the technical contracts.

Start with: [`3-Layer-Model/README.md`](3-Layer-Model/README.md)

## Canonical documentation boundaries

- Kristal v4 remains the external normative source for Kristal artifact contracts and schemas.
- kOA technical contracts live under `2-Technical-Reference/`.
- The Overview may summarize behavior but should not redefine technical contracts.
- The Layer Model is conceptual and should reference, not duplicate, technical definitions.

## Repository map

```text
docs/
├── index.md
├── status/
├── 1-Overview/
├── 2-Technical-Reference/
│   ├── 00-overview/
│   ├── 10-system/
│   ├── 20-nodes/
│   ├── 30-artifacts/
│   ├── 40-integration/
│   ├── 50-operations/
│   ├── 60-guides/
│   └── 90-reference/
└── 3-Layer-Model/
    └── layers/
```


## Decision-path correction (2026-09-12)

For Konnaxion civic/public decisions, **Konnaxion/eThikos finalizes the decision and pushes the decision handoff directly to Orgo**. UCKK is optional for publication/distribution and is not a mandatory decision authority or relay. See `2-Technical-Reference/90-reference/adr/adr-0007-konnaxion-ethikos-decision-authority.md`.
