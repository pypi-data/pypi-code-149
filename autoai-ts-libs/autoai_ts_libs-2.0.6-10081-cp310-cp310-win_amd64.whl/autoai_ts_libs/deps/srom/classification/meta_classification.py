# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, ClassifierMixin
from autoai_ts_libs.deps.srom.classification.optimized_ensemble import Optimized_Ensemble_one, Optimized_Ensemble_two
from sklearn.metrics import log_loss
from sklearn.calibration import CalibratedClassifierCV

"""
.. module:: meta_classification
   :synopsis: Code to perform meta classification, for predictive maintainance type of data.

.. moduleauthor:: SROM Team
"""

# define MetaEnsemble here

class MetaClassifier(BaseEstimator, ClassifierMixin):
    """_summary_

    Args:
        BaseEstimator (_type_): _description_
        ClassifierMixin (_type_): _description_
    """

    def __init__(
        self, base_model,
    ):
        """_summary_

        Args:
            base_model (list of pipelines): This list contains a set of top-k performing pipeline.
            num_classes (_type_): _description_
        """
        self.base_model = base_model

    def fit(self, X, y):
        """
        Learn the optimal weights by solving an optimization problem.
        Parameters:
        ----------
        Xs: list of predictions to be ensembled
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        y: array-like
        Class labels
        """

        # Spliting train data into training and validation sets.
        X_train, X_valid, y_train, y_valid = train_test_split(
            X, y, test_size=0.25, random_state=123
        )
        
        p_valid = []
        for clf in self.base_model:
            # First run. Training on (X_train, y_train) and predicting on X_valid.
            clf.fit(X_train, y_train.ravel())
            yv = clf.predict_proba(X_valid)
            p_valid.append(yv)


        # combine the results
        XV = np.hstack(p_valid)
        self.num_classes_ = len(np.unique(y))

        self.ensemble_one_ = Optimized_Ensemble_one(self.num_classes_)
        self.ensemble_one_.fit(XV, y_valid.ravel())

        self.calibrated_ensemble_one_ = CalibratedClassifierCV(base_estimator=Optimized_Ensemble_one(self.num_classes_))
        self.calibrated_ensemble_one_.fit(XV, y_valid.ravel())

        self.ensemble_two_ = Optimized_Ensemble_two(self.num_classes_)
        self.ensemble_two_.fit(XV, y_valid.ravel())

        self.calibrated_ensemble_two_ = CalibratedClassifierCV(base_estimator=Optimized_Ensemble_two(self.num_classes_))
        self.calibrated_ensemble_two_.fit(XV, y_valid.ravel())

        return self

    def predict_proba(self, X):
        """
        Predict the class probabilites.
        
        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        p_test = []
        for clf in self.base_model:
            yt = clf.predict_proba(X)
            p_test.append(yt)

        XT = np.hstack(p_test)

        y_en1 = self.ensemble_one_.predict_proba(XT)
        y_en2 = self.ensemble_two_.predict_proba(XT)
        y_cal_en1 = self.calibrated_ensemble_one_.predict_proba(XT)
        y_cal_en2 = self.calibrated_ensemble_two_.predict_proba(XT)

        y_thirdlayer = (y_en1 * 4./9.) + (y_cal_en1 * 2./9.) + (y_en2 * 2./9.) + (y_cal_en2 * 1./9.)
        return y_thirdlayer

    def predict(self, X):
        """
        Use the weights learned in training to predict class probabilities.
        Parameters:
        ----------
        Xs: list of predictions to be blended.
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        Return:
        ------
        y_pred: array_like, shape=(n_samples, n_class)
        The blended prediction.
        """
        y_pred = self.predict_proba(X)
        
        index=[]
        for i in y_pred:
            ind=pd.Series(i).idxmax()
            index.append(ind)

        return index
