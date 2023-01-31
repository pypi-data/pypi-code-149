# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


# Licensed Materials - Property of IBM
# IBM Maximo Production Optimization SaaS
# IBM Maximo Production Optimization On-premises
# (C) Copyright IBM Corp. 2019  All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or disclosure
#  restricted by GSA ADP Schedule Contract with IBM Corp.

"""
Classification Fine Grid for RBOpt.
Contains a dictionary of hyper-parameters of classification algorithms.
"""
# important links
# TPOT - https://github.com/rhiever/tpot/blob/master/tpot/config/classifier.py
# HyperOpt https://github.com/hyperopt/hyperopt-sklearn/blob/master/hpsklearn/components.py

import numpy as np
PARAM_GRID = {}

# 1 BernoulliNB - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/BernoulliNB.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/bernoulli_nb.py
PARAM_GRID['bernoullinb__alpha'] = [1e-3, 100.0, 'R']
#PARAM_GRID['bernoullinb__fit_prior'] = [True, False]
PARAM_GRID['bernoullinb__binarize'] = [0., 1.0, 'R']

# 2 MultinomialNB - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/MultinomialNB.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/multinomial_nb.py
PARAM_GRID['multinomialnb__alpha'] = [1e-3, 100.0, 'R']
#PARAM_GRID['multinomialnb__fit_prior'] = [True, False]

# 3 DecisionTreeClassifier - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/DecisionTreeClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/decision_tree.py
#PARAM_GRID['decisiontreeclassifier__criterion'] = ["gini", "entropy"]
PARAM_GRID['decisiontreeclassifier__max_depth'] = [1, 15, 'I']
PARAM_GRID['decisiontreeclassifier__min_samples_split'] = [2, 20, 'I']
PARAM_GRID['decisiontreeclassifier__min_samples_leaf'] = [1, 20, 'I']
PARAM_GRID['decisiontreeclassifier__max_features'] = [0.1, 0.75, 'R']
PARAM_GRID['decisiontreeclassifier__min_impurity_decrease'] = [0.0, 0.00475, 'R']

# 4 ExtraTreesClassifier - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/ExtraTreesClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/extra_trees.py
PARAM_GRID['extratreesclassifier__n_estimators'] = [10, 500, 'I']
#PARAM_GRID['extratreesclassifier__criterion'] = ["gini", "entropy"]
PARAM_GRID['extratreesclassifier__max_features'] = [0.1, 0.75, 'R']
PARAM_GRID['extratreesclassifier__min_samples_split'] = [2, 20, 'I']
PARAM_GRID['extratreesclassifier__min_samples_leaf'] = [1, 20, 'I']
#PARAM_GRID['extratreesclassifier__bootstrap'] = [True, False]

# 5 RandomForestClassifier - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/RandomForestClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/random_forest.py
PARAM_GRID['randomforestclassifier__n_estimators'] = [10, 500, 'I']
#PARAM_GRID['randomforestclassifier__criterion'] = ["gini", "entropy"]
PARAM_GRID['randomforestclassifier__min_samples_split'] = [2, 20, 'I']
PARAM_GRID['randomforestclassifier__min_samples_leaf'] = [1, 20, 'I']
#PARAM_GRID['randomforestclassifier__bootstrap'] = [True, False]
PARAM_GRID['randomforestclassifier__max_features'] = [0.1, 0.75, 'R']
PARAM_GRID['randomforestclassifier__min_impurity_decrease'] = [0.0, 0.00475, 'R']

# 6 GradientBoostingClassifier - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/GradientBoostingClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/gradient_boosting.py
PARAM_GRID['gradientboostingclassifier__n_estimators'] = [10, 500, 'I']
PARAM_GRID['gradientboostingclassifier__learning_rate'] = [1e-3, 100.0, 'R']
PARAM_GRID['gradientboostingclassifier__subsample'] = [0.05, 1, 'R']
PARAM_GRID['gradientboostingclassifier__min_samples_split'] = [2, 20, 'I']
PARAM_GRID['gradientboostingclassifier__min_samples_leaf'] = [1, 20, 'I']
PARAM_GRID['gradientboostingclassifier__max_depth'] = [1, 10, 'I']
PARAM_GRID['gradientboostingclassifier__min_impurity_decrease'] = [0.0, 0.00475, 'R']
PARAM_GRID['gradientboostingclassifier__max_features'] = [0.1, 0.75, 'R']
#PARAM_GRID['gradientboostingclassifier__loss'] = ['deviance', 'exponential']

