# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Some of the functions (we should include which) are not callable from Sklearn package, so have to redefine the function in this module.
"""

import math
import warnings
import numpy as np
from scipy import linalg
from sklearn.covariance import empirical_covariance
from scipy.linalg import eigvalsh


def log_likelihood(emp_cov, precision):
    """
    Computes the empirical expected log likelihood.

    Args:
        emp_cov (ndarray, required): Maximum likelihood estimator of covariance
        precision (ndarray, required): Precision matrix of the covariance model,
                                        of the same shape as emp_cov

    Returns:
        log_likelihood_ (float) : Empirical expected log likelihood

    """
    from sklearn.utils.extmath import fast_logdet

    p = precision.shape[0]
    log_likelihood_ = (-1 * np.sum(emp_cov * precision)) + fast_logdet(precision)
    log_likelihood_ -= p * np.log(2 * np.pi)
    log_likelihood_ /= 2.0
    return log_likelihood_


def compute_KL_divergence(
    train_covariance, train_precision, test_covariance, test_precision, feature_index
):
    """
    Computes KL Divergence between train and test models along an axis.

    Args:
        train_covariance (numpy.ndarray, required): Covariance matrix of the trained model
        train_precision (numpy.ndarray, required): Precision matrix of the trained model
        test_covariance (numpy.ndarray, required): Covariance matrix of the test model
        test_precision (numpy.ndarray, required): Precision  matrix of the test model
        feature_index (int, required): Index of the feature along which KL Divergence is computed

    Returns:

    """

    # get the indices 1[,..,n_features] excluding i
    n_features = train_covariance.shape[0]
    i = feature_index
    indices = np.ma.array(list(range(n_features)), mask=False)
    indices.mask[i] = True
    S = indices.compressed()

    d1 = (
        np.dot(train_covariance[i, S], test_precision[i, S] - train_precision[i, S])
        + 1.0
        * np.dot(
            np.dot(test_precision[i, S], train_covariance[S][:, S]),
            test_precision[i, S],
        )
        / (2 * test_precision[i, i])
        - 1.0
        * np.dot(
            np.dot(train_precision[i, S], train_covariance[S][:, S]),
            train_precision[i, S],
        )
        / (2 * train_precision[i, i])
        + 1.0 * np.log(1.0 * train_precision[i, i] / test_precision[i, i]) / 2
        + 1.0
        * train_covariance[i, i]
        * (test_precision[i, i] - train_precision[i, i])
        / 2
    )

    d2 = (
        np.dot(test_covariance[i, S], train_precision[i, S] - test_precision[i, S])
        + 1.0
        * np.dot(
            np.dot(train_precision[i, S], test_covariance[S][:, S]),
            train_precision[i, S],
        )
        / (2 * train_precision[i, i])
        - 1.0
        * np.dot(
            np.dot(test_precision[i, S], test_covariance[S][:, S]), test_precision[i, S]
        )
        / (2 * test_precision[i, i])
        + 1.0 * np.log(1.0 * test_precision[i, i] / train_precision[i, i]) / 2
        + 1.0
        * test_covariance[i, i]
        * (train_precision[i, i] - test_precision[i, i])
        / 2
    )

    return np.maximum(d1, d2)


def compute_stochstic_nearest_neighbors(
    train_covariance,
    train_precision,
    test_covariance,
    test_precision,
    feature_index,
    train_sample_cov,
    test_sample_cov,
    threshold=1e-4,
):
    """
    Computes the stochastic nearest neighbors.

    Args:
        train_covariance (numpy.ndarray, optional): Covariance matrix of trained model
        train_precision (numpy.ndarray, required): Precision matrix of trained model
        test_covariance (numpy.ndarray, optional): Covariance matrix of test model
        test_precision (numpy.ndarray, required): Precision matrix of test model
        feature_index (int, required): Index of the feature along which stochastic nearest
                                    neighbors are to be computed
        train_sample_cov (numpy.ndarray, required): Covariance matrix of train samples
        test_sample_cov (numpy.ndarray, required): Covariance matrix of test samples
        threshold (float, optional): Threshold for scores. Defaults to 1e-4

    Returns:
        Stochastic nearest neighbors.
    """

    i = feature_index
    I_A = train_precision[i, :].copy()
    I_A[np.abs(I_A) < threshold] = 0
    I_A[np.abs(I_A) >= threshold] = 1
    d1 = np.abs(np.dot(I_A, (train_sample_cov[:, i] - test_sample_cov[:, i]))) / np.abs(
        (1 + np.dot(I_A, train_sample_cov[:, i]))
        * (1 + np.dot(I_A, test_sample_cov[:, i]))
    )

    I_B = test_precision[i, :].copy()
    I_B[np.abs(I_B) < threshold] = 0
    I_B[np.abs(I_B) >= threshold] = 1
    d2 = np.abs(np.dot(I_B, (train_sample_cov[:, i] - test_sample_cov[:, i]))) / np.abs(
        (1 + np.dot(I_B, train_sample_cov[:, i]))
        * (1 + np.dot(I_B, test_sample_cov[:, i]))
    )

    return np.maximum(d1, d2)


def is_invertible(a):
    """
    Checks if a matrix is invertible.

    Args:
        a (numpy.ndarray, required): Matrix to check for invertibility

    Returns:
        boolean: Denotes if the matrix is invertible

    """
    print(np.linalg.matrix_rank(a))
    print(np.linalg.det(a))
    return a.shape[0] == a.shape[1] and np.linalg.matrix_rank(a) == a.shape[0]


def compute_KL_divergence_between_distribution(
    train_covariance,
    train_precision,
    test_covariance,
    test_precision,
    mean_train,
    mean_test,
):
    """
    Computes KL divergence between the distribution of data.

    Args:
        train_covariance (numpy.ndarray, required): Covariance matrix of train model
        train_precision (numpy.ndarray, optional): Precision matrix of train model
        test_covariance (numpy.ndarray, required): Covariance matrix of test model
        test_precision (numpy.ndarray, required): Precision matrix of test model
        mean_train (numpy.ndarray, required): Arithmetic mean of train data along an axis
        mean_test (numpy.ndarray, required): Arithmetic mean of test data along an axis

    Returns:
        final_part (numpy.ndarray): KL divergence between the distribution of data

    """
    final_part = np.NAN
    try:
        n_features = train_covariance.shape[0]
        part1 = np.trace(np.dot(test_precision, train_covariance))
        part2 = np.dot(
            np.dot((mean_test - mean_train).T, test_precision), (mean_test - mean_train)
        )
        # print part2
        # final_part = part1 + part2 - n_features
        final_part = (
            part1
            + part2
            - n_features
            + math.log(
                0.0001
                + (np.linalg.det(test_covariance) / np.linalg.det(train_covariance))
            )
        )
        # print final_part
    except IOError:
        # add a logger message
        pass
    except ValueError:
        # add a logger message
        pass

    return final_part


def compute_mahalanobis(observations, precision, location):
    """
    Computes Mahalanobis distance.

    Args:
        observations (numpy.ndarray, required): X observations
        precision (numpy.ndarray, required): Precision matrix of train model
        location (float, required): Last observation in the test dataset for finding the distance

    Returns:
        mahalanobis_dist: The mahalonobis distance
    """
    # compute mahalanobis distances
    centered_obs = observations - location
    mahalanobis_dist = np.sum(np.dot(centered_obs, precision) * centered_obs, 1)
    return mahalanobis_dist


def compute_error_norm(
    comp_cov, train_covariance, norm="frobenius", scaling=True, squared=True
):
    """
    Computes the frobenius or spectral error norm.

    Args:
        comp_cov (numpy.ndarray, required): Covariance matrix of test model
        train_covariance (numpy.ndarray, required): Covariance matrix of train model
        norm (string, optional): The type of norm to compute, options are "frobenius" and "spectral".
                                Defaults to "frobenius" norm.
        scaling (boolean, optional): Option to scale the error norm. Defaults to `True`.
        squared (boolean, optional): Option to get squared norm. Defaults to `True`.

    Returns:
        result (numpy.ndarray): The error norm

    """
    # compute the error
    error = comp_cov - train_covariance
    # compute the error norm
    if norm == "frobenius":
        squared_norm = np.sum(error ** 2)
    elif norm == "spectral":
        try:
            squared_norm = np.amax(linalg.svdvals(np.dot(error.T, error)))
        except:
            return np.NAN
    else:
        raise NotImplementedError("Only spectral and frobenius norms are implemented")
    # optionally scale the error norm
    if scaling:
        squared_norm = squared_norm / error.shape[0]
    # finally get either the squared norm or the norm
    if squared:
        result = squared_norm
    else:
        result = np.sqrt(squared_norm)
    return result


def compute_score(X_test, train_precision, location, y=None):
    """
    Computes the score for log likelihood of the data.
    Args:
        X_test (numpy.ndarray, required): Data to compute empirical covariance and log likelihood for
        train_precision (numpy.ndarray, required): Precision matrix of the train model
        location (float, required): Last observation in the test dataset for finding the distance
        y (numpy.ndarray, optional): Labels for the data. Defaults to `None`

    Returns:
        res (float) : Empirical expected log likelihood of the data

    """
    # compute empirical covariance of the test set
    test_cov = empirical_covariance(X_test - location, assume_centered=True)
    # compute log likelihood
    res = log_likelihood(test_cov, train_precision)
    return res


def compute_kullback_distance(train_covariance, test_covariance):
    """
    Kullback leibler divergence between two covariance matrices train_covariance and test_covariance.

    Args:
        train_covariance: First covariance matrix
        test_covariance: Second covariance matrix
        
    Returns: 
        (float) Kullback leibler divergence between train_covariance and test_covariance

    """
    dim = train_covariance.shape[0]
    logdet = np.log(np.linalg.det(test_covariance) / np.linalg.det(train_covariance))
    kl = (
        np.trace(np.dot(np.linalg.inv(test_covariance), train_covariance))
        - dim
        + logdet
    )
    return 0.5 * kl


def compute_sym_kullback_distance(train_covariance, test_covariance):
    """
    Symmetric Kullback leibler divergence between two covariance matrices train_covariance and test_covariance.

    Args:
        train_covariance: First covariance matrix
        test_covariance: Second covariance matrix
        
    Returns: 
        (float) Kullback leibler divergence between train_covariance and test_covariance
    
    """
    return compute_kullback_distance(
        train_covariance, test_covariance
    ) + compute_kullback_distance(test_covariance, train_covariance)


def compute_euclidean_distance(train_covariance, test_covariance):
    """
    Compute Euclidean Distance between two covariance matrices train_covariance and test_covariance.

    Args:
        train_covariance: First covariance matrix
        test_covariance: Second covariance matrix
        
    Returns: 
        (float) Euclidean Distance between train_covariance and test_covariance
    
    """
    return np.linalg.norm(train_covariance - test_covariance, ord="fro")


def compute_riemannian_distance(train_covariance, test_covariance):
    """
    Compute Riemannian Distance between two covariance matrices train_covariance and test_covariance.

    Args:
        train_covariance: First covariance matrix
        test_covariance: Second covariance matrix
        
    Returns: 
        (float) Riemannian Distance between train_covariance and test_covariance
    
    """
    return np.sqrt((np.log(eigvalsh(train_covariance, test_covariance)) ** 2).sum())


def compute_logdet_distance(train_covariance, test_covariance):
    """
    Compute Log-Det Distance between two covariance matrices train_covariance and test_covariance.

    Args:
        train_covariance: First covariance matrix
        test_covariance: Second covariance matrix
        
    Returns:
        (float) LogDet Distance between train_covariance and test_covariance
    
    """
    return np.sqrt(
        np.log(np.linalg.det((train_covariance + test_covariance) / 2.0))
        - 0.5 * np.log(np.linalg.det(train_covariance) * np.linalg.det(test_covariance))
    )

