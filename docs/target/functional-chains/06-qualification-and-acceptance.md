# 06 — Qualification strategy and acceptance matrix

**Status:** `TARGET_DESIGN` · **Use:** define what would prove the final functional chains, without asserting that those proofs already exist.

## Evidence ladder

| Stage | Meaning | Permitted claim |
|---|---|---|
| `DESIGNED` | This specification defines a desired owner, interface and outcome. | "Required by the target architecture" |
| `SOURCE_OBSERVED` | Exact owner source code/docs were supplied with a digest. | "Observed in supplied snapshot" |
| `OWNER_TESTED` | Product checkout passed exact tests under specified environment/profile. | "Locally tested for this revision and campaign" |
| `CROSS_OWNER_QUALIFIED` | Actual producer and consumer code ran named positive/negative fixtures with pinned schema and evidence. | "Qualified for this exact bilateral scope" |
| `RELEASE_AUTHORIZED` | Legitimate owner issued a grant for this exact content, target and scope. | "Authorized release scope" |
| `DEPLOYED_OBSERVED` | Real deployment emitted independently inspectable host/recipient receipts, monitoring and rollback confirmation. | "Observed in named environment" |

Do not turn a diagnostic pass into a publication grant, or a source file into a deployment assertion. Multiple stages may apply independently: e.g., a static document can be released without a live service, and an offline reader can be tested without an online host.

## Test suites every affected boundary should have

1. **Schema fixtures:** accepted complete payload, missing mandatory field, unknown interface/profile, unsupported version, oversized data and optional extension.
2. **Integrity/provenance:** good digest, altered bytes, unverifiable provenance, disallowed source or license, stale/withdrawn release.
3. **Identity and authorization:** valid tenant/actor, wrong tenant, missing/expired decision, denied policy, substituted resource/intent digest, bypass attempt at actual PEP.
4. **Idempotency and terminal behavior:** fresh command, exact replay, changed-intent conflict, timeout/partial completion, process restart/recovery and terminal reconciliation.
5. **Semantic safety:** KQ/KP/KA/KS namespace boundaries, external Q/P separation, unsupported draft/schema, lexical fallback/missing visibility, no derivation-as-canon promotion.
6. **Data lifecycle and disclosure:** source custody acceptance, private/public split, access class, retention/withdrawal, audit secrecy and projection rebuild.
7. **Runtime failure:** bad ReleaseSet, missing required probes, degraded dependencies, failed deployment, last-known-good rollback, isolated effect ownership.
8. **Human-in-the-loop controls:** refused approval, changed approval scope, revocation, unsafe automation and adversarial prompts/metadata.

## Minimal final-state per-chain test matrix

