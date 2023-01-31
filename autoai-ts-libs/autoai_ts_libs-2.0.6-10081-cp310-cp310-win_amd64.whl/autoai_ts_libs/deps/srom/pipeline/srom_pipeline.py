# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
    .. module:: srom_pipeline
       :synopsis: SROMPipeline class.

    .. moduleauthor:: SROM Team
"""

import collections
import copy
import logging
import multiprocessing
import warnings
import queue
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from autoai_ts_libs.deps.srom.pipeline.graph import SROMGraph
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.utils import pipeline_utils
from autoai_ts_libs.deps.srom.utils.data_utils import data_label_split
from autoai_ts_libs.deps.srom.utils.pipeline_utils import GraphType
from autoai_ts_libs.deps.srom.utils.pipeline_utils import verbosity_to_verbose_mapping

LOGGER = logging.getLogger(__name__)


class SROMPipeline(BaseEstimator, object):
    """
    SROMPipeline is based on standard pipeline classes such as sklearn.pipeline.Pipeline \
    and pyspark.ml.Pipeline. But it has many additional utilities which \
    enhance the data science experience. \
    Like the known concept of pipeline, the idea is to assemble several steps that can be \
    cross-validated together while setting different parameters. \
    The major differentiation on these lines being that SROMPipeline allows \
    for multiple techniques to be configured for each step so that it will try all possible \
    combinations of options for that step with all other options for other steps and runs such \
    combination paths to allow model selection. For each of the such paths created, \
    it tries different parameters and chooses the best combination of parameters for techniques \
    in that path. For this, it enables various parameter settings as allowed by SROMParamGrid \
    implementation.

    Example:
        from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline \
        from sklearn.datasets import make_classification \
        from sklearn.linear_model import LogisticRegression \
        from sklearn.svm import SVC \
        from sklearn.decomposition import PCA \
        from sklearn.model_selection import train_test_split \
        from sklearn.metrics import roc_curve \
        n_estimator = 10 \
        X, y = make_classification(n_samples=800) \
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5) \
        pca = PCA() \
        rt_lm = LogisticRegression() \
        svc = SVC() \
        pipeline = SROMPipeline() \
        # if your dataset is a single dataframe including the target column, \
        # you could also use add_input_meta_data to indicate that \
        # pipeline.add_input_meta_data(id_column = 'id', label_column = 'label') \
        pipeline.set_stages([[PCA()],[LogisticRegression(), SVC()]]) \
        pipeline.create_graph() \
        pipeline.execute(X_train, y_train) \
        model = pipeline.fit(X_train, y_train) \
        predictions = pipeline.predict(X_test) \
    """

    SOURCE_NODE_LABEL = "Start"

    def __init__(self, graphtype=GraphType.Default.value):
        """[summary]

        Args:
            graphtype ([type], optional): [description]. Defaults to GraphType.Default.value.
        """

        # pipeline graph
        self.number_of_combinations = 0
        self.pipeline_id = pipeline_utils.create_pipeline_id()
        # self.graph = None

        # result related
        self.cv = 3  # default value added
        self.groups = None
        self.best_score = None
        self.best_estimator = None
        self.scoring = None
        self.best_estimators = None
        self.best_scores = None
        self.best_scores_std = None
        self.best_fit_time = None
        self.best_score_time = None
        self.execution_time_for_best_estimators = None
        self.activations = None

        # Dataset related variables
        self.time_column = None
        self.id_column = None
        self.label_column = None
        self.label_prefix = None

        # added an extra parameter now
        self.param_grid = SROMParamGrid(gridtype="empty")
        self._cross_val_score = None
        self._pipeline_type = Pipeline
        self._pipeline_init_param = {}

        self.graphtype = graphtype
        self._sromgraph = SROMGraph(graphtype=graphtype)
        self._evn_config = {}
        self.single_node_n_jobs = None

        self._execution_states = {-1: "not started", 0: "started", 1: "completed"}
        self._current_execution_state = -1

    @property
    def _is_execution_finished(self):
        return self._execution_states[self._current_execution_state]

    def add_input_meta_data(
        self, time_column=None, id_column=None, label_column=None, label_prefix=None
    ):
        """
        Sets the input meta data that can be used in other functions appropriately. \
        For most SROM pipelines, time, index and label apply, hence setting these in \
        the base pipeline class. Subclasses can add more meta data as required.

        Parameters:
            time_column (String): Name of a column which is either a timestamp or a \
                sequence number indicating the timeseries order.
            id_column (String): Name of a column indicating an identifier for assets, \
                processes etc.
            label_column (String): Name of a column which is a categorical label \
                (classification or anomaly) or a continuous target for regression etc.
            label_prefix (String): Prefix of a target column.
        """
        self.time_column = time_column
        self.id_column = id_column
        self.label_column = label_column
        self.label_prefix = label_prefix

    def set_cross_validation(self, obj):
        """
        Parameters:
            obj (int, cross-validation generator or an iterable, optional): Determines the \
                cross-validation splitting strategy. Possible inputs for cv are: None, to use \
                the default 10-fold cross validation, integer, to specify the number of folds \
                in a (Stratified)KFold, aan object to be used as a cross-validation generator. \
                An iterable yielding train, test splits.

        For integer/None inputs, if the estimator is a classifier and y is either binary or \
        multiclass, StratifiedKFold is used. In all other cases, KFold is used. \
        for scikit pipelines,refer User Guide \
        (http://scikit-learn.org/stable/modules/cross_validation.html#cross-validation) \
        for the various cross-validation strategies that can be used here.
        """
        self.cv = obj

    def set_cross_val_score(self, cross_val_score):
        self._cross_val_score = cross_val_score

    def set_pipeline_type_for_path(self, pipeline_type):
        self._pipeline_type = pipeline_type

    def set_pipeline_init_param_for_path(self, pipeline_init_param):
        self._pipeline_init_param = pipeline_init_param

    def set_groups(self, groups):
        """
        Set group labels for the samples used while splitting the \
        dataset into train/test set.

        Parameters:
            groups: array-like, with shape (n_samples,) \
                n_samples is number of sample in training data.
        """
        self.groups = groups

    def set_scoring(self, scoring):
        """
        Set scoring function to be used for model selection. \
        Only available for scikit pipelines as of now.

        Parameters:
            scoring (string, callable or None, default=None): A string \
                (see scikit model evaluation documentation) or a scorer \
                callable object/function with signature scorer(estimator, X, y). \
                If None, the score method of the estimator is used. \
                You can refer to \
                http://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html \
                for how to create a new scoring function.
        """
        self.scoring = scoring

    def set_best_estimator(self, obj):
        """
        Used to set best estimator.

        Parameters:
            Obj (object): Best estimator instance.
        """
        self.best_estimator = obj
        self.best_score = None

    def set_param_grid(self, obj):
        """
        Used to set the param grid.

        Parameters:
            Obj (object): SROMParamGrid instance.
        """
        self.param_grid = obj

    def get_best_estimator(self):
        """
        Retrieve the best_estimator.

        Returns:
            best estimator.
        """
        return self.best_estimator

    def set_stages(self, stages):
        """
        Parameters:
            stages (list of lists): An list of stages such that each element of that \
                list is an list again, of candidate algorithms to be tried for that stage.

        Example:
            The code below shows how PCA is being tried for stage 1 and RandomForest and \
            GradientBoosting for stage 2. \
            For a scikit pipeline, the candidate algorithms are any algorithms from scikit or custom \
            algorithms implemented as scikit transformers/estimators. \
            from sklearn.decomposition import PCA \
            from sklearn.ensemble import RandomForestClassifier \
            from sklearn.ensemble import GradientBoostingClassifier \
            pipeline = SROMPipeline() \
            pipeline.set_stages([[PCA()],[RandomForestClassifier(), GradientBoostingClassifier()]])
        """

        self._sromgraph.set_stages(stages)

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
        warnings.simplefilter("always", DeprecationWarning)
        warnings.warn(
            "create_graph() method is deprecated. Use sromgraph.asimage() instead",
            DeprecationWarning,
        )
        return self._sromgraph.asimage()

    def set_environment_config(self, evn_conf):
        """[summary]

        Args:
            evn_conf ([type]): [description]
        """
        self._evn_config = evn_conf

    @property
    def paths(self):
        return self._sromgraph.paths

    @property
    def sromgraph(self):
        return self._sromgraph

    @property
    def stages(self):
        return self._sromgraph.stages

    def summary(self, enable_param_grid=False, is_auto=False):
        """
        this function call return summary on
        1) number of total paths that are prepared
        2) paths with number of parameter grids
        """
        dic_result = {}
        dic_result["total_stage"] = len(self._sromgraph.stages)
        tmp_total_nodes = 0
        tmp_total_sub_paths = 1
        for pre_stage_index, per_stage in enumerate(self._sromgraph.stages):
            tmp_total_nodes = tmp_total_nodes + len(per_stage)
            if pre_stage_index < dic_result["total_stage"] - 1:
                tmp_total_sub_paths = tmp_total_sub_paths * (len(per_stage) + 1)
            else:
                tmp_total_sub_paths = tmp_total_sub_paths * (len(per_stage))
        dic_result["total_nodes"] = tmp_total_nodes
        dic_result["total_paths"] = len(self._sromgraph.paths)

        if is_auto:
            dic_result["total_pipelines"] = tmp_total_sub_paths
        else:
            dic_result["total_pipelines"] = len(self._sromgraph.paths)

        # dic_result["total_subpaths"] = tmp_total_sub_paths
        # dic_result["total_subpaths_pipelines"] = tmp_total_sub_paths

        if enable_param_grid:
            total_grid_points = 0
            if self.param_grid:
                from autoai_ts_libs.deps.srom.utils.pipeline_utils import gen_pipeline_and_grid

                # from sklearn.model_selection import ParameterGrid

                _, tmp_param_grids = gen_pipeline_and_grid(self.paths, self.param_grid)
                for param_grid in tmp_param_grids:
                    if len(param_grid) == 0:
                        total_grid_points = total_grid_points + 1
                    else:
                        tmp_cal = 1
                        for key in param_grid.keys():
                            if len(param_grid[key]) > 0:
                                tmp_cal = tmp_cal * len(param_grid[key])
                        total_grid_points = total_grid_points + tmp_cal
                        # total_grid_points = total_grid_points + len(
                        #    list(ParameterGrid(param_grid))
                        # )
            dic_result[
                "total_pipelines_with_parameter_instantaneous"
            ] = total_grid_points
            # dic_result["parameter_grid"] = self.param_grid.get_param_grid()
        return dic_result

    def _specialdatatransforms(self, X, y):

        # X may be the entire data matrix containing all columns, check and remove/create y if so
        if self.time_column is not None and self.time_column in X.columns:
            X = X.drop(self.time_column, axis=1)

        if self.id_column is not None and self.id_column in X.columns:
            X = X.drop(self.id_column, axis=1)

        if self.label_column is not None and self.label_column in X.columns:
            if y is None:
                y = X[self.label_column]
            X = X.drop(self.label_column, axis=1)

        if self.label_prefix is not None:
            if y is not None:
                raise BaseException(
                    "Multiple labels: labels can be indicated by one of \
                label column or label prefix"
                )
            X, y = data_label_split(X, self.label_prefix)

        return X, y

    def run_fit_on_all_paths(self, X, y=None):
        """
        Calls fit estimators in pipeline. This is intended mainly \
        as a means of restoring any stateful information on estimators.

        Parameters:
            X (pandas dataframe or numpy array): shape = [n_samples, n_features] \
                where n_samples is the number of samples and \
                n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                shape = [n_samples] or [n_samples, n_output].

        Returns:
            answer(list): A list of objects with state restored.
        Raises:
            Exception: If best_estimators consist of pipeline with multiple layers.
        """

        if not self.best_estimators or self.best_estimators is None:
            raise Exception("best_estimators not found. Please execute the pipeline.")

        answer = []
        LOGGER.debug(str(self.best_estimators))
        for estimator in self.best_estimators:
            if len(estimator.steps) > 1:
                # We support only one layer pipeline here. Thus pipeline will only have estimators.
                # This is done so that a common method could be called on all individual estimators
                # in the returned list
                raise Exception("Pipeline with only one layer supported.")
            estimator.fit(X, y)
            for step in estimator.steps:
                LOGGER.debug("appending %s", str(step))
                answer.append(step[1])
        return answer

    def execute_async(
        self,
        X,
        y=None,
        exectype="single_node_complete_search",
        n_jobs=multiprocessing.cpu_count(),
        pre_dispatch="2*n_jobs",
        verbosity="low",
        param_grid=SROMParamGrid(gridtype="empty"),
        num_option_per_pipeline=10,
        max_eval_time_minute=2,
        upload_data=True,
        random_state=None,
        total_execution_time=10,
    ):
        X, y = self._pre_exec(
            X,
            y,
            exectype,
            verbosity,
            param_grid,
            max_eval_time_minute,
            total_execution_time,
        )
        # Now
        import multiprocessing as mp

        global result_queue
        result_queue = mp.Queue()
        global task

        # execution
        if self._sromgraph.graphtype == 2 and exectype == "single_node":
            task = mp.Process(
                target=self._call_srom_single_node_functional_dag,
                args=(X, param_grid, total_execution_time, result_queue),
            )
        elif self._sromgraph.graphtype == 2 and exectype == "spark_node":
            task = mp.Process(
                target=self._call_srom_spark_functional_dag,
                args=(X, param_grid, total_execution_time, result_queue),
            )
        elif exectype == "single_node_complete_search" or exectype == "single_node":
            task = mp.Process(
                target=self._call_srom_single_node_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "exhaustive",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        elif exectype == "single_node_random_search":
            task = mp.Process(
                target=self._call_srom_single_node_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "random",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        elif exectype == "spark_node_random_search":
            task = mp.Process(
                target=self._call_spark_node_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "random",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        elif exectype == "spark_node_complete_search":
            task = mp.Process(
                target=self._call_spark_node_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "exhaustive",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        elif exectype == "evolutionary_search":
            task = mp.Process(
                target=self._call_evolutionary_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "evolutionary",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        elif exectype == "rbfopt_search":
            task = mp.Process(
                target=self._call_rbfopt_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "rbfopt",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        elif exectype == "hyperband_search":
            task = mp.Process(
                target=self._call_hyperband_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "hyperband",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        elif exectype == "bayesian_search":
            task = mp.Process(
                target=self._call_bayesian_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "bayesian",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        elif exectype == "serverless_search":
            task = mp.Process(
                target=self._call_serverless_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "serverless",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    upload_data,
                    result_queue,
                ),
            )
        elif exectype == "ray_search":
            task = mp.Process(
                target=self._call_serverless_search,
                args=(
                    X,
                    y,
                    param_grid,
                    num_option_per_pipeline,
                    n_jobs,
                    pre_dispatch,
                    "ray",
                    max_eval_time_minute,
                    random_state,
                    total_execution_time,
                    verbosity,
                    result_queue,
                ),
            )
        else:
            raise BaseException("Execution method not supported")

        task.start()

    def get_result(self, block=False, verbosity="low"):
        """[It produce partial results when execution is not completed]

        Args:
            block (bool, optional): [description]. Defaults to False.
            verbosity (str, optional): [description]. Defaults to "low".

        Returns:
            [type]: [description]
        """
        ret_result = None

        if self._is_execution_finished == "started":
            try:
                ret_result = result_queue.get(block=block)
                if ret_result and ret_result[0]:
                    self.best_estimators = ret_result[0]
                    self.best_scores = ret_result[1]
                    if len(self.best_scores) == len(self._sromgraph.paths):
                        self._current_execution_state = 1
                        self._post_exec(verbosity)
                        return self.best_estimator, self.best_score
            except queue.Empty:
                pass
        elif self._is_execution_finished == "completed":
            LOGGER.warning("The pipeline execution has finished.")
            return self.best_estimator, self.best_score
        else:
            LOGGER.warning("The pipeline execution has not started.")
            return
        return ret_result

    def get_best_results(self, best_estimators, best_scores):
        best_score = None
        best_estimator = None
        tmp_best_scores = np.nanmax(best_scores)
        if not np.isnan(tmp_best_scores):
            best_result_index = best_scores.index(tmp_best_scores)
            best_score = best_scores[best_result_index]
            best_estimator = copy.deepcopy(best_estimators[best_result_index])
        return best_estimator, best_score

    def stop_execution(self):
        # if process is still running, we initiate its cleaning
        import time

        try:
            if task.is_alive():
                task.terminate()
                time.sleep(1)
                task.join()
                time.sleep(1)
        except Exception as ex:
            pass

    def _pre_exec(
        self,
        X,
        y,
        exectype,
        verbosity,
        param_grid,
        max_eval_time_minute,
        total_execution_time,
    ):
        """[Internal Method]

        Args:
            X ([type]): [description]
            y ([type]): [description]
            exectype ([type]): [description]
            verbosity ([type]): [description]
            param_grid ([type]): [description]
            max_eval_time_minute ([type]): [description]
            total_execution_time ([type]): [description]

        Raises:
            ValueError: [description]
            ValueError: [description]
        """
        if self._is_execution_finished == "started":
            LOGGER.warning("The pipeline execution has already started.")
            return

        self.best_estimators = []
        self.best_estimator = None
        self.best_scores = []
        self.best_scores_std = []
        self.best_score = None
        self.number_of_combinations = 0
        self.param_grid = param_grid
        # set current execution state to "started"
        self._current_execution_state = 0

        if total_execution_time != -1 and total_execution_time < max_eval_time_minute:
            raise ValueError(
                "total_execution_time={} is less than the max_eval_time_minute={}".format(
                    total_execution_time, max_eval_time_minute
                )
            )

        # obtain data
        X, y = self._specialdatatransforms(X, y)

        # filter grid based on data
        # param_grid = pipeline_utils.clean_param_grid(param_grid, X.shape)
        self.param_grid = param_grid

        if self.groups is not None and len(X) != len(self.groups):
            raise ValueError(
                "Inconsistent number of samples in groups. "
                "It should be equal to number of samples in X."
            )

        if (
            "TUNING_PARAM" in self._evn_config
            and "n_jobs" in self._evn_config["TUNING_PARAM"]
        ):
            self.single_node_n_jobs = self._evn_config["TUNING_PARAM"]["n_jobs"]
            LOGGER.info(
                "*****We reset n_jobs to evn_config[TUNING_PARAM][n_jobs]:*****"
            )

        # Print pipeline paths
        if verbosity == "high":
            LOGGER.info("*****All pipeline paths in the graph are:*****")
            pipeline_utils.print_paths(self._sromgraph.paths)


        if exectype == "serverless_search":
            from autoai_ts_libs.deps.srom.pipeline.utils.lithops_helper import replace_srom_classes

            # replace srom classes
            self.set_stages(replace_srom_classes(self.stages))
        if self.stages:
            for stage in self.stages[-1]:
                if (type(stage) not in [list]) and ('base_learner' in stage[1].get_params()) and ('verbose' in stage[1].base_learner.get_params()):
                        stage[1].base_learner.set_params(verbose=verbosity_to_verbose_mapping(verbosity))
        if (
            exectype == "single_node_halving_complete_search"
            or exectype == "single_node_halving_random_search"
        ):
            from packaging import version
            import sklearn

            if version.parse("0.24.2") > version.parse(sklearn.__version__):
                exectype = "single_node_complete_search"
                LOGGER.warning(
                    "exectype=`"
                    + str(exectype)
                    + "` not supported for sklearn version lower than 0.24.2. Changing to exectype=`single_node_complete_search`."
                )

        return X, y

    def _post_exec(self, verbosity):
        """ """
        # set execution state
        self._current_execution_state = 1
        # print execution result
        if verbosity == "medium" or verbosity == "high":
            if self.label_column is not None:
                LOGGER.info("SROM pipeline execution for target: %s", self.label_column)
            pipeline_utils.print_estimators_and_scores(
                self.best_estimators, self.best_scores
            )

        if self.best_scores:
            self.best_estimator, self.best_score = self.get_best_results(
                self.best_estimators, self.best_scores
            )

        # extra logging information
        # this is potentially expensive so...
        if LOGGER.getEffectiveLevel() >= logging.INFO:
            # would be cleaner in python>=3.5 adict = {**dict1, **dict2}
            if self.best_estimator:
                adict = self.__dict__.copy()
                # print(self.best_estimator)
                adict.update(
                    {"plstring": pipeline_utils.get_pipeline_str(self.best_estimator)}
                )
                adict.update({"number_of_paths": len(self._sromgraph.paths)})
                if self.label_column is not None:
                    LOGGER.info(
                        """The best estimator for all {number_of_paths} pipeline paths
                    for target {label_column} is: {plstring} with a
                    score of {best_score}""".format(
                            **adict
                        )
                    )
                else:
                    LOGGER.info(
                        """The best estimator for all {number_of_paths} pipeline paths 
                    is: {plstring} with a score of {best_score}""".format(
                            **adict
                        )
                    )
            else:
                LOGGER.info("No best estimator found (or set).")

    def _call_srom_single_node_functional_dag(
        self, X, param_grid, total_execution_time, result_queue=None
    ):
        """[summary]"""
        from autoai_ts_libs.deps.srom.pipeline.execution_types.exploration.srom_single_node_transform import (
            srom_single_node_transform,
            srom_single_node_transform_async,
        )

        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
            ) = srom_single_node_transform(
                X,
                paths=self._sromgraph.paths,
                param_grid=param_grid,
                total_execution_time=total_execution_time,
            )
        else:
            srom_single_node_transform_async(
                X,
                paths=self._sromgraph.paths,
                param_grid=param_grid,
                total_execution_time=total_execution_time,
                result_out=result_queue,
            )

    def _call_srom_spark_functional_dag(
        self, X, param_grid, total_execution_time, result_queue=None
    ):
        """[summary]"""
        from autoai_ts_libs.deps.srom.pipeline.execution_types.exploration.srom_spark_transform import (
            srom_spark_transform,
            srom_spark_transform_async,
        )
        from pyspark import SparkContext
        from autoai_ts_libs.deps.srom.utils.package_version_check import check_pyspark_version

        check_pyspark_version()
        sc = SparkContext.getOrCreate()

        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
            ) = srom_spark_transform(
                X,
                sc,
                paths=self._sromgraph.paths,
                param_grid=param_grid,
                total_execution_time=total_execution_time,
            )
        else:
            srom_spark_transform_async(
                X,
                sc,
                paths=self._sromgraph.paths,
                param_grid=param_grid,
                total_execution_time=total_execution_time,
                result_queue=result_queue,
            )

    def _call_srom_single_node_search(
        self,
        X,
        y,
        param_grid,
        num_option_per_pipeline,
        n_jobs,
        pre_dispatch,
        mode,
        max_eval_time_minute,
        random_state,
        total_execution_time,
        verbosity,
        result_queue=None,
    ):
        from autoai_ts_libs.deps.srom.pipeline.execution_types.srom_single_node_search import (
            srom_single_node_search,
            srom_single_node_search_async,
        )

        if self.single_node_n_jobs is not None:
            n_jobs = self.single_node_n_jobs
        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
            ) = srom_single_node_search(
                X,
                y,
                param_grid=param_grid,
                num_option_per_pipeline=num_option_per_pipeline,
                n_jobs=n_jobs,
                pre_dispatch=pre_dispatch,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                mode=mode,
                groups=self.groups,
                max_eval_time_minute=max_eval_time_minute,
                random_state=random_state,
                total_execution_time=total_execution_time,
                pipeline_type=self._pipeline_type,
                pipeline_init_param=self._pipeline_init_param,
                verbosity=verbosity,
                evn_config=self._evn_config,
            )
        else:
            srom_single_node_search_async(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                self._sromgraph.paths,
                self.cv,
                self.scoring,
                mode,
                self.groups,
                max_eval_time_minute,
                random_state,
                total_execution_time,
                self._pipeline_type,
                self._pipeline_init_param,
                verbosity,
                self._evn_config,
                result_queue,
            )

    def _call_spark_node_search(
        self,
        X,
        y,
        param_grid,
        num_option_per_pipeline,
        n_jobs,
        pre_dispatch,
        mode,
        max_eval_time_minute,
        random_state,
        total_execution_time,
        verbosity,
        result_queue=None,
    ):
        from autoai_ts_libs.deps.srom.pipeline.execution_types.srom_spark_search import (
            srom_spark_search,
            srom_spark_search_async,
        )
        from pyspark import SparkContext
        from autoai_ts_libs.deps.srom.utils.package_version_check import check_pyspark_version

        check_pyspark_version()

        if "SparkConf" in self._evn_config:
            from pyspark import SparkConf

            conf = SparkConf()
            for k in self._evn_config["SparkConf"]:
                if k == "master":
                    master_str = self._evn_config["SparkConf"][k]
                    conf.setMaster(master_str)
                else:
                    conf.set(k, self._evn_config["SparkConf"][k])
            print(conf.getAll())
            sc = SparkContext.getOrCreate(conf=conf)
        else:
            sc = SparkContext.getOrCreate()

        if verbosity == "high":
            # The following is useful for debugging purposes
            LOGGER.info(
                "*****exectype is spark_node_random_search. srom_spark_search being invoked*****"
            )
        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
                self.best_fit_time,
                self.best_score_time,
            ) = srom_spark_search(
                X,
                y,
                sc=sc,
                param_grid=param_grid,
                num_option_per_pipeline=num_option_per_pipeline,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                max_eval_time_minute=max_eval_time_minute,
                mode=mode,
                groups=self.groups,
                cross_val_score=self._cross_val_score,
                pipeline_type=self._pipeline_type,
                pipeline_init_param=self._pipeline_init_param,
                random_state=random_state,
                verbosity=verbosity,
                evn_config=self._evn_config,
            )
        else:
            srom_spark_search_async(
                X,
                y,
                sc=sc,
                param_grid=param_grid,
                num_option_per_pipeline=num_option_per_pipeline,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                max_eval_time_minute=max_eval_time_minute,
                mode=mode,
                groups=self.groups,
                cross_val_score=self._cross_val_score,
                pipeline_type=self._pipeline_type,
                pipeline_init_param=self._pipeline_init_param,
                random_state=random_state,
                verbosity=verbosity,
                evn_config=self._evn_config,
                result_queue=result_queue,
            )

    def _call_evolutionary_search(
        self,
        X,
        y,
        param_grid,
        num_option_per_pipeline,
        n_jobs,
        pre_dispatch,
        mode,
        max_eval_time_minute,
        random_state,
        total_execution_time,
        verbosity,
        result_queue=None,
    ):
        from autoai_ts_libs.deps.srom.pipeline.execution_types.evolutionary_model_selection import (
            evolutionary_search,
            evolutionary_search_async,
        )

        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
            ) = evolutionary_search(
                X,
                y,
                param_grid=param_grid,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                pre_dispatch=pre_dispatch,
                n_jobs=n_jobs,
                max_eval_time_minute=max_eval_time_minute,
                random_state=random_state,
                verbosity=verbosity,
            )
        else:
            evolutionary_search_async(
                X,
                y,
                param_grid=param_grid,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                pre_dispatch=pre_dispatch,
                n_jobs=n_jobs,
                max_eval_time_minute=max_eval_time_minute,
                random_state=random_state,
                verbosity=verbosity,
                result_queue=result_queue,
            )

    def _call_rbfopt_search(
        self,
        X,
        y,
        param_grid,
        num_option_per_pipeline,
        n_jobs,
        pre_dispatch,
        mode,
        max_eval_time_minute,
        random_state,
        total_execution_time,
        verbosity,
        result_queue=None,
    ):
        from autoai_ts_libs.deps.srom.pipeline.execution_types.rbfopt_model_selection import (
            rbfopt_search,
            rbfopt_search_async,
        )

        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
            ) = rbfopt_search(
                X,
                y,
                param_grid=param_grid,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                pre_dispatch=pre_dispatch,
                n_jobs=n_jobs,
                num_option_per_pipeline=num_option_per_pipeline,
                random_state=random_state,
                verbosity=verbosity,
            )
        else:
            rbfopt_search_async(
                X,
                y,
                param_grid=param_grid,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                pre_dispatch=pre_dispatch,
                n_jobs=n_jobs,
                num_option_per_pipeline=num_option_per_pipeline,
                random_state=random_state,
                verbosity=verbosity,
                result_queue=result_queue,
            )

    def _call_hyperband_search(
        self,
        X,
        y,
        param_grid,
        num_option_per_pipeline,
        n_jobs,
        pre_dispatch,
        mode,
        max_eval_time_minute,
        random_state,
        total_execution_time,
        verbosity,
        result_queue=None,
    ):
        from autoai_ts_libs.deps.srom.pipeline.execution_types.hyperband_model_selection import (
            hyperband_search,
            hyperband_search_async,
        )

        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
            ) = hyperband_search(
                X,
                y,
                param_grid=param_grid,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                pre_dispatch=pre_dispatch,
                n_jobs=n_jobs,
                num_option_per_pipeline=num_option_per_pipeline,
                random_state=random_state,
                verbosity=verbosity,
            )
        else:
            hyperband_search_async(
                X,
                y,
                param_grid=param_grid,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                pre_dispatch=pre_dispatch,
                n_jobs=n_jobs,
                num_option_per_pipeline=num_option_per_pipeline,
                random_state=random_state,
                verbosity=verbosity,
                result_queue=result_queue,
            )

    def _call_bayesian_search(
        self,
        X,
        y,
        param_grid,
        num_option_per_pipeline,
        n_jobs,
        pre_dispatch,
        mode,
        max_eval_time_minute,
        random_state,
        total_execution_time,
        verbosity,
        result_queue=None,
    ):
        from autoai_ts_libs.deps.srom.pipeline.execution_types.bayesian_model_selection import (
            bayesian_search,
            bayesian_search_async,
        )

        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
            ) = bayesian_search(
                X,
                y,
                param_grid=param_grid,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                pre_dispatch=pre_dispatch,
                n_jobs=n_jobs,
                num_option_per_pipeline=num_option_per_pipeline,
                max_eval_time_minute=max_eval_time_minute,
                random_state=random_state,
                verbosity=verbosity,
            )
        else:
            bayesian_search_async(
                X,
                y,
                param_grid=param_grid,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                pre_dispatch=pre_dispatch,
                n_jobs=n_jobs,
                num_option_per_pipeline=num_option_per_pipeline,
                max_eval_time_minute=max_eval_time_minute,
                random_state=random_state,
                verbosity=verbosity,
                result_queue=result_queue,
            )

    def _call_serverless_search(
        self,
        X,
        y,
        param_grid,
        num_option_per_pipeline,
        n_jobs,
        pre_dispatch,
        mode,
        max_eval_time_minute,
        random_state,
        total_execution_time,
        verbosity,
        upload_data,
        result_queue=None,
    ):
        from autoai_ts_libs.deps.srom.pipeline.execution_types.srom_lithops_search import (
            srom_lithops_search,
            srom_lithops_search_async,
        )

        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
                self.execution_time_for_best_estimators,
                self.activations,
            ) = srom_lithops_search(
                X,
                y,
                param_grid=param_grid,
                num_option_per_pipeline=num_option_per_pipeline,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                max_eval_time_minute=max_eval_time_minute,
                mode="random",
                groups=self.groups,
                cross_val_score=self._cross_val_score,
                evn_config=self._evn_config,
                upload_data=upload_data,
                random_state=random_state,
                verbosity=verbosity,
                pipeline_type=self._pipeline_type,
                pipeline_init_param=self._pipeline_init_param,
            )
        else:
            srom_lithops_search_async(
                X,
                y,
                param_grid=param_grid,
                num_option_per_pipeline=num_option_per_pipeline,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                max_eval_time_minute=max_eval_time_minute,
                mode="random",
                groups=self.groups,
                cross_val_score=self._cross_val_score,
                evn_config=self._evn_config,
                upload_data=upload_data,
                random_state=random_state,
                verbosity=verbosity,
                pipeline_type=self._pipeline_type,
                pipeline_init_param=self._pipeline_init_param,
                result_queue=result_queue,
            )

    def _call_ray_search(
        self,
        X,
        y,
        param_grid,
        num_option_per_pipeline,
        n_jobs,
        pre_dispatch,
        mode,
        max_eval_time_minute,
        random_state,
        total_execution_time,
        verbosity,
        result_queue=None,
    ):
        from autoai_ts_libs.deps.srom.pipeline.execution_types.srom_ray_search import (
            srom_ray_search,
            srom_ray_search_async,
        )

        if not result_queue:
            (
                self.best_estimators,
                self.best_scores,
                self.number_of_combinations,
                self.best_scores_std,
                self.execution_time_for_best_estimators,
                self.activations,
            ) = srom_ray_search(
                X,
                y,
                total_execution_time=total_execution_time,
                param_grid=param_grid,
                num_option_per_pipeline=num_option_per_pipeline,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                max_eval_time_minute=max_eval_time_minute,
                mode="random",
                groups=self.groups,
                cross_val_score=self._cross_val_score,
                evn_config=self._evn_config,
                random_state=random_state,
                verbosity=verbosity,
            )
        else:
            srom_ray_search_async(
                X,
                y,
                total_execution_time=total_execution_time,
                param_grid=param_grid,
                num_option_per_pipeline=num_option_per_pipeline,
                paths=self._sromgraph.paths,
                cv=self.cv,
                scorer=self.scoring,
                max_eval_time_minute=max_eval_time_minute,
                mode="random",
                groups=self.groups,
                cross_val_score=self._cross_val_score,
                evn_config=self._evn_config,
                random_state=random_state,
                verbosity=verbosity,
                result_queue=result_queue,
            )

    def _call_custom_search(self):
        pass

    def execute(
        self,
        X,
        y=None,
        exectype="single_node_complete_search",
        n_jobs=multiprocessing.cpu_count(),
        pre_dispatch="2*n_jobs",
        verbosity="low",
        param_grid=SROMParamGrid(gridtype="empty"),
        num_option_per_pipeline=10,
        max_eval_time_minute=2,
        upload_data=True,
        random_state=None,
        total_execution_time=10,
    ):
        """
        Execute method runs cross validation on a given dataset along all possible paths in the DAG. \
        There are spark as well as single node implementations of execute which can be used to speed \
        up model as well as for hyper-parameter selection. \
        SROMParamGrid is used to set the possible parameter values which is tried for each algorithm.
        
        Parameters:
            X (pandas dataframe or numpy array): The dataset to be used for model selection. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. This is optional, \
                if target_column is added in the meta data, it is used from there. \
                shape = [n_samples] or [n_samples, n_output].
            exectype (String): Default value is "single_node_complete_search".
                "spark": Executes the pipeline on a Spark cluster.
                "single_node" or "single_node_complete_search": Executes the pipeline for all \
                    parameter samples on single node.
                "single_node_random_search": Executes the pipeline for random parameter samples \
                    on single node.
                "spark_node_random_search": Executes the pipeline for random parameter samples \
                    on spark.
                "spark_node_complete_search": Executes the pipeline for all parameter samples \
                    on spark.
                "pipeline_path_complete_search": Option is only avaialble for WML executor \
                    (run a particular path).
                "pipeline_path_random_search": Option is only avaialble for WML executor \
                    (run a particular path).
                "evolutionary_search": Execute each pipeline path using evolutionary search.
                "rbfopt_search": Execute each pipeline path using rbfopt search.
                "hyperband_search" : Execute each pipeline path using hyperband search.
                "bayesian_search" : Execute each pipeline path using bayesian_search.
            n_jobs (int, optional): Default value is multiprocessing.cpu_count(). Number of parallel \
                jobs. Only required for "single_node_random_search"/"single_node_complete_search"
            pre_dispatch (:int:string, optional): Default valueis "2*n_jobs". \
                Controls the number of jobs that get dispatched during parallel execution. \
                Reducing this number can be useful to avoid an explosion of memory consumption \
                when more jobs get dispatched than CPUs can process.
            verbosity (String, Optional) Default value is "low". Possible values: "low", "medium",\
                "high".
            param_grid (dict): Default is {}.Dictionary with parameters names (string) as keys and \
                lists of parameter settings to try as values, or a list of such dictionaries, in \
                which case the grids spanned by each dictionary in the list are explored.
            num_option_per_pipeline (integer): Default is 10. Number of parameter settings that are \
                sampled. This parameter is applicable for "spark_node_random_search" and \
                "single_node_random_search" exectype.
            max_eval_time_minute (integer): In minutes. Default is 2. Maximum timeout for execution of \
                pipelines with unique parameter grid combination. This parameter is applicable for \
                "spark_node_random_search" and "spark_node_complete_search" exectype.
            upload_data (Boolean) = False,
            random_state (int or None) = None,
            total_execution_time (integer, minute) = 10

        Returns (tuple):
            Returns the tuple containing:
                best_estimator (sklearn Pipeline instance)
                best_score (numpy.float64)

        Raises:
            BaseException:
                If exectype is not supported.
        """
        X, y = self._pre_exec(
            X,
            y,
            exectype,
            verbosity,
            param_grid,
            max_eval_time_minute,
            total_execution_time,
        )

        # execution

        if self._sromgraph.graphtype == 2 and exectype == "single_node":
            self._call_srom_single_node_functional_dag(
                X, param_grid, total_execution_time
            )
            return self.best_estimators, self.best_scores
        elif self._sromgraph.graphtype == 2 and exectype == "spark_node":
            self._call_srom_spark_functional_dag(X, param_grid, total_execution_time)
            return self.best_estimators, self.best_scores
        elif exectype == "single_node_complete_search" or exectype == "single_node":
            self._call_srom_single_node_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "exhaustive",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        elif exectype == "single_node_random_search":
            self._call_srom_single_node_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "random",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        elif exectype == "spark_node_random_search":
            self._call_spark_node_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "random",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        elif exectype == "spark_node_complete_search":
            self._call_spark_node_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "exhaustive",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        elif exectype == "evolutionary_search":
            self._call_evolutionary_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "evolutionary",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        elif exectype == "rbfopt_search":
            self._call_rbfopt_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "rbfopt",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        elif exectype == "hyperband_search":
            self._call_hyperband_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "hyperband",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        elif exectype == "bayesian_search":
            self._call_bayesian_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "bayesian",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        elif exectype == "serverless_search":
            self._call_serverless_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "serverless",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
                upload_data,
            )
        elif exectype == "ray_search":
            self._call_ray_search(
                X,
                y,
                param_grid,
                num_option_per_pipeline,
                n_jobs,
                pre_dispatch,
                "ray",
                max_eval_time_minute,
                random_state,
                total_execution_time,
                verbosity,
            )
        else:
            raise BaseException("Execution method not supported")

        self._post_exec(verbosity)
        return self.best_estimator, self.best_score

    def get_best_model(self):
        """
        Return the best pipeline model.

        Return:
            best estimator, which is a pipeline object.
        """
        LOGGER.warning("Deprecated: Instead of this use get_best_estimator method.")
        return self.best_estimator

    def get_best_score(self):
        """
        Return the score corresponding to the best performing pipeline.

        Return:
            best score.
        """
        return self.best_score

    def set_best_model(self, pipeline):
        """
        Set/override the best model. This option is only rarely used when \
        a user is not satisfied with the best model selected by executing the DAG. \

        Parameters:
            pipeline: Pipeline object to set the best model to. For scikit pipeline, \
                it is an object of class sklearn.pipeline.Pipeline. For Spark ML, it is \
                an object of class pyspark.ml.Pipeline. Only scikit supported as of now.
        """
        LOGGER.warning("Deprecated: Instead of this use set_best_estimator method.")
        if isinstance(pipeline, Pipeline):
            self.best_estimator = pipeline
            self.best_score = None
        else:
            raise BaseException("Model type not supported")

    def get_best_estimators_and_scores(self):
        """
        Retrieves all the best_estimators and their corresponding scores.

        Returns:
            best_estimators (list): List of estimator pipelines which capture the best \
                hyper-parameters for each pipeline path in the DAG.
            best_scores (list): List of scores corresponding to best_estimators.
        """
        return self.best_estimators, self.best_scores

    def fit(self, X, y=None, **kwargs):
        """
        Train the best model on the given data.
        
        Parameters:
            X (pandas dataframe or numpy array): Training dataset. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Target vector to be used. \
                if target_column is added in the meta data, it is \
                used from there. shape = [n_samples] or [n_samples, n_output].
            kwargs (dict): Dictionary of optional parameters.

        Returns:
            Returns the trained pipeline object. \
            This would be an instance of the original pipeline class \
            i.e. sklearn.pipeline.Pipeline or pyspark.ml.Pipeline not SROMPipeline.
        """

        # see if best_estimator is set or not
        error_msg = (
            "fit should be a called only if best_estimator is initialized or generated."
        )
        if self.best_estimator is None:
            raise Exception(error_msg)

        # get the data
        X, y = self._specialdatatransforms(X, y)

        return self.best_estimator.fit(X, y)

    def predict(self, X, **kwargs):
        """
        Predict the class labels/regression targets/anomaly scores etc. using \
        the trained model pipeline.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.
            kwargs (dict): Dictionary of optional parameters.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs]
        """

        if self.best_estimator is None:
            raise Exception("Train the model first by calling execute/fit method")

        # get the data
        X, _ = self._specialdatatransforms(X, None)
        return self.best_estimator.predict(X, **kwargs)

    def predict_proba(self, X, **kwargs):
        """
        Predict the class probability/regression targets/anomaly scores etc. using \
        the trained model pipeline.
        
        Args:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.
            kwargs (dict): Dictionary of optional parameters.
        
        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """

        if self.best_estimator is None:
            raise Exception("Train the model first by calling execute/fit method")

        # get the data
        X, _ = self._specialdatatransforms(X, None)
        return self.best_estimator.predict_proba(X)

    def score(self, X, y=None):
        """
        Parameters:
            X (pandas dataframe or numpy array): Test samples.
            y (pandas dataframe or numpy array): Ground truth values.

        Returns:
            Performance metric value.

        Raises:
            Exception:
                1. If best_estimator is None.
                2. If scoring option is not supported.
        """

        if self.best_estimator is None:
            raise Exception("Train the model first by calling execute/fit method")

        X, y = self._specialdatatransforms(X, y)

        if isinstance(self.scoring, collections.Callable):
            # callable scorer
            score_value = self.scoring(self.best_estimator, X, y)
        else:
            if self.scoring:
                from sklearn.metrics import SCORERS as sklearn_score_mapping

                if self.scoring in sklearn_score_mapping:
                    # string scorer
                    score_value = sklearn_score_mapping[self.scoring](
                        self.best_estimator, X, y
                    )
                else:
                    raise Exception("Scoring option is not supported")
            else:
                # default scorer
                score_value = self.best_estimator.score(X, y)

        return score_value

    def pipeline_graph_result_analysis(self, top_k=5):
        """
        Parameters:
            top_k (int): Ground truth values.
            
        Returns:
            A dictonary, with key = name of nodes, value = % of timesthat node appears \
            in top-k best paths.
            Note that value can be > 1, as some time there is a tie for last best path.
        """

        if top_k <= 0:
            return []

        A = self.best_scores

        # added >= 0, to enable more search on classifier/regressor's parameter.
        # ideally we shd be aware about is it classifier or regression problem
        # such as we can esitmate the upper bound and
        # stop the search as early as possible.
        # such as r2=1, mse=0, the upper bound knowledge.
        # this early stopping functionality will be added soon.

        tmpS = []
        for item in A:
            if np.abs(item) >= 0:
                tmpS.append(item)

        node_operations_stats = {}
        if len(tmpS) == 0:
            return node_operations_stats

        tmpS = np.sort(tmpS)
        thresholdS = tmpS[0]
        if len(tmpS) > top_k:
            thresholdS = tmpS[-top_k]

        for i in range(len(self._sromgraph.paths)):
            if self.best_scores[i] >= thresholdS:
                for path_node in self._sromgraph.paths[i]:
                    if path_node[0] in node_operations_stats.keys():
                        node_operations_stats[path_node[0]] = (
                            node_operations_stats[path_node[0]] + 1
                        )
                    else:
                        node_operations_stats[path_node[0]] = 1

        for node_key in node_operations_stats.keys():
            node_operations_stats[node_key] = node_operations_stats[node_key] / (
                top_k * 1.0
            )

        return node_operations_stats

    def __str__(self):
        return (
            self.__class__.__name__
            + "(Pipeline Id="
            + str(self.pipeline_id)
            + ", Stages="
            + str(self.stages)
            + ", Id Column="
            + str(self.id_column)
            + ", Time Column="
            + str(self.time_column)
            + ", Label Column="
            + str(self.label_column)
            + ", Label Prefix="
            + str(self.label_prefix)
            + ", Cross Validation="
            + str(self.cv)
            + ", Scoring="
            + str(self.scoring)
            + ", Best Estimator="
            + str(self.best_estimator)
            + ", Best Score="
            + str(self.best_score)
            + ")"
        )

    def __repr__(self):
        return self.__str__()

    def get_best_pipelines(self):
        pass
