import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator


class MeanModel(StateSpaceEstimator, BaseEstimator):
    """A base line prediction model : predict training mean"""

    def __init__(
        self, time_column=[0], feature_columns=[0], target_columns=[0], pred_win=1
    ):
        """
        Parameters:
            target_columns (numpy array): target indices
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.pred_win = pred_win

    def fit(self, X, y=None):
        """
        No learning, return the object as it is.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        X = X[:, self.target_columns].astype(float)
        self._mean = np.array([X.mean(axis=0)])
        return self

    def predict(self, X=None, prediction_type="forecast"):
        """
        Args:
            X (numpy array or time tensor) - input.
        """
        n_rows = 1
        n_cols = self.pred_win
        if prediction_type == "sliding":
            if X is None:
                raise Exception("X cannot be None for this option")
            n_rows = X.shape[0] - self.pred_win + 1
            if n_rows <= 0:
                raise Exception("X must be > pred_win for this option")
        if prediction_type == "training":
            if X is None:
                raise Exception("X cannot be None for this option")
            n_rows = X.shape[0]
        return np.tile(self._mean, (n_rows, n_cols))
