"""
Unit test cases for testing run_timeseries_anomaly
"""
import os
import unittest

import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.time_series.run_timeseries_anomaly import run_timeseries_anomaly
from autoai_ts_libs.deps.srom.time_series.utils.types import (
    TSPDAGType,
    AnomalyAlgorithmType,
    AnomalyScoringPredictionType,
    AnomalyScoringAlgorithmType,
    AnomalyExecutionModeType,
    ReconstructADAlgorithmType,
    RelationshipADAlgorithmType,
)


class TestRunTimeseriesAnomaly(unittest.TestCase):
    """Test class for run_timeseries_anomaly"""

    @classmethod
    def setUpClass(cls):
        """Setup method: Called once before test-cases execution"""

        file_dir = os.path.dirname(os.path.realpath(__file__))
        cls.filename = os.path.join(file_dir, "../datasets/seasonal+trend.csv",)
        df = pd.read_csv(cls.filename, index_col=0)
        cls.X = df.reset_index()

        cls.time_column = "Time"
        cls.feature_columns = np.setdiff1d(df.columns, cls.time_column)
        cls.target_columns = np.setdiff1d(df.columns, cls.time_column)
        cls.pred_win = 1
        cls.lookback_win = 5

        cls.execution_type = "single_node_random_search"
        cls.total_execution_time = 1
        cls.num_estimators = 5
        cls.execution_mode = AnomalyExecutionModeType.BATCH
        cls.time_format = "%Y-%m-%d %H:%M:%S"
        cls.dag_type = TSPDAGType.BENCHMARK_ML
        cls.total_execution_time = 1
        cls.lookback_win = "auto"
        cls.observation_window = int(0.1 * df.shape[0])
        cls.scoring_method = AnomalyScoringAlgorithmType.QSCORE
        cls.pred_type = AnomalyScoringPredictionType.BATCH
        cls.scoring_threshold = 10
        cls.X[cls.time_column] = pd.to_datetime(
            cls.X[cls.time_column], format=cls.time_format
        )

    # DeepAD is tested in separate class, redundant test class

    def test_predad_batch_iid(self):
        """Test predad batch method"""
        results = run_timeseries_anomaly(
            dataName=self.filename,
            execution_mode=self.execution_mode,
            train_test_split_ratio=1,
            feature_columns=self.feature_columns,
            target_columns=self.target_columns,
            time_column=self.time_column,
            time_format=self.time_format,
            algorithm_type=AnomalyAlgorithmType.PREDAD,
            dag_type=self.dag_type,
            total_execution_time=self.total_execution_time,
            num_estimators=self.num_estimators,
            execution_time_per_pipeline=-1,
            execution_type="single_node_random_search",
            lookback_win=self.lookback_win,
            observation_window=self.observation_window,
            scoring_method=self.scoring_method,
            scoring_threshold=self.scoring_threshold,
            prediction_type=self.pred_type,
        )
        self.assertNotIn("error", results)
        self.assertIn("run_time", results)
        self.assertIn("lookback_window", results)
        self.assertIn("result", results)
        self.assertGreaterEqual(len(results["result"]), 1)
        self.assertIn("timestamp", results["result"][0])
        self.assertIn("value", results["result"][0])
        self.assertIn("anomaly_score", results["result"][0]["value"])
        self.assertIn("anomaly_label", results["result"][0]["value"])
        predictions = []
        for elem in results['result']:
            predictions.append(elem['value']['anomaly_label'])
        self.assertTrue(len(np.unique(np.array(predictions)))<=2)
        self.assertIn([-1,1],np.unique(np.array(predictions)))
        self.assertIsInstance(predictions[0], list)
        anomaly_scores = []
        for elem in results['result']:
            anomaly_scores.append(elem['value']['anomaly_score'])
        self.assertIsInstance(anomaly_scores[0], list)
        # check timestamp format
        self.assertEqual(
            results["result"][-1]["timestamp"],
            str(self.X[self.time_column].astype(str).values[self.X.shape[0] - 1]),
        )

    def test_windowad_batch_iid(self):
        """Test windowad batch method"""
        results = run_timeseries_anomaly(
            dataName=self.filename,
            execution_mode=self.execution_mode,
            train_test_split_ratio=1,
            feature_columns=self.feature_columns,
            target_columns=self.target_columns,
            time_column=self.time_column,
            time_format=self.time_format,
            algorithm_type=AnomalyAlgorithmType.WINDOWAD,
            dag_type=self.dag_type,
            total_execution_time=self.total_execution_time,
            num_estimators=self.num_estimators,
            execution_time_per_pipeline=-1,
            execution_type="single_node_random_search",
            lookback_win=self.lookback_win,
            observation_window=self.observation_window,
            scoring_method=self.scoring_method,
            scoring_threshold=self.scoring_threshold,
            prediction_type=self.pred_type,
        )
        self.assertNotIn("error", results)
        self.assertIn("run_time", results)
        self.assertIn("lookback_window", results)
        self.assertIn("result", results)
        self.assertGreaterEqual(len(results["result"]), 1)
        self.assertIn("timestamp", results["result"][0])
        self.assertIn("value", results["result"][0])
        self.assertIn("anomaly_score", results["result"][0]["value"])
        self.assertIn("anomaly_label", results["result"][0]["value"])
        predictions = []

        for elem in results['result']:
            predictions.append(elem['value']['anomaly_label'])
        self.assertTrue(len(np.unique(np.array(predictions))) <= 2)
        self.assertIn([-1, 1], np.unique(np.array(predictions)))
        self.assertIsInstance(predictions[0], list)
        anomaly_scores = []
        for elem in results['result']:
            anomaly_scores.append(elem['value']['anomaly_score'])
        self.assertIsInstance(anomaly_scores[0], list)
        # check timestamp format
        self.assertEqual(
            results["result"][-1]["timestamp"],
            str(self.X[self.time_column].astype(str).values[self.X.shape[0] - 1]),
        )

    def test_relationshipad_batch_iid(self):
        """Test relationshipad batch method"""
        results = run_timeseries_anomaly(
            dataName=self.filename,
            execution_mode=self.execution_mode,
            train_test_split_ratio=1,
            feature_columns=self.feature_columns,
            target_columns=self.target_columns,
            time_column=self.time_column,
            time_format=self.time_format,
            algorithm_type=AnomalyAlgorithmType.RELATIONSHIPAD,
            dag_type=self.dag_type,
            total_execution_time=self.total_execution_time,
            num_estimators=self.num_estimators,
            execution_time_per_pipeline=-1,
            execution_type="single_node_random_search",
            lookback_win=self.lookback_win,
            observation_window=self.observation_window,
            scoring_method=AnomalyScoringAlgorithmType.IID,
            scoring_threshold=self.scoring_threshold,
            prediction_type=self.pred_type,
            anomaly_estimator=RelationshipADAlgorithmType.GMM_L0,
        )
        self.assertNotIn("error", results)
        self.assertIn("run_time", results)
        self.assertIn("lookback_window", results)
        self.assertIn("result", results)
        self.assertGreaterEqual(len(results["result"]), 1)
        self.assertIn("timestamp", results["result"][0])
        self.assertIn("value", results["result"][0])
        self.assertIn("anomaly_score", results["result"][0]["value"])
        anomaly_scores = []
        for elem in results['result']:
            anomaly_scores.append(elem['value']['anomaly_score'])
        self.assertIsInstance(anomaly_scores[0], list)
        # check timestamp format
        self.assertEqual(
            results["result"][-1]["timestamp"],
            str(self.X[self.time_column].astype(str).values[self.X.shape[0] - 1]),
        )

    def test_reconstructad_batch_iid(self):
        """Test reconstructad batch method"""
        results = run_timeseries_anomaly(
            dataName=self.filename,
            execution_mode=self.execution_mode,
            train_test_split_ratio=1,
            feature_columns=self.feature_columns,
            target_columns=self.target_columns,
            time_column=self.time_column,
            time_format=self.time_format,
            algorithm_type=AnomalyAlgorithmType.RECONSTRUCTAD,
            dag_type=self.dag_type,
            total_execution_time=self.total_execution_time,
            num_estimators=self.num_estimators,
            execution_time_per_pipeline=-1,
            execution_type="single_node_random_search",
            lookback_win=self.lookback_win,
            observation_window=self.observation_window,
            scoring_method=self.scoring_method,
            scoring_threshold=self.scoring_threshold,
            prediction_type=self.pred_type,
            anomaly_estimator=ReconstructADAlgorithmType.DNN_AE,
        )
        self.assertNotIn("error", results)
        self.assertIn("run_time", results)
        self.assertIn("lookback_window", results)
        self.assertIn("result", results)
        self.assertGreaterEqual(len(results["result"]), 1)
        self.assertIn("timestamp", results["result"][0])
        self.assertIn("value", results["result"][0])
        self.assertIn("anomaly_score", results["result"][0]["value"])
        self.assertIn("anomaly_label", results["result"][0]["value"])
        predictions = []
        for elem in results['result']:
            predictions.append(elem['value']['anomaly_label'])
        self.assertTrue(len(np.unique(np.array(predictions))) <= 2)
        self.assertIn([-1, 1], np.unique(np.array(predictions)))
        self.assertIsInstance(predictions[0], list)
        anomaly_scores = []
        for elem in results['result']:
            anomaly_scores.append(elem['value']['anomaly_score'])
        self.assertIsInstance(anomaly_scores[0], list)
        # check timestamp format
        self.assertEqual(
            results["result"][-1]["timestamp"],
            str(self.X[self.time_column].astype(str).values[self.X.shape[0] - 1]),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
