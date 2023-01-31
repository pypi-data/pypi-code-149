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

# 1 ADRRegression
PARAM_GRID["adrregression__tol"] = (1e-5, 1e-1)
PARAM_GRID["adrregression__alpha_1"] = (0.000001, 0.01)
PARAM_GRID["adrregression__alpha_2"] = (0.000001, 0.01)
PARAM_GRID["adrregression__lambda_1"] = (0.000001, 0.01)
PARAM_GRID["adrregression__lambda_2"] = (0.000001, 0.01)
PARAM_GRID["adrregression__threshold_lambda"] = (1000, 100000)

# 2 ElasticNetCV
PARAM_GRID["elasticnetcv__l1_ratio"] = (0.0, 1.0)
PARAM_GRID["elasticnetcv__tol"] = (1e-5, 1e-1)

# 3 DecisionTreeRegression
PARAM_GRID["decisiontreeregressor__max_depth"] = (1, 11)
PARAM_GRID["decisiontreeregressor__min_samples_split"] = (2, 21)
PARAM_GRID["decisiontreeregressor__min_samples_leaf"] = (1, 21)
PARAM_GRID["decisiontreeregressor__criterion"] = ["mse", "friedman_mse", "mae"]

# 4 ExtraTreesRegression
PARAM_GRID["extratreesregressor__n_estimators"] = (10, 500)
PARAM_GRID["extratreesregressor__max_features"] = (0.05, 1.0)
PARAM_GRID["extratreesregressor__min_samples_split"] = (2, 21)
PARAM_GRID["extratreesregressor__min_samples_leaf"] = (1, 21)
PARAM_GRID["extratreesregressor__bootstrap"] = [True, False]
PARAM_GRID["extratreesregressor__criterion"] = ["mse", "mae"]
PARAM_GRID["extratreesregressor__max_depth"] = (3, 10)

# 5 RandomForestRegression
PARAM_GRID["randomforestregressor__n_estimators"] = (10, 500)
PARAM_GRID["randomforestregressor__criterion"] = ["mse", "mae"]
PARAM_GRID["randomforestregressor__min_samples_split"] = (2, 20)
PARAM_GRID["randomforestregressor__min_samples_leaf"] = (1, 20)
PARAM_GRID["randomforestregressor__bootstrap"] = [True, False]
PARAM_GRID["randomforestregressor__max_features"] = (0.1, 0.99)
# PARAM_GRID['randomforestregressor__min_impurity_decrease'] =  (0., 0.005)

# 6 GradientBoostingClassifier
PARAM_GRID["gradientboostingregressor__n_estimators"] = (10, 500)
PARAM_GRID["gradientboostingregressor__loss"] = ["ls", "lad", "huber", "quantile"]
PARAM_GRID["gradientboostingregressor__learning_rate"] = (1e-3, 1.0)
PARAM_GRID["gradientboostingregressor__max_depth"] = (1, 11)
PARAM_GRID["gradientboostingregressor__min_samples_split"] = (2, 21)
PARAM_GRID["gradientboostingregressor__min_samples_leaf"] = (1, 21)
PARAM_GRID["gradientboostingregressor__subsample"] = (0.05, 1.0)
PARAM_GRID["gradientboostingregressor__max_features"] = (0.05, 1.0)
PARAM_GRID["gradientboostingregressor__alpha"] = (0.75, 0.99)

# 7 KNeighborsRegression
PARAM_GRID["kneighborsregressor__n_neighbors"] = (1, 100)
PARAM_GRID["kneighborsregressor__weights"] = ["uniform", "distance"]
PARAM_GRID["kneighborsregressor__p"] = (1, 2)

# 8 LassoLarsCV
PARAM_GRID["lassolarscv__normalize"] = [True, False]
PARAM_GRID["lassolars__alpha"] = (0.001, 1)

# 9 Linear SVR
PARAM_GRID["linearsvr__epsilon"] = (1e-4, 1.0)
PARAM_GRID["linearsvr__loss"] = ["epsilon_insensitive", "squared_epsilon_insensitive"]
PARAM_GRID["linearsvr__dual"] = [True, False]
PARAM_GRID["linearsvr__tol"] = (1e-5, 1e-1)
PARAM_GRID["linearsvr__C"] = (1e-4, 25.0)

