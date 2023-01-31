################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022, 2023. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################


from autoai_ts_libs.anomaly_detection.estimators.watfore.pointwise_bounded_ad  import (  # type: ignore # noqa
    PointwiseBoundedAnomalyDetector as model_to_be_wrapped,
)
from ._common_schemas import *
from autoai_ts_libs.anomaly_detection.estimators.constants import RUNMODE_TEST

import lale.docstrings
import lale.operators


class _PointwiseBoundedAnomalyDetectorImpl:
    def __init__(
        self,
        confidence_interval=0.95,
        algorithm="hw",
        algorithm_type="additive",
        ts_icol_loc=-1,
        log_transform=False,
        lookback_win=1,
        target_column_indices=-1,
        feature_column_indices=-1,
        error_history_length=2,
        use_full_error_history=False,
        error_horizon_length=2,
        max_anomaly_count=-1,
        update_with_anomaly=True,
        run_mode=RUNMODE_TEST,
        **kwargs
    ):
        self._wrapped_model = model_to_be_wrapped(
            confidence_interval=confidence_interval,
            algorithm=algorithm,
            algorithm_type=algorithm_type,
            ts_icol_loc=ts_icol_loc,
            log_transform=log_transform,
            lookback_win=lookback_win,
            target_column_indices=target_column_indices,
            feature_column_indices=feature_column_indices,
            error_history_length=error_history_length,
            use_full_error_history=use_full_error_history,
            error_horizon_length=error_horizon_length,
            max_anomaly_count=max_anomaly_count,
            update_with_anomaly=update_with_anomaly,
            run_mode=run_mode,
            **kwargs
        )

    def fit(self, X, y=None, _reset_model=True, **fit_params):
        self._wrapped_model.fit(X, y, _reset_model, **fit_params)
        return self

    def predict(self, X=None):
        return self._wrapped_model.predict(X)


