# Yesod — compilation coordination role

Yesod is a conceptual kOA role for coordinating deterministic compilation work. Kristal remains the owner of Kristal compilation semantics and artifact schemas.

## Kristal v5 rule

Compilation and validation are separate. A policy may allow:

```text
Structured Epistemic State
→ compile
→ Working Exchange
```

before validation or authority recognition is complete.

Therefore Yesod/Orgo must not implement a universal “no compile on fail” assumption.

## Stage-specific gates

A deployment/profile may instead gate specific later transitions, for example:

- eligibility for Reference Exchange status;
- publication to a reference channel;
- distribution;
- production activation;
- Reader Policy visibility.

Build evidence must record the actual status of each transition separately.
