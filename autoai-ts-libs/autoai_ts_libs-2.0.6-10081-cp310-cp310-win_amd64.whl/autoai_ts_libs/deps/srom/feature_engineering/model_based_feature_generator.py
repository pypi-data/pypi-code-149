# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: model_based_feature_generator
   :synopsis: Model Based Feature Generator.

.. moduleauthor:: SROM Team
"""
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin
from sklearn.utils import check_array


class ModelbasedFeatureGenerator(BaseEstimator, TransformerMixin):
    """
       A model based feature generator for adding predictions and/or \
        class probabilities as features.
    """

    def __init__(self, estimator):
        """
        Parameters:
            estimator: Object with fit, predict, and predict_proba methods.
        """
        self.estimator = estimator
        self.y_shape = 1

    def fit(self, X, y, **fit_params):
        """
        Parameters:
            X (dataframe or numpy array, required): The dataset to be used for model selection. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.
            y (dataframe or numpy array, required): Target vector to be used. \
                shape = [n_samples] or [n_samples, n_output].

        Return:
            self
        """
        self.estimator.fit(X, y, **fit_params)
        self.y_shape = y.shape[1] if len(y.shape) > 1 else 1
        return self

    def transform(self, X):
        """
        Parameters:
            X (dataframe or numpy array, required): The dataset to be used for model selection. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.

        Return:
            transformed numpy array.
        """
        X = check_array(X)
        X_transformed = np.copy(X)

        if issubclass(self.estimator.__class__, ClassifierMixin) and hasattr(
            self.estimator, "predict_proba"
        ):
            X_transformed = np.hstack((self.estimator.predict_proba(X), X))

        X_transformed = np.hstack(
            (np.reshape(self.estimator.predict(X), (-1, self.y_shape)), X_transformed)
        )

        return X_transformed

    def __str__(self):
        return self.__class__.__name__ + "(estimator=" + str(self.estimator) + ")"

    def __repr__(self):
        return self.__str__()
