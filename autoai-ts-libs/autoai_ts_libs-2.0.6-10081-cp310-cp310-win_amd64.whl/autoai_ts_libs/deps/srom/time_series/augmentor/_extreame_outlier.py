import numpy as np
from autoai_ts_libs.deps.srom.time_series.augmentor._base import BaseAugmentor


def _extreme_outlier(x, prob, factor, random_state):
    additional_values = []
    if random_state is not None:
        np.random.seed(random_state)

    for timestamp_index in range(len(x)):
        local_std = x[max(0, timestamp_index - 10) : min(timestamp_index + 10, len(x))]
        local_std = np.std(local_std)
        value = np.random.choice([-1, 1]) * factor * local_std
        avalue = np.random.choice(
            [x[timestamp_index], value],
            p=[(1 - prob), prob],
        )
        additional_values.append(avalue)
    return np.asarray(additional_values, dtype=np.float32)


class ExtremeOutlier(BaseAugmentor):
    """
    Class for ExtremeOutlier
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        outlier_factor=8,
        prob=0.3,
        random_state=1,
    ):
        self.outlier_factor = outlier_factor
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.random_state = random_state
        self.prob = prob
        super().__init__()

    def transform(self, X):
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = np.apply_along_axis(
            _extreme_outlier,
            0,
            X[:, clm_index],
            self.prob,
            self.outlier_factor,
            self.random_state,
        )
        return X
