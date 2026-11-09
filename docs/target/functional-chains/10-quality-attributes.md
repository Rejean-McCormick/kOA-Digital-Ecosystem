# 10 — Non-functional requirements and system-wide design constraints

**Status:** `TARGET_DESIGN`. This is the common **quality contract** expected of any chain where the requirement applies. It does not impose universal numeric service-level objectives before owners have selected deployment profiles and measured baselines.

## Quality attributes and tests

| Attribute | Architectural requirement | Minimum qualifying evidence |
|---|---|---|
| **Ownership isolation** | Product state remains writable only by the owning product; bridges may submit admitted requests but never bypass domain persistence. | Negative cross-owner write tests, permission-bound contracts and reconciled effect receipts. |
| **Integrity** | Immutable referenced evidence and releases have verifiable exact digests, provenance and approved version pins. | Corrupt bytes, substituted signatures and incompatible manifest tests fail closed. |
| **Reproducibility** | Semantic builds, diagnostic campaigns and derived views can be repeated from identified inputs. | Source/toolchain lock plus deterministic comparison or documented nondeterministic bounds. |
| **Idempotent delivery** | Commands and imports are safe under retry and out-of-order delivery where operationally relevant. | Identical replay, conflicting replay, crash-after-acceptance and terminal reconciliation fixtures. |
| **Least privilege** | Actors/workloads only get the minimum tenant/resource/action/duration necessary. | Actual PEP denial, expired token, wrong tenant and digest substitution tests. |
| **Privacy by construction** | No student, patient, account secret, private source or privileged log leaks through publication, metrics, documentation or UI shell. | Data classification reviews and adversarial public export tests. |
| **Provenance transparency** | Source, semantic, lexical, editorial and business decisions remain distinguishable and attributable. | Trace from visible output back to exact author/release/source or explicit unknown. |
| **Offline/local-first modes** | Where owner promises offline use, no implicit network dependency prevents local authoring, inspection or read. | Network-denied roundtrip and documented limitations. |
| **Accessibility** | Learning, civic, public and creative interfaces support accessible navigation and identifiable language alternatives for declared audiences. | Keyboard/screen-reader audits, contrast reviews, bilingual/locale negative tests per owner. |
| **Internationalization** | Semantic identity remains stable across locales; direct/fallback/missing lexical resolution is transparent. | Parallel multilingual fixtures and missing-lexeme disclosure. |
| **Observability** | Actual effect and health states use owner correlation IDs, bounded logs and visible degraded states. | Backtrace request→effect receipt, backend-down UI probe and privacy-safe audit. |
| **Recovery** | Each state machine has an owner-controlled rollback, replay, rebuild or manual-resolution strategy. | Failed activation, partial execution, data restore and last-known-good proof appropriate to profile. |
| **Supply-chain safety** | Executable packages, external schemas and signed release artifacts are pinned/verified before admission. | Incompatible lockfile, forged artifact, untrusted dependency and unauthorized build failures. |
| **Composability** | Optional products can be removed or unavailable without corrupting independent authoritative states. | Standalone product smoke and missing-shell/missing-read-service degradation tests. |
| **Human oversight** | High-impact public, civic, clinical, student or privileged effects require legitimate approval beyond generated advice/diagnostics. | Refusal, revocation, scope change and hostile proposal tests. |

## Profile-dependent numeric objectives — owners must specify

The final design requires an owner-approved measurement plan for **latency, throughput, retention, recovery point/time (RPO/RTO), availability, storage growth, index freshness, retry budgets, locale coverage and accessibility standards**, but does **not** fabricate thresholds here. Each deployment profile must record: objective, measurement period, percentiles if relevant, traffic/data workload, accountable owner, instrumentation, observed baseline and safe degradation behavior. An offline desktop tool and a public multi-tenant endpoint should not inherit the same arbitrary SLO.

## Security and ethical boundaries

- **School:** institutions control student identities and Moodle actions; teachers approve real-world effects; age/context safety and inclusion apply to content and visualization.
- **Healthcare:** software conformance is not clinical safety or regulatory clearance. No live patient workflows without domain consent, qualified oversight and applicable safety governance.
- **Civic:** finalized decisions have formal legitimacy rules; an execution subsystem cannot rewrite them through operational results.
- **AI agents:** untrusted model output remains a proposal; real effects pass owner authority and durable acceptance.
- **External knowledge:** research sources and public/provider identifiers are not canonical truth. Semantic approval has its own identity and provenance model.
- **Public publishing:** public URLs, Git repos and audit dashboards are disclosure surfaces. Release a selected derived view, not an entire private repository snapshot.

## Definition of done

For each chain/profile, owners explicitly classify these quality attributes as **required**, **not applicable** or **not yet qualified** and provide tests/evidence for applicable requirements. Unknown is not pass. A C0 check can test that requirements and links are present; it cannot certify medical, security, operational or production quality by itself.
