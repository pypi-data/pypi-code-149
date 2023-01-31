from sklearn.base import BaseEstimator
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator
import numpy as np


class HoltWinters(BaseEstimator, StateSpaceEstimator):
    """A Placeholder."""

    def __init__(
        self,
        time_column=[0],
        feature_columns=[0],
        target_columns=[0],
        season_len=24,
        alpha=0.5,
        beta=0.5,
        gamma=0.5,
    ):
        """[summary]

        Args:
            season_len (int, optional): [description]. Defaults to 24.
            alpha (float, optional): [description]. Defaults to 0.5.
            beta (float, optional): [description]. Defaults to 0.5.
            gamma (float, optional): [description]. Defaults to 0.5.
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.beta = beta
        self.alpha = alpha
        self.gamma = gamma
        self.season_len = season_len

    def fit(self, series):
        """[summary]

        Args:
            series ([type]): [description]

        Returns:
            [type]: [description]
        """
        beta = self.beta
        alpha = self.alpha
        gamma = self.gamma
        season_len = self.season_len
        seasonals = self._initial_seasonal(series)

        # initial values
        predictions = []
        smooth = series[0]
        trend = self._initial_trend(series)
        predictions.append(smooth)

        for i in range(1, len(series)):
            value = series[i]
            previous_smooth = smooth
            seasonal = seasonals[i % season_len]
            smooth = alpha * (value - seasonal) + (1 - alpha) * (
                previous_smooth + trend
            )
            trend = beta * (smooth - previous_smooth) + (1 - beta) * trend
            seasonals[i % season_len] = (
                gamma * (value - smooth) + (1 - gamma) * seasonal
            )
            predictions.append(smooth + trend + seasonals[i % season_len])

        self.trend_ = trend
        self.smooth_ = smooth
        self.seasonals_ = seasonals
        self.predictions_ = predictions
        return self

    def _initial_trend(self, series):
        """[summary]

        Args:
            series ([type]): [description]

        Returns:
            [type]: [description]
        """
        season_len = self.season_len
        total = 0.0
        for i in range(season_len):
            total += (series[i + season_len] - series[i]) / season_len

        trend = total / season_len
        return trend

    def _initial_seasonal(self, series):
        """[summary]

        Args:
            series ([type]): [description]

        Returns:
            [type]: [description]
        """
        season_len = self.season_len
        n_seasons = len(series) // season_len

        season_averages = np.zeros(n_seasons)
        for j in range(n_seasons):
            start_index = season_len * j
            end_index = start_index + season_len
            season_average = np.sum(series[start_index:end_index]) / season_len
            season_averages[j] = season_average

        seasonals = np.zeros(season_len)
        seasons = np.arange(n_seasons)
        index = seasons * season_len
        for i in range(season_len):
            seasonal = np.sum(series[index + i] - season_averages) / n_seasons
            seasonals[i] = seasonal

        return seasonals

    def predict(self, n_preds=10):
        """
        Parameters
        ----------
        n_preds: int, default 10
            Predictions horizon. e.g. If the original input time series to the .fit
            method has a length of 50, then specifying n_preds = 10, will generate
            predictions for the next 10 steps. Resulting in a prediction length of 60.
        """
        predictions = self.predictions_
        original_series_len = len(predictions)
        for i in range(original_series_len, original_series_len + n_preds):
            m = i - original_series_len + 1
            prediction = (
                self.smooth_ + m * self.trend_ + self.seasonals_[i % self.season_len]
            )
            predictions.append(prediction)

        return predictions
