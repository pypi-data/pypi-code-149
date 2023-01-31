"""
Mixin base classes for sklearn native estimators, pipelines, etc.
"""

# Standard
from contextlib import contextmanager
from typing import Any, Dict
import copy
import inspect
import os
import pickle

# First Party
from watson_core import ModuleConfig
from watson_core.toolkit.errors import error_handler
import alog

# Local
from .base import EstimatorBase, PredictorBase, TransformerBase
from .toolkit.timeseries_conversions import (
    HAVE_PANDAS,
    HAVE_PYSPARK,
    TIMESTAMP_SOURCE_ARG,
    TIMESTAMP_TARGET_NAME_ARG,
    VALUE_SOURCE_ARG,
    VALUE_TARGET_NAME_ARG,
    TimeseriesType,
    to_ndarray,
    to_spark_df,
)

log = alog.use_channel("SKLWRAP")
error = error_handler.get(log)


class SKLearnEstimatorWrapper:
    """This base class provides common construction semantics for all modules
    that wrap an sklearn estimator. It should not be used directly since it is
    used by the below mixins.
    """

    _ARTIFACTS_DIR = "artifacts"
    _MODEL_FILE = "model.pkl"
    _MODEL_BIN_KEY = "model_binary"

    # By default, the internal timeseries type is np.ndarray, but other types
    # may be specified. The following types are supported:
    #
    # - "numpy" -> "np.ndarray"
    # - "spark" -> "pyspark.sql.DataFrame"
    # - "pandas" -> "pd.DataFrame" [TODO]
    #
    # NOTE: We use the string enums here rather than the concrete types to avoid
    #   requiring these types to be available here in the base class
    #   functionality.
    _INTERNAL_TIMESERIES_TYPE = "numpy"

    # TODO: Make this abstract!
    _WRAPPED_CLASS = None

    # Optional class properties that can be set to influence how columns are
    # found. When the wrapped model has member attributes that indicate where to
    # find the timeseries and value data, these should be set in order to take
    # advantage of runtime column selection in the conversion functions.

    # Set this if the wrapped model needs to find a single timeseries column
    # using a member attribute.
    _TS_COL_PARAM = None

    # Set this if the wrapped model needs to find one or more value columns
    # using a member attribute
    _VAL_COLS_PARAM = None

    ## Construction ############################################################

    def __init__(self, *args, **kwargs):
        """Construct the underlying model unless the model is given directly"""

        # Make sure that the _WRAPPED_CLASS is in fact a type
        cls = self.__class__
        error.value_check(
            "<WTS59233452E>",
            isinstance(cls._WRAPPED_CLASS, type),
            "Programming Error: cls._WRAPPED_CLASS must be a type: [{}]",
            cls._WRAPPED_CLASS,
        )

        # Make sure the class has a valid internal timeseries type
        error.value_check(
            "<WTS59233451E>",
            cls._INTERNAL_TIMESERIES_TYPE in ["numpy", "pandas", "spark"],
            "Programming Error: Invalid internal timeseries type ['{}']",
            cls._INTERNAL_TIMESERIES_TYPE,
        )

        # Set up the internal model either from a prebuilt model or by
        # delegating the init args to the wrapped class
        model = kwargs.pop("model", None)
        cls = self.__class__
        if model is not None:
            log.debug("Constructing with pre-constructed wrapped model")
            self._wrapped_model = model
        else:
            log.debug("Constructing with wrapper model arguments")
            self._wrapped_model = cls._WRAPPED_CLASS(*args, **kwargs)
        self._has_col_params = any(
            [col is not None for col in [cls._TS_COL_PARAM, cls._VAL_COLS_PARAM]]
        )

    def get_params(self, *args, **kwargs) -> Dict[str, Any]:
        """Delegate get_params to the wrapped model"""
        return self._wrapped_model.get_params(*args, **kwargs)

    def set_params(self, *args, **kwargs):
        """Delegate set_params to the wrapped model"""
        return self._wrapped_model.set_params(*args, **kwargs)

    def _save_artifacts(self, model_path: str):
        """Supporting method to save artifacts

        Args:
            model_path:  str
                The path on disk where the model will live
        Notes:
            If wrapped object supports a "save_model" method, it will be called.
            Otherwise pickle is used.
        """

        if self._wrapped_model and hasattr(self._wrapped_model, "save_model"):
            self._wrapped_model.save_model(model_path)
        else:
            with open(model_path, "wb") as handle:
                pickle.dump(self._wrapped_model, handle)

    @classmethod
    def _load_artifacts(cls, model_path: str) -> Dict:
        """Supporting method to load artifacts

        Args:
            model_path:  str
                The path on disk where the model lives

        Notes:
            If wrapped object supports a "load_model" method, it will be called.
            Otherwise pickle is used.

        Returns:
            artifacts:  Dict
                The loaded artifacts as a dictionary. This will be passed to the init
                method of the class, thus keys should be valid arrguments of the init method.
                By default, the "model" key is populated with the loaded model.
        """
        if cls._WRAPPED_CLASS and hasattr(cls._WRAPPED_CLASS, "load_model"):
            model = cls._WRAPPED_CLASS.load_model(model_path)
        else:
            with open(model_path, "rb") as handle:
                model = pickle.load(handle)
        return {"model": model}

    @contextmanager
    def _convert_to_internal_timeseries_type(
        self,
        timeseries: TimeseriesType,
        **kwargs,
    ) -> TimeseriesType:
        """Shared conversion wrapper for arbitrary input timeseries types. This
        wrapper will, if configured to do so, update the local params to point
        to the post-conversion columns, then return them after the context
        exits.

        WARNING: This is NOT thread safe! If multiple threads enter contexts
            concurrently with different values, they may conflict with each
            other badly! In a multi-threaded environment, conversion args that
            are managed as instance params should not be used.
        """

        # Shallow copy the kwargs so that mutating ops don't accidentally
        # mutate a shared kwargs dict
        kwargs = copy.copy(kwargs)

        # Get values for the column source params from the kwargs
        kwarg_ts_col_val = kwargs.pop(TIMESTAMP_SOURCE_ARG, None)
        kwarg_val_cols_val = kwargs.pop(VALUE_SOURCE_ARG, None)

        # Convert to the desired internal type
        #
        # NOTE: The cls._INTERNAL_TIMESERIES_TYPE is checked at __init__ time so
        #   we don't check it here. This _could_ lead to errors if a user
        #   changes it after construction, but that would be an intentional
        #   misuse of private class data and is not worth guarding against.
        cls = self.__class__
        if cls._INTERNAL_TIMESERIES_TYPE == "numpy":
            # Third Party
            import numpy as np

            if not isinstance(timeseries, np.ndarray):
                log.debug2("Converting from %s to np.ndarray", type(timeseries))
                convert_kwargs = {
                    "ignore_unused_col_args": self._has_col_params,
                    TIMESTAMP_SOURCE_ARG: kwarg_ts_col_val,
                    VALUE_SOURCE_ARG: kwarg_val_cols_val,
                }
                timeseries = to_ndarray(timeseries, **convert_kwargs)

                # If conversion kwargs present, update them to match the converted
                # array. Converted arrays will have the timestamp column at index 0
                # and the series of value columns starting at index 1.
                if kwarg_ts_col_val is not None:
                    kwarg_ts_col_val = 0
                if kwarg_val_cols_val is not None:
                    if isinstance(kwarg_val_cols_val, (list, tuple)):
                        new_val = list(range(1, len(kwarg_val_cols_val) + 1))
                    else:
                        new_val = 1
                    kwarg_val_cols_val = new_val

        elif cls._INTERNAL_TIMESERIES_TYPE == "pandas":
            assert HAVE_PANDAS, f"Cannot use {cls} without pandas installed"
            raise NotImplementedError("TODO!")

        elif cls._INTERNAL_TIMESERIES_TYPE == "spark":
            assert HAVE_PYSPARK, f"Cannot use {cls} without pyspark installed"
            # Third Party
            import pyspark

            if not isinstance(timeseries, pyspark.sql.DataFrame):
                log.debug2(
                    "Converting from %s to pyspark.sql.DataFrame", type(timeseries)
                )

                # when converting we need to be more aware of input type
                # if raw or tspy then we know ts/val columns already --> new spark df should use values from object's instance variables
                # if numpy we need additional args here
                # if pandas we should check for args here, but fall back to values from object's instance variables
                convert_kwargs = {
                    "ignore_unused_col_args": self._has_col_params,
                    TIMESTAMP_SOURCE_ARG: kwarg_ts_col_val,
                    VALUE_SOURCE_ARG: kwarg_val_cols_val,
                    TIMESTAMP_TARGET_NAME_ARG: kwargs.pop(
                        TIMESTAMP_TARGET_NAME_ARG, None
                    ),
                    VALUE_TARGET_NAME_ARG: kwargs.pop(VALUE_TARGET_NAME_ARG, None),
                }
                log.debug3("Convert Kwargs: %s", convert_kwargs)
                timeseries = to_spark_df(timeseries, **convert_kwargs)

                # Extract the names of the timestamp and value target columns
                ts_targ = getattr(timeseries, TIMESTAMP_TARGET_NAME_ARG, None)
                val_targ = getattr(timeseries, VALUE_TARGET_NAME_ARG, None)
                assert (
                    ts_targ is not None
                ), f"Programming Error: {TIMESTAMP_TARGET_NAME_ARG} not attached to converted data frame"
                assert (
                    val_targ is not None
                ), f"Programming Error: {VALUE_TARGET_NAME_ARG} not attached to converted data frame"

                # Update the column args to point to the new target columns
                kwarg_ts_col_val = ts_targ
                kwarg_val_cols_val = val_targ

        # If the wrapped model has column params, grab the current values and
        # update them to point at the given kwargs
        current_params = self.get_params()
        current_ts_col_val = current_params.get(cls._TS_COL_PARAM)
        current_val_cols_val = current_params.get(cls._VAL_COLS_PARAM)
        updated_params = {}
        if None not in [cls._TS_COL_PARAM, kwarg_ts_col_val]:
            updated_params[cls._TS_COL_PARAM] = kwarg_ts_col_val
        if None not in [cls._VAL_COLS_PARAM, kwarg_val_cols_val]:
            updated_params[cls._VAL_COLS_PARAM] = kwarg_val_cols_val

        # If there are member params to update, make the update
        if updated_params:
            log.debug3("Updating internal params: %s", updated_params)
            self.set_params(**updated_params)

        # Yield to the converted timeseries to the wrapped context
        yield timeseries, kwargs

        # Reset to the previous values
        reset_params = {}
        if current_ts_col_val is not None:
            reset_params[cls._TS_COL_PARAM] = current_ts_col_val
        if current_val_cols_val is not None:
            reset_params[cls._VAL_COLS_PARAM] = current_val_cols_val
        if reset_params:
            self.set_params(**reset_params)


