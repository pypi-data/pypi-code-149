# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: evolutionary_model_selection
   :synopsis: This module use evolutionary grid search.

.. moduleauthor:: SROM Team
"""
import logging
import multiprocessing
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.base import clone
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.utils.pipeline_utils import generate_param_grid
from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException
from autoai_ts_libs.deps.srom.utils.pipeline_utils import _check_param_grid
#temporary fix
import sklearn.model_selection._search
sklearn.model_selection._search._check_param_grid = _check_param_grid
from evolutionary_search import EvolutionaryAlgorithmSearchCV
import random
from autoai_ts_libs.deps.srom.utils.pipeline_utils import verbosity_to_verbose_mapping

LOGGER = logging.getLogger(__name__)


def evolutionary_search_async(
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
    random_state=None,
    verbosity='low',
    result_queue=None
):
    evolutionary_search(
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
        random_state=None,
        verbosity='low',
        result_queue=result_queue
    )
    return


def evolutionary_search(
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
    random_state=None,
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
        param_grid (dict): Dictionary with parameter names(string) as keys and lists of \
            parameter settings to try as values, or a list of such dictionaries, in which \
            case the grids spanned by each dictionary in the list are explored.
        paths (list): Consists of estimator paths.
        cv (integer, cross-validation generator or an iterable): Determines the cross-validation \
            splitting strategy.
        scorer (string, callable, list/tuple, dict or None): A single string or a callable to \
            evaluate the predictions on the test set.
        n_jobs(integer): Number of parallel jobs.
        pre_dispatch (integer, or string):  Controls the number of jobs that get dispatched during \
            parallel execution. Reducing this number can be useful to avoid an explosion of memory \
            consumption when more jobs get dispatched than CPUs can process.
        num_option_per_pipeline (integer): Default: 10. Number of parameter settings that are sampled. \
            This parameter is applicable if mode is 'random'

    Returns: (tuple)
        best_estimators: (list)
        best_scores: (list)
        number_of_combinations: (integer)
        best_scores_std : (list)

    Raises:
        IncorrectValueException:
            1. If paths is none or empty.
            2. If n_jobs is none or is not instance of integer.
            3. If pre_dispatch is none or is not instance of integer or string.
            4. If num_option_per_pipeline is none or is not instance of integer \
               or num_option_per_pipeline is less than 1.
        MemoryError:
            If operation is out of memory.
    """
    # Validations
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
        param_grid = SROMParamGrid(gridtype="empty")

    # setting the verbose parameter to be passed to the GridSearchCV
    verbose = verbosity_to_verbose_mapping(verbosity)

    # Initialize return values
    number_of_combinations = 0
    best_estimators = []
    best_scores = []
    best_scores_std = []

    # for each path in self.paths, create a pipeline.
    for path in paths:

        # step 1. pipeline creation
        # we'll always have named estimators that are unique now
        pipeline_path_obj = Pipeline(path)

        # step 2. Get the parameters from param_grid - know what parameter to search
        tmp_param_grid = generate_param_grid(
            pipeline=pipeline_path_obj, param_grid=param_grid
        )

        try:
            # Compute n_jobs using total combination of grid parameters and CPU count.
            n_jobs = min(multiprocessing.cpu_count(), n_jobs)
            LOGGER.debug("Reset n_jobs to more sane value of %i", n_jobs)

            if random_state:
                random.seed(random_state)

            evaluator = EvolutionaryAlgorithmSearchCV(
                estimator=pipeline_path_obj,
                params=tmp_param_grid,
                cv=cv,
                n_jobs=n_jobs,
                scoring=scorer,
                error_score=-10000000,
                population_size=50,
                gene_mutation_prob=0.10,
                tournament_size=3,
                generations_number=10,
                verbose=verbose,
            )

            def timebound_fit(output):
                ret_result = (0, np.NaN, np.NaN, np.NaN)
                try:
                    evaluator.fit(X, y)
                    ret_result = (
                        len(evaluator.cv_results_["params"]),
                        evaluator.best_params_,
                        evaluator.best_score_,
                        evaluator.cv_results_["std_test_score"][evaluator.best_index_],
                    )
                except Exception:
                    pass
                output.put(ret_result)

            time_bound = True
            ret_result = (0, np.NaN, np.NaN, np.NaN)

            if time_bound:
                import multiprocessing as mp

                output = mp.Queue()
                import time

                # task_timeout in seconds
                task_timeout = max_eval_time_minute * 60.0
                task = mp.Process(target=timebound_fit, args=(output,))
                task.start()
                task.join(task_timeout)

                if task.is_alive():
                    task.terminate()
                    time.sleep(1)
                    task.join()
                    time.sleep(1)
                else:
                    try:
                        ret_result = output.get(False)
                    except Exception:
                        pass
            else:
                evaluator.fit(X, y)
                ret_result = (
                    len(evaluator.cv_results_["params"]),
                    evaluator.best_params_,
                    evaluator.best_score_,
                    evaluator.cv_results_["std_test_score"][evaluator.best_index_],
                )

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
                "Operation out of memory. Please try to configure according \
                                                            to the system's memory."
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
            LOGGER.error(str(ex))
        if result_queue is not None:
            result_queue.put([best_estimators, best_scores, number_of_combinations, best_scores_std])

    return best_estimators, best_scores, number_of_combinations, best_scores_std
