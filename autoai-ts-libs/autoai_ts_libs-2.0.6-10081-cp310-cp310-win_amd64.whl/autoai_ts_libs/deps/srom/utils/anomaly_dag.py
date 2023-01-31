"""
This is an utility file to properly document the anomaly detector compatible with
srom pipeline
"""

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_ensembler import AnomalyEnsembler
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_robust_pca import AnomalyRobustPCA
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.bayesian_gmm_outlier import BayesianGMMOutlier
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.extended_isolation_forest import (
    ExtendedIsolationForest,
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.ggm_pgscps import GraphPgscps
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.ggm_quic import GraphQUIC
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.gmm_outlier import GMMOutlier
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.hotteling_t2 import HotellingT2
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.lof_nearest_neighbor import (
    LOFNearestNeighborAnomalyModel,
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.nearest_neighbor import (
    NearestNeighborAnomalyModel,
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.negative_sample_anomaly import NSA
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.neural_network_nsa import NeuralNetworkNSA
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.pca_q import AnomalyPCA_Q
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.pca_t2 import AnomalyPCA_T2
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.random_partition_forest import (
    RandomPartitionForest,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import IsolationForest
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.sample_svdd import SampleSVDD
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.ggm_pgscps import GraphPgscps

from sklearn.covariance import (
    EmpiricalCovariance,
    EllipticEnvelope,
    LedoitWolf,
    MinCovDet,
    OAS,
    ShrunkCovariance,
)
from sklearn.neighbors import KernelDensity
from sklearn.svm import OneClassSVM
from autoai_ts_libs.deps.srom.anomaly_detection.gaussian_graphical_anomaly_model import (
    GaussianGraphicalModel,
)

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.cusum import CUSUM
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.spad import SPAD
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.extended_spad import ExtendedSPAD
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.oob import OOB

# deep learning model
from autoai_ts_libs.deps.srom.deep_learning.anomaly_detector import DNNAutoEncoder

RANDOM_STATE = 42

anomaly_dag = [
    (IsolationForest(random_state=RANDOM_STATE), -1, "decision_function", "isolationforest"),
    (NearestNeighborAnomalyModel(), 1, "anomaly_score", "nearestneighboranomalymodel"),
    (MinCovDet(random_state=RANDOM_STATE), 1, "mahalanobis", "mincovdet"),
    (AnomalyEnsembler(random_state=RANDOM_STATE), 1, "anomaly_score", "anomalyensembler"),
    (
        NSA(
            scale=True,
            sample_ratio=25.0,
            sample_delta=0.05,
            base_model=RandomForestClassifier(random_state=2),
        ),
        1,
        "anomaly_score",
        "nsa"
    ),
    (
        AnomalyEnsembler(predict_only=True, random_state=RANDOM_STATE),
        1,
        "anomaly_score",
        "predictonly_anomalyensembler"
    ),
    (AnomalyRobustPCA(), 1, "anomaly_score", "anomalyrobustpca"),
    (ExtendedIsolationForest(), 1, "anomaly_score", "extendedisolationforest"),
    (LOFNearestNeighborAnomalyModel(), 1, "anomaly_score","lofnearestneighboranomalymodel"),
    (
        NeuralNetworkNSA(
            scale=True,
            sample_ratio=25.0,
            sample_delta=0.05,
            batch_size=10,
            epochs=1,
            dropout=0.85,
            layer_width=150,
            n_hidden_layers=2,
        ),
        -1,
        "anomaly_score",
        "neuralnetworknsa"
    ),
    (AnomalyPCA_T2(), 1, "anomaly_score", "anomalypca_t2"),
    (AnomalyPCA_Q(), 1, "anomaly_score", "anomalypca_q"),
    #(RandomPartitionForest(), -1, "anomaly_score", "randompartitionforest"),
    (SampleSVDD(), -1, "anomaly_score", "samplesvdd"),
    (EmpiricalCovariance(), 1, "mahalanobis", "empiricalcovariance"),
    (EllipticEnvelope(random_state=RANDOM_STATE), 1, "mahalanobis", "ellipticenvelope"),
    (LedoitWolf(), 1, "mahalanobis", "ledoitwolf"),
    (OAS(), 1, "mahalanobis", "oas"),
    (ShrunkCovariance(), 1, "mahalanobis", "shrunkcovariance"),
    (OneClassSVM(), -1, "decision_function", "oneclasssvm"),
    (GaussianGraphicalModel(sliding_window_size=0, scale=False), 1, "predict", "gaussiangraphicalmodel"),
    (GMMOutlier(random_state=RANDOM_STATE, method="quantile"), 1, "decision_function", "gmmoutlier"),
    (CUSUM(), 1, "predict", "cusum"),
    (KernelDensity(), -1, "score_samples", "kerneldensity"),
    (GraphPgscps(), 1, "mahalanobis", "graphpgscps"),
    (HotellingT2(), 1, "decision_function", "hotellingt2"),
    (SPAD(), -1, "decision_function", "spad"),
    (ExtendedSPAD(), -1, "decision_function", "extendedspad"),
    (OOB(), 1, "decision_function", "oob"),
    (DNNAutoEncoder(random_state=RANDOM_STATE), 1, "predict", "DeepDNNAutoEncoder")
]

extended_anomaly_dag = [
    (GaussianGraphicalModel(sliding_window_size=0, scale=True), 1, "predict","gaussiangraphicalmodel_base"),
    (
        GaussianGraphicalModel(
            sliding_window_size=0, base_learner=GraphQUIC(), scale=False,
        ),
        1,
        "predict",
        "gaussiangraphicalmodel_scale"
    ),
    (
        GaussianGraphicalModel(
            sliding_window_size=0, base_learner=GraphQUIC(), scale=True,
        ),
        1,
        "predict",
        "gaussiangraphicalmodel_scale_lo"
    ),
    (
        GaussianGraphicalModel(
            sliding_window_size=0, base_learner=GraphPgscps(), scale=False,
        ),
        1,
        "predict",
        "gaussiangraphicalmodel_lo"
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="tied", method="quantile"
        ),
        1,
        "decision_function",
        "gmmoutlier_tied_quantile"
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="diag", method="quantile"
        ),
        1,
        "decision_function",
        "gmmoutlier_diag_quantile"
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="full", method="quantile"
        ),
        1,
        "decision_function",
        "gmmoutlier_full_quantile"
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="spherical", method="quantile"
        ),
        1,
        "decision_function",
        "gmmoutlier_spherical_quantile"
    ),
    (GMMOutlier(random_state=RANDOM_STATE, method="stddev"), 1, "decision_function", "gmmoutlier_stddev"),
    (
        GMMOutlier(random_state=RANDOM_STATE, covariance_type="tied", method="stddev"),
        1,
        "decision_function",
        "gmmoutlier_tied_stddev"
    ),
    (
        GMMOutlier(random_state=RANDOM_STATE, covariance_type="diag", method="stddev"),
        1,
        "decision_function",
        "gmmoutlier_diag_stddev"
    ),
    (
        GMMOutlier(random_state=RANDOM_STATE, covariance_type="full", method="stddev"),
        1,
        "decision_function",
        "gmmoutlier_full_stddev"
    ),
    (
        GMMOutlier(
            random_state=RANDOM_STATE, covariance_type="spherical", method="stddev"
        ),
        1,
        "decision_function",
        "gmmoutlier_spherical_stddev"
    ),
    (
        BayesianGMMOutlier(random_state=RANDOM_STATE, method="quantile"),
        1,
        "decision_function",
        "bayesiangmmoutlier_quantile"
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="tied", method="quantile"
        ),
        1,
        "decision_function",
        "bayesiangmmoutlier_tied_quantile"
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="diag", method="quantile"
        ),
        1,
        "decision_function",
        "bayesiangmmoutlier_diag_quantile"
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="full", method="quantile"
        ),
        1,
        "decision_function",
        "bayesiangmmoutlier_full_quantile"
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="spherical", method="quantile"
        ),
        1,
        "decision_function",
        "bayesiangmmoutlier_spherical_quantile"
    ),
    (
        BayesianGMMOutlier(random_state=RANDOM_STATE, method="stddev"),
        1,
        "decision_function",
        "bayesiangmmoutlier_stddev"
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="tied", method="stddev"
        ),
        1,
        "decision_function",
        "bayesiangmmoutlier_tied_stddev"
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="diag", method="stddev"
        ),
        1,
        "decision_function",
        "bayesiangmmoutlier_diag_stddev"
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="full", method="stddev"
        ),
        1,
        "decision_function",
        "bayesiangmmoutlier_full_stddev"
    ),
    (
        BayesianGMMOutlier(
            random_state=RANDOM_STATE, covariance_type="spherical", method="stddev"
        ),
        1,
        "decision_function",
        "bayesiangmmoutlier_spherical_stddev"
    ),
]

extended_anomaly_dag = anomaly_dag + extended_anomaly_dag
pyod_algorithms = []
outlier_algorithms = []

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_pca import AnomalyPCA
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.kde import KDE
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.sparse_structure_learning import (
    SparseStructureLearning,
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.hbos import HBOS

outlier_algorithms = [
    (HBOS(), 1, "decision_function", "hbos"),
    (SparseStructureLearning(), 1, "decision_function", "sparsestructurelearning"),
    (KDE(), 1, "decision_function", "kde"),
    (AnomalyPCA(), 1, "decision_function", "pca"),
]
