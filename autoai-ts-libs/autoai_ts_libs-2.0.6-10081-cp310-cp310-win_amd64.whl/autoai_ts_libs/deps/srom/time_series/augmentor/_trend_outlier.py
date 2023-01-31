from autoai_ts_libs.deps.srom.time_series.augmentor._base import BaseAugmentor
import numpy as np


def _trend_outlier(x, trend_outlier_ts, outlier_factor, random_state):
    if trend_outlier_ts == []:
        if random_state is not None:
            np.random.seed(random_state)
        start = np.random.choice(range(len(x) - 10))
        end = start + 10
        slope = np.random.choice([-1, 1]) * outlier_factor * np.arange(end - start)
        x[list(range(start, end))] += slope
    for start, end in trend_outlier_ts:
        if random_state is not None:
            np.random.seed(random_state)
        slope = np.random.choice([-1, 1]) * outlier_factor * np.arange(end - start)
        x[list(range(start, end))] += slope
    return x


class TrendOutlier(BaseAugmentor):
    """
    Class for TrendOutlier
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        trend_outlier_ts=[],
        outlier_factor=8,
        random_state=1,
    ):
        self.trend_outlier_ts = trend_outlier_ts
        self.outlier_factor = outlier_factor
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.random_state = random_state
        super().__init__()

    def transform(self, X):
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = np.apply_along_axis(
            _trend_outlier,
            0,
            X[:, clm_index],
            self.trend_outlier_ts,
            self.outlier_factor,
            self.random_state,
        )
        return X
