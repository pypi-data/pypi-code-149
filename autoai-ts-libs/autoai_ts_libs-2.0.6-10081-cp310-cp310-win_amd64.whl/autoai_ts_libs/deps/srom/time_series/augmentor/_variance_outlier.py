import numpy as np
import random
from autoai_ts_libs.deps.srom.time_series.augmentor._base import BaseAugmentor


def _variance_outlier(x, timestamps, outlier_factor, random_state):
    if timestamps == []:
        if random_state is not None:
            random.seed(random_state)

        start = random.choice(range(len(x) - 10))
        end = start + 10
        difference = (
            np.diff(x[start - 1 : end])
            if start > 0
            else np.insert(np.diff(x[start:end]), 0, 0)
        )
        x[list(range(start, end))] += (outlier_factor - 1) * difference
    else:
        for start, end in timestamps:
            difference = (
                np.diff(x[start - 1 : end])
                if start > 0
                else np.insert(np.diff(x[start:end]), 0, 0)
            )
            x[list(range(start, end))] += (outlier_factor - 1) * difference
    return np.asarray(x, dtype=np.float32)


class VarianceOutlier(BaseAugmentor):
    """
    Class for VarianceOutlier
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        timestamps=[],
        outlier_factor=8,
        random_state=1,
    ):
        self.outlier_factor = outlier_factor
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.random_state = random_state
        self.timestamps = timestamps
        super().__init__()

    def transform(self, X):
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = np.apply_along_axis(
            _variance_outlier,
            0,
            X[:, clm_index],
            self.timestamps,
            self.outlier_factor,
            self.random_state,
        )
        return X
