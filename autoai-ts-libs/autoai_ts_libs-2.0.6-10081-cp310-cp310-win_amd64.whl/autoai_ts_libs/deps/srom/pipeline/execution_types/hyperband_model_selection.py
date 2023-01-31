# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: hyperband_model_selection
   :synopsis: This module use hyper-band search.

.. moduleauthor:: SROM Team
"""
import logging
from math import log, ceil
import numpy as np
from sklearn.model_selection import GridSearchCV, ParameterGrid
from sklearn.pipeline import Pipeline
from sklearn.base import clone
from autoai_ts_libs.deps.srom.utils.pipeline_utils import generate_param_grid
from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException
from sklearn.model_selection import ParameterSampler
from autoai_ts_libs.deps.srom.utils.pipeline_utils import verbosity_to_verbose_mapping

LOGGER = logging.getLogger(__name__)
HyperbandGrid = {
    "GradientBoostingRegressor": "n_estimators:5",
    "DecisionTreeClassifier": "max_depth:3",
    "SGDRegressor": "n_iter:1",
    "XGBRegressor": "n_estimators:5",
    "ExtraTreesRegressor": "n_estimators:5",
    "RandomForestRegressor": "n_estimators:5",
    "KNeighborsRegressor": "n_neighbors:3",
    "MLPRegressor": "max_iter:5",
    "ARDRegression": "n_iter:5",
    "AdaboostRegression": "n_estimators:5",
    "GradientBoostingClassifier": "n_estimators:5",
    "SGDClassifier": "n_iter:1",
    "XGBClassifier": "n_estimators:5",
    "ExtraTreesClassifier": "n_estimators:5",
    "RandomForestClassifier": "n_estimators:5",
    "KNeighborsClassifier": "n_neighbors:3",
    "MLPClassifier": "max_iter:5",
    "ARDClassifier": "n_iter:5",
    "AdaBoostClassifier": "n_estimators:5",
    "BaggingClassifier": "n_estimators:5",
}


def hyperband_search_async(
    X,
    y,
    param_grid,
    paths,
    cv,
    scorer,
    n_jobs,
    pre_dispatch,
    num_option_per_pipeline=10,
    random_state=None,
    verbosity='low',
    result_queue=None
):
    hyperband_search(
        X,
        y,
        param_grid,
        paths,
        cv,
        scorer,
        n_jobs,
        pre_dispatch,
        num_option_per_pipeline,
        random_state,
        verbosity,
        result_queue
    )
    return


def hyperband_search(
    X,
    y,
    param_grid,
    paths,
    cv,
    scorer,
    n_jobs,
    pre_dispatch,
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
            shape = [n_samples] or [n_samples, n_output]
        param_grid (dict): Dictionary with parameter names(string) as keys and lists of parameter \
            settings to try as values, or a list of such dictionaries, in which case the grids \
            spanned by each dictionary in the list are explored.
        paths (list): Consists of estimator paths.
        cv (integer, cross-validation generator or an iterable): Determines the cross-validation \
            splitting strategy.
        scorer (string, callable, list/tuple, dict or None): A single string or a callable to \
            evaluate the predictions on the test set.
        n_jobs (integer): Number of parallel jobs.
        pre_dispatch (integer, or string): Controls the number of jobs that get dispatched during \
            parallel execution.Reducing this number can be useful to avoid an explosion of memory \
            consumption when more jobs get dispatched than CPUs can process.
        num_option_per_pipeline (integer): Default: 10. Number of parameter settings that are sampled.\
            This parameter is applicable if mode is 'random'

    Returns: (tuple)
        best_estimators: (list)
        best_scores: (list)
        number_of_combinations: (integer)
        best_scores_std: (list)

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

        # strp 3 - identify the parameter that will be removed from search space
        removed_params = []
        removed_params_default_value = []
        for step in pipeline_path_obj.steps:
            tmp_class_name = step[1].__class__.__name__
            if tmp_class_name in HyperbandGrid.keys():
                tmp_param_name = step[0]
                tmp_class_name_value = HyperbandGrid[tmp_class_name].split(":")[0]
                removed_params.append(tmp_param_name + "__" + tmp_class_name_value)
                tmp_param_grid.pop(tmp_param_name + "__" + tmp_class_name_value, None)
                removed_params_default_value.append(
                    HyperbandGrid[tmp_class_name].split(":")[1]
                )

        def num(s):
            try:
                return int(s)
            except ValueError:
                return float(s)

        try:
            if len(removed_params) == 0:
                best_estimators.append(pipeline_path_obj)
                best_scores.append(np.NaN)
                best_scores_std.append(np.NaN)
            else:
                # start hyperband, if removed_params are many, we just select the first one
                experimental_param = removed_params[0]
                experimental_param_default_value = num(removed_params_default_value[0])

                max_iter = num_option_per_pipeline
                eta = 3
                logeta = lambda x: log(x) / log(eta)
                s_max = int(logeta(max_iter))
                B = (s_max + 1) * max_iter
                skip_last = 0

                tested_params = []
                tested_values = []
                tested_values_std = []

                for s in reversed(range(s_max + 1)):
                    n = int(ceil(B / max_iter / (s + 1) * eta ** s))
                    r = max_iter * eta ** (-s)
                    grid_combo_len = len(ParameterGrid(tmp_param_grid))
                    T = list(
                        ParameterSampler(
                            tmp_param_grid,
                            n_iter=np.min([n, grid_combo_len]),
                            random_state=random_state,
                        )
                    )
                    for i in range((s + 1) - int(skip_last)):
                        n_configs = n * eta ** (-i)
                        n_iterations = r * eta ** (i)
                        val_losses = []
                        val_losses_std = []
                        for exp_param in T:
                            tmp_exp_param = exp_param
                            tmp_exp_param[experimental_param] = (
                                int(n_iterations) * experimental_param_default_value
                            )
                            pipeline_path_obj.set_params(**tmp_exp_param)
                            evaluator = GridSearchCV(
                                estimator=pipeline_path_obj,
                                param_grid={},
                                cv=cv,
                                n_jobs=n_jobs,
                                pre_dispatch=pre_dispatch,
                                scoring=scorer,
                                error_score=np.NaN,
                                verbose=verbose,
                            )
                            evaluator.fit(X, y)
                            number_of_combinations = number_of_combinations + len(
                                evaluator.cv_results_["params"]
                            )
                            val_losses.append(evaluator.best_score_)
                            val_losses_std.append(
                                evaluator.cv_results_["std_test_score"][
                                    evaluator.best_index_
                                ]
                            )
                        tested_params.extend(T)
                        tested_values.extend(val_losses)
                        tested_values_std.extend(val_losses_std)
                        indices = np.argsort(val_losses)[::-1]
                        T = [T[i] for i in indices]
                        T = T[0 : int(n_configs / eta)]
                best_index = np.where(tested_values == np.max(tested_values))[0][0]
                local_pipeline = clone(pipeline_path_obj)
                local_pipeline.set_params(**tested_params[best_index])
                best_estimators.append(local_pipeline)
                best_scores.append(tested_values[best_index])
                best_scores_std.append(tested_values_std[best_index])
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
