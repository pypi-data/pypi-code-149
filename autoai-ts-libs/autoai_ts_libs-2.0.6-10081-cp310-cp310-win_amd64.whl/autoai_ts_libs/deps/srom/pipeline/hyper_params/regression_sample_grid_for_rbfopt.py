# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Regression Fine Grid: for RBOpt.
"""
# important links
# TPOT - https://github.com/rhiever/tpot/blob/master/tpot/config/regressor.py
# HyperOpt https://github.com/hyperopt/hyperopt-sklearn/blob/master/hpsklearn/components.py
# AutoML - https://github.com/automl/auto-sklearn/tree/master/autosklearn/pipeline/components/regression

PARAM_GRID = {}

# 0 ADRRegression
PARAM_GRID['adrregression__tol'] = [1e-5, 1e-1, 'R']
PARAM_GRID['adrregression__alpha_1'] = [0.000001, 0.01, 'R']
PARAM_GRID['adrregression__alpha_2'] = [0.000001, 0.01, 'R']
PARAM_GRID['adrregression__lambda_1'] = [0.000001, 0.01, 'R']
PARAM_GRID['adrregression__lambda_2'] = [0.000001, 0.01, 'R']
PARAM_GRID['adrregression__threshold_lambda'] = [1000, 100000, 'I']

# 1 ElasticNetCV
PARAM_GRID['elasticnetcv__l1_ratio'] = [0.01, 1.01, 'R']
PARAM_GRID['elasticnetcv__tol'] = [1e-5, 1e-1, 'R']

# 2 DecisionTreeRegression
PARAM_GRID['decisiontreeregressor__max_depth'] = [1,11,'I']
PARAM_GRID['decisiontreeregressor__min_samples_split'] = [2, 21,'I']
PARAM_GRID['decisiontreeregressor__min_samples_leaf'] = [1,21,'I']
#PARAM_GRID['decisiontreeregressor__criterion'] = ['mse', 'friedman_mse', 'mae']

# 4 ExtraTreesRegression
PARAM_GRID['extratreesregressor__n_estimators'] = [10, 500, 'I']
PARAM_GRID['extratreesregressor__max_features'] = [0.05, 1.01, 'I']
PARAM_GRID['extratreesregressor__min_samples_split'] = [2, 21, 'I']
PARAM_GRID['extratreesregressor__min_samples_leaf'] = [1,21,'I']
#PARAM_GRID['extratreesregressor__bootstrap'] = [True, False]
#PARAM_GRID['extratreesregressor__criterion'] = ['mse', 'mae']
PARAM_GRID['extratreesregressor__max_depth'] = [1, 10, 'I']

# 5 RandomForestRegression
PARAM_GRID['randomforestregressor__n_estimators'] = [10, 500, 'I']
#PARAM_GRID['randomforestregressor__criterion'] = ['mse', 'mae']
PARAM_GRID['randomforestregressor__min_samples_split'] = [2, 20, 'I']
PARAM_GRID['randomforestregressor__min_samples_leaf'] = [1, 20, 'I']
#PARAM_GRID['randomforestregressor__bootstrap'] = [True, False]
PARAM_GRID['randomforestregressor__max_features'] = [0.1, 1.0, 'R']
PARAM_GRID['randomforestregressor__min_impurity_decrease'] =  [0.001, 0.005, 'R']

# 6 GradientBoostingClassifier
PARAM_GRID['gradientboostingregressor__n_estimators'] = [10, 500, 'I']
#PARAM_GRID['gradientboostingregressor__loss'] = ["ls", "lad", "huber", "quantile"]
PARAM_GRID['gradientboostingregressor__learning_rate'] = [1e-3, 1., 'R']
PARAM_GRID['gradientboostingregressor__max_depth'] = [1, 11, 'I']
PARAM_GRID['gradientboostingregressor__min_samples_split'] = [2, 21, 'I']
PARAM_GRID['gradientboostingregressor__min_samples_leaf'] = [1, 21, 'I']
PARAM_GRID['gradientboostingregressor__subsample'] = [0.05, 1.0, 'R']
PARAM_GRID['gradientboostingregressor__max_features'] = [0.05, 1.0, 'R']
PARAM_GRID['gradientboostingregressor__alpha'] = [0.75, 0.99, 'R']


# 7 KNeighborsRegression
PARAM_GRID['kneighborsregressor__n_neighbors'] = [1, 100, 'I']
#PARAM_GRID['kneighborsregressor__weights'] = ["uniform", "distance"]
PARAM_GRID['kneighborsregressor__p'] = [1, 2, 'I']

# 8 LassoLarsCV
#PARAM_GRID['lassolarscv__normalize'] = [True, False]
PARAM_GRID['lassolars__alpha'] = [0.001, 1, 'R']

# 9 Linear SVR
PARAM_GRID['linearsvr__epsilon'] = [1e-4, 1, 'R']
#PARAM_GRID['linearsvr__loss'] = ["epsilon_insensitive", "squared_epsilon_insensitive"]
#PARAM_GRID['linearsvr__dual'] = [True, False]
PARAM_GRID['linearsvr__tol'] = [1e-5, 1e-1, 'R']
PARAM_GRID['linearsvr__C'] = [1e-4, 25, 'R']

# 10 XGBRegression
PARAM_GRID['xgbregressor__n_estimators'] = [10, 500, 'I']
PARAM_GRID['xgbregressor__max_depth'] = [1, 50, 'I']
PARAM_GRID['xgbregressor__learning_rate'] = [0.001, 1, 'R']
PARAM_GRID['xgbregressor__subsample'] = [0.05, 1, 'R']
PARAM_GRID['xgbregressor__min_child_weight'] = [1, 20, 'I']
PARAM_GRID['xgbregressor__nthread'] = [1, 3,'I']
PARAM_GRID['xgbregressor__gamma'] = [0.01, 0.51,'R']

# 11 SGDRegression
#PARAM_GRID['sgdregressor__loss'] = ['squared_loss', 'huber', 'epsilon_insensitive', 'squared_epsilon_insensitive']
#PARAM_GRID['sgdregressor__penalty'] = ['none', 'l2', 'l1', 'elasticnet']
PARAM_GRID['sgdregressor__alpha'] = [0.001, 1, 'R']
PARAM_GRID['sgdregressor__l1_ratio'] = [0.01, 0.5, 'R']
#PARAM_GRID['sgdregressor__learning_rate'] = ['constant', 'optimal', 'invscaling']
PARAM_GRID['sgdregressor__eta0'] = [0.0001, 0.01, 'R']


# 11 SVR - https://github.com/rhiever/sklearn-benchmarks/blob/master/model_code/grid_search/SVC.py
PARAM_GRID['svr__C'] = [0.01, 100, 'R']
PARAM_GRID['svr__gamma'] = [0.01, 100, 'R']
#PARAM_GRID['svr__kernel'] = ['poly', 'rbf', 'sigmoid']
PARAM_GRID['svr__degree'] = [2, 3, 'I']
PARAM_GRID['svr__coef0'] = [0.1, 100, 'R']

#12 MLP skipped for now
PARAM_GRID['mlpregressor__number_of_hidden_layers'] = [1,10,'I']
PARAM_GRID['mlpregressor__number_of_neurons_in_hidden_layers'] = [0,200,'I']
#PARAM_GRID['mlpregressor__hidden_layer_sizes'] = [(50, 50, 50), (100, 100, 100)]
#PARAM_GRID['mlpregressor__activation'] = ['identity', 'logistic', 'tanh', 'relu']
#PARAM_GRID['mlpregressor__solver'] = ['lbfgs', 'sgd', 'adam']
#PARAM_GRID['mlpregressor__alpha'] = 10.0 ** (-np.arange(1, 4))

# 13 PassiveAggressiveRegression
#PARAM_GRID['passiveaggressiveregressor__fit_intercept'] = [True, False]
PARAM_GRID['passiveaggressiveregressor__C'] = [0.000001, 100, 'R']
#PARAM_GRID['passiveaggressiveregressor__loss'] = ['epsilon_insensitive', 'squared_epsilon_insensitive']

# 14 AdaBoostRegression
# https://github.com/automl/auto-sklearn/blob/master/autosklearn/pipeline/components/classification/adaboost.py
PARAM_GRID['adaboostregression__n_estimators'] = [10, 500, 'I']
PARAM_GRID['adaboostregression__learning_rate'] = [1e-3, 1, 'R']
#PARAM_GRID['adaboostregression__loss'] = ["linear", "square", "exponential"]
PARAM_GRID['adaboostregression__max_depth'] = [1, 11,'I']

# 15 KernelRedge
PARAM_GRID['kernelridge__alpha'] = [0.0001, 0.001, 'R']
#PARAM_GRID['kernelridge__kernel'] = ['linear', 'rbf', 'laplacian', 'polynomial', 'chi2', 'sigmoid']

# 16 Lasso
PARAM_GRID['lasso__alpha'] = [0.001, 1, 'R']

# 17 Ridge
PARAM_GRID['ridge__alpha'] = [0.001, 1, 'R']

# 18
PARAM_GRID['baggingregressor__n_estimators'] = [50, 100, 'I']
#PARAM_GRID['baggingregressor__bootstrap'] = ['True', 'False']
#PARAM_GRID['baggingregressor__bootstrap_features'] = ['True', 'False']

#19 PLS
PARAM_GRID['plsregression__n_components']=[2, 5, 'I']
#PARAM_GRID['plsregression__scale']=[]
PARAM_GRID['plsregression__max_iter']=[500, 750, 'I']
PARAM_GRID['plsregression__tol']=[1e-06, 0.01, 'R']
#PARAM_GRID['plsregression__copy']=[]

#20 OMP
#PARAM_GRID['orthogonalmatchingpursuit__n_nonzero_coefs']=[]
PARAM_GRID['orthogonalmatchingpursuit__tol']=[1e-06, 1e-03, 'R']
#PARAM_GRID['orthogonalmatchingpursuit__normalize']=[]
#PARAM_GRID['orthogonalmatchingpursuit__precompute']=[]

#xgboost
PARAM_GRID['xgboostregressor__min_child_weight'] = [1, 9, 'I']
PARAM_GRID['xgboostregressor__gamma'] = [0.0, 5.0, 'R']
PARAM_GRID['xgboostregressor__subsample'] = [0.6, 1.0, 'R']
PARAM_GRID['xgboostregressor__colsample_bytree'] = [0.3, 1.0, 'R']
PARAM_GRID['xgboostregressor__max_depth'] = [3, 15, 'I']
PARAM_GRID['xgboostregressor__n_estimators'] = [10, 500, 'I']
PARAM_GRID['xgboostregressor__learning_rate'] = [0.03, 0.3, 'R']

# partitionregressor
PARAM_GRID['partitionregressor__partition_model__max_depth'] = [1, 11, 'I']
PARAM_GRID['partitionregressor__partition_model__min_samples_split'] = [1, 21, 'I']
PARAM_GRID['partitionregressor__partition_model__min_samples_leaf'] = [1, 12, 'I']
#PARAM_GRID['partitionregressor__partition_model__criterion'] = ['mse', 'friedman_mse', 'mae']
#PARAM_GRID['partitionregressor__regression_model__fit_intercept'] = [True, False]
