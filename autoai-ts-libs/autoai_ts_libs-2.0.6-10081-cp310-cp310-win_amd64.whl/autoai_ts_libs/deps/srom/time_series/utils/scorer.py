import numpy as np
from sklearn.metrics._scorer import _BaseScorer, _cached_call
from autoai_ts_libs.deps.srom.time_series.pipeline import Forecaster
from functools import partial


class _TSPredictScorer(_BaseScorer):
    """
    ??? add doc string ??? or explanation
    """

    def __call__(self, estimator, X, y_true=None, sample_weight=None):
        """Evaluate predicted target values for X relative to y_true.
        Parameters
        ----------
        estimator : object
            Trained estimator to use for scoring. Must have a predict_proba
            method; the output of that is used to compute the score.
        X : {array-like, sparse matrix}
            Test data that will be fed to estimator.predict.
        y_true : array-like
            Gold standard target values for X.
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.
        Returns
        -------
        score : float
            Score function applied to prediction of estimator on X.
        """
        return self._score(partial(_cached_call, None), estimator, X, y_true,
                           sample_weight=sample_weight)


    def _score(self, method_caller, estimator, X, y_true=None, sample_weight=None):
        y_pred = method_caller(estimator, "predict", X, prediction_type="sliding")

        # generate y_true, we need which column of X to be used as output column, what is the pred_win and step size
        # this information we can expect to obtain from estimator, assume estimator is of type Forecaster, we can get it
        # we need to generate the groudthuth now, generate y_true
        # compare the shape of y_ture and y_pred if there is a miss match raise an exception

        if isinstance(estimator, Forecaster):

            def _generate_ground_truth(X):
                new_X = X[:, estimator.target_columns].copy()
                n = new_X.shape[0]
                return np.hstack(
                    new_X[i : 1 + n + i - estimator.pred_win : 1]
                    for i in range(0, estimator.pred_win)
                )

            y_true = _generate_ground_truth(X)
        else:
            raise ValueError("estimator must be instance of Forecaster")

        if sample_weight is not None:
            return self._sign * self._score_func(
                y_true, y_pred, sample_weight=sample_weight, **self._kwargs
            )
        else:
            return self._sign * self._score_func(y_true, y_pred, **self._kwargs)


def make_ts_scorer(score_func, *, greater_is_better=True, **kwargs):
    sign = 1 if greater_is_better else -1
    return _TSPredictScorer(score_func, sign, kwargs)
