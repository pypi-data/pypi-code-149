################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022, 2023. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################


from autoai_ts_libs.deps.srom.anomaly_detection.gaussian_graphical_anomaly_model  import (  # type: ignore # noqa
    GaussianGraphicalModel as model_to_be_wrapped,
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_graph_lasso import AnomalyGraphLasso

import lale.docstrings
import lale.operators


class _GaussianGraphicalModelImpl:
    def __init__(
        self,
        base_learner=None,
        distance_metric="KL_Divergence",
        sliding_window_size=50,
        sliding_window_data_cutoff=15,
        scale=True,
    ):
        if base_learner is None:
            base_learner = AnomalyGraphLasso(alpha=0.5)

        self._wrapped_model = model_to_be_wrapped(
            base_learner=base_learner,
            distance_metric=distance_metric,
            sliding_window_size=sliding_window_size,
            sliding_window_data_cutoff=sliding_window_data_cutoff,
            scale=scale,
        )

    def fit(self, X, y=None):
        self._wrapped_model.fit(X, y)
        return self

    def predict(self, X):
        return self._wrapped_model.predict(X)


_hyperparams_schema = {
    "allOf": [
        {
            "description": "This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.",
            "type": "object",
            "additionalProperties": False,
            "required": [
                "base_learner",
                "distance_metric",
                "sliding_window_size",
                "sliding_window_data_cutoff",
                "scale",
            ],
            "relevantToOptimizer": [],
            "properties": {
                "base_learner": {
                    "description": "Covariance model instance to be used.",
                    "anyOf": [
                        {"laleType": "operator"},
                        {
                            "enum": [None],
                            "description": "AnomalyGraphLasso(alpha=0.5)",
                        },
                    ],
                    "default": None,
                },
                "distance_metric": {
                    "description": "Distance metric.",
                    "enum": [
                        "KL_Divergence",
                        "Frobenius_Norm",
                        "Likelihood",
                        "Spectral",
                        "Mahalanobis_Distance",
                    ],
                    "default": "KL_Divergence",
                },
                "sliding_window_size": {
                    "description": "",
                    "anyOf": [
                        {"type": "integer", "minimum": 0},
                        {
                            "enum": [-1],
                            "description": "The setting corresponds to \"outlier analysis\""
                        }
                    ],
                    "default": 50,
                },
                "sliding_window_data_cutoff": {
                    "description": "",
                    "type": "integer",
                    "minimum": 0,
                    "default": 15,
                },
                "scale": {
                    "description": "",
                    "type": "boolean",
                    "default": True,
                },
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
    "documentation_url": "https://lale-autoai.readthedocs.io/en/latest/modules/lale_autoai.autoai_ts_libs.gaussian_graphical_anomaly_model.html",
    "import_from": "autoai_ts_libs.deps.srom.anomaly_detection.gaussian_graphical_anomaly_model",
    "type": "object",
    "tags": {"pre": [], "op": ["classifer", "regressor", "estimator"], "post": []},
    "properties": {
        "hyperparams": _hyperparams_schema,
        "input_fit": _input_fit_schema,
        "input_predict": _input_predict_schema,
        "output_predict": _output_predict_schema,
    },
}

GaussianGraphicalModel = lale.operators.make_operator(
    _GaussianGraphicalModelImpl, _combined_schemas
)
lale.docstrings.set_docstrings(GaussianGraphicalModel)
