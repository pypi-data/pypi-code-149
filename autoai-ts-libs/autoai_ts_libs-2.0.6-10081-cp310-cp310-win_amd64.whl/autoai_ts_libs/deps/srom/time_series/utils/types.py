from enum import Enum
from argparse import ArgumentTypeError, Action
from autoai_ts_libs.deps.srom.utils.timeseries_pred_dag import (
    ML_FORECAST_DAG,
    DL_FORECAST_DAG,
    TS_DL_FORECAST_DAG,
    STATS_FORECAST_DAG,
    STATS_FORECAST_DAG_Multi_Output_DAG,
    Extended_ML_Forecast_DAG,
    BENCHMARK_ML_Forecaster_DAG,
    BENCHMARK_ML_Forecaster_Multi_Output_DAG,
)


class TSPDAGType(Enum):
    STATS = STATS_FORECAST_DAG
    STATS_MULTI_OUTPUT = STATS_FORECAST_DAG_Multi_Output_DAG
    EXT_ML = Extended_ML_Forecast_DAG
    BENCHMARK_ML = BENCHMARK_ML_Forecaster_DAG
    BENCHMARK_ML_MULTI_OUTPUT = BENCHMARK_ML_Forecaster_Multi_Output_DAG
    DL = DL_FORECAST_DAG
    TS_DL = TS_DL_FORECAST_DAG
    ML = ML_FORECAST_DAG


class AnomalyAlgorithmType(Enum):
    DEEPAD = "DeepAD"
    WINDOWAD = "WindowAD"
    PREDAD = "PredAD"
    RELATIONSHIPAD = "RelationshipAD"
    RECONSTRUCTAD = "ReconstructAD"


class AnomalyScoringAlgorithmType(Enum):
    IID = "iid"
    CHISQUARE = "Chi-Square"
    QSCORE = "Q-Score"
    SLIDING_WINDOW = "Sliding-Window"
    ADAPTIVE_SLIDING_WINDOW = "Adaptive-Sliding-Window"
    CONTEXTUAL_ANOMALY = "Contextual-Anomaly"


class AnomalyScoringPredictionType(Enum):
    # TRAINING = "training" # not exposing to user
    RECENT = "recent"
    BATCH = "batch"
    SLIDING = "sliding" # not exposing to user


class AnomalyExecutionModeType(Enum):
    STREAM = "Stream"
    BATCH = "Batch"


class WindowADAlgorithmType(Enum):
    ISOLATION_FOREST = "IsolationForest"
    NEAREST_NEIGHBOR = "NearestNeighbor"
    NSA = "SyntheticRandomForestTrainer"
    MIN_COV_DET = "MinCovDet"
    ANOMALY_ENSEMBLER = "AnomalyEnsembler"


class ReconstructADAlgorithmType(Enum):
    DNN_AE = "DNN_AutoEncoder"
    SEQ2SEQ = "Seq2seq_AutoEncoder"
    CNN = "CNN_AutoEncoder"
    DNN_VAE = "DNN_VariationalAutoEncoder"


class RelationshipADAlgorithmType(Enum):
    COVARIANCE = "Covariance"
    GMM_L0 = "GMM_L0"
    GMM_L1 = "GMM_L1"
    MACHINE_TRANSLATION = "MachineTranslation"


def lookback_win_type(x):
    try:
        return int(x)
    except:
        if x == "auto":
            return x
        else:
            raise ArgumentTypeError(
                "Lookback window should either be 'auto' or an integer."
            )


class AnomalyExecutionModeAction(Action):
    def __call__(self, parser, args, values, option_string=None):
        found = False
        for e in AnomalyExecutionModeType:
            if e.name == values:
                found = True
                setattr(args, self.dest, e)
        if not found:
            raise ArgumentTypeError("{} is not allowed.".format(values))


class AnomalyAlgoAction(Action):
    def __call__(self, parser, args, values, option_string=None):
        found = False
        for e in AnomalyAlgorithmType:
            if e.name == values:
                found = True
                setattr(args, self.dest, e)
        if not found:
            raise ArgumentTypeError("{} is not allowed.".format(values))


class DagAction(Action):
    def __call__(self, parser, args, values, option_string=None):
        found = False
        for e in TSPDAGType:
            if e.name == values:
                found = True
                setattr(args, self.dest, e)
        if not found:
            raise ArgumentTypeError("{} is not allowed.".format(values))


class AnomalyScoringAlgoAction(Action):
    def __call__(self, parser, args, values, option_string=None):
        found = False
        for e in AnomalyScoringAlgorithmType:
            if e.name == values:
                found = True
                setattr(args, self.dest, e)
        if not found:
            raise ArgumentTypeError("{} is not allowed.".format(values))


class PredTypeAction(Action):
    def __call__(self, parser, args, values, option_string=None):
        found = False
        for e in AnomalyScoringPredictionType:
            if e.name == values:
                found = True
                setattr(args, self.dest, e)
        if not found:
            raise ArgumentTypeError("{} is not allowed.".format(values))


class AnomalyEstimatorAction(Action):
    def __call__(self, parser, args, values, option_string=None):
        found = False
        for e in WindowADAlgorithmType:
            if e.name == values:
                found = True
                setattr(args, self.dest, e)
        if not found:
            raise ArgumentTypeError("{} is not allowed.".format(values))
