# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Maintains pipeline utility functions
"""
import warnings
import logging
import random
import uuid
import io
from enum import Enum
import numpy as np
import pandas as pd
import copy
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.utils.srom_tabulate import tabulate
from collections.abc import Sequence

LOGGER = logging.getLogger(__name__)

#This code is obtained from the older version of sklearn
def _check_param_grid(param_grid):
    if hasattr(param_grid, "items"):
        param_grid = [param_grid]

    for p in param_grid:
        for name, v in p.items():
            if isinstance(v, np.ndarray) and v.ndim > 1:
                raise ValueError("Parameter array should be one-dimensional.")

            if isinstance(v, str) or not isinstance(v, (np.ndarray, Sequence)):
                raise ValueError(
                    "Parameter grid for parameter ({0}) needs to"
                    " be a list or numpy array, but got ({1})."
                    " Single values need to be wrapped in a list"
                    " with one element.".format(name, type(v))
                )

            if len(v) == 0:
                raise ValueError(
                    "Parameter values for parameter ({0}) need "
                    "to be a non-empty sequence.".format(name)
                )


def check_custom_stage_random_state(stages):
    """warns user to set random state parameter"""
    for sets in stages:
        for estimator in sets:
            try:
                if (estimator[1].get_params().__contains__("random_state")) and (
                    estimator[1].get_params()["random_state"] is None
                ):
                    warnings.warn(
                        "random_state argument not set for {0}".format(
                            estimator[1].__class__.__name__
                        ),
                        category=UserWarning,
                    )
            except Exception:
                pass


def get_pipeline_description(pipeline):
    """get pipeline description in string"""
    str_rep = "["
    for step in pipeline.steps:
        str_rep = str_rep + str(step) + ","
    str_rep = str_rep + "]"
    return str_rep.replace("\n", "").replace("\t", "").replace(" ", "")


def get_pipeline_name(pipeline):
    """get pipeline name in string"""
    str_rep = ""
    for step in pipeline.steps:
        str_rep = str_rep + step[0] + ","
    return str_rep.rstrip(",")


def create_pipeline_id():
    """
    create pipeline id
    """
    return uuid.uuid4().hex


def check_srom_pipeline_stages(stages):
    """
    check pipeline stages should be a list of lists or
    list of lists of tuples and it should be non-empty
    """
    error_msg = "Stages should be a list of lists or list of lists of tuples and it should be non-empty."
    if isinstance(stages, list) and stages:
        for stage in stages:
            if not isinstance(stage, list) or not stage:
                raise Exception(error_msg)
    else:
        raise Exception(error_msg)


def print_paths(paths):
    """
    Print pipeline paths in a tabular format.
    :param paths: A list of pipeline paths
    """
    try:
        rows = []
        for index, path in enumerate(paths):
            rows.append(["Model#", str(index + 1)])
            for key, estimator in enumerate(path):
                if isinstance(estimator, tuple):
                    rows.append(["Stage " + str(key + 1), str(estimator[0])])
                else:
                    rows.append(
                        ["Stage " + str(key + 1), str(estimator.__class__.__name__)]
                    )
        print(("-" * 80))
        print(
            (
                tabulate(
                    rows, headers=["Pipeline", "Detail"], tablefmt="grid", stralign=None
                )
            )
        )
        print(("-" * 80))
    except Exception as ex:
        LOGGER.error("Error while printing pipeline paths" + str(ex))


def print_estimators_and_scores(best_estimators, best_scores):
    """
    Given a list of estimators and their corresponding scores, print those in tabular format
    :param best_estimators: A list of pipeline estimator objects
    :param best_scores: Evaluation scores corresponding to the estimators
    """
    try:
        rows = []
        # Convert to the list instance
        if not isinstance(best_estimators, list):
            best_estimators = [best_estimators]
        if not isinstance(best_scores, list):
            best_scores = [best_scores]
        # Compute rows and print
        header = ["Model", "Stages", "Score"]
        for estimator_index, estimator in enumerate(best_estimators):
            row = []
            row.append([str(estimator_index + 1)])
            stage = []
            for _, step in enumerate(estimator.steps):
                stage.append(step[1])
            row.append(stage)
            row.append(["Score", str(best_scores[estimator_index])])
            rows.append(row)
        print(("-" * 80))
        print((tabulate(rows, header, tablefmt="grid", stralign=None)))
        print(("-" * 80))
    except Exception:
        LOGGER.error("Error while printing a list of estimators and scores.")


def get_pipeline_str(best_estimator):
    """
    Given the best estimator and its corresponding score
    :param best_estimator: A pipeline estimator object
    :param best_score: Evaluation scores corresponding to the estimators
    """
    pipeline_str = io.StringIO()
    pipeline_str.write("Pipeline(steps=[")
    for step in best_estimator.steps:
        pipeline_str.write("(%s)," % step[0])
    pipeline_str.write("])")
    return pipeline_str.getvalue()


def generate_param_grid(pipeline, param_grid):
    """
    Generates param grid from user provided parameters
    based on provided pipeline.
    :param pipeline: Pipeline created for a unique path
    :param param_grid: User provided parameters
    :return generated_param_grid
    """
    generated_param_grid = {}
    if param_grid and param_grid.default_param_grid:
        params = pipeline.get_params()
        for pipeline_param_key in params:
            user_param_value = param_grid.get_param(pipeline_param_key)
            if isinstance(user_param_value, np.ndarray):
                user_param_value = user_param_value.tolist()
            if user_param_value:
                generated_param_grid[pipeline_param_key] = user_param_value

    if generated_param_grid:
        # Validate generated param_grid
        _check_param_grid(generated_param_grid)
    return generated_param_grid


def pipeline_and_grid_generator(
    paths, grid, sample=1.0, pipeline_type=Pipeline, pipeline_init_param={}
):
    """Generates sklearn pipeline for each path and generates
        relevant grid parameters for each path.

    Arguments:
        paths (list): A list of pipeline paths, each path is an estimator.
        grid (SROMParamGrid): Instance of SROMParamGrid
        sample: random fraction to sample 0 < sample <= 1.0
    Returns a generator object of tuple: All the generated pipelines, and related grid parameters.
    """

    if not sample >= 0 and sample <= 1.0:
        raise Exception("sample must be between in range (0,1]")

    for path in paths:
        if random.random() > sample:
            continue
        pipeline = pipeline_type(path, **pipeline_init_param)
        param_grid = generate_param_grid(pipeline=pipeline, param_grid=grid)
        yield pipeline, param_grid


def gen_pipeline_and_grid(paths, grid, pipeline_type=Pipeline, pipeline_init_param={}):
    """
    Generates sklearn pipeline for each path and generates relevant grid parameters for each path.
    Args:
        paths (list): A list of pipeline paths, each path is an estimator.
        grid (SROMParamGrid): Instance of SROMParamGrid
    Returns tuple: All the generated pipelines, and related grid parameters.
    """
    pipelines = []
    param_grids = []
    labels = set()

    for pipeline, param_grid in pipeline_and_grid_generator(
        paths,
        grid,
        1.0,
        pipeline_type=pipeline_type,
        pipeline_init_param=pipeline_init_param,
    ):
        pipelines.append(pipeline)
        param_grids.append(param_grid)

        # Check if for any stage, user provided grid does not match
        # We will leverage the fact that parameter grid for a certain stage must
        # start with the name of the stage
        # Note: This might log false messages as user might have intentionally skipped parameters
        # for a particular stage
        for step in pipeline.named_steps:
            step_found = False
            step_with_seperator = step + "__"
            for p_grid in param_grid:
                if step_with_seperator in p_grid:
                    step_found = True
                    break
            if not step_found:
                labels.add(step)

    if grid.default_param_grid and labels:
        LOGGER.info(
            "No grid parameter matched for the following stages: %s", ", ".join(labels)
        )

    # Check if any of the user provided grid matches for the stages set
    if grid.default_param_grid and param_grids and not any(param_grids):
        LOGGER.warning("None of the grid parameters matched for the given stages.")

    return pipelines, param_grids


def trim_greater(val, params):
    """[summary]

    Args:
        val ([type]): [description]
        params ([type]): [description]

    Returns:
        [type]: [description]
    """
    s = set()
    for param in params:
        if param > val:
            x = max(1, val)
            s.add(x)
        else:
            s.add(param)
    new_params = sorted(s)
    return new_params


def trim_greater_or_equal(val, params):
    """[summary]

    Args:
        val ([type]): [description]
        params ([type]): [description]

    Returns:
        [type]: [description]
    """
    s = set()
    for param in params:
        if param >= val:
            x = max(1, val - 1)
            s.add(x)
        else:
            s.add(param)
    new_params = sorted(s)
    return new_params


def clean_param_grid(param_grid, shape):
    """
    modifies parameter grid based on the data and set of rules associated with data and algorithms.
    Args:
        param_grid (SROMParamGrid): Instance of SROMParamGrid.
        shape (tuple): tuple containing no of rows and no of cols. Eg. X.shape
    Returns param_grid: Instance of modified SROMParamGrid.
    """

    # original untouched version of input grid
    ori_grid = copy.deepcopy(param_grid.get_param_grid())

    # filtering using # of columns
    column_grid_filter_config = {
        "selectkbest__k": trim_greater,
        "truncatedsvd__n_components": trim_greater_or_equal,
        "locallylinearembedding__n_components": trim_greater,
        "featureagglomeration__n_clusters": trim_greater,
    }
    column_grid_filter_config_value = shape[1]

    # filtering using # of rows
    row_grid_filter_config = {
        "kmean__k": trim_greater,
    }
    row_grid_filter_config_value = shape[0]

    # column and row based filtering
    row_column_grid_filter_config = {
        "pcaimputer__n_components": trim_greater,
        "kernelpcaimputer__n_components": trim_greater,
        "truncatedsvdimputer__n_components": trim_greater,
        "nmfimputer__n_components": trim_greater,
        "incrementalpcaimputer__n_components": trim_greater,
    }
    row_column_grid_filter_value = min(shape)

    # condition to be checked here
    # keys in each of the above grid? it has to be disjoint? column_grid_filter_config,
    # row_column_grid_filter_config

    for grid_filter_config, grid_filter_config_value in [
        (column_grid_filter_config, column_grid_filter_config_value),
        (row_column_grid_filter_config, row_column_grid_filter_value),
        (row_grid_filter_config, row_grid_filter_config_value),
    ]:
        # changing in each iteration
        grid = copy.deepcopy(param_grid.get_param_grid())

        for key in grid.keys():
            if key in grid_filter_config:
                attribute_value = grid[key]
                include_none = False
                if None in attribute_value:
                    include_none = True
                    attribute_value = list(filter(None, attribute_value))
                if len(attribute_value) == 0:
                    attribute_value.append(grid_filter_config_value)
                func = grid_filter_config[key]
                new_params = func(grid_filter_config_value, attribute_value)
                if include_none:
                    new_params.insert(0, None)
                param_grid.set_param(key, new_params)
                if len(new_params) == 0:
                    LOGGER.warning("grid parameters for {0} is empty.".format(key))
                else:
                    LOGGER.info(
                        "grid parameters for {0} updated from {1} to {2}".format(
                            key, ori_grid[key], new_params
                        )
                    )

    return param_grid


class ModelOutput(Enum):
    """
    Capture the model output
    """

    Timeout = 0
    Success = 1
    Failed = -1


class GraphType(Enum):
    """
    Capture the graph type
    """

    Default = 1
    Functional = 2


def verbosity_to_verbose_mapping(verbosity="low"):
    """
    this is a utility file to convert srom's verbosity to sklearn verbose
    mapping
    """
    verbose = 0
    if verbosity == "low":
        verbose = 0
    elif verbosity == "medium":
        verbose = 2
    elif verbosity == "high":
        verbose = 3
    else:
        pass
    return verbose


def rank_pipelines(pipeline_exp_results):
    """
    Rank pipelines from list of pipeline experiment results.
    Args:
        pipeline_exp_results (list): A list of pandas dataframes with pipeline experiment \
            results with columns 'model', 'CV score'.

    Returns tuple: All the generated pipelines, and related grid parameters.
    """
    all_pipelines = set()
    for df in pipeline_exp_results:
        df.dropna(subset=["CV score"], inplace=True)
        df["rank"] = df["CV score"].rank(method="dense", ascending=False)
        all_pipelines.update(df["model"].values)

    tuples = []
    for pipe in list(all_pipelines):
        tup = []
        for df in pipeline_exp_results:
            if pipe in df["model"].values:
                tup.append(df[df["model"] == pipe]["rank"].values[0])
        tup = tuple(tup)

        tuples.append(tup)

    rank_df = pd.DataFrame(
        {
            "model": list(all_pipelines),
            "rank_sum": [sum(tup) for tup in tuples],
            "counter": [len(tup) for tup in tuples],
        }
    )

    rank_df = rank_df.sort_values(["counter", "rank_sum"], ascending=[False, True])
    rank_df["rank_mean"] = rank_df["rank_sum"] / rank_df["counter"]
    rank_df["final_rank"] = rank_df["rank_mean"].rank(method="dense", ascending=True)
    rank_df.sort_values("final_rank", inplace=True)
    return rank_df
