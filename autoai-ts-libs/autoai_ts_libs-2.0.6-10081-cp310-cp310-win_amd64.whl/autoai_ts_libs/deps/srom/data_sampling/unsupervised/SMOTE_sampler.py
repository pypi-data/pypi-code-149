# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""SMOTE Sampler Module.

.. moduleauthor:: SROM Team

"""


import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.neighbors import NearestNeighbors


def sample(
    X,
    y,
    proportion=1.0,
    n_neighbors=5,
    w=0.005,
    n_jobs=1,
    random_state=None,
    threshold=2,
):
    """
    sample generation.
    Args:
        X (np.ndarray): training set
        y (np.array): target labels
    Returns:
        (np.ndarray, np.array): the extended training set and target labels
    """

    def _sample_between_points(x, y):
        """
            sample between points method.
        """
        return x + (y - x) * random_state.random_sample()

    def _det_n_to_sample(strategy, n_maj, n_min):
        """
            det n to sample
        """
        if isinstance(strategy, float) or isinstance(strategy, int):
            return max([0, int((n_maj - n_min) * strategy)])
        else:
            m = "Value %s for parameter strategy is not supported" % strategy
            raise ValueError(m)

    if random_state is None:
        random_state = np.random
    elif isinstance(random_state, int):
        random_state = np.random.RandomState(random_state)
    elif isinstance(random_state, np.random.RandomState):
        random_state = random_state
    elif random_state is np.random:
        random_state = random_state
    else:
        raise ValueError("random state cannot be initialized by " + str(random_state))

    unique, counts = np.unique(y, return_counts=True)
    class_stats = dict(zip(unique, counts))
    min_label = unique[0] if counts[0] < counts[1] else unique[1]
    maj_label = unique[1] if counts[0] < counts[1] else unique[0]

    if class_stats[min_label] < threshold:
        m = "The number of minority samples (%d) is not enough " "for sampling"
        m = m % class_stats[min_label]
        return X.copy(), y.copy()

    n_to_sample = _det_n_to_sample(
        proportion,
        class_stats[maj_label],
        class_stats[min_label],
    )

    if n_to_sample == 0:

        return X.copy(), y.copy()

    bound_set = []
    pos_set = []

    X_min_indices = np.where(y == min_label)[0]
    X_min = X[X_min_indices]

    dm = pairwise_distances(X, X)
    d_max = np.max(dm, axis=1)
    max_dist = np.max(dm)
    np.fill_diagonal(dm, max_dist)
    d_min = np.min(dm, axis=1)

    delta = d_min + w * (d_max - d_min)

    n_neighbors = min([n_neighbors + 1, len(X)])
    nn = NearestNeighbors(n_neighbors=n_neighbors, n_jobs=n_jobs)
    nn.fit(X)
    for i in range(len(X)):
        indices = nn.radius_neighbors(
            X[i].reshape(1, -1), delta[i], return_distance=False
        )

        n_minority = np.sum(y[indices[0]] == min_label)
        n_majority = np.sum(y[indices[0]] == maj_label)
        if y[i] == min_label and not n_minority == len(indices[0]):
            bound_set.append(i)
        elif y[i] == maj_label and n_majority == len(indices[0]):
            pos_set.append(i)

    bound_set = np.array(bound_set)
    pos_set = np.array(pos_set)

    if len(pos_set) == 0 or len(bound_set) == 0:
        return X.copy(), y.copy()

    n_neighbors = min([len(X_min), n_neighbors + 1])
    nn = NearestNeighbors(n_neighbors=n_neighbors, n_jobs=n_jobs)
    nn.fit(X_min)
    distances, indices = nn.kneighbors(X[bound_set])

    samples = []
    trials = 0
    while len(samples) < n_to_sample:
        idx = random_state.choice(len(bound_set))
        random_neighbor_idx = random_state.choice(indices[idx][1:])
        x_new = _sample_between_points(X[bound_set[idx]], X_min[random_neighbor_idx])

        dist_from_pos_set = np.linalg.norm(X[pos_set] - x_new, axis=1)
        if np.all(dist_from_pos_set > delta[pos_set]):
            samples.append(x_new)
        trials = trials + 1
        if trials > 1000 and len(samples) == 0:
            trials = 0
            w = w * 0.9

    return (
        np.vstack([X, np.vstack(samples)]),
        np.hstack([y, np.repeat(min_label, len(samples))]),
    )
