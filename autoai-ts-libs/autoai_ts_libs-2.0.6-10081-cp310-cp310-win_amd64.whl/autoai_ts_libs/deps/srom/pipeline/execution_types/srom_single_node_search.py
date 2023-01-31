# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: srom_single_node_search
   :synopsis: This module is used for single node based exhaustive/random search. \
        Here, pipeline is executed with all/some parameters given in param grid \
        for each estimator on single node depending on mode. \
        It returns the best scores, best estimators and number of combinations.

.. moduleauthor:: SROM Team
"""
import logging
import queue
import time
import multiprocessing
import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, ParameterGrid
from sklearn.base import clone
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.utils.pipeline_utils import gen_pipeline_and_grid
from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException
from sklearn.pipeline import Pipeline
from sklearn.utils import parallel_backend
from autoai_ts_libs.deps.srom.utils.pipeline_utils import verbosity_to_verbose_mapping
import warnings
from sklearn.exceptions import FitFailedWarning

LOGGER = logging.getLogger(__name__)


def timebound_fit(output, X, y, groups, evaluator, parallel_backend_value, path_n_jobs):
    ret_result = (0, np.NaN, np.NaN, np.NaN)
    try:
        if parallel_backend_value:
            with parallel_backend(parallel_backend_value, n_jobs=path_n_jobs):
                evaluator.fit(X, y, groups=groups)
        else:
            evaluator.fit(X, y, groups=groups)

        ret_result = (
            len(evaluator.cv_results_["params"]),
            evaluator.best_params_,
            evaluator.best_score_,
            evaluator.cv_results_["std_test_score"][evaluator.best_index_],
        )
    except Exception as ex:
        LOGGER.error("SearchCV failed: %s", evaluator)
        LOGGER.exception(str(ex))
        pass
    output.put(ret_result)
    return


def srom_single_node_search_async(
    X,
    y,
    param_grid,
    num_option_per_pipeline,
    n_jobs,
    pre_dispatch,
    paths,
    cv,
    scorer,
    mode,
    groups,
    max_eval_time_minute,
    random_state,
    total_execution_time,
    pipeline_type,
    pipeline_init_param,
    verbosity,
    evn_config,
    result_out,
):
    """ """

    srom_single_node_search(
        X,
        y,
        param_grid,
        paths,
        cv,
        scorer,
        n_jobs,
        pre_dispatch,
        max_eval_time_minute,
        num_option_per_pipeline,
        mode,
        groups,
        random_state,
        total_execution_time,
        pipeline_type,
        pipeline_init_param,
        evn_config,
        verbosity,
        result_out,
    )
    return


def srom_single_node_search(
    X,
    y,
    param_grid,
    paths,
    cv,
    scorer,
    n_jobs,
    pre_dispatch,
    max_eval_time_minute,
    num_option_per_pipeline=10,
    mode="exhaustive",
    groups=None,
    random_state=None,
    total_execution_time=10,
    pipeline_type=Pipeline,
    pipeline_init_param={},
    evn_config=None,
    verbosity="low",
    result_out=None,
):
    """
    Parameters:
        X (pandas dataframe or numpy array): The dataset to be used for model selection. \
            shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        y (pandas dataframe or numpy array): Target vector to be used. This is optional, \
            if target_column is added in the meta data, it is used from there. \
            shape = [n_samples] or [n_samples, n_output]
        param_grid (dict): Dictionary with parameter names(string) as keys and lists of parameter \
            settings to try as values, or a list of such dictionaries, in which case the grids \
            spanned by each dictionary in the list are explored.
        paths (list): Consists of estimator paths.
        cv (integer, cross-validation generator or an iterable): Determines the cross-validation \
            splitting strategy.
        scorer (string, callable, list/tuple, dict or None): A single string or a callable to evaluate \
            the predictions on the test set.
        n_jobs (integer): Number of parallel jobs.
        max_eval_time_minute (integer) (minutes): Maximum timeout for execution of pipelines with unique \
            parameter grid combination.
        pre_dispatch (integer, or string): Controls the number of jobs that get dispatched during parallel \
            execution. Reducing this number can be useful to avoid an explosion of memory consumption when \
            more jobs get dispatched than CPUs can process.
        num_option_per_pipeline (integer): Default: 10. Number of parameter settings that are sampled. \
            This parameter is applicable if mode is 'random'.
        mode (String): Default: "exhaustive". Possible values: "random" or "exhaustive".

    Returns: (tuple)
        best_estimators: (list)
        best_scores: (list)
        number_of_combinations: (integer)
        best_scores_std: (list)

    Raises:
        IncorrectValueException:
            1. If mode not in ['exhaustive', 'random'].
            2. If paths is none or empty.
            3. If n_jobs is none or is not instance of integer.
            4. If pre_dispatch is none or is not instance of integer or string.
            5. If num_option_per_pipeline is none or is not instance of integer \
               or num_option_per_pipeline is less than 1.
        MemoryError:
            If operation is out of memory.
    """

    parallel_backend_value = None
    if evn_config and len(evn_config.keys()) > 0:
        if "parallel_backend" in evn_config.keys():
            parallel_backend_value = evn_config["parallel_backend"]
        # else:
        #     raise IncorrectValueException(
        #         "please provide parallel_backend in evn_config."
        #     )

    # Validations
    if mode not in ["exhaustive", "random"]:
        raise IncorrectValueException(
            "Supported mode should be provided: 'exhaustive' or 'random'"
        )
    if cv == 1:
        raise IncorrectValueException("cv = 1 is not supported")
    if not paths:
        raise IncorrectValueException("Paths should be not be None or empty.")
    if not n_jobs or not isinstance(n_jobs, int):
        raise IncorrectValueException("Value of n_jobs should be int.")
    if not pre_dispatch or not isinstance(pre_dispatch, (int, str)):
        raise IncorrectValueException(
            "Value of pre_dispatch should be either int or string."
        )
    if (
        not num_option_per_pipeline
        or not isinstance(num_option_per_pipeline, int)
        or num_option_per_pipeline < 1
    ):
        raise IncorrectValueException(
            "Value of num_option_per_pipeline should be int and greater than 1."
        )
    if not param_grid:
        LOGGER.debug("Setting empty parameter grid")
        param_grid = SROMParamGrid(gridtype="empty")

    # setting the verbose parameter to be passed to the GridSearchCV
    verbose = verbosity_to_verbose_mapping(verbosity)

    # Initialize return values
    number_of_combinations = 0
    best_estimators = []
    best_scores = []
    best_scores_std = []

    pipeline_paths, param_grids = gen_pipeline_and_grid(
        paths, param_grid, pipeline_type, pipeline_init_param
    )

    experiment_start_time = time.time()

    # limit n_jobs to <= # of CPUs, don't allow unconstrained (-1)
    if n_jobs < 1:
        n_jobs = multiprocessing.cpu_count()
    else:
        n_jobs = min(n_jobs, multiprocessing.cpu_count())

    for index, _ in enumerate(pipeline_paths):
        pipeline_path_obj = pipeline_paths[index]
        tmp_param_grid = param_grids[index]

        try:
            grid_combo_len = len(list(ParameterGrid(tmp_param_grid)))
            # for now, use global n_jobs, later we will look into per path n_jobs setting
            path_n_jobs = n_jobs
            LOGGER.debug(
                "Reset n_jobs for pipeline path to more sane value of %i", path_n_jobs
            )
            LOGGER.debug("The pipeline is : %s", str(pipeline_path_obj))

            is_total_space_smaller = (
                mode == "random" and grid_combo_len < num_option_per_pipeline
            )
            if mode == "exhaustive" or is_total_space_smaller:
                # exhaustive/complete search
                if is_total_space_smaller:
                    LOGGER.debug(
                        """The total space of parameters is smaller than provided
                    num_option_per_pipeline. Running exhaustive search."""
                    )
                evaluator = GridSearchCV(
                    estimator=pipeline_path_obj,
                    param_grid=tmp_param_grid,
                    cv=cv,
                    n_jobs=path_n_jobs,
                    pre_dispatch=pre_dispatch,
                    scoring=scorer,
                    error_score=np.NaN,
                    refit=False,
                    verbose=verbose,
                )
            else:
                # random search
                evaluator = RandomizedSearchCV(
                    estimator=pipeline_path_obj,
                    param_distributions=tmp_param_grid,
                    cv=cv,
                    n_jobs=path_n_jobs,
                    pre_dispatch=pre_dispatch,
                    scoring=scorer,
                    error_score=np.NaN,
                    n_iter=num_option_per_pipeline,
                    random_state=random_state,
                    refit=False,
                    verbose=verbose,
                )

            time_bound = True
            # if user like to make sure all the parameter get evaluated
            if max_eval_time_minute == -1:
                time_bound = False

            ret_result = (0, np.NaN, np.NaN, np.NaN)

            if time_bound:
                import multiprocessing as mp

                output = mp.Queue()

                # task_timeout in seconds
                task_timeout = max_eval_time_minute * 60.0
                task = mp.Process(
                    target=timebound_fit,
                    args=(
                        output,
                        X,
                        y,
                        groups,
                        evaluator,
                        parallel_backend_value,
                        path_n_jobs,
                    ),
                )
                task.start()
                try:
                    ret_result = output.get(True, task_timeout)
                except queue.Empty:
                    LOGGER.error(
                        "Pipeline Execution is not completed: %s", pipeline_path_obj
                    )
                    # if process is still running, we initiate its cleaning
                    if task.is_alive():
                        task.terminate()
                        time.sleep(1)
                        task.join()
                        time.sleep(1)
                except Exception as ex:
                    LOGGER.error("Pipeline failed: %s", pipeline_path_obj)
                    LOGGER.error("Pipeline failed reason: %s", str(ex))
                    LOGGER.exception(str(ex))
                    pass
            else:
                try:
                    if parallel_backend_value:
                        with parallel_backend(
                            parallel_backend_value, n_jobs=path_n_jobs
                        ):
                            with warnings.catch_warnings(record=True) as w:
                                warnings.filterwarnings(
                                    "always", ".*", FitFailedWarning
                                )
                                evaluator.fit(X, y, groups=groups)
                                if w:
                                    for item in w:
                                        print(item.message)
                    else:
                        with warnings.catch_warnings(record=True) as w:

                            warnings.filterwarnings("always", ".*", FitFailedWarning)
                            evaluator.fit(X, y, groups=groups)
                            if w:
                                for item in w:
                                    print(item.message)

                    ret_result = (
                        len(evaluator.cv_results_["params"]),
                        evaluator.best_params_,
                        evaluator.best_score_,
                        evaluator.cv_results_["std_test_score"][evaluator.best_index_],
                    )
                except Exception as ex:
                    LOGGER.error("SearchCV failed: %s", evaluator)
                    LOGGER.exception(str(ex))

            number_of_combinations = number_of_combinations + ret_result[0]
            local_pipeline = clone(pipeline_path_obj)
            if ret_result[0] > 0:
                local_pipeline.set_params(**ret_result[1])
            best_estimators.append(local_pipeline)
            best_scores.append(ret_result[2])
            best_scores_std.append(ret_result[3])
        except MemoryError as memory_error:
            # Handling Memory error
            # As memory is insufficient we cannot continue with execution of next pipeline.
            # Hence, raising exception.
            LOGGER.error(
                "Operation out of memory. Please try to configure according to the system's memory."
            )
            LOGGER.error("Pipeline failed: %s", pipeline_path_obj)
            LOGGER.exception(memory_error)
            raise memory_error
        except Exception as ex:
            # Handling Generic exceptions.
            # Continuing with next pipeline execution hence not raising exception.
            best_estimators.append(pipeline_path_obj)
            best_scores.append(np.NaN)
            best_scores_std.append(np.NaN)
            LOGGER.error("Pipeline failed: %s", pipeline_path_obj)
            LOGGER.exception(str(ex))

        end_time = time.time()
        elapsed_time = (end_time - experiment_start_time) / 60.0
        if result_out is not None:
            result_out.put(
                [best_estimators, best_scores, number_of_combinations, best_scores_std]
            )

        # we gracefully exit the loop, as crossed the allocated time
        if (
            total_execution_time != -1
            and elapsed_time > total_execution_time
            and (index + 1) < len(pipeline_paths)
        ):
            # prepare for exit
            # pipeline must return all the needed info
            for index_ in range(index + 1, len(pipeline_paths)):
                best_estimators.append(pipeline_paths[index_])
                best_scores.append(np.NaN)
                best_scores_std.append(np.NaN)
            break

    return best_estimators, best_scores, number_of_combinations, best_scores_std
