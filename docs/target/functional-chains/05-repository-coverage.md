# 05 — Complete repository-to-chain coverage

**Classification:** `TARGET_DESIGN` based on the **53 registered repository identities** in [`portfolio.v1.json`](../portfolio.v1.json). This is a functional inclusion map, not a claim that every repository is a running service.

Each repository is assigned at least one **primary or supporting functional chain**. An entry means a responsibility in the target architecture; it does not prove a tested integration. A supporting tool such as a diagnostic, content pack, documentation portal or local template remains a separate project, not an independently required runtime.

| Registered repository | Functional chains | Source-backed target role (abbreviated) |
|---|---|---|
| `Akor` | [FC-10](chains/FC-10-education-design.md), [FC-11](chains/FC-11-learning-delivery.md) | Collaborative learner missions with complementary roles; runtime tasks remain governed by Orgo. |
| `Arketype` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md) | Non-normative archetypes, structural templates and visual plans for Kristal workspaces. |
| `Daat` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-14](chains/FC-14-identity-and-policy.md), [FC-23](chains/FC-23-external-interop.md) | Authenticated, authorized and explicitly versioned mapping boundary into owner-native contracts. |
| `diK` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md), [FC-12](chains/FC-12-language-runtime.md) | Offline multilingual dictionaries, language-coverage audits and reviewed external identifier mapping proposals. |
| `Ekole` | [FC-11](chains/FC-11-learning-delivery.md), [FC-10](chains/FC-10-education-design.md) | Reusable neutral educational engine and learner/teacher surfaces, separate from curriculum packs. |
| `Ekole-Pastorale` | [FC-11](chains/FC-11-learning-delivery.md) | Independent pastoral educational content pack consumed by the neutral Ekole engine. |
| `EncyKlopedia` | [FC-06](chains/FC-06-knowledge-consumption.md), [FC-13](chains/FC-13-editorial-publishing.md) | Read-only multilingual encyclopedia/public knowledge-delivery application, not the acquisition engine. |
| `HomePage-initkoa.org` | [FC-22](chains/FC-22-public-presence.md), [FC-13](chains/FC-13-editorial-publishing.md) | Next.js public site and initiative/reading portal with site-owned pages and build scripts; not the owner of authoritative domain data or canonical Kristal knowledge. |
| `initkoa-docs` | [FC-22](chains/FC-22-public-presence.md), [FC-18](chains/FC-18-diagnostics-and-audit.md) | MkDocs Material ecosystem documentation portal that aggregates owner wiki documentation for navigation; not a normative owner or code source of truth. |
| `Interaction-Kernel` | [FC-23](chains/FC-23-external-interop.md), [FC-07](chains/FC-07-civic-deliberation.md), [FC-08](chains/FC-08-governed-execution.md) | Versioned interoperability envelopes, profiles and portable runtimes; no participant business state. |
| `Karacter` | [FC-21](chains/FC-21-creative-assets.md), [FC-10](chains/FC-10-education-design.md) | Offline-first bilingual fictional-character creation studio with author-controlled stories, explainable character simulations, visual prompts and local exports; not a psychology diagnostic or Kristal canon owner. |
| `kOA-Digital-Ecosystem` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-22](chains/FC-22-public-presence.md), [FC-24](chains/FC-24-operations-and-recovery.md) | Architecture of the final system: roles, boundaries, contracts, target journeys and acceptance gates; C0 only. |
| `kOA-Linux-Koali` | [FC-16](chains/FC-16-platform-lifecycle.md), [FC-17](chains/FC-17-application-composition.md), [FC-24](chains/FC-24-operations-and-recovery.md) | Local-first workload platform, release/admission profiles, trust and system composition. |
| `Koali-Control-Panel` | [FC-16](chains/FC-16-platform-lifecycle.md), [FC-17](chains/FC-17-application-composition.md) | Operator/developer console for preparing, starting and observing builds without owning product state. |
| `Koali-Scenario-Mosaic` | [FC-22](chains/FC-22-public-presence.md) | Astro bilingual static-first scenario mosaic presenting 36 documented sociotechnical problems and their Koali response patterns; an editorial interface, not an operational workflow owner. |
| `Koali-Spaces` | [FC-17](chains/FC-17-application-composition.md), [FC-16](chains/FC-16-platform-lifecycle.md) | Optional application surface composition, routing and presentation; no product business-data authority. |
| `Kolor` | [FC-21](chains/FC-21-creative-assets.md), [FC-10](chains/FC-10-education-design.md) | Bilingual desktop character-sheet and palette production studio with reviewed pose/asset exports for Kontexte and Ekole layouts; not a semantic canon or application runtime owner. |
| `Kompiler` | [FC-06](chains/FC-06-knowledge-consumption.md) | Read-only context preparation from approved, derived Kristal read views. |
| `Kompose` | [FC-10](chains/FC-10-education-design.md), [FC-08](chains/FC-08-governed-execution.md) | Educational capsule design, checking and local simulation; Orgo alone executes real operational work. |
| `Konductor` | [FC-15](chains/FC-15-agentic-workflows.md), [FC-08](chains/FC-08-governed-execution.md) | Durable control plane for bounded AI workflows, checkpoints, approvals and recovery. |
| `Konfid` | [FC-14](chains/FC-14-identity-and-policy.md), [FC-23](chains/FC-23-external-interop.md) | Cross-product policy decision, scoped authorization and governed containment, without super-admin authority. |
| `Konnaxion` | [FC-07](chains/FC-07-civic-deliberation.md), [FC-08](chains/FC-08-governed-execution.md) | Owner of civic/public participation, deliberation and finalized decisions. |
| `Konnaxion-Capsule-Manager` | [FC-16](chains/FC-16-platform-lifecycle.md), [FC-07](chains/FC-07-civic-deliberation.md) | Nonprivileged capsule-management and deployment coordination, subject to independent enforcement. |
| `Konnaxion-Worlds` | [FC-09](chains/FC-09-world-contexts.md), [FC-07](chains/FC-07-civic-deliberation.md) | Canonical Universe/World control plane and isolated WorldRelease lifecycle for Konnaxion. |
| `KonnaxionDiag` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-16](chains/FC-16-platform-lifecycle.md) | Independent functional/security diagnostic campaigns and signed admission evidence for Konnaxion. |
| `Konstellation` | [FC-06](chains/FC-06-knowledge-consumption.md) | Read-only navigation and visual exploration of authorized Kristal views and collections. |
| `Konstellation-Light` | [FC-06](chains/FC-06-knowledge-consumption.md), [FC-19](chains/FC-19-offline-portability.md) | Standalone local/static reader of verified derived collection views, without publication authority. |
| `Konstellation-Publisher` | [FC-05](chains/FC-05-knowledge-release.md), [FC-19](chains/FC-19-offline-portability.md) | Fail-closed packaging and transaction rehearsal; actual remote deployment requires independent gates. |
| `Kontainer` | [FC-19](chains/FC-19-offline-portability.md), [FC-05](chains/FC-05-knowledge-release.md) | Portable, integrity-checked and optionally encrypted single-file Kristal packaging. |
| `Kontexte` | [FC-10](chains/FC-10-education-design.md) | Reusable situation/scenario definitions for learning; not a second task orchestrator. |
| `Kristal-Authoring-Kit` | [FC-04](chains/FC-04-semantic-authoring.md), [FC-05](chains/FC-05-knowledge-release.md) | Owner of local Kristal workspace authoring, structural checks and builds; not public activation. |
| `Kristal-Framework` | [FC-04](chains/FC-04-semantic-authoring.md), [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) | Owner of canonical Kristal semantic identity, state/contract semantics and conformance rules. |
| `Kristal-Integration-Pack` | [FC-06](chains/FC-06-knowledge-consumption.md), [FC-04](chains/FC-04-semantic-authoring.md), [FC-23](chains/FC-23-external-interop.md) | Non-authoritative, version-pinned bridges and derived Framework v11 read-view handoffs. |
| `Kristal-Manager` | [FC-05](chains/FC-05-knowledge-release.md), [FC-04](chains/FC-04-semantic-authoring.md) | Inventory and management of actual local Kristal instances and their controlled sync eligibility. |
| `kristal-public` | [FC-05](chains/FC-05-knowledge-release.md), [FC-06](chains/FC-06-knowledge-consumption.md) | Read-only hosted collection of specifically authorized and qualified Kristal releases. |
| `KristalDiag` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-05](chains/FC-05-knowledge-release.md) | Independent Kristal conformance and release-candidate diagnostic evidence. |
| `Kristalizer` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md) | Candidate identity reconciliation and controlled staging toward the separately installed Kit. |
| `LevelUpDiag-kOA-Linux` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-16](chains/FC-16-platform-lifecycle.md) | Independent system and release qualification campaigns for kOA-Linux. |
| `LevelUpDiag-Orgo` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-08](chains/FC-08-governed-execution.md) | Independent operational/software validation campaigns for Orgo. |
| `LevelUpDiag_SemantiK-Architect` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-12](chains/FC-12-language-runtime.md) | Independent verification of SemantiK Architect and its contracts. |
| `Mediatheque` | [FC-02](chains/FC-02-source-custody.md), [FC-11](chains/FC-11-learning-delivery.md) | Shared engine for durable source, snapshot, representation and file-version custody. |
| `Mediatheque-blank` | [FC-02](chains/FC-02-source-custody.md) | Empty isolated library-instance template using the shared Médiathèque engine. |
| `MediKristal` | [FC-20](chains/FC-20-medical-domain.md) | Independent medical knowledge/pathway platform with explicit interfaces; not clinically qualified. |
| `MediKristal-LevelUpDiag-` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-20](chains/FC-20-medical-domain.md) | Independent engineering diagnostics for MediKristal, not medical validation. |
| `Orgo` | [FC-08](chains/FC-08-governed-execution.md), [FC-24](chains/FC-24-operations-and-recovery.md) | Owner of governed Signals, Workflows, Cases, Tasks and durable execution reconciliation. |
| `Orgo-Worlds` | [FC-09](chains/FC-09-world-contexts.md), [FC-08](chains/FC-08-governed-execution.md) | Orgo-owned world model and integrations; exact target contracts reviewed via owner technical specification. |
| `SemantiK-Architect` | [FC-12](chains/FC-12-language-runtime.md), [FC-13](chains/FC-13-editorial-publishing.md) | Deterministic semantic-to-human communication planning and realization over approved inputs. |
| `SemantiK_Runtime_Orchestrator` | [FC-12](chains/FC-12-language-runtime.md), [FC-16](chains/FC-16-platform-lifecycle.md) | RuntimeSet release sequencing, integrity gates, promotion, activation and rollback. |
| `SenTient` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) | Experimental entity candidate generation and reconciliation; no semantic-canon approval. |
| `Skope` | [FC-01](chains/FC-01-research-and-acquisition.md), [FC-02](chains/FC-02-source-custody.md) | Local research scopes and the integrated EncyK source-acquisition/intake engine; no canonical promotion. |
| `Spek` | [FC-13](chains/FC-13-editorial-publishing.md), [FC-22](chains/FC-22-public-presence.md) | Independent multilingual document composition and editorial layout from typed semantic units. |
| `UCKK-Assets` | [FC-11](chains/FC-11-learning-delivery.md), [FC-21](chains/FC-21-creative-assets.md) | UCKK canonical educational/cultural content and public assets, not application or Moodle code. |
| `UCKK-Ops-Console` | [FC-11](chains/FC-11-learning-delivery.md), [FC-02](chains/FC-02-source-custody.md) | Local console for UCKK operations and bridges; no independent Moodle or Kristal authority. |

## Coverage integrity

- **53/53** registered repositories have at least one functional assignment; the assignment can be revised without changing the owner registry.
- Each owner source is recorded with its evidence path and SHA-256 in [the machine-readable portfolio](../portfolio.v1.json). A provided snapshot identifies supplied bytes, not currently deployed status.
- The target chain set also describes **cross-cutting capabilities** (identity, incident handling, release, diagnostics) that span repositories but do not become new C0-owned operational services.
- The [adjacent-project survey](../adjacent-projects.md) includes additional projects such as GF Wordbench and `uckk-moodle`. These may be important adapters or evidence sources, but are *not automatically inserted into the 53-repository register*.
- [Boundary registry](../BOUNDARIES.md) contains 26 proposed/selected target edges, fewer than all conceivable connections described here. Cross-owner interfaces without adopted identifiers are blocked pending owner decisions.

## Coverage maintenance rule

When a repository enters/leaves the registered portfolio, regenerate or manually update this table from the authoritative registry and fail validation if the identities differ. When a chain changes owner, update its owner documentation, code alignment ticket and proof gates together. **Never** make a missing service look implemented merely by assigning it to a functional row.
