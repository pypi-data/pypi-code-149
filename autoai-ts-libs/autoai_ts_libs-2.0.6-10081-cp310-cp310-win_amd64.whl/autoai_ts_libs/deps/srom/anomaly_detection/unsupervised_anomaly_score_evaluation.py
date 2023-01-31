# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: unsupervised_anomaly_score_evaluation
   :synopsis: unsupervised anomaly score evaluation

.. moduleauthor:: SROM Team
"""
import numpy as np
import dill  # Do not remove.
from sklearn.metrics import auc
from sklearn.model_selection import KFold
import pandas as pd
import time


def unsupervised_anomaly_cross_val_score(
    clf,
    X,
    y=None,
    groups=None,
    cv=None,
    scoring="em_score",
    return_train_score=False,
    verbose=0,
):
    """[summary]
    This function is for cross_val_score for unsupervised_anomaly pipeline

    Args:
        clf ([type]): [description]
        X ([type]): [description]
        y ([type], optional): [description]. Defaults to None.
        groups ([type], optional): [description]. Defaults to None.
        cv ([type], optional): [description]. Defaults to None.
        scoring (str, optional): [description]. Defaults to "em_score".
        return_train_score (bool, optional): [description]. Defaults to False.
        verbose (int, optional): [description]. Defaults to 0.
    """

    def em_score(clf, x, y=None):
        """[summary]

        Args:
            clf ([type]): [description]
            x ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        lim_inf = np.min(x)
        lim_sup = np.max(x)
        n_features = x.shape[1]
        volume_support = (lim_sup - lim_inf).prod()
        t = np.arange(0, 100 / volume_support, 0.01 / volume_support)
        unif = np.random.uniform(lim_inf, lim_sup, size=(n_generated, n_features))

        s_X = clf.predict(x)
        s_unif = clf.predict(unif)

        EM_t = np.zeros(t.shape[0])
        n_samples = s_X.shape[0]
        s_X_unique = np.unique(s_X)
        EM_t[0] = 1.0
        for u in s_X_unique:
            EM_t = np.maximum(
                EM_t,
                1.0 / n_samples * (s_X > u).sum()
                - t * (s_unif > u).sum() / n_generated * volume_support,
            )

        amax = np.argmax(EM_t <= t_max) + 1
        if amax == 1:
            amax = -1
        em_score = auc(t[:amax], EM_t[:amax])
        return em_score

    def mv_score(clf, x, y=None):
        """[summary]

        Args:
            clf ([type]): [description]
            x ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        lim_inf = np.min(x)
        lim_sup = np.max(x)
        n_features = x.shape[1]
        axis_alpha = np.arange(alpha_min, alpha_max, 0.0001)
        volume_support = (lim_sup - lim_inf).prod()
        unif = np.random.uniform(lim_inf, lim_sup, size=(n_generated, n_features))
        s_X = clf.predict(x)
        s_unif = clf.predict(unif)

        n_samples = s_X.shape[0]
        s_X_argsort = s_X.argsort()
        mass = 0
        cpt = 0
        u = s_X[s_X_argsort[-1]]
        mv = np.zeros(axis_alpha.shape[0])
        for i in range(axis_alpha.shape[0]):
            while mass < axis_alpha[i]:
                cpt += 1
                u = s_X[s_X_argsort[-cpt]]
                mass = 1.0 / n_samples * cpt
            mv[i] = float((s_unif >= u).sum()) / n_generated * volume_support

        return auc(axis_alpha, mv)

    def al_score(clf, x, y=None):
        """[summary]

        Args:
            clf ([type]): [description]
            x ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        n_features = x.shape[1]
        U = np.zeros((n_generated, n_features))

        for l in range(0, x.shape[1]):
            U[:, l] = np.random.uniform(x[0, l], x[1, l], n_generated)

        score_U = clf.predict(U)
        score_test = clf.predict(x)

        vol_tot_cube = np.prod(x[1, :] - x[0, :])

        alphas = np.arange(alpha_min, alpha_max, 0.05)
        offsets_p = np.percentile(score_test, 100 * (1 - alphas))

        # compute volumes of associated level sets
        vol_p = (
            np.array([np.mean(score_U >= offset) for offset in offsets_p])
            * vol_tot_cube
        )

        return auc(alphas, vol_p)

    n_generated = 10000
    t_max = 0.9
    alpha_min = 0.9
    alpha_max = 0.999
    scores = {}
    scores["test_score"] = []
    scores["fit_time"] = []
    scores["score_time"] = []
    if scoring == "em_score":
        scorer = em_score
    elif scoring == "mv_score":
        scorer = mv_score
    elif scoring == "al_score":
        scorer = al_score
    else:
        raise Exception("scorer not supported")

    if isinstance(X, pd.DataFrame):
        X = X.values

    if cv == None or type(cv) == int:
        k = cv or 5
        cv = KFold(n_splits=k)
    for train_index, test_index in cv.split(X):
        X_train, X_test = X[train_index], X[test_index]
        start_time = time.time()
        clf.fit(X_train)
        fit_time = time.time() - start_time
        scores["fit_time"].append(fit_time)
        start_time = time.time()
        scores["test_score"].append(scorer(clf, x=X_train))
        score_time = time.time() - start_time
        scores["score_time"].append(score_time)
    return scores


