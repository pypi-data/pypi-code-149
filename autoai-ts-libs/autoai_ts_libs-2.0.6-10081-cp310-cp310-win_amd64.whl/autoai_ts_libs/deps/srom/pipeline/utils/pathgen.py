# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2019 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
Generators for 'unrolling' an underlying DAG of operations.
This module does not handle distribution or tracking of execution of DAG paths.
"""

import logging
import copy

from sklearn.model_selection._search import ParameterGrid, ParameterSampler

from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.utils.pipeline_utils import pipeline_and_grid_generator

LOGGER = logging.getLogger(__file__)


def with_random_hpgrid(
    apipeline,
    aparamgrid,
    nsamples,
    pipeline_type: object,
    pipeline_init_params: dict,
    samplefraction=1.0,
):
    """Returns a list of pipelines, each with a parameter grid generated
        from sampling from given aparamgrid.


    Arguments:
        apipeline SROMPipeline -- a SROMPipeline instance
        aparamgrid SROMParamGrid -- a SROMParamGrid instance (ideally with enough implied elements to support nsamples)
        nsamples int -- number of random samples to draw from aparamgrid

    Returns:
        a generator object for paths
    """

    # pipelines, param_grids = _pipelines_and_grids(apipeline, aparamgrid, sample)
    for ypipeline, ygrid in pipeline_and_grid_generator(
        paths=apipeline.paths,
        grid=aparamgrid,
        sample=samplefraction,
        pipeline_init_param=pipeline_init_params,
        pipeline_type=pipeline_type,
    ):

        sklparamgrid = ParameterGrid(ygrid)
        # if our grid is too small to support the number of samples requested,
        # use everything that's there (getting as close as possible to nsamples)
        if len(sklparamgrid) < nsamples:
            param_list = list(sklparamgrid)
        else:
            param_list = list(ParameterSampler(ygrid, n_iter=nsamples))

        for params in param_list:
            apipeline = copy.deepcopy(ypipeline)
            apipeline.set_params(**params)
            LOGGER.debug("yielding %s", apipeline)
            yield apipeline
