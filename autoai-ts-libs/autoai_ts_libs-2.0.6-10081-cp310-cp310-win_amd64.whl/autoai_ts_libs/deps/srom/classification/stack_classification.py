# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: Stack Classification
   :synopsis: Contains StackClassifier class.

.. moduleauthor:: SROM Team
"""
import warnings
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.base import clone
import scipy.sparse as sparse

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


class StackClassifier(BaseEstimator, ClassifierMixin):
    """
    The stack classification for scikit-learn estimators for classifation. \

    """

    def __init__(
        self,
        base_models,
        meta_model,
        use_meta_features_only=True,
        use_probas=True,
        average_probas=False,
        refit=True,
    ):
        """
            Parameters:
            base_model (list of pipelines): This list contains a set of top-k performing pipeline.
            meta model (model) : this is also a model
            use_meta_features_only (boolean) : True or False
            use_probas (boolean) : True or False
            refit (boolean) : True or False
        """
        self.base_models = base_models
        self.meta_model = meta_model
        self.use_meta_features_only = use_meta_features_only
        self.use_probas = use_probas
        self.average_probas = average_probas
        self.refit = refit

    def fit(self, X, y):
        """
        fitting model
        """

        if self.refit:
            self.base_models_ = clone(self.base_models)
            self.meta_model_ = clone(self.meta_model)
        else:
            self.base_models_ = self.base_models
            self.meta_model_ = self.meta_model

        for regr in self.base_models_:
            regr.fit(X, y)

        _meta_features = self._generate_meta_features(X)

        if not self.use_meta_features_only:
            pass
        elif sparse.issparse(X):
            _meta_features = sparse.hstack((X, _meta_features))
        else:
            _meta_features = np.hstack((X, _meta_features))

        self.meta_model_.fit(_meta_features, y)

        return self

    def _generate_meta_features(self, X):
        """
        Generate meta features.

        Parameters:
            X (pandas dataframe/matrix, required): Input Data (Only limited to binary data).
        Returns:
            vals
        """
        if self.use_probas:
            probas = np.asarray(
                [bs_mdl.predict_proba(X) for bs_mdl in self.base_models_]
            )
            if self.average_probas:
                vals = np.average(probas, axis=0)
            else:
                vals = np.concatenate(probas, axis=1)
        else:
            vals = np.column_stack([bs_mdl.predict(X) for bs_mdl in self.base_models_])
        return vals

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
        _meta_features = self._generate_meta_features(X)
        if not self.use_meta_features_only:
            pass
        elif sparse.issparse(X):
            _meta_features = sparse.hstack((X, _meta_features))
        else:
            _meta_features = np.hstack((X, _meta_features))
        return self.meta_model_.predict(_meta_features)

    def predict_proba(self, X):
        """
        Predict the class probabilites.
        
        Parameters:
            X (pandas dataframe or numpy array): Input samples to be used for prediction.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].
        """
        _meta_features = self._generate_meta_features(X)
        if not self.use_meta_features_only:
            pass
        elif sparse.issparse(X):
            _meta_features = sparse.hstack((X, _meta_features))
        else:
            _meta_features = np.hstack((X, _meta_features))
        return self.meta_model_.predict_proba(_meta_features)
