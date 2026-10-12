# kOA Digital Ecosystem — Agent / contributor guidance

This repository is **C0 architecture and coordination**, not a domain authority, GitHub publisher, nor a canonical Kristal source. Keep all changes in English unless a historical quoted artifact requires its original language.

- Establish the responsible **owner repository** and approved contract revision before updating cross-system maps.
- Distinguish `OBSERVED_SNAPSHOT`, `DOCUMENTED`, `USER_DECIDED`, `PROPOSED`, `BLOCKED`, and `UNKNOWN`. Do not claim current GitHub HEAD, public release, qualified proof, or production operation from a ZIP snapshot.
- Preserve the historical v6 knowledge-projection baseline in `docs/2-Technical-Reference/40-integration/knowledge-projection-contract-set.json`. Add separate v9/v10 coordination records instead of retroactively changing contract identities.
- Maintain separate boundaries for logical state, materialization, local build, independently qualified validation, read-surface sync, immutable publication, and activation.
- A push or PR to a **public** GitHub repository may disclose bytes. Obtain independently qualified exact-input evidence and explicit per-Kristal authorization before any such operation; a policy statement is not a release grant.
- Konstellation is the fleet and concept navigator, Manager owns instance inventory, Arketype owns design-only patterns, and Kompiler is read-only. Do not duplicate their implementations in C0.
- Every C0 work item has an owner, evidence status, dependencies, and acceptance gate. Never promote a proposed task to `qualified_integrated` without exact source revision and producer/consumer evidence.
- Run `python scripts/validate_c0_coordination.py` and `python -m unittest discover -s tests -v` after changes. No side effects outside this repository should result.
