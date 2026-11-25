# diK semantic federation — cross-owner coordination, 24 November 2026

**Status: DOCUMENTED / IMPLEMENTATION_CANDIDATE.** This record is not a
Framework contract amendment, qualification certificate, publication grant,
or decision about active Kristal revisions.

## Shared contract boundary

The canonical identity is `(namespace_id, KQ/KP)`; an unqualified `KQ1001`
is not globally unique. Wikidata `Q...` and `P...` are typed **external**
identifiers, never replacements for local KQ/KP. Wikidata L/S/F lexemes are
separate from Wikidata Q/P entity/property mappings. Labels, definitions,
translations, fallbacks and citations must remain recoverable in their
lexical/source layers; no consumer may reconstruct an ID by guessing a word.

The Framework v11 source in the 24 November SmartDump declares
`11.0.0-draft.4`, the Authoring Kit `4.0.0-draft.4` and diK package
`1.0.0a16`. The **11 vendored Framework v11 schema files** in diK match the
Framework source byte-for-byte in this snapshot. Run
`python scripts/check_semantic_schema_parity.py` on the actual Windows
checkouts to re-evaluate that assertion; it checks integrity, not the entire
API/TCK compatibility or the active Git HEAD.

## Owner and consumer gates

| Owner / consumer | Required behavior | Forbidden inference |
|---|---|---|
| Kristal Framework | Own v11 formats, identities and reference validation | Name or QID becomes a canonical KQ |
| Kristal Authoring Kit | Own canonical graph creation, catalog registration and versioned writes | diK selection is a write authorization |
| diK | Own lexical catalogs and derived multi-revision indexes; reviewed external crosswalk evidence | `accepted` in an ambiguous source revision is global approval |
| kristal-public | Host only expressly authorized immutable/public artifacts | Repository visibility establishes an active revision |
| EncyKlopedia | Produce private, sourced propositions and optional read-only links | A QID or EncyK suggestion creates an island/canonical assertion |
| Kristalizer | Propose local staging identity/Wikidata candidates | Candidate becomes exactMatch |
| Kristal Manager | Inventory instances; distinguish selection and deployment evidence | Highest version/date/size is the active v11 revision |
| KristalDiag | Validate exact pinned inputs and report uncertainty | Local diagnostics certify public publication |
| Integration Pack | Validate/render read-only v11 projections with pinned Framework | Projection is canonical or authorizes activation |
| Konstellation | Navigate authorized read views | Visual identity/label equality merges namespaces |
| SemantiK Architect | Plan using typed semantic references | Missing KQ is guessed from natural language |
| GF_Wordbench | Qualify GF grammar artifacts per language | Dictionary label proves a compiled realization |
| SemantiK Runtime Orchestrator | Enforce independent RuntimeSet gates and rollback | Source diK mapping permits auto-activation |
| Spek | Review editorial composition and publication gates | Candidate lexical or semantic source is publishable |
| kOA Digital Ecosystem | Coordinate owners, dependencies and evidence statuses | Central coordination confers any owner authority |

## Revision-selection safety decision

The historical diK derived selection file profile `/0.1` did not pin
`graph_sha256`. diK now introduces
`dik.canonical-selection-decisions/0.2`: **all five SHA-256 values** for
state index, registry, crosswalk, inspected graph and catalog are mandatory.
New builds reject `/0.1` decision files rather than silently re-signing a
review. Previously generated views remain historical records, not approvals.
`OPERATOR_PINNED_DERIVED_VIEW` and `SINGLE_DECLARED_DERIVED_VIEW` remain
**derived-only**; the Framework active/authoritative revision is still
unresolved wherever the source lacks an explicit authority marker.

Historical V5.11 evidence reported 126 Kristals, 77 with V11, 180 source
revisions, 72 multirevision Kristals without automatic selection and 49
without V11. Seven declared artifacts were absent in the Windows diagnostic,
and seven graphs were not fully inspected in the lightweight profile. These
are **dated observations**, not a fresh global certification.

## Language and delivery boundaries

- Target 13 languages: `en fr es de nl sv da nn fi et af it pt`.
- Historical `no` is preserved but removed from the *new target set*; no
  deletion or rewrite of old dictionaries is authorized by this record.
- The 14-component local-root manifest remains under
  `docs/inventory/semantic-stack-local-roots.v1.json` (plus C0 as coordinator).
- Read-only checks and derived rebuilds must use new output directories.
- Wikidata equivalence review, license clearance, exact source authority,
  independent validation, public release and activation are independent gates.
- The owner-specific notes `docs/DIK_FEDERATION_V02_BOUNDARY.md` live in
  each affected consumer repository. No code of those applications is
  automatically activated merely by the presence of these notes.

**Acceptance:** source SHA preflight before edits; explicit refusal tests for
missing graph hash, stale graph bytes, profile `/0.1`, missing schema and
schema drift; no write into `kristals/*/canon`, historical dictionaries,
Wikidata sources, Git remotes or release/activation directories.
