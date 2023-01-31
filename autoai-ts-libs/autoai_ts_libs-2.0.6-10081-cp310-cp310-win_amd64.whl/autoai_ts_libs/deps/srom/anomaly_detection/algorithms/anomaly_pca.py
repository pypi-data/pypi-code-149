import numpy as np
from sklearn.decomposition import PCA
from sklearn.utils.validation import check_is_fitted
from sklearn.base import BaseEstimator
from scipy.spatial.distance import cdist


class AnomalyPCA(BaseEstimator):
    """Outlier detector using Principal Component Analysis (PCA).
    Attributes
    ----------
    anomaly_score_ : array-like of shape (n_samples,)
        Anomaly score for each training data.
    contamination_ : float
        Actual proportion of outliers in the data set.
    threshold_ : float
        Threshold.
    """

    def __init__(
        self,
        contamination=0.1,
        iterated_power="auto",
        n_components=None,
        random_state=42,
        svd_solver="auto",
        tol=0.0,
        whiten=False,
        anomaly_score_option="projected_l2",
    ):
        """
            Parameters
            ----------
            contamination : float, default 0.1
                Proportion of outliers in the data set. Used to define the threshold.
            iterated_power : int, default 'auto'
                Number of iterations for the power method computed by svd_solver ==
                'randomized'.
            n_components : int, float, or string, default None
                Number of components to keep.
            random_state : int or RandomState instance, default None
                Seed of the pseudo random number generator.
            svd_solver : string, default 'auto'
                SVD solver to use. Valid solvers are
                ['auto'|'full'|'arpack'|'randomized'].
            tol : float, default 0.0
                Tolerance to declare convergence for singular values computed by
                svd_solver == 'arpack'.
            whiten : bool, default False
                If True, the ``components_`` vectors are multiplied by the square root
                of n_samples and then divided by the singular values to ensure
                uncorrelated outputs with unit component-wise variances.
        """
        self.contamination = contamination
        self.iterated_power = iterated_power
        self.n_components = n_components
        self.random_state = random_state
        self.svd_solver = svd_solver
        self.tol = tol
        self.whiten = whiten
        self.anomaly_score_option = anomaly_score_option

    def _fit(self, X):
        """
            Internal fit method.

            Parameters:
                
        """
        self.estimator_ = PCA(
            iterated_power=self.iterated_power,
            n_components=self.n_components,
            random_state=self.random_state,
            svd_solver=self.svd_solver,
            tol=self.tol,
            whiten=self.whiten,
        ).fit(X)

        return self

    def fit(self, X, y=None):
        """
        Fit the model using X
        Parameters:
            X: array-like, shape=(n_columns, n_samples,) training data.
            y: ignored but kept in for pipeline support.
        Return: 
            Returns an instance of self.
        """
        return self._fit(X)

    def anomaly_score(self, X):
        """Anomaly score

        Args:
            X array-like, shape=(n_columns, n_samples,) training data.

        Returns:
            anomaly score
        """
        if self.anomaly_score_option == "reconstruction":
            return np.sum((X - self._reconstruct(X)) ** 2, axis=1)
        elif self.anomaly_score_option == "log-likelihood":
            return self._log_likelihood(X)
        elif self.anomaly_score_option == "projected_l2":
            return self._projected_l2(X)
        else:
            raise (Exception, "Pass a valid anomaly_score_option")

    def _reconstruct(self, X):
        """Apply dimensionality reduction to the given data, and transform the
        data back to its original space.
        """
        return self.estimator_.inverse_transform(self.estimator_.transform(X))

    def _log_likelihood(self, X):
        """[summary]

        Args:
            X array-like, shape=(n_columns, n_samples,) training data.

        Returns:
            [type]: [description]
        """
        return np.negative(self.estimator_.score_samples(X))

    def _projected_l2(self, X):
        """[summary]

        Args:
            X array-like, shape=(n_columns, n_samples,) training data.
        """
        n_selected_components = self.estimator_.n_components_
        selected_components = self.estimator_.components_[
            -1 * n_selected_components :, :
        ]
        selected_w_components = self.estimator_.explained_variance_ratio_[
            -1 * n_selected_components :
        ]

        return np.sum(
            cdist(X, selected_components, metric="euclidean") / selected_w_components,
            axis=1,
        ).ravel()

    def decision_function(self, X):
        """Predict raw anomaly score of X using the fitted detector.
        """
        return self.anomaly_score(X)
