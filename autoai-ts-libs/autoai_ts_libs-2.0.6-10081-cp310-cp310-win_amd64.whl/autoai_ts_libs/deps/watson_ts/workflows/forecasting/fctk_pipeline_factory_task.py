"""
Implementation of a forecasting workflows for FCTK estimators.
"""

# First Party
from fctk.pipeline import FCTKPipeline
from fctk.pipelinefactory.feature_pipeline_factory import (
    FeatureBasedForecastPipelineFactory as WrappedFactory,
)
from watson_core import workflow

# Local
from .fctk_factories_base import FeatureBasedForecastPipelineFactoryBase
from autoai_ts_libs.deps.watson_ts.blocks.forecasting.fctk_deepar_estimator import DeepAREstimator
from autoai_ts_libs.deps.watson_ts.blocks.forecasting.fctk_l2f import NormedL2F
from autoai_ts_libs.deps.watson_ts.blocks.forecasting.fctk_lightgbm_ray import RayDistributedLightGBM
from autoai_ts_libs.deps.watson_ts.blocks.forecasting.fctk_random_forest import RandomForestRegressor


@workflow("ae5f4e29-be1a-4e4c-b90d-bac0780962fe", "Feature Based Pipeline", "0.0.1")
class FeatureBasedForecastPipelineFactory(FeatureBasedForecastPipelineFactoryBase):
    """
    Implementation of a forecasting workflow task for the FCTK feature based forecast pipeline factory.
    """

    _WRAPPED_CLASS = FCTKPipeline
    _FACTORY_CLASS = WrappedFactory

    _INTERNAL_TIMESERIES_TYPE = "spark"


@workflow(
    "84d8b14b-741f-4856-8bf7-048398282c69", "NormedL2F Feature Based Pipeline", "0.0.1"
)
class NormedL2FFeatureBasedForecastPipeline(FeatureBasedForecastPipelineFactoryBase):
    """
    Implementation of feature based forecast pipeline factory for Normed L2F.
    """

    _WRAPPED_CLASS = FCTKPipeline
    _FACTORY_CLASS = WrappedFactory

    _INTERNAL_TIMESERIES_TYPE = "spark"
    _INTERNAL_ESTIMATOR_CLASS = NormedL2F


@workflow(
    "4ff210c5-491c-4d50-bd79-00254267c079", "LightGBM Feature Based Pipeline", "0.0.1"
)
class LightGBMFeatureBasedForecastPipeline(FeatureBasedForecastPipelineFactoryBase):
    """
    Implementation of feature based forecast pipeline factory for LightGBM.
    """

    _WRAPPED_CLASS = FCTKPipeline
    _FACTORY_CLASS = WrappedFactory

    _INTERNAL_TIMESERIES_TYPE = "spark"
    _INTERNAL_ESTIMATOR_CLASS = RayDistributedLightGBM


@workflow(
    "a868c266-8cd9-42d2-bb55-d9ce9cbc77a6", "Random Feature Based Pipeline", "0.0.1"
)
class RandomForestFeatureBasedForecastPipeline(FeatureBasedForecastPipelineFactoryBase):
    """
    Implementation of feature based forecast pipeline factory for Random Forest.
    """

    _WRAPPED_CLASS = FCTKPipeline
    _FACTORY_CLASS = WrappedFactory

    _INTERNAL_TIMESERIES_TYPE = "spark"
    _INTERNAL_ESTIMATOR_CLASS = RandomForestRegressor


@workflow(
    "0d533277-1b32-4a89-b704-7c6f53d2d627", "DeepAR Feature Based Pipeline", "0.0.1"
)
class DeepARFeatureBasedForecastPipeline(FeatureBasedForecastPipelineFactoryBase):
    """
    Implementation of feature based forecast pipeline factory for DeepAR.
    """

    _WRAPPED_CLASS = FCTKPipeline
    _FACTORY_CLASS = WrappedFactory

    _INTERNAL_TIMESERIES_TYPE = "spark"
    _INTERNAL_ESTIMATOR_CLASS = DeepAREstimator
