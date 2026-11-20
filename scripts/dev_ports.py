#!/usr/bin/env python3
"""C0 local development port plan: validate, inspect, and preflight. Stdlib only.

This is a design registry, not an OS reservation, process manager, or release gate.
"""
from __future__ import annotations

import argparse
import json
import re
import socket
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = ROOT / 'config' / 'local-dev-ports.v1.json'
ID_RE = re.compile(r'^[a-z][a-z0-9-]*$')


class RegistryError(ValueError):
    pass


def load(path: Path = DEFAULT_REGISTRY) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def validate(data: dict) -> list[str]:
    """Validate internal coherence; does NOT claim ports free on a target machine."""
    errors: list[str] = []
    if data.get('schema_version') != 1:
        errors.append('schema_version must be 1')
    if data.get('decision_status') not in ('proposed', 'adopted'):
        errors.append('decision_status must be proposed or adopted')
    if data.get('host') != '127.0.0.1' or data.get('transport') != 'tcp':
        errors.append('v1 supports IPv4 loopback TCP only')
    if data.get('scope') != 'developer-loopback-only':
        errors.append('v1 is local-development-only')
    policy = data.get('policy', {})
    if (policy.get('fallback_to_next_free_port') is not False or
            policy.get('collision_action') != 'fail-with-diagnostics' or
            policy.get('production_ports_in_scope') is not False):
        errors.append('policy must forbid fallback and exclude production')
    pool = data.get('pool', {})
    start, end = pool.get('start'), pool.get('end')
    if not (isinstance(start, int) and not isinstance(start, bool) and
            isinstance(end, int) and not isinstance(end, bool) and
            1024 <= start <= end < 49152):
        errors.append('pool must be within 1024..49151')
        start, end = 1, 0
    seen_block_owners: set[str] = set()
    occupied_blocks: set[int] = set()
    blocks = data.get('blocks', [])
    if not isinstance(blocks, list) or not blocks:
        errors.append('blocks must be a nonempty list')
        blocks = []
    for block in blocks:
        owner, lo, hi = block.get('owner'), block.get('start'), block.get('end')
        if not (isinstance(owner, str) and ID_RE.fullmatch(owner)):
            errors.append(f'invalid block owner: {owner}')
            continue
        if owner in seen_block_owners:
            errors.append(f'duplicate block owner: {owner}')
        seen_block_owners.add(owner)
        if not (type(lo) is int and type(hi) is int and start <= lo <= hi <= end):
            errors.append(f'invalid range for block {owner}')
            continue
        for port in range(lo, hi + 1):
            if port in occupied_blocks:
                errors.append(f'overlapping block at port {port}')
            occupied_blocks.add(port)
    if occupied_blocks != set(range(start, end + 1)):
        errors.append('blocks must cover the pool exactly once')
    seen_ids: set[str] = set()
    seen_ports: dict[int, str] = {}
    services = data.get('services', [])
    if not isinstance(services, list) or not services:
        errors.append('services must be a nonempty list')
        services = []
    for service in services:
        sid, owner, port = service.get('id'), service.get('owner'), service.get('port')
        if not (isinstance(sid, str) and ID_RE.fullmatch(sid)):
            errors.append(f'invalid service id: {sid}')
            continue
        if sid in seen_ids:
            errors.append(f'duplicate service id: {sid}')
        seen_ids.add(sid)
        if service.get('adoption') not in ('proposed', 'adopted'):
            errors.append(f'invalid adoption status for {sid}')
        if not (type(port) is int and start <= port <= end):
            errors.append(f'out-of-pool port for {sid}: {port}')
        elif port in seen_ports:
            errors.append(f'duplicate port {port}: {sid} and {seen_ports[port]}')
        else:
            seen_ports[port] = sid
        if not any(b.get('owner') == owner and type(port) is int and
                   type(b.get('start')) is int and type(b.get('end')) is int and
                   b['start'] <= port <= b['end'] for b in blocks):
            errors.append(f'port {port} is outside {owner} block for {sid}')
        legacy = service.get('legacy_observed', [])
        if not isinstance(legacy, list) or any(type(p) is not int for p in legacy):
            errors.append(f'legacy_observed invalid for {sid}')
    for client in data.get('clients', []):
        if client.get('target_service') not in seen_ids:
            errors.append(f'unknown target for client {client.get("id")}')
    return errors


def service_by_id(data: dict, sid: str) -> dict:
    for entry in data['services']:
        if entry['id'] == sid:
            return entry
    raise RegistryError(f'Unknown service {sid!r}; run `list` to see available ids')


def preflight(host: str, port: int) -> str:
    """Try a temporary bind to detect a local collision. There is still a TOCTOU race."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind((host, port))
        except OSError as exc:
            return f'BLOCKED ({type(exc).__name__}: {exc})'
    return 'AVAILABLE (at check time only)'


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', type=Path, default=DEFAULT_REGISTRY)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('validate', help='Check registry coherence, no network access')
    sub.add_parser('list', help='Print proposed assignments')
    p_get = sub.add_parser('get', help='Print one service port or local URL')
    p_get.add_argument('service')
    p_get.add_argument('--format', choices=('port', 'url', 'json'), default='port')
    p_check = sub.add_parser('check', help='Local bind preflight (not a reservation)')
    p_check.add_argument('--service', help='Only check the given service')
    args = parser.parse_args(argv)
    try:
        data = load(args.registry)
        errors = validate(data)
        if errors:
            for item in errors:
                print(f'ERROR: {item}', file=sys.stderr)
            return 2
        if args.command == 'validate':
            print(f'PASS: {len(data["services"])} target services, {len(data["blocks"])} blocks; status={data["decision_status"]}')
            return 0
        if args.command == 'list':
            print('SERVICE                     TARGET  OWNER         ADOPTION   LEGACY OBSERVED')
            for s in data['services']:
                legacy = ','.join(str(p) for p in s['legacy_observed']) or '—'
                print(f'{s["id"]:27} {s["port"]:6}  {s["owner"]:12}  {s["adoption"]:9}  {legacy}')
            return 0
        if args.command == 'get':
            s = service_by_id(data, args.service)
            if args.format == 'port':
                print(s['port'])
            elif args.format == 'url':
                print(f'http://{data["host"]}:{s["port"]}')
            else:
                print(json.dumps(s, indent=2, ensure_ascii=False))
            return 0
        if args.command == 'check':
            services = [service_by_id(data, args.service)] if args.service else data['services']
            failures = 0
            for s in services:
                result = preflight(data['host'], s['port'])
                if not result.startswith('AVAILABLE'):
                    failures += 1
                print(f'{s["id"]}: {data["host"]}:{s["port"]} {result}')
            if failures:
                print('Do not switch to another port. Inspect the port owner / Windows exclusions.', file=sys.stderr)
            return 1 if failures else 0
    except (OSError, ValueError, KeyError, TypeError, RegistryError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
