# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: rbfopt_model_selection
   :synopsis: This module is used for using RBFOpt.

.. moduleauthor:: SROM Team
"""
import io
import os
import logging
import tempfile
import zipfile
import multiprocessing
import requests
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.base import clone
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.utils.pipeline_utils import generate_param_grid
from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException
import rbfopt
from autoai_ts_libs.deps.srom.utils.pipeline_utils import verbosity_to_verbose_mapping

LOGGER = logging.getLogger(__name__)


def rbfopt_search_async(
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
    rbfopt_search(
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


def rbfopt_search(
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
            shape = [n_samples] or [n_samples, n_output].
        param_grid (dict): Dictionary with parameter names(string) as keys and lists of \
            parameter settings to try as values, or a list of such dictionaries, in which \
            case the grids spanned by each dictionary in the list are explored.
        paths (list): Consists of estimator paths.
        cv (integer, cross-validation generator or an iterable): Determines the cross-validation \
            splitting strategy.
        scorer (string, callable, list/tuple, dict or None): A single string or a callable to \
            evaluate the predictions on the test set.
        n_jobs (integer): Number of parallel jobs.
        pre_dispatch (integer, or string): Controls the number of jobs that get dispatched during \
            parallel execution. Reducing this number can be useful to avoid an explosion of memory \
            consumption when more jobs get dispatched than CPUs can process.
        num_option_per_pipeline (integer): Default: 10. Number of parameter settings that are sampled. \
            This parameter is applicable if mode is 'random'.

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
    if not param_grid:
        param_grid = SROMParamGrid(gridtype="empty")

    opt_dir = _get_problem_solver()

    number_of_combinations = 0
    best_estimators = []
    best_scores = []
    best_scores_std = []

    # setting the verbose parameter to be passed to the GridSearchCV
    verbose = verbosity_to_verbose_mapping(verbosity)

    # for each path in self.paths, create a pipeline.
    for path in paths:

        # step 1. pipeline creation
        # we'll always have named estimators that are unique now
        pipeline_path_obj = Pipeline(path)

        # step 2. Get the parameters from param_grid - know what parameter to search
        tmp_param_grid = generate_param_grid(
            pipeline=pipeline_path_obj, param_grid=param_grid
        )

        lower_bounds = []
        upper_bounds = []
        keyName = []
        typeParam = []

        # added this special handling - that create a appropriate param for MLP
        if "MLPRegressor" in str(pipeline_path_obj):
            num_hidden_layers = param_grid.get_param(
                "mlpregressor__number_of_hidden_layers"
            )[1]
            num_neurons = param_grid.get_param(
                "mlpregressor__number_of_neurons_in_hidden_layers"
            )
            for i_num_hidden_layers in range(num_hidden_layers):
                lower_bounds.append(num_neurons[0])
                upper_bounds.append(num_neurons[1])
                typeParam.append("I")
                keyName.append("Extra@_layer_" + str(i_num_hidden_layers))

        # added this special handling - that create an appropriate param for MLP
        if "MLPClassifier" in str(pipeline_path_obj):
            num_hidden_layers = param_grid.get_param(
                "mlpclassifier__number_of_hidden_layers"
            )[1]
            num_neurons = param_grid.get_param(
                "mlpclassifier__number_of_neurons_in_hidden_layers"
            )
            for i_num_hidden_layers in range(num_hidden_layers):
                lower_bounds.append(num_neurons[0])
                upper_bounds.append(num_neurons[1])
                typeParam.append("I")
                keyName.append("Extra@_layer_" + str(i_num_hidden_layers))

        # other normal handling
        for item in tmp_param_grid.keys():
            val = tmp_param_grid[item]
            lower_bounds.append(val[0])
            upper_bounds.append(val[1])
            typeParam.append(val[2])
            keyName.append(item)

        try:
            # Compute n_jobs using total combination of grid parameters and CPU count.
            n_jobs = min(multiprocessing.cpu_count(), n_jobs)
            LOGGER.debug("Reset n_jobs to more sane value of %i", n_jobs)

            def obj_funct(x):
                x = x.reshape(1, len(x))
                temp = pipeline_path_obj.get_params()
                for i in range(len(keyName)):
                    if keyName[i] in temp.keys():
                        if typeParam[i] == "I":
                            temp[keyName[i]] = int(x[:, i])
                        else:
                            temp[keyName[i]] = float(x[:, i])

                # if it is MLP classifier, then we need to process little extra
                if "MLPRegressor" in str(pipeline_path_obj):
                    exp_hidden_layer_sizes = ()
                    for num_i in range(len(keyName)):
                        if "Extra@_layer_" in keyName[i]:
                            if int(x[:, num_i]) > 0:
                                exp_hidden_layer_sizes += (int(x[:, num_i]),)
                            else:
                                break
                    temp["mlpregressor__hidden_layer_sizes"] = exp_hidden_layer_sizes

                if "MLPClassifier" in str(pipeline_path_obj):
                    exp_hidden_layer_sizes = ()
                    for num_i in range(len(keyName)):
                        if "Extra@_layer_" in keyName[i]:
                            if int(x[:, num_i]) > 0:
                                exp_hidden_layer_sizes += (int(x[:, num_i]),)
                            else:
                                break
                    temp["mlpclassifier__hidden_layer_sizes"] = exp_hidden_layer_sizes

                try:
                    pipeline_path_obj.set_params(**temp)
                    model = GridSearchCV(
                        estimator=pipeline_path_obj,
                        param_grid={},
                        cv=cv,
                        n_jobs=n_jobs,
                        pre_dispatch=pre_dispatch,
                        scoring=scorer,
                        error_score=np.NaN,
                    )
                    model.fit(X, y)
                    return -1 * model.best_score_
                except:
                    return 10000000

            lower_bounds = np.array(lower_bounds)
            upper_bounds = np.array(upper_bounds)
            typeParam = np.array(typeParam)
            bb = rbfopt.RbfoptUserBlackBox(
                len(keyName), lower_bounds, upper_bounds, typeParam, obj_funct
            )
            settings = rbfopt.RbfoptSettings(
                minlp_solver_path=opt_dir + "/bonmin",
                nlp_solver_path=opt_dir + "/ipopt",
                max_iterations=num_option_per_pipeline,
                rand_seed=random_state,
            )
            alg = rbfopt.RbfoptAlgorithm(settings, bb)
            try:
                val, x, itercount, _, _ = alg.optimize()
                x = x.reshape(1, len(x))
                temp = pipeline_path_obj.get_params()
                number_of_combinations = number_of_combinations + itercount

                for i in range(len(keyName)):
                    if keyName[i] in temp.keys():
                        if typeParam[i] == "I":
                            temp[keyName[i]] = int(x[:, i])
                        else:
                            temp[keyName[i]] = float(x[:, i])

                # if it is MLP classifier, then we need to process little extra
                if "MLPRegressor" in str(pipeline_path_obj):
                    exp_hidden_layer_sizes = ()
                    for num_i in range(len(keyName)):
                        if "Extra@_layer_" in keyName[i]:
                            if int(x[:, num_i]) > 0:
                                exp_hidden_layer_sizes += (int(x[:, num_i]),)
                            else:
                                break
                    temp["mlpregressor__hidden_layer_sizes"] = exp_hidden_layer_sizes

                if "MLPClassifier" in str(pipeline_path_obj):
                    exp_hidden_layer_sizes = ()
                    for num_i in range(len(keyName)):
                        if "Extra@_layer_" in keyName[i]:
                            if int(x[:, num_i]) > 0:
                                exp_hidden_layer_sizes += (int(x[:, num_i]),)
                            else:
                                break
                    temp["mlpclassifier__hidden_layer_sizes"] = exp_hidden_layer_sizes

                pipeline_path_obj.set_params(**temp)

                local_pipeline = clone(pipeline_path_obj)
                local_pipeline.set_params(**temp)
                best_estimators.append(local_pipeline)
                best_scores.append(-1 * val)
                best_scores_std.append(np.NaN)
            except Exception as e1:
                # print ('Error - ', str(e1))
                best_estimators.append(pipeline_path_obj)
                best_scores.append(np.NaN)
                best_scores_std.append(np.NaN)
                LOGGER.error(str(e1))
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
            _clean_problem_solver(opt_dir)
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
    _clean_problem_solver(opt_dir)
    return best_estimators, best_scores, number_of_combinations, best_scores_std


def _get_problem_solver():
    temp_dir = tempfile.mkdtemp()
    bonmin_url = "https://ampl.com/dl/open/bonmin/bonmin-linux64.zip"
    res = requests.get(bonmin_url)
    if res.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(res.content))
        z.extractall(temp_dir)
        os.chmod(temp_dir + "/bonmin", 0o777)
    else:
        raise RuntimeError("Unable to fetch bonmin for optimization")

    ipopt_url = "https://ampl.com/dl/open/ipopt/ipopt-linux64.zip"
    res = requests.get(ipopt_url)
    if res.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(res.content))
        z.extractall(temp_dir)
        os.chmod(temp_dir + "/ipopt", 0o777)
    else:
        raise RuntimeError("Unable to fetch bonmin for optimization")

    return temp_dir


def _clean_problem_solver(temp_dir):
    import shutil
    import errno

    try:
        shutil.rmtree(temp_dir)
    except OSError as exc:
        if exc.errno != errno.ENOENT:
            raise
