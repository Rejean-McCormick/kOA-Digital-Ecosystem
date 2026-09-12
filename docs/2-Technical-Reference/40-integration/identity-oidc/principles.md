# Common Identity Principles

**Status:** Normative (kOA)

## 1) Hard invariants

```text
authentication != authorization
federated identity != local account
same person != same role
same email != same identity
SSO available != SSO required
IdP unavailable != application unavailable
```

## 2) Application ownership

Each application owns its local accounts, memberships, roles, permissions, sessions, and audit records.

No application may authorize ordinary local actions by calling another application at request time.

## 3) No shared credential store

Passwords MUST NOT be synchronized across Orgo, Konnaxion, and UCKK-Moodle. Application-local credentials remain application-owned. IdP credentials remain IdP-owned.

## 4) No shared user database

Cross-system identity linkage MUST use explicit identifiers and supported APIs/configuration. Direct cross-database access to user tables is prohibited.

## 5) Optional federation

OIDC is an additional authentication path. A deployment MAY require federation for ordinary users, but critical deployments MUST retain a documented administrative recovery path independent of the IdP.

## 6) Personas and actors

A domain actor or synthetic persona is not automatically an authenticatable account. Demo fixtures MUST default to `create_login = false` unless account creation is explicitly requested and authorized.