# 7 KNeighborsClassifier -  https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/KNeighborsClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/k_nearest_neighbors.py
PARAM_GRID['kneighborsclassifier__n_neighbors'] = [1, 100, 'I']
#PARAM_GRID['kneighborsclassifier__weights'] = ["uniform", "distance"]
PARAM_GRID['kneighborsclassifier__p'] = [1, 2, 'I']

# 8 Linear SVC - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/LinearSVC.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/libsvm_svc.py
#PARAM_GRID['linearsvc__penalty'] = ["l1", "l2"]
#PARAM_GRID['linearsvc__loss'] = ["hinge", "squared_hinge"]
#PARAM_GRID['linearsvc__fit_intercept'] = [True, False]
#PARAM_GRID['linearsvc__dual'] = [True, False]
PARAM_GRID['linearsvc__tol'] = [1e-5, 1e-1, 'R']
PARAM_GRID['linearsvc__C'] = [1e-4, 25.0, 'R']

# 9 LogisticRegression - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/LogisticRegression.py
# No AutoML
#PARAM_GRID['logisticregression__penalty'] = ["l1", "l2"]
PARAM_GRID['logisticregression__C'] = [1e-4, 25.0, 'R']
#PARAM_GRID['logisticregression__dual'] = [True, False]
#PARAM_GRID['logisticregression__fit_intercept'] = [True, False]

# 10 XGBClassifier - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/XGBClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/xgradient_boosting.py
PARAM_GRID['xgbclassifier__n_estimators'] = [10, 500, 'I']
PARAM_GRID['xgbclassifier__max_depth'] = [1, 50, 'I']
PARAM_GRID['xgbclassifier__learning_rate'] = [1e-3, 100.0, 'R']
PARAM_GRID['xgbclassifier__subsample'] = [0.05, 1.0, 'R']
PARAM_GRID['xgbclassifier__min_child_weight'] = [1, 20, 'I']
PARAM_GRID['xgbclassifier__nthread'] = [-1, 1, 'I']
PARAM_GRID['xgbclassifier__gamma'] = [0., 0.5, 'R']
PARAM_GRID['xgbclassifier__colsample_bylevel'] = [1, 2, 'I']
PARAM_GRID['xgbclassifier__colsample_bytree'] = [1, 2, 'I']
PARAM_GRID['xgbclassifier__max_delta_step'] = [0, 1, 'I']

# 11 SGDClassifier - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/SGDClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/sgd.py
#PARAM_GRID['sgdclassifier__loss'] = ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron']
#PARAM_GRID['sgdclassifier__penalty'] = ['none', 'l2', 'l1', 'elasticnet']
PARAM_GRID['sgdclassifier__n_iter'] = [5, 10, 'I']
PARAM_GRID['sgdclassifier__alpha'] = [0.000001, 0.01, 'R']
#PARAM_GRID['sgdclassifier__learning_rate'] = ['constant', 'optimal', 'invscaling']
#PARAM_GRID['sgdclassifier__fit_intercept'] = [True, False]
PARAM_GRID['sgdclassifier__l1_ratio'] = [0., 1.0, 'R']
PARAM_GRID['sgdclassifier__eta0'] = [0.01, 100.0, 'R']
PARAM_GRID['sgdclassifier__power_t'] = [0., 100.0, 'R']
# max_iter and tol parameters have been added in 0.19
# If both are left unset, they default to max_iter=5 and tol=None.
# From 0.21, default max_iter will be 1000, and default tol will be 1e-3.
# PARAM_GRID['sgdclassifier__max_iter'] = [5]
# PARAM_GRID['sgdclassifier__tol'] = [None]

