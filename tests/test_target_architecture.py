"""Final-system target documentation is machine-reproducible, not deployed-state evidence."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_target_architecture import validate
from render_target_portfolio import render
from render_repository_inventory import render as render_repositories
from render_target_boundaries import render as render_boundaries


class TargetArchitectureTests(unittest.TestCase):
    def setUp(self):
        self.target = json.loads((ROOT / 'docs/target/portfolio.v1.json').read_text(encoding='utf-8'))

    def test_valid_target_portfolio(self):
        self.assertEqual(validate(ROOT), [])
        self.assertEqual(len(self.target['repositories']), 55)
        self.assertEqual(sum(r['evidence'] == 'owner_snapshot' for r in self.target['repositories']), 54)

    def test_exact_canonical_set(self):
        source = json.loads((ROOT / 'docs/inventory/repositories.json').read_text(encoding='utf-8'))
        self.assertEqual({r['repository'] for r in self.target['repositories']},
                         {r['github_repo'] for r in source})

    def test_generated_view_matches_json(self):
        self.assertEqual(render(ROOT), (ROOT / 'docs/target/PORTFOLIO.md').read_text(encoding='utf-8'))

    def test_generated_repository_inventory_matches_json(self):
        self.assertEqual(render_repositories(ROOT), (ROOT / 'docs/inventory/repositories.md').read_text(encoding='utf-8'))

    def test_target_boundaries_have_only_canonical_endpoints(self):
        edges = json.loads((ROOT / 'docs/target/boundaries.v1.json').read_text(encoding='utf-8'))
        self.assertEqual(len(edges['links']), 26)
        all_ids = {r['repository'] for r in self.target['repositories']}
        for edge in edges['links']:
            self.assertIn(edge['producer'], all_ids)
            self.assertIn(edge['consumer'], all_ids)
            self.assertEqual(edge['state'], 'target_design_not_qualified')
        self.assertEqual(render_boundaries(ROOT), (ROOT / 'docs/target/BOUNDARIES.md').read_text(encoding='utf-8'))

    def test_sources_absent_are_explicit(self):
        missing = {r['repository'].split('/')[-1] for r in self.target['repositories']
                   if r['evidence'] == 'source_absent'}
        self.assertEqual(missing, {'Ekole-Atelier-Images'})

    def test_code_snapshot_ledger_is_structural_and_complete(self):
        ledger = json.loads((ROOT / 'docs/inventory/code-snapshots-53.v1.json').read_text(encoding='utf-8'))
        rows = ledger['repositories']
        self.assertEqual(len(rows), 53)
        self.assertEqual({r['repository'] for r in rows},
                         {r['repository'] for r in self.target['repositories']
                          if r['repository'] not in {'Rejean-McCormick/Ekole-Quebec',
                                                     'Rejean-McCormick/Ekole-Atelier-Images'}})
        for r in rows:
            self.assertEqual(r['evidence_level'], 'OBSERVED_SNAPSHOT')
            self.assertEqual(r['doc_code_conformity'], 'NOT_EVALUATED')
            self.assertEqual(r['tests_executed'], 'NOT_RUN')
            self.assertIsNone(r['git_revision'])

    def test_new_studios_have_precise_separate_owners(self):
        byrepo = {r['repository'].split('/')[-1]: r for r in self.target['repositories']}
        self.assertEqual(byrepo['Kolor']['family'], 'creative_tooling')
        self.assertEqual(byrepo['Karacter']['family'], 'creative_tooling')
        self.assertIn('palette', byrepo['Kolor']['target_role'])
        self.assertIn('character', byrepo['Karacter']['target_role'])

    def test_malformed_snapshot_status_is_rejected(self):
        with tempfile.TemporaryDirectory() as dirname:
            copy = Path(dirname) / 'repo'
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('__pycache__', '.git'))
            file = copy / 'docs/inventory/code-snapshots-53.v1.json'
            ledger = json.loads(file.read_text(encoding='utf-8'))
            ledger['repositories'][0]['tests_executed'] = 'PASS'
            file.write_text(json.dumps(ledger), encoding='utf-8')
            self.assertTrue(any('snapshot cannot assert' in issue for issue in validate(copy)))

    def _check_modified_row(self, slug, field, value):
        with tempfile.TemporaryDirectory() as dirname:
            copy = Path(dirname) / 'repo'
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('__pycache__', '.git'))
            file = copy / 'docs/target/portfolio.v1.json'
            target = json.loads(file.read_text(encoding='utf-8'))
            row = next(x for x in target['repositories'] if x['repository'].endswith('/' + slug))
            row[field] = value
            file.write_text(json.dumps(target, ensure_ascii=False), encoding='utf-8')
            return validate(copy)

    def test_missing_digest_fails(self):
        self.assertTrue(any('source SHA-256' in issue for issue in
                            self._check_modified_row('Skope', 'source_sha256', None)))

    def test_enyclopedia_cannot_become_acquisition_owner(self):
        issues = self._check_modified_row('EncyKlopedia', 'target_role',
                                          'Owns primary source acquisition and canonical identity release.')
        self.assertTrue(any('EncyKlopedia' in issue for issue in issues))

    def test_target_cannot_be_promoted_to_deployed_by_metadata(self):
        issues = self._check_modified_row('Mediatheque', 'target_state', 'production_verified')
        self.assertTrue(any('may not claim deployed' in issue for issue in issues))


if __name__ == '__main__':
    unittest.main()
