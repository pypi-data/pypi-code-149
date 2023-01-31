"""
Mixin to simplify wrapping spark estimators.
"""

# Standard
from typing import Any, Dict, Union
import os

# First Party
from watson_core.toolkit.errors import error_handler
import alog

# Local
from .sklearn_mixins import (
    SKLearnEstimatorMixin,
    SKLearnPredictorMixin,
    SKLearnTransformerMixin,
)
from autoai_ts_libs.deps.watson_ts.toolkit.timeseries_conversions import TimeseriesType

log = alog.use_channel("SparkTransformerMixin")
error = error_handler.get(log)


class SparkEstimatorModelMixin(SKLearnEstimatorMixin, SKLearnTransformerMixin):
    """Mixin which provides appropriate conversion functionality for spark estimator-model pairs. Wraps
    both the estimator (derived from pyspark.ml.Estimator) and model (pyspark.ml.Model) objects to provide
    consistent functionality."""

    def __init__(self, *args, **kwargs):
        # Make sure that the _WRAPPED_CLASS is in fact a type
        cls = self.__class__

        error.value_check(
            "<WTS85604519E>",
            isinstance(cls._WRAPPED_PYSPARK_MODEL_CLASS, type),
            "Programming Error: cls._WRAPPED_PYSPARK_MODEL_CLASS must be a type: [{}]",
            cls._WRAPPED_PYSPARK_MODEL_CLASS,
        )

        # Check model and trmodel
        model = kwargs.get("model")
        trmodel = kwargs.pop("_trmodel", None)
        # either both of trmodel, model must be specified, or neither specified
        error.value_check(
            "<WTS02746657E>",
            (trmodel is not None and model is not None)
            or (trmodel is None and model is None),
            "Cannot initialize with prebuilt model unless both model and _trmodel are specified",
        )
        self._trmodel = trmodel

        # Call the parent
        super(SKLearnEstimatorMixin, self).__init__(*args, **kwargs)

    def fit(
        self, timeseries: TimeseriesType, *args, **kwargs
    ) -> "SparkEstimatorModelMixin":
        """Delegate fitting to the wrapped model"""
        with self._convert_to_internal_timeseries_type(timeseries, **kwargs) as (
            timeseries,
            kwargs,
        ):
            self._trmodel = self._wrapped_model.fit(timeseries, *args, **kwargs)
        return self

    def transform(
        self, timeseries: TimeseriesType, *_, **kwargs: Dict[str, Any]
    ) -> TimeseriesType:
        with self._convert_to_internal_timeseries_type(timeseries, **kwargs) as (
            timeseries,
            kwargs,
        ):
            return self._trmodel.transform(dataset=timeseries, **kwargs)

    def _save_artifacts(self, model_path: str):
        tr_path = os.path.join(model_path, "estimator")
        md_path = os.path.join(model_path, "model")
        self._wrapped_model.save_model(tr_path)
        self._trmodel.save_model(md_path)

    @classmethod
    def _load_artifacts(cls, model_path: str):
        md_path = os.path.join(model_path, "model")
        trmodel = cls._WRAPPED_PYSPARK_MODEL_CLASS.load_model(md_path)

        tr_path = os.path.join(model_path, "estimator")
        model = cls._WRAPPED_CLASS.load_model(tr_path)

        return {"model": model, "_trmodel": trmodel}


class SparkTransformerMixin(SKLearnTransformerMixin):
    """Mixin which provides appropriate conversion functionality for spark transformers
    (spark objects inheriting from pyspark.ml.Transformer)."""