# 12 SVC - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/SVC.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/libsvm_svc.py
PARAM_GRID['svc__C'] = [0.01, 100., 'R']
PARAM_GRID['svc__gamma'] = [0.01, 100., 'R']
#PARAM_GRID['svc__kernel'] = ['poly', 'rbf', 'sigmoid']
PARAM_GRID['svc__degree'] = [2, 3, 'I']
PARAM_GRID['svc__coef0'] = [0.0, 100.0, 'R']
#PARAM_GRID['svc__probability'] = [True]

# 13 Perceptron
#PARAM_GRID['perceptron__penalty'] = ['none', 'l2', 'l1', 'elasticnet']
PARAM_GRID['perceptron__n_iter'] = [5, 10, 'I']

# 14 MLP Classifier
PARAM_GRID['mlpclassifier__number_of_hidden_layers'] = [1, 10, 'I']
PARAM_GRID['mlpclassifier__number_of_neurons_in_hidden_layers'] = [0, 200, 'I']
PARAM_GRID['mlpclassifier__alpha'] = [1e-05, 1e-01, 'R']
# PARAM_GRID['mlpclassifier__activation'] = ['identity','logistic','tanh','relu']

# 15 PassiveAggressiveClassifier https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/PassiveAggressiveClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/passive_aggressive.py
#PARAM_GRID['passiveaggressiveclassifier__fit_intercept'] = [True, False]
PARAM_GRID['passiveaggressiveclassifier__C'] = [0.000001, 100.0, 'R']
#PARAM_GRID['passiveaggressiveclassifier__loss'] = ['hinge', 'squared_hinge']

# 16 AdaBoostClassifier - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/AdaBoostClassifier.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/adaboost.py
PARAM_GRID['adaboostclassifier__learning_rate'] = [0.01, 100.0, 'R']
PARAM_GRID['adaboostclassifier__n_estimators'] = [10, 500, 'I']
#PARAM_GRID['adaboostclassifier__algorithm'] = ["SAMME.R", "SAMME"]
PARAM_GRID['adaboostclassifier__max_depth'] = [1, 15, 'I']
#PARAM_GRID['adaboostclassifier__loss'] = ['exponential', 'square', 'linear']


# 17 GaussianNB https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/GaussianNB.py
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/gaussian_nb.py
# None

# LDA
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/lda.py
PARAM_GRID['lineardiscriminantanalysis__shrinkage'] = [0.01, 0.99, 'R']
#PARAM_GRID['lineardiscriminantanalysis__shrinkage_factor'] = [0,0.2,0.5,0.7,0.9,1.0]
PARAM_GRID['lineardiscriminantanalysis__n_components'] = [1, 250, 'I']
PARAM_GRID['lineardiscriminantanalysis__tol'] = [1e-5, 1e-1, 'R']

# QDA
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/qda.py
PARAM_GRID['quadraticdiscriminantanalysis__reg_param'] = [0.0, 1.0, 'R']

# GaussianProcessClassifier
# from sklearn.gaussian_process.kernels import ConstantKernel, RBF, RationalQuadratic, ExpSineSquared
# ker_rbf = ConstantKernel(1.0, constant_value_bounds="fixed") * RBF(1.0, length_scale_bounds="fixed")
# ker_rq = ConstantKernel(1.0, constant_value_bounds="fixed") * RationalQuadratic(alpha=0.1, length_scale=1)
# ker_expsine = ConstantKernel(1.0, constant_value_bounds="fixed") * ExpSineSquared(1.0, 5.0, periodicity_bounds=(1e-2, 1e1))
# PARAM_GRID['gaussianprocessclassifier__kernel'] = [None, ker_rbf, ker_rq]
# PARAM_GRID['gaussianprocessclassifier__optimizer'] = ['fmin_l_bfgs_b']
PARAM_GRID['gaussianprocessclassifier__n_restarts_optimizer'] = [1, 3, 'I'] 
# PARAM_GRID['gaussianprocessclassifier__copy_X_train'] = [True]
PARAM_GRID['gaussianprocessclassifier__max_iter_predict'] = [50, 150, 'I'] 
# PARAM_GRID['gaussianprocessclassifier__random_state'] = [0]

