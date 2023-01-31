from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.svm import LinearSVR
from sklearn.neural_network import MLPRegressor
from sklearn.multioutput import MultiOutputRegressor
import logging
from autoai_ts_libs.deps.srom.utils.no_op import NoOp

LOGGER = logging.getLogger(__name__)

xgboost_installed = False
try:
    from xgboost import XGBRegressor

    xgboost_installed = True
except:
    LOGGER.error("ImportError in timeseries_pred_dag.py : xgboost is not installed ")
    pass

lgbm_installed = False
try:
    import lightgbm as lgb

    lgbm_installed = True
except:
    LOGGER.error("ImportError in timeseries_pred_dag.py : lightgbm is not installed ")
    pass

tf_installed = False
try:
    import tensorflow as tf

    tf_installed = True
except:
    LOGGER.error("ImportError in timeseries_pred_dag.py : tensorflow is not installed ")
    pass

if tf_installed:
    from autoai_ts_libs.deps.srom.deep_learning.regressor import (
        DeepCNNRegressor,
        DeepDNNRegressor,
        DeepLSTMRegressor,
        DNNRegressor,
        SeriesNetRegressor,
        SimpleCNNRegressor,
        SimpleLSTMRegressor,
        WaveNetRegressor,
    )

from autoai_ts_libs.deps.srom.preprocessing.transformer import (
    Anscombe,
    Fisher,
    Log,
    MeanDivision,
    MeanDivisionLog,
    MeanSubtraction,
    MeanSubtractionLog,
    # MinMaxScaler,
    Reciprocal,
    Sqrt,
    TSMinMaxScaler,
    MinMaxXYScaler,
)
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import (
    AdvancedSummaryStatistics,
    FFTFeatures,
    Flatten,
    HigherOrderStatistics,
    SummaryStatistics,
    TimeTensorTransformer,
    WaveletFeatures,
    NormalizedFlatten,
    DifferenceFlatten,
    DifferenceNormalizedFlatten,
    LocalizedFlatten,
)
from autoai_ts_libs.deps.srom.time_series.models.arima import ARIMAModel
from autoai_ts_libs.deps.srom.time_series.models.mean import MeanModel

from autoai_ts_libs.deps.srom.time_series.models.MT2RForecaster import MT2RForecaster
from autoai_ts_libs.deps.srom.time_series.models.sarima import SARIMAModel
from autoai_ts_libs.deps.srom.time_series.models.T2RForecaster import T2RForecaster
from autoai_ts_libs.deps.srom.time_series.models.zero import ZeroModel

RANDOM_STATE = 42


def get_ML_forcaster_dag():
    """
    This Dag is used for a) Timeseries Prediction Pipeline (Regression)
    as non-timeseries models
    """

    function_transformers = [
        ("Log", Log()),
        ("Reciprocal", Reciprocal()),
        ("Anscombe", Anscombe()),
        ("Sqrt", Sqrt()),
        ("Fisher", Fisher()),
        ("MeanDivision", MeanDivision()),
        ("MeanSubtraction", MeanSubtraction()),
        ("MeanDivisionLog", MeanDivisionLog()),
        ("MeanSubtractionLog", MeanSubtractionLog()),
    ]
    data_transformers = [
        ("Flatten", Flatten()),
        ("WaveletFeatures", WaveletFeatures()),
        ("FFTFeatures", FFTFeatures()),
        ("SummaryStatistics", SummaryStatistics()),
        ("AdvancedSummaryStatistics", AdvancedSummaryStatistics()),
        ("HigherOrderStatistics", HigherOrderStatistics()),
    ]
    models = [
        ("LinearRegression", LinearRegression()),
        ("DecisionTreeRegressor", DecisionTreeRegressor(random_state=RANDOM_STATE)),
    ]

    stages = [function_transformers, data_transformers, models]
    return stages


