# kOA Digital Ecosystem — Agent / contributor guidance

This repository is **C0 architecture and coordination**, not a domain authority, GitHub publisher, nor a canonical Kristal source. The primary documentation objective is the **final-system target** under `docs/target/`; implementation maturity is a separate evidence view. Keep all changes in English unless a historical quoted artifact requires its original language.

- Establish the responsible **owner repository** and approved contract revision before updating cross-system maps.
- Distinguish `OBSERVED_SNAPSHOT`, `DOCUMENTED`, `USER_DECIDED`, `PROPOSED`, `BLOCKED`, and `UNKNOWN`. Do not claim current GitHub HEAD, public release, qualified proof, or production operation from a ZIP snapshot.
- Preserve the historical v6 knowledge-projection baseline in `docs/2-Technical-Reference/40-integration/knowledge-projection-contract-set.json`. Add separate v9/v10 coordination records instead of retroactively changing contract identities.
- Maintain separate boundaries for logical state, materialization, local build, independently qualified validation, read-surface sync, immutable publication, and activation.
- A push or PR to a **public** GitHub repository may disclose bytes. Obtain independently qualified exact-input evidence and explicit per-Kristal authorization before any such operation; a policy statement is not a release grant.
- Konstellation is the fleet and concept navigator, Manager owns instance inventory, Arketype owns design-only patterns, and Kompiler is read-only. Do not duplicate their implementations in C0.
- Every C0 work item has an owner, evidence status, dependencies, and acceptance gate. Never promote a proposed task to `qualified_integrated` without exact source revision and producer/consumer evidence.
- The 53-snapshot ledger establishes offline provenance, not code compliance; owner branch kits are work instructions with empty reports. Keep source observations independent of test results.
- Maintain `docs/target/functional-chains/` as the cumulative English functional specification: common authority/contract/failure model first, then distinct chain documents, cross-chain scenarios, complete current repository coverage and negative acceptance tests. A target design never counts as qualification; preserve owner exact-contract precedence.
- Generate GitHub Wiki final-system pages only from canonical central Markdown using `python scripts/render_target_wiki.py`; keep manual navigation and dated evidence separate. Do not claim the wiki remote is updated when only the ZIP is produced.
- Run `python scripts/render_target_wiki.py --validate`, `python scripts/render_repository_inventory.py --check`, `python scripts/validate_c0_coordination.py`, `python scripts/validate_target_architecture.py`, `python scripts/render_target_portfolio.py --check`, `python scripts/render_target_boundaries.py --check`, and `python -m unittest discover -s tests -v` after changes. No side effects outside this repository should result.

## Branch-10 public target projection

Maintain `docs/target/public-architecture.v1.json` with `python scripts/export_public_architecture.py`; run `--check` before handing updates to the docs portal, Homepage or Mosaic. No local roots, source snapshot paths, personal data or deployment claims belong in that public projection. The site build/publishing owners retain independent release authorization. See `docs/integration/BRANCH10_PUBLIC_ARCHITECTURE_2026-11-09.md`.
