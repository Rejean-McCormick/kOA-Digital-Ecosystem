"""Check the documentary companion reference without network or publication."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit"
PUBLIC = "https://rejean-mccormick.github.io/kOA-Digital-Ecosystem-GitHub-Audit/"

class GitHubAuditReferenceTests(unittest.TestCase):
    def test_companion_is_separate_from_canonical_inventory(self):
        registry = json.loads((ROOT / "docs/inventory/companion-tools.v1.json").read_text(encoding="utf-8"))
        inventory = json.loads((ROOT / "docs/inventory/repositories.json").read_text(encoding="utf-8"))
        matches = [x for x in registry["repositories"] if x["github_repo"] == REPO]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["public_dashboard_url"], PUBLIC)
        self.assertEqual(len(inventory), 55)
        self.assertNotIn(REPO, [x["github_repo"] for x in inventory])
        self.assertEqual(matches[0]["weekly_observation"]["security_coverage"], "UNKNOWN")

    def test_public_dashboard_is_discoverable(self):
        for path in ("README.md", "docs/index.md", "docs/inventory/README.md",
                     "docs/inventory/ECOSYSTEM_TOOLING.md", "docs/inventory/GITHUB_AUDIT.md",
                     "docs/status/current.md", "docs/inventory/repositories.md"):
            with self.subTest(path=path):
                self.assertIn(PUBLIC, (ROOT / path).read_text(encoding="utf-8"))

    def test_dated_evidence_and_boundaries(self):
        text = (ROOT / "docs/inventory/GITHUB_AUDIT.md").read_text(encoding="utf-8")
        for marker in ("LOCAL_OBSERVE", "OBSERVE", "27 8 * * 1", "46097058483",
                       "46146239397", "unknown for all 55", "--confirm-publish",
                       "not a verified zero-alert count"):
            self.assertIn(marker, text)

if __name__ == "__main__":
    unittest.main()
