################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022, 2023. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################


from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import (  # type: ignore # noqa
    Flatten as model_to_be_wrapped,
)
from ._common_schemas import schema_feature_columns, schema_target_columns, get_schema_time_column, schema_lookback_win, \
    get_schema_pred_win

import lale.docstrings
import lale.operators


class _FlattenImpl:
    def __init__(
            self,
            feature_columns=[0],
            target_columns=[0],
            id_column=None,
            time_column="time",
            lookback_win=1,
            pred_win=1,
            skip_observation=0,
            mode="forecasting",
    ):
        self._wrapped_model = model_to_be_wrapped(
            feature_columns=feature_columns,
            target_columns=target_columns,
            id_column=id_column,
            time_column=time_column,
            lookback_win=lookback_win,
            pred_win=pred_win,
            skip_observation=skip_observation,
            mode=mode,
        )

    def fit(self, X, y=None):
        self._wrapped_model.fit(X, y)
        return self

    def transform(self, X, y=None):
        return self._wrapped_model.transform(X, y)


_hyperparams_schema = {
    "allOf": [
        {
            "description": "This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.",
            "type": "object",
            "additionalProperties": False,
            "required": [
                "feature_columns",
                "target_columns",
                "id_column",
                "time_column",
                "lookback_win",
                "pred_win",
                "skip_observation",
                "mode",
            ],
            "relevantToOptimizer": [],
            "properties": {
                "feature_columns": schema_feature_columns,
                "target_columns": schema_target_columns,
                "id_column": {
                    "description": "",
                    "anyOf": [{"type": "integer"}, {"enum": [None]}],
                    "default": None,
                },
                "time_column": get_schema_time_column("time"),
                "lookback_win": schema_lookback_win,
                "pred_win": get_schema_pred_win(1),
                "skip_observation": {
                    "description": "",
                    "type": "integer",
                    "minimum": 0,
                    "default": 0,
                },
                "mode": {
                    "description": "",
                    "enum": [
                        "forecasting",
                        "classification",
                    ],
                    "default": "forecasting",
                },
            },
        }
    ]
}

_input_fit_schema = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": True,
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

_input_transform_schema = {
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
    },
}

_output_transform_schema = {
    "description": "Features; the outer array is over samples.",
    "anyOf": [
        {"type": "array", "items": {"laleType": "Any"}},
        {"type": "array", "items": {"type": "array", "items": {"laleType": "Any"}}},
    ],
}

_combined_schemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": """Operator from `autoai_ts_libs`_.

.. _`autoai_ts_libs`: https://pypi.org/project/autoai-ts-libs""",
    "documentation_url": "https://lale-autoai.readthedocs.io/en/latest/modules/lale_autoai.autoai_ts_libs.flatten.html",
    "import_from": "autoai_ts_libs.deps.srom.preprocessing.ts_transformer",
    "type": "object",
    "tags": {"pre": [], "op": ["transformer", "imputer"], "post": []},
    "properties": {
        "hyperparams": _hyperparams_schema,
        "input_fit": _input_fit_schema,
        "input_transform": _input_transform_schema,
        "output_transform": _output_transform_schema,
    },
}

Flatten = lale.operators.make_operator(_FlattenImpl, _combined_schemas)

lale.docstrings.set_docstrings(Flatten)
