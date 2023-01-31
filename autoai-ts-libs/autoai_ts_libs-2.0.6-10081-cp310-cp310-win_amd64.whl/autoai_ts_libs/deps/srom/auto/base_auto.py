# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: base_auto
   :synopsis: Contains SROMAuto class.

.. moduleauthor:: SROM Team
"""
import logging
import math
import os
import random
import tempfile
import time
import uuid
import warnings
from abc import ABC, abstractmethod
from operator import itemgetter
import itertools

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator

from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.pipeline.utils.lithops_helper import replace_srom_classes
from autoai_ts_libs.deps.srom.utils.estimator_utils import get_estimator_meta_attributes
from autoai_ts_libs.deps.srom.utils.export_utils import export_pipeline
from autoai_ts_libs.deps.srom.utils.pipeline_utils import check_srom_pipeline_stages
from autoai_ts_libs.deps.srom.utils.pipeline_utils import (
    get_pipeline_description,
    get_pipeline_name,
    check_custom_stage_random_state,
)
from sklearn.inspection import permutation_importance
from sklearn.pipeline import Pipeline
from pathlib import Path
from autoai_ts_libs.deps.srom.utils.file_utils import gettempdir

LOGGER = logging.getLogger(__name__)


class SROMAuto(ABC):
    """
    == BASE / ABSTRACT == \
    (adding this comment till standard nomenclature is not generated)

    An SROMAuto class implements the default version of the pipeline which other Auto pipelines \
    will build upon.
    """

    @abstractmethod
    def automate(self, X, y):
        """This method should conduct the automation of DAG"""

    @abstractmethod
    def fit(self, X, y, **fit_params):
        """This method should fit the best discovered pipeline after the automation"""

    @abstractmethod
    def predict(self, X):
        """This method should produce the output of trained pipeline"""


class SROMAutoPipeline(SROMAuto, BaseEstimator):
    """
    == BASE / ABSTRACT == \
    (adding this comment till standard nomenclature is not generated)

    """

    @abstractmethod
    def __init__(
        self,
        level,
        save_prefix,
        execution_platform,
        cv,
        scoring,
        stages,
        execution_time_per_pipeline,
        num_options_per_pipeline_for_random_search,
        num_option_per_pipeline_for_intelligent_search,
        total_execution_time,
        bayesian_paramgrid,
        rbopt_paramgrid,
        param_grid,
    ):
        """
        Parameters:
            level (String): Level of exploration (default or comprehensive).
            save_prefix (string): String prefix for the output save file.
            execution_platform (string): Platform for execution from autoai_ts_libs.deps.srom pipeline. Supports spark also.
            cv (int): Value of 'k' in K-crossvalidation. This parameters is used from the sklearn \
                    function GridSearchCV. \
                    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
            scoring (Sting, function): The value that defines the metrics for scoring the paths. \
                    Can be a string if sklearn defined metrics used. Can be a funtion if a user \
                    defined metric is used. This parameters is used from the sklearn function GridSearchCV. \
                    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
            stages (list of list of estimators): A list of list containing the transformer and \
                    estimator tuples for customizing the preconfigured auto pipeline.
            execution_time_per_pipeline (int): Integer value denoting time (minutes) of execution \
                    per path (path: combination of estimators and transformers)
            num_options_per_pipeline_for_random_search (int): Integer value denoting number \
                    of parameters to use while performing randomized param search in *which* rounds.
            num_option_per_pipeline_for_intelligent_search: Integer value denoting number of \
                    parameters to use while performing more intelligent param search in *which* rounds.
            total_execution_time (int): Total execution time (minutes) for the auto classification pipeline.
            param_grid (SROMParamGrid): Param grid with various parameter combination.
        """

        self.level = level
        self.save_prefix = save_prefix
        self.execution_platform = execution_platform
        self.cv = cv
        self.scoring = scoring
        self.stages = stages
        self.execution_time_per_pipeline = execution_time_per_pipeline
        self.num_options_per_pipeline_for_random_search = (
            num_options_per_pipeline_for_random_search
        )
        self.num_option_per_pipeline_for_intelligent_search = (
            num_option_per_pipeline_for_intelligent_search
        )
        self.total_execution_time = total_execution_time
        self.bayesian_paramgrid = bayesian_paramgrid
        self.rbopt_paramgrid = rbopt_paramgrid
        self.enable_autoai = False

        # internal parameters to be optimized in subsequent phase
        self._top_k_bottom_nodes = 3
        self._top_k_paths = 3
        self.best_estimator_so_far = None
        self.best_score_so_far = None
        self.explored_estimator = []
        self.explored_score = []
        self.csv_filename = ""
        self.dill_filename = ""
        self.estimator_id = 1
        self.best_path_info = None
        self.number_of_combinations = 0
        self.successive_halve_factor = 0.5
        self.suffix = ""

        # check total_execution_time and execution_time_per_pipeline before execution
        if self.total_execution_time == -1:  # total_execution_time is unrestricted
            pass
        # execution_time_per_pipeline is restricted but total_execution_time is not restricted
        elif self.execution_time_per_pipeline == -1:
            raise ValueError(
                "execution_time_per_pipeline is restricted but total_execution_time is not restricted."
            )
        elif self.total_execution_time < self.execution_time_per_pipeline:
            raise ValueError(
                "total_execution_time={} is smaller than execution_time_per_pipeline={}.".format(
                    self.total_execution_time, self.execution_time_per_pipeline
                )
            )

        # setting execution environment
        if execution_platform == "spark":
            self.execution_platform = "spark_node_random_search"
        elif execution_platform == "serverless":
            self.execution_platform = "serverless_search"
        elif execution_platform == "ray":
            self.execution_platform = "ray_search"
        else:
            pass

        if execution_platform is None:
            self.execution_platform = "single_node_random_search"

        if param_grid is None:
            self.param_grid = SROMParamGrid(gridtype="empty")
        else:
            self.param_grid = param_grid

        self._evn_config = {}
        self.additional_stages = None

        # added a few more internal parameter
        self._pipeline_type = Pipeline
        self._pipeline_init_param = {}

        # added an internal parameter, we will externalize it soon
        self._random_state = 33
        self._num_raondom_points = 100000
        self._internal_queue = None
        self._internal_queue_pointer = -1

    def set_pipeline_type_for_path(self, pipeline_type):
        """
            Set pipeline type for path method.
        """
        self._pipeline_type = pipeline_type

    def set_pipeline_init_param_for_path(self, pipeline_init_param):
        """
            Set pipeline initialize param for path
        """
        self._pipeline_init_param = pipeline_init_param

    def set_environment_config(self, evn_conf):
        """
        The configuration setting for lithops, code engine, cloud function
        """
        self._evn_config = evn_conf

    def _get_next_random_number(self):
        """
        This method is added to provide a sequence of random numbers
        for parameter generation process
        """
        if not self._internal_queue:
            # create it first
            random.seed(self._random_state)

            elements_seed = list(range(self._num_raondom_points))
            random.shuffle(elements_seed)
            self._internal_queue_pointer = -1
            self._internal_queue = []
            for item in elements_seed:
                self._internal_queue.append(item)

        if self._internal_queue_pointer == self._num_raondom_points:
            raise Exception("Not Implemented")
        else:
            self._internal_queue_pointer += 1
            return self._internal_queue[self._internal_queue_pointer]

    def _init_pipeline(self, stages=None):
        """
        This is a central point for the initialization
        """
        self.auto_pipeline = SROMPipeline()
        self.auto_pipeline.set_cross_validation(self.cv)
        self.auto_pipeline.set_scoring(self.scoring)
        if self._evn_config:
            self.auto_pipeline.set_environment_config(self._evn_config)

        # this is added to support the custom pipeline
        self.set_pipeline_type_for_path(self._pipeline_type)
        self.set_pipeline_init_param_for_path(self._pipeline_init_param)

        # set default stages if custom stages not provided
        if stages is None:
            if self.stages is None:
                self.stages = self._initialize_default_stages()
            if self.execution_platform == "serverless_search":
                self.stages = replace_srom_classes(self.stages)
            self.auto_pipeline.set_stages(self.stages)
            check_custom_stage_random_state(self.stages)
        else:
            if self.execution_platform == "serverless_search":
                stages = replace_srom_classes(stages)
            self.auto_pipeline.set_stages(stages)
            check_custom_stage_random_state(stages)

    def _init_autoai_pipeline(self):
        """
        Initialize autoai pipeline in a pre-defined manner.
        """
        # this function shd prepare a
        # self.autoai_pipeline

        # this is left pending for future work
        # this we can even make more fancy
        # if user have provided a DAG explicitly, we can specify what estimators
        # user like to optimiza via AutoAI, but this is future todo
        from autoai_ts_libs.deps.srom.wml.AutoAIEstimator import AutoAIEstimator

        self.autoai_pipeline = AutoAIEstimator(
            self._evn_config.wml_credentials,
            self._evn_config.cos_credentials,
            self._evn_config.space_id,
            self._evn_config.target_column,
            self._evn_config.scoring,
            self._evn_config.prediction_type,
            self._evn_config.experiment_name,
            self._evn_config.background_mode,
            self._evn_config.t_shirt_size,
            self._evn_config.positive_label,
        )

    @abstractmethod
    def _initialize_default_stages(self):
        pass

    @abstractmethod
    def _initialize_additional_stages(self):
        pass

    @abstractmethod
    def summary(self, enable_param_grid=False):
        pass

    def get_model_info(self):
        """
        Retrive model information in the form of dictionary containing model_name,model_family and model_family.
        Returns:
            dict
        """
        model_name = "model_not_fitted"
        model_family = "sklearn"
        model_description = "model_not_fitted"
        info = {
            "model_name": model_name,
            "model_family": model_family,
            "model_description": model_description,
        }
        if self.best_estimator_so_far:
            model_name = get_pipeline_name(self.best_estimator_so_far)
            model_description = get_pipeline_description(self.best_estimator_so_far)
            info["model_name"] = model_name
            info["model_family"] = model_family
            info["model_description"] = model_description
            attrs = get_estimator_meta_attributes(
                self.best_estimator_so_far.steps[-1][1]
            )
            if attrs:
                info["attributes"] = attrs
            else:
                info["attributes"] = "cannot find/discover parameters"
        return info

    def _get_sklearn_str_repr(self, sk_pipeline):
        """
        Utility function to print out the string representation of sklearn pipeline
        """
        str_rep = "["
        for sI in sk_pipeline.steps:
            str_rep = str_rep + str(sI) + ","
        str_rep = str_rep + "]"
        return str_rep.replace(" ", "").replace("\n", "")

    def _generate_ML_graph(self, original_graph, best_pairs, pair_scores):
        """
        Generate ML graph.

        Parameters:
            original_graph: Original SROMPipeline.
            best_pairs: Pair of two nodes in SROMPipeline (path of lenght 2).
            pair_scores: Score of each pair in best_pairs.
        """
        c_name = {}
        stage_set = []
        best_scores = []

        # there may be some path of length 1, eliminate them
        # prepare c_name,
        # assuming last element is an estimators
        for item in best_pairs:
            if len(item.steps) > 1:
                c_name[item.steps[-1][0]] = item

        # identify the useful nodes w.r.t. each node in c_name and prepare graph
        # one graph for each terminal node
        for clf in c_name.keys():
            imp_nodes = []
            tmp_best_scores = []
            imp_nodes.append(clf)
            for item_i, item in enumerate(best_pairs):
                if len(item.steps) > 1:
                    # current assumption is we have length 2 node only
                    if item.steps[0][0] not in imp_nodes and item.steps[-1][0] == clf:
                        imp_nodes.append(item.steps[0][0])
                        tmp_best_scores.append(pair_scores[item_i])

            # prepare the graph
            modified_states = []
            for lvl_one_item in original_graph:
                tmp_itm = []
                for lvl_two_item in lvl_one_item:
                    if lvl_two_item[0] in imp_nodes:
                        tmp_itm.append(lvl_two_item)
                if len(tmp_itm) > 0:
                    modified_states.append(tmp_itm)

            stage_set.append(modified_states)
            best_scores.append(np.max(tmp_best_scores))
        return stage_set, best_scores

    def _detect_resource_aware_estimator_selection_round(
        self,
        num_activation,
        num_estimators,
        num_preprocessor,
        num_round_1_param,
        num_round_2_param,
        num_round_3_param,
        adjust_params=False,
    ):
        """
        This method identify which round to jump based on availability of the
        allocated resournces.
        round_1_limit/... - this is rough upper bound
        internally - it shd be weighed sampling than the fixed sampling
        Round 1, 2 or 3.
        """
        total_options = num_estimators * np.max([num_preprocessor, 1])
        round_1_limit = total_options * num_round_1_param
        round_2_limit = total_options * num_round_2_param
        round_3_limit = total_options * num_round_3_param

        if adjust_params:
            if num_activation > round_3_limit:
                return (
                    3,
                    num_round_1_param,
                    num_round_2_param,
                    int(
                        np.min(
                            [
                                int(np.floor(num_activation * 1.0 / total_options)),
                                int(num_round_3_param * 2),
                            ]
                        )
                    ),
                )
            elif num_activation > round_2_limit:
                return (
                    2,
                    num_round_1_param,
                    int(
                        np.min(
                            [
                                int(np.floor(num_activation * 1.0 / total_options)),
                                num_round_2_param * 2,
                            ]
                        )
                    ),
                    num_round_3_param,
                )
            elif num_activation > round_1_limit:
                return (
                    1,
                    int(
                        np.min(
                            [
                                int(np.floor(num_activation * 1.0 / total_options)),
                                num_round_1_param * 2,
                            ]
                        )
                    ),
                    num_round_2_param,
                    num_round_3_param,
                )
            else:
                return (1, num_round_1_param, num_round_2_param, num_round_3_param)
        else:
            if num_activation > round_3_limit:
                return 3, num_round_1_param, num_round_2_param, num_round_3_param
            elif num_activation > round_2_limit:
                return 2, num_round_1_param, num_round_2_param, num_round_3_param
            else:
                return 1, num_round_1_param, num_round_2_param, num_round_3_param

    def _detect_resource_aware_operator_selection_mode(
        self,
        num_activation,
        num_estimators,
        num_preprocessor,
        level_wise_operators,
        number_randomized,
    ):
        """
        This is now taking into account the other operator we have in the DAG
        This is for at max two combination
        The preprocessor and estimator does not have any parameter to be optimized
        """
        total_options = num_estimators * np.max([num_preprocessor, 1])
        # here we should also
        for lwopt in level_wise_operators:
            total_options += lwopt

        if num_activation > total_options:
            if num_activation > total_options * number_randomized:
                return 0  # with parameter - 4+5
            else:
                return 1  # only 4

        total_options /= num_estimators

        if num_activation > total_options:
            if num_activation > total_options * number_randomized:
                return 2  # with parameter - 4+5
            else:
                return 3  # only 4

        return 4

    def _detect_resource_aware_graph_exploration_mode(
        self, num_activation, tmp_graph, number_randomized, top_k_path
    ):
        """
        This is for a DAG: Shall we have one DAG and run it or Shall we run
        each DAG in turn and do parameter optimization
        """
        tmp_graph_size = []
        global_task_size = 0
        for grp in tmp_graph:
            total_task = 1
            for each_layer in grp:
                total_task *= len(each_layer)
            tmp_graph_size.append(total_task)
            global_task_size += total_task

        if len(tmp_graph_size) == 0:
            return 3

        max_tmp_graph_size = np.max(tmp_graph_size)

        if num_activation >= global_task_size * number_randomized:
            return 0

        if num_activation >= global_task_size:
            return 1

        if num_activation >= max_tmp_graph_size * number_randomized:
            return 2

        return 3

    def _update_best_estimator(self, estimator, score):
        """
        Updates the pipeline object internal list of best estimators with the \
        newer ones from the recently executed round.
        """
        if not score:
            return 0
        if score == None:
            return 0
        if np.isnan(score):
            return 0
        if self.best_estimator_so_far:
            if score > self.best_score_so_far:
                self.best_estimator_so_far = estimator
                self.best_score_so_far = score
        else:
            self.best_estimator_so_far = estimator
            self.best_score_so_far = score

    def _check_total_time_spend(self, experiment_start_time):
        """
        utility function to see the time-out
        """
        if self.total_execution_time == -1:  # if total_execution_time is unrestricted
            return False

        total_time_spent = (time.time() - experiment_start_time) / 60.0
        if (
            total_time_spent
            >= self.total_execution_time - self.execution_time_per_pipeline
        ):
            return True
        else:
            return False

    def _get_remaining_time(self, experiment_start_time):
        """get remaining time for pipeline execution

        Args:
            experiment_start_time (float): the timestamp when the experiment started
        """
        if self.total_execution_time == -1:  # if total_execution_time is unrestricted
            return -1

        total_time_spent = (time.time() - experiment_start_time) // 60.0

        if total_time_spent >= self.total_execution_time:
            return 0
        else:
            return math.ceil(self.total_execution_time - total_time_spent)

    def _set_explored_estimators(self, tmp_explored_estimator, tmp_explored_score):
        """
        utility function to set the explored estimators
        """
        self.explored_estimator = tmp_explored_estimator
        self.explored_score = tmp_explored_score

    def _get_stages_from_pipeline(self, imp_nodes):
        """
        it return name of the pipeline node
        """
        modified_states = []
        for lvl_one_item in self.auto_pipeline.stages:
            tmp_itm = []
            for lvl_two_item in lvl_one_item:
                if lvl_two_item[0] in imp_nodes:
                    tmp_itm.append(lvl_two_item)
            modified_states.append(tmp_itm)
        return modified_states

    def _flush_results_locally(
        self,
        pipeline,
        round_name,
        start_time,
        end_time,
        execution_time,
        save_condition=None,
    ):
        """
        Saves the results locally.

        Parameters:
            pipeline (SROMPipeline object): The trained pipeline with best estimators and best scores \
                    for each path.
            round_name (str): Name representing the round for which the results are to be flushed.
            execution_time (str): String denoting the time of execution of round.
            save_condition (float): If condition provided, then compare model with the condition score \
                    and store only if score more than `save_condition` value.
        """
        # flush the resuts
        f = open(self.csv_filename, "a+")

        # flush the round info
        best_estimator_str = (
            "None"
            if pipeline.best_estimator is None
            else self._get_sklearn_str_repr(pipeline.best_estimator)
        )
        f.write(
            round_name
            + " \t"
            + "round"
            + "\t"
            + str(execution_time)
            + "\t"
            + str(pipeline.best_score)
            + "\t"
            + best_estimator_str
            + "\t"
            + str(pipeline.number_of_combinations)
            + "\t"
            + str(pipeline.activations)
            + "\n"
        )

        i = 0
        result_i = 0
        for i, result_i in enumerate(pipeline.best_scores):
            execution_time = (
                None
                if pipeline.execution_time_for_best_estimators is None
                else pipeline.execution_time_for_best_estimators[i]
            )

            # store into best_path_info dictionary
            self.best_path_info["best_path"].append(
                {
                    "estimator_id": self.estimator_id,
                    "round": round_name,
                    "start_time": start_time,  # not correct
                    "end_time": end_time,  # not correct
                    "execution_time": execution_time,
                    "best_score": str(result_i),
                    "best_estimator": pipeline.best_estimators[i],
                    "best_params": {
                        j[0]: j[1].get_params()
                        for j in pipeline.best_estimators[i].steps
                    },
                }
            )

            # flush only if result is better
            if save_condition is None or result_i > save_condition:
                f.write(
                    round_name
                    + " \t"
                    + str(self.estimator_id)
                    + "\t"
                    + str(execution_time)
                    + "\t"
                    + str(result_i)
                    + "\t"
                    + self._get_sklearn_str_repr(pipeline.best_estimators[i])
                    + "\t\t\n"
                )

            # increment
            self.estimator_id += 1
        f.close()

    def export_pipeline_exploration_info(self):
        """This function is to expore the pipeline exploration information into dill file"""
        import dill

        with open(self.dill_filename, "wb") as dill_file:
            dill.dump(self.best_path_info, dill_file)

    def _explore_automate_default(self, X, y, verbosity="low"):
        """
        This option is to explore the number of automate paths in SROM Pipeline Style
        Complete Exploration of the DAG:
        """
        start_time = time.time()
        best_estimator, best_score = self.auto_pipeline.execute(
            X,
            y,
            exectype="spark_node_random_search",
            max_eval_time_minute=self.execution_time_per_pipeline,
            random_state=self._get_next_random_number(),
            verbosity=verbosity,
            total_execution_time=self._get_remaining_time(start_time),
        )
        self.number_of_combinations = self.auto_pipeline.number_of_combinations
        end_time = time.time()
        execution_time = (end_time - start_time) / 60.0
        self._update_best_estimator(best_estimator, best_score)

        # flush the resuts
        self._flush_results_locally(
            pipeline=self.auto_pipeline,
            round_name="1",
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_time,
            save_condition=None,
        )

        self.best_path_info["end_time"] = time.time()
        self.best_path_info["execution_time"] = (
            self.best_path_info["end_time"] - start_time
        )
        return self.best_estimator_so_far, self.best_score_so_far

    def _autoai_exploration(self, X, y):
        """
            here you can call the AutoAI-Estimators and get the list of pipelines
            that are explored
            it must be in sklearn style
            you shd get the score also
            unfortunately score are not comparable
            so we need to use internal train and test split to prepare a rank
            actually autoai- does provide the train and test split of the data
            we can evatually use that to get the final rank

            see _admm_style_exploration for how we prepare and return the above four
            list
        """
        tmp_explored_estimator = []
        tmp_explored_score = []
        best_scores_max = None
        paths_for_hp_tuning = []
        base_score_of_paths = []

        self.autoai_pipeline.fit(X, y)
        summary_df = self.auto_pipeline.summary()
        tmp_explored_estimator.append(self.autoai_pipeline.best_pipeline())
        # tmp_explored_score.append(summary_df.iloc[0].holdout_r2)

        try:
            key = "holdout_" + self._env_config["scoring"]
        except Exception:
            key = "holdout_r2"

        tmp_explored_score.append(summary_df.iloc[0].key)

        pipelines = self.autoai_pipeline.get_all_pipelines()
        pipeline_detail = self.autoai_pipeline.get_pipeline_details()
        for i in range(len(pipelines)):
            paths_for_hp_tuning.append(pipelines[i])
            base_score_of_paths.append(pipeline_detail.iloc[i].ml_metrics.iloc[8])

        return (
            tmp_explored_estimator,
            tmp_explored_score,
            paths_for_hp_tuning,
            base_score_of_paths,
        )

    def _admm_style_exploration(
        self,
        X,
        y,
        experiment_start_time,
        paths_for_hp_tuning_,
        tmp_explored_estimator_,
        verbosity,
    ):
        """
        This is ADMM style of exploration
        """
        imp_nodes = []
        est_nodes = []

        tmp_explored_estimator = []
        tmp_explored_score = []
        best_scores_max = self.best_score_so_far
        paths_for_hp_tuning = []
        base_score_of_paths = []

        # pipeline path
        for pipeline_path in paths_for_hp_tuning_:
            print(pipeline_path)
            if len(pipeline_path.steps) == 1:
                # this are the node that are already explored
                if pipeline_path.steps[-1][0] not in est_nodes:
                    est_nodes.append(pipeline_path.steps[-1][0])
            else:
                # this are the node that are operator going to be explored
                for pipeline_step in pipeline_path.steps[:-1]:
                    if pipeline_step[0] not in imp_nodes:
                        imp_nodes.append(pipeline_step[0])

        print(imp_nodes, est_nodes)
        # do not explore more than 10 operators
        if len(imp_nodes) == 0 or len(imp_nodes) > 10:
            return (
                tmp_explored_estimator,
                tmp_explored_score,
                paths_for_hp_tuning,
                base_score_of_paths,
            )

        # find out the remaining node
        remaining_est_nodes = []
        remaining_est_nodes_name = []
        for pipeline_path in tmp_explored_estimator_:
            print(pipeline_path, len(pipeline_path.steps))
            if len(pipeline_path.steps) == 1:
                if (
                    pipeline_path.steps[-1][0] not in est_nodes
                    and pipeline_path.steps[-1][0] not in remaining_est_nodes_name
                ):
                    remaining_est_nodes.append(pipeline_path.steps[-1])
                    remaining_est_nodes_name.append(pipeline_path.steps[-1][0])

        if len(remaining_est_nodes) == 0:
            return (
                tmp_explored_estimator,
                tmp_explored_score,
                paths_for_hp_tuning,
                base_score_of_paths,
            )

        # prepare the graph
        modified_states = []
        for lvl_one_item in self.stages[:-1]:
            tmp_itm = []
            for lvl_two_item in lvl_one_item:
                tmp_itm.append(lvl_two_item)
            if len(tmp_itm) > 0:
                modified_states.append(tmp_itm)

        if len(modified_states) == 0:
            return (
                tmp_explored_estimator,
                tmp_explored_score,
                paths_for_hp_tuning,
                base_score_of_paths,
            )

        modified_states.append(remaining_est_nodes)

        # find nodes other than the leaf node (take paths having lenght > 1)
        # if above is empty then no need to travel any thing
        # find leaf nodes that are not explored
        # make a DAG:

        graph_exploration_mode = self._detect_resource_aware_graph_exploration_mode(
            self._evn_config["TUNING_PARAM"]["activations_limit"],
            [modified_states],
            self.num_options_per_pipeline_for_random_search,
            self._top_k_paths,
        )
        print(modified_states)

        # graph exploration mode
        self._init_pipeline(modified_states)
        if graph_exploration_mode == 0:
            num_options_per_pipeline_for_random_search = (
                self.num_options_per_pipeline_for_random_search
            )
        else:
            num_options_per_pipeline_for_random_search = 1

        fine_param_grid = self.param_grid

        start_time = time.time()
        best_estimator, best_score = self.auto_pipeline.execute(
            X,
            y,
            param_grid=fine_param_grid,
            exectype=self.execution_platform,
            max_eval_time_minute=self.execution_time_per_pipeline,
            random_state=self._get_next_random_number(),
            num_option_per_pipeline=num_options_per_pipeline_for_random_search,
            verbosity=verbosity,
            total_execution_time=self._get_remaining_time(experiment_start_time),
        )
        self.number_of_combinations += self.auto_pipeline.number_of_combinations
        end_time = time.time()
        execution_time = (end_time - start_time) / 60.0

        self._update_best_estimator(best_estimator, best_score)
        tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
        tmp_explored_score.extend(self.auto_pipeline.best_scores)
        for i, result_i in enumerate(self.auto_pipeline.best_scores):
            if result_i > best_scores_max:
                paths_for_hp_tuning.append(self.auto_pipeline.best_estimators[i])
                base_score_of_paths.append(result_i)

        # flushing the results
        self._flush_results_locally(
            pipeline=self.auto_pipeline,
            round_name="A_6",
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_time,
            save_condition=best_scores_max,
        )

        if (
            self._check_total_time_spend(experiment_start_time)
            or graph_exploration_mode == 0
        ):
            return (
                tmp_explored_estimator,
                tmp_explored_score,
                paths_for_hp_tuning,
                base_score_of_paths,
            )

        # start random exploration
        imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(self._top_k_paths)

        # As imp_nodes is a blank dictionary there is no point in processing further.
        if imp_nodes:

            modified_states = self._get_stages_from_pipeline(imp_nodes)
            try:
                check_srom_pipeline_stages(modified_states)
            except Exception:
                pass

            # update the states so now we only has limited states
            self._init_pipeline(modified_states)
            fine_param_grid = self.param_grid

            start_time = time.time()
            best_estimator, best_score = self.auto_pipeline.execute(
                X,
                y,
                param_grid=fine_param_grid,
                num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                exectype=self.execution_platform,
                max_eval_time_minute=self.execution_time_per_pipeline,
                random_state=self._get_next_random_number(),
                verbosity=verbosity,
                total_execution_time=self._get_remaining_time(experiment_start_time),
            )
            self.number_of_combinations += self.auto_pipeline.number_of_combinations
            end_time = time.time()
            execution_time = (end_time - start_time) / 60.0

            self._update_best_estimator(best_estimator, best_score)
            tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
            tmp_explored_score.extend(self.auto_pipeline.best_scores)
            for i, result_i in enumerate(self.auto_pipeline.best_scores):
                if result_i > best_scores_max:
                    paths_for_hp_tuning.append(self.auto_pipeline.best_estimators[i])
                    base_score_of_paths.append(result_i)

            # flushing the results
            self._flush_results_locally(
                pipeline=self.auto_pipeline,
                round_name="Ad_1",
                start_time=start_time,
                end_time=end_time,
                execution_time=execution_time,
                save_condition=best_scores_max,
            )

        return (
            tmp_explored_estimator,
            tmp_explored_score,
            paths_for_hp_tuning,
            base_score_of_paths,
        )

    def _resource_adaptive_automate(self, X, y, verbosity="low"):
        """
        This is work in progress to demonstrate the effect of increasing the
        available resources while executing the method
        """

        # starting value of model ID. Will be assigned to best estimators in order in every Round
        self.estimator_id = 1
        self.number_of_combinations = 0

        warnings.filterwarnings("ignore")
        warnings.simplefilter(action="ignore", category=FutureWarning)

        # creating file for storing result
        suffix = uuid.uuid4().hex
        csv_filename = suffix + ".csv"
        dill_filename = suffix + ".dill"

        # adjust name based on user req.
        if len(self.save_prefix) > 0:
            csv_filename = self.save_prefix + "_" + csv_filename
            dill_filename = self.save_prefix + "_" + dill_filename

        # you can't be sure you can always write
        # to a non system temp directory
        tempdir = gettempdir()
        tempdir = os.path.realpath(tempdir)
        csv_filename = str(Path(tempdir) / csv_filename)
        dill_filename = str(Path(tempdir) / dill_filename)

        # rare exception where we use print
        # to make sure user sees this
        if verbosity == "high":
            print("Output CSV: {}".format(csv_filename))
            print("Output JSON: {}".format(dill_filename))
            LOGGER.info("Output CSV: {}".format(csv_filename))
            LOGGER.info("Output JSON: {}".format(dill_filename))

        # saving file name to csv and dill
        self.csv_filename = csv_filename
        self.dill_filename = dill_filename

        # creating header in csv_filename result file
        f = open(self.csv_filename, "a+")
        f.write(
            "round\testimator_id\texecution_time_minutes\tbest_scores\tbest_estimator\tn_pipelines\tactivation_list\n"
        )
        f.close()

        # store the intermediate results
        tmp_explored_estimator = []
        tmp_explored_score = []

        # store overall path info
        self.best_path_info = {"experiment_id": uuid.uuid4().hex, "best_path": []}
        experiment_start_time = time.time()
        self.best_path_info["start_time"] = experiment_start_time

        # start with an SROM Pipeline
        self._init_pipeline(self.stages)

        # execute it - this is a default srom path
        # check with tipu to clarify
        if self.execution_platform == "default":
            return self._explore_automate_default(X, y, verbosity)

        # function call to learn the resources req.
        (
            option,
            num_round_1_param,
            num_round_2_param,
            num_round_3_param,
        ) = self._detect_resource_aware_estimator_selection_round(
            self._evn_config["TUNING_PARAM"]["activations_limit"],
            len(self.stages[-1]),
            0,
            1,
            self.num_options_per_pipeline_for_random_search,
            self.num_options_per_pipeline_for_random_search * 2,
            adjust_params=True,
        )

        num_parameter_to_tune = 1
        if option == 1:
            num_parameter_to_tune = num_round_1_param
        elif option == 2:
            num_parameter_to_tune = num_round_2_param
        elif option == 3:
            num_parameter_to_tune = num_round_3_param
        else:
            pass

        #####################################
        # Round 1/2/3, Just run the initial round
        #####################################
        # execute the default layer - prepare a pipeline using last layer and identify best estimators

        total_nodes = len(self.stages[-1])
        self.auto_pipeline.set_stages([self.stages[-1]])
        fine_param_grid = self.param_grid

        start_time = time.time()
        best_estimator, best_score = self.auto_pipeline.execute(
            X,
            y,
            exectype=self.execution_platform,
            param_grid=fine_param_grid,
            max_eval_time_minute=self.execution_time_per_pipeline,
            num_option_per_pipeline=num_parameter_to_tune,
            upload_data=True,
            random_state=self._get_next_random_number(),
            verbosity=verbosity,
            total_execution_time=self._get_remaining_time(experiment_start_time),
        )

        # execution time in minutes
        self.number_of_combinations = self.auto_pipeline.number_of_combinations
        end_time = time.time()
        execution_time = (end_time - start_time) / 60.0

        # storing and updating the results (just first stages)
        tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
        tmp_explored_score.extend(self.auto_pipeline.best_scores)
        self._update_best_estimator(best_estimator, best_score)

        if best_score is None or np.isnan(best_score):
            LOGGER.info("Cannot run further. check the execution log for a error.")
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            return None, None

        # flush the resuts
        self._flush_results_locally(
            pipeline=self.auto_pipeline,
            round_name=str(option),
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_time,
            save_condition=None,
        )

        # return best estimator if user total execution time is over.
        if self._check_total_time_spend(experiment_start_time):
            self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            return self.best_estimator_so_far, self.best_score_so_far

        # put an extra check
        if sum(np.isnan(np.array(tmp_explored_score))) == len(tmp_explored_estimator):
            LOGGER.info(
                "Increase execution_time_per_pipeline or total_execution_time if your datasize is big"
            )
            return None, None

        #####################################
        # Round 2, if option was 1, we follow a default method
        #####################################
        # Select 50%, execute top 50% performer for random param grid
        # in future, we should adjust these based on remaining time and execution time of individual node
        if option == 1:
            top_k_path_selections = math.ceil(
                total_nodes * self.successive_halve_factor
            )
            num_options_per_pipeline_for_random_search = (
                self.num_options_per_pipeline_for_random_search
            )
            imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(
                top_k_path_selections
            )

            # As imp_nodes is a blank dictionary there is no point in processing further.
            if not imp_nodes:
                return self.best_estimator_so_far, self.best_score_so_far

            modified_states = self._get_stages_from_pipeline(imp_nodes)

            # update the states so now we only have limited states
            self._init_pipeline(modified_states)
            fine_param_grid = self.param_grid

            start_time = time.time()
            best_estimator, best_score = self.auto_pipeline.execute(
                X,
                y,
                param_grid=fine_param_grid,
                num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                exectype=self.execution_platform,
                max_eval_time_minute=self.execution_time_per_pipeline,
                random_state=self._get_next_random_number(),
                verbosity=verbosity,
                total_execution_time=self._get_remaining_time(experiment_start_time),
            )
            self.number_of_combinations += self.auto_pipeline.number_of_combinations
            end_time = time.time()
            execution_time = (end_time - start_time) / 60.0

            # storing and updating the results
            tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
            tmp_explored_score.extend(self.auto_pipeline.best_scores)
            self._update_best_estimator(best_estimator, best_score)

            # flush the resuts
            self._flush_results_locally(
                pipeline=self.auto_pipeline,
                round_name="2",
                start_time=start_time,
                end_time=end_time,
                execution_time=execution_time,
                save_condition=None,
            )

            # check if execution has exceded maximum time
            if self._check_total_time_spend(experiment_start_time):
                self._set_explored_estimators(
                    tmp_explored_estimator, tmp_explored_score
                )
                self.best_path_info["end_time"] = time.time()
                self.best_path_info["execution_time"] = (
                    self.best_path_info["end_time"] - experiment_start_time
                )
                return self.best_estimator_so_far, self.best_score_so_far
        elif option == 2:
            # incase the option is 2, then we can set the value
            # this way we can run the round 3
            top_k_path_selections = math.ceil(
                total_nodes * self.successive_halve_factor
            )
        elif option == 3:
            # incase the option is 3, then we can
            top_k_path_selections = 0
        else:
            raise Exception("Unknown Value : Option")

        #####################################
        # Round 3 (this will be executed only when the option is 1 or 2)
        #####################################
        # execute top-top-25% with more random parameters
        top_k_path_selections = math.ceil(
            top_k_path_selections * self.successive_halve_factor
        )
        num_options_per_pipeline_for_random_search = (
            self.num_options_per_pipeline_for_random_search * 2
        )

        imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(
            top_k_path_selections
        )

        # process round 3 only
        # if imp_nodes has some values.
        if imp_nodes:
            modified_states = self._get_stages_from_pipeline(imp_nodes)

            # update the states so now we only has limited states
            self._init_pipeline(modified_states)
            fine_param_grid = self.param_grid

            start_time = time.time()
            best_estimator, best_score = self.auto_pipeline.execute(
                X,
                y,
                param_grid=fine_param_grid,
                num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                exectype=self.execution_platform,
                max_eval_time_minute=self.execution_time_per_pipeline,
                random_state=self._get_next_random_number(),
                verbosity=verbosity,
                total_execution_time=self._get_remaining_time(experiment_start_time),
            )
            self.number_of_combinations += self.auto_pipeline.number_of_combinations
            end_time = time.time()
            execution_time = (end_time - start_time) / 60.0

            # storing and updating the results
            tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
            tmp_explored_score.extend(self.auto_pipeline.best_scores)
            self._update_best_estimator(best_estimator, best_score)

            # flush the resuts
            self._flush_results_locally(
                pipeline=self.auto_pipeline,
                round_name="3",
                start_time=start_time,
                end_time=end_time,
                execution_time=execution_time,
                save_condition=None,
            )

        # check if execution has exceded maximum time
        if self._check_total_time_spend(experiment_start_time):
            self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            return self.best_estimator_so_far, self.best_score_so_far

        """
        This is a place where we finished the round 1/2/3.
        Now we select the best models. We now follow simple ADMM style
        Select x number of estimators (self._top_k_bottom_nodes)
        """

        # now we have understanding what base algorithm works
        indices, _ = zip(*sorted(enumerate(tmp_explored_score), key=itemgetter(1)))
        explored_estimator = []
        paths_for_hp_tuning = []
        base_score_of_paths = []
        tmp_tmp_explored_estimator = []
        tmp_tmp_explored_score = []

        # time to make decision 2
        # self._top_k_bottom_nodes
        level_wise_operators = [len(stg_lvl) for stg_lvl in self.stages[:-1]]
        for k in indices[::-1]:
            if tmp_explored_estimator[k].steps[0][0] in explored_estimator:
                continue
            if tmp_explored_score[k] == np.NaN or np.isnan(tmp_explored_score[k]):
                continue

            explored_estimator.append(tmp_explored_estimator[k].steps[0][0])
            paths_for_hp_tuning.append(tmp_explored_estimator[k])
            base_score_of_paths.append(tmp_explored_score[k])

            if len(explored_estimator) >= self._top_k_bottom_nodes:
                break

        num_selected_bottom_nodes = len(explored_estimator)
        round_4_5_options = self._detect_resource_aware_operator_selection_mode(
            self._evn_config["TUNING_PARAM"]["activations_limit"],
            num_selected_bottom_nodes,
            0,
            level_wise_operators,
            self.num_options_per_pipeline_for_random_search,
        )
        # this one will tells the options
        # the following code automatically unroll as many path

        # find best node (note that there are None and Nan also exists)
        for k in range(num_selected_bottom_nodes):

            # this is an issue that we may think in detail (is it best score of a path or global)
            # tmp_baseline_score = base_score_of_paths[k]
            # little strict control
            tmp_baseline_score = np.max(base_score_of_paths[:num_selected_bottom_nodes])

            # each layer one after another
            for i in range(len(self.stages) - 1):

                #####################################
                # Round 4
                #####################################
                # select top-3
                num_options_per_pipeline_for_random_search = 1
                if round_4_5_options == 4:
                    # this is a default mode
                    # tmp_baseline_score = base_score_of_paths[k]
                    total_nodes = len(self.stages[i])
                    modified_states = [self.stages[i], paths_for_hp_tuning[k].steps]
                elif round_4_5_options == 2 or round_4_5_options == 3:
                    # this is a mode where we explore all the operators together
                    # tmp_baseline_score = base_score_of_paths[k]
                    level1_nodes = list(itertools.chain(*self.stages[:-1]))
                    level2_nodes = [paths_for_hp_tuning[k].steps[-1]]
                    total_nodes = len(level1_nodes)
                    modified_states = [level1_nodes, level2_nodes]
                    if round_4_5_options == 2:
                        num_options_per_pipeline_for_random_search = (
                            self.num_options_per_pipeline_for_random_search
                        )
                elif round_4_5_options == 0 or round_4_5_options == 1:
                    # this is a mode where we explore all the choices + estimators together
                    # tmp_baseline_score = np.max(base_score_of_paths)
                    level1_nodes = list(itertools.chain(*self.stages[:-1]))
                    level2_nodes = [
                        exp_estimator.steps[-1]
                        for exp_estimator in paths_for_hp_tuning[
                            :num_selected_bottom_nodes
                        ]
                    ]
                    total_nodes = len(level1_nodes)
                    modified_states = [level1_nodes, level2_nodes]
                    if round_4_5_options == 0:
                        num_options_per_pipeline_for_random_search = (
                            self.num_options_per_pipeline_for_random_search
                        )
                else:
                    raise Exception("Wrong Option")

                self._init_pipeline(modified_states)
                fine_param_grid = self.param_grid

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    exectype=self.execution_platform,
                    max_eval_time_minute=self.execution_time_per_pipeline,
                    random_state=self._get_next_random_number(),
                    num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_tmp_explored_score.extend(self.auto_pipeline.best_scores)
                for i, result_i in enumerate(self.auto_pipeline.best_scores):
                    if result_i > tmp_baseline_score:
                        paths_for_hp_tuning.append(
                            self.auto_pipeline.best_estimators[i]
                        )
                        base_score_of_paths.append(result_i)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="4",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=tmp_baseline_score,
                )

                if self._check_total_time_spend(experiment_start_time):
                    break

                # parameter is already explored in the previous round.
                if round_4_5_options == 0 or round_4_5_options == 2:
                    break

                #####################################
                # Round 5
                #####################################
                top_k_path_selections = math.ceil(
                    total_nodes * self.successive_halve_factor
                )
                num_options_per_pipeline_for_random_search = (
                    self.num_options_per_pipeline_for_random_search
                )
                imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(
                    top_k_path_selections
                )

                # this is inside a for loop
                # So, we should process only if the imp_nodes has a values.
                if imp_nodes:

                    modified_states = self._get_stages_from_pipeline(imp_nodes)

                    # update the states so now we only has limited states
                    self._init_pipeline(modified_states)
                    fine_param_grid = self.param_grid

                    start_time = time.time()
                    best_estimator, best_score = self.auto_pipeline.execute(
                        X,
                        y,
                        param_grid=fine_param_grid,
                        num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                        exectype=self.execution_platform,
                        max_eval_time_minute=self.execution_time_per_pipeline,
                        random_state=self._get_next_random_number(),
                        verbosity=verbosity,
                        total_execution_time=self._get_remaining_time(
                            experiment_start_time
                        ),
                    )
                    self.number_of_combinations += (
                        self.auto_pipeline.number_of_combinations
                    )
                    end_time = time.time()
                    execution_time = (end_time - start_time) / 60.0

                    self._update_best_estimator(best_estimator, best_score)
                    tmp_tmp_explored_estimator.extend(
                        self.auto_pipeline.best_estimators
                    )
                    tmp_tmp_explored_score.extend(self.auto_pipeline.best_scores)
                    for i, result_i in enumerate(self.auto_pipeline.best_scores):
                        if result_i > tmp_baseline_score:
                            paths_for_hp_tuning.append(
                                self.auto_pipeline.best_estimators[i]
                            )
                            base_score_of_paths.append(result_i)

                    # flushing the results
                    self._flush_results_locally(
                        pipeline=self.auto_pipeline,
                        round_name="5",
                        start_time=start_time,
                        end_time=end_time,
                        execution_time=execution_time,
                        save_condition=tmp_baseline_score,
                    )

                if self._check_total_time_spend(experiment_start_time):
                    break

                # we already explored all the stages together
                if round_4_5_options == 1 or round_4_5_options == 3:
                    break

            if self._check_total_time_spend(experiment_start_time):
                break

            # all the extream exploration is done
            if round_4_5_options == 0 or round_4_5_options == 1:
                break

        """
        -------------------------------------
        Operator Selection round is Completed.
        -------------------------------------
        Round 6, 6-1.
        """

        tmp_explored_estimator.extend(tmp_tmp_explored_estimator)
        tmp_explored_score.extend(tmp_tmp_explored_score)
        tmp_tmp_explored_estimator = []
        tmp_tmp_explored_score = []

        if self._check_total_time_spend(experiment_start_time):
            self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            return self.best_estimator_so_far, self.best_score_so_far

        # prepare graph
        # process it further - explore graph
        # you will get many srom graphs, and expected best_score
        tmpGraphs, best_scores = self._generate_ML_graph(
            self.stages, paths_for_hp_tuning, base_score_of_paths
        )

        graph_exploration_mode = self._detect_resource_aware_graph_exploration_mode(
            self._evn_config["TUNING_PARAM"]["activations_limit"],
            tmpGraphs,
            self.num_options_per_pipeline_for_random_search,
            self._top_k_paths,
        )

        for tmp_index, tmp_graph in enumerate(tmpGraphs):

            # across all the best score
            best_scores_max = np.max(best_scores)

            # graph exploration mode
            if graph_exploration_mode == 0 or graph_exploration_mode == 1:
                self._init_pipeline(tmp_graph)
                for tmp_index_i in range(tmp_index, len(tmpGraphs)):
                    self.auto_pipeline.sromgraph.add_stages(tmpGraphs[tmp_index_i])
                if graph_exploration_mode == 0:
                    num_options_per_pipeline_for_random_search = (
                        self.num_options_per_pipeline_for_random_search
                    )
                else:
                    num_options_per_pipeline_for_random_search = 1
                # add remaining nodes
            elif graph_exploration_mode == 2:
                # no need of next step: parameter optimization together
                self._init_pipeline(tmp_graph)
                num_options_per_pipeline_for_random_search = (
                    self.num_options_per_pipeline_for_random_search
                )
            elif graph_exploration_mode == 3:
                self._init_pipeline(tmp_graph)
                num_options_per_pipeline_for_random_search = 1
            else:
                raise Exception("Wrong Choice")

            fine_param_grid = self.param_grid

            start_time = time.time()
            best_estimator, best_score = self.auto_pipeline.execute(
                X,
                y,
                param_grid=fine_param_grid,
                exectype=self.execution_platform,
                max_eval_time_minute=self.execution_time_per_pipeline,
                random_state=self._get_next_random_number(),
                num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                verbosity=verbosity,
                total_execution_time=self._get_remaining_time(experiment_start_time),
            )
            self.number_of_combinations += self.auto_pipeline.number_of_combinations
            end_time = time.time()
            execution_time = (end_time - start_time) / 60.0

            self._update_best_estimator(best_estimator, best_score)
            tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
            tmp_explored_score.extend(self.auto_pipeline.best_scores)
            for i, result_i in enumerate(self.auto_pipeline.best_scores):
                if result_i > best_scores_max:
                    paths_for_hp_tuning.append(self.auto_pipeline.best_estimators[i])
                    base_score_of_paths.append(result_i)

            # flushing the results
            self._flush_results_locally(
                pipeline=self.auto_pipeline,
                round_name="6",
                start_time=start_time,
                end_time=end_time,
                execution_time=execution_time,
                save_condition=best_scores_max,
            )

            if self._check_total_time_spend(experiment_start_time):
                self._set_explored_estimators(
                    tmp_explored_estimator, tmp_explored_score
                )
                self.best_path_info["end_time"] = time.time()
                self.best_path_info["execution_time"] = (
                    self.best_path_info["end_time"] - experiment_start_time
                )
                return self.best_estimator_so_far, self.best_score_so_far

            if graph_exploration_mode == 2:
                continue

            if graph_exploration_mode == 0:
                break

            # start random exploration
            imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(
                self._top_k_paths
            )

            # As imp_nodes is a blank dictionary there is no point in processing further.
            if imp_nodes:

                modified_states = self._get_stages_from_pipeline(imp_nodes)

                try:
                    check_srom_pipeline_stages(modified_states)
                except Exception:
                    continue

                # update the states so now we only has limited states
                self._init_pipeline(modified_states)
                fine_param_grid = self.param_grid

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                    exectype=self.execution_platform,
                    max_eval_time_minute=self.execution_time_per_pipeline,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_explored_score.extend(self.auto_pipeline.best_scores)
                for i, result_i in enumerate(self.auto_pipeline.best_scores):
                    if result_i > best_scores_max:
                        paths_for_hp_tuning.append(
                            self.auto_pipeline.best_estimators[i]
                        )
                        base_score_of_paths.append(result_i)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="6_1",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=best_scores_max,
                )

            if self._check_total_time_spend(experiment_start_time):
                self._set_explored_estimators(
                    tmp_explored_estimator, tmp_explored_score
                )
                self.best_path_info["end_time"] = time.time()
                self.best_path_info["execution_time"] = (
                    self.best_path_info["end_time"] - experiment_start_time
                )
                return self.best_estimator_so_far, self.best_score_so_far

            if graph_exploration_mode == 1:
                break

        #####################################
        # ADMM Style Accelerator
        # 1. Replace Estimators
        # just find the other three estimators and make a graph
        # In active development
        #####################################

        (
            tmp_explored_estimator_,
            tmp_explored_score_,
            paths_for_hp_tuning_,
            base_score_of_paths_,
        ) = self._admm_style_exploration(
            X,
            y,
            experiment_start_time,
            paths_for_hp_tuning,
            tmp_explored_estimator,
            verbosity,
        )

        if len(tmp_explored_estimator) > 0:
            tmp_explored_estimator.extend(tmp_explored_estimator_)
            tmp_explored_score.extend(tmp_explored_score_)

        if len(paths_for_hp_tuning_) > 0:
            paths_for_hp_tuning.extend(paths_for_hp_tuning_)
            base_score_of_paths.extend(base_score_of_paths_)

        if self._check_total_time_spend(experiment_start_time):
            self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            return self.best_estimator_so_far, self.best_score_so_far

        #####################################
        # Intelligent Optimization
        #####################################

        if self.level == "comprehensive":
            num_option_per_pipeline_for_intelligent_search = (
                self.num_option_per_pipeline_for_intelligent_search
            )
            execution_time_per_pipeline_for_intelligent_search = (
                self.execution_time_per_pipeline
            )
            if (
                num_option_per_pipeline_for_intelligent_search
                > num_options_per_pipeline_for_random_search
            ):
                factor = (int)(
                    num_option_per_pipeline_for_intelligent_search
                    / num_options_per_pipeline_for_random_search
                )
                execution_time_per_pipeline_for_intelligent_search *= factor

            # Genetic Optimization
            for path in paths_for_hp_tuning:
                # create a SROM pipeline with single path
                stages = []
                for item in path.steps:
                    stages.append([item])
                self._init_pipeline(stages)
                execution_platform = "evolutionary_search"
                fine_param_grid = self.param_grid

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    num_option_per_pipeline=num_option_per_pipeline_for_intelligent_search,
                    exectype=execution_platform,
                    max_eval_time_minute=execution_time_per_pipeline_for_intelligent_search,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_explored_score.extend(self.auto_pipeline.best_scores)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="genetic",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=None,
                )

                if self._check_total_time_spend(experiment_start_time):
                    self._set_explored_estimators(
                        tmp_explored_estimator, tmp_explored_score
                    )
                    self.best_path_info["end_time"] = time.time()
                    self.best_path_info["execution_time"] = (
                        self.best_path_info["end_time"] - experiment_start_time
                    )
                    return self.best_estimator_so_far, self.best_score_so_far

            # Bayesian Optimization
            for path in paths_for_hp_tuning:
                # create a SROM pipeline with single path
                stages = []
                for item in path.steps:
                    stages.append([item])
                self._init_pipeline(stages)
                execution_platform = "bayesian_search"
                fine_param_grid = SROMParamGrid()
                fine_param_grid.set_param_grid(self.bayesian_paramgrid)

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    num_option_per_pipeline=num_option_per_pipeline_for_intelligent_search,
                    exectype=execution_platform,
                    max_eval_time_minute=execution_time_per_pipeline_for_intelligent_search,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_explored_score.extend(self.auto_pipeline.best_scores)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="bayesian",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=None,
                )

                if self._check_total_time_spend(experiment_start_time):
                    self._set_explored_estimators(
                        tmp_explored_estimator, tmp_explored_score
                    )
                    self.best_path_info["end_time"] = time.time()
                    self.best_path_info["execution_time"] = (
                        self.best_path_info["end_time"] - experiment_start_time
                    )
                    return self.best_estimator_so_far, self.best_score_so_far

            # Hyper-band Search
            for path in paths_for_hp_tuning:
                # create a SROM pipeline with single path
                stages = []
                for item in path.steps:
                    stages.append([item])
                self._init_pipeline(stages)
                execution_platform = "hyperband_search"
                fine_param_grid = self.param_grid

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    num_option_per_pipeline=num_option_per_pipeline_for_intelligent_search,
                    exectype=execution_platform,
                    max_eval_time_minute=execution_time_per_pipeline_for_intelligent_search,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_explored_score.extend(self.auto_pipeline.best_scores)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="hyperband",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=None,
                )

                if self._check_total_time_spend(experiment_start_time):
                    self._set_explored_estimators(
                        tmp_explored_estimator, tmp_explored_score
                    )
                    self.best_path_info["end_time"] = time.time()
                    self.best_path_info["execution_time"] = (
                        self.best_path_info["end_time"] - experiment_start_time
                    )
                    return self.best_estimator_so_far, self.best_score_so_far

            try:
                # RBFOpt
                for path in paths_for_hp_tuning:
                    # create a SROM pipeline with single path
                    stages = []
                    for item in path.steps:
                        stages.append([item])
                    self._init_pipeline(stages)
                    execution_platform = "rbfopt_search"
                    fine_param_grid = SROMParamGrid()
                    fine_param_grid.set_param_grid(self.rbopt_paramgrid)

                    start_time = time.time()
                    best_estimator, best_score = self.auto_pipeline.execute(
                        X,
                        y,
                        param_grid=fine_param_grid,
                        num_option_per_pipeline=num_option_per_pipeline_for_intelligent_search,
                        exectype=execution_platform,
                        max_eval_time_minute=execution_time_per_pipeline_for_intelligent_search,
                        random_state=self._get_next_random_number(),
                        verbosity=verbosity,
                        total_execution_time=self._get_remaining_time(
                            experiment_start_time
                        ),
                    )
                    end_time = time.time()
                    execution_time = (end_time - start_time) / 60.0
                    self.number_of_combinations += (
                        self.auto_pipeline.number_of_combinations
                    )

                    self._update_best_estimator(best_estimator, best_score)
                    tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                    tmp_explored_score.extend(self.auto_pipeline.best_scores)

                    # flushing the results
                    self._flush_results_locally(
                        pipeline=self.auto_pipeline,
                        round_name="rbf_opt",
                        start_time=start_time,
                        end_time=end_time,
                        execution_time=execution_time,
                        save_condition=None,
                    )

                    if self._check_total_time_spend(experiment_start_time):
                        self._set_explored_estimators(
                            tmp_explored_estimator, tmp_explored_score
                        )
                        self.best_path_info["end_time"] = time.time()
                        self.best_path_info["execution_time"] = (
                            self.best_path_info["end_time"] - experiment_start_time
                        )
                        return self.best_estimator_so_far, self.best_score_so_far
            except Exception as ex:
                LOGGER.exception(ex)
        self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
        self.best_path_info["end_time"] = time.time()
        self.best_path_info["execution_time"] = (
            self.best_path_info["end_time"] - experiment_start_time
        )
        return self.best_estimator_so_far, self.best_score_so_far

    def _automate_setup(self):
        """
            Method automate setup for environment setup.
        """
        if self.execution_platform == "serverless_search":
            if len(self._evn_config) == 0:
                raise Exception("Environment config is not set.")

            if "COS_CREDS" not in self._evn_config.keys():
                raise Exception("No COS_CREDS information is provided.")

            # add suffix to env config
            self._evn_config["COS_CREDS"]["suffix"] = self.suffix
            self.auto_pipeline.set_environment_config(self._evn_config)

    def _automate_clean(self):
        """ 
            Method autumate clean to clean the environment setup.
        """
        if self.execution_platform == "serverless_search":
            X_filename = "X_" + self.suffix
            y_filename = "y_" + self.suffix

            # delete local X and y
            os.remove(X_filename + ".csv.gz")
            os.remove(y_filename + ".csv.gz")

            # delete X and y in COS
            if "COS_CREDS" not in self._evn_config.keys():
                raise Exception("No COS_CREDS information is provided.")

            from autoai_ts_libs.deps.srom.utils.s3utils import boto3client

            # TODO: remove hardcoded param
            cos_client = boto3client(
                self._evn_config["COS_CREDS"],
                resiliency="regional",
                region="us-south",
                public=True,
                location="us-south",
            )
            cos_client.delete_object(
                Bucket=self._evn_config["COS_CREDS"]["bucket"], Key=X_filename
            )
            cos_client.delete_object(
                Bucket=self._evn_config["COS_CREDS"]["bucket"], Key=y_filename
            )

    @abstractmethod
    def automate(self, X, y, verbosity="low"):
        """
            Automate method 
        """

        if verbosity not in ["low", "medium", "high"]:
            raise ValueError("Value of verbosity parameter is wrong!")

        # transfer the call
        if self._evn_config and "TUNING_PARAM" in self._evn_config.keys():
            if "adaptive_execution" in self._evn_config["TUNING_PARAM"].keys():
                if self._evn_config["TUNING_PARAM"]["adaptive_execution"]:
                    return self._resource_adaptive_automate(X, y, verbosity)

        # starting value of model ID. Will be assigned to best estimators in order in every Round
        self.estimator_id = 1
        self.number_of_combinations = 0

        warnings.filterwarnings("ignore")
        warnings.simplefilter(action="ignore", category=FutureWarning)

        # creating file for storing result
        suffix = uuid.uuid4().hex
        self.suffix = str(suffix)
        csv_filename = suffix + ".csv"
        dill_filename = suffix + ".dill"

        if len(self.save_prefix) > 0:
            csv_filename = self.save_prefix + "_" + csv_filename
            dill_filename = self.save_prefix + "_" + dill_filename

        # you can't be sure you can always write
        # to a non system temp directory
        tempdir = gettempdir()
        tempdir = os.path.realpath(tempdir)
        csv_filename = str(Path(tempdir) / csv_filename)
        dill_filename = str(Path(tempdir) / dill_filename)

        # rare exception where we use print
        # to make sure user sees this
        if verbosity == "high":
            print("Output CSV: {}".format(csv_filename))
            print("Output JSON: {}".format(dill_filename))
            LOGGER.info("Output CSV: {}".format(csv_filename))
            LOGGER.info("Output JSON: {}".format(dill_filename))

        self.csv_filename = csv_filename
        self.dill_filename = dill_filename

        # creating header in csv_filename result file
        f = open(self.csv_filename, "a+")
        f.write(
            "round\testimator_id\texecution_time_minutes\tbest_scores\tbest_estimator\tn_pipelines\tactivation_list\n"
        )
        f.close()

        # store the intermediate results
        tmp_explored_estimator = []
        tmp_explored_score = []

        # store overall path info
        self.best_path_info = {"experiment_id": uuid.uuid4().hex, "best_path": []}
        experiment_start_time = time.time()
        self.best_path_info["start_time"] = experiment_start_time

        # start with an SROM Pipeline
        self._init_pipeline(self.stages)
        self._automate_setup()

        # execute it - this is a default srom path
        if self.execution_platform == "default":
            self._automate_clean()
            return self._explore_automate_default(X, y, verbosity)

        #####################################
        # Round 1
        #####################################
        # execute the default layer - prepare a pipeline using last layer and identify best estimators

        total_nodes = len(self.stages[-1])
        self.auto_pipeline.set_stages([self.stages[-1]])
        fine_param_grid = self.param_grid

        start_time = time.time()
        best_estimator, best_score = self.auto_pipeline.execute(
            X,
            y,
            exectype=self.execution_platform,
            param_grid=fine_param_grid,
            max_eval_time_minute=self.execution_time_per_pipeline,
            num_option_per_pipeline=1,
            upload_data=True,
            random_state=self._get_next_random_number(),
            verbosity=verbosity,
            total_execution_time=self._get_remaining_time(experiment_start_time),
        )

        # execution time in minutes
        self.number_of_combinations = self.auto_pipeline.number_of_combinations
        end_time = time.time()
        execution_time = (end_time - start_time) / 60.0

        # storing and updating the results (just first stages)
        tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
        tmp_explored_score.extend(self.auto_pipeline.best_scores)
        self._update_best_estimator(best_estimator, best_score)

        if best_score is None or np.isnan(best_score):
            LOGGER.info("Cannot run further. check the execution log for a error.")
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            self._automate_clean()

            return None, None

        # flush the resuts
        self._flush_results_locally(
            pipeline=self.auto_pipeline,
            round_name="1",
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_time,
            save_condition=None,
        )

        # return best estimator if user total execution time is over.
        if self._check_total_time_spend(experiment_start_time):
            self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            self._automate_clean()

            return self.best_estimator_so_far, self.best_score_so_far

        # put an extra check
        if sum(np.isnan(np.array(tmp_explored_score))) == len(tmp_explored_estimator):
            LOGGER.info(
                "Increase execution_time_per_pipeline or total_execution_time if your datasize is big"
            )
            self._automate_clean()

            return None, None

        #####################################
        # Round 2
        #####################################
        # Select 50%, execute top 50% performer for random param grid
        # in future, we should adjust these based on remaining time and execution time of individual node
        top_k_path_selections = math.ceil(total_nodes * self.successive_halve_factor)
        num_options_per_pipeline_for_random_search = (
            self.num_options_per_pipeline_for_random_search
        )
        imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(
            top_k_path_selections
        )

        # this is not happening at See Line 373 to 377.
        # As imp_nodes is a blank dictionary there is no point in processing further.
        if not imp_nodes:
            self._automate_clean()

            return self.best_estimator_so_far, self.best_score_so_far

        modified_states = self._get_stages_from_pipeline(imp_nodes)

        # update the states so now we only have limited states
        self._init_pipeline(modified_states)
        fine_param_grid = self.param_grid

        start_time = time.time()
        best_estimator, best_score = self.auto_pipeline.execute(
            X,
            y,
            param_grid=fine_param_grid,
            num_option_per_pipeline=num_options_per_pipeline_for_random_search,
            exectype=self.execution_platform,
            max_eval_time_minute=self.execution_time_per_pipeline,
            random_state=self._get_next_random_number(),
            verbosity=verbosity,
            total_execution_time=self._get_remaining_time(experiment_start_time),
        )
        self.number_of_combinations += self.auto_pipeline.number_of_combinations
        end_time = time.time()
        execution_time = (end_time - start_time) / 60.0

        # storing and updating the results
        tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
        tmp_explored_score.extend(self.auto_pipeline.best_scores)
        self._update_best_estimator(best_estimator, best_score)

        # flush the resuts
        self._flush_results_locally(
            pipeline=self.auto_pipeline,
            round_name="2",
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_time,
            save_condition=None,
        )

        # check if execution has exceded maximum time
        if self._check_total_time_spend(experiment_start_time):
            self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            self._automate_clean()

            return self.best_estimator_so_far, self.best_score_so_far

        #####################################
        # Round 3
        #####################################
        # execute top-top-25% with more random parameters
        top_k_path_selections = math.ceil(
            top_k_path_selections * self.successive_halve_factor
        )
        num_options_per_pipeline_for_random_search = (
            self.num_options_per_pipeline_for_random_search * 2
        )

        imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(
            top_k_path_selections
        )

        # process round 3 only
        # if imp_nodes has some values.
        if imp_nodes:
            modified_states = self._get_stages_from_pipeline(imp_nodes)

            # update the states so now we only has limited states
            self._init_pipeline(modified_states)
            fine_param_grid = self.param_grid

            start_time = time.time()
            best_estimator, best_score = self.auto_pipeline.execute(
                X,
                y,
                param_grid=fine_param_grid,
                num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                exectype=self.execution_platform,
                max_eval_time_minute=self.execution_time_per_pipeline,
                random_state=self._get_next_random_number(),
                verbosity=verbosity,
                total_execution_time=self._get_remaining_time(experiment_start_time),
            )
            self.number_of_combinations += self.auto_pipeline.number_of_combinations
            end_time = time.time()
            execution_time = (end_time - start_time) / 60.0

            # storing and updating the results
            tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
            tmp_explored_score.extend(self.auto_pipeline.best_scores)
            self._update_best_estimator(best_estimator, best_score)

            # flush the resuts
            self._flush_results_locally(
                pipeline=self.auto_pipeline,
                round_name="3",
                start_time=start_time,
                end_time=end_time,
                execution_time=execution_time,
                save_condition=None,
            )

        # check if execution has exceded maximum time
        if self._check_total_time_spend(experiment_start_time):
            self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            self._automate_clean()

            return self.best_estimator_so_far, self.best_score_so_far

        # now we have understanding what base algorithm works
        indices, _ = zip(*sorted(enumerate(tmp_explored_score), key=itemgetter(1)))
        explored_estimator = []
        paths_for_hp_tuning = []
        base_score_of_paths = []
        tmp_tmp_explored_estimator = []
        tmp_tmp_explored_score = []

        # find best node (note that there are None and Nan also exists)
        for k in indices[::-1]:

            if tmp_explored_estimator[k].steps[0][0] in explored_estimator:
                continue
            if tmp_explored_score[k] == np.NaN or np.isnan(tmp_explored_score[k]):
                continue

            explored_estimator.append(tmp_explored_estimator[k].steps[0][0])
            paths_for_hp_tuning.append(tmp_explored_estimator[k])
            base_score_of_paths.append(tmp_explored_score[k])
            tmp_baseline_score = tmp_explored_score[k]

            # each layer one after another
            for i in range(len(self.stages) - 1):

                #####################################
                # Round 4
                #####################################
                # select top-3

                total_nodes = len(self.stages[i])
                modified_states = [self.stages[i], tmp_explored_estimator[k].steps]
                self._init_pipeline(modified_states)

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    exectype=self.execution_platform,
                    max_eval_time_minute=self.execution_time_per_pipeline,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_tmp_explored_score.extend(self.auto_pipeline.best_scores)
                for i, result_i in enumerate(self.auto_pipeline.best_scores):
                    if result_i > tmp_baseline_score:
                        paths_for_hp_tuning.append(
                            self.auto_pipeline.best_estimators[i]
                        )
                        base_score_of_paths.append(result_i)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="4",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=tmp_baseline_score,
                )

                if self._check_total_time_spend(experiment_start_time):
                    break

                #####################################
                # Round 5
                #####################################
                top_k_path_selections = math.ceil(
                    total_nodes * self.successive_halve_factor
                )
                num_options_per_pipeline_for_random_search = (
                    self.num_options_per_pipeline_for_random_search
                )
                imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(
                    top_k_path_selections
                )

                # this is inside a for loop
                # So, we should process only if the imp_nodes has a values.
                if imp_nodes:

                    modified_states = self._get_stages_from_pipeline(imp_nodes)

                    # update the states so now we only has limited states
                    self._init_pipeline(modified_states)
                    fine_param_grid = self.param_grid

                    start_time = time.time()
                    best_estimator, best_score = self.auto_pipeline.execute(
                        X,
                        y,
                        param_grid=fine_param_grid,
                        num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                        exectype=self.execution_platform,
                        max_eval_time_minute=self.execution_time_per_pipeline,
                        random_state=self._get_next_random_number(),
                        verbosity=verbosity,
                        total_execution_time=self._get_remaining_time(
                            experiment_start_time
                        ),
                    )
                    self.number_of_combinations += (
                        self.auto_pipeline.number_of_combinations
                    )
                    end_time = time.time()
                    execution_time = (end_time - start_time) / 60.0

                    self._update_best_estimator(best_estimator, best_score)
                    tmp_tmp_explored_estimator.extend(
                        self.auto_pipeline.best_estimators
                    )
                    tmp_tmp_explored_score.extend(self.auto_pipeline.best_scores)
                    for i, result_i in enumerate(self.auto_pipeline.best_scores):
                        if result_i > tmp_baseline_score:
                            paths_for_hp_tuning.append(
                                self.auto_pipeline.best_estimators[i]
                            )
                            base_score_of_paths.append(result_i)

                    # flushing the results
                    self._flush_results_locally(
                        pipeline=self.auto_pipeline,
                        round_name="5",
                        start_time=start_time,
                        end_time=end_time,
                        execution_time=execution_time,
                        save_condition=tmp_baseline_score,
                    )

                if self._check_total_time_spend(experiment_start_time):
                    break

            if self._check_total_time_spend(experiment_start_time):
                break

            if len(explored_estimator) >= self._top_k_bottom_nodes:
                break

        tmp_explored_estimator.extend(tmp_tmp_explored_estimator)
        tmp_explored_score.extend(tmp_tmp_explored_score)
        tmp_tmp_explored_estimator = []
        tmp_tmp_explored_score = []

        if self._check_total_time_spend(experiment_start_time):
            self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
            self.best_path_info["end_time"] = time.time()
            self.best_path_info["execution_time"] = (
                self.best_path_info["end_time"] - experiment_start_time
            )
            self._automate_clean()

            return self.best_estimator_so_far, self.best_score_so_far

        # process it further - explore graph
        # you will get many srom graphs, and expected best_score
        tmpGraphs, best_scores = self._generate_ML_graph(
            self.stages, paths_for_hp_tuning, base_score_of_paths
        )
        for tmp_index, tmp_graph in enumerate(tmpGraphs):
            self._init_pipeline(tmp_graph)
            fine_param_grid = self.param_grid

            start_time = time.time()
            best_estimator, best_score = self.auto_pipeline.execute(
                X,
                y,
                param_grid=fine_param_grid,
                exectype=self.execution_platform,
                max_eval_time_minute=self.execution_time_per_pipeline,
                random_state=self._get_next_random_number(),
                verbosity=verbosity,
                total_execution_time=self._get_remaining_time(experiment_start_time),
            )
            self.number_of_combinations += self.auto_pipeline.number_of_combinations
            end_time = time.time()
            execution_time = (end_time - start_time) / 60.0

            self._update_best_estimator(best_estimator, best_score)
            tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
            tmp_explored_score.extend(self.auto_pipeline.best_scores)
            for i, result_i in enumerate(self.auto_pipeline.best_scores):
                if result_i > best_scores[tmp_index]:
                    paths_for_hp_tuning.append(self.auto_pipeline.best_estimators[i])
                    base_score_of_paths.append(result_i)

            # flushing the results
            self._flush_results_locally(
                pipeline=self.auto_pipeline,
                round_name="6",
                start_time=start_time,
                end_time=end_time,
                execution_time=execution_time,
                save_condition=best_scores[tmp_index],
            )

            if self._check_total_time_spend(experiment_start_time):
                self._set_explored_estimators(
                    tmp_explored_estimator, tmp_explored_score
                )
                self.best_path_info["end_time"] = time.time()
                self.best_path_info["execution_time"] = (
                    self.best_path_info["end_time"] - experiment_start_time
                )
                self._automate_clean()

                return self.best_estimator_so_far, self.best_score_so_far

            # start random exploration
            imp_nodes = self.auto_pipeline.pipeline_graph_result_analysis(
                self._top_k_paths
            )

            # As imp_nodes is a blank dictionary there is no point in processing further.
            if imp_nodes:

                modified_states = self._get_stages_from_pipeline(imp_nodes)

                # this is an additional check
                from autoai_ts_libs.deps.srom.utils.pipeline_utils import check_srom_pipeline_stages

                try:
                    check_srom_pipeline_stages(modified_states)
                except Exception:
                    continue

                # update the states so now we only has limited states
                self._init_pipeline(modified_states)
                fine_param_grid = self.param_grid

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    num_option_per_pipeline=num_options_per_pipeline_for_random_search,
                    exectype=self.execution_platform,
                    max_eval_time_minute=self.execution_time_per_pipeline,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_explored_score.extend(self.auto_pipeline.best_scores)
                for i, result_i in enumerate(self.auto_pipeline.best_scores):
                    if result_i > best_scores[tmp_index]:
                        paths_for_hp_tuning.append(
                            self.auto_pipeline.best_estimators[i]
                        )
                        base_score_of_paths.append(result_i)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="6_1",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=best_scores[tmp_index],
                )

            if self._check_total_time_spend(experiment_start_time):
                self._set_explored_estimators(
                    tmp_explored_estimator, tmp_explored_score
                )
                self.best_path_info["end_time"] = time.time()
                self.best_path_info["execution_time"] = (
                    self.best_path_info["end_time"] - experiment_start_time
                )
                self._automate_clean()

                return self.best_estimator_so_far, self.best_score_so_far

        ####################################
        # AutoAI exploration
        if self.enable_autoai:
            (
                tmp_explored_estimator_,
                tmp_explored_score_,
                paths_for_hp_tuning_,
                base_score_of_paths_,
            ) = self._autoai_exploration(X, y)

            if len(tmp_explored_estimator_) > 0:
                tmp_explored_estimator.extend(tmp_explored_estimator_)
                tmp_explored_score.extend(tmp_explored_score_)

            if len(paths_for_hp_tuning_) > 0:
                paths_for_hp_tuning.extend(paths_for_hp_tuning_)
                base_score_of_paths.extend(base_score_of_paths_)

            if self._check_total_time_spend(experiment_start_time):
                self._set_explored_estimators(
                    tmp_explored_estimator, tmp_explored_score
                )
                self.best_path_info["end_time"] = time.time()
                self.best_path_info["execution_time"] = (
                    self.best_path_info["end_time"] - experiment_start_time
                )
                return self.best_estimator_so_far, self.best_score_so_far

        ####################################

        #####################################
        # Intelligent Optimization
        #####################################

        if self.level == "comprehensive":
            num_option_per_pipeline_for_intelligent_search = (
                self.num_option_per_pipeline_for_intelligent_search
            )
            execution_time_per_pipeline_for_intelligent_search = (
                self.execution_time_per_pipeline
            )
            if (
                num_option_per_pipeline_for_intelligent_search
                > num_options_per_pipeline_for_random_search
            ):
                factor = (int)(
                    num_option_per_pipeline_for_intelligent_search
                    / num_options_per_pipeline_for_random_search
                )
                execution_time_per_pipeline_for_intelligent_search *= factor

            # Genetic Optimization
            for path in paths_for_hp_tuning:
                # create a SROM pipeline with single path
                stages = []
                for item in path.steps:
                    stages.append([item])
                self._init_pipeline(stages)
                execution_platform = "evolutionary_search"
                fine_param_grid = self.param_grid

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    num_option_per_pipeline=num_option_per_pipeline_for_intelligent_search,
                    exectype=execution_platform,
                    max_eval_time_minute=execution_time_per_pipeline_for_intelligent_search,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_explored_score.extend(self.auto_pipeline.best_scores)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="genetic",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=None,
                )

                if self._check_total_time_spend(experiment_start_time):
                    self._set_explored_estimators(
                        tmp_explored_estimator, tmp_explored_score
                    )
                    self.best_path_info["end_time"] = time.time()
                    self.best_path_info["execution_time"] = (
                        self.best_path_info["end_time"] - experiment_start_time
                    )
                    self._automate_clean()

                    return self.best_estimator_so_far, self.best_score_so_far

            # Bayesian Optimization
            for path in paths_for_hp_tuning:
                # create a SROM pipeline with single path
                stages = []
                for item in path.steps:
                    stages.append([item])
                self._init_pipeline(stages)
                execution_platform = "bayesian_search"
                fine_param_grid = SROMParamGrid()
                fine_param_grid.set_param_grid(self.bayesian_paramgrid)

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    num_option_per_pipeline=num_option_per_pipeline_for_intelligent_search,
                    exectype=execution_platform,
                    max_eval_time_minute=execution_time_per_pipeline_for_intelligent_search,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_explored_score.extend(self.auto_pipeline.best_scores)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="bayesian",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=None,
                )

                if self._check_total_time_spend(experiment_start_time):
                    self._set_explored_estimators(
                        tmp_explored_estimator, tmp_explored_score
                    )
                    self.best_path_info["end_time"] = time.time()
                    self.best_path_info["execution_time"] = (
                        self.best_path_info["end_time"] - experiment_start_time
                    )
                    self._automate_clean()

                    return self.best_estimator_so_far, self.best_score_so_far

            # Hyper-band Search
            for path in paths_for_hp_tuning:
                # create a SROM pipeline with single path
                stages = []
                for item in path.steps:
                    stages.append([item])
                self._init_pipeline(stages)
                execution_platform = "hyperband_search"
                fine_param_grid = self.param_grid

                start_time = time.time()
                best_estimator, best_score = self.auto_pipeline.execute(
                    X,
                    y,
                    param_grid=fine_param_grid,
                    num_option_per_pipeline=num_option_per_pipeline_for_intelligent_search,
                    exectype=execution_platform,
                    max_eval_time_minute=execution_time_per_pipeline_for_intelligent_search,
                    random_state=self._get_next_random_number(),
                    verbosity=verbosity,
                    total_execution_time=self._get_remaining_time(
                        experiment_start_time
                    ),
                )
                self.number_of_combinations += self.auto_pipeline.number_of_combinations
                end_time = time.time()
                execution_time = (end_time - start_time) / 60.0

                self._update_best_estimator(best_estimator, best_score)
                tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                tmp_explored_score.extend(self.auto_pipeline.best_scores)

                # flushing the results
                self._flush_results_locally(
                    pipeline=self.auto_pipeline,
                    round_name="hyperband",
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    save_condition=None,
                )

                if self._check_total_time_spend(experiment_start_time):
                    self._set_explored_estimators(
                        tmp_explored_estimator, tmp_explored_score
                    )
                    self.best_path_info["end_time"] = time.time()
                    self.best_path_info["execution_time"] = (
                        self.best_path_info["end_time"] - experiment_start_time
                    )
                    self._automate_clean()

                    return self.best_estimator_so_far, self.best_score_so_far

            try:
                # RBFOpt
                for path in paths_for_hp_tuning:
                    # create a SROM pipeline with single path
                    stages = []
                    for item in path.steps:
                        stages.append([item])
                    self._init_pipeline(stages)
                    execution_platform = "rbfopt_search"
                    fine_param_grid = SROMParamGrid()
                    fine_param_grid.set_param_grid(self.rbopt_paramgrid)

                    start_time = time.time()
                    best_estimator, best_score = self.auto_pipeline.execute(
                        X,
                        y,
                        param_grid=fine_param_grid,
                        num_option_per_pipeline=num_option_per_pipeline_for_intelligent_search,
                        exectype=execution_platform,
                        max_eval_time_minute=execution_time_per_pipeline_for_intelligent_search,
                        random_state=self._get_next_random_number(),
                        verbosity=verbosity,
                        total_execution_time=self._get_remaining_time(
                            experiment_start_time
                        ),
                    )
                    end_time = time.time()
                    execution_time = (end_time - start_time) / 60.0
                    self.number_of_combinations += (
                        self.auto_pipeline.number_of_combinations
                    )

                    self._update_best_estimator(best_estimator, best_score)
                    tmp_explored_estimator.extend(self.auto_pipeline.best_estimators)
                    tmp_explored_score.extend(self.auto_pipeline.best_scores)

                    # flushing the results
                    self._flush_results_locally(
                        pipeline=self.auto_pipeline,
                        round_name="rbf_opt",
                        start_time=start_time,
                        end_time=end_time,
                        execution_time=execution_time,
                        save_condition=None,
                    )

                    if self._check_total_time_spend(experiment_start_time):
                        self._set_explored_estimators(
                            tmp_explored_estimator, tmp_explored_score
                        )
                        self.best_path_info["end_time"] = time.time()
                        self.best_path_info["execution_time"] = (
                            self.best_path_info["end_time"] - experiment_start_time
                        )
                        self._automate_clean()

                        return self.best_estimator_so_far, self.best_score_so_far
            except Exception as ex:
                LOGGER.exception(ex)
        self._set_explored_estimators(tmp_explored_estimator, tmp_explored_score)
        self.best_path_info["end_time"] = time.time()
        self.best_path_info["execution_time"] = (
            self.best_path_info["end_time"] - experiment_start_time
        )
        self._automate_clean()
        return self.best_estimator_so_far, self.best_score_so_far

    def get_leaders(self, num_leader=5, check_pred_proba_cond=False):
        """
            Method get leaders to get the number of explored estimator.
        """
        if num_leader > len(self.explored_estimator):
            raise Exception(
                "Insufficient number of explored estimator as compared to number leader provided"
            )

        tmp_score = []
        tmp_mdl = []
        for i in range(len(self.explored_score)):
            if not np.isnan(self.explored_score[i]):
                tmp_score.append(self.explored_score[i])
                tmp_mdl.append(self.explored_estimator[i])

        indices, _ = zip(*sorted(enumerate(tmp_score), key=itemgetter(1)))
        leaders = []
        leaders_rep = []
        leader_scores = []

        def get_str_rep(pipeline):
            name_list = []
            for i_v in pipeline.steps:
                text = str(i_v[0])
                if not text.startswith("skip"):
                    name_list.append(i_v[0])
            return name_list

        def get_pair_match(pSet, rSet):
            """
                Method get pair match to find the pair.
            """
            match_count = 0
            for item in rSet:
                if item in pSet:
                    match_count = match_count + 1
            if match_count == len(rSet):
                return 1

            match_count = 0
            for item in pSet:
                if item in rSet:
                    match_count = match_count + 1
            if match_count == len(pSet):
                return 1

            return 0

        def check_match(rSet):
            """
                Method check match to check if it is a match or not. 
            """
            for pSet in leaders_rep:
                if get_pair_match(pSet, rSet) == 1:
                    return 1
            return 0

        for k in indices[::-1]:

            # extra check. This condition remove model that are not suitable for generating
            # class probability
            if check_pred_proba_cond:
                if "predict_proba" not in dir(tmp_mdl[k].steps[-1][1]):
                    continue

            # get_str_representation
            rSet = get_str_rep(tmp_mdl[k])
            if check_match(rSet) == 1:
                continue

            leaders_rep.append(rSet)
            leaders.append(tmp_mdl[k])
            leader_scores.append(tmp_score[k])
            if len(leaders) >= num_leader:
                break

        return leaders

    @abstractmethod
    def fit(self, X, y):
        """
        Train the best model on the given data.

        Parameters:
            X (pandas dataframe or numpy array): Training dataset. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                If target_column is added in the meta data, it is \
                used from there. shape = [n_samples] or [n_samples, n_output]

        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline.
        """

        if self.best_estimator_so_far:
            self.best_estimator_so_far.fit(X, y)
        return self

    @abstractmethod
    def predict(self, X):
        """
        Predict the class labels/regression targets/anomaly scores etc. using \
        the trained model pipeline.
        
        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        if self.best_estimator_so_far:
            return self.best_estimator_so_far.predict(X)

    def predict_proba(self, X):
        """
        Use the weights learned in training to predict class probabilities.
        Parameters:
        ----------
        Xs: list of predictions to be blended.
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        Return:
        ------
        y_pred: array_like, shape=(n_samples, n_class)
        The blended prediction.
        """
        if self.best_estimator_so_far:
            if "predict_proba" in dir(
                self.best_estimator_so_far
            ) and "predict_proba" in dir(self.best_estimator_so_far.steps[-1][-1]):
                return self.best_estimator_so_far.predict_proba(X)
            elif "decision_function" in dir(
                self.best_estimator_so_far
            ) and "decision_function" in dir(self.best_estimator_so_far.steps[-1][-1]):
                return self.best_estimator_so_far.decision_function(X)
            else:
                raise Exception(
                    "The fitted model does not have probability/decision function"
                )

    @property
    def sromgraph(self):
        """
            sromgraph method
        """
        tmp_auto_pipeline = SROMPipeline()
        tmp_s = self.stages
        if tmp_s is None:
            tmp_s = self._initialize_default_stages()
            tmp_auto_pipeline.set_stages(tmp_s)
        else:
            tmp_auto_pipeline.set_stages(tmp_s)
        return tmp_auto_pipeline.sromgraph

    def export(
        self, code_file_path="srom_pipeline.py", random_state=None, data_file_path=""
    ):
        """
            Export method to return best_estimator_so_far, code_file_path, random_state, data_file_path.
        """
        if self.best_estimator_so_far is None:
            raise Exception("Train the model first by calling automate/fit method")
        return export_pipeline(
            self.best_estimator_so_far, code_file_path, random_state, data_file_path
        )

    def get_plot_best_score_over_time(self):
        """
        return the information to plot the best score over the execution time period.

        Returns
        -------
        x_axis_label: str
        y_axis_label: str
        timeline: list
        best_score_so_far: list
        """
        if self.csv_filename is None or not os.path.exists(self.csv_filename):
            raise FileNotFoundError("The csv file %s is not found." % self.csv_filename)

        stats_df = pd.read_csv(self.csv_filename, sep="\t")
        stats_df["best_scores"].replace("None", np.nan, inplace=True)
        stats_df["best_scores"] = stats_df["best_scores"].astype("float64")
        stats_df["execution_time_minutes"].replace("None", np.nan, inplace=True)
        stats_df["execution_time_minutes"] = stats_df["execution_time_minutes"].astype(
            "float64"
        )
        round_stats_df = stats_df[stats_df["estimator_id"] == "round"]
        timeline = list(round_stats_df["execution_time_minutes"].cumsum())
        best_score_so_far = list(round_stats_df["best_scores"].expanding().max())
        x_axis_label = "Execution Timeline (min)"
        y_axis_label = "Best Score So Far"

        return x_axis_label, y_axis_label, timeline, best_score_so_far

    def get_plot_n_pipelines_over_time(self):
        """
        return the information to plot the total number of pipelines explored over the execution time period.

        Returns
        -------
        x_axis_label: str
        y_axis_label: str
        timeline: list
        n_pipelines: list
        """
        if self.csv_filename is None or not os.path.exists(self.csv_filename):
            raise FileNotFoundError("The csv file %s is not found." % self.csv_filename)

        stats_df = pd.read_csv(self.csv_filename, sep="\t")
        stats_df["best_scores"].replace("None", np.nan, inplace=True)
        stats_df["best_scores"] = stats_df["best_scores"].astype("float64")
        stats_df["execution_time_minutes"].replace("None", np.nan, inplace=True)
        stats_df["execution_time_minutes"] = stats_df["execution_time_minutes"].astype(
            "float64"
        )
        round_stats_df = stats_df[stats_df["estimator_id"] == "round"]
        timeline = list(round_stats_df["execution_time_minutes"].cumsum())
        n_pipelines = list(round_stats_df["n_pipelines"].cumsum())
        timeline.insert(0, 0)
        n_pipelines.insert(0, 0)
        x_axis_label = "Execution Timeline (min)"
        y_axis_label = "Number of Pipelines Explored So Far"

        return x_axis_label, y_axis_label, timeline, n_pipelines

    def get_best_pipelines(self):
        pass

    def feature_importances(
        self,
        *,
        model=None,
        X=None,
        y=None,
        type="permutation_importance",
        n_repeats=10,
        random_state=42
    ):
        """Extract feature importances from models.

        types: "permutation_importance", "native", "shap".

        Parameters
        ---------
        model : Best estimator
        X (pandas dataframe or numpy array): Training dataset. \
            shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        y (pandas dataframe or numpy array, optional): Target vector to be used. \
            If target_column is added in the meta data, it is \
            used from there. shape = [n_samples] or [n_samples, n_output]
        type :  "permutation_importance", "native", "shap"
        n_repeats : Number of times to permute a feature.
        random_state : Pseudo-random number generator to control the permutations of each feature.
            Pass an int to get reproducible results across function calls

        Returns
        -------
        array of feature importances.
        """
        if model is None:
            model = self.best_estimator_so_far

        if (
            X is None
            and y is None
            and model is None
            and type == "permutation_importance"
        ):
            raise Exception(
                "X, y and model/best estimator are requried for permutation importance."
            )

        if type == "native":
            if hasattr(model, "coef_"):
                coefs = np.square(model.coef_).sum(axis=0)
            else:
                coefs = model.feature_importances_
            return coefs
        elif type == "permutation_importance":
            return permutation_importance(
                model, X, y, n_repeats=n_repeats, random_state=random_state
            )
        elif type == "shap":
            try:
                from shap import TreeExplainer

                explainer = TreeExplainer(
                    model, feature_perturbation="tree_path_dependent"
                )
                coefs = explainer.shap_values(X)

                if isinstance(coefs, list):
                    coefs = list(map(lambda x: np.abs(x).mean(0), coefs))
                    coefs = np.sum(coefs, axis=0)
                else:
                    coefs = np.abs(coefs).mean(0)

                return coefs
            except Exception:
                raise Exception("Unable to use Shap library.")
        else:
            raise ValueError("Enter a valid type argument.")
