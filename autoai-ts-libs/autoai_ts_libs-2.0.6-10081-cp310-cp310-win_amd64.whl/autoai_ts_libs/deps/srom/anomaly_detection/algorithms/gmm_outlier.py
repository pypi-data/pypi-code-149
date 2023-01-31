# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: gmm_outlier
   :synopsis: Gaussian mixture model with quick algorithm.

.. moduleauthor:: SROM Team
"""

import numpy as np
from scipy.optimize import minimize_scalar
from sklearn.mixture import GaussianMixture
from sklearn.utils.validation import check_is_fitted, check_array, FLOAT_DTYPES

from scipy.stats import gaussian_kde


class GMMOutlier(GaussianMixture):
    """
    Anomaly class based on Gaussian mixture model.        
    """

    def __init__(
        self,
        threshold=0.99,
        method="quantile",
        n_components=1,
        covariance_type="full",
        tol=1e-3,
        reg_covar=1e-6,
        max_iter=100,
        n_init=1,
        init_params="kmeans",
        weights_init=None,
        means_init=None,
        precisions_init=None,
        random_state=None,
        warm_start=False,
        verbose=0,
        verbose_interval=10,
    ):
        """
        Parameters:
            threshold : Threshold for anomaly,
            method: Method can be "quantile" or "stddev",
            n_components : Number of compoments for gmm,
            covariance_type : Covariance_type for gmm,
            tol : The convergence threshold. EM iterations will stop when the lower bound average gain on the likelihood (of the training data with respect to the model) is below this threshold.,
            reg_covar : Non-negative regularization added to the diagonal of covariance. Allows to assure that the covariance matrices are all positive.,
            max_iter : The number of EM iterations to perform.,
            n_init : The number of initializations to perform. The result with the highest lower bound value on the likelihood is kept.,
            init_params : The method used to initialize the weights, the means and the covariances,
            weight_concentration_prior_type : String describing the type of the weight concentration prior,
            weight_concentration_prior : The dirichlet concentration of each component on the weight distribution (Dirichlet),
            mean_precision_prior : The precision prior on the mean distribution (Gaussian).,
            mean_prior : The prior on the mean distribution (Gaussian). ,
            degrees_of_freedom_prior : The prior of the number of degrees of freedom on the covariance distributions (Wishart).,
            covariance_prior : The prior on the covariance distribution (Wishart). ,
            random_state : Controls the random seed given to the method chosen to initialize the parameter,
            warm_start : If â€˜warm_startâ€™ is True, the solution of the last fitting is used as initialization for the next call of fit().,
            verbose : Enable verbose output.,
            verbose_interval : Number of iteration done before the next print.
        """
        self.threshold = threshold
        self.method = method
        self.random_state = random_state
        self.allowed_methods = ["quantile", "stddev"]
        super(GMMOutlier, self).__init__(
            n_components=n_components,
            covariance_type=covariance_type,
            tol=tol,
            reg_covar=reg_covar,
            max_iter=max_iter,
            n_init=n_init,
            init_params=init_params,
            weights_init=weights_init,
            means_init=means_init,
            precisions_init=precisions_init,
            random_state=random_state,
            warm_start=warm_start,
            verbose=verbose,
            verbose_interval=verbose_interval,
        )

    def fit(self, X, y=None):
        """
        Fit the model using X, y as training data.
        Parameters:
            X: array-like, shape=(n_columns, n_samples,) training data.
            y: ignored but kept in for pipeline support
        Return: 
            Returns an instance of self.
        """

        # GMM sometimes throws an error if you don't do this
        X = check_array(X, estimator=self, dtype=FLOAT_DTYPES)
        if len(X.shape) == 1:
            X = np.expand_dims(X, 1)

        if (self.method == "quantile") and (
            (self.threshold > 1) or (self.threshold < 0)
        ):
            raise ValueError(
                f"Threshold {self.threshold} with method {self.method} needs to be 0 < threshold < 1"
            )
        if (self.method == "stddev") and (self.threshold < 0):
            raise ValueError(
                f"Threshold {self.threshold} with method {self.method} needs to be 0 < threshold "
            )
        if self.method not in self.allowed_methods:
            raise ValueError(
                f"Method not recognised. Method must be in {self.allowed_methods}"
            )

        super(GMMOutlier, self).fit(X)
        score_samples = self.score_samples(X, call_parent=True)

        if self.method == "quantile":
            self.likelihood_threshold_ = np.quantile(score_samples, 1 - self.threshold)

        if self.method == "stddev":
            density = gaussian_kde(score_samples)
            max_x_value = minimize_scalar(lambda x: -density(x)).x
            mean_likelihood = score_samples.mean()
            new_likelihoods = score_samples[score_samples < max_x_value]
            new_likelihoods_std = np.std(new_likelihoods - mean_likelihood)
            self.likelihood_threshold_ = mean_likelihood - (
                self.threshold * new_likelihoods_std
            )

        return self

    def score_samples(self, X, call_parent=False):
        """
        Compute the weighted log probabilities for each sample.
        Parameters:
            X: array-like, shape=(n_columns, n_samples,)data.
        """
        if call_parent:
            return super(GMMOutlier, self).score_samples(X)
        X = check_array(X, estimator=self, dtype=FLOAT_DTYPES)
        check_is_fitted(self, ["likelihood_threshold_"])
        if len(X.shape) == 1:
            X = np.expand_dims(X, 1)

        return -super(GMMOutlier, self).score_samples(X)

    def decision_function(self, X):
        """
        Calculate raw anomaly score.
        Parameters:
            X: array-like, shape=(n_columns, n_samples, ) data.
        """
        # We subtract self.offset_ to make 0 be the threshold value for being an outlier:
        return self.score_samples(X) + self.likelihood_threshold_

    def predict(self, X):
        """
        Predict if a point is an outlier.
        Parameters:
            X: array-like, shape=(n_columns, n_samples, ) training data.
        Rreturn: 
            array, shape=(n_samples,) the predicted data. 1 for inliers, -1 for outliers.
        """
        predictions = (self.decision_function(X) >= 0).astype(int)
        predictions[predictions == 1] = -1
        predictions[predictions == 0] = 1
        return predictions
