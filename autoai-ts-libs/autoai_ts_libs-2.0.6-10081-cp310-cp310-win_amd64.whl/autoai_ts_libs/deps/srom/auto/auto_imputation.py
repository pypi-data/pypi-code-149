# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: auto_imputation
   :synopsis: AutoImputation class.

.. moduleauthor:: SROM Team
"""

import numpy as np
from operator import itemgetter
from multiprocessing import cpu_count
from autoai_ts_libs.deps.srom.auto.base_auto import SROMAutoPipeline
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from sklearn.impute import SimpleImputer
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.imputation.pipeline_utils import cross_validate_impute
from autoai_ts_libs.deps.srom.imputation.metrics import (
    r2_imputation_score,
    median_absolute_imputation_score,
    mean_squared_log_imputation_score,
    mean_absolute_imputation_score,
    mean_squared_imputation_score,
    root_mean_squared_imputation_score,
)

from autoai_ts_libs.deps.srom.utils.imputation_dag import get_timeseries_imputers_dag

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

from autoai_ts_libs.deps.srom.imputation.decomposition_imputers import (
    PCAImputer,
    KernelPCAImputer,
    TruncatedSVDImputer,
    NMFImputer,
    IncrementalPCAImputer,
)

from autoai_ts_libs.deps.srom.imputation.predictive_imputer import PredictiveImputer
from autoai_ts_libs.deps.srom.imputation.pipeline_utils import (
    ImputationKFold,
    MNARImputationKFold,
    MARImputationKFold,
    TsIIDConsecutiveKFold,
    TsVariableConsecutiveKFold,
)

from autoai_ts_libs.deps.srom.utils.pipeline_utils import check_custom_stage_random_state


class AutoImputation(SROMAutoPipeline):
    """
    The class for performing the autoimputation.

    Example:
    >>> from autoai_ts_libs.deps.srom.auto.auto_imputation import AutoImputation
    >>> X = np.transpose([[1,2,np.nan,2,2,1,2],[5,6,3,2,np.nan,3,1]])
    >>> ai = AutoImputation()
    >>> ai.automate(X,X)
    >>> ai.fit(X, X)
    >>> output = ai.transform(X)
    """

    def __init__(
        self,
        level="default",
        save_prefix="auto_imputation_",
        execution_platform="spark_node_random_search",
        cv_type="ImputationKFold",
        cv=5,
        scoring="neg_mean_absolute_error",
        stages=None,
        execution_time_per_pipeline=2,
        num_options_per_pipeline_for_random_search=10,
        num_option_per_pipeline_for_intelligent_search=30,
        total_execution_time=10,
        param_grid=None,
        missing_vals=0.1,
        random_state=42,
        imputation_type="iid",
    ):
        """
        Parameters:
            level (String): Level of exploration (default or comprehensive).
            save_prefix (string): String prefix for the output save file.
            execution_platform (string): Platform for execution from autoai_ts_libs.deps.srom pipeline. Supports spark also.
            cv_type (string):  Defines the mechanism of generating the artificial missing follows
                specific missing patterns.  The logic is similar to the KFold selection for
                the training/testing split.  However, this type specifies how the artificial
                missing is generated.  There are missing patterns for non-time-series
                (such as ImputationKFold, MARImputationKFold, and MNARImputationKFold)
                and time-series (such as ImputationKFold, TsIIDConsecutiveKFold, and
                TsVariableConsecutiveKFold).
            cv (int): Value of 'k' in KFold used for generating a multiple datasets with artificial
                    missing values based on cv_type.
            scoring (Sting, function): The value defines the metrics for scoring the imputation
                    performance. It is a value of string defining a mapping to a function
                    to compare the ground truth and imputed values. The internal function uses
                    the sklearn defined metrics (such as neg_mean_absolute_error).  The final
                    performance is based on comparing the generating the artificial missing with
                    the ground over KFold.
            stages (list of imputers): stages (list of imputers): A list of candidate imputers utilizing
                    different imputation algorithms and strategies.  Each imputer might have different
                    imputation parameters and typically associated with a grid for the possible values.
                    The list is used for customizing the preconfigured auto pipeline.
            execution_time_per_pipeline (int): Integer value denoting time (minutes) of execution
                    per path (path: combination of estimators and transformers).
            total_execution_time (int): Total execution time (minutes) for the auto imputation pipeline.
            num_options_per_pipeline_for_random_search (int): Integer value denoting number of parameters to
                    use while performing randomized param search in *which* rounds.
            num_option_per_pipeline_for_intelligent_search: Integer value denoting number of parameters to use
                    while performing more intelligent param search in *which* rounds.
            total_execution_time (int): Total execution time (minutes) for the auto imputation pipeline.
            param_grid (SROMParamGrid): Param grid with various parameter combination for the parameters used
                    for the impuers defined in the stages.
            missing_vals (float) : Amount of missing values automatically sampled to test the performance.
                                    If the value is a floating value and less than 1, then the missing samples
                                    are based on the ratio.  The ratio is equal to â€˜missing_valsâ€™
                                    For example, if missing_vals = 0.1, it means that we sample 10% of missing.
                                    However, if the value is a positive integer, such as missing_vals = 10,
                                    it means that we randomly sample a fixed number of missing data points (10).
                                    The default is missing_vals  = 0.1, i.e., 10% of artificial missing.
            random_state (int) : seed for randomness.
            imputation_type (string) : iid (assuming that samples are independent of each other). It is used
                                    to specify that it is not a time-series imputation.
                                    timeseries (assuming the samples have temporal dependency.)  It is used
                                    to specifcy that we need to use time-series oriented imputation.
        """

        super(AutoImputation, self).__init__(
            level=level,
            save_prefix=save_prefix,
            execution_platform=execution_platform,
            cv=cv,
            scoring=scoring,
            stages=stages,
            execution_time_per_pipeline=execution_time_per_pipeline,
            num_options_per_pipeline_for_random_search=num_options_per_pipeline_for_random_search,
            num_option_per_pipeline_for_intelligent_search=num_option_per_pipeline_for_intelligent_search,
            total_execution_time=total_execution_time,
            bayesian_paramgrid=None,
            rbopt_paramgrid=None,
            param_grid=param_grid,
        )

        # to extra initialization
        self.random_state = random_state
        self.cv_type = cv_type
        self.missing_vals = missing_vals
        self.imputation_type = imputation_type

        if param_grid is None:

            if self.imputation_type == "timeseries":
                self.param_grid = SROMParamGrid(gridtype="imputation_time_series_grid")
            else:
                self.param_grid = SROMParamGrid(gridtype="imputation_iid_grid")

        cv_type_mapping = {
            "ImputationKFold": ImputationKFold,
            "MARImputationKFold": MARImputationKFold,
            "MNARImputationKFold": MNARImputationKFold,
            "TsIIDConsecutiveKFold": TsIIDConsecutiveKFold,
            "TsVariableConsecutiveKFold": TsVariableConsecutiveKFold,
        }

        self.cross_validate_impute = cross_validate_impute
        self.scoring = self._get_impute_scorer(scoring)
        self.cv = cv_type_mapping[cv_type](
            n_iteration=cv, impute_size=missing_vals, random_state=random_state
        )

    def _get_impute_scorer(self, scoring):
        """
            Get impute scorer method to get score for different scoring method.
        """
        if scoring == "r2":
            return r2_imputation_score
        elif scoring == "neg_mean_absolute_error":
            return mean_absolute_imputation_score
        elif scoring == "neg_mean_squared_error":
            return mean_squared_imputation_score
        elif scoring == "neg_root_mean_squared_error":
            return root_mean_squared_imputation_score
        elif scoring == "neg_mean_squared_log_error":
            return mean_squared_log_imputation_score
        elif scoring == "neg_median_absolute_error":
            return median_absolute_imputation_score
        else:
            return scoring

    def _initialize_default_stages(self, random_state=42):
        """
        Set stages for the pipeline in a pre-defined manner.
        """
        # initialize the stages of the pipeline
        if self.imputation_type == "iid":
            self.stages = [
                [
                    ("simpleimputer", SimpleImputer()),
                    ("pcaimputer", PCAImputer()),
                    ("nmfimputer", NMFImputer()),
                    ("predictiveimputer", PredictiveImputer()),
                    ("knnimputer", KNNImputer()),
                    ("iterativeimputer", IterativeImputer()),
                ]
            ]
        elif self.imputation_type == "timeseries":
            # this list need to be populated after carefully review
            """
            Set stages for the pipeline in a pre-defined manner.
            """
            # initialize the stages of the pipeline
            self.stages = get_timeseries_imputers_dag()
        else:
            raise Exception("The imputation type is not supported...")
        return self.stages

    def _initialize_additional_stages(self, random_state=42):
        """
        Initialize additionsl stages for the pipeline in a pre-defined manner.
        """
        self.additional_stages = None
        return self.additional_stages

    def _init_pipeline(self, stages=None):
        """
        Initialize pipeline method.
        """
        self.auto_pipeline = SROMPipeline()
        self.auto_pipeline.set_cross_validation(self.cv)
        self.auto_pipeline.set_scoring(self.scoring)
        self.auto_pipeline.set_cross_val_score(self.cross_validate_impute)

        # set default stages if custom stages not provided
        if stages is None:
            if self.stages is None:
                self.stages = self._initialize_default_stages()
            self.auto_pipeline.set_stages(self.stages)
            check_custom_stage_random_state(self.stages)
        else:
            self.auto_pipeline.set_stages(stages)
            check_custom_stage_random_state(stages)

    def automate(self, X, y=None, verbosity="low"):
        """
        The function for executing the automated training of the SROM pipeline. This \
        code follows a well-defined strategy for iteratively training a subset of pipeline \
        and finding the best estimator in each iteration. This strategy provides best results \
        in the shortest amount of time.

        Parameters:
            X (pandas dataframe or numpy array): The dataset to be used for model selection. \
                    shape = [n_samples, n_features] \
                    where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. This is optional, \
                    if target_column is added in the meta data, it is used from \
                    there.shape = [n_samples] or [n_samples, n_output].
        """
        return super(AutoImputation, self).automate(X, y, verbosity)

    def fit(self, X, y):
        """
        Train the best model on the given data.

        Parameters:
            X (pandas dataframe or numpy array): Training dataset. \
                    shape = [n_samples, n_features] \
                    where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                    if target_column is added in the meta data, it is \
                    used from there. shape = [n_samples] or [n_samples, n_output]

        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline.
        """
        super(AutoImputation, self).fit(X, y)
        return self

    def transform(self, X):
        """
        Predict the class labels/regression targets/anomaly scores etc. using \
        the trained model pipeline.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """

        if self.best_estimator_so_far:
            return self.best_estimator_so_far.transform(X)

    def summary(self, enable_param_grid=False):
        """
        Summary method to get the summary of the pipeline.
        """
        tmp_auto_pipeline = SROMPipeline()
        if self.stages:
            tmp_auto_pipeline.set_stages(self.stages)
        else:
            tmp_auto_pipeline.set_stages(self._initialize_default_stages())
        if self.param_grid:
            tmp_auto_pipeline.set_param_grid(self.param_grid)
        return tmp_auto_pipeline.summary(
            enable_param_grid=enable_param_grid, is_auto=True
        )

    def predict(self, X):
        """
        Predict is no-op here
        """
        pass
