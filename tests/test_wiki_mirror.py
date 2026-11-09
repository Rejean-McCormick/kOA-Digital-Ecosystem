"""Wiki generation checks operate on local files only (never publish remotely)."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("render_target_wiki", ROOT / "scripts/render_target_wiki.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class WikiMirrorTests(unittest.TestCase):
    def setUp(self):
        self.mapping = MODULE.build_map(ROOT)
        self.pages = MODULE.render(ROOT)

    def test_all_canonical_target_markdown_is_mirrored(self):
        expected = list((ROOT / "docs/target").rglob("*.md"))
        for f in expected:
            self.assertIn(f.resolve(), self.mapping)
        self.assertEqual(len(self.pages), len(expected) + 2)

    def test_all_24_functional_chains_are_mirrored(self):
        self.assertEqual(len(list((ROOT / "docs/target/functional-chains/chains").glob("FC-*.md"))), 24)
        self.assertEqual(len([n for n in self.pages if n.startswith("FC-")]), 24)

    def test_generated_internal_links_resolve(self):
        self.assertEqual(MODULE.validate_pages(self.pages), [])
        self.assertIn("[FC-01](FC-01-research-and-acquisition)", self.pages["Functional-Chains.md"])

    def test_no_claim_of_live_deployment(self):
        for name, text in self.pages.items():
            with self.subTest(page=name):
                self.assertIn("Target requirements are not evidence of deployed behavior", text)
                self.assertTrue(text.startswith(MODULE.GENERATED_MARKER))

    def test_canonical_source_hash_is_reproducible(self):
        self.assertEqual(self.pages, MODULE.render(ROOT))
        self.assertIn("SHA-256:", self.pages["Final-System.md"])

    def test_nonmirrored_json_links_point_to_canonical_repo(self):
        page = self.pages["Final-Portfolio.md"]
        self.assertIn("https://github.com/", page)
        self.assertNotIn("](portfolio.v1.json)", page)

    def test_rewrite_ref_can_be_selected_without_mutating_sources(self):
        changed = MODULE.render(ROOT, ref="integration-branch")
        self.assertIn("blob/integration-branch/", changed["Final-System.md"])
        self.assertNotEqual(changed["Final-System.md"], self.pages["Final-System.md"])
        self.assertEqual(changed["FC-01-research-and-acquisition.md"].count("SHA-256:"), 1)


if __name__ == "__main__":
    unittest.main()
