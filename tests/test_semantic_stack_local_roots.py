"""The workstream path map is documentary and never revises the C0 perimeter."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from render_semantic_stack_local_roots import render, validate


class SemanticStackLocalRootTests(unittest.TestCase):
    def test_reported_roots_agree_with_existing_registered_repositories(self):
        rows = validate(ROOT)
        self.assertEqual(len(rows), 14)
        self.assertEqual(sum(r['github_repo'] is not None for r in rows), 13)
        by_name = {r['name']: r for r in rows}
        self.assertEqual(by_name['diK']['local_root'], r'C:\mycode\diK\diK')
        self.assertEqual(by_name['SemantiK-Architect']['local_root'],
                         r'C:\mycode\SemantiK_Architect\SemantiK_Architect')
        self.assertEqual(by_name['GF_Wordbench']['local_root'],
                         r'C:\mycode\Grammatical-Framework\GF_Wordbench')
        self.assertIsNone(by_name['GF_Wordbench']['github_repo'])

    def test_55_owner_identities_are_not_modified(self):
        inventory = json.loads((ROOT / 'docs/inventory/repositories.json').read_text(encoding='utf-8'))
        self.assertEqual(len(inventory), 55)
        self.assertNotIn('Rejean-McCormick/GF_Wordbench',
                         {r['github_repo'] for r in inventory})

    def test_generated_english_documentation_is_current(self):
        self.assertEqual((ROOT / 'docs/inventory/SEMANTIC_STACK_LOCAL_ROOTS.md').read_text(encoding='utf-8'), render(ROOT))
        self.assertTrue((ROOT / 'scripts/check_semantic_stack_local_roots.ps1').is_file())


if __name__ == '__main__':
    unittest.main()
