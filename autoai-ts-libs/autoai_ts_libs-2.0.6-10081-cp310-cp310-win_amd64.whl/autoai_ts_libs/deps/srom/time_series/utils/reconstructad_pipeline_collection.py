from autoai_ts_libs.deps.srom.deep_learning.anomaly_detector import (
    DNNAutoEncoder,
    LSTMAutoEncoder,
    CNNAutoEncoder,
)
from autoai_ts_libs.deps.srom.deep_learning.anomaly_detector import DNNVariationalAutoEncoder
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import TimeTensorTransformer
from autoai_ts_libs.deps.srom.time_series.pipeline import ReconstructAD

# add models here:

valid_reconstruct_algorithms = {}
valid_reconstruct_algorithms["DNN_AutoEncoder"] = DNNAutoEncoder(
    input_dimension=20, encoding_dimension=10, epochs=50
)
valid_reconstruct_algorithms["Seq2seq_AutoEncoder"] = LSTMAutoEncoder(
    input_dimension=(10, 2), hidden_dimension=2, epochs=50
)
valid_reconstruct_algorithms["CNN_AutoEncoder"] = CNNAutoEncoder(
    input_dimension=(20, 2), epochs=50
)
valid_reconstruct_algorithms["DNN_VariationalAutoEncoder"] = DNNVariationalAutoEncoder(
    generator_dimension=3, epochs=50
)


def get_reconstructad_anomaly_estimator(
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
    Returns ReconstructAD pipeline based on choice of anomaly estimator

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
        ReconstructAD Pipeline
    """
    if anomaly_estimator not in valid_reconstruct_algorithms.keys():
        raise Exception("Not a valid anomaly estimator")
    if anomaly_estimator.startswith("DNN"):
        pipeline = ReconstructAD(
            steps=[
                ("flatten", Flatten()),
                (anomaly_estimator, valid_reconstruct_algorithms[anomaly_estimator]),
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
    else:
        pipeline = ReconstructAD(
            steps=[
                ("TimeTensor", TimeTensorTransformer()),
                (anomaly_estimator, valid_reconstruct_algorithms[anomaly_estimator]),
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
