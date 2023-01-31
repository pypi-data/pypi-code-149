# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
    .. module:: deep_isolation_forest
       :synopsis: DeepIsolationForest class.

    .. moduleauthor:: SROM Team
"""

import numpy as np
from sklearn.utils import check_array
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import initializers
from sklearn.utils.validation import check_is_fitted
from sklearn.base import BaseEstimator

class DeepIsolationForest(BaseEstimator):
    """_summary_
    """
    def __init__(
        self,
        network=None,
        n_ensemble=50,
        n_estimators=6,
        max_samples=256,
        n_jobs=1,
        random_state=42,
        n_processes=15,
        batch_size=10000,
        device="cuda",
        verbose=1,
        **network_args,
    ):
        """
            Init method
        """
        self.n_ensemble = n_ensemble
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.n_jobs = n_jobs
        self.random_state = random_state
        self.n_processes = n_processes
        self.batch_size = batch_size
        self.device = device
        self.network_args = network_args
        self.verbose = verbose
    
    def _pre_fit(self):
        """_summary_
        """
        self.net_lst_ = []
        self.iForest_lst_ = []
        self.x_reduced_lst_ = []
        self.score_lst_ = []
        self.decision_scores_ = None
        if self.random_state is not None:
            np.random.seed(self.random_state)

    def fit(self, X, y=None):
        """
        Fit detector. y is ignored in unsupervised methods.
        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The input samples.
        y : Ignored
            Not used, present for API consistency by convention.
        Returns
        -------
        self : object
            Fitted estimator.
        """
        self._pre_fit()
        n_features = X.shape[-1]
        ensemble_seeds = np.random.randint(0, 100000, self.n_ensemble)
        
        # for each ensemble
        for i in range(self.n_ensemble):
            x_tensor = tf.convert_to_tensor(X)
            tf.random.set_seed(ensemble_seeds[i])
            model = keras.Sequential(
                [
                    layers.Dense(20, 
                                activation=None, 
                                name="layer1",
                                use_bias=False,
                                kernel_initializer=initializers.RandomNormal(mean=0.0, stddev=1.0, seed=4),),
                ]
            )
            x_reduced = model(x_tensor).numpy()

            ss = StandardScaler()
            x_reduced = ss.fit_transform(x_reduced)
            x_reduced = np.tanh(x_reduced)

            self.x_reduced_lst_.append(x_reduced)
            self.net_lst_.append(model)
            self.iForest_lst_.append(
                IsolationForest(
                    n_estimators=self.n_estimators,
                    max_samples=self.max_samples,
                    n_jobs=self.n_jobs,
                    random_state=ensemble_seeds[i],
                )
            )
            self.iForest_lst_[i].fit(x_reduced)

        return self

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector.
        The anomaly score of an input sample is computed based on different
        detector algorithms. For consistency, outliers are assigned with
        larger anomaly scores.
        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The training input samples. Sparse matrices are accepted only
            if they are supported by the base estimator.
        Returns
        -------
        anomaly_scores : numpy array of shape (n_samples,)
            The anomaly score of the input samples.
        """
        x_reduced_lst = []
        for i in range(self.n_ensemble):
            x_reduced = self.net_lst_[i](
                tf.convert_to_tensor(X)
            ).numpy()
            ss = StandardScaler()
            x_reduced = ss.fit_transform(x_reduced)
            x_reduced = np.tanh(x_reduced)
            x_reduced_lst.append(x_reduced)
            
        n_samples = x_reduced_lst[0].shape[0]
        self.score_lst = np.zeros([self.n_ensemble, n_samples])
        for i in range(self.n_ensemble):
            scores = self.iForest_lst_[i].decision_function(x_reduced_lst[i])
            self.score_lst[i] = scores
        final_scores = np.average(self.score_lst, axis=0)
        return final_scores

    def predict(self, X):
        """
        Predict if a particular sample is an outlier or not.
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The input samples. Internally, it will be converted to
            ``dtype=np.float32`` and if a sparse matrix is provided
            to a sparse ``csr_matrix``.
        Returns
        -------
        is_inlier : ndarray of shape (n_samples,)
            For each observation, tells whether or not (+1 or -1) it should
            be considered as an inlier according to the fitted model.
        """
        check_is_fitted(self)
        decision_func = self.decision_function(X)
        is_inlier = np.ones_like(decision_func, dtype=int)
        is_inlier[decision_func < 0] = -1
        return is_inlier