def get_extended_ML_forcaster_dag():
    """
    This Dag is used for a) Timeseries Prediction Pipeline (Regression)
    as non-timeseries models
    """

    function_transformers = [
        ("SkipTransformer", NoOp()),
        ("Log", Log()),
        ("Reciprocal", Reciprocal()),
        ("Anscombe", Anscombe()),
        ("Sqrt", Sqrt()),
        ("Fisher", Fisher()),
        ("MeanDivision", MeanDivision()),
        ("MeanSubtraction", MeanSubtraction()),
        ("MeanDivisionLog", MeanDivisionLog()),
        ("MeanSubtractionLog", MeanSubtractionLog()),
    ]
    data_transformers = [
        ("Flatten", Flatten()),
        # ("WaveletFeatures", WaveletFeatures()),
        # ("FFTFeatures", FFTFeatures()),
        # ("SummaryStatistics", SummaryStatistics()),
        # ("AdvancedSummaryStatistics", AdvancedSummaryStatistics()),
        # ("HigherOrderStatistics", HigherOrderStatistics()),
        ("NormalizedFlatten", NormalizedFlatten()),
        ("DifferenceFlatten", DifferenceFlatten()),
        ("DifferenceNormalizedFlatten", DifferenceNormalizedFlatten()),
        ("LocalizedFlatten", LocalizedFlatten()),
    ]
    models = [
        ("LinearRegression", LinearRegression()),
        ("DecisionTreeRegressor", DecisionTreeRegressor(random_state=RANDOM_STATE)),
        ("MLPRegressor", MLPRegressor(random_state=RANDOM_STATE)),
        ("LinearSVR", LinearSVR(random_state=RANDOM_STATE)),
        ("HuberRegressor", HuberRegressor()),
        ("RandomForestRegressor", RandomForestRegressor(random_state=RANDOM_STATE)),
        (
            "GradientBoostingRegressor",
            GradientBoostingRegressor(random_state=RANDOM_STATE),
        ),
    ]

    if xgboost_installed:
        models.append(("xgboost", XGBRegressor()))

    if lgbm_installed:
        lightGBM = lgb.LGBMRegressor(random_state=RANDOM_STATE)
        models.append(("lightGBM", lightGBM))

    stages = [function_transformers, data_transformers, models]
    return stages


def get_benchmarked_ML_forcaster_dag(multi_output=False):
    """
    This Dag is used for a) Timeseries Prediction Pipeline (Regression)
    as non-timeseries models

    Parameters
    ----------
    multi_output : boolean
        True if more than 1 target columns are present, otherwise False. Default is set to False.
    """

    function_transformers = [
        ("SkipTransformer", NoOp()),
        ("Log", Log()),
        ("Reciprocal", Reciprocal()),
        # ("Anscombe", Anscombe()),
        ("Sqrt", Sqrt()),
        # ("Fisher", Fisher()),
        ("MeanDivision", MeanDivision()),
        ("MeanSubtraction", MeanSubtraction()),
        ("MeanDivisionLog", MeanDivisionLog()),
        # ("MeanSubtractionLog", MeanSubtractionLog()),
    ]
    data_transformers = [
        ("Flatten", Flatten()),
        # ("WaveletFeatures", WaveletFeatures()),
        # ("FFTFeatures", FFTFeatures()),
        # ("SummaryStatistics", SummaryStatistics()),
        # ("AdvancedSummaryStatistics", AdvancedSummaryStatistics()),
        # ("HigherOrderStatistics", HigherOrderStatistics()),
        ("NormalizedFlatten", NormalizedFlatten()),
        ("DifferenceFlatten", DifferenceFlatten()),
        ("DifferenceNormalizedFlatten", DifferenceNormalizedFlatten()),
        ("LocalizedFlatten", LocalizedFlatten()),
    ]
    models = [
        ("LinearRegression", LinearRegression()),
        ("LinearSVR", LinearSVR(random_state=0)),
        ("HuberRegressor", HuberRegressor()),
        (
            "RandomForestRegressor",
            RandomForestRegressor(random_state=0),
        ),
    ]

    if multi_output:
        models = [
            ("LinearRegression", MultiOutputRegressor(LinearRegression())),
            # ("DecisionTreeRegressor", DecisionTreeRegressor()),
            # ("MLPRegressor", MLPRegressor(random_state=0)),
            ("LinearSVR", MultiOutputRegressor(LinearSVR(random_state=0))),
            ("HuberRegressor", MultiOutputRegressor(HuberRegressor())),
            (
                "RandomForestRegressor",
                MultiOutputRegressor(RandomForestRegressor(random_state=0)),
            ),
            # ("GradientBoostingRegressor", GradientBoostingRegressor(random_state=0)),
        ]
    """
    if xgboost_installed:
        models.append(("xgboost", XGBRegressor()))

    if lgbm_installed:
        lightGBM = lgb.LGBMRegressor()
        models.append(("lightGBM", lightGBM))
    """

    stages = [function_transformers, data_transformers, models]
    return stages


def get_fast_ML_forecaster_dag():
    """
    This Dag is used for Timeseries Prediction Pipeline (Regression)
    as non-timeseries models.
    """

    data_transformers = [
        ("Flatten", Flatten()),
        ("NormalizedFlatten", NormalizedFlatten()),
        ("DifferenceFlatten", DifferenceFlatten()),
        ("DifferenceNormalizedFlatten", DifferenceNormalizedFlatten()),
        ("LocalizedFlatten", LocalizedFlatten()),
    ]
    models = [
        ("LinearRegression", LinearRegression()),
        ("DecisionTreeRegressor", DecisionTreeRegressor(random_state=RANDOM_STATE)),
        ("MLPRegressor", MLPRegressor(random_state=RANDOM_STATE)),
        ("LinearSVR", LinearSVR(random_state=RANDOM_STATE)),
        ("HuberRegressor", HuberRegressor()),
        (
            "GradientBoostingRegressor",
            GradientBoostingRegressor(random_state=RANDOM_STATE),
        ),
    ]

    stages = [data_transformers, models]
    return stages


