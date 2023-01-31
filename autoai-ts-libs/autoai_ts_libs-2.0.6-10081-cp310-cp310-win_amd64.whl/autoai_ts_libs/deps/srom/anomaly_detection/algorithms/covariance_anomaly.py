from sklearn.base import BaseEstimator
import numpy as np
import pandas as pd
from sklearn.utils.estimator_checks import check_estimator
from autoai_ts_libs.deps.srom.utils.distance_metric_utils import (
    compute_euclidean_distance,
    compute_riemannian_distance,
    compute_logdet_distance,
    compute_sym_kullback_distance,
)
from joblib import Parallel, delayed


class CovarianceAnomaly(BaseEstimator):
    """[summary]

    Args:
        BaseEstimator ([type]): [description]
    """

    def __init__(
        self,
        base_learner="covariance",
        distance_metric="euclidean",
        lookback_win=50,
        lookback_win_data_cutoff=0.1,
        n_jobs=1,
    ):
        """[summary]

        Args:
            base_learner (str, optional): [description]. Defaults to "covariance".
            distance_metric (str, optional): [description]. Defaults to "euclidean".
            lookback_win (int, optional): [description]. Defaults to 50.
            lookback_win_data_cutoff (int, optional): [description]. Defaults to 15.
            scale (bool, optional): [description]. Defaults to True.
            windowing (bool, optional): [description]. Defaults to False.
            
            BaseEstimator : shd be pushed into some other base model
            base_learner : string or an object of a class that gives covariance
            distance_metric : string or a callable function that compute distance
            sliding_window_size : int
            sliding_window_data_cutoff : what if I have many missing values
            scale : bool : this is a placeholder
            windowing : bool : whether to use sliding window or not.
            
        """
        self.base_learner = base_learner
        self.distance_metric = distance_metric
        self.lookback_win = lookback_win
        self.lookback_win_data_cutoff = lookback_win_data_cutoff
        self.n_jobs = n_jobs

    def _get_cov(self, X):
        """
        depending upon type of base_learner, call the function
        """
        if self.base_learner in ("covariance", "slide_covariance"):
            tmp_X = pd.DataFrame(X).dropna().values  # remove NULL
            if tmp_X.shape[0] < int(self.lookback_win_data_cutoff * self.lookback_win):
                raise Exception("Insufficient Data Point for Learning")
            return np.cov(tmp_X.T)
        elif not isinstance(self.base_learner, str) and check_estimator(self.base_learner) is None:
            estm = self.base_learner.fit(X)
            return estm.covariance_
        else:
            raise Exception("Invalid base learner.")

    def _get_distance(self, X):
        """
        depending upon type of distance metric and base learner, 
        call the appropriate function
        """
        if len(self.train_covDB_) == 1:
            if self.distance_metric == "euclidean":
                return compute_euclidean_distance(self.train_covDB_[0], X)
            elif self.distance_metric == "logdet":
                return compute_logdet_distance(self.train_covDB_[0], X)
            elif self.distance_metric == "riemannian":
                return compute_riemannian_distance(self.train_covDB_[0], X)
            elif self.distance_metric == "kullback":
                return compute_sym_kullback_distance(self.train_covDB_[0], X)

    def fit(self, X, y=None):
        """
        Fit method
        """
        # we will apply time delay embedding code here as time goes, but zeroth order is
        # the simple pass
        # this is a very baseline code
        self.train_covDB_ = []
        ans = self._get_cov(X.copy())
        if isinstance(ans, list):
            self.train_covDB_.extend(ans)
        else:
            self.train_covDB_.append(ans)
        return self

    def predict(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.anomaly_score(X)

    def anomaly_score(self, X):
        """[summary]

        Args:
            X: array-like, shape=(n_columns, n_samples,) training data.

        Returns:
            score: array-like shape of scores.
        """
        n_samples, n_features = X.shape[0], X.shape[1]
        slide_window = self.lookback_win
        n_windows = n_samples - slide_window + 1

        scores = np.zeros([n_samples, n_features])
        scores[:] = np.NAN  # added a NAN to check
        start_scores = n_samples - n_windows
        Xt = X.copy()
        if type(Xt) == pd.DataFrame:
            Xt = Xt.values

        def score_cov(test_X):
            """
                Score cov method using test_X

                Paramaters:
                    test_X: array like shape, training data
                
                Returns:
                    list
            """
            n_features = test_X.shape[1]
            tmp_X = test_X[~(np.isnan(test_X).any(axis=1))]
            if tmp_X.shape[0] < int(self.lookback_win_data_cutoff * slide_window):
                return [np.NaN] * n_features
            ans = self._get_cov(tmp_X.copy())
            result = self._get_distance(ans.copy())
            return [result] * n_features

        results = Parallel(n_jobs=self.n_jobs)(
            delayed(score_cov)(Xt[i : i + slide_window, :]) for i in range(n_windows)
        )

        for win_index in range(n_windows):
            score_index = start_scores + win_index
            scores[score_index, :] = results[win_index]
        return scores
