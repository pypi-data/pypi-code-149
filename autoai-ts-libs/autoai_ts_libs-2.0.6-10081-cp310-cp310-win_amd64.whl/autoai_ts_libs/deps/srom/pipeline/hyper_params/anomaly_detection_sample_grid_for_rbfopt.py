# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Anomaly Detection Fine Grid for RBOpt.
Contains a dictionary of hyper-parameters for anomaly algorithms.
"""
PARAM_GRID = {}

# ************************************
# ******** Parameter Grid for GAM ****
# ************************************

# Isolation Forest
PARAM_GRID['isolationforest__base_learner__n_estimators'] = [10, 200, 'I']
PARAM_GRID['isolationforest__base_learner__max_samples'] = [0.1, 1000.0, 'R']
PARAM_GRID['isolationforest__base_learner__contamination'] = [0.1, 0.5, 'R']
PARAM_GRID['isolationforest__base_learner__max_features'] = [0.1, 5.0, 'R']

# Gaussian Mixture
PARAM_GRID['gaussianmixture__base_learner__n_components'] = [1, 10, 'I']
#PARAM_GRID['gaussianmixture__base_learner__covariance_type'] = ['full', 'tied', 'diag', 'spherical']
#PARAM_GRID['gaussianmixture__base_learner__init_params'] = ['kmeans', 'random']

# Bayesian Gaussian Mixture
PARAM_GRID['bayesiangaussianmixture__base_learner__n_components'] = [1, 10, 'I']
#PARAM_GRID['bayesiangaussianmixture__base_learner__covariance_type'] = ['full', 'tied', 'diag', 'spherical']
#PARAM_GRID['bayesiangaussianmixture__base_learner__init_params'] = ['kmeans', 'random']

# One Class SVM
#PARAM_GRID['oneclasssvm__base_learner__kernel'] = ['rbf', 'linear', 'poly', 'sigmoid']
PARAM_GRID['oneclasssvm__base_learner__nu'] = [0.1, 0.9, 'R']
PARAM_GRID['oneclasssvm__base_learner__degree'] = [1, 10, 'I']
PARAM_GRID['oneclasssvm__base_learner__gamma'] = [0.1, 0.3, 'R']
PARAM_GRID['oneclasssvm__base_learner__coef0'] = [0.0, 0.8, 'R']

# Nearest Neighbor Anomaly Model
PARAM_GRID['nearestneighboranomalymodel__base_learner__n_neighbors'] = [1, 20, 'I']

# lof Nearest Neighbor Anomaly Model
PARAM_GRID['lofnearestneighboranomalymodel__base_learner__n_neighbors'] = [1, 20, 'I']

# HotellingT2
PARAM_GRID['hotellingt2__base_learner__sliding_window_size'] = [7, 24, 'I']
PARAM_GRID['hotellingt2__base_learner__sliding_window_data_cutoff'] = [5, 15, 'I']

# AnomalyPCA_T2
#PARAM_GRID['anomalypca_t2__base_learner__scale'] = [True, False]
PARAM_GRID['anomalypca_t2__base_learner__variance_threshold'] = [0.7, 0.95, 'R']
PARAM_GRID['anomalypca_t2__base_learner__alpha'] = [0.05, 0.1, 'R']

# AnomalyPCA_Q
#PARAM_GRID['anomalypca_q__base_learner__scale'] = [True, False]
PARAM_GRID['anomalypca_q__base_learner__variance_threshold'] = [0.1, 0.9, 'R']
PARAM_GRID['anomalypca_q__base_learner__alpha'] = [0.05, 0.1, 'R']

# ************************************
# ******** Parameter Grid for GGM ****
# ************************************

# Elliptic Envelope
PARAM_GRID['ellipticenvelope__base_learner__support_fraction'] = [0.1, 0.9, 'R']
PARAM_GRID['ellipticenvelope__base_learner__contamination'] = [0.1, 0.5, 'R']

# MinCovDet
PARAM_GRID['mincovdet__base_learner__support_fraction'] = [0.1, 0.9, 'R']

# Shrunk Covariance
PARAM_GRID['shrunkcovariance__base_learner__shrinkage'] = [0.1, 0.9, 'R']

# AnomalyGraphLasso
#PARAM_GRID['anomalygraphLasso__base_learner__mode'] = ['cd', 'lars']
PARAM_GRID['anomalygraphLasso__base_learner__max_iter'] = [100, 1000, 'I']
PARAM_GRID['anomalygraphLasso__base_learner__alpha'] = [0.1, 1.0, 'R']

# GraphPgscps
PARAM_GRID['graphpgscps__base_learner__sparsity'] = [10, 400, 'I']
PARAM_GRID['graphpgscps__base_learner__reg'] = [0.1, 0.9, 'R']

# EmpiricalCovariance
#PARAM_GRID['empiricalcovariance__base_learner__store_precision'] = [True, False]

# QuicGraphLasso
PARAM_GRID['quicgraphlasso__base_learner__lam'] = [0.1, 0.9, 'R']
PARAM_GRID['quicgraphlasso__base_learner__max_iter'] = [100, 1000, 'I']
#PARAM_GRID['quicgraphlasso__base_learner__init_method'] = ['cov', 'corrcoef']

# OAS
#PARAM_GRID['oas__base_learner__store_precision'] = [True, False]

# LedoitWolf
#PARAM_GRID['ledoitwolf__base_learner__store_precision'] = [True, False]
