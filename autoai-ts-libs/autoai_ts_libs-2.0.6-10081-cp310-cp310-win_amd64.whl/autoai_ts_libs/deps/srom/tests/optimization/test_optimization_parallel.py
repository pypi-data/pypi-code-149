# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Unit test cases for testing classes under optimization.py"""
import unittest

from collections import OrderedDict
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.preprocessing import MinMaxScaler

from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.optimization import OptimizationParallel
from autoai_ts_libs.deps.srom.feature_selection import FeatureListSelector
from autoai_ts_libs.deps.srom.utils.data_utils import train_test_split


class TestOptimizationParallel(unittest.TestCase):
    """Test class for OptimizationParallel class"""

    # Defining objective methods
    # Defining them at top makes sure that they are pickleable
    def objective_function(df, *xargs):
        """Objective function to maximize"""
        # Buyer will be most interested in buying house with:
        # more RM - average number of rooms per dwelling
        # less TAX - full-value property-tax rate per $10,000
        # less LSTAT - % lower status of the population
        # less PTRATIO - pupil-teacher ratio by town
        return (
            (df["RM"] / (df["TAX"] * df["LSTAT"] * df["PTRATIO"] * df["PRICE"])).mean(),
            True,
        )

    def reverse_objective_function(df, *xargs):
        """Objective function to minimize"""
        # Buyer will be most interested in buying house with:
        # more RM - average number of rooms per dwelling
        # less TAX - full-value property-tax rate per $10,000
        # less LSTAT - % lower status of the population
        # less PTRATIO - pupil-teacher ratio by town
        reduction_factor = xargs[0]["reduction_factor"]
        return (
            ((df["TAX"] * df["LSTAT"] * df["PTRATIO"] * df["PRICE"]) / df["RM"]).mean()
            * reduction_factor,
            False,
        )

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""
        # Load and split data
        b_data, target = load_boston(return_X_y=True)
        data = pd.DataFrame(b_data)
        data.columns = [
            "CRIM",
            "ZN",
            "INDUS",
            "CHAS",
            "NOX",
            "RM",
            "AGE",
            "DIS",
            "RAD",
            "TAX",
            "PTRATIO",
            "B",
            "LSTAT",
        ]
        data["PRICE"] = target
        data_for_model_training, data_for_recommendations = train_test_split(
            data, test_rows=2
        )

        # Setup pipeline and execute
        target = "PRICE"
        inputs = {"PRICE": ["TAX", "RM", "PTRATIO", "LSTAT"]}
        pipelines_ordered_dict = OrderedDict()
        pipelines_dict = {}
        feature_list = inputs[target]
        stages = [
            [FeatureListSelector(feature_list)],
            [MinMaxScaler()],
            [RandomForestRegressor()],
        ]
        pipeline = SROMPipeline()
        pipeline.set_scoring("r2")
        pipeline.add_input_meta_data(label_column=target)
        pipeline.set_stages(stages)
        pipeline.execute(data_for_model_training, exectype="single_node")

        # Fit pipelines
        fitted_pipeline = pipeline.fit(data_for_model_training)
        pipelines_ordered_dict[target] = fitted_pipeline
        pipelines_dict[target] = fitted_pipeline

        # Add data to be shared across tests
        cls.data_for_recommendations = data_for_recommendations[feature_list]
        cls.pipelines_ordered_dict = pipelines_ordered_dict
        cls.pipelines_dict = pipelines_dict
        cls.feature_list = feature_list
        # TAX and RM are controllable variables
        cls.param_grid = {
            "TAX": np.array([200, 256, 350, 450, 550, 666]),
            "RM": np.array([2, 3, 4, 5, 6, 7]),
        }
        cls.param_grid_with_list = {
            "TAX": cls.param_grid["TAX"].tolist(),
            "RM": cls.param_grid["RM"].tolist(),
        }

    @classmethod
    def tearDownClass(cls):
        """teardown class method: Called once after test-cases execution"""
        pass

    def test_predict_method(self):
        """Test predict method"""
        test_class = self.__class__
        param_grid = test_class.param_grid
        pipelines_dict = test_class.pipelines_dict
        data_for_recommendations = test_class.data_for_recommendations

        expected_objective_value_list = [
            (7 / (200 * 6.48 * 21.0 * 5.0), 7 / (200 * 6.48 * 21.0 * 50.0)),
            (7 / (200 * 7.88 * 21.0 * 5.0), 7 / (200 * 7.88 * 21.0 * 50.0)),
        ]
        expected_param_combos = [
            {"RM": 7.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 256.0},
        ]

        with OptimizationParallel(
            objective_function=TestOptimizationParallel.objective_function,
            param_grid=param_grid,
            estimator_dict=pipelines_dict,
        ) as opt:
            pipeline_opt = SROMPipeline()
            pipeline_opt.set_stages([[opt]])
            pipeline_opt.set_best_estimator(opt)

            for index in range(data_for_recommendations.shape[0]):
                prediction_data = pd.DataFrame(
                    data_for_recommendations.iloc[[index]],
                    columns=data_for_recommendations.columns,
                )
                results_dict = pipeline_opt.predict(prediction_data)
                best_objective_value = results_dict["objective_value"]
                parameter_combination = results_dict["parameter_combination"]
                data_frame = results_dict["data_frame"]

                # Below assertion are dependent on predicted value for target
                # predicted value falls in the range: [5.0, 50.0]
                self.assertLessEqual(
                    best_objective_value, expected_objective_value_list[index][0]
                )
                self.assertGreaterEqual(
                    best_objective_value, expected_objective_value_list[index][1]
                )
                lstat = data_frame.LSTAT.values[0]
                ptratio = data_frame.PTRATIO.values[0]
                price = data_frame.PRICE.values[0]
                # Trying to get value generated by optimization function
                value = parameter_combination["RM"] / (
                    parameter_combination["TAX"] * lstat * ptratio * price
                )
                self.assertAlmostEqual(best_objective_value, value, delta=0.1)
                self.assertIn(parameter_combination, expected_param_combos)

    def test_predict_method_with_param_grid_with_lists(self):
        """Test predict method with param grid with lists"""
        test_class = self.__class__
        param_grid = test_class.param_grid_with_list
        pipelines_dict = test_class.pipelines_dict
        data_for_recommendations = test_class.data_for_recommendations

        expected_objective_value_list = [
            (7 / (200 * 6.48 * 21.0 * 5.0), 7 / (200 * 6.48 * 21.0 * 50.0)),
            (7 / (200 * 7.88 * 21.0 * 5.0), 7 / (200 * 7.88 * 21.0 * 50.0)),
        ]
        expected_param_combos = [
            {"RM": 7.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 256.0},
        ]

        with OptimizationParallel(
            objective_function=TestOptimizationParallel.objective_function,
            param_grid=param_grid,
            estimator_dict=pipelines_dict,
        ) as opt:
            pipeline_opt = SROMPipeline()
            pipeline_opt.set_stages([[opt]])
            pipeline_opt.set_best_estimator(opt)

            for index in range(data_for_recommendations.shape[0]):
                prediction_data = pd.DataFrame(
                    data_for_recommendations.iloc[[index]],
                    columns=data_for_recommendations.columns,
                )
                results_dict = pipeline_opt.predict(prediction_data)
                best_objective_value = results_dict["objective_value"]
                parameter_combination = results_dict["parameter_combination"]

                # Below assertion are dependent on predicted value for target
                # predicted value falls in the range: [5.0, 50.0]
                self.assertLessEqual(
                    best_objective_value, expected_objective_value_list[index][0]
                )
                self.assertGreaterEqual(
                    best_objective_value, expected_objective_value_list[index][1]
                )
                self.assertIn(parameter_combination, expected_param_combos)

    def test_predict_method_with_wrong_param_grid_value(self):
        """Checking with wrong param_grid values. Should give an exception."""
        test_class = self.__class__
        param_grid = {"TAX": (200, 256, 350, 450, 550, 666), "RM": (2, 3, 4, 5, 6, 7)}
        pipelines_dict = test_class.pipelines_dict

        # Should raise exception when wrong value type is provided for param_grid
        self.assertRaises(
            Exception,
            OptimizationParallel,
            TestOptimizationParallel.objective_function,
            None,
            param_grid,
            pipelines_dict,
        )

    def test_predict_method_with_ordered_dict(self):
        """Test predict method with ordered dict"""
        ### Need to add more estimator in dict ###
        test_class = self.__class__
        param_grid = test_class.param_grid
        pipelines_ordered_dict = test_class.pipelines_ordered_dict
        data_for_recommendations = test_class.data_for_recommendations

        expected_objective_value_list = [
            (7 / (200 * 6.48 * 21.0 * 5.0), 7 / (200 * 6.48 * 21.0 * 50.0)),
            (7 / (200 * 7.88 * 21.0 * 5.0), 7 / (200 * 7.88 * 21.0 * 50.0)),
        ]
        expected_param_combos = [
            {"RM": 7.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 256.0},
        ]

        with OptimizationParallel(
            objective_function=TestOptimizationParallel.objective_function,
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
                results_dict = pipeline_opt.predict(prediction_data)
                best_objective_value = results_dict["objective_value"]
                parameter_combination = results_dict["parameter_combination"]

                # Below assertion are dependent on predicted value for target
                # predicted value falls in the range: [5.0, 50.0]
                self.assertLessEqual(
                    best_objective_value, expected_objective_value_list[index][0]
                )
                self.assertGreaterEqual(
                    best_objective_value, expected_objective_value_list[index][1]
                )
                self.assertIn(parameter_combination, expected_param_combos)

    def test_fit_method(self):
        """Test fit method"""
        test_class = self.__class__
        param_grid = test_class.param_grid
        pipelines_ordered_dict = test_class.pipelines_ordered_dict

        with OptimizationParallel(
            objective_function=TestOptimizationParallel.objective_function,
            param_grid=param_grid,
            estimator_dict=pipelines_ordered_dict,
        ) as opt:
            fitted_model = opt.fit()
            self.assertEqual(id(fitted_model), id(opt))

    def test_with_empty_param_grid(self):
        """Test predict method with empty param_grid"""
        test_class = self.__class__
        param_grid = {}
        pipelines_dict = test_class.pipelines_dict

        # Should raise exception
        self.assertRaises(
            Exception,
            OptimizationParallel,
            TestOptimizationParallel.objective_function,
            None,
            param_grid,
            pipelines_dict,
        )

    def test_optimization_with_smaller_is_better(self):
        """Test predict method with optimization method with smaller_is_better"""
        test_class = self.__class__
        param_grid = test_class.param_grid
        pipelines_dict = test_class.pipelines_dict
        data_for_recommendations = test_class.data_for_recommendations
        of_param = {"reduction_factor": 1e-06}
        expected_objective_value_list = [
            (
                (200 * 6.48 * 21.0 * 5.0) / 7 * 1e-06,
                (200 * 6.48 * 21.0 * 50.0) / 7 * 1e-06,
            ),
            (
                (200 * 7.88 * 21.0 * 5.0) / 7 * 1e-06,
                (200 * 7.88 * 21.0 * 50.0) / 7 * 1e-06,
            ),
        ]
        expected_param_combos = [
            {"RM": 7.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 256.0},
        ]

        with OptimizationParallel(
            objective_function=TestOptimizationParallel.reverse_objective_function,
            param_grid=param_grid,
            estimator_dict=pipelines_dict,
            objective_function_params=of_param,
        ) as opt:
            pipeline_opt = SROMPipeline()
            pipeline_opt.set_stages([[opt]])
            pipeline_opt.set_best_estimator(opt)

            for index in range(data_for_recommendations.shape[0]):
                prediction_data = pd.DataFrame(
                    data_for_recommendations.iloc[[index]],
                    columns=data_for_recommendations.columns,
                )
                results_dict = pipeline_opt.predict(prediction_data)
                best_objective_value = results_dict["objective_value"]
                parameter_combination = results_dict["parameter_combination"]

                # Below assertion are dependent on predicted value for target
                # predicted value falls in the range: [5.0, 50.0]
                self.assertLessEqual(
                    best_objective_value, expected_objective_value_list[index][1]
                )
                self.assertGreaterEqual(
                    best_objective_value, expected_objective_value_list[index][0]
                )
                self.assertIn(parameter_combination, expected_param_combos)

    def test_with_none_param_grid(self):
        """Test predict method with None param_grid"""
        test_class = self.__class__
        param_grid = None
        pipelines_dict = test_class.pipelines_dict

        # Should raise exception
        self.assertRaises(
            Exception,
            OptimizationParallel,
            TestOptimizationParallel.objective_function,
            None,
            param_grid,
            pipelines_dict,
        )

    def test_with_none_objective_function(self):
        """Test predict method with None objective_function"""
        test_class = self.__class__
        param_grid = test_class.param_grid
        pipelines_dict = test_class.pipelines_dict

        # Should raise exception
        self.assertRaises(
            Exception, OptimizationParallel, None, None, param_grid, pipelines_dict
        )

    def test_with_none_estimator_dict(self):
        """Test predict method with None estimator_dict"""
        test_class = self.__class__
        param_grid = test_class.param_grid
        pipelines_dict = None

        # Should raise exception
        self.assertRaises(
            Exception,
            OptimizationParallel,
            TestOptimizationParallel.objective_function,
            None,
            param_grid,
            pipelines_dict,
        )

    def test_with_empty_estimator_dict(self):
        """Test predict method with empty estimator_dict"""
        test_class = self.__class__
        param_grid = test_class.param_grid
        pipelines_dict = {}

        # Should raise exception
        self.assertRaises(
            Exception,
            OptimizationParallel,
            TestOptimizationParallel.objective_function,
            None,
            param_grid,
            pipelines_dict,
        )

    def test_predict_method_multiple_times(self):
        """Test predict method multiple times"""
        test_class = self.__class__
        param_grid = test_class.param_grid
        pipelines_dict = test_class.pipelines_dict
        data_for_recommendations = test_class.data_for_recommendations

        expected_objective_value_list = [
            (7 / (200 * 6.48 * 21.0 * 5.0), 7 / (200 * 6.48 * 21.0 * 50.0)),
            (7 / (200 * 7.88 * 21.0 * 5.0), 7 / (200 * 7.88 * 21.0 * 50.0)),
        ]
        expected_param_combos = [
            {"RM": 7.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 200.0},
            {"RM": 6.0, "TAX": 256.0},
        ]

        with OptimizationParallel(
            objective_function=TestOptimizationParallel.objective_function,
            param_grid=param_grid,
            estimator_dict=pipelines_dict,
        ) as opt:
            pipeline_opt = SROMPipeline()
            pipeline_opt.set_stages([[opt]])
            pipeline_opt.set_best_estimator(opt)

            for index in range(data_for_recommendations.shape[0]):
                prediction_data = pd.DataFrame(
                    data_for_recommendations.iloc[[index]],
                    columns=data_for_recommendations.columns,
                )
                # Call predict
                pipeline_opt.predict(prediction_data)
                # Call predict once more, this ensure that internally
                # earlier predict did not made any breaking changes
                results_dict = pipeline_opt.predict(prediction_data)
                best_objective_value = results_dict["objective_value"]
                parameter_combination = results_dict["parameter_combination"]
                data_frame = results_dict["data_frame"]

                # Below assertion are dependent on predicted value for target
                # predicted value falls in the range: [5.0, 50.0]
                self.assertLessEqual(
                    best_objective_value, expected_objective_value_list[index][0]
                )
                self.assertGreaterEqual(
                    best_objective_value, expected_objective_value_list[index][1]
                )
                lstat = data_frame.LSTAT.values[0]
                ptratio = data_frame.PTRATIO.values[0]
                price = data_frame.PRICE.values[0]
                # Trying to get value generated by optimization function
                value = parameter_combination["RM"] / (
                    parameter_combination["TAX"] * lstat * ptratio * price
                )
                self.assertAlmostEqual(best_objective_value, value, delta=0.1)
                self.assertIn(parameter_combination, expected_param_combos)

