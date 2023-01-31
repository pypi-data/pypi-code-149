# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
    .. module:: ActiveLearning
       :synopsis: ImbActiveLearner class.

    .. moduleauthor:: SROM Team
"""

import numpy as np
import random

from sklearn.neighbors import KDTree
from sklearn.decomposition import PCA


class LabelQueryStrategy(object):
    """
    Strategy for identifying instances to query labels for

    Parameters:
        oracle: instance of teacher that supplies labels
        default_step_size: number of labels to query each time
    """

    def __init__(self, oracle, default_step_size=50):
        """Init method"""
        self.default_step_size = default_step_size
        self.oracle = oracle

    def query_oracle(self, ixs):
        """query oracle method for get labels"""
        return self.oracle.get_labels(ixs)

    def get_new_labels(
        self, estimator, Xtrain, labeled_ix, n_new_labels=None, ignore_indices=None
    ):
        """
        Function to obtain new labels by first identifying instances to query \
            the oracle for, queries the oracle and returns labels

        Parameters:
            estimator : the base estimator - should implement predict_proba()
            Xtrain : training array - no targets
            labeled_ix : indices for which the learner already know the labels for
            n_new_labels : number of labels to obtain (defaults to default_step_size)
            ignore_indices : indices of instances to ignore
        returns:
            - list of indices for which the target labels are obtained
            - target labels for a selection of instances
        """

        step_size = self.default_step_size if n_new_labels == None else n_new_labels
        avoid = (
            np.zeros(Xtrain.shape[0]).astype(bool)
            if ignore_indices == None
            else ignore_indices
        )
        avoid = avoid | labeled_ix
        probs = estimator.predict_proba(Xtrain)
        pdf = probs[:, 1] - 0.5
        sortix = np.argsort(abs(pdf))
        add_sample = [ix for ix in sortix if ~avoid[ix]][: int(1.2 * step_size)]
        add_sample = random.sample(add_sample, step_size)
        return add_sample, self.query_oracle(add_sample)


class LabelOracle(object):
    """
    LabelOracle aka teacher -  supplies target labels

    Parameters:
        Xtrain : n x m  array - all n training instances of only m independent-variable data (no target variable data)
        yvals : 1-d array - all n target labels
    """

    def __init__(self, Xtrain, yvals):
        """Init method for Xtrain and Yvals"""
        if Xtrain.shape[0] != yvals.shape[0]:
            raise ValueError("Xtrain.shape[0] is not equal to yvals.shape[0].")
        self.Xtrain = Xtrain
        self.train_labels = yvals

    def get_labels(self, ixs):
        """get lables method"""
        return self.train_labels[ixs]


class ImbActiveLearner(object):
    """
    Active Learner for class-imbalance setting: indentifies samples to obtain labels for based on the \
        state of the model learned so far, and updates the model with the new labeled samples

    Parameters:
        base_estimator : a classification model that can emit class uncertainty (through predict_proba)
        querier : object implementing a querying mechanism that identifies which instances to query \
            the oracle for, queries the oracle and returns labels
        Xtrain : n x m  array - all n training instances of only m independent-variable data (no target variable data)
        yinit : 1-d array - target labels to initialize with. unknown/unsupplied labels are initilized with -1 \
            (0 - negative class, 1 - positive class)
    """

    def __init__(
        self,
        base_estimator,  # = ExtraTreesClassifier,
        Xtrain,
        querier=None,
        yinit=None,
        # class_weight = None,
        *args,
        **kwargs,
    ):
        """
        base_estimator: Any sklearn classifier

        Parameters:
            Xtrain: 2-d numpy array - training data
            yinit: keeps track of known target values
            n_queried: keeps track of number of labels queried
            sampling_history: list of lists - keeps track of sample indices for which \
                labels were requested - over the iterations
            queried_ix: indices for which labels are known so far
        """
        self.base_estimator = base_estimator
        self.querier = querier
        self.Xtrain = Xtrain
        if not yinit:
            self.ytrain = np.full(Xtrain.shape[0], -1)
        else:
            if Xtrain.shape[0] != yinit.shape[0]:
                raise ValueError("Xtrain.shape[0] is not equal to yinit.shape[0].")
            self.ytrain = yinit
        self.n_queried = 0
        self.queried_ix = np.zeros(Xtrain.shape[0]).astype(bool)
        self.sampling_history = []
        self.args = args
        self.kwargs = kwargs

    def _update_label_info(self, new_label_ix, yvals):
        """internal method to update label info"""
        self.sampling_history.append(new_label_ix)
        self.queried_ix[new_label_ix] = True
        self.ytrain[new_label_ix] = yvals
        self.n_queried = sum(self.queried_ix)

    def update_model(self, new_train_ix, yvals):
        """update model method for best estimator"""
        self.base_estimator.fit(
            self.Xtrain[self.queried_ix], self.ytrain[self.queried_ix]
        )
        return self.base_estimator

    def query_labels(self, n_new_labels):
        """query labels method"""
        new_train_ix, yvals = self.querier.get_new_labels(
            self.base_estimator, self.Xtrain, self.queried_ix, n_new_labels
        )
        self._update_label_info(new_train_ix, yvals)
        return new_train_ix, yvals

    def get_init_labels(self, est_class_ratio):
        """get init labels method"""
        avoid = np.zeros(self.Xtrain.shape[0]).astype(bool)
        stepsize = 20
        radius = 10

        pca = PCA(0.95)
        Xp = pca.fit_transform(self.Xtrain)
        kdt = KDTree(Xp, leaf_size=20)
        kddens = kdt.kernel_density(Xp, h=1)

        yinit = self.ytrain  # np.full(Xtrain.shape[0], -1)
        labeled_ix = []

        wts = 1 / kddens
        # while (sum(self.ytrain[self.queried_ix]) <= 0):
        while sum(yinit[labeled_ix]) < 1:
            if (len(avoid) == 0) or (len(wts) == 0):
                print(
                    "error here avoid {} wts {}".format(len(avoid), len(wts))
                )  # added to check random error
            rs = random.choices(
                np.where(~avoid)[0], weights=wts[~avoid], k=stepsize
            )  # 200)
            # self.queried_ix[rs] = True
            # self.ytrain[rs] = self.querier.query_oracle(rs)
            yinit[rs] = self.querier.query_oracle(rs)
            labeled_ix.extend(rs)
            avoid[rs] = True
            nbrs = kdt.query_radius(Xp[rs], radius)
            for nbr in nbrs:
                avoid[nbr] = True
        self._update_label_info(labeled_ix, yinit[labeled_ix])
        # self.n_queried = sum(self.queried_ix)
        # self.sampling_history.append(np.where(self.queried_ix))
        return labeled_ix, avoid
