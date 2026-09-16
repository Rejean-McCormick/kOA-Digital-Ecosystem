# Release Record v2 — deprecated compatibility projection

**Status:** Deprecated for authoritative release state.

The current kOA-Linux platform contract already defines **Release Set** as the artifact that binds compatible versions across independent release channels.

Digital Ecosystem must therefore not create a competing release authority.

If a legacy Release Record is retained for analytics, audit or migration, it MUST:

- identify itself as a non-authoritative projection;
- reference the authoritative `release_set_id`;
- reference owner-component activation/publication receipts;
- avoid inventing a second activation state;
- preserve the independent status of Kristal compile/validation/recognition and platform activation.

The former `schemas/release-record.schema.json` remains compatibility-only and should not be used for new authoritative writes.
