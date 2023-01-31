################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022, 2023. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################


from autoai_ts_libs.anomaly_detection.estimators.watson_ts.relationship_ad  import (  # type: ignore # noqa
    UnivariateGraphLassoAD as model_to_be_wrapped,
)
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.anomaly_detection.gaussian_graphical_anomaly_model import GaussianGraphicalModel
from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.ggm_quic import GraphQUIC

from ._common_schemas import *

import lale.docstrings
import lale.operators


class _UnivariateGraphLassoADImpl:
    def __init__(
        self,
        steps=None,
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
        if steps is None:
            steps = [
                ("flatten", Flatten()),
                (
                    "GGM_GraphLasso",
                    GeneralizedAnomalyModel(
                        base_learner=GaussianGraphicalModel(sliding_window_size=0, base_learner=GraphQUIC(), scale=True),
                        predict_function="predict",
                        score_sign=1,
                    ),
                ),
            ]

        self._wrapped_model = model_to_be_wrapped(
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

    def fit(self, X, y=None, **fit_params):
        self._wrapped_model.fit(X, y, **fit_params)
        return self

    def predict(self, X=None, **predict_params):
        return self._wrapped_model.predict(X, predict_params)


_hyperparams_schema = {
    "allOf": [
        {
            "description": "This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.",
            "type": "object",
            "additionalProperties": False,
            "required": [
                "steps",
                "feature_columns",
                "target_columns",
                "lookback_win",
                "time_column",
                "store_lookback_history",
                "distance_metric",
                "observation_window",
                "scoring_method",
                "scoring_threshold",
            ],
            "relevantToOptimizer": [],
            "properties": {
                "steps": get_schema_two_steps("""
                            [
                                ("flatten", Flatten()),
                                (
                                    "GGM_GraphLasso",
                                    GeneralizedAnomalyModel(
                                        base_learner=GaussianGraphicalModel(sliding_window_size=0, base_learner=GraphQUIC(), scale=True),
                                        predict_function="predict",
                                        score_sign=1,
                                    ),
                                ),
                            ]
                            """),
                "feature_columns": get_schema_feature_columns(None),
                "target_columns": get_schema_target_columns(None),
                "lookback_win": get_schema_lookback_win(None),
                "pred_win": get_schema_pred_win(0),
                "time_column": get_schema_time_column(None),
                "store_lookback_history": schema_store_lookback_history,
                "distance_metric": schema_distance_metric,
                "observation_window": schema_observation_window,
                "scoring_method": schema_scoring_method,
                "scoring_threshold": schema_scoring_threshold,
            },
        }
    ]
}

_input_fit_schema = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": False,
    "properties": {
        "X": {  # Handles 1-D arrays as well
            "anyOf": [
                {"type": "array", "items": {"laleType": "Any"}},
                {
                    "type": "array",
                    "items": {"type": "array", "items": {"laleType": "Any"}},
                },
            ]
        },
        "y": {"laleType": "Any"},
    },
}

_input_predict_schema = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": False,
    "properties": {
        "X": {  # Handles 1-D arrays as well
            "anyOf": [
                {"type": "array", "items": {"laleType": "Any"}},
                {
                    "type": "array",
                    "items": {"type": "array", "items": {"laleType": "Any"}},
                },
            ]
        }
    },
}

_output_predict_schema = {
    "description": "Features; the outer array is over samples.",
    "anyOf": [
        {"type": "array", "items": {"laleType": "Any"}},
        {
            "type": "array",
            "items": {"type": "array", "items": {"laleType": "Any"}},
        },
    ],
}

_combined_schemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": """Operator from `autoai_ts_libs`_.
.. _`autoai_ts_libs`: https://pypi.org/project/autoai-ts-libs""",
    "documentation_url": "https://lale-autoai.readthedocs.io/en/latest/modules/lale_autoai.autoai_ts_libs.graph_lasso_ad.html",
    "import_from": "autoai_ts_libs.anomaly_detection.estimators.watson_ts.relationship_ad",
    "type": "object",
    "tags": {"pre": [], "op": ["classifer", "regressor", "estimator"], "post": []},
    "properties": {
        "hyperparams": _hyperparams_schema,
        "input_fit": _input_fit_schema,
        "input_predict": _input_predict_schema,
        "output_predict": _output_predict_schema,
    },
}

UnivariateGraphLassoAD = lale.operators.make_operator(
    _UnivariateGraphLassoADImpl, _combined_schemas
)
lale.docstrings.set_docstrings(UnivariateGraphLassoAD)
