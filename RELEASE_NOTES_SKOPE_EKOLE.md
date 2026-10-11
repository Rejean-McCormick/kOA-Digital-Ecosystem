# Delivery note — Skope and Ékole ecosystem mapping

This archive is a **complete kOA Digital Ecosystem snapshot plus additive reconciliation**, not a publication to a remote GitHub repository.

## What changed

- Added Skope and Ékole to the overview, authority and component maps.
- Added a proposed integration boundary and local port matrix under `docs/2-Technical-Reference/40-integration/skope-ekole/`.
- Added product status to the current maturity map, with no fabricated E2E acceptance.
- Added machine-readable supplemental application inventory and English GitHub descriptions (each ≤350 characters).
- Added unit tests covering the inventory and port invariants.
- Preserved the original frozen Kristal v6 cross-system baseline and historical repository corpus.

## Delivery / Git usage

Inspect differences before merging into an existing checkout. Import using a feature branch or compare/overlay tools; **do not reset an existing working tree**. This archive does not change Ékole's runtime or its launchers. It documents Ékole's port sharing at `8766` between teacher and OpsConsole. Skope's new default is `8767`.

To test: `python -m unittest discover -s tests -v` from this repo root.

The new port map is for loopback developer sessions, not a production service registry. The two supplied owner snapshots were not checked against a live GitHub checkout; remote repository URLs are intentionally not asserted.
