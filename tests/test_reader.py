import unittest
from hyperyaml.reader import YAMLReader

class TestReader(unittest.TestCase):
    def setUp(self):
        self.fp = "mock/params.yaml"

    def test_init(self):
        reader = YAMLReader.read(self.fp)
        self.assertIsNotNone(reader)

    def test_init_nofile(self):
        with self.assertRaises(ValueError):
            YAMLReader.read("no_such_file")

    def test_len(self):
        params = YAMLReader.read(self.fp)
        self.assertEqual(2, len(params))

    def test_field_types(self):
        params = YAMLReader.read(self.fp)
        fst = params[0]
        self.assertIsInstance(fst.name, str)
        self.assertIsInstance(fst.dtype, str)
        self.assertIsInstance(fst.min, int)
        self.assertIsInstance(fst.max, int)
