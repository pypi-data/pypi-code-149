# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

import logging
import time

import numpy as np

from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.utils.pipeline_utils import gen_pipeline_and_grid
from autoai_ts_libs.deps.srom.pipeline.utils.functional_pipeline import FunctionPipeline

LOGGER = logging.getLogger(__name__)


def srom_single_node_transform_async(
    X,
    paths,
    param_grid,
    total_execution_time,
    result_out=None
):
    '''
    '''
    srom_single_node_transform(
        X,
        paths,
        param_grid,
        total_execution_time,
        result_out)
    return


def srom_single_node_transform(
    X,
    paths,
    param_grid=None,
    total_execution_time=10,
    result_out=None
):
    """Single node exploration."""
    if not paths:
        raise IncorrectValueException("Paths should be not be None or empty.")

    # Initialize return values
    pipelines = []
    params = []
    scores = []

    if not param_grid:
        param_grid = SROMParamGrid(gridtype="empty")
    pipeline_paths, param_grids = gen_pipeline_and_grid(
        paths, param_grid, pipeline_type=FunctionPipeline
    )

    experiment_start_time = time.time()
    elapsed_time = 0
    for index, _ in enumerate(pipeline_paths):
        pipeline = pipeline_paths[index]
        try:
            pipeline.fit(X, **param_grids[index])

            end_time = time.time()
            elapsed_time = (end_time - experiment_start_time) / 60.0

            pipelines.append(pipeline)
            params.append(param_grids[index])
            scores.append(pipeline.score)
        except Exception:
            pipelines.append(pipeline)
            params.append(param_grids[index])
            scores.append(np.NaN)

        # we gracefully exit the loop, as crossed the allocated time
        if total_execution_time != -1 and elapsed_time > total_execution_time:
            for index_ in range(index, len(paths)):
                pipelines.append(pipeline)
                params.append(param_grids[index])
                scores.append(np.nan)
        if result_out is not None:
            result_out.put([pipelines, scores, params, []])
    return pipelines, scores, params, []
