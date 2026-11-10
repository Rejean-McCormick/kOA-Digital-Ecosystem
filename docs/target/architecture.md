# Final-system reference architecture

**Status:** `TARGET_DESIGN`. The ecosystem is a federation of **53 registered repository identities**, not 53 mandatory running services. Each product retains the final authority for its mutable state and accepted contracts.

## Functional topology

```text
Research (Skope/EncyK) → Custody (Médiathèque) → reviewed mapping (DaaT/diK/Kristalizer)
                                                     ↓ approval
Framework semantic identity + Authoring Kit local workspace → independent qualification
              ↓                                             ↓ explicit owner release consent
       private/local operation                  immutable collection and derived read views
                                                     ↓
                                       Integration Pack → Kompiler / EncyKlopedia / Konstellation

Civic Konnaxion finalized decisions → adopted IK intent → Orgo durable Tasks → terminal impact
Education Kontexte / Kompose / Akor → supervised learning intent → Ékole + UCKK/Moodle
Language SemantiK RuntimeSets → reviewed Spek editorial → public site (separate consent)
Security: Konfid + each owner PEP        Platform: kOA-Linux/agent/optional Koali Spaces
Operations: independent diagnostics, measured recovery, offline portability
```

These arrows are **desired handoffs, not proof of live integration**. One product can operate without unrelated chains; a local author can create a private Kristal without research, public Git or a shared UI.

## Non-negotiable ownership

| Object or decision | Owner | Boundary |
|---|---|---|
| Research scope, acquisition candidates | Skope / integrated EncyK | Noncanonical data; no automatic truth approval |
| Source, Snapshot, Representation custody | Médiathèque instance | Library access permissions and durable receiver receipt |
| KQ/KP/KA/KS identity and semantic conformance | Framework / approved authoring authority | Separate from Wikidata Q/P and lexical labels |
| Local semantic workspace and build | Authoring Kit / workspace author | Build does not authorize publication |
| Product release audience and destination | Explicit content/release owner | Independent qualification is evidence only |
| Civic participation and DecisionRecord | Konnaxion | Not an Orgo Case or Task |
| Durable execution, outbox and reconciliation | Orgo | No external direct database writes |
| Educational scenario and learning projection | Kontexte/Kompose/Akor; Ékole/UCKK | Preview is not a Moodle/Orgo write |
| Language realization and grammar runtime | SemantiK Architect + Runtime Orchestrator | Output does not grant truth/authority |
| Host deployment and presentation | Platform/privileged agent; optional Koali Spaces | Separate lifecycle from content publication |
| Public site/wiki and architecture map | Site owners / C0 design | Read-only publication of approved metadata |

## Operating constraints

- Treat identity, tenant/World, license, purpose and byte classification as explicit admission inputs.
- Prevent replay conflicts and unknown terminal effects from becoming duplicate real operations.
- Deny unsupported schema/Framework/RuntimeSet versions; preserve independent owner rollback.
- Prefer read-only derived representations and reproducible source-hash references.
- Do not infer public permissions from a Git repository, GUI state or diagnostic badge.

See [functional model](functional-chains/00-system-model.md), [owner map](functional-chains/01-authority-and-ownership.md), [contracts and receipts](functional-chains/02-contract-and-receipts.md), [quality constraints](functional-chains/10-quality-attributes.md), and [code-alignment backlog](CODE_ALIGNMENT_INSTRUCTIONS.md).
