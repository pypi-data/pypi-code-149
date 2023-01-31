# Standard
from typing import Any, Dict, Union
import os

# First Party
from fctk.transformers.imputation import (
    FillMissingValueTransformer as WrappedFillMissingValueTransformer,
)
from fctk.transformers.imputation import MissingDatesFiller as WrappedMissingDatesFiller
from fctk.transformers.imputation import TSImputer as WrappedTSImputer
from fctk.transformers.preprocessing import TSStandardScaler as WrappedTSStandardScaler
from fctk.transformers.preprocessing import TSStandardScalerModel
from fctk.transformers.seasonal import (
    SeasonalContextGenerator as WrappedSeasonalContextGenerator,
)
from fctk.transformers.segmentation import (
    PeriodSummaryFeatureTransformer as WrappedPeriodSummaryFeatureTransformer,
)
from fctk.transformers.segmentation import (
    SegmentingWithTargetListFormTransformer as WrappedSegmentingWithTargetListFormTransformer,
)
from fctk.transformers.timeseries.differencing import ForwardDifferencingBucketizerModel
from fctk.transformers.timeseries.differencing import (
    ForwardDifferencingBucketizerTransformer as WrappedEstimator,
)
from fctk.transformers.utils.columnops import ColumnSelector as WrappedColumnSelector
from fctk.transformers.utils.dropping import NullDropper as WrappedNullDropper
from watson_core import block

# Local
from ..spark_mixins import SparkEstimatorModelMixin, SparkTransformerMixin


@block(
    "fffaa94e-8b1b-4dc9-b75a-3566fabeb1b2",
    "SegmentingWithTargetListFormTransformer",
    "0.0.1",
)
class SegmentingWithTargetListFormTransformer(SparkTransformerMixin):

    """Create windows of features and targets from a timeseries."""

    _WRAPPED_CLASS = WrappedSegmentingWithTargetListFormTransformer
    _INTERNAL_TIMESERIES_TYPE = "spark"


@block("f8230021-3e73-4ad0-a4e7-f257f6939674'", "TSScaler", "0.0.1")
class TSStandardScaler(SparkEstimatorModelMixin):

    """An spark-dataframe-compatible timeseries standard scaler."""

    _WRAPPED_CLASS = WrappedTSStandardScaler
    _WRAPPED_PYSPARK_MODEL_CLASS = TSStandardScalerModel
    # _TS_COL_PARAM = "time_column"  # TS is not passed to L2F model
    # _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns


@block(
    "59334c35-29d2-47ce-976f-c2cf7b08d0a6",
    "Period Summary Feature Transformer",
    "0.0.1",
)
class PeriodSummaryFeatureTransformer(SparkTransformerMixin):

    """Period Summary Feature Transformer"""

    _WRAPPED_CLASS = WrappedPeriodSummaryFeatureTransformer
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns


@block(
    "f8230021-3e73-4ad0-a4e7-f257f6939632",
    "Forward Differencing Bucketizer",
    "0.0.1",
)
class ForwardDifferencingBucketizerTransformer(SparkEstimatorModelMixin):

    """An spark-dataframe-compatible time series differencing bucketizer."""

    _WRAPPED_CLASS = WrappedEstimator
    _WRAPPED_PYSPARK_MODEL_CLASS = ForwardDifferencingBucketizerModel
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns


@block(
    "6eb5534f-a3a4-4e6e-9dda-7787421caac2",
    "Fill Missing Value Transformer",
    "0.0.1",
)
class FillMissingValueTransformer(SparkTransformerMixin):

    """Fill Missing Value Transformer"""

    _WRAPPED_CLASS = WrappedFillMissingValueTransformer
    # _TS_COL_PARAM = "time_column"
    _VAL_COLS_PARAM = "inputCol"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns


@block(
    "85f52a11-ce31-4ea2-8873-74cfaf540a81",
    "Missing Dates Filter Transformer",
    "0.0.1",
)
class MissingDatesFiller(SparkTransformerMixin):

    """Missing Dates Filter Transformer"""

    _WRAPPED_CLASS = WrappedMissingDatesFiller
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns


@block(
    "15e6e930-a3ef-473d-bc49-ff44e7d70429",
    "TS Imputer Transformer",
    "0.0.1",
)
class TSImputer(SparkTransformerMixin):

    """TS Imputer Transformer"""

    _WRAPPED_CLASS = WrappedTSImputer
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns


@block(
    "7f78418e-0ed0-47d6-b8a1-d4869ae43cde",
    "Simple transformer which selects one or more columns.",
    "0.0.1",
)
class ColumnSelector(SparkTransformerMixin):

    """Simple transformer which selects one or more columns."""

    _WRAPPED_CLASS = WrappedColumnSelector
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns


@block(
    "1d6388d8-cbdd-4ffe-9aa6-f3717579dd5d",
    "Simple transformer which drops any rows with null/None values",
    "0.0.1",
)
class NullDropper(SparkTransformerMixin):

    """Simple transformer which drops any rows with null/None values"""

    _WRAPPED_CLASS = WrappedNullDropper
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns


@block(
    "befe781a-0227-40bc-a7ef-d79432c9f93e",
    "Generate seasonal context vectors transformer",
    "0.0.1",
)
class SeasonalContextGenerator(SparkTransformerMixin):

    """Generate seasonal context vectors transformer"""

    _WRAPPED_CLASS = WrappedSeasonalContextGenerator
    # _TS_COL_PARAM = "time_column"
    # _VAL_COLS_PARAM = "feature_columns"

    _INTERNAL_TIMESERIES_TYPE = "spark"
    # need to handle these columns
    # id_columns, feature_columns, target_columns
