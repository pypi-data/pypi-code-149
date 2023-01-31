import copy
from sklearn.pipeline import Pipeline
from inspect import signature


class FunctionPipeline(Pipeline):
    def __init__(self, steps):
        self.steps = steps
        self.score = None

    def fit(self, X=None, **fit_params):
        fit_params_steps = self._check_fit_params(**fit_params)
        if X is not None:
            X_ = copy.deepcopy(X)
            for name, obj in self.steps:
                fit_params = {
                    key: val[0] for key, val in fit_params_steps[name].items()
                }
                X_ = obj(X_, **fit_params)
        else:
            for name, obj in self.steps:
                fit_params = {
                    key: val[0] for key, val in fit_params_steps[name].items()
                }
                X_ = obj(**fit_params)

        self.score = X_

    def score(self, X):
        if self.score is None:
            self.fit(X)
        return self.score

    def __get_function_params(self, name, func):
        """
        Returns parameter dictionary for any function
        """
        sign = signature(func)

        param_dict = {}
        for i in sign.parameters.items():
            key = i[0]
            val = sign.parameters[key].default
            if str(val) == "<class 'inspect._empty'>":
                val = "no params"
            param_dict[str(name) + "__" + key] = val
        return param_dict

    def get_params(self, deep=True):
        params = super(FunctionPipeline, self).get_params(deep=deep)
        for step in params["steps"]:
            param_dict = self.__get_function_params(name=step[0], func=step[1])
            params.update(param_dict)

        return params
