"""Ensure offline C0/EncyK source observations do not confer Git authority."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from render_repository_inventory import render


class RepositorySnapshotObservationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads((ROOT / 'docs/inventory/repositories.json').read_text(encoding='utf-8'))
        cls.ledger = json.loads((ROOT / 'docs/inventory/owner-source-observations-2026-11-24.v1.json').read_text(encoding='utf-8'))

    def test_canonical_identity_perimeter_is_unchanged(self):
        self.assertEqual(len(self.inventory), 55)
        self.assertEqual(len({r['github_repo'] for r in self.inventory}), 55)
        by_repo = {r['github_repo']: r for r in self.inventory}
        self.assertIn('Rejean-McCormick/EncyKlopedia', by_repo)
        self.assertEqual(by_repo['Rejean-McCormick/EncyKlopedia']['status'], 'local_git_marker_seen')
        self.assertEqual(by_repo['Rejean-McCormick/kOA-Digital-Ecosystem']['status'], 'local_git_marker_seen')

    def test_only_two_explicit_offline_observations(self):
        with_metadata = {r['github_repo'] for r in self.inventory if 'latest_snapshot_observation' in r}
        self.assertEqual(with_metadata, {'Rejean-McCormick/EncyKlopedia', 'Rejean-McCormick/kOA-Digital-Ecosystem'})
        self.assertEqual({r['repository'] for r in self.ledger['entries']}, with_metadata)
        self.assertEqual((self.ledger['repository_count_before'], self.ledger['repository_count_after']), (55, 55))
        for row in self.inventory:
            o = row.get('latest_snapshot_observation')
            if not o:
                continue
            self.assertEqual(o['status'], 'OBSERVED_SNAPSHOT')
            self.assertEqual(o['date'], '2026-11-24')
            self.assertTrue((ROOT / o['ledger']).is_file())

    def test_ledger_contains_digests_but_no_remote_claim(self):
        for entry in self.ledger['entries']:
            self.assertEqual(len(entry['zip_sha256']), 64)
            self.assertTrue(int(entry['zip_sha256'], 16) >= 0)
            self.assertGreater(entry['zip_member_count'], 0)
            self.assertEqual(entry['status'], 'OBSERVED_SNAPSHOT')
            self.assertIn('git_origin', entry['not_verified'])
            self.assertIn('exact_commit_sha', entry['not_verified'])
            self.assertIn('publication', entry['not_verified'])

    def test_readable_inventory_generated_deterministically(self):
        expected = (ROOT / 'docs/inventory/repositories.md').read_text(encoding='utf-8')
        self.assertEqual(expected, render(ROOT))
        self.assertIn('55.', expected)
        self.assertEqual(expected.count('· [offline record]'), 2)


if __name__ == '__main__':
    unittest.main()
