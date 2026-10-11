"""Cross-repository Skope and Ekole mapping does not exceed supported snapshot claims."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class SkopeEkoleInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT/'docs/inventory/apps-skope-ekole.json').read_text(encoding='utf-8'))
        cls.apps = {x['name']:x for x in cls.data['applications']}

    def test_descriptions_under_github_limit(self):
        for app in self.apps.values():
            desc=app['repo_description_en']
            self.assertLessEqual(len(desc),350)
            self.assertEqual(len(desc),app['description_length'])

    def test_port_plan_and_collision_visible(self):
        self.assertEqual(self.apps['Skope']['local_port'],8767)
        ports=self.apps['Ekole']['local_ports']
        self.assertEqual(ports['core_student'],8765)
        self.assertEqual(ports['teacher'],ports['opsconsole'])
        text=(ROOT/'docs/2-Technical-Reference/40-integration/skope-ekole/local-ports.md').read_text(encoding='utf-8')
        self.assertIn('collide',text)

    def test_explicit_unqualified_boundaries(self):
        text=(ROOT/'docs/2-Technical-Reference/40-integration/skope-ekole/index.md').read_text(encoding='utf-8')
        self.assertIn('not qualified',text)
        self.assertIn('proposed',text.lower())
        self.assertIn('202', (ROOT/'docs/1-Overview/Components-Skope-and-Ekole.md').read_text(encoding='utf8'))

if __name__=='__main__':unittest.main()
