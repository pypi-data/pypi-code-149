# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Regression Fine Grid: Contains a dictionary of hyper-parameters of
regression algorithms.
"""
# important links
# TPOT - https://github.com/rhiever/tpot/blob/master/tpot/config/regressor.py
# HyperOpt https://github.com/hyperopt/hyperopt-sklearn/blob/master/hpsklearn/components.py
# AutoML - https://github.com/automl/auto-sklearn/tree/master/autosklearn/pipeline/components/regression

import numpy as np

PARAM_GRID = {}

# 1 ARDRegression
PARAM_GRID["ardregression__tol"] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
PARAM_GRID["ardregression__alpha_1"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
PARAM_GRID["ardregression__alpha_2"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
PARAM_GRID["ardregression__lambda_1"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
PARAM_GRID["ardregression__lambda_2"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
PARAM_GRID["ardregression__threshold_lambda"] = [1000, 10000, 100000]
PARAM_GRID["ardregression__fit_intercept"] = [True, False]

# 2 ElasticNetCV
PARAM_GRID["elasticnetcv__l1_ratio"] = np.arange(0.0, 1.01, 0.05)
PARAM_GRID["elasticnetcv__tol"] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]

# 3 DecisionTreeRegression
PARAM_GRID["decisiontreeregressor__max_depth"] = list(range(1, 11))
PARAM_GRID["decisiontreeregressor__min_samples_split"] = list(range(2, 21))
PARAM_GRID["decisiontreeregressor__min_samples_leaf"] = list(range(1, 21))
PARAM_GRID["decisiontreeregressor__criterion"] = ["mse", "friedman_mse", "mae"]

# 4 ExtraTreesRegression
PARAM_GRID["extratreesregressor__n_estimators"] = [100, 500]
PARAM_GRID["extratreesregressor__max_features"] = np.arange(0.05, 1.01, 0.05)
PARAM_GRID["extratreesregressor__min_samples_split"] = list(range(2, 21))
PARAM_GRID["extratreesregressor__min_samples_leaf"] = list(range(1, 21))
PARAM_GRID["extratreesregressor__bootstrap"] = [True, False]
PARAM_GRID["extratreesregressor__criterion"] = ["mse", "friedman_mse", "mae"]
PARAM_GRID["extratreesregressor__max_depth"] = [5, 10, None]

# 5 RandomForestRegression
PARAM_GRID["randomforestregressor__n_estimators"] = [100, 500]
PARAM_GRID["randomforestregressor__criterion"] = ["mse", "friedman_mse", "mae"]
PARAM_GRID["randomforestregressor__min_samples_split"] = [2, 5, 10, 15, 20]
PARAM_GRID["randomforestregressor__min_samples_leaf"] = [1, 5, 10, 15, 20]
PARAM_GRID["randomforestregressor__bootstrap"] = [True, False]
PARAM_GRID["randomforestregressor__max_features"] = [
    0.1,
    0.25,
    0.5,
    0.75,
    1.0,
    "sqrt",
    "log2",
    None,
]
# PARAM_GRID['randomforestregressor__min_impurity_decrease'] =  np.arange(0., 0.005, 0.00025)

# 6 GradientBoostingClassifier
PARAM_GRID["gradientboostingregressor__n_estimators"] = [100, 500]
PARAM_GRID["gradientboostingregressor__loss"] = ["ls", "lad", "huber", "quantile"]
PARAM_GRID["gradientboostingregressor__learning_rate"] = [1e-3, 1e-2, 1e-1, 0.5, 1.0]
PARAM_GRID["gradientboostingregressor__max_depth"] = np.arange(1, 11, 3)
PARAM_GRID["gradientboostingregressor__min_samples_split"] = np.arange(2, 21, 3)
PARAM_GRID["gradientboostingregressor__min_samples_leaf"] = np.arange(1, 21, 3)
PARAM_GRID["gradientboostingregressor__subsample"] = np.arange(0.05, 1.01, 0.15)
PARAM_GRID["gradientboostingregressor__max_features"] = np.arange(0.05, 1.01, 0.15)
PARAM_GRID["gradientboostingregressor__alpha"] = [0.75, 0.8, 0.85, 0.9, 0.95, 0.99]

# 7 KNeighborsRegression
PARAM_GRID["kneighborsregressor__n_neighbors"] = [1, 10, 20, 50, 70, 100]
PARAM_GRID["kneighborsregressor__weights"] = ["uniform", "distance"]
PARAM_GRID["kneighborsregressor__p"] = [1, 2]

# 8 LassoLarsCV
PARAM_GRID["lassolarscv__normalize"] = [True, False]
PARAM_GRID["lassolars__alpha"] = [1, 0.1, 0.01, 0.001]

# 9 Linear SVR
PARAM_GRID["linearsvr__epsilon"] = [1e-4, 1e-3, 1e-2, 1e-1, 1.0]
PARAM_GRID["linearsvr__loss"] = ["epsilon_insensitive", "squared_epsilon_insensitive"]
PARAM_GRID["linearsvr__dual"] = [True, False]
PARAM_GRID["linearsvr__tol"] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
PARAM_GRID["linearsvr__C"] = [
    1e-4,
    1e-3,
    1e-2,
    1e-1,
    0.5,
    1.0,
    5.0,
    10.0,
    15.0,
    20.0,
    25.0,
]
PARAM_GRID["linearsvr__fit_intercept"] = [True, False]

# 10 XGBRegression
PARAM_GRID["xgbregressor__n_estimators"] = [100, 500]
PARAM_GRID["xgbregressor__max_depth"] = [1, 2, 3, 4, 5, 10, 20, 50]
PARAM_GRID["xgbregressor__subsample"] = [0.05, 0.2, 0.5, 0.7, 0.9, 1]
PARAM_GRID["xgbregressor__min_child_weight"] = [0.01, 0.05, 1, 5, 10, 15, 20]
PARAM_GRID["xgbregressor__nthread"] = [1]
PARAM_GRID["xgbregressor__gamma"] = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 1.0, 1.5, 2, 5]
PARAM_GRID["xgbregressor__colsample_bytree"] = [0.1, 0.3, 0.4, 0.5, 0.7, 0.8, 1.0]
PARAM_GRID["xgbregressor__colsample_bylevel"] = [0.1, 0.3, 0.4, 0.5, 0.7, 0.8, 1.0]
PARAM_GRID["xgbregressor__learning_rate"] = [
    0.03,
    0.07,
    0.12,
    0.18,
    0.23,
    0.26,
    0.3,
    0.5,
    1.0,
]
PARAM_GRID["xgbregressor__booster"] = ["gbtree", "dart"]
PARAM_GRID["xgbregressor__normalize_type"] = ["tree", "forest"]
PARAM_GRID["xgbregressor__sample_type"] = ["uniform", "weighted"]
PARAM_GRID["xgbregressor__reg_alpha"] = [0.000000001, 0.00001, 0.001, 0.1]
PARAM_GRID["xgbregressor__reg_lambda"] = [0.000000001, 0.00001, 0.001, 0.1]
PARAM_GRID["xgbregressor__rate_drop"] = [1e-10, 1e-5, 1e-1, 0.5, 0.75, 0.9999]

# 11 SGDRegression
PARAM_GRID["sgdregressor__loss"] = [
    "squared_loss",
    "huber",
    "epsilon_insensitive",
    "squared_epsilon_insensitive",
]
PARAM_GRID["sgdregressor__penalty"] = ["none", "l2", "l1", "elasticnet"]
PARAM_GRID["sgdregressor__alpha"] = [1, 0.1, 0.01, 0.001]
PARAM_GRID["sgdregressor__l1_ratio"] = [0.5, 0.1, 0.01]
PARAM_GRID["sgdregressor__learning_rate"] = ["constant", "optimal", "invscaling"]
PARAM_GRID["sgdregressor__eta0"] = [0.1, 0.05, 0.01, 0.001, 0.0001]
PARAM_GRID["sgdregressor__fit_intercept"] = [False, True]
PARAM_GRID["sgdregressor__average"] = [False, True]
PARAM_GRID["sgdregressor__power_t"] = [0.0001, 0.001, 0.01, 0.25, 1.0]
PARAM_GRID["sgdregressor__epsilon"] = [0.0001, 0.001, 0.01, 0.05, 0.1]
PARAM_GRID["sgdregressor__tol"] = [0.0001, 0.001, 0.01, 0.05, 0.1]

# 12 SVR - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/SVC.py
PARAM_GRID["svr__C"] = [0.01, 0.1, 0.5, 1.0, 10.0, 50.0, 100.0]
PARAM_GRID["svr__gamma"] = [0.01, 0.1, 0.5, 1.0, 10.0, 50.0, 100.0, "auto"]
PARAM_GRID["svr__kernel"] = ["poly", "rbf", "sigmoid", "linear"]
PARAM_GRID["svr__degree"] = [2, 3, 4, 5]
PARAM_GRID["svr__coef0"] = [0.0, 0.1, 0.5, 1.0, 10.0, 50.0, 100.0]
PARAM_GRID["svr__epsilon"] = [0.001, 0.01, 0.05, 0.1]
PARAM_GRID["svr__tol"] = [0.0001, 0.001, 0.01, 0.05, 0.1]

# 13 MLP Regression
PARAM_GRID["mlpregressor__hidden_layer_sizes"] = [
    (10, 5),
    (50, 50, 50),
    (100, 100, 100),
    (5, 10),
]
PARAM_GRID["mlpregressor__activation"] = ["identity", "logistic", "tanh", "relu"]
PARAM_GRID["mlpregressor__solver"] = ["lbfgs", "sgd", "adam"]
PARAM_GRID["mlpregressor__alpha"] = 10.0 ** (-np.arange(1, 4))

# 14 PassiveAggressiveRegression
PARAM_GRID["passiveaggressiveregressor__fit_intercept"] = [True, False]
PARAM_GRID["passiveaggressiveregressor__C"] = [
    0.000001,
    0.00001,
    0.0001,
    0.001,
    0.01,
    0.1,
    0.5,
    1.0,
    10.0,
    50.0,
    100.0,
]
PARAM_GRID["passiveaggressiveregressor__loss"] = [
    "epsilon_insensitive",
    "squared_epsilon_insensitive",
]

# 15 AdaBoostRegression
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/adaboost.py
PARAM_GRID["adaboostregression__n_estimators"] = [50, 100, 200, 500]
PARAM_GRID["adaboostregression__learning_rate"] = [1e-3, 1e-2, 1e-1, 0.5, 1.0]
PARAM_GRID["adaboostregression__loss"] = ["linear", "square", "exponential"]
PARAM_GRID["adaboostregression__max_depth"] = list(range(1, 11))

# 16 KernelRedge
PARAM_GRID["kernelridge__alpha"] = [0.001, 0.0001]
PARAM_GRID["kernelridge__kernel"] = [
    "linear",
    "rbf",
    "laplacian",
    "polynomial",
    "chi2",
    "sigmoid",
]

# 17 Lasso
PARAM_GRID["lasso__alpha"] = [1, 0.1, 0.01, 0.001]

# 18 Ridge
PARAM_GRID["ridge__alpha"] = [10.0, 1, 0.1, 0.01, 0.001]
PARAM_GRID["ridge__fit_intercept"] = [True, False]
PARAM_GRID["ridge__tol"] = [0.0001, 0.001, 0.01, 0.1]

# 19 Baggingregressor
PARAM_GRID["baggingregressor__n_estimators"] = [50, 100]
PARAM_GRID["baggingregressor__bootstrap"] = ["True", "False"]
PARAM_GRID["baggingregressor__bootstrap_features"] = ["True", "False"]

# 20 LinearRegression
PARAM_GRID["linearregression__fit_intercept"] = [True, False]

# 21 deep nueral network
PARAM_GRID["kerasregressor__epochs"] = [10, 50, 100, 500, 1000]
PARAM_GRID["kerasregressor__batch_size"] = [10, 20, 40, 60, 80, 100]
PARAM_GRID["kerasregressor__optimizer"] = ["SGD", "RMSprop", "Adam"]
PARAM_GRID["kerasregressor__learn_rate"] = [0.001, 0.01, 0.1, 0.2, 0.3]
PARAM_GRID["kerasregressor__momentum"] = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9]
PARAM_GRID["kerasregressor__init_network_weight"] = [
    "uniform",
    "lecun_uniform",
    "normal",
    "zero",
    "glorot_normal",
    "glorot_uniform",
    "he_normal",
    "he_uniform",
]
PARAM_GRID["kerasregressor__neuron_activation"] = ["relu", "sigmoid"]
PARAM_GRID["kerasregressor__dropout_rate"] = [
    0.0,
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
PARAM_GRID["kerasregressor__neuron_in_layer1"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer2"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer3"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer4"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer5"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer6"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer7"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer8"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer9"] = [1, 5, 10, 15, 20, 25, 30]
PARAM_GRID["kerasregressor__neuron_in_layer10"] = [1, 5, 10, 15, 20, 25, 30]

# 22 partitionregressor
PARAM_GRID["partitionregressor__partition_model__max_depth"] = list(range(1, 11))
PARAM_GRID["partitionregressor__partition_model__min_samples_split"] = list(
    range(2, 21)
)
PARAM_GRID["partitionregressor__partition_model__min_samples_leaf"] = list(range(1, 21))
PARAM_GRID["partitionregressor__partition_model__criterion"] = [
    "mse",
    "friedman_mse",
    "mae",
]
PARAM_GRID["partitionregressor__regression_model__fit_intercept"] = [True, False]

# 23 PLS
PARAM_GRID["plsregression__n_components"] = [2, 5, 7, 10]
PARAM_GRID["plsregression__scale"] = [True, False]
PARAM_GRID["plsregression__max_iter"] = [100, 500, 750]
PARAM_GRID["plsregression__tol"] = [1e-06, 1e-03, 0.005, 0.01]

# 24 OMP
PARAM_GRID["orthogonalmatchingpursuit__n_nonzero_coefs"] = [None, 1, 5]
PARAM_GRID["orthogonalmatchingpursuit__tol"] = [1e-06, 1e-03, 0.005, 0.01]
PARAM_GRID["orthogonalmatchingpursuit__normalize"] = [True, False]
PARAM_GRID["orthogonalmatchingpursuit__fit_intercept"] = [True, False]

# 25 Multivariate Adaptive Regression
PARAM_GRID["multivariateadaptiveregression__max_degree"] = [1, 2, 3]
PARAM_GRID["multivariateadaptiveregression__base_model__max_terms"] = [
    10,
    25,
    50,
    100,
    200,
    400,
]
PARAM_GRID["multivariateadaptiveregression__base_model__penalty"] = [1, 3, 5, 7, 9]
PARAM_GRID["multivariateadaptiveregression__base_model__endspan_alpha"] = [
    0.005,
    0.01,
    0.05,
    0.1,
    0.3,
    0.5,
    0.9,
]
PARAM_GRID["multivariateadaptiveregression__base_model__minspan_alpha"] = [
    0.005,
    0.01,
    0.05,
    0.1,
    0.3,
    0.5,
    0.9,
]
PARAM_GRID["multivariateadaptiveregression__base_model__min_search_points"] = [
    10,
    50,
    100,
    200,
    300,
]
PARAM_GRID["multivariateadaptiveregression__base_model__fast_K"] = [
    10,
    50,
    100,
    200,
    300,
]
PARAM_GRID["multivariateadaptiveregression__base_model__fast_h"] = [
    10,
    50,
    100,
    200,
    300,
]

# 26 bayesianridge
PARAM_GRID["bayesianridge__n_iter"] = [100, 300, 500]
PARAM_GRID["bayesianridge__tol"] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
PARAM_GRID["bayesianridge__alpha_1"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
PARAM_GRID["bayesianridge__alpha_2"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
PARAM_GRID["bayesianridge__lambda_1"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
PARAM_GRID["bayesianridge__lambda_2"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]
PARAM_GRID["bayesianridge__fit_intercept"] = [True, False]
PARAM_GRID["bayesianridge__normalize"] = [True, False]

# 27 isotonic
PARAM_GRID["isotonic__increasing"] = [True, False]

# 28 Huberregressor
PARAM_GRID["huberregressor__epsilon"] = [1.1, 1.35, 1.5, 2.0]
PARAM_GRID["huberregressor__max_iter"] = [100, 300, 500]
PARAM_GRID["huberregressor__alpha"] = [0.000001, 0.001, 0.1, 1.0]
PARAM_GRID["huberregressor__fit_intercept"] = [True, False]
PARAM_GRID["huberregressor__tol"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]

# 29 theilsenregressor
PARAM_GRID["theilsenregressor__fit_intercept"] = [True, False]
PARAM_GRID["theilsenregressor__max_iter"] = [100, 300, 500]
PARAM_GRID["theilsenregressor__tol"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]

# 30 RANSACRegressor
# no parameter

# 31 gaussianprocessregressor
# no parameter

PARAM_GRID["nmf__l1_ratio"] = [0, 0.2, 0.5, 0.7, 1]
PARAM_GRID["nmf__tol"] = [1e-5, 1e-4, 1e-2, 1e-1]
PARAM_GRID["nmf__n_components"] = [3, 5, 10, None]

# feature processing
# pca
PARAM_GRID["pca__svd_solver"] = ["auto", "full", "randomized"]
PARAM_GRID["pca__n_components"] = [None, 3, 5]

# fastica
PARAM_GRID["fastica__n_components"] = [None, 3, 5, 10]
PARAM_GRID["fastica__algorithm"] = ["parallel", "deflation"]
PARAM_GRID["fastica__whiten"] = ["False", "True"]
PARAM_GRID["fastica__fun"] = ["logcosh", "exp", "cube"]

# kernelpca
PARAM_GRID["kernelpca__kernel"] = ["linear", "poly", "rbf", "sigmoid", "cosine"]
PARAM_GRID["kernelpca__n_components"] = [None, 3, 5, 10]
PARAM_GRID["kernelpca__coef0"] = [-1.0, -0.75, -0.50, -0.25, 0.0, 0.25, 0.50, 0.75, 1.0]
PARAM_GRID["kernelpca__gamma"] = [0.0001, 0.001, 0.01, 1.0, 2.0]
PARAM_GRID["kernelpca__degree"] = [2, 3, 4, 5]

# Nystroem
PARAM_GRID["nystroem__kernel"] = ["poly", "rbf", "sigmoid", "cosine"]
PARAM_GRID["nystroem__n_components"] = [5, 10, 20]
PARAM_GRID["nystroem__gamma"] = [0.0001, 0.01, 0.1, 1.0]
PARAM_GRID["nystroem__degree"] = [2, 3, 4, 5]

# selectkbest
PARAM_GRID["selectkbest__k"] = [1, 3, 5, 10]

# variancethreshold
PARAM_GRID["variancethreshold__threshold"] = [0.0, 0.01, 0.05, 0.1]

# lowvariancefeatureelimination
PARAM_GRID["lowvariancefeatureelimination__var_threshold_value"] = [
    0.0,
    0.01,
    0.05,
    0.1,
]

# feature post processing
PARAM_GRID["kbinsdiscretizer__n_bins"] = [3, 5, 7, 9]
PARAM_GRID["kbinsdiscretizer__encode"] = ["onehot-dense", "ordinal"]
PARAM_GRID["kbinsdiscretizer__strategy"] = ["uniform", "quantile", "kmeans"]

# polynomial features
PARAM_GRID["polynomialfeatures__degree"] = [2, 3]
PARAM_GRID["polynomialfeatures__interaction_only"] = [True, False]

# onehot
PARAM_GRID["onehotencoder__categories"] = ["auto"]
PARAM_GRID["onehotencoder__sparse"] = ["False"]

# powertransformer
PARAM_GRID["powertransformer__method"] = ["yeo-johnson", "box-cox"]
PARAM_GRID["powertransformer__standardize"] = ["True", "False"]

# normalizer
PARAM_GRID["normalizer__norm"] = ["l1", "l2", "max"]

# RandomTreesEmbedding
PARAM_GRID["randomtreesembedding__n_estimators"] = [10, 30, 50, 70, 100]
PARAM_GRID["randomtreesembedding__max_depth"] = [2, 5, 7, 10]
PARAM_GRID["randomtreesembedding__min_samples_split"] = [2, 6, 10, 15, 20]
PARAM_GRID["randomtreesembedding__min_samples_leaf"] = [2, 6, 10, 15, 20]

# selectpercentile
from sklearn.feature_selection import f_regression, mutual_info_regression

PARAM_GRID["selectpercentile__percentile"] = [1, 20, 50, 70, 90]
PARAM_GRID["selectpercentile__score_func"] = [f_regression, mutual_info_regression]

# truncated SVD
PARAM_GRID["truncatedsvd__n_components"] = [2, 5, 10]

# feature agglomeration
PARAM_GRID["featureagglomeration__n_clusters"] = [2, 5, 10, 30, 50]
PARAM_GRID["featureagglomeration__affinity"] = ["euclidean", "manhattan", "cosine"]
PARAM_GRID["featureagglomeration__linkage"] = ["ward", "complete", "average"]
PARAM_GRID["featureagglomeration__pooling_func"] = ["mean", "median", "max"]

# standardscaler
PARAM_GRID["standardscaler__with_mean"] = ["True", "False"]
PARAM_GRID["standardscaler__with_std"] = ["True", "False"]

PARAM_GRID["rbfsampler__gamma"] = [0.00001, 0.001, 0.01, 0.1, 0.5, 1.0]
PARAM_GRID["rbfsampler__n_components"] = [50, 100, 200]

PARAM_GRID["skewedchi2sampler__n_components"] = [50, 100, 200]

PARAM_GRID["sparsepca__n_components"] = [None, 5, 10]
PARAM_GRID["sparsepca__alpha"] = [1.0, 2.0, 0.5]
PARAM_GRID["sparsepca__ridge_alpha"] = [0.01, 0.5, 1.0]
PARAM_GRID["sparsepca__method"] = ["lars", "cd"]

PARAM_GRID["isomap__n_neighbors"] = [2, 5, 10]
PARAM_GRID["isomap__n_components"] = [2, 5, 10]
PARAM_GRID["isomap__eigen_solver"] = ["auto", "arpack", "dense"]
PARAM_GRID["isomap__path_method"] = ["auto", "FW", "D"]

PARAM_GRID["locallylinearembedding__n_neighbors"] = [2, 5, 10]
PARAM_GRID["locallylinearembedding__n_components"] = [2, 5, 10]
PARAM_GRID["locallylinearembedding__reg"] = [0.001, 0.01, 0.1]
PARAM_GRID["locallylinearembedding__eigen_solver"] = ["auto", "arpack", "dense"]

PARAM_GRID["mds__n_components"] = [2, 5, 10]
PARAM_GRID["mds__metric"] = [True, False]

PARAM_GRID["spectralembedding__n_components"] = [2, 5, 10]
PARAM_GRID["spectralembedding__affinity"] = ["nearest_neighbors", "rbf"]
PARAM_GRID["spectralembedding__eigen_solver"] = [None, "arpack", "lobpcg", "amg"]

PARAM_GRID["tsne__n_components"] = [2, 5, 10]
PARAM_GRID["tsne__learning_rate"] = [10.0, 100.0, 200.0, 1000.0]

PARAM_GRID["selectfrommodel__extratreesregressor__n_estimators"] = [10, 50, 100]
PARAM_GRID["selectfrommodel__extratreesregressor__criterion"] = [
    "mse",
    "friedman_mse",
    "mae",
]
PARAM_GRID["selectfrommodel__extratreesregressor__max_features"] = [
    0.1,
    0.3,
    0.5,
    0.7,
    1.0,
]
PARAM_GRID["selectfrommodel__extratreesregressor__min_samples_split"] = [
    2,
    5,
    10,
    15,
    20,
]
PARAM_GRID["selectfrommodel__extratreesregressor__min_samples_leaf"] = [
    1,
    5,
    10,
    15,
    20,
]
PARAM_GRID["selectfrommodel__extratreesregressor__bootstrap"] = ["True", "False"]

### LGBM REGRESSOR
PARAM_GRID["lightGBM__boosting_type"] = ["gbdt", "goss", "dart"]
PARAM_GRID["lightGBM__num_leaves"] = list(range(20, 150))
PARAM_GRID["lightGBM__learning_rate"] = list(
    np.logspace(np.log10(0.005), np.log10(0.5), base=10, num=1000)
)
PARAM_GRID["lightGBM__subsample_for_bin"] = list(range(20000, 300000, 20000))
PARAM_GRID["lightGBM__min_child_samples"] = list(range(20, 500, 5))
PARAM_GRID["lightGBM__reg_alpha"] = list(np.linspace(0, 1))
# PARAM_GRID["lightGBM__reg_lambda"] = list(np.linspace(0, 1)),
PARAM_GRID["lightGBM__colsample_bytree"] = list(np.linspace(0.6, 1, 10))
PARAM_GRID["lightGBM__subsample"] = list(np.linspace(0.5, 1, 100))
PARAM_GRID["lightGBM__is_unbalance"] = [True, False]
