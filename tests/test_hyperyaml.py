from hyperyaml.hyperyaml import HyperYaml
from tests.mock.model_builder import ModelBuilerMock
import unittest
from os.path import isfile
from os import remove


class testHyperYAML(unittest.TestCase):
    def setUp(self):

        self.fp = "tests/mock/params.yaml"
        self.out_fp = "out.yaml"
        self.model_builder = ModelBuilerMock()
        self.max_trials = 400
        self.hy = HyperYaml(self.fp, self.model_builder, self.max_trials)

    def test_init(self):
        self.assertIsNotNone(self.hy)

    def test_run(self):
        best, trials = self.hy.run()
        self.assertAlmostEqual(0.5, min(trials.losses()), places=1)

    def test_out(self):
        self.hy.run()
        self.hy.write(self.out_fp)

    def tearDown(self):
        if isfile(self.out_fp):
            remove(self.out_fp)
