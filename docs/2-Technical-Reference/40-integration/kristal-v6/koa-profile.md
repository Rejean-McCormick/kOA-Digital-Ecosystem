# kOA profile for Kristal v6

The kOA profile keeps Kristal's representation semantics separate from ecosystem execution policy.

## Automation rule

A represented action with `actionability.mode = automatic` may be routed automatically only when all of the following hold:

- required inputs are complete;
- the relevant owner contract/profile exists;
- the caller possesses required authority;
- the receiving owner admits the request;
- no declared human review/decision requirement applies;
- no local safety/governance policy blocks it.

The receiving owner remains the only writer of its operational state. Human review and decisions should be returned as traceable decision/observed records when they materially affect future reasoning.
