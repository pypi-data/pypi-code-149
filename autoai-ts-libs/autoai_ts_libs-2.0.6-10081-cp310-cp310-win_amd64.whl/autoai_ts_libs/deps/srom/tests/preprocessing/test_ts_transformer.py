import unittest
import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import (
    Flatten,
    TimeTensorTransformer,
    WaveletFeatures,
    FFTFeatures,
    TensorAggregateTransformer,
    SummaryStatistics,
    AdvancedSummaryStatistics,
    HigherOrderStatistics,
    RandomTimeSeriesFeatures,
    RandomTimeTensorTransformer,
    TimeSeriesFeatureUnion,
    customTimeSeriesFeatures,
    NormalizedFlatten,
    DifferenceNormalizedFlatten,
    DifferenceFlatten,
    LocalizedFlatten,
    DivisionFlatten,
    DivisionFlattenX,
    DifferenceFlattenX,
    LocalizedFlattenX,
    NormalizedFlattenX,
    TensorFlattenTransformer,
)
from autoai_ts_libs.deps.srom.feature_engineering.timeseries.function_map import MAPPING


class TestTsTransformer(unittest.TestCase):
    """Test various ts tranformer classes"""

    @classmethod
    def setUpClass(test_class):
        pass

    @classmethod
    def tearDownClass(test_class):
        pass

    def test_fit_transform_general_transformers(self):
        """Test fit transform mthod for some general transformers"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        transformers = [
            Flatten,
            #WaveletFeatures,
            FFTFeatures,
            SummaryStatistics,
            AdvancedSummaryStatistics,
            HigherOrderStatistics,
            TimeSeriesFeatureUnion,
            # RandomTimeSeriesFeatures,
            customTimeSeriesFeatures,
        ]

        params = [
            {
                "feature_columns": [0, 1],
                "target_columns": [0, 1],
                "lookback_win": lookback_win,
                "pred_win": 1,
            },
            {
                "feature_columns": [0],
                "target_columns": [0, 1],
                "lookback_win": lookback_win,
                "pred_win": 1,
            },
            {
                "feature_columns": [0],
                "target_columns": [0],
                "lookback_win": lookback_win,
                "pred_win": 1,
            },
            {
                "feature_columns": [0, 1],
                "target_columns": [0, 1],
                "lookback_win": lookback_win,
                "pred_win": 3,
            },
            {
                "feature_columns": [0],
                "target_columns": [0, 1],
                "lookback_win": lookback_win,
                "pred_win": 3,
            },
            {
                "feature_columns": [0],
                "target_columns": [0],
                "lookback_win": lookback_win,
                "pred_win": 3,
            },
        ]

        for est in transformers:
            for param in params:
                # print("********************", est, param, "**************************")
                if est == customTimeSeriesFeatures:
                    param["pd_func_list"] = ["mean"]
                    param["func_list"] = ["friedrich_coefficients"]
                    param["n_jobs"] = 1
                if est != Flatten:
                    param[
                        "n_jobs"
                    ] = 1  # workaround for joblib pickle issue https://github.com/joblib/joblib/issues/767

                estimator = est(**param)
                X_tf, y_tf = estimator.fit_transform(X_train)
                self.assertEqual(
                    X_tf.shape[0],
                    y_tf.shape[0],
                    "Failed estimator :" + str(est) + str(param),
                )
                self.assertEqual(
                    len(y_tf.shape), 2, "Failed estimator :" + str(est) + str(param)
                )
                self.assertEqual(
                    y_tf.shape[1],
                    len(param["target_columns"]) * param["pred_win"],
                    "Failed estimator :" + str(est) + str(param),
                )

    def test_fit_transform_normal_transformers(self):
        """Test fit transform method for some normal transformers"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        transformers = [
            NormalizedFlatten,
            #DifferenceNormalizedFlatten,
            DifferenceFlatten,
            LocalizedFlatten,
            DivisionFlatten,
            DivisionFlattenX,
            DifferenceFlattenX,
        ]

        params = [
            {
                "feature_columns": [0, 1],
                "target_columns": [0, 1],
                "lookback_win": lookback_win,
                "pred_win": 1,
            },
            {
                "feature_columns": [0],
                "target_columns": [0],
                "lookback_win": lookback_win,
                "pred_win": 1,
            },
            {
                "feature_columns": [0, 1],
                "target_columns": [0, 1],
                "lookback_win": lookback_win,
                "pred_win": 2,
            },
        ]

        for est in transformers:
            for param in params:
                print("********************", est, param, "**************************")
                if est == DifferenceFlattenX:
                    param['feature_columns'] = [0,1]
                    param['target_columns'] = [0]
                estimator = est(**param)
                X_tf, y_tf = estimator.fit(X_train).transform(X_train)
                self.assertEqual(
                    X_tf.shape[0],
                    y_tf.shape[0],
                    "Failed estimator :" + str(est) + str(param),
                )
                # print("X_train", X_train)
                # print("X_tf", X_tf)
                # print("y_tf", y_tf)
                # print("inverse", estimator.inverse_transform(y_tf))
                self.assertEqual(
                    len(y_tf.shape), 2, "Failed estimator :" + str(est) + str(param)
                )
                self.assertEqual(
                    y_tf.shape[1],
                    param["pred_win"],
                    "Failed estimator :" + str(est) + str(param),
                )

    # def test_fit_transform_custom_features_transformers(self):
    #     data = np.array(
    #         [
    #             [1, 1],
    #             [2, 2],
    #             [3, 3],
    #             [4, 4],
    #             [5, 5],
    #             [6, 6],
    #             [7, 7],
    #             [8, 8],
    #             [9, 9],
    #             [10, 10],
    #         ]
    #     )
    #     X = data.reshape(-1, 2)
    #     y = data.reshape(-1, 2)
    #     X = X.astype(float)
    #     y = y.astype(float)
    #     train_size = int(len(X) * 0.8)
    #     lookback_win = 4
    #     X_train = X[:train_size]
    #     y_train = y[:train_size]

    #     params = [
    #         {
    #             "feature_columns": [0, 1],
    #             "target_columns": [0, 1],
    #             "lookback_win": lookback_win,
    #             "pred_win": 1,
    #         },
    #         {
    #             "feature_columns": [0],
    #             "target_columns": [0],
    #             "lookback_win": lookback_win,
    #             "pred_win": 1,
    #         },
    #     ]

    #     for func in MAPPING.keys():
    #         for param in params:
    #             if func in [
    #                 "mean",
    #                 "max",
    #                 "min",
    #                 "median",
    #                 "std",
    #                 "sum",
    #                 "count",
    #                 "skew",
    #                 "kurt",
    #             ]:
    #                 param["pd_func_list"] = [func]
    #                 param["func_list"] = None
    #             else:
    #                 param["pd_func_list"] = None
    #                 param["func_list"] = [func]
    #             tf = customTimeSeriesFeatures(**param)
    #             # print("********************", tf, param, "**************************")
    #             X_tf, y_tf = tf.fit(X_train).transform(X_train)
    #             self.assertEqual(
    #                 X_tf.shape[0],
    #                 y_tf.shape[0],
    #                 "Failed transformer :" + str(tf) + str(param),
    #             )
    #             self.assertEqual(
    #                 len(y_tf.shape), 2, "Failed transformer :" + str(tf) + str(param),
    #             )

    def test_fit_transform_base_transformers(self):
        """Test fit transform method for some base transformers"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        transformers = [RandomTimeTensorTransformer, TimeTensorTransformer,LocalizedFlattenX]

        params = [
            {
                "feature_columns": [0,1],
                "target_columns": [0],
                "lookback_win": lookback_win,
                "pred_win": 1,
            }
        ]

        for est in transformers:
            for param in params:
                # print("********************", est, param, "**************************")
                estimator = est(**param)
                X_tf, y_tf = estimator.fit(X_train).transform(X_train)
                self.assertEqual(
                    X_tf.shape[0],
                    y_tf.shape[0],
                    "Failed estimator :" + str(est) + str(param),
                )
                self.assertEqual(
                    len(y_tf.shape), 2, "Failed estimator :" + str(est) + str(param)
                )
        
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = -1
        X_train = X[:train_size]
        y_train = y[:train_size]

        transformers2 = [ TimeTensorTransformer]

        params = [
            {
                "feature_columns": [1],
                "target_columns": [0],
                "lookback_win": lookback_win,
                "pred_win": -1,
            }
        ]

        for est in transformers2:
            for param in params:
                # print("********************", est, param, "**************************")
                estimator = est(**param)
                X_tf, y_tf = estimator.fit(X_train).transform(X_train)
                self.assertEqual(
                    X_tf.shape[0],
                    y_tf.shape[0],
                    "Failed estimator :" + str(est) + str(param),
                )
                self.assertEqual(
                    len(y_tf.shape), 1, "Failed estimator :" + str(est) + str(param)
                )

    # def test_division_flatten_fit_transform(self):
    #     data = np.array(
    #         [
    #             [1, 101],
    #             [2, 102],
    #             [3, 103],
    #             [4, 104],
    #             [5, 105],
    #             [6, 106],
    #             [7, 107],
    #             [8, 108],
    #             [9, 109],
    #             [10, 110],
    #         ]
    #     )

    #     X = data.reshape(-1, 2)
    #     y = data.reshape(-1, 2)
    #     X = X.astype(float)
    #     y = y.astype(float)
    #     train_size = int(len(X) * 0.8)
    #     lookback_win = -1
    #     X_train = X[:train_size]
    #     y_train = y[:train_size]

    #     transformers2 = [ LocalizedFlattenX]

    #     params = [
    #         {
    #             "feature_columns": [0,1],
    #             "target_columns": [0],
    #             "lookback_win": lookback_win,
    #             "pred_win": 1,
    #             "skip_observation":0,
    #         }
    #     ]

    #     for est in transformers2:
    #         for param in params:
    #             # print("********************", est, param, "**************************")
    #             estimator = est(**param)
    #             X_tf, y_tf = estimator.fit(X_train).transform(X_train)
    #             self.assertEqual(
    #                 X_tf.shape[0],
    #                 y_tf.shape[0],
    #                 "Failed estimator :" + str(est) + str(param),
    #             )
    #             self.assertEqual(
    #                 len(y_tf.shape), 1, "Failed estimator :" + str(est) + str(param)
                # )

    def test_TimeTensorTransformer_fit_transform_classification(self):
        """Test fit transform method for time tensor transformer"""
        # test if X and y are numpy array
        X = np.array(
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
        y = np.array(
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

        lookback_win = 4
        param = {
            "feature_columns": [2, 3],
            "target_columns": [2],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "mode": "classification",
        }

        param["id_column"] = 0
        param["time_column"] = 1
        estimator = TimeTensorTransformer(**param)
        X_tf, y_tf = estimator.fit(X).transform(X, y)
        context = estimator.context_
        self.assertEqual(X_tf.shape[0], 8)
        self.assertEqual(y_tf.shape[0], 8)
        self.assertEqual(context.shape[0], 8)
        self.assertTrue(list(y_tf.flatten()) == [0, 1, 1, 0, 1, 1, 0, 0])

        lookback_win = 4
        param = {
            "feature_columns": [2, 3],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": -1,
            "mode": "classification",
        }

        param["id_column"] = 0
        param["time_column"] = 1
        estimator = TimeTensorTransformer(**param)
        X_tf, y_tf = estimator.fit(X).transform(X, y)
        context = estimator.context_
        self.assertEqual(X_tf.shape[0], 8)
        self.assertEqual(y_tf.shape[0], 8)
        self.assertEqual(context.shape[0], 8)

        # test if X and y are pandas dataframe
        X = pd.DataFrame(X, columns=["asset_id", "time", "sensor1", "sensor2"])
        y = pd.DataFrame(y, columns=["asset_id", "time", "failed"])

        lookback_win = 4
        param = {
            "feature_columns": ["sensor1", "sensor2"],
            "target_columns": ["failed"],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "mode": "classification",
        }

        param["id_column"] = "asset_id"
        param["time_column"] = "time"
        estimator = TimeTensorTransformer(**param)
        X_tf, y_tf = estimator.fit(X).transform(X, y)
        context = estimator.context_
        self.assertEqual(X_tf.shape[0], 8)
        self.assertEqual(y_tf.shape[0], 8)
        self.assertEqual(context.shape[0], 8)
        self.assertTrue(list(y_tf.flatten()) == [0, 1, 1, 0, 1, 1, 0, 0])

    def test_fftfeatures_fit_transform(self):
        """Test fit transform method for fftfeatures"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "apply_mean_imputation":True,
        }

        estimator = FFTFeatures(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        self.assertTrue(list(y_tf.flatten()) == [2,3,4,5,6,7,8])

    def test_higher_order_statistics_fit_transform(self):
        """Test fit transform method for higher order statistics"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "n_jobs":None,
            "apply_mean_imputation":True,
        }

        estimator = HigherOrderStatistics(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        self.assertTrue(list(y_tf.flatten()) == [2,3,4,5,6,7,8])

    def test_advanced_summary_statistics_fit_transform(self):
        """Test fit transform method for advanced summary statistics"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "n_jobs":None,
            "apply_mean_imputation":True,
        }

        estimator = AdvancedSummaryStatistics(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        self.assertTrue(list(y_tf.flatten()) == [2,3,4,5,6,7,8])

    def test_summary_statistics_fit_transform(self):
        """Test fit transform method for summary statistics"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "n_jobs":1,
            "apply_mean_imputation":True,
        }

        estimator = SummaryStatistics(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        self.assertTrue(list(y_tf.flatten()) == [2,3,4,5,6,7,8])

    def test_localized_flatten_fit_transform(self):
        """Test fit transform method for localized flatten"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "skip_observation":0,
        }

        estimator = LocalizedFlatten(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        self.assertTrue(list(y_tf.flatten()) == [2,3,4,5,6,7,8])

    def test_tensor_aggregate_transformer_fit_transform(self):
        """Test fit transform method for tensor aggregate transformer"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "flatten_type":"summary_statistics",
        }

        estimator = TensorAggregateTransformer(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        self.assertTrue(list(y_tf.flatten()) == [2,3,4,5,6,7,8])

    def test_normalized_flatten_x_fit_transform(self):
        """Test fit transform method for normalized flattenx"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0,1],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "skip_observation":0,
        }

        estimator = NormalizedFlattenX(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        self.assertTrue(list(y_tf.flatten()) == [1, 1, 1, 1, 1, 1, 1])

    def test_localized_flatten_x_fit_transform(self):
        """Test fit transform method for localized flattenx"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0,1],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "skip_observation":0,
        }

        estimator = LocalizedFlattenX(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        self.assertTrue(list(y_tf.flatten()) == [2,3,4,5,6,7,8])

    def test_division_flatten_x_fit_transform(self):
        """Test fit transform method for division flattenx"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "skip_observation":0,
        }

        estimator = DivisionFlattenX(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)

    def test_difference_normalized_flatten_fit_transform(self):
        """Test fit transform method for difference normalized flatten"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [0],
            "lookback_win": lookback_win,
            "pred_win": 1,
        }

        estimator = DifferenceNormalizedFlatten(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertEqual(X_tf.shape[0], 7)
        self.assertEqual(y_tf.shape[0], 7)
        #self.assertTrue(list(y_tf.flatten()) == [2,3,4,5,6,7,8])

    def test_random_time_series_features_fit_transform(self):
        """Test fit transform method for random time series features"""
        data = np.array(
            [
                [1, 101],
                [2, 102],
                [3, 103],
                [4, 104],
                [5, 105],
                [6, 106],
                [7, 107],
                [8, 108],
                [9, 109],
                [10, 110],
            ]
        )
        X = data.reshape(-1, 2)
        y = data.reshape(-1, 2)
        X = X.astype(float)
        y = y.astype(float)
        train_size = int(len(X) * 0.8)
        lookback_win = 4
        X_train = X[:train_size]
        y_train = y[:train_size]

        lookback_win = 1
        param = {
            "feature_columns": [0],
            "target_columns": [1],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "n_jobs":None,
            #"n_interval":"sqrt",
            "n_random_features":0,
            "baseline_feature":"identity",
        }

        estimator = RandomTimeSeriesFeatures(**param)
        X_tf, y_tf = estimator.fit(X_train).transform(X_train,y_train)
        self.assertIsNotNone(X_tf)
        self.assertIsNotNone(y_tf)


    def test_Flatten_fit_transform_classification(self):
        """Test fit transform method for flatten"""
        # test if X and y are numpy array
        X = np.array(
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
        y = np.array(
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

        lookback_win = 4
        param = {
            "feature_columns": [2, 3],
            "target_columns": [2],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "mode": "forecasting",
        }

        param["id_column"] = 0
        param["time_column"] = 1
        estimator = Flatten(**param)
        X_tf, y_tf = estimator.fit(X).transform(X, y)
        self.assertEqual(X_tf.shape[0], 10)
        self.assertEqual(y_tf.shape[0], 10)
        self.assertTrue(list(y_tf.flatten()) == [0, 1, 1, 0, 1, 1, 0, 0] or [7, 8, 9, 3, 4, 5, 6, 7, 8, 9])

        lookback_win = 4
        param = {
            "feature_columns": [2, 3],
            "target_columns": [2],
            "lookback_win": lookback_win,
            "pred_win": 3,
            "mode": "forecasting",
        }

        param["id_column"] = 0
        param["time_column"] = 1
        estimator = Flatten(**param)
        X_tf, y_tf = estimator.fit(X).transform(X, y)
        self.assertEqual(X_tf.shape[0], 8)
        self.assertEqual(y_tf.shape[0], 8)
        self.assertTrue(list(y_tf.flatten()) == [0, 1, 1, 0, 1, 1, 0, 0] or [7, 8, 9, 3, 4, 5, 6, 7, 8, 9])

        # test if X and y are pandas dataframe
        X = pd.DataFrame(X, columns=["asset_id", "time", "sensor1", "sensor2"])
        y = pd.DataFrame(y, columns=["asset_id", "time", "failed"])

        lookback_win = 4
        param = {
            "feature_columns": ["sensor1", "sensor2"],
            "target_columns": ["failed"],
            "lookback_win": lookback_win,
            "pred_win": 1,
            "mode": "classification",
        }

        param["id_column"] = "asset_id"
        param["time_column"] = "time"
        estimator = Flatten(**param)
        X_tf, y_tf = estimator.fit(X).transform(X, y)
        context = estimator.context_
        self.assertEqual(X_tf.shape[0], 8)
        self.assertEqual(y_tf.shape[0], 8)
        self.assertEqual(context.shape[0], 8)
        self.assertTrue(list(y_tf.flatten()) == [0, 1, 1, 0, 1, 1, 0, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
