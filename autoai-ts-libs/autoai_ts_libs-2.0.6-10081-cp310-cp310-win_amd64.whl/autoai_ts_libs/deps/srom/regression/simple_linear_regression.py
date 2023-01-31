# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: simple_linear_regression
   :synopsis: Contains SimpleLinearRegression class.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.utils.validation import check_is_fitted

class SimpleLinearRegression(BaseEstimator, RegressorMixin):
    """
    A linear regression regressor.

    Parameters:
        base_model: A linear model.
        scaling: Used for scaling.

    Notes:
        If base_model = None, then automatically using LinearRegression model.
        If we want to use for optimization then we need to set ``Scaling = True`` \
        for internally scaling.

    References:
        1. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
        2. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor
        3. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor
        4. https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor
    """

    def __init__(self, base_model=None, scaling=False):

        self.model = base_model
        self.scaling = scaling
        
        if base_model is None:
            self.model = LinearRegression()

    def set_params(self, **kwarg):
        model_param = {}
        for d_item in kwarg:
            if 'base_model__' in d_item:
                model_param[d_item.split('base_model__')[1]] = kwarg[d_item]
        self.model.set_params(**model_param)
        return self

    def get_params(self, deep=False):
        model_param = {}
        model_param['base_model'] = self.model
        if deep:
            for item in self.model.get_params().keys():
                model_param['base_model__'+item] = self.model.get_params()[item]
        return model_param

    def fit(self, X, y):
        """
        Build a Linear Regression from the training set(X, y).
        
        Parameters
        ----------
            X: Array-like, shape = [m, n] where m is the number of samples \
               and n is the number of features the training predictors. \
               The X parameter can be a numpy array, a pandas DataFrame, a patsy \
               DesignMatrix, or a tuple of patsy DesignMatrix objects as \
               output by patsy.dmatrices.
            y: Array-like, shape = [m, p] where m is the number of samples \
               the training responds, p the number of outputs. The y parameter \
               can be a numpy array, a pandas DataFrame, a Patsy DesignMatrix, \
               or can be left as None (default) if X was the output of a call to \
               patsy.dmatrices (in which case, X contains the response).
            
        Returns:
            self : object
        """        
        
        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X,columns=['tmpclm_' + str(i) for i in range(X.shape[1])])

        self.input_features = list(X.columns)

        if not isinstance(y, pd.Series):
            if y.ndim == 2:
                y = y.ravel()
            y = pd.Series(y)

        if self.scaling:
            from sklearn.preprocessing import StandardScaler
            self.scalerObj = StandardScaler()
            X = self.scalerObj.fit_transform(X)
            X = pd.DataFrame(X)
            X.columns = self.input_features

        self.model.fit(X, y)
        return self

    def predict(self, X):
        """
        Predict the response based on the input data X.

        Parameters:
            X: Aarray-like, shape = [m, n] where m is the number of samples and \
               n is the number of features, the training predictors. The X parameter \
               can be a numpy array, a pandas DataFrame, or a patsy DesignMatrix.
            
        Returns:
            y: Array of shape = [m] or [m, p] where m is the number of samples
               and p is the number of outputs, the predicted values.
        """
        check_is_fitted(self, 'model')    

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X,columns=['tmpclm_' + str(i) for i in range(X.shape[1])])

        if self.scaling:
            X = self.scalerObj.transform(X)
            X = pd.DataFrame(X)
            X.columns = self.input_features

        return self.model.predict(X)

    def _get_regression_model_coefficient(self, reg_model):
        if reg_model.__class__.__name__ == 'RANSACRegressor':
            return reg_model.estimator_.coef_
        else:
            return reg_model.coef_
            
    def _get_regression_model_intercept(self, reg_model):
        if reg_model.__class__.__name__ == 'RANSACRegressor':
            return reg_model.estimator_.intercept_
        else:
            return reg_model.intercept_

    def _get_terms(self, reg_model):
        if self.scaling:
            coefficients = self._get_regression_model_coefficient(reg_model) / np.sqrt(self.scalerObj.var_)
            var_intercepts = (- self._get_regression_model_coefficient(reg_model) / np.sqrt(self.scalerObj.var_) \
                * self.scalerObj.mean_)
            intercept = self._get_regression_model_intercept(reg_model) + np.sum(var_intercepts)
            return intercept, coefficients
        else:
            return self._get_regression_model_intercept(reg_model), self._get_regression_model_coefficient(reg_model)

    def _make_regression_rows(self, reg_model, x_var, y_var, \
        min_value, max_value):
        intercept, coefficients = self._get_terms(reg_model)
        df = pd.DataFrame(columns=['y_var','reg_num'])
        df['x_var'] = x_var
        df['x_min'] = min_value
        df['x_max'] = max_value
        df['coefficient'] = coefficients
        df['intercept'] = intercept
        df['y_var'] = y_var
        return df

    def get_coefficient_table(self, min_value = np.NINF, max_value = np.inf):
        """
        Get a coefficient table.

        Parameters:
            min_value (optional): the minimum value of the variables.
            max_value (optional): the maximum value of the variables.

        Returns:
            Table : DataFrame.
            Achieve a table with information of coefficients and intercept \
            corresponding to each feature variables. We could also obtain \
            the min and max values of each feature variables.
        """ 
        check_is_fitted(self, 'model')    

        df_model = pd.DataFrame()
        df_part = self._make_regression_rows(self.model, self.input_features, 'target',\
            min_value, max_value)
        df_part['reg_num'] = 1
        df_model = pd.concat([df_model, df_part])
        slr_spec_tbl = df_model.copy()
        return slr_spec_tbl

    def get_optimization_table(self, param_data, min_value = np.NINF, max_value = np.inf):
        """
        Get an optimization table.

        Parameters:
            param_data (Dictionary): The observed variable and its value. \
                Example: {feature_01: value_01} where \
                ``feature_01 = 'F1'`` and ``value_01 = 10``.
            min_value (optional): the minimum value of the variables.
            max_value (optional): the maximum value of the variables.

        Returns:
            Table : DataFrame. 
            Achieve a table with information of coefficients and intercept \
            corresponding to each feature variables after MERGING with an \
            observed variable. We could also obtain the min and max values \
            of each feature variables. 
        """ 

        check_is_fitted(self, 'model')    
        
        df_raw = pd.DataFrame.from_dict(param_data, orient='index')
        param_data = df_raw.copy()
        param_data.columns = ['x_val']

        slr_to_opt = pd.DataFrame()
        df_model = self.get_coefficient_table(min_value, max_value)
        df_model = df_model.merge(param_data, how='left', left_on='x_var', right_index=True).sort_values(
            by='reg_num').reset_index(drop=True)

        df_model.loc[df_model['x_val'].notna(), 'offset'] = df_model['coefficient'] * df_model['x_val']
        df_model = df_model.join(df_model.groupby('reg_num')['offset'].sum(), on='reg_num', rsuffix='_r')
        df_model.drop('offset', inplace=True, axis=1)
        df_model['intercept'] = df_model['intercept'] + df_model['offset_r']
        df_model.drop('offset_r', inplace=True, axis=1)
        df_model = df_model.loc[(df_model['x_val']).isna()]
        df_model = df_model.sort_values(by=['reg_num', 'x_var'])
        df_model['reg_num'] = df_model['reg_num'].astype(int)
        df_model.drop('x_val', axis=1, inplace=True)
        df_model['running_intercept'] = 0
        slr_to_opt = pd.concat([slr_to_opt, df_model], axis=0)
        return slr_to_opt

    def get_optimization_json(self, param_data, min_value = np.NINF, max_value = np.inf):
        """
        Get an optimization table.

        Parameters:
            param_data (Dictionary): The observed variable and its value. \
                Example: {feature_01: value_01} where \
                ``feature_01 = 'F1'  `` and ``value_01 = 10``.
            min_value (optional): the minimum value of the variables.
            max_value (optional): the maximum value of the variables.

        Returns:
            Optimization in JSON Files.
        """ 
        check_is_fitted(self, 'model')    

        slr_to_opt = self.get_optimization_table(param_data, min_value, max_value)
        import json
        slr_to_opt_df = json.loads(slr_to_opt.reset_index().to_json())
        dicts = []
        for index in list(slr_to_opt_df['index'].keys()):
            dicts.append(
                {
                    'y_var': slr_to_opt_df['y_var'][index],
                    'reg_num': slr_to_opt_df['reg_num'][index],
                    'x_var': slr_to_opt_df['x_var'][index],
                    'x_min': slr_to_opt_df['x_min'][index],
                    'x_max': slr_to_opt_df['x_max'][index],
                    'coefficient': slr_to_opt_df['coefficient'][index],
                    'intercept': slr_to_opt_df['intercept'][index],
                    'running_intercept': slr_to_opt_df['running_intercept'][index]
                }
            )
        slr_to_opt_dicts = {
            'ModelToOptimization': dicts
        }
        return slr_to_opt_dicts
