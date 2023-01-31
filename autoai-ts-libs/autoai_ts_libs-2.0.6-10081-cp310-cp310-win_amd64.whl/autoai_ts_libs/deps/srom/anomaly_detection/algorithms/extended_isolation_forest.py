# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: extende_isolation_forest
   :synopsis: Extended isolation forest with quick algorithm.

.. moduleauthor:: SROM Team
"""


from sklearn.base import BaseEstimator
import numpy as np
import pandas as pd
import random as rn
import numbers
from warnings import warn


class Node(object):
    """
    Class to create a node of tree.
    """

    def __init__(self, len_X, n, p, e, left, right, node_type=""):
        """
            Init method for class Node
        """
        self.size = len_X
        self.n = n
        self.p = p
        self.e = e
        self.left = left
        self.right = right
        self.ntype = node_type


class iTree(object):
    """
    Class to create tree of sample data.

    """

    def __init__(self, X, cur_depth, max_depth, num_features):
        """
        Parameters:
        X: input X to be used for sampling, 
        cur_depth: current depth, 
        max_depth: max depth, 
        num_features: number of features.
        """
        self.cur_depth = cur_depth
        self.max_depth = max_depth
        self.num_features = num_features
        self.exnodes = 0

        self.size = len(X)
        self.dim = X.shape[1]

        self.Q = np.arange(np.shape(X)[1], dtype="int")
        self.p = None
        self.n = None

        self.root = self.make_tree(X, cur_depth, max_depth)

    def make_tree(self, X, cur_depth, max_depth):
        """
        Make tree of samples using input data.
        Parameters:
        X: numpy array of input data.
        cur_depth: int, L current depth. 
        max_depth: int, maximum depth of tree.
        """

        self.cur_depth = cur_depth

        if cur_depth >= max_depth or len(X) <= 1:
            left = None
            right = None
            self.exnodes += 1
            return Node(
                len(X), self.n, self.p, cur_depth, left, right, node_type="exNode"
            )
        else:
            mins = X.min(axis=0)
            maxs = X.max(axis=0)
            idxs = np.random.choice(
                range(self.dim), self.dim - self.num_features, replace=False
            )
            self.n = np.random.normal(0, 1, self.dim)
            self.n[idxs] = 0
            self.p = np.random.uniform(
                mins, maxs
            )  # Picking a random intercept point for the hyperplane splitting data.
            w = (X - self.p).dot(
                self.n
            ) < 0  # Criteria that determines if a data point should go to the left or right child node.
            return Node(
                len(X),
                self.n,
                self.p,
                cur_depth,
                left=self.make_tree(X[w], cur_depth + 1, max_depth),
                right=self.make_tree(X[~w], cur_depth + 1, max_depth),
                node_type="inNode",
            )


class ExtendedIsolationForest(BaseEstimator):
    """
    This is a simple Python implementation for the Extended Isolation Forest method described in 
    this (https://doi.org/10.1109/TKDE.2019.2947676). 
    It is an improvement on the original algorithm Isolation Forest which is described 
    (among other places) in this paper for detecting anomalies and outliers for multidimensional data point distributions. 
    """

    def __init__(
        self, n_estimators=100, max_samples="auto", max_features=1.0, std_threshold=2.5
    ):
        """
        Parameters:
            n_estimators (int): Number of estimators to be used. 
            max_samples (int or str): Max number of samples to be used.
            max_features (number): Max number of features to be used.
            std_threshold: std threshold for outlier.
        """
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.max_features = max_features
        self.std_threshold = std_threshold

    def fit(self, X, y=None):
        """
        Fit estimator.
        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of ExtendedIsolationForest. 

        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        X = X.astype(np.float64)

        # setting number of samples to be used for modeling each tree
        n_samples = X.shape[0]
        if isinstance(self.max_samples, str):
            if self.max_samples == "auto":
                max_samples = min(256, n_samples)
            else:
                raise ValueError(
                    "max_samples (%s) is not supported."
                    'Valid choices are: "auto", int or'
                    "float" % self.max_samples
                )
        elif isinstance(self.max_samples, numbers.Integral):
            if self.max_samples > n_samples:
                warn(
                    "max_samples (%s) is greater than the "
                    "total number of samples (%s). max_samples "
                    "will be set to n_samples for estimation."
                    % (self.max_samples, n_samples)
                )
                max_samples = n_samples
            else:
                max_samples = self.max_samples
        else:  # float
            if not 0.0 < self.max_samples <= 1.0:
                raise ValueError(
                    "max_samples must be in (0, 1], got %r" % self.max_samples
                )
            max_samples = int(self.max_samples * n_samples)
        self.max_samples_ = max_samples
        self.max_depth_ = int(np.ceil(np.log2(max(max_samples, 2))))

        # setting number of fetures
        n_columns = X.shape[1]
        if isinstance(self.max_features, numbers.Integral):
            if self.max_features > n_columns:
                warn("max_features should be between 1 to (%s)" % (n_columns))
                max_features = n_columns
            elif self.max_features < 1:
                warn("max_features should be between 1 to (%s)" % (n_columns - 1))
                max_features = 1
            else:
                max_features = self.max_features
        else:  # float
            if not 0.0 < self.max_features <= 1.0:
                raise ValueError(
                    "max_features must be in [0, 1), got %r" % self.max_features
                )
            max_features = int(self.max_features * n_columns)
            if max_features < 1:
                max_features = 1
        self.max_features_ = max_features

        self.Trees = []
        self.c = self.c_factor(self.max_samples_)

        nobjs = len(X)
        for _ in range(self.n_estimators):
            ix = rn.sample(range(nobjs), self.max_samples_)
            X_p = X[ix]
            self.Trees.append(iTree(X_p, 0, self.max_depth_, self.max_features_))

        return self

    def c_factor(self, n):
        """
        Internal function.
        """
        return 2.0 * (np.log(n - 1) + 0.5772156649) - (2.0 * (n - 1.0) / (n * 1.0))

    def predict(self, X):
        """
        Calls anomaly_score() and returns -1 as anomaly and 1 as non 
        anomaly if score is out of given times of std deviation threshold.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            tmp_score (numpy.ndarray): Anomaly scores.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values
        outliers = []
        tmp_score = self.anomaly_score(X)
        tmp_mean_x = np.mean(tmp_score)
        tmp_std_x = np.std(tmp_score)
        for i in tmp_score:
            z = (i - tmp_mean_x) / tmp_std_x
            if abs(z) > self.std_threshold:
                outliers.append(-1)
            else:
                outliers.append(1)
        return np.array(outliers)

    def anomaly_score(self, X):
        """
        Compute anomaly score of X using the fitted detector.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.        
        """
        if isinstance(X, pd.DataFrame):
            X = X.values
        S = np.zeros(len(X))
        for i in range(len(X)):
            h_temp = 0
            for j in range(self.n_estimators):
                h_temp += self._find_paths(X[i], self.Trees[j].root, 0) * 1.0
            Eh = h_temp / self.n_estimators
            S[i] = 2.0 ** (-Eh / self.c)
        return S

    def _find_paths(self, x, T, depth):
        """
            Internal method to help calculate anomaly score
        """
        if T.ntype == "exNode":
            if T.size <= 1:
                return depth
            else:
                return depth + self.c_factor(T.size)
        else:
            if (x - T.p).dot(T.n) < 0:
                return self._find_paths(x, T.left, depth + 1)
            else:
                return self._find_paths(x, T.right, depth + 1)

    def decision_function(self, X):
        """
        Compute anomaly score of X using the fitted detector.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.        
        """
        return self.anomaly_score(X)