def EM_score_parameter(lim_inf, lim_sup, n_features, n_generated, t_max):
    """
        em score paramter method 

        Returns:
            em score
    """
    def EM_score(clf, X, y_true=None):
        """
            em score method using x
            
            Parameters:
                X (pandas dataframe or numpy array): Input Samples.
                y_true(default=None)

            Returns:
                ems_score
        """
        volume_support = (lim_sup - lim_inf).prod()
        t = np.arange(0, 100 / volume_support, 0.01 / volume_support)
        unif = np.random.uniform(lim_inf, lim_sup, size=(n_generated, n_features))
        s_X = clf.predict(X)
        s_unif = clf.predict(unif)

        EM_t = np.zeros(t.shape[0])
        n_samples = s_X.shape[0]
        s_X_unique = np.unique(s_X)
        EM_t[0] = 1.0
        for u in s_X_unique:
            EM_t = np.maximum(
                EM_t,
                1.0 / n_samples * (s_X > u).sum()
                - t * (s_unif > u).sum() / n_generated * volume_support,
            )

        amax = np.argmax(EM_t <= t_max) + 1
        if amax == 1:
            amax = -1
        em_score = auc(t[:amax], EM_t[:amax])
        return em_score

    return EM_score


# roc-auc em curve for the neg label
# roc-auc curve for the pos_label
def MV_score_parameter(lim_inf, lim_sup, n_features, n_generated, alpha_min, alpha_max):
    """
        mv score parameter

        Returns: 

    """
    def MV_score(clf, X, y_true=None):
        """
            em score method using x
            
            Parameters:
                X (pandas dataframe or numpy array): Input Samples.
                y_true(default=None).

            Returns:
                mv_score
        """
        axis_alpha = np.arange(alpha_min, alpha_max, 0.0001)
        volume_support = (lim_sup - lim_inf).prod()
        unif = np.random.uniform(lim_inf, lim_sup, size=(n_generated, n_features))
        s_X = clf.predict(X)
        s_unif = clf.predict(unif)

        n_samples = s_X.shape[0]
        s_X_argsort = s_X.argsort()
        mass = 0
        cpt = 0
        u = s_X[s_X_argsort[-1]]
        mv = np.zeros(axis_alpha.shape[0])
        for i in range(axis_alpha.shape[0]):
            while mass < axis_alpha[i]:
                cpt += 1
                u = s_X[s_X_argsort[-cpt]]
                mass = 1.0 / n_samples * cpt
            mv[i] = float((s_unif >= u).sum()) / n_generated * volume_support

        return auc(axis_alpha, mv)

    return MV_score


# approach 3
def AL_score_parameter(X_range, n_features, n_generated, alpha_min, alpha_max):
    """
        al score paramter method

        Returns: compute_scores

    """
    def compute_scores(clf, X, y_true=None):
        """
            compute scores method using x
            
            Parameters:
                X (pandas dataframe or numpy array): Input Samples.
                y_true(default=None).

            Returns:
                auc
        """
        U = np.zeros((n_generated, n_features))
        for l in range(n_features):
            U[:, l] = np.random.uniform(X_range[0, l], X_range[1, l], n_generated)

        score_U = clf.predict(U)
        score_test = clf.predict(X)

        vol_tot_cube = np.prod(X_range[1, :] - X_range[0, :])

        alphas = np.arange(alpha_min, alpha_max, 0.05)
        offsets_p = np.percentile(score_test, 100 * (1 - alphas))

        # compute volumes of associated level sets
        vol_p = (
            np.array([np.mean(score_U >= offset) for offset in offsets_p])
            * vol_tot_cube
        )

        return auc(alphas, vol_p)

    return compute_scores
