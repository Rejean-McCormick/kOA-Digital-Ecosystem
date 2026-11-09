# 01 — Ownership and authority map

**Status:** `TARGET_DESIGN`. This table states the intended boundaries; owner repository contracts and scoped approval remain authoritative for implementation.

## Ownership by kind of state

| Authoritative state or decision | Owner | Non-owner clients / forbidden shortcut |
|---|---|---|
| Research perimeter and acquisition job | Skope / integrated EncyK | Médiathèque may preserve; Kristal may later use reviewed evidence, but neither automatically accepts candidate truth. |
| Source, snapshot, representation, file version and library instance | Médiathèque engine / instance owner | Skope, Ékole and UCKK consume custody references; none overwrite the library database. |
| Canonical semantic identity and validation semantics | Kristal Framework, with owner-approved semantic authoring process | diK, Kristalizer, Arketype and external Q/P identifiers propose, label or template; they cannot mint/merge canon unilaterally. |
| Local workspace/build | Kristal Authoring Kit (in the author's approved workspace) | Manager inventories; diagnostics judge; viewers never edit. |
| Local instance/sync eligibility | Kristal Manager | Read clients and publisher do not become instance administrators. |
| Release/publish permission for a particular Kristal | Authorized content owner + release policy | Build success, CI pass, synchronization and a C0 listing are not permission. |
| Hosted authorized knowledge collection | kristal-public / authorized release publisher | Konstellation, EncyKlopedia and Kompiler only consume admitted versions. |
| Lexical catalogs and reviewed mapping proposals | diK / relevant review tools within their scoped roles | Dictionary labels are not semantic identifiers; Wikidata IDs remain external. |
| Civic participation and finalized decisions | Konnaxion | Orgo may execute adopted decisions but cannot rewrite their legitimacy. |
| Real work, Case/Task lifecycle, outbox and reconciliation | Orgo | Kompose, Akor, Konductor and Konnaxion request/observe through contracts; no direct database write. |
| Universe/World release and domain-specific World context | Konnaxion-Worlds or Orgo-Worlds respectively | Ownership stays per product; WorldRelease is not a universal cross-domain grant. |
| Educational situation, simulation and learning mission | Kontexte, Kompose and Akor respectively | They prepare learning intent; Orgo alone accepts real operational effects. |
| Neutral learning engine / independent educational content | Ékole / each content pack owner | A content pack cannot secretly rewrite engine or institution policies. |
| Campus/Moodle imports and institutional decisions | UCKK and its appointed Moodle authority | Ékole and UCKK-Ops-Console make authorized proposals, not uncontrolled remote writes. |
| Language planning and realization | SemantiK Architect | Runtime orchestrator moves qualified RuntimeSets but does not invent semantic truth. |
| Editorial documents | Spek / editorial publisher | Generated wording is not an automatically approved canonical assertion. |
| Identity and policy decision | Trust provider + Konfid and owner policies | Every actual effect is rechecked at an owner-controlled policy enforcement point (PEP). |
| Agent checkpoints and job state | Konductor | Agent plans cannot cause durable Orgo effects without accepted owner commands. |
| Artifact admission/platform runtime lifecycle | kOA-Linux / selected host runtime and authorized agents | Product releases do not self-admit. Control Panel is operator tooling, not security authority. |
| Optional shared shell/presentation | Koali Spaces | Module UIs remain independently operable; shell registration grants no product state rights. |
| Diagnostic verdict/evidence | Respective independent Diag owner | A verdict cannot perform or approve privileged state transitions. |
| Architecture map and coordinated evidence | kOA Digital Ecosystem (C0) | Descriptive only: not live canonical product state, not deployment, not source of publication permission. |
| Public presentation portals, audit dashboard | Homepage, initkoa-docs, Koali Scenario Mosaic, GitHub Audit as applicable | Read and publish only selected, classified views; not sources of owner contracts. |

## Decision rights at a boundary

A crossing has **at least two decisions**: the producer decides whether it may disclose the selected information; the consumer decides whether to admit it and how (or whether) to modify consumer-owned state. Where a privileged effect follows, the execution authority separately authorizes the action at the real enforcement point. These rights cannot be inferred from a published README, a shared library or an authenticated network connection alone.

## Interoperability roles

- **Interaction Kernel (IK):** typed envelopes/profile rules where both owners adopt them; no participant business state and no universal mandatory bus.
- **DaaT:** versioned mapping and security boundary; its current documented host-injected model is not proof of a deployed integration service.
- **Kristal Integration Pack:** derived semantic read adapters; never a second Framework.
- **Koali Spaces:** application presentation contracts; never a business data integration layer.
- **C0:** architectural coordination and evidence navigation only.

## Conflicts and missing decisions

When two products appear to claim the same mutable state, **do not pick one silently**: flag a blocked authority decision. When the interface version, owner, identity namespace, retention policy or deployment target is unknown, label the contract `TBD`; do not invent an ID to make the diagram complete. See [the actionable backlog](07-code-alignment-backlog.md).
