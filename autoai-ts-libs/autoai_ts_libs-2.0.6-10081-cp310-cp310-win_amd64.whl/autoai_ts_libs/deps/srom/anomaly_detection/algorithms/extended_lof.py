from sklearn.neighbors import LocalOutlierFactor
import numpy as np

class ExtendedLocalOutlierFactor(LocalOutlierFactor):

    def fit(self, X, y=None):
        self.trainX_ = X
        return self

    def fit_predict_score(self, X):
        newX = np.concatenate([self.trainX_,X])
        super().fit(newX)
        return self.negative_outlier_factor_[len(self.trainX_):]
