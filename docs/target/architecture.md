# Target architecture: functions, owners and trust boundaries

**Classification:** `TARGET_DESIGN` / C0 architecture. This is how the final system **should** fit together. It is not a statement that the listed interfaces already operate end-to-end. Owner code and contracts always supersede C0 description of what is currently implemented.

## 1. Target shape: independently owned products, connected by contracts

```text
                          EXTERNAL SOURCES / PROVIDERS
                                     |
                     reviewed local scopes, evidence and intake
                                     v
                       Skope + integrated EncyK research
                                     |
                         source handoff, owner receipt
                                     v
                          Mediatheque source custody
                                     |
                    evidence references / explicit mapping
                                     v
            DaaT boundary / Authoring Kit (owner-specific route)
                                     |
                Framework v11 identity + semantic validation
               [KQ / KP / KA / KS, approved lexical split]
                                     |
                     independent checks and release gates
                                     v
            authorized, immutable published / derived read view
                    /                |                 \
                   v                 v                  v
           Konstellation          Kompiler         EncyKlopedia
           navigation          context assembly   public read-only
                                     |
                       optional learning consumers
                              Ekole / UCKK

CROSSCUTTING BUT NOT CENTRAL OWNERS OF PRODUCT STATE:
  Konnaxion civic decisions -> Orgo governed work (explicit IK profiles)
  Konfid identity/authorization policy -> owner-controlled enforcement
  kOA-Linux admission and release -> runtime activation under its owners
  Koali Spaces -> optional app presentation; Konductor -> bounded agentic jobs
  SemantiK Architect + GF -> communication; Spek -> separate publication product
  C0 / GitHub Audit -> descriptive coordination and evidence, never deployment
```

**Important:** the drawn chain is a *functional decomposition*, **not one mandatory synchronous pipeline**. Local authoring can start without Skope; a source handoff cannot automatically mint KQ identities; an app can consume a valid derived view without participating in public GitHub publication. Exact Skope → Médiathèque → Kit mappings require owner acceptance and are tracked in the [implementation instructions](CODE_ALIGNMENT_INSTRUCTIONS.md).

## 2. Responsibility and non-authority matrix

| Function | Primary owner / product | Target responsibility | Must not do |
|---|---|---|---|
| Scope discovery and acquisition engine | **Skope**, with integrated **EncyK** | Controlled local research, acquisition/intake, identity candidates, provenance and export | Claim semantic canon or automatically publish |
| Durable source preservation | **Médiathèque** engine + its separately configured instances | Source UUID, snapshots, physical and logical representations, checksums, acceptance receipts | Mint canonical Kristal identities or own business decisions |
| Public encyclopedic reading | **EncyKlopedia** | Public-facing multilingual search/read-only articles from admitted read views | Become source-acquisition engine or validator |
| External interoperability | **DaaT** + opt-in **Interaction Kernel** profiles | Explicit ACL mapping, authentication/admission, versioned payload exchange | Store owner domain state or replace owners' authorization |
| Canonical semantic rules | **Kristal Framework** | KQ/KP/KA/KS semantics, approved identity and lexical boundaries, conformance rules | Acquire raw sources or perform public activation |
| Local semantic authoring | **Kristal Authoring Kit** | Local workspaces, validation and reproducible builds under approved profiles | Grant public release permission or own global fleet |
| Lexical preparation / identity candidates | **diK**, **Kristalizer** | Reviewable dictionaries, coverage, external mapping proposals and Kit staging | Automatically merge referents or claim independent semantic authority |
| Derived adapters and contexts | **Kristal Integration Pack**, **Kompiler** | Pinned read-only transformations and context construction | Validate truth, modify canon or activate deployments |
| Local instance control | **Kristal Manager** | Instance inventory, eligibility and controlled sync proposals | Replace semantic canon or bypass release gates |
| Independent qualification | **KristalDiag**, product-specific **LevelUpDiag** and **KonnaxionDiag** | Exact-input diagnostics/qualification receipts | Enforce a live transition merely by issuing a green report |
| Publication and read hosting | Owner-authorized publisher / **kristal-public** collection | Immutable, authorized versions and reproducible derived surfaces | Assume a commit, sync or successful build equals publication authority |
| Interactive knowledge explorer | **Konstellation**, **Konstellation Light** | Authorized read-only browsing, scope-aware navigation and display | Modify semantic identities or approve publication |
| Learning / curriculum | **Ékole**, curriculum repositories, **UCKK** | Educational content packs, learner/teacher experiences and scoped projections | Become semantic canon or write uncontrolled Moodle state |
| Education situation and missions | **Kontexte**, **Kompose**, **Akor** | Situation design, educational plan/simulation and collaboration | Duplicate Orgo's actual Case/Task execution authority |
| Civic and operational decisions | **Konnaxion**, **Orgo** | Civic state/DecisionRecord and operational work respectively | Write each other's authoritative databases |
| Worlds / environments | **Konnaxion-Worlds**, **Orgo-Worlds** | World packaging/ownership within the respective application domain | Implicitly transfer cross-product business authority |
| Security policy and execution | **Konfid**, IdP, app authorization, trusted agents | Scoped decisions, enforcement contracts, audit and controlled containment | Universal super-admin privileges or unchecked autonomous enforcement |
| Agentic work control | **Konductor** | Bounded, auditable AI workflow execution | Replace Orgo's civic/business task authority |
| Platform and UI composition | **kOA-Linux**, **Koali Control Panel**, **Koali Spaces** | Admission/release, developer operations, optional experience shell | Transfer application business or semantic state ownership |
| Language and narrative | **SemantiK Architect**, **SemantiK Runtime Orchestrator**, **Spek** | Faithful realization, versioned grammar runtime promotion, independent editorial composition | Decide semantic truth or collapse release lifecycles |
| Architecture and public evidence | **kOA Digital Ecosystem** (C0) and **GitHub Audit** (separate consumer) | Source-backed maps, evidence links, controlled publication of *documentation views* | Own operational state or certify live deployments by displaying them |

