# Kristal and Da'at

Kristal is the ecosystem's **structured epistemic/reference system**. Da'at is the **Kristal integration boundary** used by the kOA ecosystem.

## Kristal v5 lifecycle

The active model is not a single “truth pipeline”. The principal lifecycle is:

```text
source / native input
        ↓
Structured Epistemic State
        ↓
Working Exchange
        ↓
validation / review / authority recognition
        ↓
Reference Exchange (when recognized for a declared scope)
        ↓
Runtime Pack (policy-dependent)
```

Claim-IR and Resolved Claim-IR remain supported extractor/resolution profiles, but they are not mandatory universal stages.

## Epistemic distinctions

Kristal v5 keeps these concepts separate:

- assertion status;
- certainty level;
- validation status;
- `validated_as` classification;
- authority channel and scope;
- recognition status;
- reader policy.

A signature proves integrity/authorship under its key context; it does not automatically mean that content is validated, certain or authority-recognized.

## Working vs Reference

A **Working Exchange** is deterministic and content-addressed but may contain unreviewed, disputed or rejected material with explicit labels.

A **Reference Exchange** is an Exchange recognized as a reference by declared authority channel(s) for a declared scope.

Validation is not a universal compile blocker. Production policies may require validation/recognition before reference publication, distribution or activation.

## Da'at responsibilities

Da'at:

- maps ecosystem/IK requests to Kristal-native contracts;
- preserves source ownership and provenance;
- preserves epistemic labels and authority scope;
- returns ArtifactRefs/status rather than transferring domain ownership;
- must not collapse Working and Reference status.

Da'at does not turn an Orgo or Konnaxion record into “truth” merely because it crosses the boundary.

## Pinned dependency

The current ecosystem baseline pins Kristal `5.0.0-rc.1`, tag `v5.0.0-rc.1`, commit `af703bf02ee04a69a5f2ad6694fa8b8e56ae2b19`, canonicalization profile `kristal.v5:jcs-rfc8785` version `1`.
