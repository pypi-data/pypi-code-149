# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Imputation Grid: Contains a dictionary of hyper-parameters for
imputation algorithms for time-series datasets.
"""

from sklearn.linear_model import (
    LinearRegression,
    ElasticNet,
    RidgeCV,
    LassoCV,
    BayesianRidge,
)
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from autoai_ts_libs.deps.srom.imputation.interpolators import PreMLImputer

PARAM_GRID = {}

# ************************************
# ******** Parameter Grid for Imputation of Time Series Datasets ****
# ************************************

# Imputation using K nearest neighbors
PARAM_GRID["knnimpute__n_neighbors"] = [1, 3, 5, 10, 20, 40, 70, 100]
PARAM_GRID["knnimpute__weights"] = ["uniform", "distance"]

# simple imputation
PARAM_GRID["simpleimputer__strategy"] = ["mean", "median", "most_frequent", "constant"]

# iterative imputer
PARAM_GRID["iterativeimputer__sample_posterior"] = [True, False]
PARAM_GRID["iterativeimputer__estimator"] = [
    BayesianRidge(),
    DecisionTreeRegressor(max_features="sqrt", random_state=0),
    ExtraTreesRegressor(n_estimators=10, random_state=0),
    ExtraTreesRegressor(n_estimators=40, random_state=0),
    ExtraTreesRegressor(n_estimators=100, random_state=0),
    KNeighborsRegressor(n_neighbors=15),
    KNeighborsRegressor(n_neighbors=30),
    KNeighborsRegressor(n_neighbors=45),
]
PARAM_GRID["iterativeimputer__max_iter"] = [1, 3, 5, 7, 10]
PARAM_GRID["iterativeimputer__imputation_order"] = [
    "ascending",
    "descending",
    "roman",
    "arabic",
    "random",
]
# Decomposition Imputers
# PCAImputer
PARAM_GRID["pcaimputer__svd_solver"] = ["auto", "full", "arpack", "randomized"]
PARAM_GRID["pcaimputer__n_components"] = [None, 3, 5, 10]
PARAM_GRID["pcaimputer__tol"] = [1e-5, 1e-4, 1e-2, 1e-1]
PARAM_GRID["pcaimputer__whiten"] = [True, False]
PARAM_GRID["pcaimputer__max_iter"] = [1, 14, 19]
PARAM_GRID["pcaimputer__order"] = [3, 5, 7]
PARAM_GRID["pcaimputer__base_imputer"] = [PreMLImputer()]
# KernelPCAImputer
PARAM_GRID["kernelpcaimputer__n_components"] = [None, 3, 5, 10]
PARAM_GRID["kernelpcaimputer__tol"] = [1e-5, 1e-4, 1e-2, 1e-1]
PARAM_GRID["kernelpcaimputer__max_iter"] = [1, 14, 19]
PARAM_GRID["kernelpcaimputer__kernel"] = [
    "linear",
    "poly",
    "rbf",
    "sigmoid",
    "cosine",
    "precomputed",
]
PARAM_GRID["kernelpcaimputer__order"] = [3, 5, 7]
PARAM_GRID["kernelpcaimputer__base_imputer"] = [PreMLImputer()]
# TruncatedSVDImputer
PARAM_GRID["truncatedsvdimputer__n_components"] = [None, 3, 5, 10]
PARAM_GRID["truncatedsvdimputer__tol"] = [1e-5, 1e-4, 1e-2, 1e-1]
PARAM_GRID["truncatedsvdimputer__max_iter"] = [1, 14, 19]
PARAM_GRID["truncatedsvdimputer__algorithm"] = ["arpack", "randomized"]
PARAM_GRID["truncatedsvdimputer__order"] = [3, 5, 7]
PARAM_GRID["truncatedsvdimputer__base_imputer"] = [PreMLImputer()]
# NMFImputer
PARAM_GRID["nmfimputer__n_components"] = [None, 3, 5, 10]
PARAM_GRID["nmfimputer__tol"] = [1e-5, 1e-4, 1e-2, 1e-1]
PARAM_GRID["nmfimputer__max_iter"] = [1, 14, 19]
PARAM_GRID["nmfimputer__l1_ratio"] = [0, 0.2, 0.5, 0.7, 1]
PARAM_GRID["nmfimputer__order"] = [3, 5, 7]
PARAM_GRID["nmfimputer__base_imputer"] = [PreMLImputer()]
# IncrementalPCAImputer
PARAM_GRID["incrementalpcaimputer__n_components"] = [None, 3, 5, 10]
PARAM_GRID["incrementalpcaimputer__tol"] = [1e-5, 1e-4, 1e-2, 1e-1]
PARAM_GRID["incrementalpcaimputer__max_iter"] = [1, 14, 19]
PARAM_GRID["incrementalpcaimputer__whiten"] = [True, False]
PARAM_GRID["incrementalpcaimputer__batch_size"] = [None, 5, 10, 20, 50]
PARAM_GRID["incrementalpcaimputer__order"] = [3, 5, 7]
PARAM_GRID["incrementalpcaimputer__base_imputer"] = [PreMLImputer()]

# Interpolators
PARAM_GRID["polynomialimputer__order"] = [1, 3, 5]
PARAM_GRID["splineimputer__order"] = [1, 3, 5]

# PredictiveImputer
PARAM_GRID["predictiveimputer__base_model"] = [
    BayesianRidge(),
    DecisionTreeRegressor(max_features="sqrt", random_state=0),
    ExtraTreesRegressor(n_estimators=10, random_state=0),
    ExtraTreesRegressor(n_estimators=40, random_state=0),
    ExtraTreesRegressor(n_estimators=100, random_state=0),
    KNeighborsRegressor(n_neighbors=15),
    KNeighborsRegressor(n_neighbors=30),
    KNeighborsRegressor(n_neighbors=45),
]
PARAM_GRID["predictiveimputer__tol"] = [1e-5, 1e-4, 1e-2, 1e-1]
PARAM_GRID["predictiveimputer__n_components"] = [3, 5, 10, None]
PARAM_GRID["predictiveimputer__max_iter"] = [1, 14, 19]
PARAM_GRID["predictiveimputer__order"] = [3, 5, 7]
PARAM_GRID["predictiveimputer__base_imputer"] = [PreMLImputer()]

# FlattenImputers
# FlattenIterativeImputer
PARAM_GRID["flatteniterativeimputer__order"] = [3, 5, 7]
PARAM_GRID["flatteniterativeimputer_model_imputer__sample_posterior"] = [True, False]
PARAM_GRID["flatteniterativeimputer_model_imputer__estimator"] = [
    BayesianRidge(),
    DecisionTreeRegressor(max_features="sqrt", random_state=0),
    ExtraTreesRegressor(n_estimators=10, random_state=0),
    ExtraTreesRegressor(n_estimators=40, random_state=0),
    ExtraTreesRegressor(n_estimators=100, random_state=0),
    KNeighborsRegressor(n_neighbors=15),
    KNeighborsRegressor(n_neighbors=30),
    KNeighborsRegressor(n_neighbors=45),
]
PARAM_GRID["flatteniterativeimputer_model_imputer__max_iter"] = [1, 3, 5, 7, 10]
PARAM_GRID["flatteniterativeimputer_model_imputer__imputation_order"] = [
    "ascending",
    "descending",
    "roman",
    "arabic",
    "random",
]
# FlattenKNNImputer
PARAM_GRID["flattenknnimputer__order"] = [3, 5, 7]
PARAM_GRID["flattenknnimputer__model_imputer__n_neighbors"] = [
    1,
    3,
    5,
    10,
    20,
    40,
    70,
    100,
]
PARAM_GRID["flattenknnimputer__model_imputer__weights"] = ["uniform", "distance"]
