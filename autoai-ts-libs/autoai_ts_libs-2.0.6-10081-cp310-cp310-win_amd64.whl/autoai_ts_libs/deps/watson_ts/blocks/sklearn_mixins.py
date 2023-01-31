"""
Mixin base classes for sklearn native estimators.
"""

# Standard
import os

# First Party
# First party
from watson_core import ModuleConfig
from watson_core.blocks import BlockSaver
from watson_core.toolkit.errors import error_handler
import alog

# Local
from ..base_mixins import (
    SKLearnEstimatorBaseMixin,
    SKLearnPredictorBaseMixin,
    SKLearnTransformerBaseMixin,
)
from ..config import lib_config
from .base import EstimatorBlockBase, PredictorBlockBase, TransformerBlockBase

log = alog.use_channel("SKLWRAPBLOCK")
error = error_handler.get(log)


class SKLearnEstimatorBlockWrapper:
    """Base wrapper class that provides mechanism to save blocks"""

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
            self._save_artifacts(model_path)

            # Add the model path to the config
            block_saver.update_config(
                {
                    self._MODEL_BIN_KEY: os.path.join(
                        artifacts_rel_path, self._MODEL_FILE
                    ),
                }
            )

    @classmethod
    def load(cls, model_path: str) -> "SKLearnEstimatorBlockWrapper":
        """Load a saved model from disk

        Args:
            model_path:  str
                The path on disk where the model lives

        Returns:
            block:  SKLearnEstimatorBlockWrapper
                The loaded model
        """
        log.debug2("Loading model from %s", model_path)
        config = ModuleConfig.load(model_path)

        # Make sure the 'model_binary' key is present
        model_bin_rel_path = config.get(cls._MODEL_BIN_KEY)
        error.value_check(
            "<WTS60736558E>",
            model_bin_rel_path is not None,
            "Missing required '{}' key in model config",
            cls._MODEL_BIN_KEY,
        )

        # Load the pickled model
        model_bin_path = os.path.join(model_path, model_bin_rel_path)
        # Construct the class with the pre-loaded model
        return cls(**cls._load_artifacts(model_bin_path))


class SKLearnEstimatorMixin(
    SKLearnEstimatorBaseMixin, SKLearnEstimatorBlockWrapper, EstimatorBlockBase
):
    """This mixin base class provides a default implementation of train and fit
    for mixin wrapper classes for blocks
    """


class SKLearnPredictorMixin(
    SKLearnPredictorBaseMixin, SKLearnEstimatorBlockWrapper, PredictorBlockBase
):
    """This mixin base class provides a default implementation of run and
    predict for mixin wrapper classes for blocks
    """


class SKLearnTransformerMixin(
    SKLearnTransformerBaseMixin, SKLearnEstimatorBlockWrapper, TransformerBlockBase
):
    """This mixin base class provides a default implementation of run and
    transform for mixin wrapper classes for blocks
    """
