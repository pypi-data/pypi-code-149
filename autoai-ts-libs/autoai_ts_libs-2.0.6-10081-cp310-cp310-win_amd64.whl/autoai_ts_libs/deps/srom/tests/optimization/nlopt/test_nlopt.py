# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing classes under nlopt.py"""

from autoai_ts_libs.deps.srom.optimization.nlopt import MinBoundFunctor, MaxBoundFunctor

import unittest
import numpy as np
from pandas import DataFrame
from autoai_ts_libs.deps.srom.optimization.nlopt.nlopt import NLOptimizer


class TestNLOptimizer(unittest.TestCase):
    """Test class for NLOptimizer class"""

    def test_bounds_construction(self):
        control_vars = ["a"]
        nlopt = NLOptimizer(
            piplines_dict={},
            param_grid={"a": np.arange(0, 10, 1)},
            control_vars=control_vars,
        )

        X = DataFrame([[10]], columns=control_vars)

        lowerbounds = [lb for lb in nlopt._minbounds(control_vars)]
        for lb in lowerbounds:
            self.assertEqual(10, lb(X.iloc[0]))  # one row at a time

        upperbounds = [ub for ub in nlopt._maxbounds(control_vars)]

        # we're 1 over the limit of 9 so that's
        # a violation of -1 (negative value b/c we always use ineq constraints
        # where negative vals signal infeasibility
        for ub in upperbounds:
            self.assertEqual(-1, ub(X.iloc[0]))  # one row at a time
