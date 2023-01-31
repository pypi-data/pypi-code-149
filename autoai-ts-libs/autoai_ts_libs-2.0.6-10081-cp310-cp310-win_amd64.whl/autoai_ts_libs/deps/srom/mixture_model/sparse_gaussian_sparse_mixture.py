# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
SparseGaussianSparseMixture
"""
import time
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.cluster import KMeans

from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_graph_lasso import AnomalyGraphLasso
from .sparse_gaussian_sparse_mixture_utils import (
    log_gmm_likelihood,
    log_gauss_likelihood,
    softmax,
    l0_weights,
    srom_graph_lasso_method,
)


class SparseGaussianSparseMixture(BaseEstimator, TransformerMixin):
    """
    Iterative variational approach to estimating a sparse mixture of sparse graphical models for
    multiple tasks

    TODO: condition to check
    1. n_components cannot be less than zero
    2. assets id should not be a part of features
    3. all the values in input except asset id should be numerical entry
        (possible string and etc shd be flagged as error)
    """

    def __init__(
        self,
        base_learner=AnomalyGraphLasso(alpha=0.5),
        n_components=1,
        asset_id=None,
        features=None,
        tol=1e-5,
        max_iter=1000,
        eps=1e-4,
        tau=0.1,
        rho=0.05,
        N_min=0.1,
        beta0=1.0,
        m0=None,
        mean_estimation="point",
        weight_update="graph_lasso",
        random_state=None,
        init_params="uniform",
        randomize_samples=False,
        common_dictionary=True,
        adaptive_graph_lasso=False,
        verbose=0,
    ):
        """
        Args:
            base_learner (object, required): Covariance estimator instance to be used for initialization
            n_components (integer, required): number of components in the mixture model
            asset_id (String, optional): string containing name of column that contains asset id
                if not provided, all samples are assumed to be from the same asset
            features (list, optional): Default value([])
                list of columns to be used to build the mixture model
                if not provided, all columns are used as features (except asset_id)
            eps (float): parameter defining epsilon sparsity of mixture weights
            tau (float): l0 regularization parameter in mixture weight estimation
            rho (float): l1 regularization parameter for graphical lasso precision estimation
                (But what if skggm need another parameters)
            N_min (float): stability for l1 regularization when cluster membership is very small
            beta0 (float): precision matrix multiplier for prior on cluster means
            m0 (float): mean for cluster means prior
            mean_estimation (string): 'posterior' or 'point', decide whether or not to infer means
                using posterior
            init_params (string): 'uniform' or 'kmeans', initialize cluster means by either
                uniformly grouping the samples into clusters and computing the means or by
                running the KMeans algorithm
            max_iter (integer): number of iterations to run fitting procedure
            tol (float): convergence criterion. If relative decrease in log likelihood is smaller than this amount
                the fitting procedure will terminate
            common_dictionary (boolean): True or False. If True, we will initialize a common dictionary
                when fitting multiple assets, else n_components clusters will be initialized for each asset.
            weight_update (string): 'graph_lasso' or 'quic', method to use for graphical lasso, sklearn vs skggm
            randomize_samples (boolean): True or False. Permute samples for initialization
            adaptive_graph_lasso (boolean): True or False. Use a schedule for the rho parameter provided, based on the
                cluster membership estimate at each iteration

        Attributes:
            weights_ : numpy n_tasks x n_components array of mixture probabilities for each task
            means_ : numpy n_components x n_features array of cluster means
            precisions_ : numpy n_components x n_features x n_features array of cluster precisions
            betas_ : numpy n_components length array of precision matrix multipliers for
            cluster means posteriors
            train_likelihood
            num_iters : number of iterations it took to converge
        """
        if features is None:
            self.features = []
        else:
            self.features = features
        self.base_learner = base_learner
        self.n_components, self.asset_id = n_components, asset_id
        self.max_iter, self.init_params, self.verbose = max_iter, init_params, verbose
        self.tol, self.eps, self.tau, self.rho, self.N_min = tol, eps, tau, rho, N_min
        self.beta0, self.m0, self.mean_estimation = beta0, m0, mean_estimation
        self.weight_update = weight_update
        self.common_dictionary = common_dictionary
        self.randomize_samples = randomize_samples
        self.adaptive_graph_lasso = adaptive_graph_lasso

        if self.mean_estimation not in ["posterior", "point"]:
            self.mean_estimation = "point"

        self.means_ = None
        self.precisions_ = None
        self.weights_ = None
        self.betas_ = None
        self.num_iters = None
        self.train_likelihood = None
        self.assets = None
        self.task_sample_count = None
        self.n_tasks = None

    # Need to check wether passing extra parameter in fit is allowed or it should be initialized
    # inside the __init__
    # i noticed almost all the method has a parameter name
    # "task_sample_count" (): this is not good if we are passing same value multiple times
    def fit(self, X_df):
        """
        Args:
            X_df (pandas dataframe): pandas dataframe with data from one or more assets
        Returns: an instance of SparseGaussianSparseMixture
        Raises:
            Exception: If input dataset is not pandas dataframe
        """
        if not isinstance(X_df, pd.DataFrame):
            raise Exception("Inout to fit must be a dataframe")

        X = self._process_dataframe(X_df, train=True)
        n_samples = X.shape[0]
        self.n_samples = n_samples
        self.n_features = X.shape[1]

        # initialize means and mixture probabilities
        self._init_means_precisions(X)
        if True in np.isnan(self.means_) or True in np.isnan(self.precisions_):
            self.means_, self.precisions_ = (
                np.nan_to_num(self.means_),
                np.nan_to_num(self.precisions_),
            )
        self.weights_ = (
            1. / self.n_components * np.ones((self.n_tasks, self.n_components))
        )
        self.betas_ = (self.beta0 + n_samples / float(self.n_components)) * np.ones(
            self.n_components
        )

        loglikelihoods = np.zeros(self.max_iter)
        train_likelihood = 0
        # Run VB iterative equations until convergence
        for i in range(self.max_iter):
            t = time.time()
            r = self._update_cluster_assignments(X)
            for s in range(self.n_tasks):
                c_s = np.mean(r[s], 0)
                self.weights_[s, :] = l0_weights(c_s, tau=self.tau, eps=self.eps)

            self._update_means_precisions(X, r)

            loglikelihoods[i] = self._compute_likelihood(X, r)
            secs = time.time() - t
            if self.verbose != 0:
                print("iter: %d, likelihood: %.4f" % (i, loglikelihoods[i]))
                print("time taken: %.3f" % (secs,))
            if (i > 0) and (
                abs(loglikelihoods[i] - loglikelihoods[i - 1])
                / max(abs(loglikelihoods[i - 1]), 1)
                < self.tol
            ):
                train_likelihood = loglikelihoods[i]
                break
        self.num_iters = i + 1
        self.train_likelihood = train_likelihood

        return self

    def _process_dataframe(self, X_df, train=True):
        if self.asset_id is None:
            task_sample_count = [X_df.shape[0]]
            assets = ["asset_1"]
            if not self.features:
                self.features = list(X_df.columns)
            X = X_df.loc[:, self.features].values
            X_index = list(X_df.index)
        else:
            if not self.features:
                self.features = list(X_df.columns)
                self.features.remove(self.asset_id)

            assets, task_sample_count, X, X_index = [], [], [], []
            for name, grp in X_df.groupby(self.asset_id):
                X.append(grp.loc[:, self.features].values)
                X_index.extend(list(grp.index))
                assets.append(name)
                task_sample_count.append(grp.shape[0])
            X = np.vstack(X)
        if train:
            self.assets = assets
            self.task_sample_count = task_sample_count
            self.n_tasks = len(self.task_sample_count)
            if not self.common_dictionary:
                self.n_components = self.n_tasks * self.n_components
            return X
        else:
            return X, assets, task_sample_count, X_index

    def _get_precision_matrix_from_base_learner(self, X):
        self.base_learner.fit(X)
        return self.base_learner.precision_

    def _init_means_precisions(self, X):
        n_samples, n_features = X.shape

        if not self.task_sample_count:
            self.task_sample_count = [n_samples]

        self.means_ = np.zeros((self.n_components, n_features))
        self.precisions_ = np.zeros((self.n_components, n_features, n_features))

        if self.common_dictionary:
            if self.init_params == "kmeans":
                kmeans = KMeans(self.n_components).fit(X)
                self.means_ = kmeans.cluster_centers_
            elif self.init_params == "uniform":
                W = int(n_samples / self.n_components)
            else:
                print("Unrecognized initialization option, defaulting to uniform")
                W = int(n_samples / self.n_components)

            if self.randomize_samples:
                shuffle_idx = np.random.permutation(n_samples)
            else:
                shuffle_idx = np.arange(n_samples)
            for k in range(self.n_components):
                if self.init_params == "kmeans":
                    Xsub = X[np.where(kmeans.labels_ == k)[0], :]
                else:
                    Xsub = X[shuffle_idx[W * k : W * (k + 1)], :]
                    self.means_[k, :] = np.mean(Xsub, 0)

                k_precision = self._get_precision_matrix_from_base_learner(Xsub)
                self.precisions_[k, :, :] = k_precision
        else:
            n_components_per_task = int(self.n_components / self.n_tasks)
            for s in range(self.n_tasks):
                N_s = self.task_sample_count[s]
                N_base = sum(self.task_sample_count[:s])
                X_s = X[N_base : N_base + N_s, :]

                if self.init_params == "kmeans":
                    kmeans = KMeans(n_components_per_task).fit(X_s)
                    self.means_[
                        s * n_components_per_task : (s + 1) * n_components_per_task, :
                    ] = kmeans.cluster_centers_
                elif self.init_params == "uniform":
                    W = int(N_s / n_components_per_task)
                else:
                    print("Unrecognized initialization option, defaulting to uniform")
                    W = int(N_s / n_components_per_task)

                for k in range(n_components_per_task):
                    if self.init_params == "kmeans":
                        Xsub = X_s[np.where(kmeans.labels_ == k)[0], :]
                    else:
                        Xsub = X_s[W * k : W * (k + 1), :]
                        self.means_[s * n_components_per_task + k, :] = np.mean(Xsub, 0)

                    k_precision = self._get_precision_matrix_from_base_learner(Xsub)
                    self.precisions_[s * n_components_per_task + k, :, :] = k_precision

    def _update_cluster_assignments(self, X):
        r = []
        _, n_features = X.shape

        for s in range(self.n_tasks):
            N_s = self.task_sample_count[s]
            r_s = np.zeros((N_s, self.n_components))
            N_base = sum(self.task_sample_count[:s])
            r_s = log_gmm_likelihood(
                X[N_base : N_base + N_s, :], self.means_, self.precisions_
            ) + np.outer(np.ones(N_s), np.log(self.weights_[s, :] + 1e-100))
            if self.mean_estimation == "posterior":
                r_s -= 0.5 * n_features * np.outer(np.ones(N_s), 1. / self.betas_)
            r_s = softmax(r_s)
            r.append(r_s)
        return r

    def _update_means_precisions(self, X, r):
        n_samples, n_features = X.shape

        R = np.vstack(r)
        cluster_membership_estimate = np.sum(R, 0)
        cluster_weighted_means = np.zeros((self.n_components, n_features))
        means = np.zeros((self.n_components, n_features))
        precisions = np.zeros((self.n_components, n_features, n_features))

        no_update = np.where(np.sum(R, 0) < 1e-100)[0]
        update = np.where(np.sum(R, 0) >= 1e-100)[0]

        for k in range(self.n_components):
            if np.sum(R[:, k]) >= 1e-100:
                cluster_weighted_means[k, :] = np.average(X, axis=0, weights=R[:, k])

        self.betas_ = self.beta0 + cluster_membership_estimate
        if self.m0 is None:
            m0 = np.zeros((1, n_features))
        else:
            m0 = self.m0

        if self.mean_estimation == "posterior":
            new_means = (
                np.outer(self.beta0 / self.betas_, m0)
                + (cluster_membership_estimate / self.betas_)[:, None]
                * cluster_weighted_means
            )
        else:
            new_means = cluster_weighted_means

        means[no_update, :] = np.copy(self.means_[no_update, :])
        means[update, :] = np.copy(new_means[update, :])
        precisions[no_update, :] = np.copy(self.precisions_[no_update, :])

        for k in update:
            if self.mean_estimation == "posterior":
                B_k = R[:, k][:, None] * X
                Sigma_k = np.dot(B_k.T, X) / cluster_membership_estimate[k]
                Sigma_k -= np.outer(
                    cluster_weighted_means[k, :], cluster_weighted_means[k, :]
                )
                Q_k = Sigma_k + (self.beta0 / self.betas_[k]) * np.outer(
                    cluster_weighted_means[k, :] - m0, cluster_weighted_means[k, :] - m0
                )
            else:
                Q_k = np.cov(X, rowvar=False, aweights=R[:, k])

            rho_k = (
                (n_samples / float(self.n_components))
                * self.rho
                / (cluster_membership_estimate[k] + self.N_min)
            )

            # optional here... we can make it user defined, suggestion here..

            if self.weight_update == "graph_lasso":
                from sklearn.covariance import graphical_lasso

                # _, precisions[k, :, :] = graph_lasso(Q_k, rho_k)
                _, precisions[k, :, :] = srom_graph_lasso_method(Q_k, rho_k)
            elif self.weight_update == "quic":
                try:
                    import inverse_covariance
                except ImportError:
                    raise Exception(
                        "The library 'skggm' is not installed in the system.\
Please install skggm to use `weight_update` == 'quic' parameter."
                    )
                if self.adaptive_graph_lasso:
                    precisions[k, :, :] = inverse_covariance.quic(
                        Q_k, rho_k * np.ones((n_features, n_features))
                    )[0]
                else:
                    precisions[k, :, :] = inverse_covariance.quic(
                        Q_k, self.rho * np.ones((n_features, n_features))
                    )[0]
                # raise Exception('Currently `quic` is not supported.')
            else:
                raise Exception("Unsupported Weight Update Option")

        self.means_ = np.copy(means)
        self.precisions_ = np.copy(precisions)

    def _compute_likelihood(self, X, r):
        _, n_features = X.shape
        LL = 0

        for s in range(self.n_tasks):
            N_s = self.task_sample_count[s]
            N_base = sum(self.task_sample_count[:s])
            _r_s = r[s]
            LL += np.sum(
                r[s]
                * (
                    log_gmm_likelihood(
                        X[N_base : N_base + N_s], self.means_, self.precisions_
                    )
                    + np.outer(np.ones(N_s), np.log(self.weights_[s, :] + 1e-100))
                )
            )

        if self.m0 is None:
            m0 = np.zeros(n_features)
        else:
            m0 = self.m0
        if self.mean_estimation == "posterior":
            for k in range(self.n_components):
                LL += log_gauss_likelihood(
                    self.means_[k, :], m0, self.beta0 * self.precisions_[k, :, :]
                )

        LL += self.n_components * n_features * n_features * np.log(self.rho / 4) - (
            self.rho / 2
        ) * np.sum(abs(self.precisions_))
        return LL

    def anomaly_score(self, X_test_df, score_with_significant_clusters=True):
        """
        <description>
        Args:
            X_test_df (pandas dataframe): pandas dataframe
        Returns:
           cluster_labels: <description>
        Raises:
            Exception:
                1. If dataset is not pandas dataframe.
                2. If asset are not present
        """
        if not isinstance(X_test_df, pd.DataFrame):
            raise Exception("Input to anomaly score method must be a dataframe")

        n_samples, _ = X_test_df.shape
        X_test, test_assets, task_sample_count, X_test_index = self._process_dataframe(
            X_test_df, train=False
        )
        n_tasks = len(task_sample_count)

        task_ids = []
        for asset in test_assets:
            if asset in self.assets:
                task_ids.append(self.assets.index(asset))
            else:
                raise Exception(
                    "Asset with name %s has not been model during training" % asset
                )

        if len(self.weights_.shape) == 1:
            self.weights_ = np.expand_dims(self.weights_, 0)

        anomaly_scores = np.zeros(n_samples)

        for s in range(n_tasks):
            N_s = task_sample_count[s]
            N_base = sum(task_sample_count[:s])
            pis = np.copy(self.weights_[task_ids[s], :])

            if score_with_significant_clusters:
                pistar = pis[np.where(pis > self.eps)]
                pistar = pistar / sum(pistar)
                mstar = np.copy(self.means_[np.where(pis > self.eps)[0], :])
                Lstar = np.copy(self.precisions_[np.where(pis > self.eps)[0], :, :])
            else:
                pistar = pis
                mstar = np.copy(self.means_)
                Lstar = np.copy(self.precisions_)

            if self.mean_estimation == "posterior":
                betastar = self.betas_[np.where(pis > self.eps)]
            else:
                betastar = self.beta0 + N_s * pistar
            for j in range(N_s):
                for k, _ in enumerate(pistar):
                    A_k = (
                        0.5
                        * (betastar[k] / (1 + betastar[k]))
                        * (Lstar[k, :, :] + Lstar[k, :, :].T)
                    )
                    anomaly_scores[j + N_base] += pistar[k] * np.exp(
                        log_gauss_likelihood(X_test[j + N_base, :], mstar[k, :], A_k)
                    )

        anomaly_scores = -np.log(anomaly_scores + 1e-300)
        X_test_df.loc[X_test_index, "anomaly_score_spggm"] = anomaly_scores
        anomaly_scores = X_test_df["anomaly_score_spggm"].values
        del X_test_df["anomaly_score_spggm"]
        return anomaly_scores

    def predict(self, X_test_df):
        """
        <description>
        Args:
            X_test_df (pandas dataframe): pandas dataframe
        Returns:
           cluster_labels: <description>
        Raises:
            Exception:
                1. If dataset is not pandas dataframe.
                2. If asset are not present
        """
        if not isinstance(X_test_df, pd.DataFrame):
            raise Exception("Input to predict must be a dataframe")

        n_samples, _ = X_test_df.shape
        X, test_assets, task_sample_count, X_test_index = self._process_dataframe(
            X_test_df, train=False
        )
        n_tasks = len(task_sample_count)

        task_ids = []
        for asset in test_assets:
            if asset in self.assets:
                task_ids.append(self.assets.index(asset))
            else:
                raise Exception(
                    "Asset with name %s has not been model during training" % asset
                )

        cluster_labels = np.zeros(n_samples)

        if len(self.weights_.shape) == 1:
            self.weights_ = np.expand_dims(self.weights_, 0)

        for s in range(n_tasks):
            N_s = task_sample_count[s]
            N_base = sum(task_sample_count[:s])
            pis = np.copy(self.weights_[task_ids[s], :])
            pis[np.where(pis <= self.eps)] = 0
            pis = pis / sum(pis)
            LL = log_gmm_likelihood(
                X[N_base : N_base + N_s], self.means_, self.precisions_
            ) + np.log(self.weights_[task_ids[s], :])
            cluster_labels[N_base : N_base + N_s] = LL.argmax(axis=1)

        X_test_df.loc[X_test_index, "cluster_label_spggm"] = cluster_labels
        cluster_labels = X_test_df["cluster_label_spggm"].values
        del X_test_df["cluster_label_spggm"]
        return cluster_labels

    def get_weights(self):
        """
        
        """
        return self.weights_

    def get_means(self):
        return self.means_

    def get_precisions(self):
        return self.precisions_

    def get_AIC_score(self):
        return 2.0 * self.train_likelihood - 2.0 * self._get_model_complexity()

    def get_BIC_score(self):
        N = self.n_samples
        return 2.0 * self.train_likelihood - np.log(N) * self._get_model_complexity()

    def _get_model_complexity(self):
        d = 0
        for i_k in range(self.n_components):
            for a_t in range(self.n_tasks):
                if self.weights_[a_t, i_k] >= self.eps:
                    d = (
                        d
                        + len(np.nonzero(self.means_[i_k,]))
                        + (
                            len(np.nonzero(self.precisions_[i_k, :].ravel())[0])
                            - self.n_features
                        )
                        / 2.0
                        + self.n_features
                    )
                    break

        for i_k in range(self.n_components):
            for a_t in range(self.n_tasks):
                if self.weights_[a_t, i_k] >= self.eps:
                    d = d + 1
        return d