# RidgeClassifier
PARAM_GRID['ridgeclassifier__alpha'] = [0, 1, 'R']
# PARAM_GRID['ridgeclassifier__kernel'] = ['rbf','linear']
PARAM_GRID['ridgeclassifier__gamma'] = [1e-3, 1e-4, 'R']
PARAM_GRID['ridgeclassifier__C'] = [1, 1000, 'I']
# PARAM_GRID['ridgeclassifier__fit_intercept'] = [True, False]
# PARAM_GRID['ridgeclassifier__fit_solver'] = ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga']

# BaggingClassifier
PARAM_GRID['baggingclassifier__n_estimators'] = [10, 100, 'I']
PARAM_GRID['baggingclassifier__max_samples'] = [0.2, 1.0, 'R']
PARAM_GRID['baggingclassifier__max_features'] = [0.2, 1.0, 'R']

# NuSVC
PARAM_GRID['nusvc__nu'] = [0.1, 1.0, 'R']
# PARAM_GRID['nusvc__kernel'] = ['linear', 'poly', 'rbf', 'sigmoid']
# PARAM_GRID['nusvc__shrinking'] = [True, False]

# feature processing
PARAM_GRID['nmf__l1_ratio'] = [0, 1, 'R']
PARAM_GRID['nmf__tol'] = [1e-5, 1e-1, 'R']
PARAM_GRID['nmf__n_components'] = [3, 10, 'I']

# pca
#PARAM_GRID['pca__svd_solver'] = ['auto', 'full', 'randomized']
PARAM_GRID['pca__n_components'] = [3, 5, 'I']

# fastica
PARAM_GRID['fastica__n_components'] = [3, 10, 'I']
#PARAM_GRID['fastica__algorithm'] = ['parallel', 'deflation']
#PARAM_GRID['fastica__whiten'] = ['False', 'True']
#PARAM_GRID['fastica__fun'] = ['logcosh', 'exp', 'cube']

# kernelpca
#PARAM_GRID['kernelpca__kernel'] = ['linear', 'poly', 'rbf', 'sigmoid', 'cosine']
PARAM_GRID['kernelpca__n_components'] = [3, 10, 'I']
PARAM_GRID['kernelpca__coef0'] = [-1.0, 1.0, 'R']
PARAM_GRID['kernelpca__gamma'] = [0.0001, 2.0, 'R']
PARAM_GRID['kernelpca__degree'] = [2, 5, 'I']

# Nystroem
#PARAM_GRID['nystroem__kernel'] = ['poly', 'rbf', 'sigmoid', 'cosine']
PARAM_GRID['nystroem__n_components'] = [5, 20, 'I']
PARAM_GRID['nystroem__gamma'] = [0.0001, 1.0, 'R']
PARAM_GRID['nystroem__degree'] = [2, 5, 'I']

# selectkbest
PARAM_GRID['selectkbest__k'] = [3, 20, 'I']

# variancethreshold
PARAM_GRID['variancethreshold__threshold'] = [0.0, 0.1, 'R']

# lowvariancefeatureelimination
PARAM_GRID['lowvariancefeatureelimination__var_threshold_value'] = \
    [0.0, 0.1, 'R']

# feature post processing
PARAM_GRID['kbinsdiscretizer__n_bins'] = [3, 9, 'I']
#PARAM_GRID['kbinsdiscretizer__encode'] = ['onehot-dense','ordinal']
#PARAM_GRID['kbinsdiscretizer__strategy'] = ['uniform','quantile','kmeans']

# polynomial features
PARAM_GRID['polynomialfeatures__degree'] = [2, 3, 'I']
#PARAM_GRID['polynomialfeatures__interaction_only'] = [True, False]

# onehot
#PARAM_GRID['onehotencoder__categories'] = ['auto']
#PARAM_GRID['onehotencoder__sparse'] = ['False']

# powertransformer
#PARAM_GRID['powertransformer__method'] = ['yeo-johnson', 'box-cox']
#PARAM_GRID['powertransformer__standardize'] = ['True', 'False']

# normalizer
#PARAM_GRID['normalizer__norm'] = ['l1', 'l2', 'max']