class SKLearnEstimatorBaseMixin(SKLearnEstimatorWrapper, EstimatorBase):
    """This mixin base class provides a default implementation of train and fit
    for mixin wrapper classes
    """

    @classmethod
    def train(cls, timeseries: TimeseriesType, **kwargs) -> "SKLearnEstimatorMixin":
        """Perform static training using the fit method"""

        # Determine the names of the kwargs for the wrapped class's __init__
        init_kwargs_names = list(
            inspect.signature(cls._WRAPPED_CLASS.__init__).parameters.keys()
        )

        # Split the kwargs into those that match the keyword args for __init__
        # and fit
        init_kwargs = {
            key: val for key, val in kwargs.items() if key in init_kwargs_names
        }
        fit_kwargs = {
            key: val for key, val in kwargs.items() if key not in init_kwargs_names
        }

        # If there are init kwargs that are needed for conversion, also pass
        # them to the fit call
        ts_col_kwarg_val = kwargs.get(TIMESTAMP_SOURCE_ARG)
        if ts_col_kwarg_val is not None:
            fit_kwargs[TIMESTAMP_SOURCE_ARG] = ts_col_kwarg_val
        val_cols_kwarg_val = kwargs.get(VALUE_SOURCE_ARG)
        if val_cols_kwarg_val is not None:
            fit_kwargs[VALUE_SOURCE_ARG] = val_cols_kwarg_val

        # Log the final kwargs to init and fit
        log.debug3("Init Kwargs: %s", init_kwargs)
        log.debug3("Fit Kwargs: %s", fit_kwargs)

        # Initialize with the init kwargs passed through
        log.debug("Constructing instance of %s", cls.__name__)
        instance = cls(**init_kwargs)

        # Run fit on the data with the available keywords
        log.debug("Fitting %s", cls.__name__)
        return instance.fit(timeseries, **fit_kwargs)

    def fit(
        self, timeseries: TimeseriesType, *args, **kwargs
    ) -> "SKLearnEstimatorMixin":
        """Delegate fitting to the wrapped model"""
        with self._convert_to_internal_timeseries_type(timeseries, **kwargs) as (
            timeseries,
            kwargs,
        ):
            self._wrapped_model = self._wrapped_model.fit(timeseries, *args, **kwargs)
        return self


