################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

# will be back 
# from watson_ts.workflows.anomaly_detection.srom_window_ad import WindowAD

from autoai_ts_libs.deps.srom.time_series.pipeline import WindowAD
from autoai_ts_libs.deps.srom.time_series.utils.extended_window_ad import ExtendedWindowAD
from autoai_ts_libs.anomaly_detection.estimators.utils.prediction_types import PredictionTypes
from autoai_ts_libs.anomaly_detection.estimators.api.base import TSADEstimator
from autoai_ts_libs.anomaly_detection.estimators.constants import NON_ANOMALY, ANOMALY

import numpy as np


class Base(WindowAD, TSADEstimator):
    def __init__(
        self,
        steps,
        *,
        feature_columns=None,
        target_columns=None,
        lookback_win=None,
        pred_win=0,
        time_column=None,
        store_lookback_history=True,
        distance_metric="mse",
        observation_window=10,
        scoring_method="Chi-Square",
        scoring_threshold=10,
        **kwargs
    ):
        super().__init__(
            steps=steps,
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            time_column=time_column,
            store_lookback_history=store_lookback_history,
            distance_metric=distance_metric,
            observation_window=observation_window,
            scoring_method=scoring_method,
            scoring_threshold=scoring_threshold,
            **kwargs
        )

    def predict(self, X, prediction_type=PredictionTypes.Sliding.value):
        return super().predict(X, prediction_type=prediction_type)

    def anomaly_score(self, X, prediction_type=PredictionTypes.Sliding.value):
        return super().anomaly_score(X, prediction_type=prediction_type)

    def decision_function(self, X):
        return self.anomaly_score(X).reshape(-1, 1)

    @property
    def classes_(self):
        """The classes labels. Use labels from super() if available."""
        try:
            super().classes_
        except AttributeError:
            return np.array([NON_ANOMALY, ANOMALY])


class ExtendedBase(ExtendedWindowAD, TSADEstimator):
    def __init__(
        self,
        steps,
        *,
        feature_columns=None,
        target_columns=None,
        lookback_win=None,
        pred_win=0,
        time_column=None,
        store_lookback_history=True,
        distance_metric="mse",
        observation_window=10,
        scoring_method="Chi-Square",
        scoring_threshold=10,
        **kwargs
    ):
        super().__init__(
            steps=steps,
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            time_column=time_column,
            store_lookback_history=store_lookback_history,
            distance_metric=distance_metric,
            observation_window=observation_window,
            scoring_method=scoring_method,
            scoring_threshold=scoring_threshold,
            **kwargs
        )

    def predict(self, X, prediction_type=PredictionTypes.Sliding.value):
        return super().predict(X, prediction_type=prediction_type)

    def anomaly_score(self, X, prediction_type=PredictionTypes.Sliding.value):
        newX = np.concatenate([self.trainX_, X])
        super(ExtendedWindowAD, self).fit(newX)
        ad_score = super().anomaly_score(X, prediction_type=prediction_type)
        return ad_score[
            -len(X) :,
        ]

    def decision_function(self, X):
        return self.anomaly_score(X).reshape(-1, 1)

    @property
    def classes_(self):
        """The classes labels. Use labels from super() if available."""
        try:
            super().classes_
        except AttributeError:
            return np.array([NON_ANOMALY, ANOMALY])

