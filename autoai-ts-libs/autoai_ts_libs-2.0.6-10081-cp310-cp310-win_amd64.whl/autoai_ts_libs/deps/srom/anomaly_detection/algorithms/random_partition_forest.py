# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: random_partition_forest
   :synopsis: random_partition_forest.
   
.. moduleauthor:: SROM Team
"""

import numpy as np
import pandas as pd
from functools import partial
from multiprocessing import Pool
import random as rn
from sklearn.base import BaseEstimator
from warnings import warn
import numbers


def getSplit(X):
    """
    Get uniform distribution from input.
    Parameters:
        X (numpy array) : input
    """
    xmin = X.min()
    xmax = X.max()
    return np.random.uniform(xmin, xmax)


def similarityScore(S, node, alpha):
    """
    This is (X-mean)/std based normalized vector score.
    Parameters:
        S (numpy array) : input
        node (object) : node object.
        alpha (number) : alpha.
    """
    U = 0
    if len(S) > 0:
        d = np.shape(S)[1]
        U = (S - node.M) / node.Mstd
        U = (2) ** (-alpha * (np.sum(U * U / d, axis=1)))
    return U


def empirical_entropy(hist):
    """
    Histogram based entropy.
    Parameters:
        hist(array_like) : array of histogram
    """
    h = np.asarray(hist, dtype=np.float64)
    if h.sum() <= 0 or (h < 0).any():
        return 0
    h = h / h.sum()
    return -(h * np.ma.log2(h)).sum()


def obtainFeatureWeight(s, nbins):
    """
    Entropy is used as a feature weight
    Parameters:
        s(array_like) : Input.
        nbins(number) : Number of bins.
    
    """
    wmin = 0.02

    hist, _ = np.histogram(s, bins=nbins)
    ent = empirical_entropy(hist)
    ent = ent / np.log2(nbins)

    if np.isfinite(ent):
        return max(1.0 - ent, wmin)
    else:
        return wmin


def generateNormalizedFeature(X):
    """
    Entropy is normalized.
    Parameters:
        X(numpy array) : input
    """
    featureDistrib = []
    nbins = int(len(X) / 8) + 2
    for i in range(np.shape(X)[1]):
        featureDistrib.append(obtainFeatureWeight(X[:, i], nbins))
    featureDistrib = np.array(featureDistrib)
    featureDistrib = featureDistrib / (np.sum(featureDistrib) + 1e-5)
    return featureDistrib


def traverse_tree(
    forest, node, treeIdx, obsIdx, X, featureDistrib, depth=0, alpha=1e-2
):
    """
    This is to obtain various values.
    Parameters:
        forest (object) : Forest object. 
        node (object) : Node object. 
        treeIdx (number) : Tree index. 
        obsIdx (number) : Obs index. 
        X (numpy array) : input data. 
        featureDistrib (numpy array) : Feature distribution array. 
        depth (number) : depth. 
        alpha (number) : alpha.
    """

    if isinstance(node, LeafNode):
        Xnode = X[obsIdx]
        f = ((node.size + 1) / forest.max_samples_) / (
            (1 + len(Xnode)) / forest.XtestSize
        )
        if alpha == 0:
            forest.LD[obsIdx, treeIdx] = 0
            forest.LF[obsIdx, treeIdx] = -f
            forest.LDF[obsIdx, treeIdx] = -f
        else:
            z = similarityScore(Xnode, node, alpha)
            forest.LD[obsIdx, treeIdx] = z
            forest.LF[obsIdx, treeIdx] = -f
            forest.LDF[obsIdx, treeIdx] = z * f
    else:
        idx = (X[:, node.splitAtt] <= node.splitValue) * obsIdx
        traverse_tree(
            forest, node.left, treeIdx, idx, X, featureDistrib, depth + 1, alpha=alpha
        )
        idx = (X[:, node.splitAtt] > node.splitValue) * obsIdx
        traverse_tree(
            forest, node.right, treeIdx, idx, X, featureDistrib, depth + 1, alpha=alpha
        )


class iTree(object):
    """
    Class for preparing isolation forest tree
    Idea is use the feature weight as a weight factor in partition
    """

    def __init__(self, X, featureDistrib, max_depth, sample_size, current_depth):
        """
            Parameters:
            X (numpy array) : input data.
            featureDistrib (numpy array) : feature distribution data. 
            max_depth (number) : max depth. 
            sample_size (number) : sample size.
            current_depth (number) : cuurent depth.
        """
        self.size = len(X)
        self.depth = current_depth + 1
        n_obs, n_features = X.shape
        next_depth = current_depth + 1
        limit_not_reached = max_depth > next_depth

        if n_obs > 32:
            featureDistrib = generateNormalizedFeature(X)
        self.featureDistrib = featureDistrib

        cols = np.arange(n_features, dtype="int")
        self.splitAtt = rn.choices(cols, weights=featureDistrib)[0]
        splittingCol = X[:, self.splitAtt]
        self.splitValue = getSplit(splittingCol)
        idx = splittingCol <= self.splitValue
        X_aux = X[idx, :]

        if (
            limit_not_reached
            and X_aux.shape[0] > 5
            and (np.any(X_aux.max(0) != X_aux.min(0)))
        ):
            self.left = iTree(X_aux, featureDistrib, max_depth, sample_size, next_depth)
        else:
            self.left = LeafNode(X_aux, max_depth, X, sample_size)

        idx = np.invert(idx)
        X_aux = X[idx, :]

        if (
            limit_not_reached
            and X_aux.shape[0] > 5
            and (np.any(X_aux.max(0) != X_aux.min(0)))
        ):
            self.right = iTree(
                X_aux, featureDistrib, max_depth, sample_size, next_depth
            )
        else:
            self.right = LeafNode(X_aux, max_depth, X, sample_size)

        self.n_nodes = 1 + self.left.n_nodes + self.right.n_nodes


class LeafNode:
    """
    When iTree went to leaf node, we call it.
    """

    def __init__(self, X, depth, Xp, sample_size):
        """
            Parameters:
            X (numpy array) : input data. 
            depth (number) : depth. 
            Xp (numpy array) : Xp data. 
            sample_size (number) : sample size.
        """
        self.depth = depth + 1
        self.size = len(X)
        self.n_nodes = 1
        self.freq = self.size / sample_size
        self.freqs = 0

        if len(X) != 0:
            self.M = np.mean(X, axis=0)
            if len(X) > 10:
                self.Mstd = np.std(X, axis=0)
                self.Mstd[self.Mstd == 0] = 1e-2
            else:
                self.Mstd = np.ones(np.shape(X)[1])
        else:  # original data
            self.M = np.mean(Xp, axis=0)
            if len(Xp) > 10:
                self.Mstd = np.std(Xp, axis=0)
                self.Mstd[self.Mstd == 0] = 1e-2
            else:
                self.Mstd = np.ones(np.shape(X)[1])


class RandomPartitionForest(BaseEstimator):
    """
    Anomaly using random partition forest
    Paper : https://arxiv.org/pdf/2006.16801.pdf
    """

    def __init__(
        self,
        n_estimators=100,
        max_samples="auto",
        anomaly_type="visit_frequency",
        alpha=1.0,
        threshold=0.1,
    ):
        """
            Parameters:
            n_estimators (number) : Number of estimators.
            max_samples (str or number ) : Max samples.
            anomaly_type (str) : Anomaly type.
            alpha (number) : alpha.
            threshold (number) : threshold for anomaly.
        """
        self.n_estimators = n_estimators
        self.max_samples = max_samples
        self.alpha = alpha
        self.anomaly_type = anomaly_type
        self.threshold = threshold

    def fit(self, X, y=None):
        """
        Fit estimator.
        Parameters:
            X (pandas dataframe or numpy array, required): Normal behavior data of shape:(n_samples, n_features). \
                Set of samples, where n_samples is the number of samples and n_features is the number of features.
            y (pandas dataframe or numpy array, optional): Defaults to None.

        Returns:
            self: Trained instance of RandomPartitionForest.

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
        self._path_norm_fact = np.sqrt(len(X))

        self.Trees = []

        # obtain column wise feature entropy, normalized across all the columns
        self.featureDistrib = generateNormalizedFeature(X)

        nobjs = len(X)
        for _ in range(self.n_estimators):
            ix = rn.sample(range(nobjs), self.max_samples_)
            X_p = X[ix]
            self.Trees.append(
                iTree(X_p, self.featureDistrib, self.max_depth_, self.max_samples_, 0)
            )

        return self

    def predict(self, X):
        """
        Calls anomaly_score() which predicts if given data point is anomaly or not. 1 is non anomaly
        -1 is anomaly. 

        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.

        Returns:
            Anomaly scores.
        """
        if isinstance(X, pd.DataFrame):
            X = X.values
        predictions = self.anomaly_score(X) >= self.threshold
        predictions = predictions * 1
        predictions[predictions == 1] = -1
        predictions[predictions == 0] = 1
        return predictions

    def _traverse(self, X):
        """
            Internal method as a helper method.
        """
        self.L = np.zeros((len(X), self.n_estimators))
        self.LD = np.zeros((len(X), self.n_estimators))
        self.LF = np.zeros((len(X), self.n_estimators))
        self.LDF = np.zeros((len(X), self.n_estimators))

        for treeIdx, itree in enumerate(self.Trees):
            obsIdx = np.ones(len(X)).astype(bool)
            traverse_tree(
                self, itree, treeIdx, obsIdx, X, self.featureDistrib, alpha=self.alpha
            )

    def anomaly_score(self, X):
        """
        Compute anomaly score.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            Anomaly scores.
        
        """
        if isinstance(X, pd.DataFrame):
            X = X.values

        self.XtestSize = len(X)
        self._traverse(X)
        scD = -self.LD.mean(1)
        scF = self.LF.mean(1)
        scDF = -self.LDF.mean(1)
        if self.anomaly_type == "visit_frequency":
            return scF
        elif self.anomaly_type == "point_wise":
            return scD
        elif self.anomaly_type == "collective_anomaly":
            return scDF
        else:
            raise Exception("Unsupported Anomaly Type")

    def decision_function(self, X):
        """
        Compute anomaly score.
        Parameters:
            X (pandas dataframe or numpy array, required): Input Samples.
        Returns:
            Anomaly scores.
        """
        return self.anomaly_score(X)

