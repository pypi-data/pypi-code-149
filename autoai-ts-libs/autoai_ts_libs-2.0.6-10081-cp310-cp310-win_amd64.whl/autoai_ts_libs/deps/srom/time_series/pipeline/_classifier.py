import logging

import numpy as np
from sklearn.metrics._scorer import neg_mean_absolute_error_scorer
from sklearn.pipeline import Pipeline

LOGGER = logging.getLogger(__name__)


class Classifier(Pipeline):
    def __init__(
            self,
            steps,
            *,
            feature_columns=None,
            target_columns=None,
            time_column=None,
            id_column=None,
            lookback_win=None,
            pred_win=None,
            skip_observation=0,
            scoring=neg_mean_absolute_error_scorer,
    ):
        self.steps = steps
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.time_column = time_column
        self.scoring = scoring
        self.id_column = id_column
        self.skip_observation = skip_observation

    def set_scoring(self, scoring):
        """
        Set the scoring mechanism.
        """
        self.scoring = scoring

    def _check_X(self, X):
        """This method return X, after conversion to appropriate columns"""

        if isinstance(X, (np.ndarray, np.generic)):
            X = X.copy()
            if X.dtype != "object":
                X = X.astype(object)
            clm_for_float_conversion = list(
                set(self.feature_columns + self.target_columns)
            )
            X[:, clm_for_float_conversion] = X[:, clm_for_float_conversion].astype(
                float
            )

        return X

    def _forward_fit_data_transformation(self, X, y=None):
        """This must be called from fit only.

        Args:
            X (np.array): Input to pass through forward fit transformation
            y (np.array, optional): Labels. Defaults to None.

        Returns:
            np.array: Transformed data
        """

        Xt = X
        yt = y
        for _, transformer in self.steps[:-1]:
            if hasattr(transformer, "fit_transform"):
                res = transformer.fit_transform(Xt, yt)
            else:

                res = transformer.fit(Xt, yt).transform(Xt)

            if isinstance(res, tuple):
                x_res = res[0]
                yt = res[1]
            else:
                x_res = res

            Xt = x_res

        return Xt, yt

    def _set_steps_for_fit(self):
        """
        Sets time series params for step components
        """
        step_params = [
            "feature_columns",
            "target_columns",
            "lookback_win",
            "pred_win",
            "time_column",
            "id_column",
            "skip_observation",
        ]

        for step in self.steps:
            params = {}
            for param in step_params:
                if param in step[1].get_params().keys():
                    params[param] = getattr(self, param)
            if len(params) != 0:
                # we push responsibility back to the classifier
                step[1].set_params(**params)

    def fit(self, X, y=None):
        """
        This method create an srom estimator object and then call its fit

        Important steps:
        feature_columns attribute need to pass to the respecting object of steps

        for each step in self.steps:
            get its parameter
            set some of its parameter such as feature_columns, target_columns
            this one need little bit co-ordination across different method such as
            flatten etc
        """

        # init the parameter of each component
        self._set_steps_for_fit()

        Xt, yt = self._forward_fit_data_transformation(X, y)
        self.steps[-1][1].fit(Xt, yt)

        return self

    def predict(self, X):
        """
        This method call the predict of an srom estimator
        """
        # this is for this pipeline
        X = self._check_X(X)

        Xt, _ = self._forward_fit_data_transformation(X)
        y_pred = self.steps[-1][1].predict(Xt)

        return y_pred

    def score(self, X, y=None, sample_weight=None):
        """
        This method call the predict of an srom estimator
        """
        # this is for this pipeline
        X = self._check_X(X)

        Xt, yt = self._forward_fit_data_transformation(X, y)
        y_pred = self.steps[-1][1].predict(Xt)
        score_params = {}
        if sample_weight is not None:
            score_params["sample_weight"] = sample_weight
        if sample_weight is not None:
            return self.scoring._sign * self.scoring._score_func(
                yt, y_pred, sample_weight=sample_weight, **self.scoring._kwargs
            )
        else:
            return self.scoring._sign * self.scoring._score_func(
                yt, y_pred, **self.scoring._kwargs
            )
