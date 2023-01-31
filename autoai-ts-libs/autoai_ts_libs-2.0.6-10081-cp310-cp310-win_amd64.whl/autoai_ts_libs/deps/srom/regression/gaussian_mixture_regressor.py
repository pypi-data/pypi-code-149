# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: gaussian_mixture_regressor
   :synopsis: Contains GaussianMixtureRegressor class.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.utils import check_X_y
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.mixture import GaussianMixture

class GaussianMixtureRegressor(BaseEstimator, RegressorMixin):

    def __init__(self, base_model=GaussianMixture(), loss_steps=100):
        self.base_model = base_model
        self.min_target_value = 0
        self.max_target_value = 1
        self.loss_steps = loss_steps

    def set_params(self, **kwarg):
        model_param = {}
        for d_item in kwarg:
            if 'base_model__' in d_item:
                model_param[d_item.split('base_model__')[1]] = kwarg[d_item]
        self.base_model.set_params(**model_param)
        return self

    def get_params(self, deep=False):
        model_param = {}
        model_param['base_model'] = self.base_model
        if deep:
            for item in self.base_model.get_params().keys():
                model_param['base_model__'+item] = self.base_model.get_params()[item]
        return model_param

    def fit(self,X,y):

        X, y = check_X_y(X, y, accept_sparse=False)  
                     
        if isinstance(y, pd.DataFrame):
            y = y.values
        if isinstance(X, pd.DataFrame):
            newX = np.c_[X.values,y]
        else:
            newX = np.c_[X,y]

        self.min_target_value = np.min(y)
        self.max_target_value = np.max(y)
        self.base_model.fit(newX)
        return self

    def _generate_loss_curve(self, sample_record):
        Q = sample_record
        ans = []
        grt = []

        if len(pd.DataFrame(Q).dropna()) < 1:
            return [ans,grt]

        inter_values = np.linspace(self.min_target_value, self.max_target_value, 
                                   num=self.loss_steps)

        for i in inter_values:
            Q1 = list(Q.copy()[0])
            Q1.append(i)
            Q1 = np.array(Q1).reshape(1,-1)
            grt.append(i)
            ans.append(self.base_model.score_samples(Q1)[0])
        
        return [ans,grt]

    def _generate_prediction(self,sample_record):
        loss, pred_target = self._generate_loss_curve(sample_record)
        index_v = (np.where(np.array(loss)==np.max(loss))[0][0])
        max_pred = pred_target[index_v]
        return max_pred

    def _generate_threshold(self,sample_record,loss_threshold=1.0):
        loss, pred_target = self._generate_loss_curve(sample_record)
        index_v = (np.where(np.array(loss)==np.max(loss))[0][0])

        lower_b = loss[0:index_v-1]
        valSet = []
        for item in lower_b:
            if item >= (loss[index_v]-loss_threshold):
                valSet.append(item)    
        index_v1 = index_v
        if len(valSet) > 0:
            index_v1 = (np.where(np.array(loss)==np.min(valSet))[0][0])
        left_side_pred = pred_target[index_v1]

        upper_b = loss[index_v:]
        valSet = []
        for item in upper_b:
            if item >= (loss[index_v]-loss_threshold):
                valSet.append(item)
        index_v1 = index_v
        if len(valSet) > 0:
            index_v1 = (np.where(np.array(loss)==np.min(valSet))[0][0])
        right_side_pred = pred_target[index_v1]
        return [left_side_pred,right_side_pred]

    def predict(self,X):
        final_out = []
        if isinstance(X, pd.DataFrame):
            X = X.values
        for i in range(X.shape[0]):
            Q = X[i,:].reshape(1,-1)
            final_out.append(self._generate_prediction(Q))
        return np.array(final_out)

    def predict_interval(self,X):
        final_out = []
        if isinstance(X, pd.DataFrame):
            X = X.values
        for i in range(X.shape[0]):
            Q = X[i,:].reshape(1,-1)
            final_out.append(self._generate_threshold(Q))
        return np.array(final_out)
