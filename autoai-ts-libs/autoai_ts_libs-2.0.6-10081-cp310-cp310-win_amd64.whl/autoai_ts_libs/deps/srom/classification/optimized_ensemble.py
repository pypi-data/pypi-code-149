# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import os
import pandas as pd
import numpy as np
from sklearn.metrics import log_loss
from sklearn.base import BaseEstimator
from scipy.optimize import minimize

"""
.. module:: optimized_ensemble
   :synopsis: Optimized Ensemble.

.. moduleauthor:: SROM Team
"""

def _objective_func_1(w, Xs, y):
    """
        Return the score using log_loss.
    """
    w = np.abs(w)
    solution = np.zeros(Xs[0].shape)
    for i in range(len(w)):
        solution += Xs[i] * w[i]
    score = log_loss(y, solution)
    return score

def _objective_func_2(w, Xs, y, n_class):
    """
        Return the score using log_loss.
    """
    w_range = np.arange(len(w)) % n_class
    for i in range(n_class):
        w[w_range == i] = w[w_range == i] / np.sum(w[w_range == i])
    solution = np.zeros(Xs[0].shape)
    for i in range(len(w)):
        solution[:, i %
                    n_class] += Xs[int(i / n_class)][:, i % n_class] * w[i]
    score = log_loss(y, solution)
    return score


class Optimized_Ensemble_one(BaseEstimator):
    """
    Given a set of predictions $X_1, X_2, ..., X_n$, it computes the optimal set of weights
    $w_1, w_2, ..., w_n$; such that minimizes $log\_loss(y_T, y_E)$,
    where $y_E = X_1*w_1 + X_2*w_2 +...+ X_n*w_n$ and $y_T$ is the true solution.
    """

    def __init__(self, num_class):  # n_class=NUM_CLASS
        """
            Parameters:
                num_class (int):
        """
        self.num_class = num_class

    def fit(self, X, y):
        """
        Learn the optimal weights by solving an optimization problem.
        Parameters:
        ----------
        Xs: list of predictions to be ensembled
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        y: array-like
        Class labels
        """
        Xs = np.hsplit(X, X.shape[1] / self.num_class)  # self.n_class
        # Initial solution has equal weight for all individual predictions
        x0 = np.ones(len(Xs)) / float(len(Xs))
        # Weights must be bounded in [0,1]
        bounds = [(0, 1)] * len(x0)
        # All weights must sum to 1
        cons = ({'type': 'eq', 'fun': lambda w: 1-sum(w)})
        # calling the solver
        res = minimize(_objective_func_1, 
                       x0, 
                       args=(Xs, y),
                       method='SLSQP',
                       bounds=bounds,
                       constraints=cons)
        self.w = res.x
        self.classes_ = np.unique(y)
        return self

    def predict_proba(self, X):
        """
        Use the weights learned in training to predict class probabilities.
        Parameters:
        ----------
        Xs: list of predictions to be blended.
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        Return:
        ------
        y_pred: array_like, shape=(n_samples, n_class)
        The blended prediction.
        """
        Xs = np.hsplit(X, X.shape[1] / self.num_class)
        y_pred = np.zeros(Xs[0].shape)
        for i in range(len(self.w)):
            y_pred += Xs[i] * self.w[i]
        return y_pred


    def predict(self, X):
        """
        Use the weights learned in training to predict class probabilities.
        Parameters:
        ----------
        Xs: list of predictions to be blended.
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        Return:
        ------
        y_pred: array_like, shape=(n_samples, n_class)
        The blended prediction.
        """
        y_pred = self.predict_proba(X)
        
        index=[]
        for i in y_pred:
            ind=pd.Series(i).idxmax()
            index.append(ind)

        return index
                    

class Optimized_Ensemble_two(BaseEstimator):
    """
    Given a set of predictions $X_1, X_2, ..., X_n$, where each $X_i$ has
    $m=12$ clases, i.e. $X_i = X_{i1}, X_{i2},...,X_{im}$. The algorithm finds the optimal
    set of weights $w_{11}, w_{12}, ..., w_{nm}$; such that minimizes
    $log\_loss(y_T, y_E)$, where $y_E = X_{11}*w_{11} +... + X_{21}*w_{21} + ...
    + X_{nm}*w_{nm}$ and and $y_T$ is the true solution.
    """

    def __init__(self, num_class):  # n_class=NUM_CLASS
        self.num_class = num_class

    def fit(self, X, y):
        """
        Learn the optimal weights by solving an optimization problem.
        Parameters:
        ----------
        Xs: list of predictions to be ensembled
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        y: array-like
        Class labels
        """
        Xs = np.hsplit(X, X.shape[1] / self.num_class)  # self.n_class
        # Initial solution has equal weight for all individual preds
        x0 = np.ones(self.num_class * len(Xs)) / float(len(Xs))
        # Weights must be bounded in [0,1]
        bounds = [(0, 1)]*len(x0)
        # Calling the solver (constraints are directly defined in the objective
        # function)
        res = minimize(_objective_func_2, 
                       x0, 
                       args=(Xs, y, self.num_class),  # self.n_class
                       method='L-BFGS-B',
                       bounds=bounds,
                       )
        self.w = res.x
        self.classes_ = np.unique(y)
        return self

    def predict_proba(self, X):
        """
        Use the weights learned in training to predict class probabilities.
        Parameters:
        ----------
        Xs: list of predictions to be ensembled
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        Return:
        ------
        y_pred: array_like, shape=(n_samples, n_class)
        The ensembled prediction.
        """
        Xs = np.hsplit(X, X.shape[1]/self.num_class)
        y_pred = np.zeros(Xs[0].shape)
        for i in range(len(self.w)):
            y_pred[:, i % self.num_class] += Xs[int(
                i / self.num_class)][:, i % self.num_class] * self.w[i]
        return y_pred

    def predict(self, X):
        """
        Use the weights learned in training to predict class probabilities.
        Parameters:
        ----------
        Xs: list of predictions to be blended.
        Each prediction is the solution of an individual classifier and has shape=(n_samples, n_classes).
        Return:
        ------
        y_pred: array_like, shape=(n_samples, n_class)
        The blended prediction.
        """
        y_pred = self.predict_proba(X)
        
        index=[]
        for i in y_pred:
            ind=pd.Series(i).idxmax()
            index.append(ind)

        return index