_hyperparams_schema = {
    "allOf": [
        {
            "description": "This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.",
            "type": "object",
            "additionalProperties": False,
            "required": [
                "confidence_interval",
                "algorithm",
                "algorithm_type",
                "ts_icol_loc",
                "log_transform",
                "lookback_win",
                "target_column_indices",
                "feature_column_indices",
                "error_history_length",
                "use_full_error_history",
                "error_horizon_length",
                "max_anomaly_count",
                "update_with_anomaly",
                "run_mode",
            ],
            "relevantToOptimizer": [],
            "properties": {
                "confidence_interval": {
                    "description": "",
                    "type": "number",
                    "default": 0.95,
                },
                "algorithm": {
                    "description": """Algorithm that is used to initialize the prediction model. Currently supported are 'hw' i.e. holtwinters,
                'arima','bats', autoforecaster i.e., BATS model with Box-Conx transformation. Algorithm specific parameters
                also need to be specified.
                Additive and multiplicative variants of the Holt-Winters Seasonal forecasting method. This implementation of
                the Holt-Winter algorithm variants assumes that the data it receives satisfy the above conditions.
                Any pre-processing the data needs in order to satisfy the above assumptions should take place prior to model
                updates and calls for prediction. This approach was followed in order to allow any type of pre-processing
                (for example for filling missing values) on the data, independent of the H-W core calculations.
                Implementation of BATS (Box-Cox transform, ARMA errors, Trend, and Seasonal components) Algorithms
                Reference: Alysha M De Livera, Rob J Hyndman and Ralph D Snyder, "Forecasting time series with complex seasonal
                patterns using exponential smoothing," Journal of the American Statistical Association (2011) 106(496), 1513-1527.
                If algorithm = autoforecaster, This trains all models and to keep running statistics on their forecasting
                errors as updates are requested. The error statistics are used to continually update the selection
                of the best model, which is used to do the forecasts in the super class. The algorithm becomes initialized as
                soon as the first algorithm becomes initialized so as to allow forecasts as soon as possible. It continues to
                rate new algorithms as they become initialized and/or subsequent updates are applied.""",
                    "enum": [
                        "hw",
                        "arima",
                        "bats",
                        "autoforecaster",
                        "arimax",
                        "arimax_palr",
                        "arimax_rsar",
                        "arimax_rar",
                        "arimax_dmlr"
                    ],
                    "default": "hw",
                },
                "algorithm_type": {
                    "description": """(HoltWinters(hw) ONLY, i.e. when algorithm=watfore.Forecasters.hw or algorithm='hw')
                `additive` provides implementation of the additive variant of the Holt-Winters Seasonal forecasting method.
                The additive variant has the seasonal and trend/slope components enter the forecasting function in an
                additive manner (see ref. 1), as in
                See http://books.google.com/books?id=GSyzox8Lu9YC&source=gbs_navlinks_s for more information.
                y(t+h) = L(t) + t*H(t) + S(t+h)
                where
                t = latest time for which the model has been updated
                h = number of steps ahead for which a forecast is desired
                L(t) = is the level estimate at time t
                H(t) = is the slope at time t
                S(t+h) = is the seasonal component at time t + h.
                `multiplicative`, provides implementation of the multiplicative variant of the Holt-Winters Seasonal forecasting
                method. The multiplicative variant has the seasonal and trend/slope components enter the forecasting function
                in a multiplicative manner (see ref. 1, Brockwell, pp. 329).
                y(t+h) = (L(t) + t* H(t)) * S(t+h)""",
                    "enum": ["additive", "multiplicative", None],
                    "default": "additive",
                },
                "ts_icol_loc": {
                    "description": """This parameter tells the forecasting model the absolute location of the timestamp column. For specifying
time stamp location put value in array e.g., [0] if 0th column is time stamp. The array is to support
multiple timestamps in future. If ts_icol_loc = -1 that means no timestamp is provided and all data is
time series. With ts_icol_loc=-1, the model will assume all the data is ordered and equally sampled.""",
                    "anyOf": [
                        {"type": "array", "items": {"type": "integer"}},
                        {"enum": [-1]},
                    ],
                    "default": -1,
                },
                "log_transform": {
                    "description": "Whether a log transform of the data should be applied before fitting the estimator.",
                    "anyOf": [{"type": "boolean"}, {"enum": [None]}],
                    "default": False,
                },
                "lookback_win": get_schema_lookback_win(1),
                "target_column_indices": get_schema_target_columns(-1),
                "feature_column_indices": get_schema_feature_columns(-1),
                "error_history_length": {
                    "description": """ (hw ONLY)""",
                    "type": "integer",
                    "default": 2,
                },
                "use_full_error_history": {
                    "description": """(ARIMA and HoltWinters (hw) ONLY) Trains arima model using full
error history from the data. If False, then only the last errorHorizonLength updates will be considered in the
values returned. The resulting instance:
1. does not force a model if suitable orders and/or coefficients can not be found. This can result in a model
which can not be initialized.
2.picks the required amount of training data automatically.
3.finds the AR order automatically.
4. finds the MA order automatically.
5.finds the difference order automatically.""",
                    "type": "boolean",
                    "default": False,
                },
                "error_horizon_length": {
                    "description": """(ARIMA ONLY) This parameter is used only when algorithm='arima' or watfore.Forecasters.arima, this is error horizon for
error in arima model.""",
                    "type": "integer",
                    "default": 2,
                },
                "max_anomaly_count": {
                    "description": "",
                    "type": "integer",
                    "default": -1,
                },
                "update_with_anomaly": {
                    "description": "",
                    "type": "boolean",
                    "default": True,
                },
                "run_mode": {
                    "description": "",
                    "enum": [
                        "test",
                        "integration",
                    ],
                    "default": "test",
                },
            },
        },
        # {
        #     "description": "Algorithm type may only be specified (not None) if the algorithm is \"hw\"",
        #     "anyOf": [
        #         {"type": "object", "required": ["algorithm"], "properties": {"algorithm": {"enum": ["hw"]}}, },
        #         {"type": "object", "properties": {"algorithm_type": {"enum": [None]}}},
        #     ],
        # },
        {
            "description": "use_full_error_history can only be specified for arima or hw algorithms",
            "anyOf": [
                {"type": "object", "required": ["algorithm"], "properties": {"algorithm": {"enum": ["hw", "arima"]}}, },
                {"type": "object", "properties": {"use_full_error_history": {"enum": [False]}}},
            ],
        },
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
    "documentation_url": "https://lale-autoai.readthedocs.io/en/latest/modules/lale_autoai.autoai_ts_libs.pointwise_bounded_ad.html",
    "import_from": "autoai_ts_libs.anomaly_detection.estimators.watfore.pointwise_bounded_ad",
    "type": "object",
    "tags": {"pre": [], "op": ["classifer", "regressor", "estimator"], "post": []},
    "properties": {
        "hyperparams": _hyperparams_schema,
        "input_fit": _input_fit_schema,
        "input_predict": _input_predict_schema,
        "output_predict": _output_predict_schema,
    },
}

PointwiseBoundedAnomalyDetector = lale.operators.make_operator(
    _PointwiseBoundedAnomalyDetectorImpl, _combined_schemas
)
lale.docstrings.set_docstrings(PointwiseBoundedAnomalyDetector)
