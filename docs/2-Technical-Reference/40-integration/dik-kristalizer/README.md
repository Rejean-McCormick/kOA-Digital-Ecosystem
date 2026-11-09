# diK and Kristalizer — C0 owner-boundary coordination (2026-11-06)

**State: `OBSERVED_SNAPSHOT` for two code trees; `PROPOSED` or `BLOCKED` for cross-repository integration.** This is an additive kOA Digital Ecosystem coordination note, not an owner contract, certification, canonical write, or release approval. All statements below come from the two corresponding inner SmartDump snapshots, not a live checkout, Git remote, or runtime test.

## Repositories and exact local roots

| Repository | Windows local root from SmartDump index | Source-observed version | Role |
|---|---|---|---|
| [diK](https://github.com/Rejean-McCormick/diK) | `C:\mycode\diK\diK` | `1.0.0-alpha.7` (`pyproject.toml`: `1.0.0a7`) | Lexical dictionaries, language coverage, Wikidata candidate observations, reversible read views; **not** semantic KQ/KP authority. |
| [Kristalizer](https://github.com/Rejean-McCormick/Kristalizer) | `C:\mycode\Kristal\Kristalizer` | `1.2.2` (`VERSION`) | Inspect Kristal workspace(s), propose KQ↔QID and KP↔PID mappings, record explicit decisions, stage and build through a separate Authoring Kit; **not** autonomous canon. |

**Exact evidence:** `SmartDump_20261106_131708.zip` contains `SmartDump_20261106_131708/diK_Index_Code_snapshot.txt` and `.../Kristalizer_Index_Code_snapshot.txt`, with the `source_root` fields; `diK_Code_snapshot.zip/README.md` and `pyproject.toml`; `Kristalizer_Code_snapshot.zip/README.md`, `VERSION`, `EXTERNAL_AUTHORING_KIT.md`. The source roots describe where SmartDump read files, not a live verification of `.git/config`, `origin`, current remote SHA, or checked-out working tree.

The added inventory status `source_root_observed_in_smartdump_remote_unverified` is intentionally weaker than `github_and_local_remote_verified`. Public repository identity was located separately; registering it does **not** authorize push or publication.

## Separate owner functions

1. **Source evidence:** Skope/EncyK and a dedicated Médiathèque instance own acquisition and preserved source copies. The Wikipedia English SQL index and XML dump can be consumed locally; no ingestion into the C0 documentation repository and no bulk dataset upload to GitHub.
2. **diK:** manages lexical forms and coverage separately from canonical semantic identities. Wikidata Q/P and Lexeme L identifiers remain external. `docs/docs/30_SEMANTIK_GF_HANDOFF_V09.md` documents a *candidate-only* lexical handoff and `semantik.knowledge.json` with no inferred GF constructor or certified RuntimeSet.
3. **Kristalizer:** prepares reviewable Wikidata crosswalk decisions. `README.md` says approvals require reviewer, reason, and valid KS evidence; it can stage Kit builds and local activation **only on copies**, but does not send anything to GitHub. Bulk Wikidata statements → domain KA/KS is explicitly future enrichment work.
4. **Framework/Authoring Kit:** own canonical KQ/KP/KA/KS format, semantic validation, identity decisions and builds; neither diK nor Kristalizer replaces these owners.
5. **SemantiK Architect / Spek:** consume explicitly prepared lexical and semantic read surfaces and realize/compose articles. Language coverage must be measured per actual RuntimeSet; 14 proposed languages do not certify 14 installed realization pipelines.
6. **Publication:** EncyKlopedia/kristal-public delivery is independently gated. A local build or activation, generated Wiki draft or source observation is not public publication authorization.

## Compatibility issue requiring resolution before integration

The supplied **diK `1.0.0-alpha.7` targets Kristal Framework `11.0.0-draft.3`**; supplied **Kristalizer `1.2.2` requires a separately installed Authoring Kit `4.0.0-draft.4` pinned to Framework `11.0.0-draft.4`**. These pins cannot be assumed interoperable. Qualification must use exact revisions, schemas, tests, and real producer/consumer receipts before treating this as integrated.

## Proposed UNESCO Educational Policy pilot (not a release approval)

```text
UNESCO 41 concepts + Wikidata compact SQLite + local Wikipedia EN evidence
             │                  (observed / candidate)
             ▼
   Skope / Kristalizer — source-aware candidate identity review
             │  (no automatic exactMatch, KA or KS approval)
             ▼
       Framework v11 / Authoring Kit — one branch Kristal graph
             │  (versioned canonical KQ/KP/KA/KS + evidence)
             ▼
       diK lexical catalogs / 14 target locale coverage audit
             │  (candidate language knowledge; no certified GF binding)
             ▼
          SemantiK → Spek — 41 derived article projections
             │  (up to 14 language variants, subject to qualification)
             ▼
         EncyKlopedia / kristal-public — public publication gates
```

The **one Kristal graph → multiple article projections** model avoids 14 translations of Wikipedia and avoids minting a Kristal per article. Wikipedia English files remain local source evidence and inspiration, not independent KQ/KP identity authority. AI-generated statements remain proposals until reviewed and traced; neither a model's training knowledge nor an external link alone is a verified source.

## C0 acceptance gates

- [ ] Verify local Git roots exist and each `origin` is exactly the intended GitHub repository; record actual commit SHA(s).
- [ ] Pin a mutually accepted Framework v11/Kit cross-version adapter, or align diK before testing Kristalizer→Kit→diK.
- [ ] Read real UNESCO Workbench/Kristalizer handoffs; review candidate KQ↔QID decisions with actual KS evidence; keep rejected/pending items distinct.
- [ ] Verify diK coverage and SemantiK/GF runtime realization for the selected locales. Distinguish `direct`, `fallback`, and `missing`.
- [ ] Establish exact article projection manifest and immutable source attributions; confirm Spek syntax/semantics and status.
- [ ] Obtain independent owner-approved release attestations and public-content rights checks before any GitHub write.

**Machine coordination record:** [coordination.json](coordination.json). **Original v6 contract remains frozen:** [knowledge-projection-contract-set.json](../knowledge-projection-contract-set.json). Existing C0 v10 coordination rows remain unchanged.
