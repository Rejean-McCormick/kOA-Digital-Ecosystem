#!/usr/bin/env python3
"""Validate C0 target design / portfolio coordination data (not product qualification)."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REL = Path('docs/target/portfolio.v1.json')
FAMILIES = {
    'agentic_runtime', 'civic', 'civic_operations', 'coordination', 'creative_tooling', 'diagnostics',
    'domain_application', 'education', 'interoperability', 'knowledge_authoring',
    'knowledge_consumption', 'knowledge_core', 'knowledge_delivery',
    'knowledge_design', 'knowledge_operations', 'knowledge_packaging',
    'knowledge_publication', 'language', 'lexical', 'operations', 'platform',
    'presentation', 'public_presence', 'publication', 'release_tooling',
    'research', 'security', 'source_custody',
}
# These are architectural invariants based on owner README snapshots,
# not a claim that any cross-owner integration is production-qualified.
INVARIANTS = {
    'Skope': ('research', 'EncyK'),
    'EncyKlopedia': ('knowledge_delivery', 'read-only'),
    'Mediatheque': ('source_custody', 'source'),
    'Kristal-Framework': ('knowledge_core', 'identity'),
    'Kristal-Authoring-Kit': ('knowledge_authoring', 'authoring'),
    'Kristal-Integration-Pack': ('interoperability', 'derived'),
    'Daat': ('interoperability', 'mapping'),
    'Orgo': ('operations', 'Tasks'),
    'Koali-Spaces': ('presentation', 'presentation'),
    'Karacter': ('creative_tooling', 'character'),
    'Kolor': ('creative_tooling', 'palette'),
}


def validate(root: Path = ROOT) -> list[str]:
    issues: list[str] = []
    try:
        inventory = json.loads((root / 'docs/inventory/repositories.json').read_text(encoding='utf-8'))
        target = json.loads((root / REL).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return [f'cannot read portfolio source: {exc}']
    if target.get('format') != 'koa.target-portfolio.v1':
        issues.append('unexpected portfolio format')
    if target.get('intent') != 'final_system_design_non_normative_coordination':
        issues.append('target registry must distinguish design from deployment')
    if target.get('inventory') != 'docs/inventory/repositories.json':
        issues.append('target registry points to wrong repository inventory')
    rows = target.get('repositories')
    if not isinstance(rows, list):
        return issues + ['repositories must be a list']
    canon = [r['github_repo'] for r in inventory]
    if len(canon) != len(set(canon)):
        issues.append('source repository inventory contains duplicates')
    ids: list[str] = []
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            issues.append(f'row {i}: must be an object')
            continue
        name = row.get('repository')
        if not isinstance(name, str) or '/' not in name:
            issues.append(f'row {i}: missing repository ID')
            continue
        ids.append(name)
        slug = name.rsplit('/', 1)[-1]
        if row.get('family') not in FAMILIES:
            issues.append(f'{slug}: unsupported family')
        role = row.get('target_role')
        if not isinstance(role, str) or len(role.strip()) < 20:
            issues.append(f'{slug}: missing target role')
        if row.get('target_state') != 'design_intent_not_a_deployment_claim':
            issues.append(f'{slug}: may not claim deployed status from target role')
        ev = row.get('evidence')
        source = row.get('source_member')
        digest = row.get('source_sha256')
        if ev == 'owner_snapshot':
            if not isinstance(source, str) or not (source.startswith('repos/') or source.startswith('znapshot_kOA_Digital_Ecosystem_11091005.zip::') or source.startswith('SmartDump_20261109_113255(2).zip::SmartDump_20261109_113255/')):
                issues.append(f'{slug}: invalid owner snapshot path')
            elif '..' in Path(source).parts or '\\' in source:
                issues.append(f'{slug}: unsafe source path')
            if not isinstance(digest, str) or not re.fullmatch(r'[a-f0-9]{64}', digest):
                issues.append(f'{slug}: absent/malformed source SHA-256')
        elif ev == 'source_absent':
            if source is not None or digest is not None:
                issues.append(f'{slug}: absent source cannot have evidence pointer or hash')
        else:
            issues.append(f'{slug}: unsupported evidence status {ev!r}')
    if len(ids) != len(set(ids)):
        issues.append('duplicate target repository IDs')
    if set(ids) != set(canon):
        issues.append(f'target portfolio must cover exactly the canonical inventory (missing={sorted(set(canon)-set(ids))}; extra={sorted(set(ids)-set(canon))})')
    indexed = {r.get('repository', ''): r for r in rows if isinstance(r, dict)}
    for slug, (family, keyword) in INVARIANTS.items():
        row = indexed.get(f'Rejean-McCormick/{slug}', {})
        if row.get('family') != family or keyword.lower() not in str(row.get('target_role', '')).lower():
            issues.append(f'{slug}: target owner responsibility inconsistent with owner snapshot')
    # Target relationship graph is independent from the published, dated
    # evidence graph. An edge in this design is NEVER proof of integration.
    try:
        boundaries = json.loads((root / 'docs/target/boundaries.v1.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        issues.append(f'invalid target boundaries: {exc}')
        boundaries = {}
    if boundaries.get('format') != 'koa.target-boundaries.v1' or boundaries.get('intent') != 'target_design_not_integrated_state':
        issues.append('target boundaries: format/intent does not enforce design-only status')
    boundary_rows = boundaries.get('links', [])
    if not isinstance(boundary_rows, list):
        issues.append('target boundaries: links must be an array')
        boundary_rows = []
    seen = set()
    for row in boundary_rows:
        bid = row.get('id') if isinstance(row, dict) else None
        if not isinstance(bid, str) or not re.fullmatch(r'B-[A-Z]+-\d\d', bid) or bid in seen:
            issues.append(f'target boundaries: invalid or duplicate ID {bid}')
        seen.add(bid)
        if not isinstance(row, dict):
            continue
        if row.get('producer') not in canon or row.get('consumer') not in canon:
            issues.append(f'{bid}: target boundary endpoints must exist in canonical inventory')
        if row.get('producer') == row.get('consumer'):
            issues.append(f'{bid}: cross-owner boundary cannot loop to itself')
        if row.get('journey') not in {'knowledge', 'civic', 'education', 'platform', 'security', 'language'}:
            issues.append(f'{bid}: unknown journey')
        if row.get('state') != 'target_design_not_qualified' or row.get('optional_in_global_architecture') is not True:
            issues.append(f'{bid}: target boundary cannot claim a qualified or mandatory global integration')
        for field in ('purpose', 'evidence_required'):
            if not isinstance(row.get(field), str) or len(row[field].strip()) < 20:
                issues.append(f'{bid}: missing {field}')
        interface = row.get('interface')
        if interface is not None and (not isinstance(interface, str) or not re.fullmatch(r'[a-z][a-z0-9_.-]+/[0-9]+\.[0-9]+\.[0-9]+', interface)):
            issues.append(f'{bid}: interface is not an exact versioned profile or null')
    if len(boundary_rows) < 20:
        issues.append('target boundaries: incomplete first coverage')
    # Code snapshots are archived observations, never remote HEAD or a test result.
    try:
        ledger = json.loads((root / 'docs/inventory/code-snapshots-53.v1.json').read_text(encoding='utf-8'))
        snapshots = ledger.get('repositories', [])
        if ledger.get('format') != 'koa.code-snapshot-ledger/1.0' or \
                ledger.get('claim_level') != 'structural_inventory_sha256_only_no_source_behavior_or_execution_qualification':
            issues.append('code snapshot ledger: scope/format must be structural-only')
        if not isinstance(snapshots, list):
            issues.append('code snapshot ledger: repositories must be a list')
            snapshots = []
        snap_ids = [r.get('repository') for r in snapshots if isinstance(r, dict)]
        if len(snap_ids) != 53 or len(snap_ids) != len(set(snap_ids)) or set(snap_ids) != set(canon):
            issues.append('code snapshot ledger: must cover exactly 53 canonical repositories without duplicates')
        for row in snapshots:
            if not isinstance(row, dict):
                issues.append('code snapshot ledger: row must be an object')
                continue
            rid = row.get('repository')
            if not isinstance(row.get('snapshot_member'), str) or not row['snapshot_member'].startswith('SmartDump_20261109_113255/') or '..' in row['snapshot_member']:
                issues.append(f'{rid}: invalid code snapshot member')
            if not isinstance(row.get('snapshot_sha256'), str) or not re.fullmatch(r'[a-f0-9]{64}', row['snapshot_sha256']):
                issues.append(f'{rid}: missing code snapshot SHA-256')
            if row.get('evidence_level') != 'OBSERVED_SNAPSHOT' or row.get('doc_code_conformity') != 'NOT_EVALUATED' or row.get('tests_executed') != 'NOT_RUN' or row.get('git_revision') is not None:
                issues.append(f'{rid}: snapshot cannot assert audited code, executed tests or Git revision')
            if not isinstance(row.get('file_count'), int) or row['file_count'] < 1:
                issues.append(f'{rid}: missing structural file count')
    except (OSError, ValueError) as exc:
        issues.append(f'code snapshot ledger unreadable: {exc}')

    for rel in (
        'docs/target/README.md', 'docs/target/architecture.md',
        'docs/target/journeys.md', 'docs/target/CODE_ALIGNMENT_INSTRUCTIONS.md',
        'docs/target/PORTFOLIO.md', 'docs/target/adjacent-projects.md',
        'docs/target/boundaries.v1.json', 'docs/target/BOUNDARIES.md',
        'docs/target/SNAPSHOT_RECONCILIATION.md', 'docs/inventory/code-snapshots-53.v1.json',
    ):
        if not (root / rel).is_file():
            issues.append(f'missing target navigation document {rel}')
    for rel, expected_link in (('README.md', 'docs/target/'), ('docs/index.md', 'target/')):
        p = root / rel
        if not p.is_file() or expected_link not in p.read_text(encoding='utf-8'):
            issues.append(f'{rel}: final-system entry point missing')
    return issues


if __name__ == '__main__':
    findings = validate()
    if findings:
        for item in findings:
            print('ERROR:', item)
        sys.exit(1)
    print('PASS: target portfolio integrity and final-system navigation (not cross-owner qualification)')