class SKLearnPredictorBaseMixin(SKLearnEstimatorWrapper, PredictorBase):
    """This mixin base class provides a default implementation of run and
    predict for mixin wrapper classes
    """

    def run(self, *args, **kwargs) -> TimeseriesType:
        """Create a single-row array and delegate to predict"""
        return self.predict(*args, **kwargs)

    def predict(self, timeseries: TimeseriesType, *args, **kwargs) -> TimeseriesType:
        """Delegate predict to the wrapped model"""
        with self._convert_to_internal_timeseries_type(timeseries, **kwargs) as (
            timeseries,
            kwargs,
        ):
            return self._wrapped_model.predict(timeseries, *args, **kwargs)


class SKLearnTransformerBaseMixin(SKLearnEstimatorWrapper, TransformerBase):
    """This mixin base class provides a default implementation of run and
    transform for mixin wrapper classes
    """

    def run(self, *args, **kwargs) -> TimeseriesType:
        """Create a single-row array and delegate to transform"""
        return self.transform(*args, **kwargs)

    def transform(self, timeseries: TimeseriesType, *args, **kwargs) -> TimeseriesType:
        """Delegate transform to the wrapped model"""
        with self._convert_to_internal_timeseries_type(timeseries, **kwargs) as (
            timeseries,
            kwargs,
        ):
            return self._wrapped_model.transform(timeseries, *args, **kwargs)
