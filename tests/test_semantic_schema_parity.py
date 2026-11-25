"""A schema mismatch blocks coordination without modifying either owner."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from check_semantic_schema_parity import verify


class SemanticSchemaParityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.framework = root / 'framework'
        self.dik = root / 'dik'
        self.f = self.framework / 'schemas/v11'
        self.d = self.dik / 'src/dik/_framework/schemas/v11'
        self.f.mkdir(parents=True)
        self.d.mkdir(parents=True)
        self.roots = {'Kristal-Framework': self.framework, 'diK': self.dik}
        for n in range(11):
            name = f'schema-{n}.schema.json'
            payload = json.dumps({'kind': n}).encode()
            (self.f / name).write_bytes(payload)
            (self.d / name).write_bytes(payload)

    def test_identical_eleven_schemas_are_only_an_integrity_match(self):
        result = verify(self.roots)
        self.assertEqual(result['status'], 'MATCH')
        self.assertEqual(result['schemas_checked'], 11)
        self.assertIn('not cross-repository qualification', result['interpretation'])

    def test_one_modified_schema_blocks(self):
        (self.d / 'schema-3.schema.json').write_bytes(b'changed')
        self.assertEqual(verify(self.roots)['status'], 'BLOCKED_SCHEMA_DRIFT')

    def test_missing_schema_blocks(self):
        (self.d / 'schema-7.schema.json').unlink()
        self.assertEqual(verify(self.roots)['status'], 'BLOCKED_SCHEMA_DRIFT')


if __name__ == '__main__':
    unittest.main()
