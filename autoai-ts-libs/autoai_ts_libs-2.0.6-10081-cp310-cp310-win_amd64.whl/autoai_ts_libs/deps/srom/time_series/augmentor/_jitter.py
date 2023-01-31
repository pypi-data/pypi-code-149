import numpy as np
from autoai_ts_libs.deps.srom.time_series.augmentor._base import BaseAugmentor


def _jitter(x, loc, rs, sigma):
    if isinstance(rs, int):
        rs = np.random.RandomState(rs)
    return x + rs.normal(loc=loc, scale=sigma, size=x.shape)


class Jitter(BaseAugmentor):
    """
    Class for Jitter
    """

    def __init__(
        self,
        feature_columns=[0],
        target_columns=[0],
        sigma=0.03,
        loc=0.0,
        random_state=1,
    ):
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.sigma = sigma
        self.loc = loc
        self.random_state=random_state
        super().__init__()

    def transform(self, X):
        clm_index = list(set(self.feature_columns + self.target_columns))
        X = X.copy()
        X[:, clm_index] = np.apply_along_axis(
            _jitter, 0, X[:, clm_index], self.loc, self.random_state, self.sigma
        )
        return X
