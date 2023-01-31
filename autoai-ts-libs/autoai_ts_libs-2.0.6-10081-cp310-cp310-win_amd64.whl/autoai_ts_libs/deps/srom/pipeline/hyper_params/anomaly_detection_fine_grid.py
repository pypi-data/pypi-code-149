# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Anomaly Detection Fine Grid: Contains a dictionary of hyper-parameters for
anomaly algorithms.
"""
PARAM_GRID = {}

# ************************************
# ******** Parameter Grid for GAM ****
# ************************************

# Anomaly Robust PCA
PARAM_GRID["anomalyrobustpca__base_learner__scale"] = [True, False]
PARAM_GRID["anomalyrobustpca__base_learner__error_order"] = [1, 2]
PARAM_GRID["anomalyrobustpca__base_learner__anomaly_threshold"] = [1.0, 2.0, 3.0]

# Extended Isolation Forest
PARAM_GRID["extendedisolationforest__base_learner__n_estimators"] = [
    100,
    200,
    300,
    500,
    1000,
]
PARAM_GRID["extendedisolationforest__base_learner__max_samples"] = [
    "auto",
    300,
    400,
    500,
]
PARAM_GRID["extendedisolationforest__base_learner__max_features"] = [
    1.0,
    0.7,
    0.5,
    0.2,
]
PARAM_GRID["extendedisolationforest__base_learner__std_threshold"] = [
    2.5,
    5.0,
    1.0,
    10.0,
]


# lof Nearest Neighbor Anomaly Model
PARAM_GRID["lofnearestneighboranomalymodel__base_learner__n_neighbors"] = [
    1,
    3,
    5,
    10,
    20,
]
PARAM_GRID["lofnearestneighboranomalymodel__base_learner__anomaly_threshold"] = [
    2.5,
    5,
    1,
    2,
    3,
]


# Nearest Neighbor Anomaly Model
PARAM_GRID["nearestneighboranomalymodel__base_learner__n_neighbors"] = [1, 3, 5, 10, 20]
PARAM_GRID["nearestneighboranomalymodel__base_learner__anomaly_threshold"] = [
    2.5,
    5,
    1,
    2,
    3,
]

# NeuralNetworkNSA
PARAM_GRID["neuralnetworknsa__base_learner__sample_ratio"] = [10, 20, 30, 40, 5]
PARAM_GRID["neuralnetworknsa__base_learner__sample_delta"] = [0.05, 0, 1, 0.2, 0.005]
PARAM_GRID["neuralnetworknsa__base_learner__layer_width"] = [1, 2, 3, 4, 5]
PARAM_GRID["neuralnetworknsa__base_learner__n_hidden_layers"] = [5, 10, 15, 30]
PARAM_GRID["neuralnetworknsa__base_learner__epochs"] = [5, 10, 50, 100]
PARAM_GRID["neuralnetworknsa__base_learner__batch_size"] = [10, 20, 30]

# NSA
PARAM_GRID["nsa__base_learner__scale"] = [True, False]
PARAM_GRID["nsa__base_learner__sample_ratio"] = [10, 20, 30, 40, 5]
PARAM_GRID["nsa__base_learner__sample_delta"] = [0.05, 0, 1, 0.2, 0.005]

# AnomalyPCA_T2
PARAM_GRID["anomalypca_t2__base_learner__scale"] = [True, False]
PARAM_GRID["anomalypca_t2__base_learner__variance_threshold"] = [0.7, 0.8, 0.9, 0.95]
PARAM_GRID["anomalypca_t2__base_learner__alpha"] = [0.05, 0.1]

# AnomalyPCA_Q
PARAM_GRID["anomalypca_q__base_learner__scale"] = [True, False]
PARAM_GRID["anomalypca_q__base_learner__variance_threshold"] = [0.1, 0.9]
PARAM_GRID["anomalypca_q__base_learner__alpha"] = [0.05, 0.1]

# RandomPartitionForest
PARAM_GRID["randompartitionforest__base_learner__n_estimator"] = [100, 150, 50, 200]
PARAM_GRID["randompartitionforest__base_learner__max_samples"] = [10, 20, 30, 50]
PARAM_GRID["randompartitionforest__base_learner__anomaly_type"] = [
    "visit_frequency",
    "point_wise",
    "collective_anomaly",
]
PARAM_GRID["randompartitionforest__base_learner__alpha"] = [1.0, 2.0, 3.0, 5.0, 10.0]

# samplesvdd
PARAM_GRID["samplesvdd__base_learner__outlier_fraction"] = [
    0.001,
    0.002,
    0.005,
    0.01,
    0.5,
]
PARAM_GRID["samplesvdd__base_learner__kernel_s"] = [2, 5, 10, 20]
PARAM_GRID["samplesvdd__base_learner__maxite"] = [1000, 2000, 5000, 10000]
PARAM_GRID["samplesvdd__base_learner__resample_n"] = [10, 20, 30, 50]
PARAM_GRID["samplesvdd__base_learner__n_iter"] = [10, 20, 30, 50, 100]

# EmpiricalCovariance
PARAM_GRID["empiricalcovariance__base_learner__store_precision"] = [True, False]

# Elliptic Envelope
PARAM_GRID["ellipticenvelope__base_learner__support_fraction"] = [
    None,
    0.1,
    0.3,
    0.5,
    0.7,
    0.9,
]
PARAM_GRID["ellipticenvelope__base_learner__contamination"] = [0.1, 0.2, 0.3, 0.4, 0.5]

# LedoitWolf
PARAM_GRID["ledoitwolf__base_learner__store_precision"] = [True, False]

# MinCovDet
PARAM_GRID["mincovdet__base_learner__support_fraction"] = [
    None,
    0.1,
    0.3,
    0.5,
    0.7,
    0.9,
]

# OAS
PARAM_GRID["oas__base_learner__store_precision"] = [True, False]

# Shrunk Covariance
PARAM_GRID["shrunkcovariance__base_learner__shrinkage"] = [
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
]


# One Class SVM
PARAM_GRID["oneclasssvm__base_learner__kernel"] = ["rbf", "linear", "poly", "sigmoid"]
PARAM_GRID["oneclasssvm__base_learner__nu"] = [0.1, 0.3, 0.5, 0.7, 0.9]
PARAM_GRID["oneclasssvm__base_learner__degree"] = [1, 3, 5, 7, 10]
PARAM_GRID["oneclasssvm__base_learner__gamma"] = ["auto", 0.1, 0.2, 0.3]
PARAM_GRID["oneclasssvm__base_learner__coef0"] = [0.0, 0.2, 0.4, 0.8]

# Isolation Forest
PARAM_GRID["isolationforest__base_learner__n_estimators"] = [10, 50, 100, 150, 200]
PARAM_GRID["isolationforest__base_learner__max_samples"] = [
    "auto",
    500,
    1000,
    0.1,
    0.2,
    0.5,
    0.8,
    1.0,
]
PARAM_GRID["isolationforest__base_learner__contamination"] = [0.1, 0.2, 0.3, 0.4, 0.5]
PARAM_GRID["isolationforest__base_learner__max_features"] = [
    1,
    2,
    3,
    4,
    5,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
]
PARAM_GRID["isolationforest__base_learner__random_state"] = [42]

# GaussianGraphicalModel
PARAM_GRID["gaussiangraphicalmodel__base_learner__distance_metric"] = [
    "KL_Divergence",
    "Frobenius_Norm",
    "Likelihood",
    "Spectral",
    "Mahalanobis_Distance",
]
PARAM_GRID["gaussiangraphicalmodel__base_learner__scale"] = [True, False]
PARAM_GRID["gaussiangraphicalmodel__base_learner__sliding_window_size"] = [
    0,
    15,
    30,
    50,
]
# PARAM_GRID["gaussiangraphicalmodel__base_learner__base_learner"] = [
#     GraphQUIC(),
#     GraphPgscps(),
# ]

# GMM outlier

PARAM_GRID["gmmoutlier__base_learner__method"] = ["quantile", "stddev"]
PARAM_GRID["gmmoutlier__base_learner__n_components"] = [1, 2, 3, 5, 10]
PARAM_GRID["gmmoutlier__base_learner__covariance_type"] = [
    "full",
    "tied",
    "diag",
    "spherical",
]
PARAM_GRID["gmmoutlier__base_learner__tol"] = [
    0.000001,
    0.000002,
    0.000003,
    0.00005,
    0.005,
]
PARAM_GRID["gmmoutlier__base_learner__reg_covar"] = [0.000005, 0.00005, 0.00005, 0.0005]
PARAM_GRID["gmmoutlier__base_learner__max_iter"] = [100, 200, 300]

# bayesianGMM outlier

PARAM_GRID["bayesiangmmoutlier__base_learner__method"] = ["quantile", "stddev"]
PARAM_GRID["bayesiangmmoutlier__base_learner__n_components"] = [1, 2, 3, 5, 10]
PARAM_GRID["bayesiangmmoutlier__base_learner__covariance_type"] = [
    "full",
    "tied",
    "diag",
    "spherical",
]
PARAM_GRID["bayesiangmmoutlier__base_learner__tol"] = [
    0.000001,
    0.000002,
    0.000003,
    0.00005,
    0.005,
]
PARAM_GRID["bayesiangmmoutlier__base_learner__reg_covar"] = [
    0.000005,
    0.00005,
    0.00005,
    0.0005,
]
PARAM_GRID["bayesiangmmoutlier__base_learner__max_iter"] = [100, 200, 300]

# CUSUM
PARAM_GRID["cumsum__base_learner__drift"] = [0.1, 0.2, 0.3, 0.5]

# kerneldensity
PARAM_GRID["kerneldensity__base_learner__algorithm"] = ["kd_tree", "ball_tree", "auto"]
PARAM_GRID["kerneldensity__base_learner__kernel"] = [
    "gaussian",
    "tophat",
    "epanechnikov",
    "exponential",
    "linear",
    "cosine",
]
PARAM_GRID["kerneldensity__base_learner__breadth_first"] = [True, False]
PARAM_GRID["kerneldensity__base_learner__leaf_size"] = [40, 50, 100, 200]

# GraphPgscps
PARAM_GRID["graphpgscps__base_learner__sparsity"] = [10, 20, 50, 100, 200, 400]
PARAM_GRID["graphpgscps__base_learner__reg"] = [0.1, 0.2, 0.4, 0.5, 0.7, 0.8, 0.9]


# Gaussian Mixture
PARAM_GRID["gaussianmixture__base_learner__n_components"] = [1, 2, 3, 5, 10]
PARAM_GRID["gaussianmixture__base_learner__covariance_type"] = [
    "full",
    "tied",
    "diag",
    "spherical",
]
PARAM_GRID["gaussianmixture__base_learner__init_params"] = ["kmeans", "random"]

# Bayesian Gaussian Mixture
PARAM_GRID["bayesiangaussianmixture__base_learner__n_components"] = [1, 2, 3, 5, 10]
PARAM_GRID["bayesiangaussianmixture__base_learner__covariance_type"] = [
    "full",
    "tied",
    "diag",
    "spherical",
]
PARAM_GRID["bayesiangaussianmixture__base_learner__init_params"] = ["kmeans", "random"]
PARAM_GRID["bayesiangaussianmixture__base_learner__random_state"] = [42]


# ************************************
# ******** Parameter Grid for GGM ****
# ************************************


# AnomalyGraphLasso
PARAM_GRID["anomalygraphlasso__base_learner__mode"] = ["cd", "lars"]
PARAM_GRID["anomalygraphlasso__base_learner__max_iter"] = [100, 300, 500, 1000]
PARAM_GRID["anomalygraphlasso__base_learner__alpha"] = [
    0.1,
    0.2,
    0.4,
    0.5,
    0.7,
    0.8,
    0.9,
    1.0,
]


# QuicGraphLasso
PARAM_GRID["quicgraphlasso__base_learner__lam"] = [0.1, 0.2, 0.4, 0.5, 0.7, 0.8, 0.9]
PARAM_GRID["quicgraphlasso__base_learner__max_iter"] = [100, 300, 500, 1000]
PARAM_GRID["quicgraphlasso__base_learner__init_method"] = ["cov", "corrcoef"]


# GGM_QUIC
PARAM_GRID["graphic_quic___base_learner__regularize_param"] = [0.1, 0.2, 0.3, 0.4, 0.5]
PARAM_GRID["graphic_quic___base_learner__beta"] = [0.05, 0.1, 0.5]
PARAM_GRID["graphic_quic___base_learner__sigma"] = [0.05, 0.1]
PARAM_GRID["graphic_quic___base_learner__tol"] = [
    0.000001,
    0.000002,
    0.000003,
    0.00005,
    0.005,
]
PARAM_GRID["graphic_quic___base_learner__inner_tol"] = [
    0.000001,
    0.000002,
    0.000003,
    0.00005,
    0.005,
]
PARAM_GRID["graphic_quic___base_learner__max_iter"] = [10, 20, 30, 50, 100, 200]
PARAM_GRID["graphic_quic___base_learner__max_Newton_iter"] = [10, 20, 30, 50, 100, 200]

