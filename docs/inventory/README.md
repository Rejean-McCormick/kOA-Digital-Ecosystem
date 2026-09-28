# Inventory

This directory records **where repositories and their documentation roots are located**. It is a discovery/navigation surface, not an architecture-admission or maturity authority.

## Files

- [`repositories.json`](repositories.json) — complete supplied inventory: local roots, GitHub mappings, statuses, descriptions, documentation paths and notes.
- [`repositories.md`](repositories.md) — human-readable projection of the same inventory.

## Interpretation rule

```text
inventoried != integrated != admitted != qualified != released != deployed
```

Local paths such as `C:\mycode\...` are workstation-specific references. Cross-system authority, contracts and current maturity remain defined by the repository's Authority Map, Contract Map and Current Maturity Map.
