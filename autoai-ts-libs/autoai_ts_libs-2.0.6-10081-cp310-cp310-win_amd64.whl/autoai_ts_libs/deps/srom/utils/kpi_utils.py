# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


from operator import itemgetter

import pandas as pd
import ast
import numpy as np
import pydotplus
from IPython.display import HTML, display
from six import StringIO
from sklearn.feature_selection import SelectKBest
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from autoai_ts_libs.deps.srom.feature_engineering.timeseries.episode_feature_extractor import (
    TSFreshFeatureExtractor,
)
from autoai_ts_libs.deps.srom.utils.srom_tabulate import tabulate
from autoai_ts_libs.deps.srom.utils.tsfresh_utils import get_feature_calc_mapper

def get_config_from_string(parts):
    """
    Helper function to extract the configuration of a certain function from the column name.
    The column name parts (split by "__") should be passed to this function. It will skip the
    kind name and the function name and only use the parameter parts. These parts will be split up on "_"
    into the parameter name and the parameter value. This value is transformed into a python object
    (for example is "(1, 2, 3)" transformed into a tuple consisting of the ints 1, 2 and 3).

    Returns None of no parameters are in the column name.

    :param parts: The column name split up on "__"
    :type parts: list
    :return: a dictionary with all parameters, which are encoded in the column name.
    :rtype: dict
    """
    relevant_parts = parts[2:]
    if not relevant_parts:
        return

    config_kwargs = [s.rsplit("_", 1)[0] for s in relevant_parts]
    config_values = [s.rsplit("_", 1)[1] for s in relevant_parts]

    dict_if_configs = {}

    for key, value in zip(config_kwargs, config_values):
        if value.lower() == "nan":
            dict_if_configs[key] = np.NaN
        elif value.lower() == "-inf":
            dict_if_configs[key] = np.NINF
        elif value.lower() == "inf":
            dict_if_configs[key] = np.PINF
        else:
            dict_if_configs[key] = ast.literal_eval(value)

    return dict_if_configs

def temporal_feature_tree_kpi(
    pipeline, extracted_feature_columns=None, verbosity="high"
):
    """
    Function to extract and visualize the performance of the model.

    Args:
        pipeline (srom pipeline object, required): Fitted SROM pipeline object.
        extracted_feature_columns (list of column names, optional): column names of the extracted
        features from the Episodic Feature Extractor if feature extractor run separately from
        pipeline
        verbosity (string, optional): 'high' or 'low' depending on the information returned.
        default is 'high'

    Return:
        graph: tree graph object which can be shown in Jupyter notebook.
        featurs_table: summary table of features used and their feature importance.
    """

    if pipeline.best_estimator is None:
        raise Exception("Train the model first by calling execute/fit method")

    # Check if the feature extractor is run inside or outside pipeline
    # and notify the user
    if extracted_feature_columns is None:
        for step in pipeline.best_estimator.steps:
            if isinstance(step[1], TSFreshFeatureExtractor):
                extracted_feature_columns = step[1].extracted_features_columns

    if extracted_feature_columns is None:
        raise 'Column names of extracted features not provided.\
               Either run episodic feature extractor in pipeline or provide the \
               column names using "episodic_extractor.extracted_features_columns" from the object.)'

    # Setting order for the extractor, selector, and model in the pipeline
    extracted_features_columns = extracted_feature_columns

    mask = None
    model = None
    features_used = []

    for step in pipeline.best_estimator.steps:
        if isinstance(step[1], SelectKBest):
            mask = step[1].get_support()

            for i, col_name in enumerate(extracted_features_columns):
                if mask[i]:
                    features_used.append(col_name)

        if isinstance(step[1], DecisionTreeClassifier):
            model = step[1]

    feature_imp = model.feature_importances_

    feature_calc_desc_mapper = get_feature_calc_mapper()

    # Creating table for top k features
    node_feature = [
        [
            "Node",
            "feature",
            "feature importance",
            "feature calculation method",
            "parameters",
        ]
    ]
    feature_desc = [["feature calculation method", "description"]]
    node_feature_minimal = [["Node", "feature", "feature importance"]]
    for i, feat in enumerate(features_used):
        feat_ = feat.split("__")

        if feature_imp[i] != 0:
            node_feature.append(
                [
                    "X" + str(i),
                    feat,
                    round(feature_imp[i], 5),
                    feat_[1],
                    get_config_from_string(feat_),
                ]
            )
            node_feature_minimal.append(["X" + str(i), feat, round(feature_imp[i], 5)])
            desc_ = [
                feat_[1],
                (feature_calc_desc_mapper[feat_[1]])
                .replace("    ", "")
                .replace("\n\n", ""),
            ]
            if desc_ not in feature_desc:
                feature_desc.append(desc_)

    if len(node_feature) == 1 or len(feature_desc) == 1:
        raise ValueError(
            "The feature importance in the data for all the columns is 0."
            + " Please check if you data has 2 or more disctinct classes."
        )

    if verbosity == "low":
        node_feature = node_feature_minimal
    headers = node_feature.pop(0)
    features_table = pd.DataFrame(node_feature, columns=headers)
    features_table = features_table.sort_values("feature importance", ascending=False)
    node_feature = sorted(node_feature, key=itemgetter(2), reverse=True)

    if verbosity == "high":
        header_desc = feature_desc.pop(0)
        display(HTML(tabulate(feature_desc, headers=header_desc, tablefmt="html")))
    display(HTML(tabulate(node_feature, headers=headers, tablefmt="html")))

    # Creating tree from decision trees
    dot_data = StringIO()
    export_graphviz(
        model,
        out_file=dot_data,
        label="all",
        node_ids=True,
        filled=True,
        rounded=True,
        proportion=True,
        impurity=False,
        special_characters=True,
    )

    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    return graph, features_table
