"""
Implementation of a forecasting workflows for FCTK estimators.
"""

# First Party
from watson_core.toolkit.errors import error_handler
import alog

# Local
from ..sklearn_mixins import SKLearnWorkflowMixin
from .base import ForecasterWorkflowBase

log = alog.use_channel("FCTKFeaturePipelineFactoryBase")
error = error_handler.get(log)


class FeatureBasedForecastPipelineFactoryBase(
    ForecasterWorkflowBase, SKLearnWorkflowMixin
):
    """
    Implementation of a forecasting workflow task for the FCTK feature based forecast pipeline factory.
    """

    # these are defined in specific classes in fctk_pipeline_factory_task.py
    # _WRAPPED_CLASS = FCTKPipeline
    # _FACTORY_CLASS = WrappedFactory

    # _INTERNAL_TIMESERIES_TYPE = "spark"

    def __init__(self, *args, **kwargs):
        # Make sure that the _FACTORY_CLASS is in fact a type
        cls = self.__class__

        error.value_check(
            "<WTS85481491E>",
            isinstance(cls._FACTORY_CLASS, type),
            "Programming Error: cls._FACTORY_CLASS must be a type: [{}]",
            cls._FACTORY_CLASS,
        )

        # Check for model
        model = kwargs.get("model", None)
        if model is None:
            if hasattr(cls, "_INTERNAL_ESTIMATOR_CLASS"):
                kwargs.update(estimator_class=cls._INTERNAL_ESTIMATOR_CLASS)

            log.debug("Constructing with wrapper model arguments")
            pipeline_mode = kwargs.pop("pipeline_mode", "e2e")
            model, _ = cls._FACTORY_CLASS(*args, **kwargs).pipeline(name=pipeline_mode)
            kwargs.update({"model": model})
        else:
            if hasattr(cls, "_INTERNAL_ESTIMATOR_CLASS"):
                # check that the provided model is of the right type
                # Model is an FCTKPipeline where the last step should match the _INTERNAL_ESTIMATOR_CLASS
                error.value_check(
                    "<WTS21321473E>",
                    isinstance(model.steps[-1][1], cls._INTERNAL_ESTIMATOR_CLASS),
                    "Error: provided model argument contains an incorrect estimator: [{}]",
                    cls._INTERNAL_ESTIMATOR_CLASS,
                )

        # Call the parent
        super(SKLearnWorkflowMixin, self).__init__(*args, **kwargs)
