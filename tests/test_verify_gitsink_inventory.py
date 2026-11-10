"""Local-only GitSink enrollment must reject false identities and stay opt-in."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import verify_gitsink_inventory as verifier


def run_git(root, *args):
    result = subprocess.run(['git', *args], cwd=root, text=True,
                            capture_output=True, check=True)
    return result.stdout.strip()


class LocalVerificationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.targets = {}
        self.rows = []
        for name in ('diK', 'Karacter', 'Kolor', 'Kristalizer'):
            repo = 'Rejean-McCormick/' + name
            folder = self.root / name
            folder.mkdir()
            run_git(folder, 'init', '-q')
            run_git(folder, 'remote', 'add', 'origin', 'https://github.com/' + repo + '.git')
            self.targets[repo] = str(folder)
            self.rows.append({'github_repo': repo, 'github_url': 'https://github.com/' + repo,
                              'local_root': str(folder), 'scope': 'PUBLIC',
                              'status': verifier.SNAPSHOT_ONLY})
        for i in range(49):
            name = 'Rejean-McCormick/other-' + str(i)
            self.rows.append({'github_repo': name, 'github_url': 'https://github.com/' + name,
                              'local_root': str(self.root / ('other-' + str(i))),
                              'scope': 'PUBLIC', 'status': 'local_git_marker_seen'})

    def plan(self):
        return verifier.promotion_plan(self.rows, targets=self.targets)

    def test_four_valid_checkouts_are_promotable_and_other_rows_unchanged(self):
        results, promoted = self.plan()
        self.assertEqual(len(results), 4)
        self.assertTrue(all(s.startswith('VERIFIED') for s in results.values()))
        self.assertEqual([x['status'] for x in promoted[:4]], [verifier.LOCAL_VERIFIED] * 4)
        self.assertEqual(promoted[4:], self.rows[4:])
        self.assertEqual([x['status'] for x in self.rows[:4]], [verifier.SNAPSHOT_ONLY] * 4)

    def test_refuses_different_origin(self):
        folder = self.root / 'Kolor'
        run_git(folder, 'remote', 'set-url', 'origin', 'https://github.com/someone/other.git')
        results, _ = self.plan()
        self.assertTrue(results['Rejean-McCormick/Kolor'].startswith('BLOCKED'))

    def test_refuses_different_pushurl_even_with_matching_origin(self):
        folder = self.root / 'diK'
        run_git(folder, 'remote', 'set-url', '--push', 'origin', 'https://github.com/elsewhere/diK.git')
        results, _ = self.plan()
        self.assertTrue(results['Rejean-McCormick/diK'].startswith('BLOCKED'))

    def test_refuses_origin_rewrite(self):
        folder = self.root / 'Karacter'
        run_git(folder, 'config', '--local', 'url.https://github.com/someone/.insteadOf', 'https://github.com/Rejean-McCormick/')
        results, _ = self.plan()
        self.assertTrue(results['Rejean-McCormick/Karacter'].startswith('BLOCKED'))

    def test_refuses_missing_git_marker(self):
        folder = self.root / 'Kristalizer'
        (folder / '.git').rename(folder / '.git-deactivated')
        results, _ = self.plan()
        self.assertIn('no .git marker', results['Rejean-McCormick/Kristalizer'])

    def test_refuses_inventory_root_mismatch(self):
        self.rows[0]['local_root'] = str(self.root / 'other-folder')
        results, _ = self.plan()
        self.assertIn('scope/root', results['Rejean-McCormick/diK'])

    def test_rejects_duplicate_repo_or_incomplete_inventory(self):
        with self.assertRaises(ValueError):
            verifier.promotion_plan(self.rows[:-1], targets=self.targets)
        rows = [dict(x) for x in self.rows]
        rows[-1]['github_repo'] = rows[0]['github_repo']
        with self.assertRaises(ValueError):
            verifier.promotion_plan(rows, targets=self.targets)

    def test_malformed_github_origins(self):
        for bad in ('https://github.com/owner/repo/tree/main',
                    'https://token@github.com/owner/repo',
                    'https://github.com.evil.test/owner/repo',
                    'git@github.com:owner/repo/another', 'file:///owner/repo',
                    'https://github.com:invalid/owner/repo'):
            self.assertEqual(verifier.github_identity(bad), '', bad)
        self.assertEqual(verifier.github_identity('git@github.com:Owner/Repo.git'), 'Owner/Repo')

    def test_main_dry_run_and_apply_are_separate(self):
        inventory = self.root / 'docs' / 'inventory' / 'repositories.json'
        inventory.parent.mkdir(parents=True)
        inventory.write_text(json.dumps(self.rows, indent=2) + '\n', encoding='utf-8')
        with patch.object(verifier, 'INVENTORY', inventory), patch.object(verifier, 'ROOT', self.root), \
             patch.object(verifier, 'TARGETS', self.targets):
            self.assertEqual(verifier.main([]), 0)
            self.assertEqual(json.loads(inventory.read_text()), self.rows)
            self.assertEqual(verifier.main(['--apply']), 0)
            revised = json.loads(inventory.read_text())
            self.assertTrue(all(x['status'] == verifier.LOCAL_VERIFIED for x in revised[:4]))
            self.assertIn('Kristalizer', (inventory.parent / 'repositories.md').read_text(encoding='utf-8'))
            self.assertEqual(verifier.main(['--apply']), 0)

    def test_apply_is_all_or_nothing(self):
        inventory = self.root / 'docs' / 'inventory' / 'repositories.json'
        inventory.parent.mkdir(parents=True)
        inventory.write_text(json.dumps(self.rows, indent=2) + '\n', encoding='utf-8')
        run_git(self.root / 'diK', 'remote', 'set-url', 'origin', 'https://github.com/wrong/repo.git')
        with patch.object(verifier, 'INVENTORY', inventory), patch.object(verifier, 'ROOT', self.root), \
             patch.object(verifier, 'TARGETS', self.targets):
            self.assertEqual(verifier.main(['--apply']), 1)
        self.assertEqual(json.loads(inventory.read_text()), self.rows)


if __name__ == '__main__':
    unittest.main()