# 10 XGBRegression
PARAM_GRID["xgbregressor__n_estimators"] = (10, 500)
PARAM_GRID["xgbregressor__max_depth"] = (1, 50)
PARAM_GRID["xgbregressor__subsample"] = (0.05, 1)
PARAM_GRID["xgbregressor__min_child_weight"] = (1, 20)
PARAM_GRID["xgbregressor__nthread"] = (1, 1)
PARAM_GRID["xgbregressor__gamma"] = (0.0, 5.0)
PARAM_GRID["xgbregressor__colsample_bytree"] = (0.3, 1.0)
PARAM_GRID["xgbregressor__learning_rate"] = (0.01, 1.0)

# 11 SGDRegression
PARAM_GRID["sgdregressor__loss"] = [
    "squared_loss",
    "huber",
    "epsilon_insensitive",
    "squared_epsilon_insensitive",
]
PARAM_GRID["sgdregressor__penalty"] = ["none", "l2", "l1", "elasticnet"]
PARAM_GRID["sgdregressor__alpha"] = (0.001, 1)
PARAM_GRID["sgdregressor__l1_ratio"] = (0.01, 1.0)
PARAM_GRID["sgdregressor__learning_rate"] = ["constant", "optimal", "invscaling"]
PARAM_GRID["sgdregressor__eta0"] = (0.0001, 0.01)

# 12 SVR - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/SVC.py
PARAM_GRID["svr__C"] = (0.01, 100.0)
PARAM_GRID["svr__gamma"] = (0.01, 100.0)
PARAM_GRID["svr__kernel"] = ["poly", "rbf", "sigmoid"]
PARAM_GRID["svr__degree"] = (2, 3)
PARAM_GRID["svr__coef0"] = (0.0, 100.0)

# 13 MLP Regression
# PARAM_GRID['mlpregressor__hidden_layer_sizes'] = [(50, 50, 50), (100, 100, 100)]
PARAM_GRID["mlpregressor__activation"] = ["identity", "logistic", "tanh", "relu"]
PARAM_GRID["mlpregressor__solver"] = ["lbfgs", "sgd", "adam"]
PARAM_GRID["mlpregressor__alpha"] = (0.0001, 0.1)

# 14 PassiveAggressiveRegression
PARAM_GRID["passiveaggressiveregressor__fit_intercept"] = [True, False]
PARAM_GRID["passiveaggressiveregressor__C"] = (0.000001, 100.0)
PARAM_GRID["passiveaggressiveregressor__loss"] = [
    "epsilon_insensitive",
    "squared_epsilon_insensitive",
]

# 15 AdaBoostRegression
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/adaboost.py
PARAM_GRID["adaboostregression__n_estimators"] = (10, 500)
PARAM_GRID["adaboostregression__learning_rate"] = (1e-3, 1.0)
PARAM_GRID["adaboostregression__loss"] = ["linear", "square", "exponential"]
PARAM_GRID["adaboostregression__max_depth"] = (1, 11)

# 16 KernelRedge
PARAM_GRID["kernelridge__alpha"] = (0.000001, 0.001)
PARAM_GRID["kernelridge__kernel"] = [
    "linear",
    "rbf",
    "laplacian",
    "polynomial",
    "chi2",
    "sigmoid",
]

# 17 Lasso
PARAM_GRID["lasso__alpha"] = (0.001, 1)

# 18 Ridge
PARAM_GRID["ridge__alpha"] = (0.001, 1)

# 19
PARAM_GRID["baggingregressor__n_estimators"] = (50, 100)
PARAM_GRID["baggingregressor__bootstrap"] = ["True", "False"]
PARAM_GRID["baggingregressor__bootstrap_features"] = ["True", "False"]

# 20 LinearRegression
PARAM_GRID["linearregression__fit_intercept"] = [True, False]

# 21 deep nueral network
PARAM_GRID["kerasregressor__epochs"] = (10, 1000)
PARAM_GRID["kerasregressor__batch_size"] = (10, 100)
PARAM_GRID["kerasregressor__optimizer"] = ["SGD", "RMSprop", "Adam"]
PARAM_GRID["kerasregressor__learn_rate"] = (0.001, 0.3)
PARAM_GRID["kerasregressor__momentum"] = (0.0, 0.9)
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
PARAM_GRID["kerasregressor__dropout_rate"] = (0.0, 0.9)
PARAM_GRID["kerasregressor__neuron_in_layer1"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer2"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer3"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer4"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer5"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer6"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer7"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer8"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer9"] = (1, 30)
PARAM_GRID["kerasregressor__neuron_in_layer10"] = (1, 30)

