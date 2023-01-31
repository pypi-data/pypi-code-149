# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.f

"""
.. module:: srom_spark_search
   :synopsis: This module is used for spark based exhaustive/random search. \
        Here, pipeline is executed with all/some parameters given in param grid \
        for each estimator on spark cluster depending on mode.It returns the best \
        scores, best estimators and number of combinations.

.. moduleauthor:: SROM Team
"""
import logging
import queue
from functools import partial

import numpy as np
from pyspark import SparkContext
from sklearn.base import clone
from sklearn.model_selection import ParameterSampler
from sklearn.model_selection._search import ParameterGrid
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.pipeline.execution_types.exploration.spark_search_functions import *
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.utils.pipeline_utils import (ModelOutput, gen_pipeline_and_grid,
                                       verbosity_to_verbose_mapping)
from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException

LOGGER = logging.getLogger(__name__)



def reduce_function(x, y):
    # to be used in srom_spark_search
    if np.nanmax([x[1], y[1]]) == x[1]:
        return x
    else:
        return y

# time bound execution, if execution does not complete in two minutes, then it stop the method
def timebound_model_execution(
    tup,
    X_bc,
    y_bc,
    max_eval_time_minute_bc,
    groups_bc,
    pipelines_bc,
    cross_val_score,
    cv,
    scorer,
    verbose,
):
    """
    Performs time bound execution of pipeline. \
    If cv_learning task is not completed in max_eval_time_minute_bc minutes \
    then that task is terminated.

    Parameters:
        tup (tuple): (parameters, pipeline_index)
            parameters(list, dict): Pipeline grid combination parameters.
            pipeline_index (integer):Index for the pipeline for which cross \
                validation is to be executed.

    Returns: 
        Tuple (pipeline_index, (parameters, score)):
            pipeline_index (integer): Index for the pipeline for which cross \
                validation is to be executed.
            parameters (list, dict): Pipeline grid combination parameters.
            score (integer): Mean test score or nan if execution time exceeds \
                max_eval_time_minute_bc for processing.
    """
    (parameters, pipeline_index) = tup
    import multiprocessing as mp

    output = mp.Queue()
    import time

    # task_timeout in seconds
    task_timeout = max_eval_time_minute_bc.value * 60.0
    ret_result = (pipeline_index, (parameters, np.NaN, np.NaN, np.NaN, np.NaN))
    import platform

    tup = (
        parameters,
        pipeline_index,
        X_bc.value,
        y_bc.value,
        groups_bc.value,
        clone(pipelines_bc.value[pipeline_index]),
        cross_val_score,
        cv,
        scorer,
        verbose,
    )
    if "Windows" in str(platform.platform()) or cv == 1:
        if cv == 1:
            task = mp.Process(target=train_test_score, args=(tup, output))
        else:
            task = mp.Process(target=cv_learning_window, args=(tup, output))
    else:
        task = mp.Process(target=cv_learning, args=(tup, output))
        
    # start thread
    task.start()
    try:
        ret_result = output.get(True, task_timeout)
    except queue.Empty:
        LOGGER.error(
            "Pipeline Execution is not completed: %s", pipelines_bc.value[pipeline_index]
        )
        if task.is_alive():
            task.terminate()
            time.sleep(1)
            task.join()
            time.sleep(1)
    except Exception as ex:
        LOGGER.error("Pipeline failed: %s", pipelines_bc.value[pipeline_index])
        LOGGER.error("Pipeline failed reason: %s", str(ex))
        LOGGER.exception(str(ex))
        pass
        
    return ret_result


def srom_spark_search_async(
    X,
    y,
    sc : SparkContext,
    param_grid,
    paths,
    cv,
    scorer,
    max_eval_time_minute,
    num_option_per_pipeline=10,
    mode="exhaustive",
    groups=None,
    random_state=None,
    total_execution_time=10,
    cross_val_score=None,
    pipeline_type=Pipeline,
    pipeline_init_param={},
    evn_config=None,
    verbosity='low',
    result_queue=None
):
    srom_spark_search(
        X,
        y,
        sc,
        param_grid,
        paths,
        cv,
        scorer,
        max_eval_time_minute,
        num_option_per_pipeline,
        mode,
        groups,
        cross_val_score,
        pipeline_type,
        pipeline_init_param,
        random_state,
        evn_config,
        verbosity,
        result_queue
    )
    return


