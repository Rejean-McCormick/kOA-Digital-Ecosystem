# Functional Architecture of the Final kOA System

**Design classification:** `TARGET_DESIGN` | **Scope:** complete, federated 53-repository portfolio | **Maintainer:** kOA Digital Ecosystem / C0 | **Basis:** owner documentation and 53 code snapshots supplied on 2026-11-09.

This directory is the **cumulative functional specification** of the intended final ecosystem. It defines what the system must be capable of, which product owns each effect, which evidence can cross a boundary, how the outcome is exposed, and how to tell that the result is valid. It is **not** a claim that all described connections are currently implemented, compatible, authorized, deployed or clinically/legally certified.

## Reading order: cumulative, not one giant service pipeline

1. [00 — System and chain model](00-system-model.md): the rules shared by every functional chain.
2. [01 — Authority and ownership](01-authority-and-ownership.md): who can change what, and who cannot.
3. [02 — Interface contract and receipt model](02-contract-and-receipts.md): the shape of an admissible cross-owner handoff.
4. [03 — State, trust and failure semantics](03-state-trust-and-failure.md): the lifecycle and recovery vocabulary.
5. [Individual chains](#functional-chain-catalogue): 24 bounded end-to-end capabilities, each building on the common model and naming explicit dependencies.
6. [04 — Cross-chain compositions](04-cross-chain-compositions.md): complete user scenarios formed from selected chains.
7. [05 — Repository coverage](05-repository-coverage.md): where every one of the 53 registered repositories fits, including tools that are not deployable services.
8. [06 — Qualification and acceptance](06-qualification-and-acceptance.md): test suites, negative scenarios and target completion rules.
9. [07 — Code alignment backlog](07-code-alignment-backlog.md): changes needed in owner code or source contracts, organized by functional outcome.
10. [08 — Terminology](08-glossary.md): normative vocabulary for this documentation set.
11. [09 — Reference deployment profiles](09-reference-deployment-profiles.md): choose the smallest required set of chains for a real deployment or offline use.
12. [10 — System quality attributes](10-quality-attributes.md): performance, reliability, security, privacy and accessibility requirements across profiles.
13. [11 — Boundary traceability](11-boundary-traceability.md): all 26 registered target interfaces mapped to chains, plus candidate unapproved edges.

**Cumulative** means that every later file **inherits** the invariant rules above; a chain only states its unique responsibilities, events, data and gates. **Compositional** means an application can use one chain without being forced into all others. Some workflows run offline, some are read-only, some create durable operations, and some only render an approved view.

## Functional chain catalogue

| ID | Capability | Primary products | Main output |
|---|---|---|---|
| [FC-01](chains/FC-01-research-and-acquisition.md) | Bounded research and acquisition | Skope / integrated EncyK | Reviewed, noncanonical research package |
| [FC-02](chains/FC-02-source-custody.md) | Source custody and media preservation | Médiathèque / instances | Durable Source/Snapshot/Representation receipt |
| [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) | Mapping and lexical preparation | DaaT, diK, Kristalizer, SenTient | Reviewed, reversible candidate proposal |
| [FC-04](chains/FC-04-semantic-authoring.md) | Semantic authoring and conformance | Framework, Authoring Kit, Arketype | Locally validated Kristal state/build |
| [FC-05](chains/FC-05-knowledge-release.md) | Qualification and knowledge release | KristalDiag, Manager, kristal-public | Authorized, immutable release reference |
| [FC-06](chains/FC-06-knowledge-consumption.md) | Knowledge reading, context and exploration | Integration Pack, Kompiler, Konstellation, EncyKlopedia | Authorized, rebuildable read models |
| [FC-07](chains/FC-07-civic-deliberation.md) | Civic participation and decisions | Konnaxion | Finalized owner decision with trace |
| [FC-08](chains/FC-08-governed-execution.md) | Governed execution and accountability | Orgo / Konnaxion | Reconciled operations and civic outcome |
| [FC-09](chains/FC-09-world-contexts.md) | World / Universe and context releases | Konnaxion-Worlds, Orgo-Worlds | Versioned owner-specific WorldRelease/context |
| [FC-10](chains/FC-10-education-design.md) | Educational scenario and mission design | Kontexte, Kompose, Akor | Reviewed instructional plan or intent |
| [FC-11](chains/FC-11-learning-delivery.md) | Learning delivery and institutional projection | Ékole, content packs, UCKK | Governed local learning experience / projection |
| [FC-12](chains/FC-12-language-runtime.md) | Language realization and grammar runtimes | SemantiK Architect, Runtime Orchestrator | Faithful, traceable linguistic realization |
| [FC-13](chains/FC-13-editorial-publishing.md) | Editorial production and multilingual pages | Spek, language tools, publication clients | Editorial release distinct from canonical state |
| [FC-14](chains/FC-14-identity-and-policy.md) | Identity, security policy and enforcement | Konfid, DaaT, owner PEPs | Bound and auditable authorization outcome |
| [FC-15](chains/FC-15-agentic-workflows.md) | Bounded agentic work | Konductor, owner adapters | Reviewable job/checkpoint and approved effects |
| [FC-16](chains/FC-16-platform-lifecycle.md) | Build, admit, deploy and recover | kOA-Linux, Control Panel, Capsule Manager | Platform/runtime transition receipt |
| [FC-17](chains/FC-17-application-composition.md) | Optional application shell and navigation | Koali Spaces / product UIs | Authorized active presentation surface |
| [FC-18](chains/FC-18-diagnostics-and-audit.md) | Diagnostics, qualification and C0 evidence | KristalDiag, LevelUpDiag, KonnaxionDiag, GitHub Audit | Exact-scope independent evidence |
| [FC-19](chains/FC-19-offline-portability.md) | Portable/offline artifact workflows | Kontainer, Kit, Light, Publisher | Integrity-checked transferable artifact |
| [FC-20](chains/FC-20-medical-domain.md) | Medical-domain knowledge and pathways | MediKristal | Scoped medical knowledge feature with safety gates |
| [FC-21](chains/FC-21-creative-assets.md) | Character, palette and creative asset production | Karacter, Kolor, UCKK Assets | Reviewed, attributable creative artifact |
| [FC-22](chains/FC-22-public-presence.md) | Public discovery and documentation | Homepage, initkoa-docs, Scenario Mosaic | Dated, navigable public information |
| [FC-23](chains/FC-23-external-interop.md) | Inter-product and third-party exchange | Interaction Kernel, DaaT, owner adapters | Schema-valid, admitted owner-to-owner exchange |
| [FC-24](chains/FC-24-operations-and-recovery.md) | Observability, incident handling and recovery | Each owner, platform and control planes | Scoped evidence, recovery and continuity |

## Source of truth and precedence

- **Product owners** define their own normative APIs, schemas, decisions, exact version numbers and release policies. C0 does not overwrite those sources.
- **This directory** defines the *intended composed behavior* and design acceptance tests. Where a cross-product interface is undecided, the requirement is explicit but the identifier is `TBD`.
- [The 53-repository portfolio](../PORTFOLIO.md) and [the 26 proposed bilateral boundaries](../BOUNDARIES.md) are existing coordination registries. Not every chain has a registered edge yet: see [the code backlog](07-code-alignment-backlog.md).
- [The available evidence](../SNAPSHOT_RECONCILIATION.md) describes supplied files and their hashes. [The maturity view](../../status/current.md) records qualified claims and must not be overwritten by target prose.
- Actual source code, running infrastructure and current remote Git HEAD must be inspected separately to advance an implementation or deployment claim.

## Completion rule

A final chain is complete **only when** its owner-specific contracts, positive and negative tests, exact artifact pins, security decisions, independent cross-owner checks, rollback/rebuild behavior and appropriate deployment receipts have been demonstrated for the named scope. Until then, the document is a specification of the destination.
