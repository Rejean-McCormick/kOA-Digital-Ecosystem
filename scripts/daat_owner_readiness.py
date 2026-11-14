#!/usr/bin/env python3
"""Read-only DaAT 0.4.3 cross-owner snapshot observer.

No owner CLI is executed, source bytes are never exported, and hashes are
local consistency evidence only. NEVER turns a DaAT prototype into an IK/Kit
profile, reviewer approval, a canonical Kristal or publication permission.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PureWindowsPath
import re
import sys

FORMAT = 'koa.daat-owner-readiness/0.1.0-local-observation'
ROOT = Path(__file__).resolve().parents[1]
REPO_NAMES = {
    'kit': ('Kristal-Authoring-Kit', 'Kristal-Authoring-Kit'),
    'ik': ('Interaction-Kernel', 'interaction_kernel'),
    'kristalizer': ('Kristalizer', 'Kristalizer'),
    'dik': ('diK', 'diK'),
    'mediatheque': ('Mediatheque', 'mediatheque'),
    'skope': ('Skope', 'Skope'),
    'konfid': ('Konfid', 'konfid'),
    'integration_pack': ('Kristal-Integration-Pack', 'Kristal-Integration-Pack'),
    'c0': ('kOA-Digital-Ecosystem', 'kOA_Digital_Ecosystem'),
    'framework': ('Kristal-Framework', 'Kristal-Framework'),
    'arketype': ('Arketype', 'arketype'),
    'daat': ('Daat', 'Daat'),
}
OWNER_ROLES = tuple(x for x in REPO_NAMES if x not in {'framework', 'arketype', 'daat'})
# These are known observation anchors, NOT a versioned wire contract or delegated authority.
REQUIRED = {
    'kit': ('VERSION', 'tools/kristal.py', 'contracts/v11-framework-pin.json', 'docs/27_DIK_INTEGRATION.md'),
    'ik': ('VERSION', 'docs/kristal-daat.md', 'docs/adrs/ADR-IK-07-daat-kristal-v7-boundary.md', 'contracts/schemas/envelope.schema.json', 'contracts/schemas/receipt.schema.json'),
    'kristalizer': ('VERSION', 'kristalizer/core.py', 'kristalizer/kit_reference.py', 'EXTERNAL_AUTHORING_KIT.md'),
    'dik': ('spec/diK-1.0/AGENTS.md', 'pyproject.toml', 'src/dik/_framework/schemas/v11/kristal-semantic-graph.schema.json', 'FRAMEWORK-PIN.md'),
    'mediatheque': ('README.md', 'pyproject.toml', 'contracts/kristal-ik-1.1/export-manifest.schema.json'),
    'skope': ('VERSION', 'AGENTS.md', 'tests/test_mediatheque_receipt_correlation.py', 'tests/test_portfolio_015.py'),
    'konfid': ('README.md', 'pyproject.toml', 'docs/BRANCH08_POLICY_BRIDGE.md', 'src/konfid/adapters/policy.py'),
    'integration_pack': ('VERSION', 'tools/v11_handoff.py', 'tools/v11_integration.py', 'contracts/v11-framework-pin.json'),
    'c0': ('AGENTS.md', 'docs/inventory/repositories.json', 'docs/2-Technical-Reference/40-integration/knowledge-projection-contract-set.json'),
}
MAX_FILE_BYTES = 6_000_000
SHA = re.compile(r'^[a-f0-9]{64}$')


class ObservationError(Exception):
    pass


def _pairs(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ObservationError('duplicate_json_key')
        out[k] = v
    return out


def read_json(path: Path):
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_FILE_BYTES:
        raise ObservationError('missing_linked_or_oversize_json')
    try:
        return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_pairs,
                          parse_constant=lambda value: (_ for _ in ()).throw(ObservationError('nonfinite_json')))
    except (ValueError, UnicodeError) as exc:
        raise ObservationError('malformed_json') from exc


def safe_file(root: Path, rel: str) -> Path:
    p = Path(rel)
    if (not rel or p.is_absolute() or '\\' in rel or
            any(seg in ('', '.', '..') for seg in rel.split('/'))):
        raise ObservationError('unsafe_relative_path')
    target = root
    for seg in rel.split('/'):
        target = target / seg
        if target.is_symlink():
            raise ObservationError('symlink_in_observed_path')
    if not target.is_file() or target.stat().st_size > MAX_FILE_BYTES:
        raise ObservationError('missing_or_oversize_marker')
    return target


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for part in iter(lambda: f.read(65536), b''):
            h.update(part)
    return h.hexdigest()


def _repo_paths(inventory: Path, workspace: Path | None, snapshot_root: Path | None):
    if bool(workspace) == bool(snapshot_root):
        raise ObservationError('select_one_of_workspace_or_snapshot_root')
    records = read_json(inventory)
    if not isinstance(records, list):
        raise ObservationError('invalid_c0_inventory')
    selected = {}
    for role, (repo_name, snapshot_name) in REPO_NAMES.items():
        found = [row for row in records if isinstance(row, dict) and
                 row.get('github_repo') == 'Rejean-McCormick/' + repo_name]
        if len(found) != 1:
            raise ObservationError('missing_or_duplicate_repo_in_inventory:' + role)
        if snapshot_root:
            path = snapshot_root / snapshot_name
            if role == 'daat' and not path.is_dir():
                path = snapshot_root / 'Daat'  # optional DaAT snapshot
        else:
            declared = found[0].get('local_root')
            parts = PureWindowsPath(declared).parts if isinstance(declared, str) else ()
            if len(parts) < 3 or parts[0].lower() != 'c:\\' or parts[1].lower() != 'mycode' or any(x in ('..', '.') for x in parts[2:]):
                raise ObservationError('invalid_inventory_local_root:' + role)
            path = workspace.joinpath(*parts[2:])
        if path.is_symlink():
            raise ObservationError('symlink_owner_root:' + role)
        selected[role] = path
    return selected


def _observe(role: str, root: Path):
    evidence = {'role': role, 'available': root.is_dir(), 'markers': [],
                'status': 'BLOCKED', 'owner_gate': 'not_qualified',
                'owner_approval': False, 'canonical_write_authorized': False,
                'published': False, 'activated': False}
    if not root.is_dir():
        evidence['issues'] = ['owner_snapshot_or_checkout_missing']
        return evidence
    issues = []
    try:
        descriptor = read_json(safe_file(root, 'integrations/daat/owner-observation.json'))
        if (descriptor.get('schema') != 'koa.daat-owner-observation/0.1.0-local' or
                descriptor.get('role') != role or descriptor.get('evidence_status') != 'OBSERVED_SNAPSHOT' or
                descriptor.get('read_only') is not True):
            issues.append('descriptor_invalid')
        for key in ('prototype_consumer_adopted', 'ik_ingress_approved', 'canonical_write_authorized', 'publication_authorized'):
            if descriptor.get(key) is not False:
                issues.append('unqualified_authority_claim:' + key)
        if set(descriptor.get('markers', ())) != set(REQUIRED[role]):
            issues.append('marker_inventory_drift')
    except (ObservationError, OSError, AttributeError, TypeError) as exc:
        issues.append('descriptor_missing_or_invalid:' + str(exc))
    for rel in REQUIRED[role]:
        try:
            path = safe_file(root, rel)
            evidence['markers'].append({'relative_path': rel, 'sha256': sha(path), 'status': 'OBSERVED_FILE'})
        except (ObservationError, OSError) as exc:
            issues.append(rel + ':' + str(exc))
    evidence['status'] = 'OBSERVED_SNAPSHOT' if not issues else 'INCOMPLETE'
    evidence['issues'] = issues
    # This is observational only, even for 100% matching local source bytes.
    return evidence


def _pin_parity(paths):
    result = {'status': 'INCOMPLETE', 'files_checked': 0, 'framework_version': 'unknown',
              'kit_version': 'unknown', 'issues': []}
    fw, kit, pack = paths['framework'], paths['kit'], paths['integration_pack']
    try:
        if not all(x.is_dir() for x in (fw, kit, pack)):
            raise ObservationError('framework_kit_or_integration_pack_absent')
        fwv = safe_file(fw, 'VERSION').read_text(encoding='utf-8').strip()
        kitv = safe_file(kit, 'VERSION').read_text(encoding='utf-8').strip()
        result['framework_version'], result['kit_version'] = fwv, kitv
        if fwv != '11.0.0-draft.4' or kitv != '4.0.0-draft.4':
            raise ObservationError('unsupported_framework_or_kit_version')
        kp = read_json(safe_file(kit, 'contracts/v11-framework-pin.json'))
        ip = read_json(safe_file(pack, 'contracts/v11-framework-pin.json'))
        if kp != ip:
            raise ObservationError('kit_integration_pack_pin_mismatch')
        if kp.get('version') != fwv or kp.get('profile') != 'kristal-integration-framework-pin/v11.0-draft.4':
            raise ObservationError('unexpected_framework_pin')
        files = kp.get('files')
        if not isinstance(files, dict) or len(files) != 13:
            raise ObservationError('expected_13_pinned_framework_files')
        for rel, expected in files.items():
            if not isinstance(rel, str) or not isinstance(expected, str) or not SHA.fullmatch(expected):
                raise ObservationError('invalid_pinned_digest')
            if sha(safe_file(fw, rel)) != expected:
                raise ObservationError('framework_pin_drift:' + rel)
            result['files_checked'] += 1
        result['status'] = 'LOCAL_HASH_PARITY_ONLY'
    except (ObservationError, OSError, UnicodeError, AttributeError, TypeError) as exc:
        result['issues'].append(str(exc))
    return result


def _dik_parity(paths):
    result = {'status': 'INCOMPLETE', 'schemas_checked': 0, 'issues': []}
    fw, dik = paths['framework'], paths['dik']
    try:
        if not fw.is_dir() or not dik.is_dir():
            raise ObservationError('framework_or_dik_absent')
        if '1.0.0a7' not in safe_file(dik, 'pyproject.toml').read_text(encoding='utf-8'):
            raise ObservationError('unexpected_dik_version')
        left = fw/'schemas/v11'
        right = dik/'src/dik/_framework/schemas/v11'
        lnames = {p.name for p in left.glob('*.schema.json') if p.is_file() and not p.is_symlink()}
        rnames = {p.name for p in right.glob('*.schema.json') if p.is_file() and not p.is_symlink()}
        if len(lnames) != 11 or lnames != rnames:
            raise ObservationError('v11_schema_inventory_mismatch')
        for name in sorted(lnames):
            if sha(safe_file(fw, 'schemas/v11/' + name)) != sha(safe_file(dik, 'src/dik/_framework/schemas/v11/' + name)):
                raise ObservationError('dik_schema_byte_drift:' + name)
            result['schemas_checked'] += 1
        result['status'] = 'LOCAL_SCHEMA_PARITY_ONLY'
    except (ObservationError, OSError, UnicodeError) as exc:
        result['issues'].append(str(exc))
    return result


def run(inventory: Path, *, workspace: Path | None = None, snapshot_root: Path | None = None):
    paths = _repo_paths(inventory, workspace, snapshot_root)
    owners = [_observe(role, paths[role]) for role in OWNER_ROLES]
    pack = _pin_parity(paths)
    dik = _dik_parity(paths)
    status = 'LOCAL_CHECKS_COMPLETED_OWNER_ADMISSIONS_BLOCKED'
    if any(o['status'] != 'OBSERVED_SNAPSHOT' for o in owners) or pack['issues'] or dik['issues']:
        status = 'LOCAL_EVIDENCE_INCOMPLETE_OWNER_ADMISSIONS_BLOCKED'
    return {
        'schema': FORMAT,
        'status': status,
        'observation_scope': 'offline_sources_and_local_hashes_only',
        'owner_admissions_qualified': 0,
        'owner_admissions_required': None,  # determined only by owner-ratified acceptance contracts
        'observed_repository_roles': len(OWNER_ROLES),
        'owners': owners,
        'cross_owner_checks': {'framework_kit_integration_pack': pack, 'framework_dik': dik},
        'denied_operations': ['ik_ingress', 'source_byte_move', 'canonical_build', 'publication', 'activation'],
        'owner_effects_executed': False,
        'network_used': False,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    scope = ap.add_mutually_exclusive_group(required=True)
    scope.add_argument('--workspace', type=Path, help='C:\\mycode on Windows; inventory determines exact repo paths')
    scope.add_argument('--snapshot-root', type=Path, help='Flat extracted SmartDump sources (offline testing)')
    ap.add_argument('--inventory', type=Path, default=ROOT/'docs/inventory/repositories.json')
    ap.add_argument('--out', type=Path, help='New JSON report path; do not overwrite')
    ns = ap.parse_args(argv)
    try:
        result = run(ns.inventory, workspace=ns.workspace, snapshot_root=ns.snapshot_root)
        payload = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
        if ns.out:
            dest = ns.out.resolve()
            if dest.exists() or any(dest.is_relative_to(p.resolve()) for p in _repo_paths(ns.inventory, ns.workspace, ns.snapshot_root).values() if p.is_dir()):
                raise ObservationError('output_exists_or_is_inside_owner_checkout')
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open('x', encoding='utf-8') as f:
                f.write(payload)
        else:
            print(payload, end='')
    except (ObservationError, OSError, AttributeError, TypeError) as exc:
        ap.exit(2, 'DaAT owner readiness REFUSED: ' + str(exc) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
