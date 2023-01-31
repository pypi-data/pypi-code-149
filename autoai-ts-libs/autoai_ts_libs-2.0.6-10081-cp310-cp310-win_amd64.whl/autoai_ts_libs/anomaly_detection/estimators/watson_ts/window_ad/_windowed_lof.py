################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

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
from autoai_ts_libs.deps.srom.preprocessing.transformer import DataStationarizer
from sklearn.neighbors import LocalOutlierFactor
import numpy as np
from autoai_ts_libs.anomaly_detection.estimators.utils.prediction_types import PredictionTypes
RANDOM_STATE = 42

class ExtendedLocalOutlierFactor(LocalOutlierFactor):

    def fit(self, X, y=None):
        self.trainX_ = X
        return self

    def fit_predict_score(self, X):
        newX = np.concatenate([self.trainX_,X])
        super().fit(newX)
        return self.negative_outlier_factor_[len(self.trainX_):]

class WindowedLOF(Base):
    def __init__(
        self,
        steps=[
            (
                "Flatten",
                Flatten(),
            ),
            (
                "LocalOutlierFactor",
                GeneralizedAnomalyModel(
                    base_learner=ExtendedLocalOutlierFactor(n_neighbors=20,algorithm="auto",leaf_size=30,metric='minkowski',p=2),
                    fit_function="fit",
                    predict_function="fit_predict_score",
                    score_sign=-1,
                ),
            ),
        ],
        *,
        feature_columns=None,
        target_columns=None,
        lookback_win=100,
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
        pipeline_name = "WindowLOF"
        return pipeline_name

