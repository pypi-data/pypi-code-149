import numpy as np
from sklearn.base import BaseEstimator
from sklearn.utils.validation import check_is_fitted
from sklearn.neighbors import KernelDensity

"""
.. module:: kde
   :synopsis: kde.
   
.. moduleauthor:: SROM Team
"""

class KDE(BaseEstimator):
    """Outlier detector using Kernel Density Estimation (KDE).
    References
    ----------
    .. [#parzen62] Parzen, E.,
        "On estimation of a probability density function and mode,"
        Ann. Math. Statist., 33(3), pp. 1065-1076, 1962.
    """

    def __init__(
        self,
        algorithm="auto",
        atol=0.0,
        bandwidth=1.0,
        breadth_first=True,
        contamination=0.1,
        kernel="gaussian",
        leaf_size=40,
        metric="euclidean",
        rtol=0.0,
        metric_params=None,
    ):
        """
        Parameters
        ----------
            algorithm : str, default 'auto'
                Tree algorithm to use. Valid algorithms are
                ['kd_tree'|'ball_tree'|'auto'].
            atol : float, default 0.0
                Desired absolute tolerance of the result.
            bandwidth : float, default 1.0
                Bandwidth of the kernel.
            breadth_first : bool, default True
                If true, use a breadth-first approach to the problem. Otherwise use a
                depth-first approach.
            contamination : float, default 0.1
                Proportion of outliers in the data set. Used to define the threshold.
            kernel : str, default 'gaussian'
                Kernel to use. Valid kernels are
                ['gaussian'|'tophat'|'epanechnikov'|'exponential'|'linear'|'cosine'].
            leaf_size : int, default 40
                Leaf size of the underlying tree.
            metric : str, default 'euclidean'
                Distance metric to use.
            rtol : float, default 0.0
                Desired relative tolerance of the result.
            metric_params : dict, default None
                Additional parameters to be passed to the requested metric.
        Attributes
        ----------
            anomaly_score_ : array-like of shape (n_samples,)
                Anomaly score for each training data.
            contamination_ : float
                Actual proportion of outliers in the data set.
            threshold_ : float
                Threshold.
        """
        self.algorithm = algorithm
        self.atol = atol
        self.bandwidth = bandwidth
        self.breadth_first = breadth_first
        self.contamination = contamination
        self.kernel = kernel
        self.leaf_size = leaf_size
        self.metric = metric
        self.rtol = rtol
        self.metric_params = metric_params

    def _auto_discover_bandwidth(self, X):
        """
            Internal method as a helper method
        """
        from sklearn.model_selection import GridSearchCV
        from sklearn.model_selection import KFold

        bandwidths = np.linspace(0, 2, 10)
        # create a new KernelDensity
        grid = GridSearchCV(KernelDensity(
            algorithm=self.algorithm,
            atol=self.atol,
            breadth_first=self.breadth_first,
            kernel=self.kernel,
            leaf_size=self.leaf_size,
            metric=self.metric,
            rtol=self.rtol,
            metric_params=self.metric_params,
            ),
            {'bandwidth': bandwidths},
            cv=KFold(3))
        grid.fit(X)
        self.bandwidth_ = grid.best_params_['bandwidth']
        print (self.bandwidth_)

    def fit(self, X):
        """
        Fit estimator.

        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of \
                shape:(n_samples, n_features) \
                Set of samples, where n_samples is the number of samples \
                and n_features is the number of features.
        """
        if self.bandwidth == 'auto':
            self._auto_discover_bandwidth(X)
        else:
            self.bandwidth_ = self.bandwidth
        
        self.estimator_ = KernelDensity(
            algorithm=self.algorithm,
            atol=self.atol,
            bandwidth=self.bandwidth_,
            breadth_first=self.breadth_first,
            kernel=self.kernel,
            leaf_size=self.leaf_size,
            metric=self.metric,
            rtol=self.rtol,
            metric_params=self.metric_params,
        ).fit(X)

        return self

    def anomaly_score(self, X):
        """
        Calculates anomaly scores for given input samples.

        Paramters:
            X (pandas dataframe or numpy array, required): Input samples.
            
        Returns:
             Anomaly scores.
        """
        return -self.estimator_.score_samples(X)
