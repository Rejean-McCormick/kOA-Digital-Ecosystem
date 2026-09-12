# Standalone Operation & Identity Resilience

**Status:** Normative (kOA)

## 1) Availability principle

Federated identity MUST NOT turn the IdP into a mandatory runtime dependency for already-established local application behavior.

## 2) IdP outage

When the IdP is unavailable:

- existing sessions continue according to local session policy;
- new SSO logins may fail cleanly;
- permitted local login/recovery paths remain available;
- no synthetic or bypass identity is fabricated.

When one application is unavailable, the other applications remain independently operable within their own responsibilities.

## 3) Break-glass administration

Critical deployments MUST retain at least one documented local administrative recovery path independent of federated login.

Break-glass credentials MUST be unique, protected, tested periodically, and audited when used.

## 4) Federated-only tenant policy

A tenant MAY require SSO for ordinary users. This is tenant policy and does not remove the architectural requirement for controlled administrative recovery.

## 5) Resilience alignment

This profile extends kOA's Resilience / Autonomy principle: shared convenience must not erase local operational independence.
