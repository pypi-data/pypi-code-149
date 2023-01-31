"""
This is a very simplistic implementation of a numeric timeseries forecaster
using the bats implementation from tspy. It is meant for demo purposes only!
"""

# Standard
from typing import Any, Dict, Optional, Tuple
import os

# First Party
from watson_core import ModuleConfig, block
from watson_core.blocks import BlockSaver
from watson_core.toolkit.errors import error_handler
import alog
import tspy

# Local
from ...config import lib_config
from ...toolkit import raw_timeseries_arg
from ...toolkit.timeseries_conversions import RawTimeseries, Timestamp
from ..base import MutableEstimatorBlockBase
from ..watson_core_mixins import WatsonCoreEstimatorMixin, WatsonCorePredictorMixin
from .base import ForecasterBase

log = alog.use_channel("FCBATS")
error = error_handler.get(log)


@block("75cd5699-1e87-4a3f-9c1d-b98bf9670b2d", "BATS Forecaster", "0.0.1")
class BatsForecaster(
    ForecasterBase,  # Block hierarchy
    MutableEstimatorBlockBase,  # Require partial_fit()
    WatsonCoreEstimatorMixin,  # Default implementation of fit()
    WatsonCorePredictorMixin,  # Default implementation of predict()
):
    __doc__ = __doc__

    _ARTIFACTS_DIR = "artifacts"
    _MODEL_FILE = "model.bin"
    _MODEL_BIN_KEY = "model_binary"
    _PARAMS_KEY = "params"

    def __init__(self, **kwargs):
        """Construct with passthrough arguments to the underlying model
        constructor, or a pre-constructed in-memory model.

        Kwargs:
            model:  tspy.data_structures.forecasting.ForecastingModel.ForecastingModel
                If given, the in-memory model will be used directly
        """
        self._model = kwargs.pop("model", None)
        if self._model is None:
            self._model = tspy.forecasters.bats(**kwargs)
        self._params = kwargs

    def get_params(self, **_) -> Dict[str, Any]:
        """Return the params used to construct this model"""
        return self._params

    def set_params(self, **_):
        """This block does not support updating params"""
        raise NotImplementedError(f"{self} does not support set_params")

    @classmethod
    def load(cls, model_path: str) -> "BatsForecaster":
        """Load a saved model from disk

        Args:
            model_path:  str
                The path on disk where the model lives

        Returns:
            forecaster:  BatsForecaster
                The loaded model
        """
        log.debug2("Loading model from %s", model_path)
        config = ModuleConfig.load(model_path)

        # Make sure the 'model_binary' key is present
        model_bin_rel_path = config.get(cls._MODEL_BIN_KEY)
        error.value_check(
            "<WTS18273452E>",
            model_bin_rel_path is not None,
            "Missing required '{}' key in model config",
            cls._MODEL_BIN_KEY,
        )

        # Make sure the 'params' key is present
        params = config.get(cls._PARAMS_KEY)
        error.value_check(
            "<WTS18273453E>",
            params is not None,
            "Missing required '{}' key in model config",
            cls._PARAMS_KEY,
        )
        error.type_check("<WTS18273454E>", dict, params=params)

        # Load the tspy model from the artifact path
        model_bin_path = os.path.join(model_path, model_bin_rel_path)
        model = tspy.forecasters.load(model_bin_path)

        # Construct the block class with the pre-loaded model
        return cls(model=model, **params)

    def save(self, model_path: str):
        """Save the model to disk

        Args:
            model_path:  str
                The path to save the model to on disk
        """
        # Make operating-system correct
        model_path = os.path.normpath(model_path)
        log.debug2("Saving model to %s", model_path)

        # Set up the block saver
        block_saver = BlockSaver(
            self,
            model_path=model_path,
            library_name=lib_config.library_name,
            library_version=lib_config.library_version,
        )
        with block_saver:

            # Create the artifact directory
            artifacts_rel_path, artifacts_abs_path = block_saver.add_dir(
                self._ARTIFACTS_DIR,
            )

            # Save the model within the artifacts path
            model_path = os.path.join(artifacts_abs_path, self._MODEL_FILE)
            self._model.save(model_path)

            # Add the model path to the config
            block_saver.update_config(
                {
                    self._MODEL_BIN_KEY: os.path.join(
                        artifacts_rel_path, self._MODEL_FILE
                    ),
                    self._PARAMS_KEY: self.get_params(),
                }
            )

    @classmethod
    @raw_timeseries_arg(arg_name="timeseries")
    def train(
        cls,
        timeseries: RawTimeseries,
        training_sample_size: int,
        **kwargs,
    ) -> "BatsForecaster":
        """Train with the provided sample size and any samples known at train
        time

        Args:
            timeseries:  RawTimeseries
                Samples available at initial training time
            training_sample_size:  int
                The number of samples needed for training

        Kwargs:
            **kwargs:  Dict[str, Any]
                Additional kwargs to pass to tspy.forecasters.bats

        Returns:
            forecaster:
                The instantiated forecaster, trained over the initial samples
        """
        error.type_check(
            "<WTS18273451E>", int, training_sample_size=training_sample_size
        )
        error.value_check(
            "<WTS95862769E>",
            training_sample_size > 1,
            "'training_sample_size' of {} not > 1",
            training_sample_size,
        )

        # Construct the class instance
        log.debug("Creating model with training size %d", training_sample_size)
        instance = cls(
            training_sample_size=training_sample_size,
            **kwargs,
        )

        # Initialize with the given samples
        return instance.partial_fit(timeseries)

    def fit(self, timeseries, *_, **__):
        """Perform a fresh fitting using the same arguments given to the initial
        constructor of this instance
        """
        return self.__class__.train(timeseries, **self.get_params())

    @raw_timeseries_arg(arg_name="timeseries")
    def partial_fit(self, timeseries: RawTimeseries, *_, **__):
        """Update the state of the model with the given timeseries observations

        Args:
            timeseries:  Timeseries
                The series of observations to update the model with
        """
        for timepoint, value in timeseries:
            log.debug3("Updating with (%s, %s)", timepoint, value)
            self._model.update_model(timepoint, value)
        return self

    @raw_timeseries_arg(arg_name="timeseries")
    def run(self, timeseries: RawTimeseries, *_, lazy: bool = True) -> RawTimeseries:
        """Forecast the value of the series at the given point in time

        Args:
            timeseries:  RawTimeseries
                The series of observations at which to predict

        Kwargs:
            lazy:  bool
                If true, predictions will be made lazily as the returned series
                is iterated, otherwise they will be proactively computed

        Returns:
            forecasted_timeseries:  RawTimeseries
                The timeseries mirroring the input series with predicted values
                added. If the values of the input timeseries are None, they will
                be filled in and replaced, otherwise the predicted values will
                be added as additional multivariat values to the output.
        """
        res = (self._run_single(ts, val) for ts, val in timeseries)
        if not lazy:
            res = list(res)
        return res

    def _run_single(self, timepoint: Timestamp, value: Any) -> Tuple[Timestamp, Any]:
        """Run a single forecasting call at the given timepoint."""
        forecast_val = self._model.forecast_at(timepoint)
        log.debug3("Forecast value at %s: %s", timepoint, forecast_val)
        if value is None:
            return timepoint, forecast_val
        elif isinstance(value, tuple):
            return timepoint, tuple([*value, forecast_val])
        else:
            return timepoint, (value, forecast_val)
