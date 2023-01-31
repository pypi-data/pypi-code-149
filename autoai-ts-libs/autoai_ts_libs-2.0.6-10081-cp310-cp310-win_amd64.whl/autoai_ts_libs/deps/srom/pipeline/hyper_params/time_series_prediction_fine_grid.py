"""
Time Series Predicion Fine Grid.
"""
import numpy as np

PARAM_GRID = {}

# 01 LinearRegression
PARAM_GRID["LinearRegression__fit_intercept"] = [True, False]

# 02 DecisionTreeRegressor
PARAM_GRID["DecisionTreeRegressor__max_depth"] = list(range(1, 11))
PARAM_GRID["DecisionTreeRegressor__min_samples_split"] = list(range(2, 21))
PARAM_GRID["DecisionTreeRegressor__min_samples_leaf"] = list(range(1, 21))
PARAM_GRID["DecisionTreeRegressor__criterion"] = ["mse", "friedman_mse", "mae"]

# 03 MLPRegressor
PARAM_GRID["MLPRegressor__hidden_layer_sizes"] = [
    (10, 5),
    (50, 50, 50),
    (100, 100, 100),
    (5, 10),
]
PARAM_GRID["MLPRegressor__activation"] = ["identity", "logistic", "tanh", "relu"]
PARAM_GRID["MLPRegressor__solver"] = ["lbfgs", "sgd", "adam"]
PARAM_GRID["MLPRegressor__alpha"] = 10.0 ** (-np.arange(1, 4))

# 04 Linear SVR
PARAM_GRID["LinearSVR__epsilon"] = [1e-4, 1e-3, 1e-2, 1e-1, 1.0]
PARAM_GRID["LinearSVR__loss"] = ["epsilon_insensitive", "squared_epsilon_insensitive"]
PARAM_GRID["LinearSVR__dual"] = [True, False]
PARAM_GRID["LinearSVR__tol"] = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
PARAM_GRID["LinearSVR__C"] = [
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
PARAM_GRID["LinearSVR__fit_intercept"] = [True, False]

# 05 HuberRegressor
PARAM_GRID["HuberRegressor__epsilon"] = [1.1, 1.35, 1.5, 2.0]
PARAM_GRID["HuberRegressor__max_iter"] = [100, 300, 500]
PARAM_GRID["HuberRegressor__alpha"] = [0.000001, 0.001, 0.1, 1.0]
PARAM_GRID["HuberRegressor__fit_intercept"] = [True, False]
PARAM_GRID["HuberRegressor__tol"] = [0.000001, 0.00001, 0.0001, 0.001, 0.01]

# 06 RandomForestRegression
PARAM_GRID["RandomForestRegressor__n_estimators"] = [100, 500]
PARAM_GRID["RandomForestRegressor__criterion"] = ["mse", "friedman_mse", "mae"]
PARAM_GRID["RandomForestRegressor__min_samples_split"] = [2, 5, 10, 15, 20]
PARAM_GRID["RandomForestRegressor__min_samples_leaf"] = [1, 5, 10, 15, 20]
PARAM_GRID["RandomForestRegressor__bootstrap"] = [True, False]
PARAM_GRID["RandomForestRegressor__max_features"] = [
    0.1,
    0.25,
    0.5,
    0.75,
    1.0,
    "sqrt",
    "log2",
    None,
]

# 07 GradientBoostingClassifier
PARAM_GRID["GradientBoostingRegressor__n_estimators"] = [100, 500]
PARAM_GRID["GradientBoostingRegressor__loss"] = ["ls", "lad", "huber", "quantile"]
PARAM_GRID["GradientBoostingRegressor__learning_rate"] = [1e-3, 1e-2, 1e-1, 0.5, 1.0]
PARAM_GRID["GradientBoostingRegressor__max_depth"] = np.arange(1, 11, 3)
PARAM_GRID["GradientBoostingRegressor__min_samples_split"] = np.arange(2, 21, 3)
PARAM_GRID["GradientBoostingRegressor__min_samples_leaf"] = np.arange(1, 21, 3)
PARAM_GRID["GradientBoostingRegressor__subsample"] = np.arange(0.05, 1.01, 0.15)
PARAM_GRID["GradientBoostingRegressor__max_features"] = np.arange(0.05, 1.01, 0.15)
PARAM_GRID["GradientBoostingRegressor__alpha"] = [0.75, 0.8, 0.85, 0.9, 0.95, 0.99]

# XGBRegressor
PARAM_GRID["XGBRegressor__n_estimators"] = [100, 500]
PARAM_GRID["XGBRegressor__max_depth"] = [1, 2, 3, 4, 5, 10, 20, 50]
PARAM_GRID["XGBRegressor__subsample"] = [0.05, 0.2, 0.5, 0.7, 0.9, 1]
PARAM_GRID["XGBRegressor__min_child_weight"] = [0.01, 0.05, 1, 5, 10, 15, 20]
PARAM_GRID["XGBRegressor__nthread"] = [1]
PARAM_GRID["XGBRegressor__gamma"] = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 1.0, 1.5, 2, 5]
PARAM_GRID["XGBRegressor__colsample_bytree"] = [0.1, 0.3, 0.4, 0.5, 0.7, 0.8, 1.0]
PARAM_GRID["XGBRegressor__colsample_bylevel"] = [0.1, 0.3, 0.4, 0.5, 0.7, 0.8, 1.0]
PARAM_GRID["XGBRegressor__learning_rate"] = [
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
PARAM_GRID["XGBRegressor__booster"] = ["gbtree", "dart"]
PARAM_GRID["XGBRegressor__normalize_type"] = ["tree", "forest"]
PARAM_GRID["XGBRegressor__sample_type"] = ["uniform", "weighted"]
PARAM_GRID["XGBRegressor__reg_alpha"] = [0.000000001, 0.00001, 0.001, 0.1]
PARAM_GRID["XGBRegressor__reg_lambda"] = [0.000000001, 0.00001, 0.001, 0.1]
PARAM_GRID["XGBRegressor__rate_drop"] = [1e-10, 1e-5, 1e-1, 0.5, 0.75, 0.9999]

# Deep learning regressors

epoch_list = [10, 50, 100, 500, 1000]

PARAM_GRID["SimpleLSTMRegressor__epochs"] = epoch_list
PARAM_GRID["DeepLSTMRegressor__epochs"] = epoch_list
PARAM_GRID["SimpleCNNRegressor__epochs"] = epoch_list
PARAM_GRID["DeepCNNRegressor__epochs"] = epoch_list
PARAM_GRID["WaveNetRegressor__epochs"] = epoch_list
PARAM_GRID["SeriesNetRegressor__epochs"] = epoch_list
PARAM_GRID["DeepDNNRegressor__epochs"] = epoch_list
PARAM_GRID["DNNRegressor__epochs"] = epoch_list
