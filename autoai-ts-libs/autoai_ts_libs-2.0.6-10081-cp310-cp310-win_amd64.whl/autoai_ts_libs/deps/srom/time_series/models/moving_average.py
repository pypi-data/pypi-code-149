from typing import Optional

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator

from scipy.ndimage import uniform_filter1d


class MovingAverageModel(StateSpaceEstimator, BaseEstimator):
    """A baseline prediction model : predicts mean of the lookback window"""

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

    def fit(self, X: np.ndarray, y: Optional[np.ndarray] = None):
        """
        No learning just store lookback window
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        X = X[:, self.target_columns].astype(float)

        if self.lookback_win > X.shape[0]:
            self.lookback_X = X

        else:
            self.lookback_X = X[X.shape[0] - self.lookback_win :, :]

        return self

    def predict(
        self, X: Optional[np.ndarray] = None, prediction_type: str = "forecast"
    ) -> np.ndarray:
        """
        Args:
            X (numpy array or time tensor) - input.
        """
        if prediction_type == "forecast":
            if X is None:
                # do the moving average for self.lookback_X
                n = len(self.lookback_X)
                Xt = self.lookback_X

                predictions = np.empty((0, len(self.target_columns)))

                for _ in range(self.pred_win):
                    moving_average = np.nanmean(Xt, axis=0, keepdims=True)
                    predictions = np.concatenate((predictions, moving_average))
                    Xt = np.concatenate((Xt, moving_average))[1:, :]

            else:
                n = min(X.shape[0], self.lookback_win)
                Xt = X[X.shape[0] - n :, :]

                predictions = np.empty((0, X.shape[1]))

                for _ in range(self.pred_win):
                    moving_average = np.nanmean(Xt, axis=0, keepdims=True)
                    predictions = np.concatenate((predictions, moving_average))
                    Xt = np.concatenate((Xt, moving_average))[1:, :]

        elif prediction_type == "sliding":
            if X is None:
                raise Exception("X cannot be None for this option")

            if X.shape[0] < (self.lookback_win + self.pred_win):
                raise Exception("size of X is not enough for this option")

            predictions = np.empty((0, X.shape[1]))

            start, end = 0, self.lookback_win

            while end < X.shape[0]:
                Xt = X[start:end, :]
                moving_average = np.nanmean(Xt, axis=0, keepdims=True)
                predictions = np.concatenate((predictions, moving_average))

                start += 1
                end += 1

        return predictions
