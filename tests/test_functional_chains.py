"""Validate final-system functional-chain documentation coverage, not product execution."""
from pathlib import Path
import json
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
F = ROOT / 'docs/target/functional-chains'
T = ROOT / 'docs/target'


class FunctionalChainsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chain_files = sorted((F / 'chains').glob('FC-[0-9][0-9]-*.md'))
        cls.portfolio = json.loads((T / 'portfolio.v1.json').read_text(encoding='utf-8'))

    def test_exact_chain_index(self):
        self.assertEqual(len(self.chain_files), 24)
        ids = [re.search(r'(FC-\d\d)', x.name).group(1) for x in self.chain_files]
        self.assertEqual(ids, [f'FC-{i:02d}' for i in range(1, 25)])
        index = (F / 'README.md').read_text(encoding='utf-8')
        for file in self.chain_files:
            self.assertIn(f'chains/{file.name}', index)

    def test_common_documents_are_present(self):
        for name in ('README.md', '00-system-model.md', '01-authority-and-ownership.md',
                     '02-contract-and-receipts.md', '03-state-trust-and-failure.md',
                     '04-cross-chain-compositions.md', '05-repository-coverage.md',
                     '06-qualification-and-acceptance.md', '07-code-alignment-backlog.md',
                     '08-glossary.md', '09-reference-deployment-profiles.md',
                     '10-quality-attributes.md', '11-boundary-traceability.md'):
            self.assertTrue((F / name).is_file(), name)

    def test_owners_and_acceptance_are_specified(self):
        for p in self.chain_files:
            text = p.read_text(encoding='utf-8')
            with self.subTest(p=p.name):
                self.assertIn('`TARGET_DESIGN`', text)
                for section in ('## Functional promise', '## Nominal end-to-end behavior',
                                '## Interfaces and authority gates',
                                '## Failure, privacy and forbidden shortcuts',
                                '## Definition of done', '## Required code and contract alignment',
                                '## Source anchors and verification boundary'):
                    self.assertIn(section, text)
                self.assertIn('not proof of integration or deployment', text.lower())

    def test_53_repo_coverage_matches_registry(self):
        content = (F / '05-repository-coverage.md').read_text(encoding='utf-8')
        names = [r['repository'].rsplit('/', 1)[-1] for r in self.portfolio['repositories']]
        self.assertEqual(len(names), 53)
        rows = [line for line in content.splitlines() if line.startswith('| `')]
        found = [re.match(r'^\| `([^`]+)` \|', r).group(1) for r in rows]
        self.assertEqual(len(found), 53)
        self.assertEqual(set(found), set(names))
        for row in rows:
            self.assertRegex(row, r'\[FC-\d\d\]\(chains/FC-\d\d-')


    def test_26_boundary_identifiers_are_traceable(self):
        edges = json.loads((T / 'boundaries.v1.json').read_text(encoding='utf-8'))['links']
        content = (F / '11-boundary-traceability.md').read_text(encoding='utf-8')
        rows = [r for r in content.splitlines() if re.match(r'^\| `B-[A-Z]+-\d\d` \|',r)]
        self.assertEqual(len(rows),len(edges))
        self.assertEqual({re.search(r'`(B-[A-Z]+-\d\d)`',r).group(1) for r in rows},
                         {edge['id'] for edge in edges})
        self.assertTrue(all('target_design_not_qualified' == e['state'] for e in edges))

    def test_relative_links_resolve(self):
        for p in [*F.rglob('*.md'), ROOT/'README.md', T/'README.md', ROOT/'docs/index.md']:
            content = p.read_text(encoding='utf-8')
            for target in re.findall(r'\]\(([^)]+)\)', content):
                target = unquote(target.split('#')[0].strip())
                if not target or target.startswith(('http://','https://', 'mailto:', 'data:')):
                    continue
                with self.subTest(source=p.name, target=target):
                    self.assertTrue((p.parent / target).exists(),
                                    f'{p.relative_to(ROOT)} -> {target} missing')


if __name__ == '__main__':
    unittest.main()
