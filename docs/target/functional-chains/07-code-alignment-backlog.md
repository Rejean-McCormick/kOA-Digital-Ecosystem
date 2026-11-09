# 07 — Code and contract alignment backlog for the final functional system

**Status:** `TARGET_DESIGN` / owner-implementation instructions. This is a **future-state work order**, not a report of bugs in old releases. No cross-owner permission to patch/publish/deploy is implied. The central repository can update its documentation and validators; product owners must adopt their normative interfaces and evaluate actual code at pinned revisions.

## Execution order

Do not implement a giant automatic all-product pipeline. Deliver independently useful, thin vertical slices with **exact producer + consumer code** and positive/negative fixtures. In each slice: agree on authority → pin schema/profile → implement bounded adapter → enforce policy at recipient → run two-sided tests → record receipts → update C0 only with correct evidence level. Preserve independently usable local/offline products.

## P0 — The contract and authority spine

| Work ID | Owners | Required change in the final code/contract | Completion gate | Chains |
|---|---|---|---|---|
| `P0-01` | Framework, Kit, Integration Pack, diK | Approve a single compatible Framework v11 semantic/lexical/read-view profile across exact pinned revisions; retain separate KQ/KP/KA/KS and Q/P identifiers. | Full schema fixture matrix including intentionally incompatible draft, missing lexical entry and namespace collision. | FC-03/04/06 |
| `P0-02` | Skope, Médiathèque engine + library instance | Adopt one source evidence package and durable receiver receipt: Source/Snapshot/Representation refs, checksums, provenance, license/access class, intent digest, idempotency. | Identical replay one acceptance; conflicting replay rejected; caller and recipient code pinned. | FC-01/02 |
| `P0-03` | DaaT, Konfid, Kit | Agree on an admitted mapping interface and trusted identity/policy/audit injection; reviewer approval before workspace write. | Deny when missing PEP, actor/tenant, policy, hash, profile or approval; prove no silent KQ mint. | FC-03/14/23 |
| `P0-04` | diK, Kristalizer, Kit | Introduce explicit review/import receipts and precise compatibility between dictionary candidate/crosswalk files and Kit workspace. | Approved and denied import scenarios, rollback and `draft.3`/`draft.4` mismatch coverage. | FC-03/04 |
| `P0-05` | Kit, KristalDiag, Manager, release owner, publisher | Complete build → independent exact-input qualification → per-Kristal explicit release authorization → immutable publication path. | Public-safe fixture, tampered build refusal, no grant/no publish, duplicate publish idempotency and rollback evidence. | FC-04/05/18 |
| `P0-06` | Framework, Pack, Kompiler, EncyKlopedia, Konstellation | Approve pinned derived-read contract with stable IDs, source release, language coverage/fallback, authorization and error semantics. | At least three independent read-client imports and invalid/private/stale fixtures; no canonical write. | FC-06 |
| `P0-07` | Konnaxion, Orgo, IK | Preserve already selected decision→execution→impact profiles; qualify exact intended new deployment revisions, retry and terminal reconciliation. | Full S03 scoped trace, no duplicate effect, approved tenant and real decision owner. | FC-07/08/23 |
| `P0-08` | Orgo, Kontexte, Kompose, Akor | Define safe pedagogical design/intent formats and a separately admitted Orgo operational command where real work is desired. | Preview creates no real Case/Task; teacher denial, idempotent replay and receiver authorization tested. | FC-08/10 |
| `P0-09` | Konfid, each product PEP, platform/agent | Bind enforcement to actual effect point using authenticated actor/tenant/resource/intent and short-lived obligations. | Expired/mismatched/forged decisions produce **no effect**, with bounded nonsecret audits. | FC-14, all privileged chains |
| `P0-10` | C0, owners, diagnostic publishers | Document accepted scope and evidence claims without promoting snapshots or branch templates to "passed". | Check count and proof stage per owner/campaign; exact hashes and public-safe evidence links. | FC-18/22/24 |

## P1 — Product-level complete paths

| Work ID | Owners | Required target alignment | Completion gate | Chains |
|---|---|---|---|---|
| `P1-01` | Ékole, content-pack owners, UCKK Ops Console, Moodle owner | Adopt neutral content-pack import, educational provenance, dry-run and explicit institutional Moodle write contract. | S04 with approved and denied write, locale fallback, duplicate receipt and rebuild. | FC-10/11 |
| `P1-02` | Konnaxion-Worlds, Konnaxion; Orgo-Worlds, Orgo | Publish separate WorldRelease/context schemas and product admission gates. | Wrong World/tenant, incompatible revision, rollback and business-state-preservation tests. | FC-09 |
| `P1-03` | kOA-Linux, Control Panel, Capsule Manager, KonnaxionDiag | Align build/ReleaseSet/signature/admission with real host PEP, agent action and measured activation. | No unauthorized deploy, host-side receipt, faulted service, rollback and exact profile checks. | FC-16/18/24 |
| `P1-04` | Koali Spaces, admitted product owners | Version module manifest, runtime registry, required health probes, CSP and standalone app fallback. | UI degrades on required API failure; missing shell does not destroy owner app. | FC-17 |
| `P1-05` | SemantiK Architect, GF/RuntimeSet owners, Runtime Orchestrator, diagnostics | Lock grammar and semantic input profiles; qualification and authorization before RuntimeSet promotion. | S05 full supported/unsupported locale, fail-closed runtime mismatch and rollback. | FC-12 |
| `P1-06` | Spek, site/product editorial owners | Publish editorial manifest that distinguishes source, generated wording, human review and authorized public destination. | Signed/hashed editorial output, human approve/deny, source trace and no private content. | FC-13 |
| `P1-07` | Kontainer, Publisher, Konstellation Light, release owner | Agree portable package and offline read import profile separate from live publication. | Integrity/encryption/import failure tests and S10 offline roundtrip. | FC-19 |
| `P1-08` | Each owner + independent Diag | Extend diagnostic and environment-observation receipts to support exact profile claims. | Negative campaigns pass, signatures verify, trace to correct owner revision. | FC-18/24 |
| `P1-09` | C0, initkoa-docs, Homepage, GitHub Audit | Agree publication-safe, pinned architecture/qualification export and link/navigation validation. | S13 dated public view with no secret/false status leaks and no auto-publish. | FC-22 |
| `P1-10` | Skope, Médiathèque, Ékole / UCKK as adopters | Define distinct custody→learning-media access contracts without copying source ownership. | Private media forbidden to other tenants; approved lesson media remains traceable. | FC-02/11 |

