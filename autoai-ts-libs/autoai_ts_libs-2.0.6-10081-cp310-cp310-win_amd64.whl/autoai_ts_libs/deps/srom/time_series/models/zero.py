from sklearn.base import BaseEstimator
import pandas as pd
import numpy as np
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator


class ZeroModel(StateSpaceEstimator, BaseEstimator):
    """A base line prediction model : predict what you know"""

    def __init__(
        self,
        time_column=[0],
        feature_columns=[0],
        target_columns=[0],
        lookback_win=1,
        pred_win=1,
    ):
        """
        Parameters:
            target_columns (numpy array): target indices
            lookback_win (int, optional): Look-back window for the model.
            pred_win (int, optional): Look-ahead window for the model.
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.pred_win = pred_win

    def fit(self, X, y=None):
        """
        No learning, return the object as it is.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        X = X[:, self.target_columns].astype(float)
        self._last_known_value = X[-min(self.lookback_win, X.shape[0]), :]
        return self

    def predict(self, X=None, prediction_type="forecast"):
        """
        Args:
            X (numpy array or time tensor) - input.
        """
        n_rows = 1
        n_cols = self.pred_win
        if prediction_type == "sliding":
            n_rows = X.shape[0] - self.pred_win + 1
        return np.tile(self._last_known_value, (n_rows, n_cols))
