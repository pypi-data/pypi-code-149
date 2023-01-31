from sklearn.covariance import (
    EllipticEnvelope,
    MinCovDet,
    OAS,
    ShrunkCovariance,
)
from sklearn.ensemble import IsolationForest
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_ensembler import AnomalyEnsembler
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.bayesian_gmm_outlier import BayesianGMMOutlier
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.extended_isolation_forest import (
    ExtendedIsolationForest,
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.ggm_pgscps import GraphPgscps
# from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.ggm_quic import GraphQUIC
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.gmm_outlier import GMMOutlier
# from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.hotteling_t2 import HotellingT2
# from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.lof_nearest_neighbor import (
#    LOFNearestNeighborAnomalyModel,
# )
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.nearest_neighbor import (
    NearestNeighborAnomalyModel,
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.negative_sample_anomaly import NSA
from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
from autoai_ts_libs.deps.srom.preprocessing.transformer import DataStationarizer
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.time_series.pipeline import WindowAD

# from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_robust_pca import AnomalyRobustPCA

RANDOM_STATE = 42

top_windowad_algorithms = [
    (IsolationForest(), -1, "decision_function"),
    (NearestNeighborAnomalyModel(), 1, "anomaly_score"),
    (EllipticEnvelope(), 1, "mahalanobis"),
    (MinCovDet(random_state=RANDOM_STATE), 1, "mahalanobis"),
    (AnomalyEnsembler(random_state=RANDOM_STATE), 1, "anomaly_score"),
    (ExtendedIsolationForest(), 1, "anomaly_score"),
    (
        BayesianGMMOutlier(random_state=RANDOM_STATE, method="quantile"),
        1,
        "decision_function",
    ),
    (GMMOutlier(random_state=RANDOM_STATE, method="quantile"), 1, "decision_function"),
    (ShrunkCovariance(), 1, "mahalanobis"),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="tied", method="stddev"
        ),
        1,
        "decision_function",
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="diag", method="stddev"
        ),
        1,
        "decision_function",
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="full", method="stddev"
        ),
        1,
        "decision_function",
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="spherical", method="stddev"
        ),
        1,
        "decision_function",
    ),
    (OAS(), 1, "mahalanobis"),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="tied", method="quantile"
        ),
        1,
        "decision_function",
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="diag", method="quantile"
        ),
        1,
        "decision_function",
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="full", method="quantile"
        ),
        1,
        "decision_function",
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="spherical", method="quantile"
        ),
        1,
        "decision_function",
    ),
    (GMMOutlier(random_state=RANDOM_STATE, method="stddev"), 1, "decision_function"),
    (
        GMMOutlier(random_state=RANDOM_STATE, covariance_type="tied", method="stddev"),
        1,
        "decision_function",
    ),
    (
        GMMOutlier(random_state=RANDOM_STATE, covariance_type="diag", method="stddev"),
        1,
        "decision_function",
    ),
    (
        GMMOutlier(random_state=RANDOM_STATE, covariance_type="full", method="stddev"),
        1,
        "decision_function",
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="spherical", method="stddev"
        ),
        1,
        "decision_function",
    ),
    (GraphPgscps(), 1, "mahalanobis"),
]

valid_windowad_algorithms = {}
valid_windowad_algorithms["IsolationForest"] = (
    IsolationForest(random_state=RANDOM_STATE),
    -1,
    "decision_function",
)
valid_windowad_algorithms["NearestNeighbor"] = (
    NearestNeighborAnomalyModel(),
    1,
    "anomaly_score",
)
valid_windowad_algorithms["SyntheticRandomForestTrainer"] = (
    NSA(scale=True, sample_ratio=0.4, sample_delta=0.05),
    1,
    "anomaly_score",
)
valid_windowad_algorithms["MinCovDet"] = (
    MinCovDet(random_state=RANDOM_STATE),
    1,
    "mahalanobis",
)
valid_windowad_algorithms["AnomalyEnsembler"] = (
    AnomalyEnsembler(random_state=RANDOM_STATE),
    1,
    "anomaly_score",
)


def get_windowad_pipelines(
    num_estimators,
    lookback_win,
    target_columns,
    time_column,
    scoring_method,
    observation_window,
    scoring_threshold,
):
    """[summary]

    Args:
        num_estimators ([type]): [description]
        lookback_win ([type]): [description]
        target_columns ([type]): [description]
        time_column ([type]): [description]
        scoring_method ([type]): [description]
        observation_window ([type]): [description]
        scoring_threshold ([type]): [description]

    Returns:
        [type]: [description]
    """
    pipelines = []
    for algorithm in top_windowad_algorithms[:num_estimators]:
        pipelines.append(
            WindowAD(
                steps=[
                    (
                        "DataStationarizer",
                        DataStationarizer(
                            feature_columns=target_columns,
                            target_columns=target_columns,
                        ),
                    ),
                    (
                        "Flatten",
                        Flatten(
                            feature_columns=target_columns,
                            target_columns=target_columns,
                            lookback_win=lookback_win,
                            pred_win=0,
                        ),
                    ),
                    (
                        f"{algorithm[0]}",
                        GeneralizedAnomalyModel(
                            base_learner=algorithm[0],
                            predict_function=algorithm[2],
                            score_sign=algorithm[1],
                        ),
                    ),
                ],
                lookback_win=lookback_win,
                target_columns=target_columns,
                feature_columns=target_columns,
                time_column=time_column,
                scoring_method=scoring_method,
                observation_window=observation_window,
                scoring_threshold=scoring_threshold,
            )
        )
    return pipelines


def get_windowad_anomaly_estimator(
    anomaly_estimator,
    lookback_win=None,
    target_columns=None,
    time_column=None,
    scoring_method=None,
    observation_window=None,
    scoring_threshold=None,
    store_lookback_history=False,
):
    """[summary]

    Args:
        anomaly_estimator ([type]): [description]
        lookback_win ([type]): [description]
        target_columns ([type]): [description]
        time_column ([type]): [description]
        scoring_method ([type]): [description]
        observation_window ([type]): [description]
        scoring_threshold ([type]): [description]

    Raises:
        Exception: [description]

    Returns:
        [type]: [description]
    """
    if anomaly_estimator not in valid_windowad_algorithms.keys():
        raise Exception("Not a valid anomaly estimator")
    pipeline = WindowAD(
        steps=[
            ("DataStationarizer", DataStationarizer()),
            ("Flatten", Flatten()),
            (
                anomaly_estimator,
                GeneralizedAnomalyModel(
                    base_learner=valid_windowad_algorithms[anomaly_estimator][0],
                    predict_function=valid_windowad_algorithms[anomaly_estimator][2],
                    score_sign=valid_windowad_algorithms[anomaly_estimator][1],
                ),
            ),
        ],
        lookback_win=lookback_win,
        target_columns=target_columns,
        feature_columns=target_columns,
        time_column=time_column,
        scoring_method=scoring_method,
        observation_window=observation_window,
        scoring_threshold=scoring_threshold,
        store_lookback_history=store_lookback_history
    )

    return pipeline