### Owner-specified semantic identity for the target

Framework `11.0.0-draft.4` is the **observed owner draft**, not a certified final release. The final design intentionally preserves the v11 separation of semantic graph identities (`KQ`, `KP`, `KA`, `KS`), lexical dictionaries, and versioned external Wikidata `Q/P` crosswalks. Kit `4.0.0-draft.4` and Integration Pack `0.3.0-alpha.1` describe matching **candidates**. The diK owner README still targets `11.0.0-draft.3`: require a version-pinned compatibility matrix and proof before hardening a global contract.

## 3. Lifecycle boundaries that must remain separate

```text
SCOPE/RESEARCH -> PRESERVE SOURCE -> PROPOSE SEMANTIC MAPPING
      -> REVIEW / AUTHOR -> FRAMEWORK VALIDATION / LOCAL BUILD
      -> INDEPENDENT QUALIFICATION -> OWNER RELEASE APPROVAL
      -> IMMUTABLE PUBLICATION (if intended)
      -> CONSUMER IMPORT / READ-VIEW REBUILD
      -> OPTIONAL PLATFORM RELEASE / RUNTIME ACTIVATION
      -> OPTIONAL UI SURFACE ACTIVATION
```

Each transition must define: input reference and digest, producer/consumer owner, chosen versioned contract, authorization, idempotency and failure behavior, and receipt or replay check. In particular, *build*, *qualification*, *release*, *publication*, *activation*, *Moodle materialization* and *presentation* are distinct statuses.

## 4. Contracts are local to boundaries, never inferred from this diagram

- **Qualified local example:** Konnaxion↔Orgo `governance.decision.execute/1.0.0` and `accountability.impact.publish/1.0.0` with an explicit IK profile. This does not prove global deployment.
- **Owner-documented acquisition target:** Skope's integrated EncyK source with a Médiathèque source-storage receiver; receipt and replay acceptance are separate obligations. Do not label historical `encyklopedia.corpus-harvest-handoff/1.0.0` as the new producer contract.
- **v11 candidate reads:** Integration Pack and Kompiler can consume *derived* Framework v11 views with exact compatible tools; the final schema version/adoption and producer/consumer qualification remain gated.
- **Education target:** Ekole content packs and UCKK Moodle projections remain governed by their respective application and institutional policies. A derived educational text is not a canonical Kristal assertion.
- **Security boundary:** Konfid's policy outcome, DaaT admission, platform admission and app-local RBAC apply where adopted; any privileged effect also needs an enforcing PEP and an audit trail.

For contract identifiers that have not been approved across both owners, this document intentionally uses functional names, **not invented version strings**.

## 5. Design principles for the central repository itself

The final C0 repository should have four maintainable surfaces:

1. **Structured portfolio and boundary registry** (under `docs/target/` initially) for stable IDs, evidence references and design status. It is coordination data, not remote canonical truth.
2. **Human-facing target guides** for product purpose, global journeys, authority and deployment/release lifecycle.
3. **Owner-evidence and qualification views** that record exact snapshots/commits and maintain verified status independent of aspirations.
4. **Validation and publishing adapters** that compile/check documentation; public audit dashboards consume *pinned* C0 documents only by explicit workflow.

Do not move pre-existing legacy URLs or normative product schemas in this first increment. Incremental migration can occur when link consumers, wiki and GitHub Audit have been tested against the new navigation.

## 6. Source basis and limitations

This target was derived from user-provided owner READMEs/specs for Framework, Kit, Integration Pack, Skope, EncyKlopedia, Médiathèque, DaaT, diK, Kristalizer, Orgo, Konnaxion, Koali Spaces, Konfid, Konductor, Ékole and others. Their exact archive member names and SHA-256 evidence are in [`portfolio.v1.json`](portfolio.v1.json). Three registered website/presentation repositories are absent from the supplied bulk source archive. There has been no direct inspection of deployed runtime state or remote Git HEAD.

**Adjacent projects:** the [22-folder survey](adjacent-projects.md) identifies candidate dependencies such as GF Wordbench, `uckk-moodle` and the GitHub Audit publisher without claiming these have been admitted to the 53-repository register.