# RandomTreesEmbedding
PARAM_GRID['randomtreesembedding__n_estimators'] = [10, 100, 'I']
PARAM_GRID['randomtreesembedding__max_depth'] = [2, 10, 'I']
PARAM_GRID['randomtreesembedding__min_samples_split'] = [2, 20, 'I'] 
PARAM_GRID['randomtreesembedding__min_samples_leaf'] = [2, 20, 'I']

# selectpercentile
from sklearn.feature_selection import f_regression, mutual_info_regression
PARAM_GRID['selectpercentile__percentile'] = [1, 90, 'I']
PARAM_GRID['selectpercentile__score_func'] = [f_regression, mutual_info_regression]

# truncated SVD
PARAM_GRID['truncatedsvd__n_components'] = [2, 10, 'I']

# feature agglomeration
PARAM_GRID['featureagglomeration__n_clusters'] = [2, 50, 'I']
#PARAM_GRID['featureagglomeration__affinity'] = ["euclidean", "manhattan", "cosine"]
#PARAM_GRID['featureagglomeration__linkage'] = ["ward", "complete", "average"]
#PARAM_GRID['featureagglomeration__pooling_func'] = ["mean", "median", "max"]

# standardscaler
#PARAM_GRID['standardscaler__with_mean'] = ['True', 'False']
#PARAM_GRID['standardscaler__with_std'] = ['True', 'False']

PARAM_GRID['rbfsampler__gamma'] = [0.00001, 1.0, 'R']
PARAM_GRID['rbfsampler__n_components'] = [50, 200, 'R']

PARAM_GRID['skewedchi2sampler__n_components'] = [50, 200, 'I']

PARAM_GRID['sparsepca__n_components'] = [5, 10, 'I']
PARAM_GRID['sparsepca__alpha'] = [0.5, 2.0, 'R']
PARAM_GRID['sparsepca__ridge_alpha'] = [0.01, 1.0, 'R']
#PARAM_GRID['sparsepca__method'] = ['lars', 'cd'] 

PARAM_GRID['isomap__n_neighbors'] = [2, 10, 'I']
PARAM_GRID['isomap__n_components'] = [2, 10, 'I']
#PARAM_GRID['isomap__eigen_solver'] = ['auto', 'arpack', 'dense']
#PARAM_GRID['isomap__path_method'] = ['auto', 'FW', 'D']

PARAM_GRID['locallylinearembedding__n_neighbors'] = [2, 10, 'I']
PARAM_GRID['locallylinearembedding__n_components'] = [2, 10, 'I']
PARAM_GRID['locallylinearembedding__reg'] = [0.001, 0.1, 'R']
#PARAM_GRID['locallylinearembedding__eigen_solver'] = ['auto', 'arpack', 'dense']

PARAM_GRID['mds__n_components'] = [2, 10, 'I']
#PARAM_GRID['mds__metric'] = [True, False]

PARAM_GRID['spectralembedding__n_components'] = [2, 10, 'I']
#PARAM_GRID['spectralembedding__affinity'] = ['nearest_neighbors', 'rbf']
#PARAM_GRID['spectralembedding__eigen_solver'] = [None, 'arpack', 'lobpcg', 'amg']

PARAM_GRID['tsne__n_components'] = [2, 10, 'I']
PARAM_GRID['tsne__learning_rate'] = [10.0, 1000.0, 'R']

PARAM_GRID['selectfrommodel__extratreesregressor__n_estimators'] = [10, 100, 'I']
#PARAM_GRID['selectfrommodel__extratreesregressor__criterion'] = ['mse', 'friedman_mse', 'mae']
PARAM_GRID['selectfrommodel__extratreesregressor__max_features'] = [0.1, 1.0, 'R']
PARAM_GRID['selectfrommodel__extratreesregressor__min_samples_split'] = [2, 20, 'I']
PARAM_GRID['selectfrommodel__extratreesregressor__min_samples_leaf'] = [1, 20, 'I']
#PARAM_GRID['selectfrommodel__extratreesregressor__bootstrap'] = ['True', 'False']
