# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


from sklearn.base import BaseEstimator
import numpy as np
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.nearest_neighbor import (
    NearestNeighborAnomalyModel
)
from sklearn.neighbors import LocalOutlierFactor


class AnomalyEnsembler(BaseEstimator):
    """ 
    Ensemble model based Anomaly.
    """

    def __init__(self, random_state=42, predict_only=False):
        """
        Parameters:
            random_state : Random state,
            predict_only : Flag to use either predict function or decision function
        """
        self.random_state = random_state
        self.predict_only = predict_only

    def fit(self, X, y=None):
        """
        Fit the model using X
        Parameters:
            X: array-like, shape=(n_columns, n_samples,) training data.
            y: ignored but kept in for pipeline support.
        Return: 
            Returns an instance of self.
        """
        # root model
        self.tree_ = IsolationForest(random_state=self.random_state)

        # internal model
        self.mdl1_ = IsolationForest(random_state=self.random_state)
        self.mdl2_ = OneClassSVM()
        self.mdl3_ = NearestNeighborAnomalyModel()
        self.mdl4_ = LocalOutlierFactor(novelty=True)
        
        self.mdl1_.fit(X)
        self.mdl2_.fit(X)
        self.mdl3_.fit(X)
        self.mdl4_.fit(X)

        Xi = X.copy()

        y2 = self.mdl1_.predict(X).reshape(-1, 1)
        Xi = np.column_stack([Xi, y2[:, 0]])
        if not self.predict_only:
            y2 = self.mdl1_.decision_function(X).reshape(-1, 1)
            Xi = np.column_stack([Xi, y2[:, 0]])
  
        y2 = self.mdl2_.predict(X).reshape(-1, 1)
        Xi = np.column_stack([Xi, y2[:, 0]])
        if not self.predict_only:
            y2 = self.mdl2_.decision_function(X).reshape(-1, 1)
            Xi = np.column_stack([Xi, y2[:, 0]])
            
        if not self.predict_only:
            y2 = self.mdl3_.decision_function(X).reshape(-1, 1)
            Xi = np.column_stack([Xi, y2[:, 0]])
            
        y2 = self.mdl4_.predict(X).reshape(-1, 1)
        Xi = np.column_stack([Xi, y2[:, 0]])
        if not self.predict_only:
            y2 = self.mdl4_.decision_function(X).reshape(-1, 1)
            Xi = np.column_stack([Xi, y2[:, 0]])

        self.tree_.fit(Xi)
        return self

    def predict(self, X):
        """
        Predict if a point is an outlier.
        Parameters:
            X: array-like, shape=(n_columns, n_samples, ) training data.
        Return: 
            array, shape=(n_samples,) the predicted data. 1 for inliers, -1 for outliers.
        """
        predictions = (self._internal_score(X, "predict") < 0).astype(int)
        predictions[predictions == 1] = -1
        predictions[predictions == 0] = 1
        return predictions

    def _internal_score(self, X, mode="predict"):
        """
        Internal anomaly scoring function.
        Parameters:
            X: array-like, shape=(n_columns, n_samples, ) training data.
            mode: string like 'predict'.
        """
        Xi = X.copy()

        y2 = self.mdl1_.predict(X).reshape(-1, 1)
        Xi = np.column_stack([Xi, y2[:, 0]])
        if not self.predict_only:
            y2 = self.mdl1_.decision_function(X).reshape(-1, 1)
            Xi = np.column_stack([Xi, y2[:, 0]])

        y2 = self.mdl2_.predict(X).reshape(-1, 1)
        Xi = np.column_stack([Xi, y2[:, 0]])
        if not self.predict_only:
            y2 = self.mdl2_.decision_function(X).reshape(-1, 1)
            Xi = np.column_stack([Xi, y2[:, 0]])

        if not self.predict_only:
            y2 = self.mdl3_.decision_function(X).reshape(-1, 1)
            Xi = np.column_stack([Xi, y2[:, 0]])

        y2 = self.mdl4_.predict(X).reshape(-1, 1)
        Xi = np.column_stack([Xi, y2[:, 0]])
        if not self.predict_only:
            y2 = self.mdl4_.decision_function(X).reshape(-1, 1)
            Xi = np.column_stack([Xi, y2[:, 0]])

        if mode == "predict":
            return self.tree_.predict(Xi)

        return self.tree_.decision_function(Xi) * (-1.0)

    def anomaly_score(self, X):
        """
        Calculate Anomaly Score.
        Parameters:
            X : Pandas dataframe or numpy ndarray.
        """
        return self._internal_score(X, "score")

    def decision_function(self, X):
        """
        Calculate anomaly score.
        Parameters:
            X: array-like, shape=(n_columns, n_samples, ) data.
        """
        return self.anomaly_score(X)
