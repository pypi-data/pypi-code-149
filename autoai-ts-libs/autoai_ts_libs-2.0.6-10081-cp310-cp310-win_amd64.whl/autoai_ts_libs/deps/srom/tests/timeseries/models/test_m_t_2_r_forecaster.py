""" Test MT2RForecaster """
import unittest
import numpy as np
from autoai_ts_libs.deps.srom.time_series.models.MT2RForecaster import MT2RForecaster


class TestMT2RForecaster(unittest.TestCase):
    """ class for testing MT2RForecaster """

    @classmethod
    def setUp(cls):
        x = np.arange(30)
        y = np.arange(300, 330)
        X = np.array([x, y])
        X = np.transpose(X)
        #cls.n_jobs = 1
        cls.target_columns = [0, 1]
        cls.X = X

    def test_fit(self):
        """ method for testing the fit method of MT2RForecaster when n_jobs>1"""
        test_class = self.__class__
        model = MT2RForecaster(
            target_columns=test_class.target_columns, n_jobs=2
        )
        fitted_model = model.fit(test_class.X)
        self.assertEqual(fitted_model, model)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, n_jobs=1
        )
        fitted_model = model.fit(test_class.X)
        self.assertEqual(fitted_model, model)


    def test_predict_multicols(self):
        """ Tests the multivariate predict method of MT2RForecaster"""
        test_class = self.__class__
        model = MT2RForecaster(
            target_columns=test_class.target_columns, pred_win=2, n_jobs=2
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(test_class.X,prediction_type="sliding")
        self.assertEqual(len(ypred),29)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, pred_win=2, n_jobs=1
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(test_class.X,prediction_type="sliding")
        self.assertEqual(len(ypred),29)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, pred_win=2, n_jobs=1
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict(test_class.X)
        self.assertEqual(len(ypred),2)
        
        model = MT2RForecaster(
            target_columns=test_class.target_columns, pred_win=1, n_jobs=2
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 1)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, trend="Mean", n_jobs=2
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, trend="Poly", n_jobs=2
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, residual="Linear", n_jobs=2
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, residual="Difference", n_jobs=2
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, residual="Linear", n_jobs=1
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, residual="Difference", n_jobs=1
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 12)

    def test_predict_prob(self):
        """ Tests predict_prob method of MT2RForecaster"""
        test_class = self.__class__
        model = MT2RForecaster(target_columns=[0], pred_win=2, n_jobs=2)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_proba()
        self.assertEqual(ypred.shape, (2, 1, 2))
        model = MT2RForecaster(target_columns=[0, 1], pred_win=2, n_jobs=2)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_proba()
        self.assertEqual(ypred.shape, (2, 2, 2))
        model = MT2RForecaster(target_columns=[0], pred_win=2, n_jobs=1)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_proba()
        self.assertEqual(ypred.shape, (2, 1, 2))
        model = MT2RForecaster(target_columns=[0, 1], pred_win=2, n_jobs=1)
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_proba()
        self.assertEqual(ypred.shape, (2, 2, 2))

    def test_predict_uni_cols(self):
        """ Tests the univariate predict method of MT2RForecaster"""
        test_class = self.__class__
        x = np.arange(10)
        X = x.reshape(-1, 1)
        model = MT2RForecaster(target_columns=[0], pred_win=2, n_jobs=2)
        fitted_model = model.fit(X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 2)
        model = MT2RForecaster(target_columns=[0], pred_win=1, n_jobs=2)
        fitted_model = model.fit(X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 1)
        model = MT2RForecaster(target_columns=[0], pred_win=2, n_jobs=1)
        fitted_model = model.fit(X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 2)
        model = MT2RForecaster(target_columns=[0], pred_win=1, n_jobs=1)
        fitted_model = model.fit(X)
        ypred = fitted_model.predict()
        self.assertEqual(len(ypred), 1)

    def test_predict_multi_step_sliding_window(self):
        """ The tests multivariate predict_multi_step_sliding_window method of MT2RForecaster"""
        test_class = self.__class__
        model = MT2RForecaster(
            target_columns=test_class.target_columns, n_jobs=2
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_multi_step_sliding_window(
            test_class.X[test_class.X.shape[0] - 5 :], 3
        )
        self.assertEqual(len(ypred), 3)
        self.assertEqual(ypred.shape[1], 6)
        model = MT2RForecaster(
            target_columns=test_class.target_columns, n_jobs=1
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_multi_step_sliding_window(
            test_class.X[test_class.X.shape[0] - 5 :], 3
        )
        self.assertEqual(len(ypred), 3)
        self.assertEqual(ypred.shape[1], 6)

    def test_predict_sliding_window(self):
        """ The tests multivariate predict_multi_step_sliding_window method of MT2RForecaster"""
        test_class = self.__class__
        model = MT2RForecaster(
            target_columns=test_class.target_columns, n_jobs=2,pred_win=1
        )
        fitted_model = model.fit(test_class.X)
        ypred = fitted_model.predict_sliding_window(
            test_class.X[test_class.X.shape[0] - 5 :]
        )
        self.assertEqual(len(ypred), 5)
        self.assertEqual(ypred.shape[1], 2)

    def test_predict_uni_multi_step_sliding_window(self):
        """ The tests univariate predict_multi_step_sliding_window method of MT2RForecaster"""
        test_class = self.__class__
        x = np.arange(30)
        X = x.reshape(-1, 1)
        model = MT2RForecaster(target_columns=[0], n_jobs=2)
        fitted_model = model.fit(X)
        ypred = fitted_model.predict_multi_step_sliding_window(X[X.shape[0] - 5 :], 2)
        self.assertEqual(len(ypred), 4)
        self.assertEqual(ypred.shape[1], 2)
        model = MT2RForecaster(target_columns=[0], n_jobs=1)
        fitted_model = model.fit(X)
        ypred = fitted_model.predict_multi_step_sliding_window(X[X.shape[0] - 5 :], 2)
        self.assertEqual(len(ypred), 4)
        self.assertEqual(ypred.shape[1], 2)

    def test_predict_uni_sliding_window(self):
        """ The tests univariate predict_sliding_window method of MT2RForecaster"""
        test_class = self.__class__
        x = np.arange(30)
        X = x.reshape(-1, 1)
        model = MT2RForecaster(target_columns=[0], n_jobs=2)
        fitted_model = model.fit(X)
        ypred = fitted_model.predict_sliding_window(X[X.shape[0] - 5 :])
        self.assertEqual(len(ypred), 5)
        self.assertEqual(ypred.shape[1], 1)

    def test_parallel_predict(self):
        """Test parallel predict method"""
        test_class=self.__class__
        x = np.arange(30)
        X = x.reshape(-1, 1)
        model = MT2RForecaster(target_columns=[0], n_jobs=2)
        fitted_model = model.fit(X)
        ypred=fitted_model._parallel_predict(test_class.X)
        self.assertIsNotNone(ypred)


if __name__ == "__main__":
    unittest.main(verbosity=2, failfast=True)
