from sklearn.base import BaseEstimator
import numpy as np

class ZeroRAnomalyDetector(BaseEstimator):
    def __init__(self, feature_columns, target_columns):
        self.feature_columns = feature_columns
        self.target_columns = target_columns

    def fit(self, x):
        self.std_ = np.std(x[:, [self.target_columns]], axis=0)
        return self

    def predict(self, x):
        for idx,col in enumerate(self.target_columns):
            x[:, col][x[:, col] > (2 * self.std_[idx])] = -1
            x[:, col][x[:, col] != -1] = 1
        return x
