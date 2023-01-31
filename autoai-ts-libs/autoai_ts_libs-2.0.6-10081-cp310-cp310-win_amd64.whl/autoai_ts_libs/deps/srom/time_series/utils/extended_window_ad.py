from autoai_ts_libs.deps.srom.time_series.pipeline import WindowAD
import numpy as np

class ExtendedWindowAD(WindowAD):

    def fit(self, X, y=None):
        self.trainX_ = X
        return self

    def predict(self, X, prediction_type="training"):
        newX = np.concatenate([self.trainX_,X])
        super().fit(newX)
        ad_score = super().predict(X, prediction_type=prediction_type)
        return ad_score[-len(X):,]

    def anomaly_score(self, X, prediction_type="training"):
        newX = np.concatenate([self.trainX_,X])
        super().fit(newX)
        ad_score = super().anomaly_score(X, prediction_type=prediction_type)
        return ad_score[-len(X):,]