def srom_spark_search(
    X,
    y,
    sc : SparkContext,
    param_grid,
    paths,
    cv,
    scorer,
    max_eval_time_minute,
    num_option_per_pipeline=10,
    mode="exhaustive",
    groups=None,
    cross_val_score=None,
    pipeline_type=Pipeline,
    pipeline_init_param={},
    random_state=None,
    evn_config=None,
    verbosity='low',
    result_queue=None
):
    """
    Parameters:
        X (pandas dataframe or numpy array): The dataset to be used for model selection. \
            shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        y (pandas dataframe or numpy array): Target vector to be used. This is optional, \
            if target_column is added in the meta data, it is used from there. \
            shape = [n_samples] or [n_samples, n_output].
        sc : spark context.
        param_grid (dict): Dictionary with parameter names(string) as keys and lists of parameter \
            settings to try as values, or a list of such dictionaries, in which case the grids spanned \
            by each dictionary in the list are explored.
        paths (list): Consists of paths in scikit pipeline.
        cv (integer, cross-validation generator or an iterable): Determines the cross-validation \
            splitting strategy.
        scorer (string, callable, list/tuple, dict or None): A single string or a callable to \
            evaluate the predictions on the test set.
        max_eval_time_minute (integer) (minutes):Maximum timeout for execution of pipelines with \
            unique parameter grid combination.
        num_option_per_pipeline (integer): Default: 10.Number of parameter settings that are sampled. \
            This parameter is applicable if mode is 'random'
        mode (String): Default: "exhaustive".Possible values: "random" or "exhaustive".

    Returns: (tuple)
        best_estimators: (list)
        best_scores: (list)
        number_of_combinations: (integer)

    Raises:
        IncorrectValueException:
            1. If mode not in ['exhaustive', 'random'].
            2. If paths is none or empty.
            3. If num_option_per_pipeline is none or is not instance of integer \
               or num_option_per_pipeline is less than 1.
        Exception:
            Raises a generic exception.
    """
    spark_partition_limit = 1000
    if evn_config:
        if "numSlices" in evn_config.keys():
            spark_partition_limit = evn_config["numSlices"]

    # Validations
    if mode not in ["exhaustive", "random"]:
        raise IncorrectValueException(
            "Supported mode should be provided: 'exhaustive' or 'random'"
        )
    if not sc:
        from pyspark import SparkContext
        from autoai_ts_libs.deps.srom.utils.package_version_check import check_pyspark_version

        check_pyspark_version()
        sc = SparkContext.getOrCreate()
    if not paths:
        raise IncorrectValueException("Paths should be not be None or empty.")
    if (
        not num_option_per_pipeline
        or not isinstance(num_option_per_pipeline, int)
        or num_option_per_pipeline < 1
    ):
        raise IncorrectValueException(
            "Value of num_option_per_pipeline should be int and greater than 1."
        )
    if not param_grid:
        param_grid = SROMParamGrid(gridtype="empty")
    if not max_eval_time_minute:
        max_eval_time_minute = 2

    # setting the verbose parameter to be passed to the GridSearchCV
    verbose = verbosity_to_verbose_mapping(verbosity)

    # following three are return values
    # best_estimators is a list of all pipeline, and for each pipeline what is the best score
    number_of_combinations = 0
    best_estimators = []
    best_scores = []
    best_scores_std = []
    best_fit_time = []
    best_score_time = []

    pipelines, param_grids = gen_pipeline_and_grid(
        paths, param_grid, pipeline_type, pipeline_init_param
    )

    # we generate a sample configurations for each pipelines (based on number of options)
    pipeline_param_grid = []
    for pipeline_index in range(len(pipelines)):
        try:
            param_list = []
            grid_combo = ParameterGrid(param_grids[pipeline_index])
            is_total_space_smaller = (
                mode == "random" and len(grid_combo) < num_option_per_pipeline
            )
            if mode == "exhaustive" or is_total_space_smaller:
                if is_total_space_smaller:
                    LOGGER.debug(
                        """The total space of parameters is smaller than
                                    provided num_option_per_pipeline."""
                    )
                param_list = list(grid_combo)
            else:
                param_list = list(
                    ParameterSampler(
                        param_grids[pipeline_index],
                        n_iter=num_option_per_pipeline,
                        random_state=random_state,
                    )
                )
            for parameters in param_list:
                pipeline_param_grid.append((parameters, pipeline_index))
                number_of_combinations = number_of_combinations + 1
        except ValueError as value_error:
            LOGGER.debug(str(value_error))
        except Exception as exception:
            LOGGER.info(str(exception))
            raise exception

    number_of_partitions = min(spark_partition_limit, number_of_combinations)
    pipeline_param_grid_rdd = sc.parallelize(pipeline_param_grid, number_of_partitions)

    # the values to be shared across the executors
    X_bc = sc.broadcast(X)
    y_bc = sc.broadcast(y)
    groups_bc = sc.broadcast(groups)
    max_eval_time_minute_bc = sc.broadcast(max_eval_time_minute)
    pipelines_bc = sc.broadcast(pipelines)

    # get the scoring results
    if max_eval_time_minute == -1:
        score_results = (
            pipeline_param_grid_rdd.map(
                partial(
                    model_execution,
                    X_bc=X_bc,
                    y_bc=y_bc,
                    max_eval_time_minute_bc=max_eval_time_minute_bc,
                    groups_bc=groups_bc,
                    pipelines_bc=pipelines_bc,
                    cross_val_score=cross_val_score,
                    cv=cv,
                    scorer=scorer,
                    verbose=verbose,
                )
            )
            .reduceByKey(reduce_function)
            .collect()
        )
    else:
        score_results = (
            pipeline_param_grid_rdd.map(
                partial(
                    timebound_model_execution,
                    X_bc=X_bc,
                    y_bc=y_bc,
                    max_eval_time_minute_bc=max_eval_time_minute_bc,
                    groups_bc=groups_bc,
                    pipelines_bc=pipelines_bc,
                    cross_val_score=cross_val_score,
                    cv=cv,
                    scorer=scorer,
                    verbose=verbose,
                )
            )
            .reduceByKey(reduce_function)
            .collect()
        )
    LOGGER.debug("***** score_results in srom_spark_search is " + str(score_results))
    # process the result and arrange it in such a way that is expected by caller function
    for score_result in score_results:
        (
            pipeline_index,
            (parameters, score, score_std, fit_time, score_time),
        ) = score_result
        local_pipeline = pipelines[pipeline_index]
        local_pipeline.set_params(**parameters)
        best_estimators.append(local_pipeline)
        best_scores.append(score)
        best_scores_std.append(score_std)
        best_fit_time.append(fit_time)
        best_score_time.append(score_time)

        if result_queue is not None:
            result_queue.put([
                best_estimators,
                best_scores,
                number_of_combinations,
                best_scores_std,
                best_fit_time,
                best_score_time,
            ])

    # return - each path, its best parameters and score of the value
    return (
        best_estimators,
        best_scores,
        number_of_combinations,
        best_scores_std,
        best_fit_time,
        best_score_time,
    )