## P2 — Independent domain/optional capabilities

| Work ID | Owners | Required target alignment | Completion gate | Chains |
|---|---|---|---|---|
| `P2-01` | Konductor, Orgo, policy owner | Implement actual bounded job/checkpoint engine and **one** owner-admitted effect adapter before a general agent catalogue. | S07 interrupted/replayed/denied effect tests and prompt-injection safety. | FC-15 |
| `P2-02` | MediKristal, institutional/clinical safety owner, medical diag | Establish clinical/privacy authority and domain-specific validation before real patient deployment. | No clinical readiness claim from engineering PASS; isolation/privacy/safety review recorded. | FC-20 |
| `P2-03` | Karacter, Kolor, UCKK Assets, Kontexte/Ékole | Adopt reviewed licensed asset manifest and educational pack import; preserve fictional/creative status. | S09 rights, versioning, accessibility and prohibited-personal-image fixtures. | FC-21 |
| `P2-04` | SenTient / Kristalizer / author | Keep experimental extraction review-only, with confidence, provenance and manual rejection. | Collisions and adversarial candidates blocked from writing semantic canon. | FC-03 |
| `P2-05` | Koali Scenario Mosaic, Homepage, initkoa-docs | Expose accessible, multilingual, dated explanatory scenarios without implying deployed capabilities. | Link/claim validation and public-safe editorial approval. | FC-22 |
| `P2-06` | Independent owner ops teams | Formalize product-specific incident/recovery actions and bounded cross-owner correlation metadata. | S11 uncertain effect remains unresolved until correct owner reconciles it. | FC-24 |

## Cross-owner interface decisions still to settle

These **functional** edges appear in the final design but do not have a universally approved normative interface in the 26-edge C0 boundary catalogue. Do not invent a semver ID in these pages:

| Desired handoff | Primary decision |
|---|---|
| Skope → Médiathèque | Source package, custody library selection, classification and receipt schema |
| Médiathèque → semantic authoring | Whether DaaT, direct Kit import or another reviewed path is adopted for particular content |
| diK/Kristalizer → Kit | Exact Framework version and review/import signature |
| Framework/Pack → multiple readers | Approved derived view schema, consumer release pins and private/public scope |
| Orgo-Worlds → Orgo | WorldRelease metadata and effect of a World version change on existing Cases |
| Kontexte → Kompose; Kompose/Akor → Orgo | Preview vs executable intent semantics, teacher authority and replay policy |
| Ékole / UCKK Ops → Moodle | Institutional ownership, course mapping, dry-run, write receipt and rollback |
| SemantiK Architect → Runtime Orchestrator / Spek | RuntimeSet version/promotion and editorial acceptance boundaries |
| Konductor → any owner | Job authorization, action adapter, review and actual effect enforcement |
| Karacter/Kolor → learning pack | Creative schema, licenses, accessibility, attribute rights |
| C0 → public docs/Audit websites | Classification, publish target, data minimization, source revision selection |
| Medical domain → external products | Clinical governance, consent/privacy, purpose limitation and domain validation |

## Owner work-package format

Every implementation task should provide:

```text
Work ID / affected chains
Producer owner + consumer owner + exact baseline revisions
Normative schema / adopted profile and expected negative fixtures
Authoritative state, effect permission and actual enforcing PEP
Happy path with request/accepted/terminal receipts
Idempotency and failure/quarantine/recovery rules
Source and output digests, privacy/publication classification
Owner unit tests + bilateral tests + independent qualification
Deployment profile when applicable + operator rollback runbook
Evidence report with outcome / limitations / next blocker
```

**Updating C0:** once two owners have actually adopted an interface, add it to the machine-readable boundary registry with accepted scope and tests, then regenerate its Markdown view using `scripts/render_target_boundaries.py`. A design-only prose link does not change contract status. For additional owner-specific workstreams already scoped in the central repo, consult [`../CODE_ALIGNMENT_INSTRUCTIONS.md`](../CODE_ALIGNMENT_INSTRUCTIONS.md).
