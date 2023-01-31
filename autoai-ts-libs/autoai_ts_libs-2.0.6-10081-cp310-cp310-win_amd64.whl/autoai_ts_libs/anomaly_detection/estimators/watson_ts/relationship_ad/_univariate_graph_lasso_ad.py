################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

from ._graph_lasso_ad import GraphLassoAD
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.anomaly_detection.gaussian_graphical_anomaly_model import (
    GaussianGraphicalModel,
)
from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.ggm_quic import GraphQUIC


class UnivariateGraphLassoAD(GraphLassoAD):
    def __init__(
        self,
        steps=[
            ("flatten", Flatten()),
            (
                "GGM_GraphLasso",
                GeneralizedAnomalyModel(
                    base_learner=GaussianGraphicalModel(
                        sliding_window_size=0, base_learner=GraphQUIC(), scale=True
                    ),
                    predict_function="predict",
                    score_sign=1,
                ),
            ),
        ],
        *,
        feature_columns=None,
        target_columns=None,
        lookback_win=None,
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
