# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: sparse_structure_learning
   :synopsis: sparse_structure_learning.
   
.. moduleauthor:: SROM Team
"""


import numpy as np
from sklearn.base import BaseEstimator
from sklearn.cluster import affinity_propagation
from sklearn.covariance import GraphicalLasso
from sklearn.utils.validation import check_is_fitted


class SparseStructureLearning(BaseEstimator):
    """Outlier detector using sparse structure learning.
    References
    ----------
    .. [#ide09] Ide, T., Lozano, C., Abe, N., and Liu, Y.,
        "Proximity-based anomaly detection using sparse structure learning,"
        In Proceedings of SDM, pp. 97-108, 2009.
    """

    @property
    def _apcluster_params(self):
        if self.apcluster_params is None:
            return dict()
        else:
            return self.apcluster_params

    @property
    def covariance_(self):
        """array-like of shape (n_features, n_features): Estimated covariance
        matrix.
        """

        return self.estimator_.covariance_

    @property
    def graphical_model_(self):
        """networkx Graph: GGM.
        """

        import networkx as nx

        return nx.from_numpy_matrix(np.tril(self.partial_corrcoef_, k=-1))

    @property
    def isolates_(self):
        """array-like of shape (n_isolates,): Indices of isolates.
        """

        import networkx as nx

        return np.array(list(nx.isolates(self.graphical_model_)))

    @property
    def location_(self):
        """array-like of shape (n_features,): Estimated location.
        """

        return self.estimator_.location_

    @property
    def n_iter_(self):
        """int: Number of iterations run.
        """

        return self.estimator_.n_iter_

    @property
    def partial_corrcoef_(self):
        """array-like of shape (n_features, n_features): Partial correlation
        coefficient matrix.
        """

        n_features, _ = self.precision_.shape
        diag = np.diag(self.precision_)[np.newaxis]
        partial_corrcoef = -self.precision_ / np.sqrt(diag.T @ diag)
        partial_corrcoef.flat[:: n_features + 1] = 1.0

        return partial_corrcoef

    @property
    def precision_(self):
        """array-like of shape (n_features, n_features): Estimated pseudo
        inverse matrix.
        """

        return self.estimator_.precision_

    def __init__(
        self,
        alpha=0.01,
        assume_centered=False,
        contamination=0.1,
        enet_tol=1e-04,
        max_iter=100,
        mode="cd",
        tol=1e-04,
        apcluster_params=None,
    ):
        """
        Parameters
            ----------
            alpha : float, default 0.01
                Regularization parameter.
            assume_centered : bool, default False
                If True, data are not centered before computation.
            contamination : float, default 0.1
                Proportion of outliers in the data set. Used to define the threshold.
            enet_tol : float, default 1e-04
                Tolerance for the elastic net solver used to calculate the descent
                direction. This parameter controls the accuracy of the search direction
                for a given column update, not of the overall parameter estimate. Only
                used for mode='cd'.
            max_iter : integer, default 100
                Maximum number of iterations.
            mode : str, default 'cd'
                Lasso solver to use: coordinate descent or LARS.
            tol : float, default 1e-04
                Tolerance to declare convergence.
            apcluster_params : dict, default None
                Additional parameters passed to
                ``sklearn.cluster.affinity_propagation``.
            Attributes
            ----------
            anomaly_score_ : array-like of shape (n_samples,)
                Anomaly score for each training data.
            contamination_ : float
                Actual proportion of outliers in the data set.
            threshold_ : float
                Threshold.
            labels_ : array-like of shape (n_features,)
                Label of each feature.
        """
        self.alpha = alpha
        self.apcluster_params = apcluster_params
        self.assume_centered = assume_centered
        self.contamination = contamination
        self.enet_tol = enet_tol
        self.max_iter = max_iter
        self.mode = mode
        self.tol = tol
        self._estimator_type = "classifier"

    def _check_is_fitted(self):
        """
            Interanl method work as a helper function.
        """
        super()._check_is_fitted()

        check_is_fitted(
            self,
            [
                "covariance_",
                "labels_",
                "location_",
                "n_iter_",
                "partial_corrcoef_",
                "precision_",
            ],
        )

    def fit(self, X):
        """
        Fit estimator.
        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            
        Returns:
            self: Trained instance of SampleSVDD.
        """
        self.estimator_ = GraphicalLasso(
            alpha=self.alpha,
            assume_centered=self.assume_centered,
            enet_tol=self.enet_tol,
            max_iter=self.max_iter,
            mode=self.mode,
            tol=self.tol,
        ).fit(X)

        _, self.labels_ = affinity_propagation(
            self.partial_corrcoef_, **self._apcluster_params
        )

        return self

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """
        return self.estimator_.mahalanobis(X)

    def featurewise_anomaly_score(self, X):
        """Compute the feature-wise anomaly scores for each sample.
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Data.
        Returns
        -------
        anomaly_score : array-like of shape (n_samples, n_features)
            Feature-wise anomaly scores for each sample.
        """

        return (
            0.5 * np.log(2.0 * np.pi / np.diag(self.precision_))
            + 0.5
            / np.diag(self.precision_)
            * ((X - self.location_) @ self.precision_) ** 2
        )

