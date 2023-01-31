# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Common constraints and a base objective functor used by non-linear optimizer.
This module gives you basic min/max bound constraints as well as a template
for your specific objective function implementation.
"""

import pandas as pd

from . import utils


class MinBoundFunctor(object):
    """Enforces a minimum bound contraint in the non-linear optimizer.

    :param name: variable name (taken from a column in a pandas dataframe)
    :param names: the names of all control variables in the dataframe
    :param param_grid: a parameter grid containing minimum and maximum values for parameters
    :return: the contraint slack which is used by the non-linear
        optimizer during iterative optimization
    """

    def __init__(self, name, names, param_grid):
        self.name = name
        self.names = names
        self.param_grid = param_grid

    def bound(self):
        """
        Gives min parameter value.
        Returns:
            Integer
        """
        return self.param_grid[self.name].min()

    def __call__(self, x, *args):
        data_frame: pd.DataFrame = pd.DataFrame(data=[x], columns=self.names)
        return data_frame[self.name][0] - self.bound()


class MaxBoundFunctor(MinBoundFunctor):
    """Enforces a maximum bound contraint in the non-linear optimizer.

    :param name: variable name (taken from a column in a pandas dataframe)
    :param names: the names of all control variables in the dataframe
    :param param_grid: a parameter grid containing minimum and maximum values for parameters
    :return: the contraint slack which is used by the non-linear
        optimizer during iterative optimization
    """

    def bound(self):
        return self.param_grid[self.name].max()

    def __call__(self, x, *args):
        data_frame: pd.DataFrame = pd.DataFrame(data=[x], columns=self.names)
        return self.bound() - data_frame[self.name][0]


class ObjectiveFunctor:
    """Base class for an objective functor. Users will have to
    implement their own instance to reflect their specific objective function.
    """

    def __init__(self, control_vars, pipelines_dict):
        """
        :param control_vars a list of control variables (those being optimized)
        :param piplines_dict: the srom pipeline dictionary containing predictive models to
        (presumably) be used as part of your objective function evaluation
        self.control_vars = control_vars
        self.pipelines_dict = pipelines_dict
        """

    def __call__(self, x_vector, *args):
        """The actual object function implementation goes here.
        You must override this method.
        :param x_vector: a numpy array or array like structure containing floats of
        decision variable values. The NL optimizer will fiddle with these values.
        :param *args: variable args that can be leveraged by many implementations of
        non-linear optimizers to pass additional values into your
        objective function implementation
        """
        raise NotImplementedError(
            "you must provide a derived class implementation for this"
        )
