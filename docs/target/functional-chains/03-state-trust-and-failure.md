# 03 — State machines, trust boundaries and failure behavior

**Status:** `TARGET_DESIGN` · **Applies to:** all 24 chains.

## Independent lifecycle axes

These are **different state machines**, even if the same artifact moves between them:

| Axis | Typical target progression | Authoritative owner |
|---|---|---|
| Research | scoped → acquired → reviewed → exported / rejected | Skope |
| Custody | received → validated for custody → accepted → versioned / quarantined | Médiathèque instance |
| Candidate mapping | proposed → inspected → approved / rejected → applied under review | mapping tool + approving owner |
| Semantic authoring | workspace draft → validated → local build → qualified candidate | Framework + Kit / author |
| Publication | release requested → qualified → explicitly authorized → immutable published / denied | content/release owners |
| Read consumption | pinned → import-validated → derived → presented / rejected | consumer |
| Civic decision | opened → deliberated → finalized / cancelled | Konnaxion |
| Operational effect | intent received → accepted → executing → terminal reconciled / failed | Orgo or actual effect owner |
| Teaching/learning | designed → teacher-approved → delivered → assessed / revised | education/institution owners |
| Platform | build → assessed → admitted → deployed → activated → recovered/rolled back | platform/runtime owners |
| Shell UI | discovered → manifest-admitted → ready/degraded → displayed/disabled | Koali Spaces + module owner |
| Diagnostics | request → exact-input check → signed scoped verdict | independent diagnostic owner |

`qualified`, `published`, `deployed` and `activated` **must never be collapsed into one status**. An owner may choose finer local states, but the corresponding distinctions must survive cross-owner reporting.

## Trust boundaries

1. **Unknown external source → local research:** provider-controlled bytes are untrusted; set allowlists, provenance, resource limits and inspection.
2. **Research → preservation:** custody requires byte integrity, ownership/permission checks, explicit source identity and a durable receipt; no epistemic promotion.
3. **Preservation/reconciliation → canonical workspace:** candidate terms, AI outputs, crosswalks or templates require controlled approval and exact Framework compatibility.
4. **Canonical workspace → release:** local validation is not independent qualification; independent qualification is not owner publication consent.
5. **Release → public reader:** read surfaces are derived, classification-filtered and pinned; do not expose private raw corpora or editing controls.
6. **Instruction → privileged effect:** check fresh actor/resource binding and policy at the enforcing owner. A diagnosis/report is not a capability token.
7. **Host → UI:** admitted product surfaces get routes and presentation, not shared application authority.

## Mandatory failure behavior

| Failure | Default outcome | Required evidence |
|---|---|---|
| Missing/expired identity or authorization | Deny before effect | Scoped refusal; no secrets in log |
| Unknown schema/profile or version | Reject or quarantine; no reinterpretation | Expected/observed versions |
| Digest mismatch or content alteration | Reject and preserve forensic reference safely | Input digest and receiver check |
| Duplicate identical request | Return previous receipt, no duplicate effect | Same intent/key association |
| Duplicate key with changed intent | Conflict; no effect | Original and conflicting intent hashes |
| Partial async execution | Hold pending/failed; reconcile before retry | Outbox/terminal effect state |
| Publication without explicit content scope | Block public write | Missing approval reference |
| Derived projection out of date | Keep pinned version or mark stale; never imply freshness | Source release and build time |
| Dependent service missing | Degrade this capability or stop safely; avoid global unsafe fallback | Health and dependency checks |
| Failed deployment/activation | Roll back using owner protocol, or declare manual recovery | Host-observed state and rollback receipt |
| Failed language realization or lexical coverage | Mark missing/failed; no fabricated translation | Locale and failure reason |

## Visibility and privacy

Public C0 pages describe roles, selected contracts and **safe evidence metadata** only. Raw identity data, student records, clinical data, credentials, private source bytes, unreleased workspaces, internal operator endpoints and privileged commands are excluded unless the respective owner explicitly classifies a safe public projection. Even an immutable digest may be sensitive when it identifies private data; publication of proof metadata is a separate disclosure decision.

## Recovery principle

Prefer **replay or rebuild of derived outputs** from immutable admitted source rather than copying mutable owner databases across products. Roll back each axis at its own owner boundary; do not promise that rolling back the Koali shell reverses an Orgo Task, or that withdrawing a public read surface deletes a preserved source.
