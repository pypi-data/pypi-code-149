# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Clustering Fine Grid: Contains a dictionary of hyper-parameters for Clustering algorithms.
"""
import numpy as np

PARAM_GRID = {}

# 1 BayesianGaussianMixture
PARAM_GRID["bayesiangaussianmixture__n_components"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PARAM_GRID["bayesiangaussianmixture__covariance_type"] = [
    "full",
    "tied",
    "diag",
    "spherical",
]
PARAM_GRID["bayesiangaussianmixture__init_params"] = ["kmeans", "random"]
PARAM_GRID["bayesiangaussianmixture__weight_concentration_prior_type"] = [
    "dirichlet_process",
    "dirichlet_distribution",
]

# 2 GaussianMixture
PARAM_GRID["gaussianmixture__n_components"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PARAM_GRID["gaussianmixture__covariance_type"] = ["full", "tied", "diag", "spherical"]
PARAM_GRID["gaussianmixture__init_params"] = ["kmeans", "random"]

# 3 AgglomerativeClustering
PARAM_GRID["agglomerativeclustering__affinity"] = [
    "euclidean",
    "l1",
    "l2",
    "manhattan",
    "cosine",
]
PARAM_GRID["agglomerativeclustering__linkage"] = [
    "ward",
    "complete",
    "average",
    "single",
]

# 4 KMeans
PARAM_GRID["kmeans__init"] = ["random", "k-means++"]
