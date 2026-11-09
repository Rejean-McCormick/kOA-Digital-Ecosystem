# Final-system reference architecture — kOA Digital Ecosystem

**Document status:** `TARGET_DESIGN` — architectural destination, not a report of deployed functionality, a new owner contract, or authorization to publish. **Owner:** C0 / kOA Digital Ecosystem. **Source review:** user-supplied repository and wiki snapshots, 2026-11-09; no live Git state verified.

This is the **primary navigation for the intended final system**. It describes the stable functional shape to achieve; historical versions are not the organizing principle. The other documentation views retain their own purpose: owner source documents define product behavior, and [the maturity map](../status/current.md) records available implementation evidence. A desirable architecture must not be mistaken for tested integration.

## First read

0. **[Cumulative functional chains](functional-chains/README.md)**: full English functional specification across 24 bounded capabilities, including [53-repository coverage](functional-chains/05-repository-coverage.md), [cross-chain scenarios](functional-chains/04-cross-chain-compositions.md), [acceptance tests](functional-chains/06-qualification-and-acceptance.md), and [code alignment work](functional-chains/07-code-alignment-backlog.md).

1. [Architecture and ownership](architecture.md): system boundaries, responsibility split, the authority model and release lifecycle.
2. [End-to-end journeys](journeys.md): how content, operational decisions, learning and runtime releases are intended to move across owners.
3. [Target owner-to-owner boundaries](BOUNDARIES.md): 26 typed design edges, independent of the dated publication graph.
4. [Portfolio of 53 repositories](PORTFOLIO.md): one role per registered repository; flags and source pointers are preserved in [the JSON registry](portfolio.v1.json).
5. [Code snapshot reconciliation](SNAPSHOT_RECONCILIATION.md): code-snapshot evidence for the 53-owner target model, with integration gates and source references.
6. [Adjacent project survey](adjacent-projects.md): 22 additional archive folders that must not be silently omitted or automatically admitted.
7. [Implementation instructions](CODE_ALIGNMENT_INSTRUCTIONS.md): executable follow-up tasks for code and documents, acceptance tests and which repository must change.
8. [Maturity and qualification](../status/current.md): what was verified for specific versions and boundaries; it is not the target specification.

## Architectural operating rules

- **One owner per mutable authoritative state**; read models and UI do not inherit owner privileges.
- **Framework identity is distinct from language and external references**. The strict v11 profile uses KQ/KP/KA/KS namespace identifiers, separate lexical dictionaries, and reviewed Wikidata crosswalks. Exact draft compatibility must be qualified.
- **Research, custody, semantic validation, publication and rendering are independent functions.** No ingestion step canonizes a candidate, and no build automatically becomes a public release.
- **Independent qualification and explicit release authorization** gate public writes and live activation; diagnostics alone do not enforce a decision.
- **Interaction Kernel is an adopted protocol where needed, not a mandatory global bus**; direct owner contracts remain valid.
- **Koali Spaces is optional**. Apps remain individually operable and authoritative for their business logic.
- **The C0 repo documents and validates coordination only**. It must never create its own duplicate registries of live users, tasks, Kristal canons or app instances.

## Design status versus implementation evidence

| Value | Meaning |
|---|---|
| `TARGET_DESIGN` | Intended end-state responsibility or journey described here; adoption still needs approval from the owner. |
| `OWNER_SNAPSHOT` | Owner repository docs/code included in the supplied archive, not live GitHub HEAD. |
| `QUALIFIED_BOUNDARY` | Exact producer/consumer revision and independent evidence exists for the scoped boundary. |
| `DEPLOYED_OBSERVED` | Runtime/operational evidence at a named environment, not assumed from a local test. |
| `NOT_VERIFIED` | The repository archive does not establish the property. |

The 53-repository inventory does **not** imply 51 independent services: several repositories contain diagnostics, assets, content, adapters, design models, or instance templates. Likewise, folders not in the inventory are not automatically irrelevant: inclusion is a separate portfolio decision.

## Minimum definition of done for the final architecture

For every participating owner: a concise purpose, input/output contracts, owned state, forbidden responsibilities, security context, failure behavior, compatibility policy, evidence links and tests. For every *cross-owner* journey: producer and consumer release pins, schema compatibility checks, replay/idempotency where needed, authorization, observability and rollback/rebuild strategy. See the [instructions](CODE_ALIGNMENT_INSTRUCTIONS.md).
