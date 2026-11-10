# 05 — Full 53-repository functional coverage

**Status:** `TARGET_DESIGN`. A named chain means a target responsibility, not a tested service.

| Repository | Chain assignments | Target role |
|---|---|---|
| `Akor` | [FC-10](chains/FC-10-education-design.md), [FC-11](chains/FC-11-learning-delivery.md) | Collaborative educational missions and role-based learning experiences; real operational Tasks remain owned by Orgo. |
| `Arketype` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md) | Non-normative modeling and template material for Kristal authoring; cannot define canonical identity. |
| `Daat` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-14](chains/FC-14-identity-and-policy.md), [FC-23](chains/FC-23-external-interop.md) | Versioned external semantic mapping, identity and policy-boundary adapters with owner-injected security gates. |
| `diK` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md), [FC-12](chains/FC-12-language-runtime.md) | Multilingual lexical dictionaries and reviewed semantic language bindings, separate from KQ/KP identity. |
| `Ekole` | [FC-11](chains/FC-11-learning-delivery.md), [FC-10](chains/FC-10-education-design.md) | Curriculum-neutral learning engine and student/teacher experience; institution and Moodle data stay separate. |
| `Ekole-Pastorale` | [FC-11](chains/FC-11-learning-delivery.md) | Independent pastoral content pack and learning material consumed by the neutral Ekole engine. |
| `EncyKlopedia` | [FC-06](chains/FC-06-knowledge-consumption.md), [FC-13](chains/FC-13-editorial-publishing.md) | Read-only multilingual encyclopedia and public derived knowledge exploration; not a source acquirer. |
| `HomePage-initkoa.org` | [FC-22](chains/FC-22-public-presence.md), [FC-13](chains/FC-13-editorial-publishing.md) | Public initiative website and editorial discovery routes; no normative authority over product software. |
| `initkoa-docs` | [FC-22](chains/FC-22-public-presence.md), [FC-18](chains/FC-18-diagnostics-and-audit.md) | MkDocs documentation portal aggregating approved owner wiki and final-system read-only documentation. |
| `Interaction-Kernel` | [FC-23](chains/FC-23-external-interop.md), [FC-07](chains/FC-07-civic-deliberation.md), [FC-08](chains/FC-08-governed-execution.md) | Opt-in typed envelope and cross-owner contract profiles; no ownership of participant business state. |
| `Karacter` | [FC-21](chains/FC-21-creative-assets.md), [FC-10](chains/FC-10-education-design.md) | Author-controlled fictional character design and narrative creative studio, not clinical or semantic canon. |
| `kOA-Digital-Ecosystem` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-22](chains/FC-22-public-presence.md), [FC-24](chains/FC-24-operations-and-recovery.md) | C0 coordination, final-system design, evidence and contract traceability; no product state authority. |
| `kOA-Linux-Koali` | [FC-16](chains/FC-16-platform-lifecycle.md), [FC-17](chains/FC-17-application-composition.md), [FC-24](chains/FC-24-operations-and-recovery.md) | Platform profiles, release admission, runtime policies and host-specific deployment authorization. |
| `Koali-Control-Panel` | [FC-16](chains/FC-16-platform-lifecycle.md), [FC-17](chains/FC-17-application-composition.md) | Operator and developer workflow UI for safe local build and platform admission preparation. |
| `Koali-Scenario-Mosaic` | [FC-22](chains/FC-22-public-presence.md) | Bilingual scenario mosaic and explanatory public interface; does not own real workflow effects. |
| `Koali-Spaces` | [FC-17](chains/FC-17-application-composition.md), [FC-16](chains/FC-16-platform-lifecycle.md) | Optional product presentation shell, navigation and Space lifecycle, separate from business state. |
| `Kolor` | [FC-21](chains/FC-21-creative-assets.md), [FC-10](chains/FC-10-education-design.md) | Character-sheet, palette and visual studio with reviewed media exports for educational content. |
| `Kompiler` | [FC-06](chains/FC-06-knowledge-consumption.md) | Local context-pack compiler from pinned derived, permitted knowledge views. |
| `Kompose` | [FC-10](chains/FC-10-education-design.md), [FC-08](chains/FC-08-governed-execution.md) | Educational scenario composition, lesson-plan preview and simulation; no direct Orgo Tasks. |
| `Konductor` | [FC-15](chains/FC-15-agentic-workflows.md), [FC-08](chains/FC-08-governed-execution.md) | Bounded agent jobs, checkpoints, operator review and mediated external action requests. |
| `Konfid` | [FC-14](chains/FC-14-identity-and-policy.md), [FC-23](chains/FC-23-external-interop.md) | Scoped identity/policy decisions requiring verification at each product effect-point enforcement port. |
| `Konnaxion` | [FC-07](chains/FC-07-civic-deliberation.md), [FC-08](chains/FC-08-governed-execution.md) | Civic decisions, participation, finalization and accountability state, never Orgo Case/Task ownership. |
| `Konnaxion-Capsule-Manager` | [FC-16](chains/FC-16-platform-lifecycle.md), [FC-07](chains/FC-07-civic-deliberation.md) | Scoped capsule deployment orchestration, platform admission and privileged agent handoff. |
| `Konnaxion-Worlds` | [FC-09](chains/FC-09-world-contexts.md), [FC-07](chains/FC-07-civic-deliberation.md) | World and Universe release/context authority for the Konnaxion civic domain. |
| `KonnaxionDiag` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-16](chains/FC-16-platform-lifecycle.md) | Independent diagnostics over pinned Konnaxion and capsule/deployment revisions. |
| `Konstellation` | [FC-06](chains/FC-06-knowledge-consumption.md) | Navigation and read-only exploration of approved semantic collections and source views. |
| `Konstellation-Light` | [FC-06](chains/FC-06-knowledge-consumption.md), [FC-19](chains/FC-19-offline-portability.md) | Lightweight static or offline read-only exploration of pinned knowledge artifacts. |
| `Konstellation-Publisher` | [FC-05](chains/FC-05-knowledge-release.md), [FC-19](chains/FC-19-offline-portability.md) | Publication transaction rehearsal and safe packaging; not implicit live deployment permission. |
| `Kontainer` | [FC-19](chains/FC-19-offline-portability.md), [FC-05](chains/FC-05-knowledge-release.md) | Integrity-checked, optionally encrypted portable knowledge and artifact containers. |
| `Kontexte` | [FC-10](chains/FC-10-education-design.md) | Reusable culturally scoped pedagogical situations for composition and supervised simulations. |
| `Kristal-Authoring-Kit` | [FC-04](chains/FC-04-semantic-authoring.md), [FC-05](chains/FC-05-knowledge-release.md) | Local semantic authoring workspace, profile-bound validation and deterministic Kristal build tooling. |
| `Kristal-Framework` | [FC-04](chains/FC-04-semantic-authoring.md), [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) | Canonical Kristal semantic identity, KQ/KP/KA/KS rules and versioned conformance profile. |
| `Kristal-Integration-Pack` | [FC-06](chains/FC-06-knowledge-consumption.md), [FC-04](chains/FC-04-semantic-authoring.md), [FC-23](chains/FC-23-external-interop.md) | Versioned derived read views and consumer adapters without canonical state ownership. |
| `Kristal-Manager` | [FC-05](chains/FC-05-knowledge-release.md), [FC-04](chains/FC-04-semantic-authoring.md) | Local instance inventory, coordination and eligible synchronization scope; not an implicit publisher. |
| `kristal-public` | [FC-05](chains/FC-05-knowledge-release.md), [FC-06](chains/FC-06-knowledge-consumption.md) | Authorized immutable public knowledge collection and read release hosting. |
| `KristalDiag` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-05](chains/FC-05-knowledge-release.md) | Independent semantic build/release diagnostics on exact pinned source and verifier revisions. |
| `Kristalizer` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md) | Reviewed mapping, identity candidate reconciliation and staged authoring import proposals. |
| `LevelUpDiag-kOA-Linux` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-16](chains/FC-16-platform-lifecycle.md) | Independent platform profile and release-readiness diagnostics; no permission to deploy. |
| `LevelUpDiag-Orgo` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-08](chains/FC-08-governed-execution.md) | Independent tests and diagnostics of Orgo operational effects and task lifecycles. |
| `LevelUpDiag_SemantiK-Architect` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-12](chains/FC-12-language-runtime.md) | Independent tests and language-runtime qualification for SemantiK Architect profiles. |
| `Mediatheque` | [FC-02](chains/FC-02-source-custody.md), [FC-11](chains/FC-11-learning-delivery.md) | Durable source, snapshot, representation and file custody with instance-scoped source receipts. |
| `Mediatheque-blank` | [FC-02](chains/FC-02-source-custody.md) | Isolated source library instance template using the shared Mediatheque custody engine. |
| `MediKristal` | [FC-20](chains/FC-20-medical-domain.md) | Medical-domain knowledge/pathways and local domain decisions; requires independent clinical authorization. |
| `MediKristal-LevelUpDiag-` | [FC-18](chains/FC-18-diagnostics-and-audit.md), [FC-20](chains/FC-20-medical-domain.md) | Engineering verification of MediKristal domain software, not medical certification. |
| `Orgo` | [FC-08](chains/FC-08-governed-execution.md), [FC-24](chains/FC-24-operations-and-recovery.md) | Durable operational Signals, Workflows, Cases, Tasks, outbox, real effects and terminal reconciliation. |
| `Orgo-Worlds` | [FC-09](chains/FC-09-world-contexts.md), [FC-08](chains/FC-08-governed-execution.md) | Operational World context and release definitions under the Orgo domain owner. |
| `SemantiK-Architect` | [FC-12](chains/FC-12-language-runtime.md), [FC-13](chains/FC-13-editorial-publishing.md) | Typed semantic-to-language planning and faithful grammatical realization under pinned runtime sets. |
| `SemantiK_Runtime_Orchestrator` | [FC-12](chains/FC-12-language-runtime.md), [FC-16](chains/FC-16-platform-lifecycle.md) | Versioned linguistic RuntimeSet qualification sequencing, promotion and rollback without source truth ownership. |
| `SenTient` | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) | Experimental extraction and evidence-derived semantic candidates subject to explicit review. |
| `Skope` | [FC-01](chains/FC-01-research-and-acquisition.md), [FC-02](chains/FC-02-source-custody.md) | Research scope selection and integrated EncyK source acquisition for noncanonical candidate/evidence packages. |
| `Spek` | [FC-13](chains/FC-13-editorial-publishing.md), [FC-22](chains/FC-22-public-presence.md) | Reviewed editorial and semantic publishing layout, distinct from canonical source authorization. |
| `UCKK-Assets` | [FC-11](chains/FC-11-learning-delivery.md), [FC-21](chains/FC-21-creative-assets.md) | Independent institutional educational media and asset packs with provenance and usage rights. |
| `UCKK-Ops-Console` | [FC-11](chains/FC-11-learning-delivery.md), [FC-02](chains/FC-02-source-custody.md) | Institutional learning/Moodle operations and approval console, not a canonical semantic owner. |

All 53 recorded owners are present exactly once in this table. Their implementation and deployment evidence is tracked separately from this architecture.
