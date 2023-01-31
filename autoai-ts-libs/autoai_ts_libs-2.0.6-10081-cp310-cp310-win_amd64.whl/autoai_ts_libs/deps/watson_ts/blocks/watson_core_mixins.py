"""
Mixin base classes for watson_core native blocks
"""

# Standard
from typing import Any, Dict, Iterable
import abc
import os

# First Party
from watson_core import ModuleConfig
from watson_core.blocks import BlockSaver
from watson_core.toolkit.errors import error_handler
import alog

# Local
from ..config import lib_config
from ..toolkit import raw_timeseries_arg
from ..toolkit.timeseries_conversions import RawTimeseries, TimeseriesType
from .base import EstimatorBlockBase, PredictorBlockBase, TransformerBlockBase

## Watson Core Shared Base Implementations #####################################
#
# These Mixin base classes implement common wrapping paradigms in order to
# enable easy defaults for blocks implemented using either the standard Watson
# Core block interface (load/save/train/run) or some combination of the standard
# sklearn interfaces.
##

log = alog.use_channel("WatsonCore Mixin")
error = error_handler.get(log)


class WatsonCoreBlockWrapper:
    """
    Wrapper than implements Save/Load generic code for all watson core mixins as well as provides abstract methods for
    saving and loading the given model that is extending this class
    """

    @abc.abstractmethod
    def _save_artifacts(self, path):
        """
        Blocks implementation of save artifacts to path
        """

    @classmethod
    def _load_artifacts(cls, path: str) -> Dict:
        """
        Blocks implementation of load artifacts from path
        """

    def save(self, path: str):
        """Save model to disk

        Args:
            path:  str
                The path to save to disk
        """
        # Make operating-system correct
        path = os.path.normpath(path)
        log.debug2("Saving model to %s", path)

        # Set up the block saver
        block_saver = BlockSaver(
            self,
            model_path=path,
            library_name=lib_config.library_name,
            library_version=lib_config.library_version,
        )
        with block_saver:
            # Create the artifact directory
            artifacts_rel_path, artifacts_abs_path = block_saver.add_dir(
                self._ARTIFACTS_DIR,
            )

            # Save the model within the artifacts path
            path = os.path.join(artifacts_abs_path, self._MODEL_FILE)
            self._save_artifacts(path)

            # Add the model path to the config
            block_saver.update_config(
                {
                    self._MODEL_BIN_KEY: os.path.join(
                        artifacts_rel_path, self._MODEL_FILE
                    ),
                }
            )

    @classmethod
    def load(cls, path: str) -> "WatsonCoreBlockWrapper":
        """Load a model from disk

        Args:
            path:  str
                The path on disk where the model lives

        Returns:
            block:  WatsonCoreBlockWrapper
                The loaded model
        """
        log.debug2("Loading model from %s", path)
        config = ModuleConfig.load(path)

        # Make sure the 'model_binary' key is present
        model_bin_rel_path = config.get(cls._MODEL_BIN_KEY)
        error.value_check(
            "<WTS42008785F>",
            model_bin_rel_path is not None,
            "Missing required '{}' key in model config",
            cls._MODEL_BIN_KEY,
        )

        # Load the pickled model
        model_bin_path = os.path.join(path, model_bin_rel_path)
        # Construct the class with the pre-loaded transformer
        result = cls._load_artifacts(model_bin_path)
        return cls(**result)


class WatsonCoreEstimatorMixin(WatsonCoreBlockWrapper, EstimatorBlockBase):
    """This mixin base class provides a default implementation of the sklearn
    Estimator interface's fit() method. This implementation relies on the
    assumption that the BlockBase train method has been implemented.
    """

    def fit(
        self,
        timeseries: TimeseriesType,
        *_,
        **kwargs,
    ) -> "WatsonCoreEstimatorMixin":
        """Update the model to fit the given timeseries. This aligns with the
        corresponding sklearn method

        CITE: https://scikit-learn.org/stable/developers/develop.html#fitting

        The default implementation is an alias to the class method train. This
        is tricky because it mixes the paradigms of sklearn where the class is
        constructed with data-independent params, then trained and the block
        paradigm where training is a static method that produces an in-memory
        instance of the model. To accomplish this, we train a fresh instance,
        then update the state of _this_ instance to the state of the new
        instance.

        Args:
            timeseries:  TimeseriesType
                The timeseries to train over. Individual methods may choose to
                convert this to an implementation-desired type using the
                argument conversion framework.
            **kwargs
                Arbitrary additional parameters that should be passed through to
                inform how the fitting proceeds

        Returns:
            estimator:  WatsonCoreEstimatorMixin
                The estimator itself. This matches the sklearn API.
        """
        new_kwargs = dict(self.get_params())
        new_kwargs.update(kwargs)
        new_instance = self.__class__.train(timeseries, **new_kwargs)
        self.__dict__.update(new_instance.__dict__)
        return self


class WatsonCorePredictorMixin(WatsonCoreBlockWrapper, PredictorBlockBase):
    """This mixin base class provides a default implementation of the sklearn
    Predictor interface's predict() method. This implementation relies on the
    assumption that the BlockBase run method has been implemented.
    """

    @raw_timeseries_arg(arg_name="timeseries")
    def predict(
        self,
        timeseries: RawTimeseries,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> RawTimeseries:
        """Run a prediction against the given timepoints and produce an output
        multi-variate timeseries with the input value and the prediction at each
        point in time.

        Args:
            timeseries:  RawTimeseries
                The timeseries used for the predictions
            *args:  Iterable[Any]
                Additional positional args to pass through to run

        Kwargs:
            **kwargs:  Dict[str, Any]
                Additional arguments to pass through to run

        Returns:
            prediction_timeseries:  Timeseries
                An updated timeseries with values produced via run added as an
                additional value column
        """
        return self.run(timeseries, *args, **kwargs)


class WatsonCoreTransformerMixin(WatsonCoreBlockWrapper, TransformerBlockBase):
    """This mixin base class provides a default implementation of the sklearn
    Transformer interface's transform() method. This implementation relies on
    the assumption that the BlockBase run method has been implemented.
    """

    def transform(
        self, timeseries: RawTimeseries, *args: Iterable[Any], **kwargs: Dict[str, Any]
    ) -> RawTimeseries:
        """Perform run against the given sequence of observations and produce an
        output timeseries with the value updated for each timepoint.

        Args:
            timeseries:  RawTimeseries
                The timeseries used for the predictions
            *args:  Iterable[Any]
                Additional positional args to pass through to run

        Kwargs:
            **kwargs:  Dict[str, Any]
                Additional arguments to pass through to run

        Returns:
            prediction_timeseries:  Timeseries
                An updated timeseries with values produced via run added as an
                additional value column
        """
        return self.run(timeseries, *args, **kwargs)
