# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: srom_spark_search
   :synopsis: This module is used for spark based exhaustive/random search. \
        Here, pipeline is executed with all/some parameters given in param grid \
        for each estimator on spark cluster depending on mode.It returns the best \
        scores, best estimators and number of combinations.

.. moduleauthor:: SROM Team
"""
import logging
from functools import partial

import numpy as np
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.pipeline.utils.functional_pipeline import FunctionPipeline
from autoai_ts_libs.deps.srom.utils.pipeline_utils import gen_pipeline_and_grid
from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException

LOGGER = logging.getLogger(__name__)


def pipeline_execution(tup, X_bc):
    """
    Performs time bound execution of pipeline. \
    If cv_learning task is not completed in max_eval_time_minute_bc minutes \
    then that task is terminated.

    Parameters:
        tup (tuple): (parameters, pipeline_index)
            parameters(list, dict): Pipeline grid combination parameters.
            pipeline_index (integer):Index for the pipeline for which cross \
                validation is to be executed.
    """
    (pipeline_paths_i, param_grid_i) = tup
    try:
        local_X = X_bc.value

        pipeline_paths_i.fit(local_X, **param_grid_i)
        score = pipeline_paths_i.score

        return (pipeline_paths_i, param_grid_i, score)
    except Exception:
        return (pipeline_paths_i, param_grid_i, np.NaN)


def srom_spark_transform_async(X, sc, paths, param_grid=None, total_execution_time=10, result_queue=None):
    '''
    Asynchroneous version of srom_spark_transform
    Args:
        X ([type]): [description]
        sc ([type]): [description]
        paths ([type]): [description]
        param_grid ([type], optional): [description]. Defaults to None.
        total_execution_time (int, optional): [description]. Defaults to 10.

    Raises:
        IncorrectValueException: [description]

    Returns:
        [type]: [description]
    '''
    srom_spark_transform(X, sc, paths, param_grid, total_execution_time, result_queue)
    return


def srom_spark_transform(
    X, sc, paths, param_grid=None, total_execution_time=10, result_queue=None
):
    """[summary]

    Args:
        X ([type]): [description]
        sc ([type]): [description]
        paths ([type]): [description]
        param_grid ([type], optional): [description]. Defaults to None.
        total_execution_time (int, optional): [description]. Defaults to 10.

    Raises:
        IncorrectValueException: [description]

    Returns:
        [type]: [description]
    """

    if not sc:
        from pyspark import SparkContext
        from autoai_ts_libs.deps.srom.utils.package_version_check import check_pyspark_version

        check_pyspark_version()
        sc = SparkContext.getOrCreate()
    if not paths:
        raise IncorrectValueException("Paths should be not be None or empty.")

    if not param_grid:
        param_grid = SROMParamGrid(gridtype="empty")

    # following is return values
    pipelines = []
    params = []
    scores = []

    if not param_grid:
        param_grid = SROMParamGrid(gridtype="empty")
    pipeline_paths, param_grids = gen_pipeline_and_grid(
        paths, param_grid, pipeline_type=FunctionPipeline
    )

    # we generate a sample configurations for each pipelines (based on number of options)
    pipeline_param_grid = []
    for index, _ in enumerate(pipeline_paths):
        pipeline_param_grid.append((pipeline_paths[index], param_grids[index]))

    number_of_partitions = min(1000, len(pipeline_paths))
    pipeline_param_grid_rdd = sc.parallelize(pipeline_param_grid, number_of_partitions)

    # the values to be shared across the executors
    X_bc = sc.broadcast(X)
    # time bound execution, if execution does not complete in two minutes, then it stop the method

    # get the scoring results
    results = pipeline_param_grid_rdd.map(
        partial(pipeline_execution, X_bc=X_bc,)
    ).collect()
    LOGGER.debug("***** score_results in srom_spark_search is " + str(results))
    for index in range(len(results)):
        pipelines.append(results[index][0])
        params.append(results[index][1])
        scores.append(results[index][2])
        if result_queue is not None:
            result_queue.put([pipelines, scores, params, []])
    return pipelines, scores, params, []
