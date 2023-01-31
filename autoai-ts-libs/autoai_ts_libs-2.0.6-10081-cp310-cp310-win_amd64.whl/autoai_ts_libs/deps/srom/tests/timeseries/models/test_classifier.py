""" Test DeepAD """
import unittest

import numpy as np
from sklearn.metrics._scorer import accuracy_scorer
from sklearn.svm import SVC

from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
from autoai_ts_libs.deps.srom.time_series.pipeline import Classifier


class TestClassifier(unittest.TestCase):
    """class for testing DeepAD"""

    @classmethod
    def setUp(cls):
        cls.target_columns = [2]
        cls.feature_columns = [2, 3]
        cls.id_column = 0
        cls.time_column = 1
        cls.lookback_win = 4
        cls.pred_win = 1

        cls.X = np.array(
            [
                [1, 1, 3, 13],
                [1, 2, 4, 14],
                [1, 3, 5, 15],
                [1, 4, 6, 16],
                [1, 5, 7, 17],
                [1, 6, 8, 18],
                [1, 7, 9, 19],
                [2, 1, 3, 13],
                [2, 2, 4, 14],
                [2, 3, 5, 15],
                [2, 4, 6, 16],
                [2, 5, 7, 17],
                [2, 6, 8, 18],
                [2, 7, 9, 19],
            ]
        )
        cls.y = np.array(
            [
                [1, 1, 0],
                [1, 2, 0],
                [1, 3, 0],
                [1, 4, 0],
                [1, 5, 0],
                [1, 6, 1],
                [1, 7, 0],
                [2, 1, 0],
                [2, 2, 0],
                [2, 3, 0],
                [2, 4, 0],
                [2, 5, 1],
                [2, 6, 0],
                [2, 7, 0],
            ]
        )

    def test_fit(self):
        """method for testing the fit method of classifier"""
        test_class = self.__class__
        pipeline = Classifier(
            steps=[("flatten", Flatten(mode="classification")), ("svc", SVC())],
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            id_column=test_class.id_column,
            time_column=test_class.time_column,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
        )
        fitted_model = pipeline.fit(test_class.X, test_class.y)
        self.assertEqual(fitted_model, pipeline)

    def test_predict(self):
        """method for testing the predict method of classifier"""
        test_class = self.__class__
        pipeline = Classifier(
            steps=[("flatten", Flatten(mode="classification")), ("svc", SVC())],
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            id_column=test_class.id_column,
            time_column=test_class.time_column,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
        )
        fitted_model = pipeline.fit(test_class.X, test_class.y)
        self.assertEqual(fitted_model, pipeline)
        predicted = pipeline.predict(test_class.X)
        self.assertEqual(set(predicted), {0, 1})
        self.assertTrue(len(predicted) == 8)

    def test_score(self):
        """method for testing the score method of classifier"""
        test_class = self.__class__
        pipeline = Classifier(
            steps=[("flatten", Flatten(mode="classification")), ("svc", SVC())],
            feature_columns=test_class.feature_columns,
            target_columns=test_class.target_columns,
            id_column=test_class.id_column,
            time_column=test_class.time_column,
            lookback_win=test_class.lookback_win,
            pred_win=test_class.pred_win,
        )
        pipeline.set_scoring(accuracy_scorer)
        fitted_model = pipeline.fit(test_class.X, test_class.y)
        self.assertEqual(fitted_model, pipeline)
        score = pipeline.score(test_class.X, test_class.y)
        self.assertTrue(score <= 1.0 and score >= 0)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
