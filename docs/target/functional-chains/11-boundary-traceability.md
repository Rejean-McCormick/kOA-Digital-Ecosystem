# 11 — Boundary-to-chain traceability and open interfaces

**Status:** `TARGET_DESIGN`. This is a *projection* of the 26 owner-to-owner links in [`boundaries.v1.json`](../boundaries.v1.json). Their `target_design_not_qualified` status is preserved exactly. Existing local qualification for a particular IK profile does **not** promote the entire final chain.

## Existing C0 target-link register (all 26)

| Target edge | Producer → consumer | Handoff purpose | Functional specification(s) | Exact interface in registry |
|---|---|---|---|---|
| `B-KNOW-01` | Skope → Mediatheque | Submit reviewed noncanonical source evidence for durable custody | [FC-01](chains/FC-01-research-and-acquisition.md), [FC-02](chains/FC-02-source-custody.md) | `TBD` (owner agreement required) |
| `B-KNOW-02` | Mediatheque → Daat | Present preserved source references for explicit mapping/admission | [FC-02](chains/FC-02-source-custody.md), [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) | `TBD` (owner agreement required) |
| `B-KNOW-03` | Daat → Kristal-Authoring-Kit | Deliver versioned, explicitly authorized mapping data for authoring | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md) | `TBD` (owner agreement required) |
| `B-KNOW-04` | diK → Kristal-Authoring-Kit | Offer approved lexical catalogs with independent semantic identities | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md) | `TBD` (owner agreement required) |
| `B-KNOW-05` | Kristalizer → Kristal-Authoring-Kit | Stage explicitly reviewed reconciliation proposals | [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-04](chains/FC-04-semantic-authoring.md) | `TBD` (owner agreement required) |
| `B-KNOW-06` | Kristal-Framework → Kristal-Authoring-Kit | Define exact canonical semantic identity and build-profile conformance | [FC-04](chains/FC-04-semantic-authoring.md) | `TBD` (owner agreement required) |
| `B-KNOW-07` | Kristal-Authoring-Kit → KristalDiag | Submit exact local-build candidate for independent qualification | [FC-04](chains/FC-04-semantic-authoring.md), [FC-05](chains/FC-05-knowledge-release.md), [FC-18](chains/FC-18-diagnostics-and-audit.md) | `TBD` (owner agreement required) |
| `B-KNOW-08` | Kristal-Authoring-Kit → Kristal-Manager | Register local instance and eligible source revisions | [FC-04](chains/FC-04-semantic-authoring.md), [FC-05](chains/FC-05-knowledge-release.md) | `TBD` (owner agreement required) |
| `B-KNOW-09` | Kristal-Manager → kristal-public | Offer explicitly approved and qualified immutable publication candidate | [FC-05](chains/FC-05-knowledge-release.md) | `TBD` (owner agreement required) |
| `B-KNOW-10` | Kristal-Framework → Kristal-Integration-Pack | Provide pinned v11 graph to derive read-only consumer views | [FC-04](chains/FC-04-semantic-authoring.md), [FC-06](chains/FC-06-knowledge-consumption.md) | `TBD` (owner agreement required) |
| `B-KNOW-11` | Kristal-Integration-Pack → Kompiler | Provide validated derived read view for local context preparation | [FC-06](chains/FC-06-knowledge-consumption.md) | `TBD` (owner agreement required) |
| `B-KNOW-12` | Kristal-Integration-Pack → EncyKlopedia | Provide read-only public encyclopedia data after content authorization | [FC-06](chains/FC-06-knowledge-consumption.md) | `TBD` (owner agreement required) |
| `B-KNOW-13` | kristal-public → Konstellation | Expose immutable approved read-surface collection for navigation | [FC-05](chains/FC-05-knowledge-release.md), [FC-06](chains/FC-06-knowledge-consumption.md), [FC-19](chains/FC-19-offline-portability.md) | `TBD` (owner agreement required) |
| `B-KNOW-14` | Skope → Kristalizer | Offer optional noncanonical research candidates for human reconciliation | [FC-01](chains/FC-01-research-and-acquisition.md), [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) | `TBD` (owner agreement required) |
| `B-CIVIC-01` | Konnaxion → Orgo | Execute finalized civic decision as governed work | [FC-07](chains/FC-07-civic-deliberation.md), [FC-08](chains/FC-08-governed-execution.md), [FC-23](chains/FC-23-external-interop.md) | governance.decision.execute/1.0.0 |
| `B-CIVIC-02` | Orgo → Konnaxion | Publish durable reconciled operational impact to civic accountability | [FC-08](chains/FC-08-governed-execution.md), [FC-07](chains/FC-07-civic-deliberation.md), [FC-23](chains/FC-23-external-interop.md) | accountability.impact.publish/1.0.0 |
| `B-CIVIC-03` | Konnaxion-Worlds → Konnaxion | Provide owner-controlled WorldRelease and Universe/World context | [FC-09](chains/FC-09-world-contexts.md), [FC-07](chains/FC-07-civic-deliberation.md) | `TBD` (owner agreement required) |
| `B-EDU-01` | Kontexte → Kompose | Provide culturally scoped educational situations for plan/simulation | [FC-10](chains/FC-10-education-design.md) | `TBD` (owner agreement required) |
| `B-EDU-02` | Kompose → Orgo | Request actual educational operational tasks only after explicit authority | [FC-10](chains/FC-10-education-design.md), [FC-08](chains/FC-08-governed-execution.md) | `TBD` (owner agreement required) |
| `B-EDU-03` | Akor → Orgo | Request governed collaborative-learning mission operations | [FC-10](chains/FC-10-education-design.md), [FC-08](chains/FC-08-governed-execution.md) | `TBD` (owner agreement required) |
| `B-EDU-04` | Ekole → UCKK-Ops-Console | Propose owner-approved learning content/projection operations | [FC-11](chains/FC-11-learning-delivery.md) | `TBD` (owner agreement required) |
| `B-PLAT-01` | Koali-Control-Panel → kOA-Linux-Koali | Drive authorized local build and profile verification actions | [FC-16](chains/FC-16-platform-lifecycle.md) | `TBD` (owner agreement required) |
| `B-PLAT-02` | kOA-Linux-Koali → Koali-Spaces | Admit optional product presentation composition under platform policy | [FC-16](chains/FC-16-platform-lifecycle.md), [FC-17](chains/FC-17-application-composition.md) | `TBD` (owner agreement required) |
| `B-SEC-01` | Konfid → Daat | Supply scoped policy decisions to authenticated DaaT enforcement port | [FC-14](chains/FC-14-identity-and-policy.md), [FC-03](chains/FC-03-mapping-and-lexical-preparation.md), [FC-23](chains/FC-23-external-interop.md) | `TBD` (owner agreement required) |
| `B-LANG-01` | SemantiK-Architect → SemantiK_Runtime_Orchestrator | Submit pinned realization-runtime conformance evidence for release orchestration | [FC-12](chains/FC-12-language-runtime.md) | `TBD` (owner agreement required) |
| `B-LANG-02` | SemantiK-Architect → Spek | Offer reviewed short language realizations for editorial composition | [FC-12](chains/FC-12-language-runtime.md), [FC-13](chains/FC-13-editorial-publishing.md) | `TBD` (owner agreement required) |

