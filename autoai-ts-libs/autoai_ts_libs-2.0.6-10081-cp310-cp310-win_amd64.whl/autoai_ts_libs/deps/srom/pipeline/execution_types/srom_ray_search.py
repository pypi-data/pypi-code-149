# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import logging
import numpy as np
import pandas as pd
import ray
from sklearn.base import clone
from sklearn.model_selection import ParameterSampler
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.utils.pipeline_utils import gen_pipeline_and_grid, ModelOutput
from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException
from sklearn.model_selection import ParameterGrid
import time
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.utils.pipeline_utils import verbosity_to_verbose_mapping

LOGGER = logging.getLogger(__name__)


@ray.remote
def cv_learning(
    parameters, pipeline_index, X, y, cv, groups, pipelines, cross_val_score, scorer, verbose,
):
    """
    Performs cross validation.

    Parameters:
        tup (tuple): Tuple containing parameters and pipeline_index.

    output:
        Shared resource for multiprocessing.
    """
    start_time = time.time()
    local_logger = logging.getLogger("cv_learning")
    local_pipeline = clone(pipelines[pipeline_index])
    try:
        local_pipeline.set_params(**parameters)
        if cross_val_score:
            scores = cross_val_score(
                local_pipeline,
                X,
                y,
                groups=groups,
                cv=cv,
                scoring=scorer,
                return_train_score=False,
                verbose=verbose,
            )
        else:
            from sklearn.model_selection import cross_validate

            scores = cross_validate(
                local_pipeline,
                X,
                y,
                groups=groups,
                cv=cv,
                scoring=scorer,
                return_train_score=False,
                verbose=verbose,
            )
        ret_result = (
            pipeline_index,
            (
                parameters,
                np.mean(scores["test_score"]),
                np.std(scores["test_score"]),
                (time.time() - start_time) / 60.0,
            ),
        )
    except Exception as ex:
        local_logger.error(str(ex))
        ret_result = (
            pipeline_index,
            (parameters, np.NaN, np.NaN, (time.time() - start_time) / 60.0),
        )
    return ret_result


@ray.remote
def train_test_score(parameters, pipeline_index, X, y, pipelines, scorer, verbose):
    """
    Performs cross validation.

    Parameters:
        tup (tuple): Tuple containing parameters and pipeline_index.

    output:
        Shared resource for multiprocessing.
    """
    start_time = time.time()
    local_logger = logging.getLogger("train_test_learning")
    local_pipeline = clone(pipelines[pipeline_index])

    try:
        local_pipeline.set_params(**parameters)
        from sklearn.model_selection import train_test_split

        stratify = None
        try:
            from sklearn.base import is_classifier

            if is_classifier(local_pipeline):
                stratify = y
        except:
            pass

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, random_state=33, test_size=0.1, stratify=stratify
        )
        local_pipeline.fit(X_train, y_train)
        from sklearn.metrics import get_scorer

        scores = get_scorer(scorer)(local_pipeline, X_test, y_test)
        ret_result = (
            pipeline_index,
            (parameters, scores, np.NaN, (time.time() - start_time) / 60.0),
        )
    except Exception as ex:
        local_logger.error(str(ex))
        ret_result = (
            pipeline_index,
            (parameters, np.NaN, np.NaN, (time.time() - start_time) / 60.0),
        )
    return ret_result

def srom_ray_search_async(
    X,
    y,
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
    srom_ray_search(
        X,
        y,
        param_grid,
        paths,
        cv,
        scorer,
        max_eval_time_minute,
        num_option_per_pipeline,
        mode,
        groups,
        random_state,
        total_execution_time,
        cross_val_score,
        pipeline_type,
        pipeline_init_param,
        evn_config,
        verbosity,
        result_queue,
    )
    return

def srom_ray_search(
    X,
    y,
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
    """
    Parameters:
        X (pandas dataframe or numpy array): The dataset to be used for model selection. \
            shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        y (pandas dataframe or numpy array): Target vector to be used. This is optional, \
            if target_column is added in the meta data, it is used from there. \
            shape = [n_samples] or [n_samples, n_output].
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
    # Validations
    if mode not in ["exhaustive", "random"]:
        raise IncorrectValueException(
            "Supported mode should be provided: 'exhaustive' or 'random'"
        )

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

    CONFIG = evn_config["CONFIG"]

    # setting the verbose parameter to be passed to the GridSearchCV
    verbose = verbosity_to_verbose_mapping(verbosity)

    if not ray.is_initialized():
        if len(CONFIG) > 0:
            ray.init(**CONFIG)
        else:
            ray.init()

    # following three are return values
    # best_estimators is a list of all pipeline, and for each pipeline what is the best score
    number_of_combinations = 0
    best_estimators = []
    best_scores = []
    best_scores_std = []
    execution_times = []

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

    # Ray related work now
    # put the data in local object store now
    X_bc = ray.put(X)
    y_bc = ray.put(y)
    groups_bc = ray.put(groups)
    pipelines_bc = ray.put(pipelines)
    cross_val_score_bc = ray.put(cross_val_score)
    scorer_bc = ray.put(scorer)
    cv_bc = ray.put(cv)
    verbose_bc = ray.put(verbose)

    rayTask = []
    if cv == 1:
        rayTask = [
            train_test_score.remote(
                param, pipe_index, X_bc, y_bc, pipelines_bc, scorer_bc, verbose_bc,
            )
            for param, pipe_index in pipeline_param_grid
        ]
    else:
        rayTask = [
            cv_learning.remote(
                param,
                pipe_index,
                X_bc,
                y_bc,
                cv_bc,
                groups_bc,
                pipelines_bc,
                cross_val_score_bc,
                scorer_bc,
                verbose_bc,
            )
            for param, pipe_index in pipeline_param_grid
        ]

    ranTaskResult, notcompletedTasks = ray.wait(
        rayTask, num_returns=len(rayTask), timeout=total_execution_time * 60.0
    )
    for slowTask in notcompletedTasks:
        ray.cancel(slowTask, force=True)

    ranTaskResult = ray.get(ranTaskResult)
    from collections import OrderedDict

    def reduce_by_key(ls):
        d = OrderedDict()
        for item in ls:
            d.setdefault(item[0], []).extend([item[1]])
        return d

    ordered_ans = reduce_by_key(ranTaskResult)

    for pipeline_index in range(len(pipelines)):
        local_pipeline = pipelines[pipeline_index]
        if pipeline_index not in ordered_ans.keys():
            best_estimators.append(local_pipeline)
            best_scores.append(np.NaN)
            best_scores_std.append(np.NaN)
            execution_times.append(np.NaN)
        else:
            results = ordered_ans[pipeline_index]
            reduce_results = [item for item in results if item[1] is not np.NaN]
            if len(reduce_results) > 0:
                reduce_results.sort(key=lambda x: x[1])
                parameters, score, score_std, execution_t = reduce_results[-1]
            else:
                parameters, score, score_std, execution_t = {}, np.NaN, np.NaN, np.NaN
            local_pipeline.set_params(**parameters)
            best_estimators.append(local_pipeline)
            best_scores.append(score)
            best_scores_std.append(score_std)
            execution_times.append(execution_t)
        if result_queue is not None:
            result_queue.put([best_estimators,
                              best_scores,
                              number_of_combinations,
                              best_scores_std,
                              execution_times,
                              []])
    # close the ray
    if ray.is_initialized():
        ray.shutdown()

    return (
        best_estimators,
        best_scores,
        number_of_combinations,
        best_scores_std,
        execution_times,
        [],
    )
