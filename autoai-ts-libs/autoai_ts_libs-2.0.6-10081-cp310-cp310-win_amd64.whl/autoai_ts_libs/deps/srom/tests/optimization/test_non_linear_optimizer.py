# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing classes under optimization.py"""
import unittest
import pandas as pd
import numpy as np

from scipy.optimize import fmin_cobyla
from autoai_ts_libs.deps.srom.optimization import NonLinearOptimizer


class TestNonLinearOptimizer(unittest.TestCase):
    """Test class for NonLinearOptimizer class"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        cls.df = pd.DataFrame(dict(a=[0.0], b=[0.1], c=[0.0]))

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    @staticmethod
    def objective(x, *xargs):
        """Minimize objective function"""
        return x[0] * x[1]

    @staticmethod
    def constraint1(x):
        """Constraint x ** 2 + y ** 2 < 1"""
        return 1 - (x[0] ** 2 + x[1] ** 2)

    @staticmethod
    def constraint2(x):
        """Constraint y > 0"""
        return x[1]

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        # Minimize the objective function f(x, y) = x * y
        # subject to the constraints x ** 2 + y ** 2 < 1 and y > 0
        # Initial guess is [0.0, 0.1]
        # solution is (-sqrt(2)/2, sqrt(2)/2)
        constraint1 = TestNonLinearOptimizer.constraint1
        constraint2 = TestNonLinearOptimizer.constraint2
        objective = TestNonLinearOptimizer.objective
        solution = fmin_cobyla(
            objective, [0.0, 0.1], [constraint1, constraint2], rhoend=1e-7
        )

        nlo = NonLinearOptimizer(
            estimator_dict=None,
            objective_functor=objective,
            param_grid=dict(a=np.arange(-1, 100, 1), b=np.arange(0, 100, 1)),
            control_vars=["a", "b"],
            observable_vars=["c"],
            rhobeg=1,
            maxfun=10000,
        )
        prediction = nlo.predict(
            test_class.df.iloc[[0]], constraints=[constraint1, constraint2]
        )
        self.assertAlmostEqual(
            objective(solution), prediction["objective_value"], places=5
        )

    def test_constraintcount_method(self):
        """Test constraintcount method"""
        test_class = self.__class__
        constraint1 = TestNonLinearOptimizer.constraint1
        constraint2 = TestNonLinearOptimizer.constraint2
        objective = TestNonLinearOptimizer.objective
        nlo = NonLinearOptimizer(
            estimator_dict=None,
            objective_functor=objective,
            param_grid=dict(a=np.arange(-1, 100, 1), b=np.arange(0, 100, 1)),
            control_vars=["a", "b"],
            observable_vars=["c"],
            rhobeg=1,
            maxfun=10000,
        )
        # Should have 4 constraints:
        # 2 for control variable a
        # 2 for control variable b
        self.assertEqual(4, nlo.constraintcount())
        prediction = nlo.predict(
            test_class.df.iloc[[0]], constraints=[constraint1, constraint2]
        )
        # Manually added constraints should not persist.
        self.assertEqual(4, nlo.constraintcount())

    def test_fit_method(self):
        """Test fit method"""
        objective = TestNonLinearOptimizer.objective
        nlo = NonLinearOptimizer(
            estimator_dict=None,
            objective_functor=objective,
            param_grid=dict(a=np.arange(-1, 100, 1), b=np.arange(0, 100, 1)),
            control_vars=["a", "b"],
            observable_vars=["c"],
            rhobeg=1,
            maxfun=10000,
        )
        self.assertEqual(id(nlo), id(nlo.fit()))

    def test_get_params_method(self):
        """Test get_params method"""
        objective = TestNonLinearOptimizer.objective
        nlo = NonLinearOptimizer(
            estimator_dict=None,
            objective_functor=objective,
            param_grid=dict(a=np.arange(-1, 100, 1), b=np.arange(0, 100, 1)),
            control_vars=["a", "b"],
            observable_vars=["c"],
            rhobeg=1,
            maxfun=10000,
        )
        params = nlo.get_params()
        from autoai_ts_libs.deps.srom.optimization.nlopt import NLOptimizer

        self.assertIsInstance(params["_nlopt"], NLOptimizer)
        self.assertEqual(params["_obj_functor"], objective)
        self.assertEqual(params["_observable_vars"], ["c"])
        self.assertEqual(params["_nloptargs"], {"rhobeg": 1, "maxfun": 10000})

    def test_predict_method_multiple_times(self):
        """Test predict method multiple times"""
        test_class = self.__class__
        # Minimize the objective function f(x, y) = x * y
        # subject to the constraints x ** 2 + y ** 2 < 1 and y > 0
        # Initial guess is [0.0, 0.1]
        # solution is (-sqrt(2)/2, sqrt(2)/2)
        constraint1 = TestNonLinearOptimizer.constraint1
        constraint2 = TestNonLinearOptimizer.constraint2
        objective = TestNonLinearOptimizer.objective
        solution = fmin_cobyla(
            objective, [0.0, 0.1], [constraint1, constraint2], rhoend=1e-7
        )

        nlo = NonLinearOptimizer(
            estimator_dict=None,
            objective_functor=objective,
            param_grid=dict(a=np.arange(-1, 100, 1), b=np.arange(0, 100, 1)),
            control_vars=["a", "b"],
            observable_vars=["c"],
            rhobeg=1,
            maxfun=10000,
        )
        # Call predict
        nlo.predict(test_class.df.iloc[[0]])
        # Call predict once more, this ensure that internally
        # earlier predict did not made any breaking changes
        prediction = nlo.predict(
            test_class.df.iloc[[0]], constraints=[constraint1, constraint2]
        )
        self.assertAlmostEqual(
            objective(solution), prediction["objective_value"], places=5
        )

    def test_invalid_optmethod(self):
        """Test with invalid optmethod"""
        self.assertRaises(
            ValueError,
            NonLinearOptimizer,
            estimator_dict=None,
            objective_functor=TestNonLinearOptimizer.objective,
            param_grid=dict(a=np.arange(-1, 100, 1), b=np.arange(0, 100, 1)),
            control_vars=["a", "b"],
            observable_vars=["c"],
            optmethod="UNKNOWN",
            rhobeg=1,
            maxfun=10000,
        )

