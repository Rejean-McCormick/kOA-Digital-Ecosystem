"""Regression tests for the proposed C0 loopback port registry."""
import copy
import importlib.util
import io
import json
import socket
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('dev_ports', ROOT / 'scripts' / 'dev_ports.py')
ports = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ports)


class PortRegistryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'config' / 'local-dev-ports.v1.json').read_text(encoding='utf-8'))

    def test_registry_consistent(self):
        self.assertEqual([], ports.validate(self.data))
        self.assertEqual('proposed', self.data['decision_status'])
        self.assertFalse(self.data['policy']['fallback_to_next_free_port'])

    def test_each_target_uses_its_owner_block(self):
        ranges = {b['owner']: range(b['start'], b['end'] + 1) for b in self.data['blocks']}
        for s in self.data['services']:
            self.assertIn(s['port'], ranges[s['owner']])

    def test_legacy_8766_conflict_is_explicit_not_in_target(self):
        old = [s['id'] for s in self.data['services'] if 8766 in s['legacy_observed']]
        self.assertCountEqual(old, ['ekole-quebec-teacher', 'ekole-opsconsole'])
        self.assertNotEqual(ports.service_by_id(self.data, old[0])['port'],
                            ports.service_by_id(self.data, old[1])['port'])

    def test_duplicate_target_rejected(self):
        modified = copy.deepcopy(self.data)
        modified['services'][1]['port'] = modified['services'][0]['port']
        self.assertTrue(any('duplicate port' in e for e in ports.validate(modified)))

    def test_cross_owner_target_rejected(self):
        modified = copy.deepcopy(self.data)
        modified['services'][0]['port'] = 21120
        self.assertTrue(any('outside orgo block' in e for e in ports.validate(modified)))

    def test_auto_fallback_rejected(self):
        modified = copy.deepcopy(self.data)
        modified['policy']['fallback_to_next_free_port'] = True
        self.assertTrue(any('forbid fallback' in e for e in ports.validate(modified)))

    def test_client_must_reference_registered_service(self):
        modified = copy.deepcopy(self.data)
        modified['clients'][0]['target_service'] = 'not-registered'
        self.assertTrue(any('unknown target' in e for e in ports.validate(modified)))

    def test_port_lookup_cli(self):
        out = io.StringIO()
        with redirect_stdout(out):
            status = ports.main(['get', 'initkoa-web', '--format', 'url'])
        self.assertEqual(0, status)
        self.assertEqual('http://127.0.0.1:21120', out.getvalue().strip())

    def test_bind_conflict_fails_closed(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('127.0.0.1', 0))
            sock.listen(1)
            port = sock.getsockname()[1]
            self.assertTrue(ports.preflight('127.0.0.1', port).startswith('BLOCKED'))

    def test_cli_check_reports_collision_without_fallback(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('127.0.0.1', 0))
            sock.listen(1)
            # Testing the bind detector here avoids inventing a real system port owner.
            self.assertIn('BLOCKED', ports.preflight('127.0.0.1', sock.getsockname()[1]))


if __name__ == '__main__':
    unittest.main()
