# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: failure_pattern_analysis
    :synopsis: An abstraction built to be used by failure \
        pattern analysis pipeline(for now). 

.. moduleauthor:: SROM Team
"""

import copy
import os
import time
import uuid
import warnings
from abc import abstractmethod

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from autoai_ts_libs.deps.srom.classification.sampler_based_imbalanced_classifier import ImbalancedClassifier
from autoai_ts_libs.deps.srom.data_sampling.unsupervised.random_sampler import (
    Random_MajorityClass_DownSampler,
)
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from xgboost import XGBClassifier


class FailurePatternAnalysisPipeline(SROMPipeline):
    """
    Failure Prediction Analysis (FPA) is a solution template which allows user to \
    build machine learning models for predicting imminent failures by analyzing the \
    time-series data generated in heavy industries. \
    Advantages of this pipeline are: 1. Feature engineering and extraction is done \
    within the pipeline which reduces lot of code from notebook/workflow and reduces \
    human errors. 2. It can be used as a re-train pipeline in automated processes which \
    is not possible with de-coupled feature extraction and estimator selection. \
    3. It accepts sensor and failure tables as is which reduces steps to prepare merged \
    FPATable. 4. Multiple feature generators and pipelines or list of sklearn pipelines or \
    SROM pipelines including smart clasification can be used as stages.

    Parameters:
        asset_id_column (String): Column name for asset identifier.
        sensor_feature_columns (list of Strings): Feature column names for sensor table.
        failure_type_column (String): Column name which has information about type of failure.
        sensor_datetime_column (String): Time column in sensor table.
        failure_datetime_column (String): Time column in failure table.
        failure_detection_window (String): Pre-failure window to attribute failure to data point\
            using failure_type_column and failure_datetime_column.
        sensor_datetime_format (String): Time format for time column in sensor table.
        failure_datetime_format (String): Time format for time column in failure table.
        prediction_interval (String): Interval in which model is predicted.
    
    Example:
        from autoai_ts_libs.deps.srom.pipeline.failure_pattern_analysis import FailurePatternAnalysisPipeline \
        from autoai_ts_libs.deps.srom.feature_engineering.timeseries.rolling_window_feature_extraction import SimpleSummaryStats \
        from autoai_ts_libs.deps.srom.classification.smart_classification import SmartClassification \
        fpa_pipe = FailurePatternAnalysisPipeline(asset_id_column='asset_id', \
                                            sensor_feature_columns=['x1', 'x2'], \
                                            sensor_datetime_column='datetime', \
                                            sensor_datetime_format='%Y-%m-%d %H:%M:%S', \
                                            failure_type_column='failure_id', \
                                            failure_datetime_column='failuredate', \
                                            failure_detection_window='4D', \
                                            failure_datetime_format='%Y-%m-%d %H:%M:%S', \
                                            prediction_interval='1D') \
        simp_summary = SimpleSummaryStats(rolling_window_size='6D') \
        ac = SmartClassification(scoring='average_precision', total_execution_time=1) \
        feature_generators = [[('SimpleSummary', simp_summary)]] \
        model_builders = [('smart_classification', ac)] \
        fpa_pipe.set_stages(feature_generators, model_builders) \
        fpa_pipe.set_cross_validation(cv_type='iid') \
        fpa_pipe.execute(sensor_train, failure_train) \
    """

    @abstractmethod
    def __init__(
        self,
        asset_id_column,
        sensor_feature_columns,
        failure_type_column,
        sensor_datetime_column,
        failure_datetime_column,
        failure_detection_window,
        sensor_datetime_format,
        failure_datetime_format,
        prediction_interval,
    ):
        super(FailurePatternAnalysisPipeline, self).__init__()
        self.asset_id_column = asset_id_column
        self.sensor_feature_columns = sensor_feature_columns
        self.failure_type_column = failure_type_column
        self.sensor_datetime_column = sensor_datetime_column
        self.sensor_datetime_format = sensor_datetime_format
        self.failure_datetime_column = failure_datetime_column
        self.failure_datetime_format = failure_datetime_format
        self.failure_detection_window = failure_detection_window
        self.prediction_interval = prediction_interval

        # core component of FPA pipelines
        # feature generators is a list of list of tuples
        # model builders is a list of tuples
        self.feature_generators = None
        self.model_builders = None
        self.cv = None
        self._X_names = None

    def _preprocess_sensor_table(self, sensor_table):
        sensor_table = sensor_table.drop_duplicates(
            subset=[self.asset_id_column, self.sensor_datetime_column]
        )
        sensor_table[self.sensor_datetime_column] = pd.to_datetime(
            sensor_table[self.sensor_datetime_column],
            format=self.sensor_datetime_format,
        )
        return sensor_table

    def _preprocess_failure_table(self, failure_table):
        failure_table = failure_table.drop_duplicates(
            subset=[self.asset_id_column, self.failure_datetime_column]
        )
        failure_table[self.failure_datetime_column] = pd.to_datetime(
            failure_table[self.failure_datetime_column],
            format=self.failure_datetime_format,
        )
        failure_table = failure_table.dropna()
        return failure_table

    def _prepare_base_prediction_table(self, sensor_table):
        from autoai_ts_libs.deps.srom.failure_prediction.preprocessing import generate_key_col

        base_keys_table = generate_key_col(
            sensor_table,
            self.sensor_datetime_column,
            self.asset_id_column,
            self.prediction_interval,
        )
        return base_keys_table

    def _prepare_failure_prediction_table(self, failure_table, failure_keys):
        from autoai_ts_libs.deps.srom.failure_prediction.preprocessing import generate_failure_targets

        failure_target_table = generate_failure_targets(
            failure_table,
            failure_keys,
            self.failure_detection_window,
            self.asset_id_column,
            self.failure_datetime_column,
            self.failure_type_column,
        )
        return failure_target_table

    def _check_column_names(self, sensor_table, failure_table):

        columns_for_check = []
        columns_for_check.extend(self.sensor_feature_columns)
        columns_for_check.extend([self.asset_id_column])
        columns_for_check.extend([self.sensor_datetime_column])
        for item in columns_for_check:
            if item not in list(sensor_table.columns):
                raise Exception("Sensor table is missing a column name - ", item)

        columns_for_check = []
        columns_for_check.extend([self.asset_id_column])
        columns_for_check.extend([self.sensor_datetime_column])
        for item in columns_for_check:
            if item not in list(failure_table.columns):
                raise Exception("Failure table is missing a column name - ", item)

    def _auto_set_param_for_feature_extractor(self, feature_generators):
        tmp_feature_generators = copy.deepcopy(feature_generators)
        for i in range(len(tmp_feature_generators)):
            for j in range(len(tmp_feature_generators[i])):
                if not tmp_feature_generators[i][j][1].asset_id_column:
                    tmp_feature_generators[i][j][1]._update_param(
                        "asset_id_column", self.asset_id_column
                    )
                if not tmp_feature_generators[i][j][1].sensor_feature_columns:
                    tmp_feature_generators[i][j][1]._update_param(
                        "sensor_feature_columns", self.sensor_feature_columns
                    )
                if not tmp_feature_generators[i][j][1].sensor_datetime_column:
                    tmp_feature_generators[i][j][1]._update_param(
                        "sensor_datetime_column", self.sensor_datetime_column
                    )
                if not tmp_feature_generators[i][j][1].sensor_datetime_format:
                    tmp_feature_generators[i][j][1]._update_param(
                        "sensor_datetime_format", self.sensor_datetime_format
                    )
        return tmp_feature_generators

    def _check_pipeline_stages(self):
        if self.feature_generators is None:
            raise Exception("Feature Generators are not set")
        if self.model_builders is None:
            raise Exception("Models Builders are not set")

    def set_stages(self, feature_generators, model_builders):
        """
        Sets feature generators and model builders as stages. Each of the feature generators \
        and model builders will be used a stage in pipeline exploration.

        Parameters:
            feature_generators (list of tuples or list of lists): List of (lists of) feature generator tuples
            model_builders (list of tupes): List of model/estimator tuples.
        
        Example:
            simp_summary = SimpleSummaryStats(rolling_window_size='6D') \
            ac = SmartClassification(scoring='average_precision', total_execution_time=1) \
            feature_generators = [[('SimpleSummary', simp_summary)]] \
            model_builders = [('smart_classification', ac)] \
            fpa_pipe.set_stages(feature_generators, model_builders)
        """
        feature_generators = self._auto_set_param_for_feature_extractor(
            feature_generators
        )
        tmp_feature_generators = []
        from sklearn.pipeline import FeatureUnion

        for item in feature_generators:
            if len(item) > 1:
                fu_name = [tup[0] for tup in item]
                tmp_feature_generators.append(
                    ("+".join(fu_name), FeatureUnion(transformer_list=item))
                )
            else:
                tmp_feature_generators.append(item[0])
        self.feature_generators = tmp_feature_generators
        self.model_builders = model_builders
        srom_stages = [tmp_feature_generators, self.model_builders]
        self._sromgraph.set_stages(srom_stages)
        # super(FailurePatternAnalysisPipeline, self).set_stages(srom_stages)

    def create_graph(self):
        """
        From the stages set in the pipeline, create a graph object using networkx. \
        The graph is saved as dot file, pickle and image at the pipeline's storage location. \
        Graph File is generated only if number of node is < 40.

        Returns:
             path_graph_image (String): Location where graph is stored.
        Raises:
            ImportError:
                If pydot module is not available. In this case, graph will not be drawn.
        """
        self._check_pipeline_stages()
        return super(FailurePatternAnalysisPipeline, self).create_graph()

    def _specialdatatransforms(
        self, feature_transformation, sensor_table, failure_target_table
    ):
        featuesVal = feature_transformation.fit_transform(
            sensor_table, failure_target_table
        )
        col_headers = []
        for item in feature_transformation.get_feature_names():
            if "__" in item:
                if "asset_id" in item.split("__")[1]:
                    col_headers.append("asset_id")
                elif "datetime" in item.split("__")[1]:
                    col_headers.append("datetime")
                else:
                    col_headers.append(item)
            else:
                col_headers.append(item)

        tmp_FPA_table = pd.DataFrame(featuesVal, columns=col_headers)
        tmp_FPA_table = tmp_FPA_table.loc[:, ~tmp_FPA_table.columns.duplicated()]
        tmp_FPA_table["datetime"] = pd.to_datetime(
            tmp_FPA_table["datetime"], format="%Y-%m-%d %H:%M:%S"
        )
        FPA_table = pd.merge(
            failure_target_table,
            tmp_FPA_table,
            on=["asset_id", "datetime"],
            how="outer",
        )

        newColumns = []
        for item in FPA_table.columns:
            if "asset_id" in item:
                newColumns.append(self.asset_id_column)
            elif "datetime" in item:
                newColumns.append(self.sensor_datetime_column)
            elif "target_label" in item:
                newColumns.append(self.failure_type_column)
            else:
                newColumns.append(item)

        FPA_table.columns = newColumns
        original_size = FPA_table.shape[0]
        FPA_table = FPA_table.replace([np.inf, -np.inf], np.nan).dropna()
        new_size = FPA_table.shape[0]
        if (new_size * 1.0 / original_size) < 0.6:
            print("size is reduced significantly")
        return FPA_table, feature_transformation

    def _get_X_y(self, FPA_table, include_groups=False):
        features = list(FPA_table.columns)
        features.remove(self.failure_type_column)

        if not include_groups:
            features.remove(self.asset_id_column)
            features.remove(self.sensor_datetime_column)
        X = FPA_table[features]
        y = FPA_table[self.failure_type_column]

        return X, y

    def _prepare_cross_validator(self, FPA_table, X, y):
        if self.cv == "asset":
            groups = FPA_table[self.asset_id_column]
            from sklearn.model_selection import GroupKFold

            group_kfold = GroupKFold(n_splits=self.cv_fold)
            cv = list(group_kfold.split(X, y, groups))
        elif self.cv == "time":
            raise NotImplementedError("Need More time")
        elif self.cv == "iid":
            return self.cv_fold
        else:
            raise Exception("Wrong selection")
        return cv

    def set_cross_validation(self, cv_type="asset", cv_fold=5):
        """
        Selection of cross validator based on asset/group or iid (non-group). \
        For more information on asset/group cv, refer user guide \
        https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html. \
        For more information on cv_fold, please refer user guide \
        https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation.

        Parameters:
            cv_type (String): Cross validation type. Supported values are asset and iid.
            cv_fold (int, cross-validation generator or an iterable, optional): Determines the \
                cross-validation splitting strategy. Possible inputs for cv are: None, to use \
                the default 10-fold cross validation, integer, to specify the number of folds \
                in a (Stratified)KFold, aan object to be used as a cross-validation generator. \
                An iterable yielding train, test splits.
        """
        self.cv = cv_type
        self.cv_fold = cv_fold

    def _check_dataframe_instance(self, X):
        if not isinstance(X, pd.DataFrame):
            raise Exception("Input Data is not a pandas dataframe")

    def execute(self, sensorDb, failureDb):
        """
        This function merges the sensor and failure data using provided configuration \
        during initialization of fpa pipeline. Then, runs cross validation on a given \
        dataset along all possible paths in the DAG and returns the result of the best estimator.

        Parameters:
            sensorDb (pd.DataFrame): Sensor table along with time column, sensor \
            features and asset column.
            failureDb (pd.DataFrame): Failure table along with time column and failure type \
            and asset column.
        
        Returns (tuple):
            Returns the tuple containing:
                best_estimator (list of tuples): Each tuple in the list represent a stage in best \
                    estimator pipeline path in order.
                best_score (numpy.float64): Train score of selected best estimator.

        Raises:
            BaseException:
                If exectype is not supported.
        """
        # A lot of data dependent information is extracted and used in for defining paths,
        # hence, they are executed in this stage.

        self._check_dataframe_instance(sensorDb)
        self._X_names = list(sensorDb.columns)
        self._check_dataframe_instance(failureDb)
        self._check_column_names(sensorDb, failureDb)
        self.sensorDb = self._preprocess_sensor_table(sensorDb)
        self.failureDb = self._preprocess_failure_table(failureDb)
        self.baseDb = self._prepare_base_prediction_table(self.sensorDb)
        self.labelDb = self._prepare_failure_prediction_table(
            self.failureDb, self.baseDb
        )
        if self.cv is None:
            self.set_cross_validation()

        self.best_estimators = []
        self.best_scores = []
        self.number_of_combinations = 0

        for path in self.paths:
            feature_transformation = path[0]
            model_builder = path[1]
            FPA_table, _ = self._specialdatatransforms(
                feature_transformation[1], self.sensorDb, self.labelDb
            )
            X, y = self._get_X_y(FPA_table)
            cv = self._prepare_cross_validator(FPA_table, X, y)

            if "sklearn" in str(model_builder[1].__class__):
                from sklearn.model_selection import cross_val_score

                scores = cross_val_score(model_builder[1], X, y, cv=cv)
                tmp_path = [feature_transformation, model_builder]
                self.best_estimators.append(tmp_path)
                self.best_scores.append(np.mean(scores))
                self.number_of_combinations = self.number_of_combinations + 1
            elif "srom" in str(model_builder[1].__class__):
                if "auto" in str(model_builder[1].__class__):
                    model_builder[1].cv = cv
                    ans = model_builder[1].automate(X, y)
                    model_builder = (model_builder[0], ans[0])
                    tmp_path = [feature_transformation, model_builder]
                    self.best_estimators.append(tmp_path)
                    self.best_scores.append(ans[1])
                    self.number_of_combinations = self.number_of_combinations + 1
                elif "smart" in str(model_builder[1].__class__):
                    model_builder[1].cv = cv
                    ans = model_builder[1].fit(X, y)
                    tmp_path = [feature_transformation, model_builder]
                    self.best_estimators.append(tmp_path)
                    self.best_scores.append(ans.get_best_score())
                    self.number_of_combinations = self.number_of_combinations + 1
                else:
                    model_builder[1].set_cross_validation(cv)
                    ans = model_builder[1].execute(X, y)
                    model_builder = (model_builder[0], ans[0])
                    tmp_path = [feature_transformation, model_builder]
                    self.best_estimators.append(tmp_path)
                    self.best_scores.append(ans[1])
                    self.number_of_combinations = self.number_of_combinations + 1
            else:
                raise Exception("Unknwon model for execution")

        if self.best_scores:
            tmp_best_scores = np.nanmax(np.array(self.best_scores, dtype=np.float64))
            if not np.isnan(tmp_best_scores):
                best_result_index = self.best_scores.index(tmp_best_scores)
                self.best_score = self.best_scores[best_result_index]
                self.best_estimator = copy.deepcopy(
                    self.best_estimators[best_result_index]
                )

        return self.best_estimator, self.best_score

    def fit(self, X, y):
        """
        Fit the best estimator resulted from execute function, with the \
        sensor and failure data.

        Parameters:
            X (pd.DataFrame): Sensor table along with time column, sensor \
            features and asset column.
            y (pd.DataFrame): Failure table along with time column and failure type \
            and asset column.
        """
        if self.best_estimator is None:
            raise Exception("Execute the pipeline before calling 'fit' method.")

        self._check_dataframe_instance(X)
        self._X_names = list(X.columns)
        self._check_dataframe_instance(y)
        self._check_column_names(X, y)
        self.sensorDb = self._preprocess_sensor_table(X)
        self.failureDb = self._preprocess_failure_table(y)
        self.baseDb = self._prepare_base_prediction_table(self.sensorDb)
        self.labelDb = self._prepare_failure_prediction_table(
            self.failureDb, self.baseDb
        )

        feature_transformation = self.best_estimator[0]
        model_builder = self.best_estimator[1]
        FPA_table, tmp_feature_transformation = self._specialdatatransforms(
            feature_transformation[1], self.sensorDb, self.labelDb
        )
        feature_transformation = (feature_transformation[0], tmp_feature_transformation)
        X_, y_ = self._get_X_y(FPA_table)
        model_builder[1].fit(X_, y_)
        self.best_estimator = [feature_transformation, model_builder]
        return self.best_estimator

    def get_feature_engineered_table(self, X, y=None, include_groups=False):
        """
        This function applies feature generator from best estimator pipeline \
        and returns the feature extracted data and mapped target labels.

        Parameters:
            X (pd.DataFrame): Sensor table along with time column, sensor \
            features and asset column.
            y (pd.DataFrame): Failure table along with time column and failure type \
            and asset column.
            include_groups (Boolean): True, includes group/asset columnn and timestamp. \
                Default=False.
        
        Returns:
            Returns the tuple containing:
                tabular_data (list of tuples): Each tuple in the list represent a stage in best \
                    estimator pipeline path in order.
                targets (numpy.float64): Train score of best estimator.

        """
        if self.best_estimator is None:
            raise Exception("Execute the pipeline before calling 'fit' method.")
        try:
            self._check_dataframe_instance(X)
        except Exception:
            if len(self._X_names) == X.shape[0]:
                X = pd.DataFrame(X, columns=self._X_names)
            else:
                raise ValueError("Data Dimension does not match")

        tmp_sensorDb = self._preprocess_sensor_table(X)
        tmp_baseDb = self._prepare_base_prediction_table(tmp_sensorDb)

        if y is None:
            tmp_baseDb[self.failure_type_column] = "?"
            feature_transformation = self.best_estimator[0]
            FPA_table, _ = self._specialdatatransforms(
                feature_transformation[1], tmp_sensorDb, tmp_baseDb
            )
            X_, _ = self._get_X_y(FPA_table, include_groups=include_groups)
            return X_
        else:
            try:
                self._check_dataframe_instance(y)
                self._check_column_names(X, y)
            except Exception:
                raise Exception("check input data")
            tmp_failureDb = self._preprocess_failure_table(y)
            tmp_labelDb = self._prepare_failure_prediction_table(
                tmp_failureDb, tmp_baseDb
            )

            feature_transformation = self.best_estimator[0]
            FPA_table, _ = self._specialdatatransforms(
                feature_transformation[1], tmp_sensorDb, tmp_labelDb
            )
            X_, y_ = self._get_X_y(FPA_table, include_groups=include_groups)
            return X_, y_

    def predict(self, X):
        """
        Predict the class labels/failures using the trained best pipeline.

        Parameters:
            X (pandas dataframe or numpy array): Sensor table along with time column, sensor \
            features and asset column. 

        Returns:
            Predicted scores in an array of length n_samples.
        """
        X_ = self.get_feature_engineered_table(X)
        model_builder = self.best_estimator[1]
        predVal = model_builder[1].predict(X_)
        return predVal

    def predict_proba(self, X):
        """
        Predict the failure probability using the best estimator of the pipeline.

        Parameters:
            X (pandas dataframe or numpy array): Sensor table along with time column, sensor \
            features and asset column. 

        Returns:
            Predicted failure probabilities in an array of length n_samples.
        """
        X_ = self.get_feature_engineered_table(X)
        model_builder = self.best_estimator[1]
        predVal = model_builder[1].predict_proba(X_)
        return predVal
