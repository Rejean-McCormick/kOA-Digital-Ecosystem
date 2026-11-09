# Adjacent project survey — not automatically admitted to the canonical portfolio

**Status:** inventory triage for final-system design. The 53 repositories in [the primary portfolio](PORTFOLIO.md) are an **existing declared register**, not a claim that the intended final system excludes every other related project. The bulk source archive also contains the following **22 still-adjacent project folders**. Their inclusion, product ownership and contract adoption have **not** been decided by merely discovering their documentation.

| Project archive folder | Potential relevance to the final system | Next check |
|---|---|---|
| `ars-magna-defluens` | Independent knowledge/communication design documentation | Determine whether it is a product dependency, a separate publication, or research material |
| `BoKristal` | Book/multifaceted Kristal reference material | Clarify whether an example/reference owner or a runtime integration |
| `Civilisational_Coherence` | Conceptual research | Treat as a domain/reference project unless an owner contract is supplied |
| `Freeze-Vote-Rebuild_Operational-Peace-Framework` | Domain framework | No automatic inclusion in civic-operational infrastructure |
| `gf-core` | Grammatical Framework core/runtime reference | Determine actual runtime dependency and license/version pin with SemantiK owners |
| `GF_Observatory` | GF diagnostics and observation | Review exact relationship to SemantiK Runtime Orchestrator and GF release evidence |
| `GF_RGL_AI_Compendium` | GF Resource Grammar Library reference | Check whether data/spec or an executable dependency |
| `gf-wikidata` | GF/Wikidata integration reference | Verify project provenance before introducing any pipeline edge |
| `gf-wikidata-tools` | GF/Wikidata tooling reference | Determine whether active source or stub |
| `GF_Wordbench` | Grammar workbench and candidate SemantiK handoff | **Priority:** review RuntimeSet production boundary and contract adoption |
| `GFF_to_Wikidata_importer` | External import tool | Check whether independently adopted, and ensure Q/P never become KQ/KP canon |
| `Grammatical_Framework-Albanian` | Albanian grammar/RGL project | Review as independent language-resource producer, not semantic owner |
| `Kalendar` | Calendar-related repository | Determine whether any signed product contract exists |
| `Kamel` | Independent project | Establish concrete system role from owner documentation before mapping |
| `Kin-City` | KOALI/KIN CITY application concept | Confirm relationship to platform, navigation and app autonomy |
| `kOA-D-E-GitHub-Audit` | Independent C0 documentation consumer, qualification/publishing tool | **Priority:** define dated-source compatibility, no live-repo misrepresentation |
| `kristal-farms` | Kristal lifecycle/fleet documentation | Compare target authority boundaries with Kit/Manager/Konstellation |
| `Kristal-Kollection` | Earlier registry/reference | Establish whether any actively consumed index or merely reference data |
| `LevelUpDiag` | Diagnostic tooling | Decide which product/qualification scope it actually owns |
| `math` | Mathematics reference project | Determine interface to MathKristal / SemantiK before classifying it |
| `mediatheque-references` | Médiathèque reference/template documentation | Check whether independent active instances or documentation reference |
| `uckk-moodle` | UCKK Moodle integration/application | **Priority:** establish Moodle owner bridge and release/rollback permissions |

**Source:** `repos(1).zip`, each `repos/<folder>/README.md` when present, plus relevant `docs/`/wiki documents. Karacter and Kolor are now explicitly part of the 53-repository portfolio based on separately verified SmartDump snapshots. These 22 remaining observations are deliberately **not** merged into `docs/inventory/repositories.json`. Before any admission: verify repository identity, role in the final system, primary owner, actual code, contracts, licensing, security, and independent qualification. The observed three snapshot-alias folders (Kompose, Kontexte and Médiathèque variants) are a **separate deduplication issue**, not 3 more products.

The intended final reference architecture should eventually include both **canonical owned products** and **declared external/neighboring dependencies** with typed relationships, rather than forcing everything into one flat list of Git repositories.
