# Final-system journeys: inputs, ownership, receipts and failure gates

**Status:** `TARGET_DESIGN`. A journey is a desired connected capability, not a claim that each handoff is implemented. **Detailed cumulative specification:** [24 functional chains](functional-chains/README.md), [complete scenarios](functional-chains/04-cross-chain-compositions.md) and [acceptance criteria](functional-chains/06-qualification-and-acceptance.md). Follow links to [ownership](architecture.md), [repository roles](PORTFOLIO.md) and [required code alignment](CODE_ALIGNMENT_INSTRUCTIONS.md).

## A. Knowledge: external source to a usable, governed read surface

| Step | Owner | Input → output in the final system | Acceptance requirement |
|---|---|---|---|
| 1. Select research perimeter | Skope | Selected local scope/profile → reproducible bounded research batch | Explicit selected source, safety bounds, audit log; nothing promoted to canon |
| 2. Acquire evidence | Skope-integrated EncyK | Reviewed QID candidates/source extract → noncanonical evidence package | Provider identity, bytes/source references, digest; replay-safe export |
| 3. Preserve | Médiathèque | Evidence package → accepted Source/Snapshot/Representation and receipt | Durable custody, unique source identity, checksum, idempotency, rejection rules |
| 4. Propose mappings | DaaT, diK, Kristalizer as relevant | Preserved source references + lexical/external candidates → reviewed mapping proposal | Separation of Wikidata Q/P from KQ/KP; no automatic canon write |
| 5. Author semantic state | Kristal Authoring Kit under Framework | Approved mappings + workspace → validated local Kristal semantic state | Exact Framework profile, KQ/KP/KA/KS identity, separate dictionary/catalog, provenance |
| 6. Qualify | Owner-selected independent diagnostics | Local build + pinned inputs → independently inspectable qualification verdict | Reproducible source hash, verifier identity, full failing checks retained |
| 7. Authorize release | Kristal owner and release-policy authority | Qualified artifact + scoped approval → publishable immutable release | Approval for exact target scope, absence of implicit GitHub release |
| 8. Publish / make readable | Owner-authorized publisher, kristal-public as one host | Release → immutable collection reference + derived reader artifacts | Atomicity, version/digest and rollback/recovery information |
| 9. Consume | Integration Pack, Kompiler, Konstellation, EncyKlopedia, UCKK | Pinned read surface → read-only views, context or educational projection | Reader never becomes semantic authority; language fallback disclosed |

**Failure behavior:** reject an unrecognized mapping, source digest mismatch, invalid Framework profile, unapproved public target or unpinned derived view; retain an actionable receipt; no hidden partial publish or automatic promotion. The v11 owner documents establish the intended semantics, **not proof** of this complete pipeline.

## B. Civic decision to governed execution and impact

```text
Konnaxion finalized DecisionRecord
   └─ (adopted IK governance.decision.execute/1.0.0)
      Orgo Signal / Workflow / Case / Task
         └─ durable outbox, idempotent effects and terminal reconciliation
            (adopted IK accountability.impact.publish/1.0.0)
               Konnaxion-owned accountability result
```

The target preserves the already documented owner split: **Konnaxion owns decisions**; **Orgo owns operational state**. Konnaxion-Worlds and Orgo-Worlds retain separate scopes. A successful command acceptance is not a completed external effect. Cross-owner communication requires explicit tenant identity, authorization, versioned schema, idempotency and replay safety.

## C. Educational design, classroom work and learning projections

```text
Kontexte scenario → Kompose educational plan/simulation → Akor learning mission
                                       |                        |
                                    approved                 supervised
                                       v                        v
                                      Orgo governed actual work
                                                 |
                            Ekole engine + independent content pack
                                                 |
                                  UCKK-owned learning/Moodle projection
```

This is a *target composition*, not a requirement that every classroom module run as a microservice. Kontexte owns reusable scenario definitions; Kompose owns design/simulation; Akor owns collaborative learning experience; Orgo alone owns real Cases/Tasks. Ékole Core remains curriculum-neutral; content packs stay independent; UCKK maintains local institutional/Moodle authority. No automatic Moodle write is inferred from a candidate plan.

## D. Immutable knowledge publication and runtime activation

1. **Build** locally under the owner Framework/Kit version and commit.
2. **Independently qualify** exact output and dependency lock; a report is evidence, not permission.
3. **Authorize** the exact publication scope and selected target (human/owner rule).
4. **Publish** immutable release metadata and derived read surfaces, with receipts and rollback paths.
5. **Admit** a deployable runtime using kOA-Linux profile/release policies if runtime activation is required.
6. **Activate** via the correct runtime owner/privileged agent; collect host-side measured receipts.
7. **Render** through Koali Spaces only if that product surface is admitted and explicitly adopted.

`kristal_runtime`, a node agent, the product app, and Koali Spaces have **separate state machines**. Never infer Space activation from artifact publication, or release qualification from a green UI badge.

## E. Language and accessible publication

```text
Approved semantic / math input → SemantiK Architect planner / explicit ACL
  → versioned language/lexical binding → GF/realizer RuntimeSet (qualified)
  → faithful human communication

Typed semantic units + reviewed short realizations → Spek editorial layout
  → independently approved multilingual publication
```

The SemantiK Runtime Orchestrator sequences RuntimeSet qualification, promotion and rollback without owning source semantics or grammar truth. `diK` may prepare lexical resources subject to an explicitly adopted contract; lexical availability is **not** a guarantee of translator/conformance quality. Spek is an independent editorial product, not a hidden semantic validator.

## Cross-cutting requirements for every journey

- **Identity and authorization:** tenant/workload identity and owner-local permissions, explicit Konfid/PEP contracts where adopted, least privilege.
- **Evidence:** exact input and output hashes, source/canonical version, validator version, timestamp, bounded result scope.
- **Failure and retry:** idempotency tokens, divergent replay rejection, quarantine of invalid artifacts, visible receipt state.
- **Observability:** owner-specific correlation IDs, authorized logs, and no leakage of private corpus or identities into public docs.
- **UX:** one clear entry point per product; global navigation may link products but cannot silently federate rights.
- **Language:** lexical direct/fallback/missing status disclosed; never call fallback a certified translation.

Only qualify an end-to-end journey when the **whole scoped path** has exact producer/consumer evidence. A qualified local subpath does not qualify other branches.
