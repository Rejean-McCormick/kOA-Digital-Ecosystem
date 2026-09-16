# Build operations

Build operations use **Build Record v2** and Kristal v5 semantics.

## Knowledge build sequence

A Profile may use:

```text
native/source input
  -> Structured Epistemic State
  -> Working Exchange
  -> validation/review
  -> authority recognition
  -> Reference Exchange
  -> Runtime Pack
```

Claim-IR/Resolved Claim-IR may appear when an extractor/resolver Profile requires them.

## Gates

Do not use the historical universal rule “validation failure means compile must not run”. Instead record separate status and enforce the gate appropriate to the requested transition:

- compile eligibility;
- reference eligibility;
- publication eligibility;
- distribution eligibility;
- activation eligibility.

A production kOA policy can require validated/recognized Reference material before release or activation while still retaining a Working Exchange for diagnosis/review.

## Build evidence

Record exact dependency pins, input refs/digests, deterministic tool/profile versions, Working/Reference output refs, Validation Reports, Authority Recognition refs, Runtime Pack refs and reason codes.