| Chain | Positive end state | Mandatory rejection/negative case | Evidence owner |
|---|---|---|---|
| [FC-01](chains/FC-01-research-and-acquisition.md) | Reproducible scoped noncanonical export | Unapproved provider / altered package | Skope |
| [FC-02](chains/FC-02-source-custody.md) | Durable Source/Snapshot/Representation receipt | Duplicate conflict / cross-instance read | Médiathèque instance |
| [FC-03](chains/FC-03-mapping-and-lexical-preparation.md) | Reviewable versioned mapping/crosswalk | Automatic Q/P→KQ/KP merge / missing reviewer | DaaT/diK/Kristalizer and Kit importer |
| [FC-04](chains/FC-04-semantic-authoring.md) | Deterministic Kit build under Framework pin | Wrong namespace/profile / unexpected publication | Framework + Kit |
| [FC-05](chains/FC-05-knowledge-release.md) | Independently qualified, scoped immutable release | Publish before permission / private content leak | KristalDiag, release owner, publisher |
| [FC-06](chains/FC-06-knowledge-consumption.md) | Three consumers preserve identities/read permissions | Tampered/unapproved read view / hidden fallback | Pack + adopter consumers |
| [FC-07](chains/FC-07-civic-deliberation.md) | Finalized DecisionRecord with permitted scope | Forged finalization / wrong World | Konnaxion |
| [FC-08](chains/FC-08-governed-execution.md) | Case/Task terminal effect and accountable return | Double effect after replay / accepted-as-succeeded | Orgo + admitted sender |
| [FC-09](chains/FC-09-world-contexts.md) | Compatible owner WorldRelease selected | Wrong owner/World/tenant or stale release | World owner + app |
| [FC-10](chains/FC-10-education-design.md) | Reviewed simulation and optional admitted intent | Preview creates real Task | Kontexte/Kompose/Akor + Orgo |
| [FC-11](chains/FC-11-learning-delivery.md) | Pack import and scoped Moodle projection receipt | Unapproved institutional write | Ékole + UCKK/Moodle owner |
| [FC-12](chains/FC-12-language-runtime.md) | Faithful versioned realization in supported locale | Unqualified RuntimeSet / fabricated language fallback | SemantiK / grammar / diag |
| [FC-13](chains/FC-13-editorial-publishing.md) | Attributed accessible approved editorial version | Machine output published without editorial approval | Spek / site editor |
| [FC-14](chains/FC-14-identity-and-policy.md) | Enforced bound allow decision with effect receipt | Expired permit / actor or digest substitution | Konfid + actual PEP |
| [FC-15](chains/FC-15-agentic-workflows.md) | Checkpointed job with owner-accepted effect | Prompt injection / unapproved privileged tool | Konductor + receiving owner |
| [FC-16](chains/FC-16-platform-lifecycle.md) | Qualified signed ReleaseSet and measured activation | Signed but unauthorized activation / rollback failure | Platform + host agent + diag |
| [FC-17](chains/FC-17-application-composition.md) | Product standalone and admitted shell surface | Frontend-ready with failed backend | Koali Spaces + product |
| [FC-18](chains/FC-18-diagnostics-and-audit.md) | Exact-input verifier report and safe publication | Snapshot counted as qualified test | Diagnostics / C0 / audit publisher |
| [FC-19](chains/FC-19-offline-portability.md) | Verified offline roundtrip | Corrupt/encrypted-without-key import | Kontainer / offline reader |
| [FC-20](chains/FC-20-medical-domain.md) | Authorized attributable informational domain feature | Unsupported clinical authority / patient data leak | MediKristal + independent domain safety owner |
| [FC-21](chains/FC-21-creative-assets.md) | Approved licensed versioned asset in pack | Unlicensed image/student likeness or silent revision | Karacter / Kolor / content owner |
| [FC-22](chains/FC-22-public-presence.md) | Accessible, pinned and attributable public navigation | Private evidence leak / false production badge | Site publishers and C0 |
| [FC-23](chains/FC-23-external-interop.md) | Exact bilateral schema/admission and terminal receipt | Wrong IK profile / unauthenticated native client | IK/DaaT and actual two owners |
| [FC-24](chains/FC-24-operations-and-recovery.md) | Measured recovery preserving owner state boundaries | Unreconciled uncertain effect marked completed | Affected owner + host + diag |

## Cross-chain campaigns

- **K-01:** Skope → Médiathèque idempotent handoff, source custody and review-only mapping (`S01` first three steps).
- **K-02:** Framework v11 + Kit + diK/Kristalizer compatible and incompatible fixtures, zero publication side effects (`S01` authoring / `S02`).
- **K-03:** independent knowledge release with explicit owner permission and three consumer import proofs (`S01`, `S10`).
- **C-01:** Konnaxion finalized decision → Orgo durable work → reconciled impact with same scope and idempotency (`S03`).
- **E-01:** Kontexte/Kompose/Akor preview → Ékole content pack → UCKK dry-run and approved Moodle write; with Orgo non-effect proof for preview (`S04`).
- **L-01:** SemantiK typed input → qualified RuntimeSet → reviewed Spek editorial output, including unsupported-locale failure (`S05`).
- **S-01:** Konfid decision used at actual DaaT/product PEP with blocked unauthorized request (`S07`, `S12`).
- **P-01:** ReleaseSet/host admission → measured activation → host degradation → explicit rollback; shell status follows real probes (`S06`, `S11`, `S14`).
- **A-01:** independent diagnostic → evidence-safe C0 graph → dated public audit without false qualification claims (`S13`).

Each campaign gets one **manifest**: selected exact revisions and hashes; profile and version pins; authorized data classification; participants; isolated environment; fixtures including expected failures; executed commands; raw test/receipt references; verifier revision; outcome; unqualified scope and follow-up owner. A text checklist without attached execution evidence is not a completed campaign.

## Architecture-level definition of done

The integrated final system is accepted **per declared deployment/profile and workflow**, never as an undifferentiated "53 green repos" badge. For each named profile, all **required** chains must be owner-qualified, their necessary bilateral boundaries exercised together, credentials and permissions enforced at the effect point, restoration tested, private/public disclosure reviewed, and operational claims backed by named environment observations. **Optional** chains may remain absent without lowering correctness of a minimal profile. [Code alignment work](07-code-alignment-backlog.md) orders what must be decided to make those proofs possible.
