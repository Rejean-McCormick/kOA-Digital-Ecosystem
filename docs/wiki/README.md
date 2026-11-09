# GitHub Wiki publication of the final-system specification

**Status:** OFFLINE_INTEGRATION_PREPARED. The wiki snapshot is an independent Git repository in GitHub, not a directory automatically published from this coordination repository. The supplied files and successful local tests do **not** establish that the remote wiki, the 53 owner repositories, or production systems were updated.

## Normative documentation precedence

1. **Owner repositories** remain normative for product code, precise contracts, release policy and deployed behavior.
2. **`docs/target/`** in this central repository defines the intended federated final-system behavior. The 24 functional chains are `TARGET_DESIGN` specifications; they are not claims of qualification or deployment.
3. **`docs/status/current.md`**, source-specific receipts and owner test results describe observed implementation and qualification evidence.
4. **GitHub Wiki** is a rendered reading interface derived from the above, not a second normative spec.

## Source-to-wiki mapping

`python scripts/render_target_wiki.py` creates 47 flat pages from canonical repository Markdown:

- `docs/target/*.md` (8 pages) → `Final-*` pages, with `docs/target/README.md` → `Final-System.md`.
- `docs/target/functional-chains/README.md` → `Functional-Chains.md`.
- `docs/target/functional-chains/{00..11}*.md` (12 pages) → `Functional-*.md`.
- `docs/target/functional-chains/chains/FC-*.md` (24 pages) → `FC-*.md`.
- `docs/status/current.md` → `Implementation-Status.md`.
- `docs/inventory/README.md` → `Repository-Inventory.md`.

The export retains the Markdown content, rewrites local links to wiki page slugs, and replaces links to non-mirrored source files/JSON with repository code links. Each generated page includes the canonical source path and a SHA-256 of its source. The site navigation (`Home.md`, `_Sidebar.md`, `_Footer.md`) is maintained separately. Older wiki pages and older version-specific contract descriptions remain available but should not be presented as the final-system target.

## Repeatable offline update

From the root of this repository, with a separately extracted **wiki checkout** at `../kOA-Digital-Ecosystem.wiki`:

```bash
python scripts/render_target_wiki.py --validate
python scripts/render_target_wiki.py --write --output-dir ../kOA-Digital-Ecosystem.wiki --source-ref main
python scripts/render_target_wiki.py --check --output-dir ../kOA-Digital-Ecosystem.wiki --source-ref main
python scripts/validate_c0_coordination.py
python scripts/validate_target_architecture.py
python -m unittest discover -s tests -v
```

**Before publishing**, replace `main` with the verified default/source branch when different; the supplied ZIP archive does not establish the current remote branch. Review the generated diffs, exact contract ownership, security/privacy implications and release policy. Only commit/push the central repository and the wiki after that review. **Never run the exporter against a product owner's repository.**

The `--write` mode updates generated target pages only and does not remove, rename or alter historical/manual wiki pages. `--check` flags missing, stale and orphaned generated wiki pages, so a renamed generated page can be retired deliberately after a review. No remote Git command is performed by the script.

## Acceptance checklist

- Every target document and all 24 FC specifications has one mirrored wiki page.
- Every internal target-doc link resolves to a mirror page; non-mirrored resources link back to the source repository.
- `Home`, `_Sidebar`, `_Footer` start with the final-system architecture and preserve access to earlier scoped evidence.
- Skope/EncyK acquisition, Médiathèque custody and EncyKlopedia read-consumption are not conflated.
- Every target chain retains `TARGET_DESIGN` scope; snapshots alone are not represented as deployments.
- All central C0/target tests and mirror checks pass.
