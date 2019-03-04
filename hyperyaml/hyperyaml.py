"""
Main HyperYAML module
"""
import yaml
from hyperyaml.reader import YAMLReader
from hyperyaml.runner import Runner


class HyperYaml:
    """
    Create and Run Hyperparameter Optimizations
    Declaratively
    """
    def __init__(self, model_config, model_builder, max_evals):
        self.params = YAMLReader.read(model_config)
        self.model_builder = model_builder
        self.max_evals = max_evals
        self.best_set = None

    def run(self):
        """
        Run the hyperparameter optimization
        """
        runner = Runner(self.params, self.model_builder, self.max_evals)
        best, trials = runner.run()
        print(f"Hyperparameter optimization complete, best loss was {min(trials.losses())}")
        self.best_set = best
        return best, trials

    def write(self, out):
        """
        Write the best parameter configuration to a file
        :param out: the file path to write to
        """
        with open(out, "w") as stream:
            yaml.dump(self.best_set, stream=stream, default_flow_style=False)
