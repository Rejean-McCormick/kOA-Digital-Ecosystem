# Kristal v10 alignment — C0 change report (2026-10-12)

**Change type:** English documentation and coordination metadata only. **Status:** repository snapshot updated locally; no authenticated remote GitHub commit, publication, canonical workspace mutation, migration, or activation.

## Modified scope

- `docs/2-Technical-Reference/10-system/{architecture,authority-map}.md` — preserve existing owner boundaries; add v10 hosting, local inventory, Konstellation navigation, Arketype design-only roles.
- `docs/2-Technical-Reference/40-integration/contract-map.md` — separate frozen historical v6 knowledge projection from v9 semantic commitments and GitHub v10 hosting contracts.
- `docs/2-Technical-Reference/40-integration/kristal-v10-alignment/` — new English C0 owner map, contract table, readiness ledger, decision register and 24 machine-readable owner work items.
- `docs/2-Technical-Reference/40-integration/orchestration-c0/` — add cross-links, gated work plan and D-005 navigation decision without changing the original ten owner-interface rows.
- `docs/status/current.md`, `docs/index.md`, `README.md` — clarify current v10 alignment versus historical v6 baseline.
- `scripts/validate_c0_coordination.py`, `tests/test_c0_coordination.py`, `.github/workflows/c0-coordination.yml` — validate the new workstream registry, no fabricated qualified claims, dependencies and existing historic contract invariants.

## Verification record

- Existing C0 and Skope/Ékole inventory tests: **6/6 passed before update**.
- Updated unit tests: **9/9 passed** in the local snapshot environment.
- `python scripts/validate_c0_coordination.py`: **PASS**.
- No source file removed and no modification to `knowledge-projection-contract-set.json`.
- All Markdown relative links checked: **no broken links**.
- GitHub remote HEAD / permissions **not verified**; the connected read failed. Thus this is **not a GitHub push** or evidence of deployed alignment.

## Pending decisions

F-01 approved Framework commit and contract SHA; M-01 complete Manager runtime; D-01 independent C1 proof, C2 grant/scope and C3 index; KNAV-01 Manager local registry, KNAV-02/03 Konstellation fleet UI; Arketype visibility; legacy Kollection crosswalk. Each requires an owner commit, proof, and explicit approval where publication or access is involved.
