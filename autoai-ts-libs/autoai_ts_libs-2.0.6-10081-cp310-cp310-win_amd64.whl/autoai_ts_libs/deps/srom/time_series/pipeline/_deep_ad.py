import logging

import numpy as np
from autoai_ts_libs.deps.srom.time_series.pipeline import PredAD
from sklearn.base import clone

LOGGER = logging.getLogger(__name__)


class DeepAD(PredAD):
    """
    Deep predicaion base anomaly detector. Uses ensemble of PredAD pipelines and
    aggregates the anomaly scores to stabilize the outcome.

    DAG is a directed acyclic graph. It is defined with multiple options in consequitive steps which are all to be \
    executed in combinations with each other. It is meant as an explorative graph to execute all paths to find the best.

    Parameters
    ----------
        steps : list of PredAD pipelines
            List of PredAD pipelines to be used.
        distance_metric : string, optional
            Metric to compute residual of forecasting model predictions. Defaults to None.
        observation_window : int, optional
            Observation window is used to compute anomaly scores by specified scoring_method. Defaults to 10.
        scoring_method : string, optional
            Anomaly scoring method to compute anomaly score in specified mathematical,
            or statistical method. The computed score is used to label anomalies by
            analyzing residuals computed. Defaults to Chi-Square.
        scoring_threshold : int, optional
            Scoring threhold is used to label computed anomaly score as anomaly or normal. Defaults to 10.


    Example
    -------
    .. code-block:: python

        import pandas as pd
        from sklearn.linear_model import LinearRegression
        from sklearn.ensemble import RandomForestRegressor

        from autoai_ts_libs.deps.srom.time_series.pipeline import PredAD, DeepAD
        from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
        from autoai_ts_libs.deps.srom.utils.data_utils import load_seasonal_trend
        from autoai_ts_libs.deps.srom.time_series.utils.types import AnomalyScoringPredictionType

        df = load_seasonal_trend()
        predad_pipelines = []
        predad_pipelines.append(PredAD(steps=[("flatten", Flatten()),
                                    ("linearregression", LinearRegression())
                                ],
                            lookback_win=6,
                            feature_columns=[0],
                            target_columns=[0],
                            pred_win=1))

        predad_pipelines.append(PredAD(steps=[("flatten", Flatten()),
                                    ("RandomForestRegressor", RandomForestRegressor())
                                ],
                            lookback_win=4,
                            feature_columns=[0],
                            target_columns=[0],
                            pred_win=1))

        toypipeline = DeepAD(steps=predad_pipelines)

        toypipeline.fit(df.values)
        anomaly_scores, _ = toypipeline.anomaly_score(
                X=None, prediction_type=AnomalyScoringPredictionType.BATCH.value, return_threshold=True,
            )
    """

    def __init__(
        self,
        steps,
        distance_metric="min",
        observation_window=10,
        scoring_method="Chi-Square",
        scoring_threshold=10,
    ):
        self.steps = steps
        self.distance_metric = distance_metric
        self.observation_window = observation_window
        self.scoring_method = scoring_method
        self.scoring_threshold = scoring_threshold

    def _aggregate_residuals(self, residuals, distance_metric="min"):
        aggregated_residual = []

        if distance_metric == "min":
            residuals = np.array(residuals)
            aggregated_residual = np.nanmin(residuals, axis=0)
        else:
            raise Exception("Allowed distance metrics in DeepAD are ['min']")

        return aggregated_residual

    def fit(self, X):
        """Build a ensembler estimator from the training set (X, y).
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
        y : array-like of shape (n_samples,)
            The target values.
        Returns
        -------
        self : object
            Fitted estimator.
        """
        model_wise_training_error_ = []
        self.estimators_ = [clone(estimator) for estimator in self.steps]
        for tsmodel in self.estimators_:
            tsmodel.fit(X)
            model_wise_training_error_.append(tsmodel.training_error_)

        self.training_error_ = self._aggregate_residuals(
            model_wise_training_error_, distance_metric=self.distance_metric
        )

        return self

    def prediction_error(self, X, append_training_error=False):
        """This method is used as baseline for prediciton.
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Returns
        -------
        all_errors_ : np.array
            minimum of modelwise prediction error.
        """
        model_wise_pred_error = []
        for tsmodel in self.estimators_:
            model_wise_pred_error.append(
                tsmodel.prediction_error(X, append_training_error=append_training_error)
            )
        # we select now the minimum error
        all_error_ = self._aggregate_residuals(
            model_wise_pred_error, distance_metric=self.distance_metric
        )
        return all_error_
