################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

from ._base import Base
from autoai_ts_libs.deps.srom.time_series.models.MT2RForecaster import MT2RForecaster
from autoai_ts_libs.anomaly_detection.estimators.utils.prediction_types import PredictionTypes
import numpy as np

class MT2RForecasterAD(Base):
    def __init__(
        self,
        steps=[("mt2r", MT2RForecaster())],
        *,
        feature_columns=None,
        target_columns=None,
        lookback_win=10,
        pred_win=1,
        time_column=None,
        store_lookback_history=True,
        observation_window=10,
        distance_metric="euclidean",
        scoring_method="otsu_label",
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

    def get_pipeline_name(self):
        """
        To return unique pipeline name
        TODO: There should be an automatic mechanism between setting this name and those defined in `PIPELINE_INFO` in prep_ts_ad.py
        """
        pipeline_name = "T2RForecaster"
        return pipeline_name

    def decision_function(self, X):
        score = self.anomaly_score(X)
        score = np.nanmax(score,axis=1)
        return score.reshape(-1,1)