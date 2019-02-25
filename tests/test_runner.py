from hyperyaml.runner import Runner
from tests.mock.model_builder import ModelBuilerMock
from hyperyaml.types import Parameter
import unittest

class TestRunner(unittest.TestCase):
    def setUp(self):
        p1 = Parameter("p1", "int", 1, 4)
        p2 = Parameter("p2", "int", 2, 7)
        p3 = Parameter("p3", "float", 0.5, 2)
        self.params = [p1,p2, p3]
        self.model = ModelBuilerMock()
        self.max_evals = 250

    def test_init(self):
        runner = Runner(self.params, self.model, self.max_evals)
        self.assertIsNotNone(runner)

    def test_run(self):
        runner = Runner(self.params, self.model, self.max_evals)
        best, trials = runner.run()
        self.assertEqual(1,best["p1"])
        self.assertEqual(2, best["p2"])
        self.assertAlmostEqual(0.5, best["p3"], places=2)
        self.assertAlmostEqual(1, min(trials.losses()),places=2)