def get_DL_forcaster_dag():
    """
    This Dag is used for a) Timeseries Prediction Pipeline (Regression)
    as non-timeseries models
    """

    function_transformers = [
        ("Log", Log()),
        ("Reciprocal", Reciprocal()),
        # ("Anscombe", Anscombe()),
        ("Sqrt", Sqrt()),
        ("Fisher", Fisher()),
        ("MeanDivision", MeanDivision()),
        # ("MeanSubtraction", MeanSubtraction()),
        ("MeanDivisionLog", MeanDivisionLog()),
        ("MeanSubtractionLog", MeanSubtractionLog()),
        ("MinMaxScaler", TSMinMaxScaler()),
    ]
    data_transformers = [
        ("Flatten", Flatten()),
        ("WaveletFeatures", WaveletFeatures()),
        ("FFTFeatures", FFTFeatures()),
        ("SummaryStatistics", SummaryStatistics()),
        ("AdvancedSummaryStatistics", AdvancedSummaryStatistics()),
        ("HigherOrderStatistics", HigherOrderStatistics()),
    ]
    normalizers = [("MinMaxXYScaler", MinMaxXYScaler())]
    if tf_installed:
        models = [
            (
                "DNNRegressor",
                DNNRegressor(input_dimension=(1,), output_dimension=1, verbose=0),
            ),
            (
                "DeepDNNRegressor",
                DeepDNNRegressor(input_dimension=(1,), output_dimension=1, verbose=0),
            ),
        ]
    else:
        models = []

    stages = [function_transformers, data_transformers, normalizers, models]
    return stages


def get_timeseries_DL_forcaster_dag():
    """
    This Dag is used for a) Timeseries Prediction Pipeline (Regression)
    as timeseries models
    """

    data_preprocessor = [("MinMaxScaler", TSMinMaxScaler()), ("NoOp", NoOp())]
    transformers = [("TimeTensorTransformer", TimeTensorTransformer())]
    if tf_installed:
        ts_models = [
            (
                "SimpleLSTMRegressor",
                SimpleLSTMRegressor(
                    input_dimension=(1, 1), output_dimension=1, verbose=0
                ),
            ),
            (
                "DeepLSTMRegressor",
                DeepLSTMRegressor(
                    input_dimension=(1, 1), output_dimension=1, verbose=0
                ),
            ),
            (
                "SimpleCNNRegressor",
                SimpleCNNRegressor(
                    input_dimension=(1, 1), output_dimension=1, verbose=0
                ),
            ),
            (
                "DeepCNNRegressor",
                DeepCNNRegressor(input_dimension=(1, 1), output_dimension=1, verbose=0),
            ),
            (
                "WaveNetRegressor",
                WaveNetRegressor(input_dimension=(1, 1), output_dimension=1, verbose=0),
            ),
            (
                "SeriesNetRegressor",
                SeriesNetRegressor(
                    input_dimension=(1, 1), output_dimension=1, verbose=0
                ),
            ),
        ]
    else:
        ts_models = []
    stages = [data_preprocessor, transformers, ts_models]
    return stages


def get_stats_forcaster_dag(multi_output=False):
    """
    This Dag is used for a) Timeseries Prediction Pipeline (Regression)
    as timeseries models
    """

    stats_dag = [
        ("ARIMAModel", ARIMAModel()), # univariate
        ("SARIMAModel", SARIMAModel()), # univariate
        ("T2RForecaster", T2RForecaster()), # univariate
    ]
    if multi_output:
        stats_dag = [
            ("MeanModel", MeanModel()), # multivariate
            ("MT2RForecaster", MT2RForecaster()), # multivariate
            ("ZeroModel", ZeroModel()), # multivariate
        ]
    stages = [stats_dag]
    return stages

def get_debugging_dag():
    """
    This Dag is used for a) Timeseries Prediction Pipeline (Regression)
    as timeseries models
    """
    stages = [[("ZeroModel", ZeroModel())]]
    return stages

ML_FORECAST_DAG = get_ML_forcaster_dag()
DL_FORECAST_DAG = get_DL_forcaster_dag()
TS_DL_FORECAST_DAG = get_timeseries_DL_forcaster_dag()
STATS_FORECAST_DAG = get_stats_forcaster_dag()
STATS_FORECAST_DAG_Multi_Output_DAG = get_stats_forcaster_dag(multi_output=True)
Extended_ML_Forecast_DAG = get_extended_ML_forcaster_dag()
FAST_ML_Forecast_DAG = get_fast_ML_forecaster_dag()
BENCHMARK_ML_Forecaster_DAG = get_benchmarked_ML_forcaster_dag()
BENCHMARK_ML_Forecaster_Multi_Output_DAG = get_benchmarked_ML_forcaster_dag(multi_output=True)
DEBUG_DAG = get_debugging_dag()
