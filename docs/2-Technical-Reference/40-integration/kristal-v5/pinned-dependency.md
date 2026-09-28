# Kristal dependency and contract baselines

kOA integrations must distinguish a **contract baseline** from an **immutable release pin**.

## Current knowledge-contract baseline

```text
version                  5.0.0-rc.3
status                   release-candidate
referent registry        kristal.referent-registry/1.0.0
knowledge-model bundle   sha256:07fe0527ab29a4b40870efdd0c9e0c67c91de919e5428047245b2a2c04f8ea98
canonicalization         kristal.v5:jcs-rfc8785 / 1
```

The supplied rc.3 release metadata declares tag `v5.0.0-rc.3` but does **not** yet resolve it to an immutable commit SHA (`commit: null`). The knowledge boundary may therefore freeze the contract set while still refusing a claim that rc.3 is a fully resolved published release.

## Existing immutable downstream locks

Some downstream integrations may still pin an older immutable Kristal release. Those locks remain valid for their own scope until the owning integration explicitly updates and requalifies them. The new knowledge-projection baseline must not silently rewrite unrelated locks.

## Rule

For any conformance or release claim:

1. identify the exact integration scope;
2. identify the exact Kristal contract/release used by that scope;
3. reject floating references such as `main`, `latest` or `5.x`;
4. require tag + immutable commit for claims that depend on a published immutable release;
5. record the contract-set/model digest where the boundary defines one.