# 22 partitionregressor
PARAM_GRID["partitionregressor__partition_model__max_depth"] = (1, 11)
PARAM_GRID["partitionregressor__partition_model__min_samples_split"] = (2, 21)
PARAM_GRID["partitionregressor__partition_model__min_samples_leaf"] = (1, 21)
PARAM_GRID["partitionregressor__partition_model__criterion"] = [
    "mse",
    "friedman_mse",
    "mae",
]
PARAM_GRID["partitionregressor__regression_model__fit_intercept"] = [True, False]

# 23 PLS
PARAM_GRID["plsregression__n_components"] = (2, 10)
PARAM_GRID["plsregression__scale"] = [True, False]
PARAM_GRID["plsregression__max_iter"] = (100, 750)
PARAM_GRID["plsregression__tol"] = (1e-06, 0.01)

# 24 OMP
PARAM_GRID["orthogonalmatchingpursuit__n_nonzero_coefs"] = (1, 10)
PARAM_GRID["orthogonalmatchingpursuit__tol"] = (1e-06, 0.01)
PARAM_GRID["orthogonalmatchingpursuit__normalize"] = [True, False]
PARAM_GRID["orthogonalmatchingpursuit__fit_intercept"] = [True, False]

# 25 MAdaptive Regression
PARAM_GRID["multivariateadaptiveregression__max_terms"] = (2, 10)
PARAM_GRID["multivariateadaptiveregression__max_degree"] = (1, 3)
PARAM_GRID["multivariateadaptiveregression__penalty"] = (1, 4)

# 26 bayesianridge
PARAM_GRID["bayesianridge__n_iter"] = (100, 500)
PARAM_GRID["bayesianridge__tol"] = (1e-5, 1e-1)
PARAM_GRID["bayesianridge__alpha_1"] = (0.000001, 0.01)
PARAM_GRID["bayesianridge__alpha_2"] = (0.000001, 0.01)
PARAM_GRID["bayesianridge__lambda_1"] = (0.000001, 0.01)
PARAM_GRID["bayesianridge__lambda_2"] = (0.000001, 0.01)
PARAM_GRID["bayesianridge__fit_intercept"] = [True, False]
PARAM_GRID["bayesianridge__normalize"] = [True, False]

# 27 isotonic
PARAM_GRID["bayesianridge__increasing"] = [True, False]

# 28 Huberregressor
PARAM_GRID["huberregressor__epsilon"] = (1.1, 2.0)
PARAM_GRID["huberregressor__max_iter"] = (100, 500)
PARAM_GRID["huberregressor__alpha"] = (0.000001, 1.0)
PARAM_GRID["huberregressor__fit_intercept"] = [True, False]
PARAM_GRID["huberregressor__tol"] = (0.000001, 0.01)

# 29 theilsenregressor
PARAM_GRID["theilsenregressor__fit_intercept"] = [True, False]
PARAM_GRID["theilsenregressor__max_iter"] = (100, 500)
PARAM_GRID["theilsenregressor__tol"] = (0.000001, 0.01)

# 30 RANSACRegressor
# no parameter

# 31 gaussianprocessregressor
# no parameter

### LGBM REGRESSOR
PARAM_GRID["lightGBM__boosting_type"] = ["gbdt", "goss", "dart"]
PARAM_GRID["lightGBM__num_leaves"] = (20, 150)
PARAM_GRID["lightGBM__learning_rate"] = (0.001, 0.3)
PARAM_GRID["lightGBM__subsample_for_bin"] = (20000, 300000)
PARAM_GRID["lightGBM__min_child_samples"] = (20, 500)
# PARAM_GRID["lightGBM__reg_alpha"] = list(np.linspace(0, 1))
# PARAM_GRID["lightGBM__reg_lambda"] = list(np.linspace(0, 1)),
# PARAM_GRID["lightGBM__colsample_bytree"] = list(np.linspace(0.6, 1, 10))
# PARAM_GRID["lightGBM__subsample"] = list(np.linspace(0.5, 1, 100))
PARAM_GRID["lightGBM__is_unbalance"] = [True, False]
