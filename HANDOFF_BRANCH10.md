# HANDOFF — Branch 10: central architecture owner

**Status:** LOCAL_IMPLEMENTATION_VALIDATED; no remote deployment. The central repository is the canonical source of the *target design*, not a product execution authority. The given owner ZIP omitted `docs/target/`; the restored tree is a documented reconstruction, not a byte-identical recovered v4 historical copy.

## Produces

- `docs/target/public-architecture.v1.json` (`koa.public-architecture.v1`) with **24 target chains, 53 owner roles and 26 proposed boundaries**.
- `docs/target/functional-chains/` and final-system navigation, qualification and code alignment.
- `scripts/export_public_architecture.py` to regenerate deterministic public-safe metadata; tests and CI gate.

## Consumers / agreements

- `initkoa-docs` receives an offline source-attributed Markdown mirror of C0 `docs/target/`.
- `HomePage-initkoa.org` receives the static JSON public projection.
- `Koali-Scenario-Mosaic` receives the same projection for an EN/FR explanatory page.

The schema is **a presentation export**, not an adopted inter-product runtime IK profile. No Konnaxion, Orgo, Kristal or Moodle state is written. Public release remains a separate human/site-owner decision.

## Evidence and open gates

C0 52 unit tests pass; target renderer and validators pass. Exact source Git revision, live site builds and deployments are not established. Restore the original v3/v4 `docs/target/` source if available and perform an owner-reviewed semantic diff against this reconstruction before treating it as the canonical final authored text. Confirm source ref/branch and site permissions prior to publication.

See `docs/integration/BRANCH10_PUBLIC_ARCHITECTURE_2026-11-09.md` for all details.
