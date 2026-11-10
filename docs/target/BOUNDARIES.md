# Target owner-to-owner boundaries

> Generated from [boundaries.v1.json](boundaries.v1.json). Edit the JSON and rerun `python scripts/render_target_boundaries.py`.
> **These are intended design edges, not a qualified integration graph.** No edge grants code, release or publication authority.

**Target links:** 26. Only explicitly adopted exact interface names are recorded; `TBD` requires bilateral owner agreement.

| Journey | Producer → consumer | Purpose | Interface | Implementation acceptance gate |
|---|---|---|---|---|
| `knowledge` | **Skope → Mediatheque** (`B-KNOW-01`) | Submit reviewed noncanonical source evidence for durable custody | `TBD` | Accepted source receipt, checksums and replay-safe receiver |
| `knowledge` | **Mediatheque → Daat** (`B-KNOW-02`) | Present preserved source references for explicit mapping and admission | `TBD` | Source custody permissions and access policy tests |
| `knowledge` | **Daat → Kristal-Authoring-Kit** (`B-KNOW-03`) | Offer reviewed allowlisted mapping data for authoring import | `TBD` | Trusted identity, schema and workspace approval tests |
| `knowledge` | **diK → Kristal-Authoring-Kit** (`B-KNOW-04`) | Offer approved lexical dictionaries with independent semantic identities | `TBD` | Pinned dictionary import schema and locale coverage tests |
| `knowledge` | **Kristalizer → Kristal-Authoring-Kit** (`B-KNOW-05`) | Stage reviewed identity and crosswalk reconciliation proposals | `TBD` | Approval and rollback receipts; no automatic canon write |
| `knowledge` | **Kristal-Framework → Kristal-Authoring-Kit** (`B-KNOW-06`) | Define exact semantic identity and conformance profile | `TBD` | Version-pinned semantic schema compatibility tests |
| `knowledge` | **Kristal-Authoring-Kit → KristalDiag** (`B-KNOW-07`) | Submit exact local builds for independent qualification | `TBD` | Verifier identity and reproducible build evidence |
| `knowledge` | **Kristal-Authoring-Kit → Kristal-Manager** (`B-KNOW-08`) | Register local authoring instances and eligible revisions | `TBD` | Read-only inventory; no implicit publication |
| `knowledge` | **Kristal-Manager → kristal-public** (`B-KNOW-09`) | Offer explicitly approved immutable publication candidates | `TBD` | Per-Kristal publication permission and rollback receipts |
| `knowledge` | **Kristal-Framework → Kristal-Integration-Pack** (`B-KNOW-10`) | Provide pinned canonical graph for derived read-view transformations | `TBD` | Semantic fidelity and invalid profile rejection |
| `knowledge` | **Kristal-Integration-Pack → Kompiler** (`B-KNOW-11`) | Provide validated derived read views for bounded local context preparation | `TBD` | Digest, privacy and lexical fallback consumer tests |
| `knowledge` | **Kristal-Integration-Pack → EncyKlopedia** (`B-KNOW-12`) | Provide approved read-only public encyclopedia information | `TBD` | Content filtering and no canonical write capability |
| `knowledge` | **kristal-public → Konstellation** (`B-KNOW-13`) | Expose an immutable authorized collection index for navigation | `TBD` | Versioned index integrity and reader access |
| `knowledge` | **Skope → Kristalizer** (`B-KNOW-14`) | Offer candidate research identities for supervised reconciliation | `TBD` | Candidate-only payload and explicit consent |
| `civic` | **Konnaxion → Orgo** (`B-CIVIC-01`) | Execute a finalized civic decision as governed work | `governance.decision.execute/1.0.0` | Adopted IK profile, idempotent receiver and effect reconciliation |
| `civic` | **Orgo → Konnaxion** (`B-CIVIC-02`) | Publish terminal operational impact for civic accountability | `accountability.impact.publish/1.0.0` | Terminal receipt and accepted-versus-succeeded handling |
| `civic` | **Konnaxion-Worlds → Konnaxion** (`B-CIVIC-03`) | Provide versioned Universe and World release context | `TBD` | Tenant isolation and owner-controlled promotion |
| `education` | **Kontexte → Kompose** (`B-EDU-01`) | Provide educational situations for simulated plan composition | `TBD` | Reviewed scenario schema and safe practice mode |
| `education` | **Kompose → Orgo** (`B-EDU-02`) | Request real educational tasks only after explicit teacher authority | `TBD` | Authorization, practice isolation and idempotency |
| `education` | **Akor → Orgo** (`B-EDU-03`) | Request governed collaborative mission operations | `TBD` | Learner privacy, no direct Task table writes |
| `education` | **Ekole → UCKK-Ops-Console** (`B-EDU-04`) | Propose approved learning content and institutional projection operations | `TBD` | Content pack version, Moodle dry-run and institution approval |
| `platform` | **Koali-Control-Panel → kOA-Linux-Koali** (`B-PLAT-01`) | Drive controlled local build and release admission workflows | `TBD` | Clean worktree and platform admission checks |
| `platform` | **kOA-Linux-Koali → Koali-Spaces** (`B-PLAT-02`) | Admit optional product presentation surfaces under platform policy | `TBD` | Separate product and Space activation receipts |
| `security` | **Konfid → Daat** (`B-SEC-01`) | Supply policy decisions for Daat actual effect enforcement | `TBD` | Bound identity, expiry, tenant and fail-closed PEP |
| `language` | **SemantiK-Architect → SemantiK_Runtime_Orchestrator** (`B-LANG-01`) | Submit qualified language-runtime conformance evidence | `TBD` | Independent RuntimeSet compatibility and rollback tests |
| `language` | **SemantiK-Architect → Spek** (`B-LANG-02`) | Offer reviewed language realizations for editorial composition | `TBD` | Versioned realization, provenance and human review |

## Interpretation

Every row is scoped to a possible journey and remains `target_design_not_qualified`. For civic links, the profile name is an observed adopted identifier; the row does not assert real deployment. The currently consumed [graph registry](../inventory/graph-registry.v1.json) stays separate until the downstream publisher and owners agree on a migration.

[Architecture](architecture.md) · [Journeys](journeys.md) · [Code alignment plan](CODE_ALIGNMENT_INSTRUCTIONS.md)
