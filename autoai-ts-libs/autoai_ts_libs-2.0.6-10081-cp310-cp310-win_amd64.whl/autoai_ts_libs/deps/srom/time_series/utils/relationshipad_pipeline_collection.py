from autoai_ts_libs.deps.srom.anomaly_detection import GaussianGraphicalModel
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms import GraphPgscps
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.NMT_anomaly import NMT_anomaly
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_graph_lasso import AnomalyGraphLasso
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.covariance_anomaly import CovarianceAnomaly
from autoai_ts_libs.deps.srom.preprocessing.transformer import TSMinMaxScaler
from autoai_ts_libs.deps.srom.time_series.pipeline import RelationshipAD

ggm_l1 = GaussianGraphicalModel(
    base_learner=AnomalyGraphLasso(alpha=0.2), sliding_window_size=0
)
ggm_l0 = GaussianGraphicalModel(base_learner=GraphPgscps(sparsity=1, reg=0.1))
covariance_anomaly = CovarianceAnomaly()


valid_relationshipad_algorithms = {}
valid_relationshipad_algorithms["GMM_L1"] = (
    GaussianGraphicalModel(
        base_learner=AnomalyGraphLasso(alpha=0.2), sliding_window_size=0
    ),
    -1,
    "predict",
)
valid_relationshipad_algorithms["GMM_L0"] = (
    GaussianGraphicalModel(base_learner=GraphPgscps(sparsity=1, reg=0.1)),
    1,
    "predict",
)
valid_relationshipad_algorithms["Covariance"] = (
    CovarianceAnomaly(),
    1,
    "predict",
)
valid_relationshipad_algorithms["MachineTranslation"] = (
    NMT_anomaly(),
    1,
    "predict",
)


def get_relationshipad_anomaly_estimator(
    anomaly_estimator,
    lookback_win=None,
    target_columns=None,
    feature_columns=None,
    time_column=None,
    scoring_method=None,
    observation_window=None,
    scoring_threshold=None,
    store_lookback_history=False,
):
    """
    Returns relationshipAD pipeline based on choice of anomaly estimator

    Args:
        anomaly_estimator ([type]): [description]
        lookback_win ([type]): [description]
        target_columns ([type]): [description]
        feature_columns ([type]): [description]
        time_column ([type]): [description]
        scoring_method ([type]): [description]
        observation_window ([type]): [description]
        scoring_threshold ([type]): [description]

    Raises:
        Exception: Not a valid anomaly estimator

    Returns:
        RelationshipAD Pipeline
    """
    if anomaly_estimator not in valid_relationshipad_algorithms.keys():
        raise Exception("Not a valid anomaly estimator")
    pipeline = RelationshipAD(
        steps=[
            (
                "time_tensor",
                TSMinMaxScaler(),
            ),
            (anomaly_estimator, valid_relationshipad_algorithms[anomaly_estimator][
                        0
                    ]),
        ],
        lookback_win=lookback_win,
        target_columns=target_columns,
        feature_columns=feature_columns,
        time_column=time_column,
        scoring_method=scoring_method,
        observation_window=observation_window,
        scoring_threshold=scoring_threshold,
        store_lookback_history=store_lookback_history
        )
    return pipeline
