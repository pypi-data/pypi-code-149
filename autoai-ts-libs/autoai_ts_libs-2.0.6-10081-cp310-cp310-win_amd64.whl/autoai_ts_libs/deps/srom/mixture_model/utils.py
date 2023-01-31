# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.mixture import GaussianMixture, BayesianGaussianMixture
from autoai_ts_libs.deps.srom.data_sampling.unsupervised.random_sampler import DataSampler
from sklearn.mixture._gaussian_mixture import (
    _compute_precision_cholesky,
    _estimate_gaussian_parameters,
)
from autoai_ts_libs.deps.srom.utils.no_op import NoOp
import time


class GMMPipeline(Pipeline):
    """
    This pipeline differs in the sense sklearn does not support fit_predict
    based class. The idea presented in score function will come here in a form
    of fit method
    """

    def __init__(self, steps, *, memory=None, verbose=False, scoring='bic'):
        self.steps = steps
        self.memory = memory
        self.verbose = verbose
        self.scoring=scoring

    def _forward_fit_data_transformation(self, X, y=None):
        """_summary_

        Args:
            X (_type_): _description_
            y (_type_, optional): _description_. Defaults to None.

        Raises:
            Exception: _description_
            Exception: _description_
            Exception: _description_

        Returns:
            _type_: _description_
        """

        Xt = X
        yt = y
        step_pos = 0
        for _, transformer in self.steps[:-1]:
            if step_pos == self.cluster_step_:
                # a special need
                lbl = transformer.fit_predict(Xt, yt)
                self._set_parameter_post_clustering(Xt, lbl)
                res = (Xt, yt)     
            elif hasattr(transformer, "fit_transform"):
                res = transformer.fit_transform(Xt, yt)
            else:
                res = transformer.fit(Xt, yt).transform(Xt)

            if isinstance(res, tuple):
                x_res = res[0]
                yt = res[1]
            else:
                x_res = res

            Xt = x_res
            step_pos += 1
        return Xt, yt
    
    def _forward_data_transformation(self, X, y=None):
        Xt = X
        yt = y
        step_pos = 0
        for _, transformer in self.steps[:-1]:
            if step_pos == self.cluster_step_ or isinstance(transformer, DataSampler):
                res = (Xt, yt)
            else:
                res = transformer.transform(Xt)

            if isinstance(res, tuple):
                x_res = res[0]
                yt = res[1]
            else:
                x_res = res

            Xt = x_res
            step_pos += 1
        return Xt, yt
    
    def _n_parameters(self, X):
        """Return the number of free parameters in the model."""
        _, n_features = self.steps[-1][1].means_.shape
        # Number of effective components equals the number of unique labels
        n_effect_comp = len(np.unique(self.steps[-1][1].predict(X)))
        if self.steps[-1][1].covariance_type == 'full':
            cov_params = n_effect_comp * n_features * (n_features + 1) / 2.
        elif self.steps[-1][1].covariance_type == 'diag':
            cov_params = n_effect_comp * n_features
        elif self.steps[-1][1].covariance_type == 'tied':
            cov_params = n_features * (n_features + 1) / 2.
        elif self.steps[-1][1].covariance_type == 'spherical':
            cov_params = n_effect_comp
        mean_params = n_features * n_effect_comp
        return int(cov_params + mean_params + n_effect_comp - 1)

    def bic(self, X):
        """Bayesian information criterion for the current model on the input X.
        Parameters
        ----------
        X : array of shape (n_samples, n_dimensions)
        Returns
        -------
        bic : float
            The lower the better.
        """
        return (-2 * self.steps[-1][1].score(X) * X.shape[0] +
                self._n_parameters(X) * np.log(X.shape[0]))

    def aic(self, X):
        """Akaike information criterion for the current model on the input X.
        Parameters
        ----------
        X : array of shape (n_samples, n_dimensions)
        Returns
        -------
        aic : float
            The lower the better.
        """
        return -2 * self.steps[-1][1].score(X) * X.shape[0] + 2 * self._n_parameters(X)

    def _set_steps_for_fit(self):
        # check 1
        if (not isinstance(self.steps[-1][1], GaussianMixture)) and (not isinstance(self.steps[-1][1], BayesianGaussianMixture)):
            raise Exception("Only GaussianMixture or BayesianGaussianMixture is supported")
        
        # check 2
        self.cluster_step_ = -1
        for step_index, step in enumerate(self.steps[:-1]):
            if getattr(step[1], "_estimator_type", None) == 'clusterer' and 'n_clusters' in step[1].get_params():
                step[1].n_clusters = self.steps[-1][1].n_components
                self.cluster_step_ = step_index

    def _set_parameter_post_clustering(self, X, lbl):
        weights, means, precisions = self._get_initial_parameter(
            X, lbl, self.steps[-1][1].covariance_type
        )
        self.steps[-1][1].weights_init = weights
        self.steps[-1][1].means_init = means
        self.steps[-1][1].precision_init = precisions

    def fit(self, X, y=None, **fit_params):
        """
        fit the GMM pipeline
        """
        self._set_steps_for_fit()
        Xt, yt = self._forward_fit_data_transformation(X, y)
        self.steps[-1][1].fit(Xt, yt)
        return self

    def predict(self, X, **predict_params):
        Xt, _ = self._forward_data_transformation(X)
        return self.steps[-1][1].predict(Xt)
    
    def _get_initial_parameter(self, X, lbl, cov_type):
        n = len(lbl)
        k = max(lbl) + 1
        onehot = np.zeros([n, k])
        onehot[np.arange(n), lbl] = 1
        weights, means, covariances = _estimate_gaussian_parameters(
            X, onehot, 1e-06, cov_type
        )
        weights /= n
        precisions_cholesky_ = _compute_precision_cholesky(covariances, cov_type)

        if cov_type == "tied":
            c = precisions_cholesky_
            precisions = np.dot(c, c.T)
        elif cov_type == "diag":
            precisions = precisions_cholesky_
        else:
            precisions = [np.dot(c, c.T) for c in precisions_cholesky_]

        return weights, means, precisions

    def score(self, X, y=None, sample_weight=None, score_option=None):
        """
        Similar to `score` method in sklearn.pipeline.Pipeline.
        The input and return params of the transformers have been modified
        to incorporate X and y transformation.

        Parameters
        ----------
            X : {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
                they are supported by the base estimator.
            y : array-like of shape (n_samples,)
                The target values (class labels in classification, real numbers in
                regression).
            sample_weight : array-like of shape (n_samples,), default=None
                Sample weights. If None, then samples are equally weighted.
                Note that this is supported only if the base estimator supports
                sample weighting.
        Returns
        -------
            score : float
        """

        if score_option is None:
            score_option = self.scoring

        # this is for this pipeline
        Xt, _ = self._forward_data_transformation(X)
        if score_option == "bic":
            try:
                return self.steps[-1][1].bic(Xt) * -1.0
            except:
                return self.bic(Xt) * -1.0
        elif score_option == "aic":
            try:
                return self.steps[-1][1].aic(Xt) * -1.0
            except:
                return self.aic(Xt) * -1.0
        else:
            return np.NAN

    def _check_pure_sklearn_pipeline(self):
        """
        """
        for _steps in self.steps:
            if not _steps[1].__module__.startswith('sklearn'):
                return False
        return True
        
    def _export_sklearn_pipeline(self):
        """
        """
        if self._check_pure_sklearn_pipeline():
            return Pipeline(steps=self.steps)
        else:
            return False
        
    def export_to_onnx(self, X, score_samples=True):
        """
        Export capability
        """
        try:
            from mlprodict.onnx_conv import to_onnx
            ppl = self._export_sklearn_pipeline()
            if ppl:
                return to_onnx(ppl, X[:1], options={id(ppl.steps[-1][0]): {'score_samples': score_samples}})
            else:
                print ('pipeline has custom component that is not from sklearn')
        except Exception as ex:
            print (ex)

def GMM_score(
    clf, X, y=None, groups=None, cv=None, scoring="bic", return_train_score=False
):

    scores = {}
    scores["test_score"] = []
    scores["score_time"] = []
    scores["fit_time"] = []

    if isinstance(clf, Pipeline):
        # given clf is an sklearn pipeline
        if isinstance(clf.steps[-1][1], GaussianMixture):
            start_time = time.time()
            clf.fit(X)
            fit_time = time.time() - start_time
            scores["fit_time"].append(fit_time)
            if scoring == "bic":
                start_time = time.time()
                scores["test_score"].append(clf.steps[-1][1].bic(X) * -1.0)
                score_time = time.time() - start_time
                scores["score_time"].append(score_time)
            elif scoring == "aic":
                start_time = time.time()
                scores["test_score"].append(clf.steps[-1][1].aic(X) * -1.0)
                score_time = time.time() - start_time
                scores["score_time"].append(score_time)
            else:
                pass

    return scores
