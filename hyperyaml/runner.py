"""
HyperParameter Optimization Runner Class
A wrapper for Hyperopt
"""
from hyperopt import hp, fmin, tpe, Trials



class Runner:
    """
    Wrapper for hyperopt class
    """
    def __init__(self, params, model_builder, max_evals):
        self.params = params
        self.search_space = self._build_search_space()
        self.names = [p.name for p in params]
        self.model_builder = model_builder
        self.max_evals = max_evals
        self.trials = None

    def _build_search_space(self):
        space = []
        for parm in self.params:
            if parm.dtype == "int":
                sub = hp.quniform(parm.name, parm.min, parm.max, 1)
            else:
                sub = hp.uniform(parm.name, parm.min, parm.max)
            space.append(sub)
        return space

    def _decorator(self, values):
        combined_names = zip(self.params, values)
        type_corrected_tuples = []
        for param, value in combined_names:
            if param.dtype == int:
                value = int(value)
            type_corrected_tuples.append((param.name, value))
        args = dict(type_corrected_tuples)
        return self.model_builder.build(args)

    def get_trials(self):
        """
        get the trials object
        """
        return self.trials

    def run(self):
        """
        Run the HyperParameter Optimization
        """
        objective = self._decorator
        trials = Trials()
        best = fmin(objective,
                    space=self.search_space,
                    algo=tpe.suggest,
                    max_evals=self.max_evals,
                    trials=trials)
        self.trials = trials
        return best, trials
