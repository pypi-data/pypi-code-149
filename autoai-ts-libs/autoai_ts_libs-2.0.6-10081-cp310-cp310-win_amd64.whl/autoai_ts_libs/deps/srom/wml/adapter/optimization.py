# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: optimization
   :synopsis: This adapts the srom optimization module 
   for use with WML..

.. moduleauthor:: SROM Team
"""
import logging
import pprint
import copy
import json
import base64
import dill

from sklearn.base import BaseEstimator
import pandas as pd
from pandas import DataFrame
import numpy as np

from autoai_ts_libs.deps.srom.optimization import NonLinearOptimizer as NLOptImpl
from autoai_ts_libs.deps.srom.optimization import Optimization as Opt

LOGGER = logging.getLogger(__name__)


def _predict(impl, X, **kwargs):
    # X is going to come in as a list of lists
    # convert it to something we can use directly
    # with our impl class
    newx = X[0]
    columns = newx[0]
    constraint_list = newx[1]

    # revert to legacy kwarg handling
    # which was basically no kwargs
    mykwargs = newx[2]
    data_start_index = 3
    if not isinstance(mykwargs, dict):
        mykwargs = {}
        # don't lose what might have already
        # been there
        mykwargs.update(kwargs)
        data_start_index = 2

    # print(__name__, "grr, custom kwargs are", mykwargs)

    # print(__name__, "grr constraint list size", len(constraint_list))

    constraints = []
    for constraint in constraint_list:
        constraints.append(dill.loads(base64.b64decode(constraint.encode())))

    if len(constraints) > 0:
        mykwargs["constraints"] = constraints

    # print(__name__, "grr constraints are", repr(constraints))
    data = newx[data_start_index:]
    data_frame = pd.DataFrame(data, columns=columns)
    for col in data_frame.columns.values:
        # convert the data to numeric
        data_frame[col] = pd.to_numeric(data_frame[col], errors="ignore")
    answer = impl.predict(data_frame, **mykwargs)
    df: DataFrame = answer["data_frame"]
    optresult = answer["optresult"]
    if not optresult.success:
        for column in df.columns:
            df[column] = -999

    return np.array(json.loads(df.to_json(orient="records")))


class Optimization(BaseEstimator):
    """
    WML deployment compatible wrapper for srom.optimization module
    """

    def __init__(
        self,
        objective_function,
        objective_function_params=None,
        param_grid=None,
        estimator_dict=None,
    ):
        self._impl = Opt(
            objective_function, objective_function_params, param_grid, estimator_dict
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def estimators(self):
        """
        Returns a dictionary of estimators \
        keyed by target name.
        """
        return self._impl.estimator_dict

    def fit(self, *args):
        """
        Fit the estimator. Here it is no-op.
        """
        LOGGER.warning("fit is a no-op!")
        return self

    def predict(self, X, **kwargs):
        return _predict(self._impl, X, **kwargs)


class NonLinearOptimizer(BaseEstimator):
    """
    WML deployment compatible wrapper for srom.optimization module
    """

    def __init__(
        self,
        objective_functor,
        param_grid,
        estimator_dict,
        control_vars,
        observable_vars,
        optmethod="COBYLA",
        static_constraints=None,
        **kwargs
    ):

        constraints = (
            [dill.loads(base64.b64decode(item.encode())) for item in static_constraints]
            if static_constraints
            else []
        )

        self._impl = NLOptImpl(
            objective_functor=objective_functor,
            param_grid=param_grid,
            estimator_dict=estimator_dict,
            control_vars=control_vars,
            observable_vars=observable_vars,
            optmethod=optmethod,
            static_constraints=constraints,
            **kwargs
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def constraintcount(self):
        return self._impl.constraintcount()

    def estimators(self):
        return self._impl._nlopt.pipelines_dict

    def fit(self, *args):
        return self

    def get_params(self, deep=False):
        return self._impl.get_params(deep)

    def predict(self, X, **kwargs):
        """Calls predict on the underlying implementation object.
        This method wraps the latter by having a custom ordering for the input data X as follows:

        Args:
            X (list): a list of json serializable objects in the following order
            X[0]  : a list of scoring data column names
            X[1]  : a list of additional (base64 encoded) constraint objects
                    (pass an empty list if there are no additional constraints)
            X[2]  : a dictionary of keyword arguments to use for the call to the underlying optimizers predict method
            X[3:] : a list of lists representing the scoring data
            kwargs : **always ignored**. Necessary to create a WML compatible predict signature. Actual kwargs should be passed
                     via the value for X[2]

        Returns:
            [type]: [description]
        """

        # maintain legacy behaviod where X[2:] the data if there are no
        # passed kwargs in X[2]
        # kwwargs for wml endpoint wrapper
        # is necessarily always empty. kwargs
        # get embedded in X (the scoring payload)
        return _predict(self._impl, X, **kwargs)