**All 26 edges are architectural targets** in the target registry; use [owner-qualified evidence](../SNAPSHOT_RECONCILIATION.md) and the [maturity map](../../status/current.md) before asserting an adopted integration is runnable in a named deployment. The fixed Konnaxion↔Orgo local profiles have selected qualification evidence, but no general production endorsement is inferred.

## Candidate edges not yet named in the C0 boundary registry

These **functional needs** are described in individual chains but have no approved exact boundary identifier in the current 26-edge target register. Do not manufacture version strings or re-use unrelated IK contracts.

| Candidate relationship | Why it may be needed | Acceptance before registration |
|---|---|---|
| Orgo-Worlds → Orgo | Owner-specific operational WorldRelease/context | Typed owner context pin and existing-Case migration behavior tested |
| Kontexte/Kompose/Akor → Ékole | Learning previews and capsule delivery | Approved content/situation schema with no implicit real Task |
| UCKK Ops Console → Moodle owner | Institutional materialization and course/state updates | School authorization, dry-run, idempotent write receipt and reconciliation |
| Médiathèque → Ékole / UCKK | Permissioned media/content custody lookup | Library-instance ACL, provenance and version reference tests |
| Konductor → Orgo or another effect owner | Reviewable agent job request for actual work | Narrow adopted command, PEP, no direct writes, terminal receipts |
| Konnaxion/Orgo/Ékole → Koali Spaces | Optional owner UI runtime/surface contribution | Manifest/CSP probes, explicit opt-in and standalone availability |
| Karacter/Kolor → learning pack | Reviewed character sheets/palettes and licensed media | Manifest format, rights review and non-destructive import |
| Spek → public site / document publisher | Approved editorial release | Version, public disclosure authorization and correction/withdrawal |
| MediKristal → any outside product | Optional medical read/exchange | Clinical governance, patient privacy, security, consent and separate certification |
| C0 → initkoa-docs / GitHub Audit | Dated public-safe architecture/evidence export | Exact source pin and false-claim/data-leak checks |
| GF/runtime resources → SemantiK Architect | Qualified grammar execution | RuntimeSet compatibility and semantic-fidelity language fixtures |
| Kontainer → Konstellation Light | Optional portable static read | Integrity/key check and read-only import test |

## Rule for promoting a candidate edge

1. Identify actual sending and receiving **code owners**, not just UI applications or broad portfolio families.
2. Write the minimal versioned interface/profile in an owner repo, including identity, classification, retries, recovery and negative fixtures.
3. Have both owners approve the exact version and execute pinned producer/consumer tests.
4. Add a new stable edge to [`boundaries.v1.json`](../boundaries.v1.json) with `target_design_not_qualified` until evidence supports a separately recorded qualification claim.
5. Re-render [`BOUNDARIES.md`](../BOUNDARIES.md), update chain handoff/acceptance text and adjust this traceability table and tests.
6. Record qualification/deployment **separately** in the evidence/maturity views; never rewrite a design edge into a proof of production.
