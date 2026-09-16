# Pinned Kristal dependency

kOA pins the exact Kristal v5 release used by the current integration profile:

```text
version                  5.0.0-rc.1
tag                      v5.0.0-rc.1
commit                   af703bf02ee04a69a5f2ad6694fa8b8e56ae2b19
canonicalization_profile kristal.v5:jcs-rfc8785
canonicalization_version 1
schema_set_digest        sha256:7a94a1e8a91d5c5267b73b7f1e98977faa548324bc937bb491cd08d49fdc8c92
```

Integrations must not use floating references such as `main`, `latest` or `5.x` for conformance claims.

The pin is independent of kOA release numbering and should be recorded in Build/Release evidence whenever Kristal artifacts are produced or consumed.
