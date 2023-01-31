"""
Mixin base classes for sklearn native workflows (pipeline-like capabilities)
"""

# Standard
import os

# First Party
from watson_core import ModuleConfig
from watson_core.toolkit.errors import error_handler
from watson_core.workflows import WorkflowSaver
import alog

# Local
from ..base_mixins import SKLearnEstimatorBaseMixin, SKLearnPredictorBaseMixin
from ..config import lib_config
from .base import TSWorkflowBase

log = alog.use_channel("SKLWRAP Workflow")
error = error_handler.get(log)


class SKLearnWorkflowMixin(
    SKLearnEstimatorBaseMixin, SKLearnPredictorBaseMixin, TSWorkflowBase
):
    __doc__ = __doc__

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
        workflow_saver = WorkflowSaver(
            self,
            model_path=model_path,
            library_name=lib_config.library_name,
            library_version=lib_config.library_version,
        )
        with workflow_saver:

            # Create the artifact directory
            artifacts_rel_path, artifacts_abs_path = workflow_saver.add_dir(
                self._ARTIFACTS_DIR,
            )

            # Save the model within the artifacts path
            model_path = os.path.join(artifacts_abs_path, self._MODEL_FILE)
            self._save_artifacts(model_path)

            # Add the model path to the config
            workflow_saver.update_config(
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
            "<WTS42008785E>",
            model_bin_rel_path is not None,
            "Missing required '{}' key in model config",
            cls._MODEL_BIN_KEY,
        )

        # Load the pickled model
        model_bin_path = os.path.join(model_path, model_bin_rel_path)
        # Construct the class with the pre-loaded model
        return cls(**cls._load_artifacts(model_bin_path))
