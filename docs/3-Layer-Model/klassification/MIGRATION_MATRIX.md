# Klassification consolidation — migration matrix

**Consolidation date:** 2026-09-28  
**Source:** retired standalone `Klassification` snapshot, version `0.2`  
**Destination:** `kOA-Digital-Ecosystem`

No source text was silently rewritten into technical truth. The old repository is preserved in full under `archive/Klassification-v0.2/`.

| Former Klassification file | Disposition in Digital Ecosystem | Current status |
|---|---|---|
| `docs/00_README.md` | Replaced by this consolidated classification view + existing Layer Model README | historical source |
| `docs/01_principes.md` | Principles retained as conceptual lineage where compatible; live conceptual rules are in `docs/3-Layer-Model/README.md` | non-normative |
| `docs/02_axe-maitre.md` | Superseded by `LAYER_MODEL.md`, `LAYER_INDEX.md` and individual `layers/*` | superseded conceptual source |
| `docs/03_zones-macro.md` | Preserved as an optional legacy grouping; not merged into current Layer Model groups | legacy navigation |
| `docs/04_systeme-de-coordonnees.md` | Preserved as optional legacy classification syntax | legacy navigation |
| `docs/05_passages-et-contrats.md` | Passage labels remain conceptual; technical contract authority is `contract-map.md` + owner repositories | conceptual only |
| `docs/06_invariants.md` | Preserved for lineage; current ecosystem invariants and owner/platform invariants take precedence | historical/non-authoritative |
| `docs/07_vues-de-traduction.md` | Retained as optional reading/translation lenses | conceptual navigation |
| `docs/08_index-des-codes.md` | Preserved for migration; codes do not create technical/runtime identifiers | legacy index |
| `docs/09_exemples-de-classement.md` | Preserved as pedagogical examples only | pedagogical |
| `docs/10_glossaire.md` | Preserved for lineage; current owner and Digital Ecosystem glossaries/terminology take precedence | historical glossary |
| `docs/12_cheat-sheet-reference-card.md` | Preserved as historical reference card | historical |
| `12_atlas-des-sujets_v2.md` | Preserved as topic atlas / discovery aid | conceptual navigation |

## Authority precedence after consolidation

When a Klassification concept conflicts with a current technical source, use this order:

```text
owner repository contract / implementation evidence
    > kOA-Linux platform contract for platform-owned concerns
    > kOA-Digital-Ecosystem cross-system authority/contract mapping
    > current kOA Layer Model for conceptual orientation
    > archived Klassification v0.2 material
```

This precedence is scope-sensitive: Digital Ecosystem does not acquire internal authority from product or platform owners.

## Passages versus contracts

The old phrase “passages et contrats” combined two different ideas. They are now separated:

```text
passage
    conceptual transition / navigation lens

contract
    explicit versioned technical boundary owned by the relevant systems/protocols
```

A passage label may help describe a transition, but it never substitutes for a contract reference, Profile/version, schema, endpoint, receipt, or owner evidence.
