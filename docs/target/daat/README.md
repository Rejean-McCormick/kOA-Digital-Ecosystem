# DaaT — Universal external-data onramp in the final kOA system

**Classification:** `TARGET_DESIGN` / C0 coordination, **not an adopted owner contract or a working public integration**.  
**Date:** 2026-11-13. **Owning implementation repository:** [`Rejean-McCormick/Daat`](https://github.com/Rejean-McCormick/Daat).  
**Canonical details:** DaaT `/docs/26`–`/docs/34` and DaaT owner ADR-0004 (**proposed**). C0 does not copy or supersede DaaT's runtime contracts.

## Intended user experience

**Any permitted data source → one coherent, understandable DaaT entry experience → owner-governed source/custody/mapping/review/authoring pathway**, while retaining independent rights, provenance, validation and publication.

Examples: a local PDF archive, a pinned GitHub repository, a scholarly bibliography, an Acomba read-only export, an enterprise dataset, a sensor feed, or a remote catalogue that may only be referenced rather than copied.

This is a front-door **experience**, not a claim that DaaT itself fetches all content, stores every file, issues semantic identities or grants publication rights. Existing kOA modules remain sovereign.

## Architecture across existing functional chains (do not create FC-25)

```text
External owner / user / permitted dataset
          |
          v
DaaT source intent, access-lane selection, contract/rights preview
          |
          +--> FC-01 Skope/EncyK or authorized source adapter: acquisition
          |
          +--> FC-02 Médiathèque: source, snapshot and representation custody
          |
          +--> FC-03 DaaT mapping/admission; diK/Kristalizer lexical/crosswalk review
          |             (Arketype = design-only candidate structures)
          v
FC-04 Framework + Authoring Kit: canonical local authoring and conformance
          |
          v
FC-05 independent qualification and explicit knowledge publication
          |
          +--> FC-06 approved knowledge reading/projection

FC-23 / Interaction Kernel: only owner-adopted cross-system transports,
receipts and identity-scoped effects. Konfid + receiving PEP enforce security.
```

Every arrow is conditional on **explicit approved owner interface**. Source rights and custody are distinct from admission; admission is distinct from semantic truth; local build is distinct from public release and runtime activation. No owner effect is inferred from an IK receipt's acceptance alone.

## Three independent descriptors

| Concern | Distinguish from | Reason |
|---|---|---|
| Source protocol/lane | Source content meaning | Git, PDF, ODBC or OAI-PMH describes *how* to obtain records |
| Source-content archetype | Arketype Kristal structure | A repository or ledger may contain multiple kinds of content |
| Arketype's 19 design archetypes | Framework KQ/KP/KA/KS | Structural patterns are noncanonical until authorized semantic work |
| Kintsugi Annex/Mimic | kOA owner authority | OSS parsing tools are replaceable workers, not semantic or security authorities |

The [source landscape](source-landscape.md) summarizes categories. The full **36-family research matrix** and actual proposed pilot specifications live in DaaT `/docs/27` and `/docs/31`.

## Stable boundaries and open decisions

- The **existing** DaaT v0.3.0 implementation is an offline library/CLI with synthetic host/IK/Kristal test ports. No public generic ingress or live authenticated service is proven.
- IK's `kristal.build.request/2.0.0` and portable Kristal v6 path are **not** a generic owner-approved admission for any external source.
- DaaT cannot mint KQ/KP/KA/KS, accept unreviewed external Q/P as internal identities, override a receiver's PEP, or silently promote an AI guess.
- Framework's **Draft v5 optional PROV-O/nanopublication profile** is already specified. RO-Crate is not established as a conformant native export and is optional where demanded. Neither is a new canonical format.
- Acomba/PhilPapers and every third-party source require separate permission, license and deployment verification. Credits for OSS components are required but not substitutes for permission.
- Design owners must approve actual generic IK ingress, Médiathèque disclosure, Framework/Kit revision compatibility and deployment before integration claims.

## Related C0 target material

- [External source landscape](source-landscape.md)
- [Authority and conditional handoffs](authority-and-handoffs.md)
- [Qualification and delivery gates](qualification-and-delivery.md)
- [FC-01 — acquisition](../functional-chains/chains/FC-01-research-and-acquisition.md)
- [FC-02 — custody](../functional-chains/chains/FC-02-source-custody.md)
- [FC-03 — mapping](../functional-chains/chains/FC-03-mapping-and-lexical-preparation.md)
- [FC-04 — authoring](../functional-chains/chains/FC-04-semantic-authoring.md)
- [FC-05 — release](../functional-chains/chains/FC-05-knowledge-release.md)
- [FC-23 — interop](../functional-chains/chains/FC-23-external-interop.md)
- [Current implementation maturity](../../status/current.md)
- [C0 source/snapshot reconciliation](../SNAPSHOT_RECONCILIATION.md)

**Owner documentation:** [DaaT architectural docs](https://github.com/Rejean-McCormick/Daat/tree/main/docs) — in particular `26-UNIVERSAL-DATA-ONRAMP.md`, `29-PROCESS-AND-HANDOFFS.md`, `30-KRISTAL-STANDARDS-AND-PROVENANCE.md` and `33-CODING-ROADMAP.md` **after** this package is applied to that repository.
