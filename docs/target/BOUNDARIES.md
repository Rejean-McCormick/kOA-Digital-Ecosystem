# Target owner-to-owner boundaries

> Generated from [boundaries.v1.json](boundaries.v1.json). Edit the JSON and rerun `python scripts/render_target_boundaries.py`.
> **These are intended design edges, not a qualified integration graph.** No edge grants code, release or publication authority.

**Target links:** 26. Only explicitly adopted exact interface names are recorded; `TBD` requires bilateral owner agreement.

| Journey | Producer → consumer | Purpose | Interface | Implementation acceptance gate |
|---|---|---|---|---|
| `knowledge` | **Skope → Mediatheque** (`B-KNOW-01`) | Submit reviewed noncanonical source evidence for durable custody | `TBD` | Accepted source receipt, checksums, replay-safe receiver |
| `knowledge` | **Mediatheque → Daat** (`B-KNOW-02`) | Present preserved source references for explicit mapping/admission | `TBD` | Owner-approved custody reference and access-policy proof |
| `knowledge` | **Daat → Kristal-Authoring-Kit** (`B-KNOW-03`) | Deliver versioned, explicitly authorized mapping data for authoring | `TBD` | Versioned ACL/profile and rejected-invalid-input fixtures |
| `knowledge` | **diK → Kristal-Authoring-Kit** (`B-KNOW-04`) | Offer approved lexical catalogs with independent semantic identities | `TBD` | Pinned dictionary/namespace schema and import receipt |
| `knowledge` | **Kristalizer → Kristal-Authoring-Kit** (`B-KNOW-05`) | Stage explicitly reviewed reconciliation proposals | `TBD` | Crosswalk and user-approval receipts, non-destructive test |
| `knowledge` | **Kristal-Framework → Kristal-Authoring-Kit** (`B-KNOW-06`) | Define exact canonical semantic identity and build-profile conformance | `TBD` | Pinned v11 approved profile and compatibility tests |
| `knowledge` | **Kristal-Authoring-Kit → KristalDiag** (`B-KNOW-07`) | Submit exact local-build candidate for independent qualification | `TBD` | Reproducible build inputs and independent diagnostics |
| `knowledge` | **Kristal-Authoring-Kit → Kristal-Manager** (`B-KNOW-08`) | Register local instance and eligible source revisions | `TBD` | No implicit publication or write authority; tested inventory |
| `knowledge` | **Kristal-Manager → kristal-public** (`B-KNOW-09`) | Offer explicitly approved and qualified immutable publication candidate | `TBD` | Per-Kristal authorization and atomic publish/rollback receipts |
| `knowledge` | **Kristal-Framework → Kristal-Integration-Pack** (`B-KNOW-10`) | Provide pinned v11 graph to derive read-only consumer views | `TBD` | Exact dependency pin, semantic fidelity and mismatch denial |
| `knowledge` | **Kristal-Integration-Pack → Kompiler** (`B-KNOW-11`) | Provide validated derived read view for local context preparation | `TBD` | Consumer tests for locale, crosswalk, absent source and digest mismatch |
| `knowledge` | **Kristal-Integration-Pack → EncyKlopedia** (`B-KNOW-12`) | Provide read-only public encyclopedia data after content authorization | `TBD` | Content filtering, language fallback labeling and no private leakage |
| `knowledge` | **kristal-public → Konstellation** (`B-KNOW-13`) | Expose immutable approved read-surface collection for navigation | `TBD` | Qualified collection index, reader access and integrity checks |
| `knowledge` | **Skope → Kristalizer** (`B-KNOW-14`) | Offer optional noncanonical research candidates for human reconciliation | `TBD` | Candidate-only exchange, review/consent and no canon write |
| `civic` | **Konnaxion → Orgo** (`B-CIVIC-01`) | Execute finalized civic decision as governed work | `governance.decision.execute/1.0.0` | Preserve adopted IK profile; owner-local mutations and replay tests |
| `civic` | **Orgo → Konnaxion** (`B-CIVIC-02`) | Publish durable reconciled operational impact to civic accountability | `accountability.impact.publish/1.0.0` | Terminal receipt, idempotency and accepted-versus-succeeded handling |
| `civic` | **Konnaxion-Worlds → Konnaxion** (`B-CIVIC-03`) | Provide owner-controlled WorldRelease and Universe/World context | `TBD` | Versioned world contract, tenant isolation and controlled promotion |
| `education` | **Kontexte → Kompose** (`B-EDU-01`) | Provide culturally scoped educational situations for plan/simulation | `TBD` | Bounded simulation contract and review of source scenario |
| `education` | **Kompose → Orgo** (`B-EDU-02`) | Request actual educational operational tasks only after explicit authority | `TBD` | Teacher/tenant authorization, practice isolation and idempotency |
| `education` | **Akor → Orgo** (`B-EDU-03`) | Request governed collaborative-learning mission operations | `TBD` | Learner privacy, authorization and no direct Task table writes |
| `education` | **Ekole → UCKK-Ops-Console** (`B-EDU-04`) | Propose owner-approved learning content/projection operations | `TBD` | Content-pack version, operator review and Moodle no-write preflight |
| `platform` | **Koali-Control-Panel → kOA-Linux-Koali** (`B-PLAT-01`) | Drive authorized local build and profile verification actions | `TBD` | Clean worktree, immutable profile and no admission-policy bypass |
| `platform` | **kOA-Linux-Koali → Koali-Spaces** (`B-PLAT-02`) | Admit optional product presentation composition under platform policy | `TBD` | Independent app runtime and separate Space activation receipt |
| `security` | **Konfid → Daat** (`B-SEC-01`) | Supply scoped policy decisions to authenticated DaaT enforcement port | `TBD` | Bound request digest, tenant, expiry, obligations, fail-closed PEP |
| `language` | **SemantiK-Architect → SemantiK_Runtime_Orchestrator** (`B-LANG-01`) | Submit pinned realization-runtime conformance evidence for release orchestration | `TBD` | Independent RuntimeSet build, compatibility and rollback proof |
| `language` | **SemantiK-Architect → Spek** (`B-LANG-02`) | Offer reviewed short language realizations for editorial composition | `TBD` | Versioned output, provenance, fallback and owner publication approval |

## Interpretation

Every row is scoped to a possible journey and remains `target_design_not_qualified`. For civic links, the profile name is an observed adopted identifier; the row does not assert real deployment. The currently consumed [graph registry](../inventory/graph-registry.v1.json) stays separate until the downstream publisher and owners agree on a migration.

[Architecture](architecture.md) · [Journeys](journeys.md) · [Code alignment plan](CODE_ALIGNMENT_INSTRUCTIONS.md)
