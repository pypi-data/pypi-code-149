################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

from tkinter import W
from ._base import Base

"""
from watson_ts.blocks.transformers.srom_flatten import Flatten
from watson_ts.blocks.anomaly_detection.srom_generalized_anomaly_model import (
    GeneralizedAnomalyModel,
)
from watson_ts.blocks.transformers.srom_data_stationarizer import DataStationarizer
"""

from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.timeseries_isolation_forest import TSIsolationForest

RANDOM_STATE = 42


class WindowedTSIsolationForest(Base):
    def __init__(
        self,
        steps=[
            (
                "Flatten",
                Flatten(),
            ),
            (
                "IsolationForest",
                GeneralizedAnomalyModel(
                    base_learner=TSIsolationForest(random_state=RANDOM_STATE,n_extra_estimators=200,fit_mode='offline'),
                    fit_function="fit",
                    predict_function="decision_function",
                    score_sign=-1,
                ),
            ),
        ],
        *,
        feature_columns=None,
        target_columns=None,
        lookback_win=1,
        pred_win=0,
        time_column=None,
        store_lookback_history=True,
        distance_metric="mse",
        observation_window=10,
        scoring_method="otsu_label",
        scoring_threshold=2,
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
        :return:
        """
        pipeline_name = "WindowTSIsolationForest"
        return pipeline_name
