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
import base64
import dill

from scipy.optimize import fmin_cobyla
from autoai_ts_libs.deps.srom.wml.adapter.optimization import NonLinearOptimizer
from autoai_ts_libs.deps.srom.wml.adapter.optimization import Optimization as WMLAdapterOptimization


class TestOptimizersWithWMLAdapter(unittest.TestCase):
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
        kwargs = xargs[-1] if len(xargs) > 0 else None
        return 10 if kwargs and kwargs.get("ten", False) else x[0] * x[1]

    @staticmethod
    def constraint1(x):
        """Constraint x ** 2 + y ** 2 < 1"""
        return 1 - (x[0] ** 2 + x[1] ** 2)

    @staticmethod
    def constraint2(x):
        """Constraint y > 0"""
        return x[1]

    def test_nlo_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        # Minimize the objective function f(x, y) = x * y
        # subject to the constraints x ** 2 + y ** 2 < 1 and y > 0
        # Initial guess is [0.0, 0.1]
        # solution is (-sqrt(2)/2, sqrt(2)/2)
        constraint1 = TestOptimizersWithWMLAdapter.constraint1
        constraint2 = TestOptimizersWithWMLAdapter.constraint2
        objective = TestOptimizersWithWMLAdapter.objective
        solution = fmin_cobyla(
            objective, [0.0, 0.1], [constraint1, constraint2], rhoend=1e-7
        )

        with NonLinearOptimizer(
            estimator_dict=None,
            objective_functor=objective,
            param_grid=dict(a=np.arange(-1, 100, 1), b=np.arange(0, 100, 1)),
            control_vars=["a", "b"],
            observable_vars=["c"],
            rhobeg=1,
            maxfun=10000,
        ) as nlo:

            constraints = [
                base64.b64encode(dill.dumps(constraint1)).decode(),
                base64.b64encode(dill.dumps(constraint2)).decode(),
            ]

            prediction = nlo.predict(
                [
                    [
                        test_class.df.columns,
                        constraints,
                        test_class.df.values[0],
                    ]
                ]
            )

            self.assertAlmostEqual(
                objective(solution), prediction[0]["objective_value"], places=5
            )

    def test_nlo_predict_method_varargs(self):
        """Test predict method"""
        test_class = self.__class__
        # Minimize the objective function f(x, y) = x * y
        # subject to the constraints x ** 2 + y ** 2 < 1 and y > 0
        # Initial guess is [0.0, 0.1]
        # solution is (-sqrt(2)/2, sqrt(2)/2)
        constraint1 = TestOptimizersWithWMLAdapter.constraint1
        constraint2 = TestOptimizersWithWMLAdapter.constraint2
        objective = TestOptimizersWithWMLAdapter.objective

        with NonLinearOptimizer(
            estimator_dict=None,
            objective_functor=objective,
            param_grid=dict(a=np.arange(-1, 100, 1), b=np.arange(0, 100, 1)),
            control_vars=["a", "b"],
            observable_vars=["c"],
            rhobeg=1,
            maxfun=10000,
        ) as nlo:

            constraints = [
                base64.b64encode(dill.dumps(constraint1)).decode(),
                base64.b64encode(dill.dumps(constraint2)).decode(),
            ]

            prediction = nlo.predict(
                [
                    [
                        test_class.df.columns,
                        constraints,
                        test_class.df.values[0],
                    ]
                ],
                ten=True,  # force objective to always return 10
            )

            self.assertEqual(10, prediction[0]["objective_value"])

    def test_legacy_optimizer_predict_method(self):
        """Test predict method with ordered dict"""
        ### Need to add more estimator in dict ###
        # piggy back off of upstream for constants
        from autoai_ts_libs.deps.srom.tests.optimization.test_optimization import TestOptimization
        from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline

        test_class = TestOptimization()
        test_class.setUpClass()
        param_grid = test_class.param_grid
        pipelines_ordered_dict = test_class.pipelines_ordered_dict
        data_for_recommendations = test_class.data_for_recommendations
        objective_function = TestOptimization.objective_function
        expected_objective_value_list = [
            (7 / (200 * 6.48 * 21.0 * 5.0), 7 / (200 * 6.48 * 21.0 * 50.0)),
            (7 / (200 * 7.88 * 21.0 * 5.0), 7 / (200 * 7.88 * 21.0 * 50.0)),
        ]

        with WMLAdapterOptimization(
            objective_function=objective_function,
            param_grid=param_grid,
            estimator_dict=pipelines_ordered_dict,
        ) as opt:
            pipeline_opt = SROMPipeline()
            pipeline_opt.set_stages([[opt]])
            pipeline_opt.set_best_estimator(opt)

            for index in range(data_for_recommendations.shape[0]):
                prediction_data = pd.DataFrame(
                    data_for_recommendations.iloc[[index]],
                    columns=data_for_recommendations.columns,
                )

                results = pipeline_opt.predict(
                    [[prediction_data.columns, [], prediction_data.values[0]]]
                )[0]

                best_objective_value = results["objective_value"]

                # Below assertion are dependent on predicted value for target
                # predicted value falls in the range: [5.0, 50.0]
                self.assertLessEqual(
                    best_objective_value, expected_objective_value_list[index][0]
                )
