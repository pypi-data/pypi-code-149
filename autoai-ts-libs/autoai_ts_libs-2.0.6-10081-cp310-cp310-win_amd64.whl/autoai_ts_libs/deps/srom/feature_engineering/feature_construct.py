# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: feature_construct
   :synopsis: Contains implementation for feature based preprocessing.

.. moduleauthor:: SROM Team
"""

import numpy as np
import pandas as pd
from itertools import combinations, product
from sklearn.preprocessing import StandardScaler
import logging

LOGGER = logging.getLogger(__name__)

try:
    import sympy
except ImportError:
    LOGGER.error("ImportError in feature_construct.py : sympy is not installed ")

transformations_rule_dict = {
    "exp": lambda x: np.all(x < 10),
    "exp-": lambda x: np.all(-x < 10),
    "log": lambda x: np.all(x >= 0),
    "abs": lambda x: np.any(x < 0),
    "sqrt": lambda x: np.all(x >= 0),
    "sin": lambda x: True,
    "cos": lambda x: True,
    "2^": lambda x: np.all(x < 50),
    "^2": lambda x: np.all(np.abs(x) < 1000000),
    "^3": lambda x: np.all(np.abs(x) < 10000),
    "1+": lambda x: True,
    "1-": lambda x: True,
    "1/": lambda x: np.all(x != 0),
}

func_transform = {
    "exp": lambda x: np.exp(x),
    "exp-": lambda x: np.exp(-x),
    "log": lambda x: np.log(x),
    "abs": lambda x: np.Abs(x),
    "sqrt": lambda x: np.sqrt(x),
    "sin": lambda x: np.sin(x),
    "cos": lambda x: np.cos(x),
    "2^": lambda x: 2 ** x,
    "^2": lambda x: x ** 2,
    "^3": lambda x: x ** 3,
    "1+": lambda x: 1 + x,
    "1-": lambda x: 1 - x,
    "1/": lambda x: 1 / x,
}

func_transform_expression = {
    "exp": lambda x: "exp(" + str(x) + ")",
    "exp-": lambda x: "exp(-" + str(x) + ")",
    "log": lambda x: "log(" + str(x) + ")",
    "abs": lambda x: "Abs(" + str(x) + ")",
    "sqrt": lambda x: "Sqrt(" + str(x) + ")",
    "sin": lambda x: "Sin(" + str(x) + ")",
    "cos": lambda x: "Cos(" + str(x) + ")",
    "2^": lambda x: "2 ** " + str(x),
    "^2": lambda x: str(x) + " ** 2",
    "^3": lambda x: str(x) + " ** 3",
    "1+": lambda x: "1 + " + str(x),
    "1-": lambda x: "1 - " + str(x),
    "1/": lambda x: "1 / " + str(x),
}

func_combinations = {
    "x+y": lambda x, y: x + y,
    "x*y": lambda x, y: x * y,
    "x-y": lambda x, y: x - y,
    "y-x": lambda x, y: y - x,
    "y/x": lambda x, y: y / x,
    "x/y": lambda x, y: x / y,
}

func_combinations_expression = {
    "x+y": lambda x, y: str(x) + " + " + str(y),
    "x*y": lambda x, y: str(x) + " * " + str(y),
    "x-y": lambda x, y: str(x) + " - " + str(y),
    "y-x": lambda x, y: str(y) + " - " + str(x),
    "y/x": lambda x, y: str(y) + " / " + str(x),
    "x/y": lambda x, y: str(x) + " / " + str(y),
}


combination_rule_dict = {
    "x+y": lambda x, y: True,
    "x*y": lambda x, y: True,
    "x-y": lambda x, y: True,
    "y-x": lambda x, y: True,
    "y/x": lambda x, y: np.all(x != 0),
    "x/y": lambda x, y: np.all(y != 0),
}

rolling_transform = {
    "mean": lambda x, win: pd.Series.rolling(x, win).mean().ffill().bfill(),
    "median": lambda x, win: pd.Series.rolling(x, win).median().ffill().bfill(),
}

rolling_transform_expression = {
    "mean": lambda x, win: "mean(" + str(x) + "," + str(win) + ")",
    "median": lambda x, win: "median(" + str(x) + "," + str(win) + ")",
}

rolling_transform_param = {
    "win": [1, 4, 7],
}


def construct_transformation_feature():
    """
    Function to create a transformation
    """
    pass


def construct_combination_feature():
    """
    Function to create a combination
    """
    pass


def construct_ts_rolling_feature():
    """
    Function to create a transformation
    """
    pass


def construct_features(
    df,
    transformation=("1/", "exp", "log", "abs", "sqrt", "^2", "^3"),
    combination=("x+y", "x-y", "x*y", "y-x", "y/x", "x/y"),
    rolling=("mean", "median"),
    max_steps=3,
    feature_to_start_with=None,
    correlation_threshold=0.95,
):
    """
    This function will output the new dataframe:
    1. transformation on each columns and append as new column
    2. combination on pair of columns
    """
    exploration_pool = {}

    X = df.copy()
    if feature_to_start_with:
        original_features = feature_to_start_with
    else:
        original_features = list(X.columns)

    cat_features = {feat for feat in original_features if len(X[feat].unique()) <= 2}
    features_list = [feat for feat in original_features if feat not in cat_features]

    # add the original features into exploration_pool
    for item in original_features:
        exploration_pool[item] = item

    # step 1: operate on original data :
    # a) start trasnformation
    # b) start combination
    # c) start rolloing summary
    step = 1

    new_transform_features = []
    new_combination_features = []
    new_rolling_features = []

    # apply transformation
    for _, feat in enumerate(features_list):
        for ft in transformation:
            f_name = str(
                sympy.sympify(str(func_transform_expression[ft](sympy.symbols(feat))))
            )
            if f_name in exploration_pool:
                continue
            else:
                exploration_pool[f_name] = str(
                    func_transform_expression[ft](sympy.symbols(feat))
                )
            if transformations_rule_dict[ft](X[feat]):
                new_feat = func_transform[ft](X[feat])
                if np.isfinite(new_feat).all() and np.var(new_feat) > 1e-10:
                    corr = abs(np.corrcoef(new_feat, X[feat])[0, 1])
                    if corr < correlation_threshold:
                        X[f_name] = new_feat
                        new_transform_features.append(f_name)

    # apply combination
    feature_tuples = (
        list(combinations(features_list, 2))
        # + list(combinations(new_transform_features, 2))
        # + list(product(features_list, new_transform_features))
    )
    for _, (feat1, feat2) in enumerate(feature_tuples):
        for fc in combination:
            f_name = str(
                sympy.sympify(
                    str(
                        func_combinations_expression[fc](
                            sympy.symbols(feat1), sympy.symbols(feat2)
                        )
                    )
                )
            )
            if f_name in exploration_pool:
                continue
            else:
                exploration_pool[f_name] = str(
                    func_combinations_expression[fc](
                        sympy.symbols(feat1), sympy.symbols(feat2)
                    )
                )

            if combination_rule_dict[fc](X[feat1], X[feat2]):
                new_feat = func_combinations[fc](X[feat1], X[feat2])
                if np.isfinite(new_feat).all() and np.var(new_feat) > 1e-10:
                    corr1 = abs(np.corrcoef(new_feat, X[feat1])[0, 1])
                    corr2 = abs(np.corrcoef(new_feat, X[feat2])[0, 1])
                    corr = max(abs(corr1), abs(corr2))
                    if corr < correlation_threshold:
                        X[f_name] = new_feat
                        new_combination_features.append(f_name)

    # apply rolling aggregtes, with shift
    for _, feat in enumerate(features_list):
        for rt in rolling:
            for rt_param in rolling_transform_param["win"]:
                f_name = rolling_transform_expression[rt](feat, rt_param)
                new_feat = rolling_transform[rt](X[feat], rt_param)
                X[f_name] = new_feat
                new_rolling_features.append(f_name)

    if step >= max_steps:
        return X
    step += 1

    new_round_features = (
        new_transform_features + new_combination_features + new_rolling_features
    )
    cat_features = {feat for feat in new_round_features if len(X[feat].unique()) <= 2}
    features_list = [feat for feat in new_round_features if feat not in cat_features]

    new_transform_features = []
    new_combination_features = []
    new_rolling_features = []

    # apply transformation
    for _, feat in enumerate(features_list):
        for ft in transformation:
            f_name = str(sympy.sympify(str(func_transform_expression[ft](feat))))
            if f_name in exploration_pool:
                continue
            else:
                exploration_pool[f_name] = str(
                    func_transform_expression[ft](sympy.symbols(feat))
                )
            if transformations_rule_dict[ft](X[feat]):
                new_feat = func_transform[ft](X[feat])
                if np.isfinite(new_feat).all() and np.var(new_feat) > 1e-10:
                    corr = abs(np.corrcoef(new_feat, X[feat])[0, 1])
                    if corr < correlation_threshold:
                        X[f_name] = new_feat
                        new_transform_features.append(f_name)

    # apply combination
    feature_tuples = list(combinations(features_list, 2))
    for _, (feat1, feat2) in enumerate(feature_tuples):
        for fc in combination:
            f_name = str(
                sympy.sympify(
                    str(
                        func_combinations_expression[fc](
                            sympy.symbols(feat1), sympy.symbols(feat2)
                        )
                    )
                )
            )
            if f_name in exploration_pool:
                continue
            else:
                exploration_pool[f_name] = str(
                    func_combinations_expression[fc](
                        sympy.symbols(feat1), sympy.symbols(feat2)
                    )
                )

            if combination_rule_dict[fc](X[feat1], X[feat2]):
                new_feat = func_combinations[fc](X[feat1], X[feat2])
                if np.isfinite(new_feat).all() and np.var(new_feat) > 1e-10:
                    corr1 = abs(np.corrcoef(new_feat, X[feat1])[0, 1])
                    corr2 = abs(np.corrcoef(new_feat, X[feat2])[0, 1])
                    corr = max(abs(corr1), abs(corr2))
                    if corr < correlation_threshold:
                        X[f_name] = new_feat
                        new_combination_features.append(f_name)

    # apply rolling aggregtes, with shift
    for _, feat in enumerate(features_list):
        for rt in rolling:
            for rt_param in rolling_transform_param["win"]:
                f_name = rolling_transform_expression[rt](feat, rt_param)
                new_feat = rolling_transform[rt](X[feat], rt_param)
                X[f_name] = new_feat
                new_rolling_features.append(f_name)

    if step >= max_steps:
        return X
    step += 1

    # eliminate the redundent columns
    cols = [
        c for c in list(X.columns) if c in exploration_pool and c not in df.columns
    ]  # categorical cols not in feature_pool
    if cols:
        # check for correlated features again; this time with the start features
        corrs = dict(
            zip(
                cols,
                np.max(
                    np.abs(
                        np.dot(
                            StandardScaler().fit_transform(X[cols]).T,
                            StandardScaler().fit_transform(df),
                        )
                        / df.shape[0]
                    ),
                    axis=1,
                ),
            )
        )
        cols = [c for c in cols if corrs[c] < correlation_threshold]
    cols = list(df.columns) + cols

    return X[cols]
