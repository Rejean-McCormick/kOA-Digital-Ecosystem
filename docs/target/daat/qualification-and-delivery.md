# DaaT — Qualification, delivery and safe coding handoff

**Status:** `TARGET_DESIGN` / C0 coordination. C0 records required integration evidence, not code runtime or a release decision.

## Verification levels

1. **Specified:** documents/target and owners named; does not imply endpoint exists.
2. **Local fixture-tested:** DaaT offline tests with fake ports and pinned sample inputs.
3. **Owner contract-tested:** exact producer/consumer revisions and real owner TCK checks.
4. **Bilaterally integrated:** actual consented source/custody/IK/Kit operations observed, negative paths and terminal receipts checked.
5. **Operationally qualified:** host security, supply chain, privacy, license and recovery approved, then separately released.

Do not publish a single ambiguous green badge across these levels. Independent source revision, test environment and responsible owner are mandatory for any upgrade of maturity.

## Essential negative proofs

| Boundary | Mandatory negative proof |
|---|---|
| Source rights | Deny prohibited bulk copy/full text; no external fetch without permission |
| Host/actor | Deny unsigned/unverified actor, missing workload, cross-tenant rights and expired policy |
| Connector worker | Reject malicious archive/repository instructions, unsafe egress, excessive resource use, secret logging |
| Mapping | Reject required semantic loss, unsupported schema, bogus provenance, conflicting replay |
| Identity/knowledge | Reject external Q/P→KQ/P implicit equivalence, unchecked AI inference, false recognition |
| Custody/IK | Deny receipt without verified disclosure; no generic import stuffed into v6 build request |
| Owner effect | Reconcile uncertain post-write outcome; do not double-execute |
| Publication | Local build or signature cannot authorize public Git or runtime activation |

## Coding release sequence

**Stage A:** DaaT static catalogue/adapter contracts and deterministic extraction references (no new owner state).  
**Stage B:** local PDF and pinned Git proof-of-concepts with sandbox/fixtures.  
**Stage C:** actual owner-reviewed source references and adopted IK/Konfid source intake if/when approved.  
**Stage D:** reviewed semantic proposals to exact compatible Framework/Kit version, **not** automatic canonical promotion.  
**Stage E:** legal scholarly-metadata and private Acomba pilot; bulk/CDC only after operational stability.

The detailed pull-request sequence and blocker ledger live in **DaaT `docs/33-CODING-ROADMAP.md`**. C0 should not duplicate implementation backlog state or ship SDK code.

## C0 change-control checklist

- [ ] DaaT and C0 docs links and maturity tags verified against actual owner checkout.
- [ ] No historical v6 contract-set identity or C0 boundary numbering changed.
- [ ] No Framework/Kristal or IK schema/profile committed from central docs.
- [ ] C0 functional-chain index still has exactly **24** chains.
- [ ] No claim of public release, production deployment, legal clearance or adoption without an owner record.
- [ ] `render_target_wiki.py --validate` and C0 validation suite run in a **complete current checkout**; if not, state explicitly why.

**Related:** [target README](README.md), [C0 acceptance specification](../functional-chains/06-qualification-and-acceptance.md) and [source reconciliation](../SNAPSHOT_RECONCILIATION.md).
