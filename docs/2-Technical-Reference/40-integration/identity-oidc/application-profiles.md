# Application Identity Profiles

**Status:** Normative boundary profile; implementation maturity differs by application.

## 1) Orgo

Orgo uses a local account and local authorization model. When OIDC is enabled, the target resolution is:

```text
issuer + subject
-> Orgo local user
-> organization memberships
-> Orgo roles/permissions
```

The current Orgo implementation already contains local auth, SSO/OIDC, and identity services; implementations SHOULD extend those primitives rather than create a parallel identity subsystem.

## 2) Konnaxion

Konnaxion MUST keep a local account and local authorization model. OIDC support and account-linking details are implementation-specific and MUST be verified in the active runtime before conformance is claimed.

The Orgo<->Konnaxion business bridge is not an identity provider and MUST remain separate from human authentication.

## 3) UCKK-Moodle

UCKK-Moodle MUST retain local users, enrolments, roles/capabilities, academic authority, and administrative recovery.

```text
issuer + subject
-> Moodle local user
-> enrolments / contexts
-> Moodle roles/capabilities
```

Identity federation does not transfer academic or Assembly authority to Orgo or Konnaxion.

## 4) Service integrations

UCKK->Orgo decision handoff, Orgo->Konnaxion publication, workers, and callbacks use dedicated machine credentials/scopes rather than human SSO sessions.
