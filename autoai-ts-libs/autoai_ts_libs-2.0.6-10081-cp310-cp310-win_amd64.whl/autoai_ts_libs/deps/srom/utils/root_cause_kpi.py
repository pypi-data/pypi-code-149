# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Temporal Feature Tree KPI
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

import autoai_ts_libs.deps.srom as srom
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.utils.tsfresh_utils import get_feature_calc_mapper


class RootCauseKPI(SROMPipeline):
    """
    Information for Temporal Feature Tree.
    """

    def __init__(
        self,
        column_names,
        srom_pipeline=None,
        model_pipeline=None,
        episode_feature_extractor=None,
    ):
        self.srom_pipeline = srom_pipeline
        self.column_names = column_names
        self.episode_feature_extractor = episode_feature_extractor
        self.feature_selector = None
        self.model = None
        self.model_pipeline = model_pipeline

    def check_srom_pipeline(self):
        """
        Checking srom pipeline structure required for KPI.
        """
        # checks for srom pipeline
        if self.srom_pipeline is None:
            raise Exception("SROM pipeline not provided in the Root Cause KPI.")

        if not isinstance(self.srom_pipeline, srom.pipeline.srom_pipeline.SROMPipeline):
            raise Exception("Pipeline object provided is not a valid SROM pipeline.")

        # checks for episode_feature_extractor
        if isinstance(self.srom_pipeline.best_estimator.steps[0], tuple):
            if isinstance(
                self.srom_pipeline.best_estimator.steps[0][1],
                srom.feature_engineering.timeseries.episode_feature_extractor.TSFreshFeatureExtractor,
            ):
                self.episode_feature_extractor = (
                    self.srom_pipeline.best_estimator.steps[0][1]
                )
            else:
                raise Exception(
                    "Not valid episode_feature_extractor object \
inside pipeline.best_estimator.steps tuple. Provide a valid object - \n eg: \
`('Episode Feature Extractor', episodic_extractor)`"
                )
        elif isinstance(
            self.srom_pipeline.best_estimator.steps[0],
            srom.feature_engineering.timeseries.episode_feature_extractor.TSFreshFeatureExtractor,
        ):
            self.episode_feature_extractor = self.srom_pipeline.best_estimator.steps[0]
        else:
            raise Exception(
                "episode_feature_extractor object should be first item in the pipeline stages."
            )

        # check the feature_selector + model pipeline
        if isinstance(
            self.srom_pipeline.best_estimator.steps[1],
            (tuple, srom.pipeline.srom_pipeline.SROMPipeline),
        ):
            # checks for feature_selector
            if isinstance(
                self.srom_pipeline.best_estimator.steps[1][1].steps[0], tuple
            ):
                if isinstance(
                    self.srom_pipeline.best_estimator.steps[1][1].steps[0][1],
                    SelectKBest,
                ):
                    self.feature_selector = self.srom_pipeline.best_estimator.steps[1][
                        1
                    ].steps[0][1]
                else:
                    raise Exception(
                        "Not valid SelectKBest object \
    inside pipeline.best_estimator.steps tuple. Provide a valid object - \n eg: \
    `('Episode Feature Extractor', episodic_extractor)`"
                    )
            elif isinstance(
                self.srom_pipeline.best_estimator.steps[1][1].steps[0][1], SelectKBest
            ):
                self.feature_selector = self.srom_pipeline.best_estimator.steps[1][
                    1
                ].steps[0][1]
            else:
                raise Exception(
                    "feature_selector object not present at the right place in the modelling pipeline."
                )

            # checks for decision_trees_classifers
            if isinstance(
                self.srom_pipeline.best_estimator.steps[1][1].steps[1], tuple
            ):
                if isinstance(
                    self.srom_pipeline.best_estimator.steps[1][1].steps[1][1],
                    (
                        DecisionTreeClassifier,
                        RandomForestClassifier,
                    ),
                ):
                    self.model = self.srom_pipeline.best_estimator.steps[1][1].steps[1][
                        1
                    ]
                else:
                    raise Exception(
                        "Not valid model object \
    inside pipeline.best_estimator.steps tuple. Provide a sklearn's DecisionTreesClassfier or\
    RandomForestClassifier"
                    )
            elif isinstance(
                self.srom_pipeline.best_estimator.steps[1][1].steps[1][1],
                (
                    DecisionTreeClassifier,
                    RandomForestClassifier,
                ),
            ):
                self.model = self.srom_pipeline.best_estimator.steps[1][1].steps[1][1]
            else:
                raise Exception(
                    "Decision Tree model should second item in the pipeline stages."
                )
        else:
            raise Exception(
                "SROM_pipeline object or its tuple containing fitted feature_selector and model \
should be second item in the pipeline stages."
            )

    def generate_root_cause_pipeline(
        self, episode_feature_extractor=None, model_pipeline=None
    ):
        """
        Generate merged srom pipeline containing episode_feature_extractor and model pipeline for the user.
        """

        self.episode_feature_extractor = episode_feature_extractor
        self.model_pipeline = model_pipeline

        if self.episode_feature_extractor is None:
            raise Exception(
                "episode_feature_ectractor object not provided.\
 Provide a valid episode_feature_extractor object before calling generate_root_cause_pipeline."
            )

        if self.model_pipeline is None:
            raise Exception(
                "model_pipeline object not provided.\
 Provide a valid model_pipeline before calling generate_root_cause_pipeline."
            )

        sklpipeline = Pipeline(
            steps=[
                ("feature engg", self.episode_feature_extractor),
                ("model", self.model_pipeline),
            ]
        )
        self.srom_pipeline = SROMPipeline()
        self.srom_pipeline.set_best_estimator(sklpipeline)

    def predict(self, X):
        """
        Predict function for WML to return KPI from tree.
        """
        self.check_srom_pipeline()

        # convert X to dataframe if not a dataframe
        if isinstance(X, (list, np.ndarray)):
            X = pd.DataFrame(X)
            # column_names are mandatory parameter for root cause analysis
            if len(self.column_names) == X.shape[1]:
                X.columns = self.column_names
            else:
                raise Exception(
                    "Size of column_names must be equal to n_features in the input"
                )

        # getting the column names after feature extraction ('extracted_feature_columns')
        extracted_feature_columns = (
            self.episode_feature_extractor.extracted_features_columns
        )
        if extracted_feature_columns is None:
            raise "Column names of extracted features not provided. Run episodic feature extractor in pipeline"

        # getting the features(columns-used) used from feature selector('features_used')
        # getting the feature importances from decision tree model('feature_imp')
        mask = None
        features_used = []
        mask = self.feature_selector.get_support()

        for i, col_name in enumerate(extracted_feature_columns):
            if mask[i]:
                features_used.append(col_name)

        feature_imp = self.model.feature_importances_
        feature_calc_desc_mapper = get_feature_calc_mapper()

        # tree related features
        feature = self.model.tree_.feature
        threshold = self.model.tree_.threshold

        feature_names = [features_used[i] for i in feature]
        feature_imp_tree = [feature_imp[i] for i in feature]

        # getting info for each record
        record_tree_info = []
        for record in range(len(X)):
            x = X.loc[
                X.index[record],
                [
                    self.episode_feature_extractor.episode_id,
                    self.episode_feature_extractor.episode_data_column,
                ],
            ]
            x = pd.DataFrame(x).transpose()
            # x[self.episode_feature_extractor.episode_id] = x[self.episode_feature_extractor.episode_id].astype(str)

            x1 = self.episode_feature_extractor.transform(x)
            features_in_x1 = self.episode_feature_extractor.extracted_features_columns
            x1 = pd.DataFrame(x1, columns=features_in_x1)
            x1 = x1[extracted_feature_columns]

            # IMP NOTE: restoring the original extracted_feature_columns in self.episode_feature_extractor.
            # if the container stays warm, i.e. not shut down, then the original extracted_feature_columns
            # is replace by scoring in the few steps above.
            self.episode_feature_extractor.extracted_features_columns = (
                extracted_feature_columns
            )

            x2 = self.feature_selector.transform(x1)
            prediction = self.model.predict(x2)
            prediction_proba = self.model.predict_proba(x2)

            node_indicator = self.model.decision_path(x2)
            node_index = node_indicator.indices

            record_info = {
                "episode_id": str(
                    X.loc[X.index[record], self.episode_feature_extractor.episode_id]
                ),
                "prediction": prediction.tolist(),
                "prediction_proba": prediction_proba.tolist(),
                "tree_path": [
                    {
                        "treenode_id": int(i),
                        "feature": feature_names[i],
                        "feature_imp": feature_imp_tree[i],
                        "record_feature_val": x2[0, feature[i]],
                        "feature_decision_threshold": threshold[i],
                        "feature_desc": str(
                            (feature_calc_desc_mapper[feature_names[i].split("__")[1]])
                            .replace("    ", "")
                            .replace("\n\n", "")
                        ),
                    }
                    for i in node_index
                ],
            }
            # information for each record with decision tree is stored

            record_tree_info.append(record_info)
        return np.array(record_tree_info)
