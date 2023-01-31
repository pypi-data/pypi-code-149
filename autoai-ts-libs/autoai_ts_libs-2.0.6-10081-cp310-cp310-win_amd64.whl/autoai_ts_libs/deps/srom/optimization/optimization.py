# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
This module contains the various SROM optimization estimators for use in setpoint optimization
"""

import logging
import sys
import multiprocessing
import pprint
from collections import OrderedDict
from multiprocessing.pool import Pool
from threading import Lock
from functools import partial
import pandas as pd

from scipy.optimize import OptimizeResult

import numpy as np
from scipy.optimize import minimize
from sklearn.base import BaseEstimator
from sklearn.model_selection import ParameterGrid

import autoai_ts_libs.deps.srom as srom.utils.srom_platform as platform
from autoai_ts_libs.deps.srom.optimization.nlopt import NLOptimizer
from autoai_ts_libs.deps.srom.optimization.nlopt import utils as nlopt_utils
from autoai_ts_libs.deps.srom.optimization.nlopt.ml_scipy_utils import unflatten

LOGGER = logging.getLogger(__name__)

# used by brute force optimizers

import traceback

SUPPORTED_METHODS = ["COBYLA", "SLSQP", "TRUST-CONSTR"]


def buildconstraint(acallable, ctype="ineq"):
    """helper to construct contraints in form
    discussed in
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize
    """
    answer = []
    # we use a tuple on input to
    # keep *args
    if isinstance(acallable, tuple):
        # getting args
        thefunction = acallable[0]
        theargs = acallable[1]
        answer.append({"type": ctype, "fun": thefunction, "args": theargs})
    else:
        answer.append({"type": ctype, "fun": acallable})
    return answer


def _oncecollected(results):
    """used only by brute force legacy optimizers"""

    answer = dict(
        objective_value=None,
        data_frame=None,
        parameter_combination=None,
        greater_is_better=None,
    )

    if not results:
        LOGGER.warning("not expecting zero sized result collection!")
        return answer

    LOGGER.debug("in _oncecollected")
    best_objective = None
    for adict in results:
        greater_is_better = adict["greater_is_better"]
        objvalue = adict["objective_value"]
        if best_objective is None:
            answer = adict
            best_objective = answer["objective_value"]
            continue
        if greater_is_better:
            if objvalue > best_objective:
                answer = adict
                best_objective = objvalue
        else:
            if objvalue < best_objective:
                answer = adict
                best_objective = objvalue
    if LOGGER.getEffectiveLevel() == logging.DEBUG:
        LOGGER.debug(
            "_oncecollected returning best_objective\n%s",
            pprint.pformat(answer, indent=4),
        )
    optresult = OptimizeResult()
    optresult.success = True
    answer["optresult"] = optresult
    return answer


def _getobjvalue(
    parameter_combination,
    X,
    estimator_dict,
    objective_function,
    objective_function_params,
):
    # parameter_combination is a dictionary with a specific combination of values
    # for the given parameters,
    # in this case it will be column names and the values for those
    for param_name in list(parameter_combination.keys()):
        # Assign param_value to all rows of column "param_name"
        X[param_name] = parameter_combination[param_name]

    # X is now a dataframe with a specific combination of values for control variables.
    # Use this for prediction followed
    # by optimization
    if estimator_dict is not None and isinstance(estimator_dict, OrderedDict):
        # If the estimator dict is ordered, that means user wants to
        # chain the estimators in that order,
        # by using the output of one as input to the next
        for estimator_name in list(estimator_dict.keys()):
            # TODO: Replace the predict with a util function that checks
            # the pipeline type and calls appropriate
            # "predict" equivalent
            X[estimator_name] = estimator_dict[estimator_name].predict(X)
        final_df = X
    elif estimator_dict is not None and isinstance(estimator_dict, dict):
        # if the estimator dictionary is not ordered, they need to be applied
        # independently, so only final_df is
        # modified with the predictions
        final_df = X
        for estimator_name in list(estimator_dict.keys()):
            # TODO: Replace the predict with a util function that checks the
            # pipeline type and calls appropriate
            # "predict" equivalent
            final_df[estimator_name] = estimator_dict[estimator_name].predict(X)

    objective_value, greater_is_better = objective_function(
        final_df, objective_function_params
    )

    # insert objective value into returned dataframe
    final_df["objective_value"] = objective_value
    return dict(
        objective_value=objective_value,
        greater_is_better=greater_is_better,
        parameter_combination=parameter_combination,
        data_frame=final_df,
    )


def _validate_optimization_param(objective_function, param_grid, estimator_dict):
    """
    Validates the parameters for optimization
    Args:
        objective_function (object, required): objective_function
        param_grid (object, required): param_grid
        estimator_dict (object, required): estimator_dict
    Raises:
        Exception: if the params are not valid
    """
    if not callable(objective_function):
        raise Exception("objective_function should be callable.")
    if not param_grid or not isinstance(param_grid, dict):
        raise Exception("param_grid should be a non empty dict")
    if not estimator_dict or not (
        isinstance(estimator_dict, dict) or isinstance(estimator_dict, OrderedDict)
    ):
        raise Exception("estimator_dict should be a non empty dict or OrderedDict")


def _convert_param_grid(param_grid):
    """
    Converts param_grid values to numpy.float64
    Args:
        param_grid (dict, required) : Parameter grid
    Returns:
        dict : Converted param grid
    """
    for key in param_grid.keys():
        if isinstance(param_grid[key], np.ndarray):
            param_grid[key] = param_grid[key].astype(np.float64)
        elif isinstance(param_grid[key], list):
            param_grid[key] = np.array(param_grid[key], dtype=np.float64)
        else:
            raise Exception(
                "Values in param_grid should either be np.ndarray or list type."
            )
    return param_grid


class Optimization(BaseEstimator):
    """Brute force optimization over a param grid of values.

    Args:

    **objective_function** (callable): The objective of the optimization problem.
    It needs to accept a pandas data frame and return a scalar with the objective
    value and a flag indicating whether a higher value of the objective is better
    or not i.e. whether it is a maximization or minimization problem.

    **objective_function_params** (dict): Optional parameters to pass to objective.

    **param_grid** (numpy.arange): A parameter grid for controllable variable. Defaults to None.

    **estimator_dict** (OrderedDictionary): Estimators for target variables, defaults to None.

    """

    def __init__(
        self,
        objective_function,
        objective_function_params=None,
        param_grid=None,
        estimator_dict=None,
    ):
        # Validate
        _validate_optimization_param(objective_function, param_grid, estimator_dict)

        self.objective_function = objective_function
        self.objective_function_params = objective_function_params
        self.param_grid = _convert_param_grid(param_grid)
        self.estimator_dict = estimator_dict

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def fit(self, *args):
        """No-op. Present only for frameworks expecting it on BaseEstimator types.

        Returns:
        Optimization. This class.

        """
        LOGGER.warning("fit is a no-op!")
        return self

    def predict(self, X, **kwargs):
        """Performs optimization on data using exploring each parameter_combination in param_grid,
        estimator_dict, objective_function and objective_function_params.

        Args:

        X (pandas.DataFrame): dataframe of dimension (1,n) containing scoring data.

        Returns:

        dict. Contains optimal set points and objective value.

        """
        if LOGGER.getEffectiveLevel() >= logging.DEBUG:
            LOGGER.debug("in predict with\n%s", str(X))
        results = [
            _getobjvalue(
                X=X,
                parameter_combination=parameter_combination,
                estimator_dict=self.estimator_dict,
                objective_function=self.objective_function,
                objective_function_params=self.objective_function_params,
            )
            for parameter_combination in ParameterGrid(self.param_grid)
        ]
        return _oncecollected(results)


class OptimizationParallel(Optimization):
    """
    Performs optimization using local multi-core parallism
    for each parameter in parameter grid. This should perform faster than Optimization.

    Args:

    **objective_function** (callable): The objective of the optimization problem.
    It needs to accept a pandas data frame and return a scalar with the objective
    value and a flag indicating whether a higher value of the objective is better
    or not i.e. whether it is a maximization or minimization problem.

    **objective_function_params** (dict): Optional parameters to pass to objective.

    **param_grid** (numpy.arange): A parameter grid for controllable variable. Defaults to None.

    **estimator_dict** (OrderedDictionary): Estimators for target variables, defaults to None.

    """

    def __init__(
        self,
        objective_function,
        objective_function_params=None,
        param_grid=None,
        estimator_dict=None,
    ):
        super(OptimizationParallel, self).__init__(
            objective_function, objective_function_params, param_grid, estimator_dict
        )

    def predict(self, X, **kwargs):
        """Performs optimization on data using exploring each parameter_combination in param_grid,
        estimator_dict, objective_function and objective_function_params.

        Args:

        X (pandas.DataFrame): dataframe of dimension (1,n) containing scoring data.

        Returns:

        dict. Contains optimal set points and objective value.
        """
        # We assume X is a pandas dataframe
        skl_param_grid = ParameterGrid(self.param_grid)
        pool = Pool(processes=multiprocessing.cpu_count())
        results = [
            pool.apply_async(
                _getobjvalue,
                (
                    parameter_combination,
                    X,
                    self.estimator_dict,
                    self.objective_function,
                    self.objective_function_params,
                ),
            )
            for parameter_combination in skl_param_grid
        ]
        return _oncecollected([res.get() for res in results])


class OptimizationSpark(BaseEstimator):
    """Performs optimization in parallel using Spark.

    Args:

    **objective_function** (callable): The objective of the optimization problem.
    It needs to accept a pandas data frame and return a scalar with the objective
    value and a flag indicating whether a higher value of the objective is better
    or not i.e. whether it is a maximization or minimization problem.

    **objective_function_params** (dict): Optional parameters to pass to objective.

    **param_grid** (numpy.arange): A parameter grid for controllable variable. Defaults to None.

    **estimator_dict** (OrderedDictionary): Estimators for target variables, defaults to None.

    **num_nodes** (int): Should be set to the number of spark nodes you have available
    to you on your cluster.

    **num_cores_per_node** (int): Number of cores available to you per node.
    Defaults to total cores available. For example, if you know you have two
    CPUs on each node, each being six cores, you should set this value to 12.
    If you are unsure, the default should suffice. Getting these values "right"
    in that they reflect the true state of your cluster, will maximize
    the parallism that OptimizeSpark is able to leverage.
    """

    def __init__(
        self,
        objective_function,
        objective_function_params=None,
        param_grid=None,
        estimator_dict=None,
        num_nodes=7,
        num_cores_per_node=multiprocessing.cpu_count(),
    ):
        # Validate
        _validate_optimization_param(objective_function, param_grid, estimator_dict)
        if not isinstance(num_nodes, int):
            raise Exception("num_nodes should be an integer.")
        if not isinstance(num_cores_per_node, int):
            raise Exception("num_cores_per_node should be an integer.")

        if platform.is_windows():
            raise NotImplementedError("Not implemented on Windows")
        self.objective_function = objective_function
        self.objective_function_params = objective_function_params
        self.param_grid = _convert_param_grid(param_grid)
        self.estimator_dict = estimator_dict
        self.num_partitions = num_nodes * num_cores_per_node
        self.param_grid_rdd = None

    def __enter__(self):
        return self

    def _cleanup(self):
        LOGGER.info("cleaning up....")
        if self.param_grid_rdd is not None:
            self.param_grid_rdd.unpersist()
            self.param_grid_rdd = None

    def __exit__(self, exc_type, exc_value, traceback):
        self._cleanup()

    def estimators(self):
        """returns a dictionary of estimators keyed by target name"""
        return self.estimator_dict

    def fit(self, *args):
        """
        Fit the estimator. Here it is no-op.
        """
        LOGGER.warning("fit is a no-op!")
        return self

    def predict(self, X, **kwargs):
        """
        Performs optimization on spark cluster over data for each parameter_combination
        in param_grid, estimator_dict, objective_function and objective_function_params.
        Args:
            **X** (pandas.DataFrame, required): objective_function accepts X.
        Returns:
            dict: Contains best_objective values.
        """
        estimator_dict = self.estimator_dict
        objective_function = self.objective_function
        objective_function_params = self.objective_function_params
        param_grid = []

        if self.param_grid_rdd is None:
            from pyspark import SparkContext
            from autoai_ts_libs.deps.srom.utils.package_version_check import check_pyspark_version

            check_pyspark_version()

            LOGGER.info("parallizing param_grid")
            for parameter_combination in ParameterGrid(self.param_grid):
                param_grid.append(parameter_combination)

            spark_context = SparkContext.getOrCreate()
            LOGGER.info("param_grid has size %d", len(param_grid))
            LOGGER.info("num_partitions is %d", self.num_partitions)
            self.param_grid_rdd = spark_context.parallelize(
                param_grid, self.num_partitions
            )
            self.param_grid_rdd.cache()

        results = self.param_grid_rdd.map(
            partial(
                _getobjvalue,
                X=X,
                estimator_dict=estimator_dict,
                objective_function=objective_function,
                objective_function_params=objective_function_params,
            )
        ).collect()
        return _oncecollected(results)


LOCK = Lock()


class NonLinearOptimizer(BaseEstimator):
    """A non-linear optimizer conforming (roughly) to same interface as other SROM grid-based
    optimizers.
    """

    def __init__(
        self,
        objective_functor,
        param_grid,
        estimator_dict,
        control_vars,
        observable_vars,
        optmethod: str = "COBYLA",
        static_constraints=None,
        round_solution=False,
        round_decimals=0,
        **kwargs,
    ):
        """
        Args:
            Args:

        **objective_functor** (object, required): A callable object (function or functor with
        __call__ method defined) representing the objective
        function. Note that since we always minimize in our
        non-linear optimizer, if you are running a maximization
        problem, be sure to return the negative of the value
        you are trying to optimize in your objective function.

        **param_grid** (dict, required): A parameter grid for controllable variable. This is used to
        obtain the minimum and maximum bounds for each control
        variable. We do not explore the full grid as is done with
        grid-search based optimization.

        **estimator_dict** (dict, required): A dictionary of estimators for target variables.

        **control_vars** (list, required): A string list of variables that are controllable.

        **observable_vars** (list, required): A string list of variables that are purely observable.
        That is, should NOT be altered by the optimizer.

        **optmethod** (string, optional): A string specifying the optimization method to use.
        Defaults to 'COBYLA'.
        Currently supported values are one of the following:
        'COBYLA': Constrained Optimization BY Linear Approximation
        'SLSQP': Sequential Least Squares Programming
        'trust-constr' trust-region algorithm for constrained optimization

        **round_solution**: If True, the optimizer will return only integer solutions. Caution,
        this could lead to infeasible solutions. As the underlying optimization techniques used by SROM
        are _continous_ in nature, integer truncation provide absolutely no guaranetee of optimal (locally or globbal) solutions much
        less feasible ones. User should use this option with great care checking the feasibility of the solution carefully.

        **round_decimals**: If solution_round is True, the number of decimals places to round solution to (default 0). Will be ignored
        if round_solution is False

        **\*\*kwargs** (optional): Keyword arguments that will be passed to the non-linear optimizer.
            These arguments affect the behavior of the optimizer.
            For example, if using 'COBYLA' for optmethod, passing maxiter=50000,
            rhobeg=10 would set the maximum functional evaluations and initial
            value perturbation to 50000 and 10 respectively (see function
            documentation for more details).

        Raises:
            ValueError: [description]
        """
        self._nlopt = NLOptimizer(
            piplines_dict=estimator_dict,
            control_vars=control_vars,
            param_grid=_convert_param_grid(param_grid),
        )
        self._obj_functor = objective_functor
        self._observable_vars = observable_vars
        self._force_rounding = round_solution
        self._round_decimals = round_decimals

        if optmethod.upper() not in SUPPORTED_METHODS:
            raise ValueError(
                "invalid optmethod %s, please choose one of %s"
                % (optmethod, ",".join(SUPPORTED_METHODS))
            )

        self._optmethod = optmethod
        self._nloptargs = kwargs

        unsupported_args = {"TRUST-CONSTR": ["rhobeg", "maxfun"]}

        # prune unsupported args
        for method, unsupported_list in unsupported_args.items():
            if optmethod.upper() == method:
                for unsupported in unsupported_list:
                    if unsupported in kwargs:
                        LOGGER.warning("removing unsupported argument %s", unsupported)
                        kwargs.pop(unsupported)

        self._static_constraints = static_constraints if static_constraints else []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def _templateanswer(self):
        return dict(
            objective_value=None,
            data_frame=None,
            parameter_combination=None,
            greater_is_better=False,
            optresult=OptimizeResult(),
        )

    def constraintcount(self):
        """Returns number of constraints."""
        return len(self._nlopt.constraints)

    def estimators(self):
        """returns a dictionary of estimators keyed by target name"""
        return self._nlopt.pipelines_dict

    def fit(self, *args):
        """
        Fit the estimator. Here it is no-op.
        """
        LOGGER.warning("fit is a no-op!")
        return self

    def get_params(self, deep=False):
        return self.__dict__

    def _postop(
        self,
        optarray,
        answer,
        adf_observables,
        adf_controllables,
        optresult,
        output_columns,
        **kwargs,
    ):
        setpoints_df: pd.DataFrame = pd.DataFrame(
            data=[optarray], columns=self._nlopt.control_vars
        )

        answer["data_frame"] = setpoints_df.join(adf_observables)

        # from notebooks sometimes it's REALLY hard to get
        # logging working properly so resort to this craziness
        # print('grrr')
        # print('setpoints_df', setpoints_df)
        # print('adf_observables', adf_observables)
        # print('self._nlopt.control_vars', self._nlopt.control_vars)
        # print('self._observable_vars', self._observable_vars)

        idx = 0
        adict = {}
        for controllable in self._nlopt.control_vars:
            adict[controllable] = optarray[idx]
            idx += 1

        # next two kept for backward compatibiltiy
        # with older brute force return type
        answer["parameter_combination"] = adict
        answer["objective_value"] = self._obj_functor(
            setpoints_df.values[0], adf_observables, adf_controllables, kwargs
        )
        answer["optresult"] = optresult
        if LOGGER.getEffectiveLevel() >= logging.DEBUG:
            LOGGER.debug("_postop returning\n%s", pprint.pformat(answer))

        # reorder (to make it look nice on output)
        # print(output_columns)
        # print(answer['data_frame'])
        if output_columns:
            answer["data_frame"] = answer["data_frame"][output_columns]

        flattened_info = kwargs.get("flattened_info", None)

        # unflatten if we have flattened info
        if flattened_info:
            answer["data_frame"] = unflatten(flattened_info, answer["data_frame"])

        # append the objective value to the returned value
        answer["data_frame"]["objective_value"] = answer["objective_value"]
        # set predict the value of targets
        # https://github.ibm.com/srom/docs/issues/36
        targetfilter = kwargs.get("targetfilter", None)
        if self._nlopt.pipelines_dict is not None:
            for target, model in self._nlopt.pipelines_dict.items():
                if targetfilter and not target in targetfilter:
                    LOGGER.info(
                        "skipping call to .predict for target %s as it's not in targetfilter.",
                        target,
                    )
                    continue
                try:
                    answer["data_frame"][target] = model.predict(answer["data_frame"])
                except ValueError as ve:  # this can happen if we're in flattened space
                    LOGGER.warning(ve)
                    LOGGER.warning(f"can not update answer['data_frame'][{target}]")

        # print(answer["data_frame"])
        return answer

    def predict(self, X: pd.DataFrame, **kwargs):
        """
        Performs the optimization over a dataframe containing a single row of values.
        Args:
            X (pandas.DataFrame, required): objective_function accepts X.
        Returns:
            dict: Contains best_objective values.
        """
        # print("in predict with %s" % str(X))
        # print(
        #    "we have %d total constraints including autogen bounding"
        #    % self.constraintcount()
        # )
        # print(__file__, "kwargs", kwargs)
        if LOGGER.getEffectiveLevel() >= logging.DEBUG:
            LOGGER.debug("in predict with\n%s", str(X))
            LOGGER.debug("we have %d total constraints", self.constraintcount())

        answer = self._templateanswer()

        adf_controllables = X[self._nlopt.control_vars]
        # print("adf_controllables", adf_controllables)
        adf_observables = X[self._observable_vars]
        # build bounding constraint dictionaries, one per constraint
        inequ_constraints = []
        # these come in from initial grid so
        # no need for special tuple arg handling
        for constraint in self._nlopt.constraints:
            inequ_constraints.append({"type": "ineq", "fun": constraint})
        # need special tuple arg handling
        for constraint in self._static_constraints:
            inequ_constraints += buildconstraint(constraint)

        # we assume args contains additional constraint callables
        # as inequalities
        if "constraints" in kwargs:
            passed_constraints = kwargs["constraints"]
            for acallable in passed_constraints:
                aconstraint = buildconstraint(acallable)
                inequ_constraints += aconstraint
                # print(__name__, "grr added inequ constraint", repr(aconstraint))
            # remove it from kwargs b/c it'll cause downstream issues
            # with sklearn estimators invalid kwargs
            kwargs.pop("constraints")

        # concession to PO, disable optimization if requested
        if kwargs.get("disableoptimization", False):
            LOGGER.warning("predict is skipping optimization")
            optarray = adf_controllables.values[0]
            optresult = OptimizeResult()
            optresult.success = True
            optresult.message = "Unoptimized values"
        else:
            # print(__name__, "grr inequ constraints has size", len(inequ_constraints))
            try:
                LOCK.acquire()
                optresult = minimize(
                    self._obj_functor,
                    adf_controllables.values[0],
                    args=(
                        adf_observables,
                        adf_controllables,
                        kwargs,
                    ),  # ALWAYS keep kwargs last!!
                    method=self._optmethod,
                    jac=None,
                    hess=None,
                    hessp=None,
                    bounds=None,
                    constraints=tuple(inequ_constraints),
                    tol=None,
                    callback=None,
                    options=self._nloptargs,
                )
                # truncate to integer and check
                # this is the best we can do without a non-linear
                # integer solver
                if optresult.success and self._force_rounding:
                    optresult.x = np.round(optresult.x, self._round_decimals)
                    print(
                        "checking feasibility of constraints with control variable rounding"
                    )
                    for constr in inequ_constraints:
                        if constr["fun"](optresult.x) < 0:
                            optresult.success = False
                            LOGGER.warning(
                                "forced rounding has yielded an infeasible solution"
                            )
                            print(
                                "forced rounding has yielded an infeasible solution",
                                file=sys.stderr,
                            )
                            break
                    if optresult.success:
                        print("solution still feasible!")

                if not optresult.success:
                    print("message", optresult.message)
                    if hasattr(optresult, "maxcv"):
                        print("maxcv", optresult.maxcv)
                optarray = optresult.x
            except Exception as e:
                LOGGER.exception(e)
                return None
            finally:
                LOCK.release()

        return self._postop(
            optarray,
            answer,
            adf_observables,
            adf_controllables,
            optresult,
            X.columns.values.tolist(),
            **kwargs,
        )
