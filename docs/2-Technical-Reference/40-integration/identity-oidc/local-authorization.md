# Local Authorization

**Status:** Normative (kOA)

Federation answers **who is authenticating**. Each application answers **what that local account may do**.

## Orgo

Orgo remains authoritative for organization memberships, RBAC, workflow administration rights, task/case access, and tenant authorization.

## Konnaxion

Konnaxion remains authoritative for its participation, moderation, deliberation, distribution, and application-specific permissions.

## UCKK-Moodle

UCKK-Moodle remains authoritative for enrolments, course/context roles, capabilities, academic permissions, and institutional/Assembly permissions.

## No universal role table

The ecosystem MUST NOT assume equivalence such as:

```text
Moodle teacher == Orgo supervisor == Konnaxion moderator
```

Mappings MAY be configured locally, but remain application policy rather than identity truth.
