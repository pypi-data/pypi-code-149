# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Sparse Gauss
"""
import numpy as np
from sklearn.covariance import shrunk_covariance, graphical_lasso


def l0_weights(H, tau=0.1, eps=1e-4):
    """
    Solve a Convex MIP to obtain an eps-sparse vector of mixture
    probabilities minimizing negative log-likelihood.
    Args:
        H (list, required): vector of expected log-likelihoods for each mixture component
        tau (integer, required): l0 regularization
        eps (integer, required): sparsity threshold
    Returns:
        pi_star: eps-sparse vector of mixture probabilities
    """
    if len(H.shape) == 2:
        a = np.sum(H, 0) / H.shape[0]
    else:
        a = H
    # a = H
    if np.sum(a) == 0:
        raise ZeroDivisionError("division by zero")
    a = a / np.sum(a)
    N = len(a)

    # Sort the vector a and get the permutation
    a_sorted = np.sort(a)
    idx_sort = np.argsort(a)
    idx_rev = np.argsort(idx_sort)

    # Find the level of eps-sparsity of the vector a
    # and the corresponding objective value
    init_sparsity = len(a_sorted[np.where(a_sorted <= eps)])
    init_obj = -1 * np.sum(a * np.log(a + 1e-100)) + tau * (N - init_sparsity)

    objective = init_obj * np.ones(N)
    pi_all_runs = np.zeros((N, N))

    # Run through each value of the sparsity parameter and
    # solve a convex program
    for k in range(N):
        pi, f_opt, _m_opt = continuous_subprob(a_sorted, k, tau, eps, init_obj, init_sparsity)
        objective[k] = f_opt
        pi_all_runs[:, k] = pi.T

    # Find the sparsity level which corresponds to the lowest
    # objective value
    opt_sparsity = np.max(np.where(objective == np.min(objective))[0])
    pi_star = pi_all_runs[idx_rev, opt_sparsity]
    return pi_star


def srom_graph_lasso_method(cov_k, alpha_k):
    """
    Helper class to deal with graph lasso limitation
    cov_k: covariance matrix, 
    alpha_k: The regularization parameter, positive float

    It returns covariance matrix and precision matrix
    """
    try:
        return graphical_lasso(cov_k, alpha_k)
    except FloatingPointError:
        done = True
        shrinkage_th = 0.1
        shrunk_cov = None
        while done:
            try:
                shrunk_cov = shrunk_covariance(cov_k, shrinkage=shrinkage_th)
                tmp_result = graphical_lasso(shrunk_cov, alpha=alpha_k)
                return tmp_result
            except FloatingPointError:
                shrinkage_th = shrinkage_th + 0.1
                if shrinkage_th >= 1:
                    done = False
    raise Exception('Graph Lasso Method is unable to identify result')


def continuous_subprob(a, sparsity, tau, eps, init_obj, init_sparsity):
    """
    Solve a convex program to obtain an eps-sparse vector of mixture
    probabilities for a given sparsity level
    Args:
        a (list, required): sorted, normalized vector of log-likelihoods
        sparsity (integer, required): sparsity level
        tau (integer, required): l0 regularization parameter
        eps (integer, required): sparsity threshold parameter
        init_obj (integer, required): objective value for vector a
        init_sparsity (integer, required): sparsity value for vector a
    Returns (tuple):
        pi: eps-sparse vector of mixture probabilities
        f_opt: objective value at pi
        m_opt: sparsity level of pi
    """
    N = len(a)
    pi = np.zeros(N)

    if sparsity == 0:
        pi = a
        m_opt = init_sparsity
        f_opt = init_obj
    elif a[sparsity - 1] <= eps:
        pi = a
        m_opt = init_sparsity
        f_opt = init_obj
    else:
        breakpoint = -1
        for j in range(sparsity, 0, -1):
            if a[j - 1] >= eps:
                pi[j - 1] = eps
            else:
                breakpoint = j
                break
        if breakpoint == -1:
            lambda_inv = (1 - sparsity * eps) / (1 - np.sum(a[:sparsity]))
            pi[sparsity:] = lambda_inv*a[sparsity:]
        else:
            while breakpoint >= 0:
                lambda_inv = (1 - (sparsity - breakpoint) * eps) / \
                             (1 - np.sum(a[breakpoint:sparsity]))
                pi[breakpoint - 1] = a[breakpoint - 1] * lambda_inv
                if pi[breakpoint - 1] <= eps:
                    pi[:breakpoint] = lambda_inv * a[:breakpoint]
                    pi[sparsity:] = lambda_inv * a[sparsity:]
                    breakpoint = -1
                else:
                    pi[breakpoint - 1] = eps
                    breakpoint = breakpoint - 1
        m_opt = len(pi[np.where(pi <= eps)])
        f_opt = -1 * np.sum(a * np.log(pi + 1e-100)) + tau * (N - m_opt)

    return pi, f_opt, m_opt


# following functions should be made part of "distance_metric_utils.py" of srom core packages
def log_gmm_likelihood(X, mus, Lambdas):
    """
    <function description>
    Args:
        X (<datatype>, required): <description>
        mus (<datatype>, required): <description>
        Lambdas (<datatype>, required): <description>
    Returns:
        <description>
    """
    num_clusters = mus.shape[0]
    num_samples = X.shape[0]
    LL = np.zeros((num_samples, num_clusters))
    for k in range(num_clusters):
        LL[:, k] = 0.5 * np.log(np.linalg.det(Lambdas[k, :, :])) - 0.5 * \
                    np.sum(np.dot(X - mus[k, :], Lambdas[k, :, :]) * (X - mus[k, :]), 1)
    return LL


def log_gauss_likelihood(x, mu, Lambda):
    """
    <function description>
    Args:
        X (<datatype>, required): <description>
        mu (<datatype>, required): <description>
        Lambda (<datatype>, required): <description>
    Returns:
        <description>
    """
    return 0.5 * np.log(np.linalg.det(Lambda)) - 0.5 * \
        np.trace(np.dot(Lambda, np.outer(x - mu, x - mu)))


def softmax(x):
    """
    <function description>
    Args:
        X (<datatype>, required): <description>
    Returns:
        <description>
    """
    if len(x.shape) == 1:
        x = np.reshape(x, (1, x.shape[0]))
    e_x = np.exp(x - np.reshape(np.max(x, 1), (x.shape[0], 1)))
    return np.squeeze(e_x / np.reshape(np.sum(e_x, 1), (x.shape[0], 1)))
