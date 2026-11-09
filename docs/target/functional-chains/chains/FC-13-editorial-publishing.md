# FC-13 — Editorial composition, multilingual documents and public knowledge pages

**Classification:** `TARGET_DESIGN` — a destination specification, **not proof of integration or deployment**.

**Builds on:** [FC-12](FC-12-language-runtime.md), [FC-06](FC-06-knowledge-consumption.md), [FC-14](FC-14-identity-and-policy.md), [FC-22](FC-22-public-presence.md)  
**Inherits:** [system model](../00-system-model.md), [owner authority](../01-authority-and-ownership.md), [contract/receipts](../02-contract-and-receipts.md), [failure semantics](../03-state-trust-and-failure.md).

## Functional promise

**Initiator:** An editor assembles permitted typed content, validated references and accessible prose into a document or public-facing view.

**Expected final outcome:** An editorially approved versioned publication, visibly attributed and independent from the underlying Kristal semantic canon.

**Owner(s) of state and decisions:** Spek for independently approved editorial documents; SemantiK Architect for optional reviewed short realization; EncyKlopedia and site owners for their own presentation surfaces.

## Nominal end-to-end behavior

| # | Stage | Responsible party | Input → output | Acceptance/meaning |
|---|---|---|---|---|
| 1 | Select source | Editorial owner | licensed/releasable semantic or institutional input → editorial brief | Privacy, provenance and audience restrictions enforced |
| 2 | Produce wording | SemantiK Architect optional | approved typed units → reviewed locale realizations | Language output supports, but does not authorize, editorial publication |
| 3 | Compose | Spek | typed units, content components and layout → preview artifact | No hidden new factual assertions; accessibility and attribution |
| 4 | Review | Human editorial owner | draft + references → approved revision | Language, legal, privacy and institutional checks performed |
| 5 | Publish | Product-specific publisher | approved artifact → public/read-only editorial release | Target and cache invalidation explicit; not semantic release |
| 6 | Correct/withdraw | Editorial owner | superseding revision → new version and withdrawal metadata | Consumers can distinguish current text from canonical source version |

## Interfaces and authority gates

`B-LANG-02` is proposed; other editorial/website interfaces require specific owners to agree on export formats before an integrated push is defined.

## Failure, privacy and forbidden shortcuts

Publication is not semantic validation; no public transfer of student/clinical/private documents, no unreviewed machine-generated claims, no implied official institutional endorsement.

## Definition of done — acceptance and negative tests

Test legal/visibility review, source-citation fidelity, language fallback, accessible output, tampered source rejection, hidden/private content controls, correction/supersession and exact published artifact hash.

## Required code and contract alignment

Owner implementation: establish Spek input and output manifest with release permission metadata; test optional SA draft→editor approval rather than automatic website publication.

## Product-specific notes

An encyclopedia article and a Spek editorial document are different product outputs even when they reuse the same derived knowledge reference.

## Source anchors and verification boundary

Spek and SemantiK Architect owner READMEs; B-LANG-02; homepage/documentation and EncyKlopedia snapshots.

The cited owner files are from the **supplied November 2026 snapshots**; the fact that a file exists is not evidence that this full final journey is running. Exact source-member names, hashes and repository roles are recorded in [the portfolio registry](../../portfolio.v1.json), [the portfolio guide](../../PORTFOLIO.md) and [snapshot reconciliation](../../SNAPSHOT_RECONCILIATION.md). Contract identifiers absent from [BOUNDARIES](../../BOUNDARIES.md) remain subject to owner agreement.
