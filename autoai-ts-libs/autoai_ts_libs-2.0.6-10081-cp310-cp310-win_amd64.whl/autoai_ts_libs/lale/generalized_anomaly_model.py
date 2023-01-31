################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022, 2023. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################


from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model  import (  # type: ignore # noqa
    GeneralizedAnomalyModel as model_to_be_wrapped,
)
from sklearn.ensemble import IsolationForest

import lale.docstrings
import lale.operators


class _GeneralizedAnomalyModelImpl:
    def __init__(
        self,
        base_learner=None,
        fit_function="fit",
        predict_function="predict",
        score_sign=-1,
    ):
        if base_learner is None:
            base_learner = IsolationForest()

        self._wrapped_model = model_to_be_wrapped(
            base_learner=base_learner,
            fit_function=fit_function,
            predict_function=predict_function,
            score_sign=score_sign,
        )

    def fit(self, X, y=None):
        self._wrapped_model.fit(X, y)
        return self

    def predict(self, X, y=None):
        return self._wrapped_model.predict(X, y)

    def anomaly_score(self, X, y=None):
        return self._wrapped_model.anomaly_score(X, y)

    def decision_function(self, X):
        return self._wrapped_model.decision_function(X)


_hyperparams_schema = {
    "allOf": [
        {
            "description": "This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.",
            "type": "object",
            "additionalProperties": False,
            "required": [
                "base_learner",
                "fit_function",
                "predict_function",
                "score_sign",
            ],
            "relevantToOptimizer": [],
            "properties": {
                "base_learner": {
                    "description": "Base learning model instance to be used.",
                    "anyOf": [
                        {"laleType": "operator"},
                        {
                            "enum": [None],
                            "description": "IsolationForest()",
                        },
                    ],
                    "default": None,
                },
                "fit_function": {
                    "description": "Fit function to be used while training.",
                    "enum": [
                        "fit",
                    ],
                    "default": "fit",
                },
                "predict_function": {
                    "description": " Predict function to be used while prediction.",
                    "enum": [
                        "predict",
                        "srom_log_liklihood",
                        "decision_function",
                        "fit_predict_score",
                    ],
                    "default": "predict",
                },
                "score_sign": {
                    "description": "",
                    "enum": [
                        1,
                        -1
                    ],
                    "default": -1,
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
    "documentation_url": "https://lale-autoai.readthedocs.io/en/latest/modules/lale_autoai.autoai_ts_libs.generalized_anomaly_model.html",
    "import_from": "autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model",
    "type": "object",
    "tags": {"pre": [], "op": ["classifer", "regressor", "estimator"], "post": []},
    "properties": {
        "hyperparams": _hyperparams_schema,
        "input_fit": _input_fit_schema,
        "input_predict": _input_predict_schema,
        "output_predict": _output_predict_schema,
    },
}

GeneralizedAnomalyModel = lale.operators.make_operator(
    _GeneralizedAnomalyModelImpl, _combined_schemas
)
lale.docstrings.set_docstrings(GeneralizedAnomalyModel)
