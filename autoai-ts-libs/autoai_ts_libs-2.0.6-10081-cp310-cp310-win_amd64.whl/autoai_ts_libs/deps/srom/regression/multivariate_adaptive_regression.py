# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: multivariate_adaptive_regression
   :synopsis: Contains MultiVariateAdaptiveRegression class.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, RegressorMixin
from pyearth import Earth
import pandas as pd
import numpy as np
from sklearn.utils.validation import check_is_fitted


class MultiVariateAdaptiveRegression(BaseEstimator, RegressorMixin):
    """
    A multivariate adaptive regression splines(MARS) regressor.
    
    Parameters:
        base_model: A model based MARS.
        scaling: Used for scaling.
    
    Notes:
        If base_model = None, then automatically using py-earth model.
        If we want to use for optimization then we need to set ``Scaling = True`` \
            for internally scaling.
    
    References:  
        1. Friedman, Jerome. Multivariate Adaptive Regression Splines.
           Annals of Statistics. Volume 19, Number 1 (1991), 1-67.
        2. https://contrib.scikit-learn.org/py-earth/
        3. https://github.com/scikit-learn-contrib/py-earth/blob/master/pyearth/earth.py
    
    """

    def __init__(self, base_model=None, scaling=False):

        self.model = base_model
        self.scaling = scaling

        if base_model is None:
            self.model = Earth()

    def set_params(self, **kwarg):
        model_param = {}
        for d_item in kwarg:
            if "base_model__" in d_item:
                model_param[d_item.split("base_model__")[1]] = kwarg[d_item]
        self.model.set_params(**model_param)
        return self

    def get_params(self, deep=False):
        model_param = {}
        model_param["base_model"] = self.model
        if deep:
            for item in self.model.get_params().keys():
                model_param["base_model__" + item] = self.model.get_params()[item]
        return model_param

    def fit(self, X, y):

        """
        Build a MARS from the training set (X, y).
        
        Parameters:
            X: Array-like, shape = [m, n] where m is the number of samples \
                and n is the number of features, the training predictors. \
                The X parameter can be a numpy array, a pandas DataFrame, a patsy
                DesignMatrix, or a tuple of patsy DesignMatrix objects as
                output by patsy.dmatrices.
            y: Array-like, shape = [m, p] where m is the number of samples \
                the training responds, p the number of outputs. \
                The y parameter can be a numpy array, a pandas DataFrame, \
                a Patsy DesignMatrix, or can be left as None(default) if X was \
                the output of a call to patsy.dmatrices (in which case, X contains \
                the response).
            
        Returns:
            self : object.
        """

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

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
            X: Array-like, shape = [m, n] where m is the number of samples and n \
                is the number of features, the training predictors. The X parameter \
                can be a numpy array, a pandas DataFrame, or a patsy DesignMatrix.
            
        Returns:
            y: Array of shape = [m] or [m, p] where m is the number of samples \
                and p is the number of outputs.The predicted values.
        """
        check_is_fitted(self, "model")

        if self.scaling:
            X = self.scalerObj.transform(X)
            X = pd.DataFrame(X)
            X.columns = self.input_features

        return self.model.predict(X)

    # scaler_params has tuples of (mean, var)
    def _get_hinge(self, hinge, scaler_params, min_value, max_value):

        scaled_coef = hinge[1]
        hinge = str(hinge[0])
        limits = [min_value, max_value]
        if "*" not in hinge:
            return ["intercept", None, None, scaled_coef, None]
        else:
            if "Max" not in hinge:
                var = hinge.split("*")[1]
                coef, offset = self._orig_scale(scaled_coef, scaler_params[var], 0)
                return [var, *limits, coef, offset]
            else:
                hinge = hinge.split(",")[1].lstrip().rstrip(")")
                hinge = hinge.split(" ")

                if str(hinge[1]) == "-" and str(hinge[2]) in self.input_features:

                    hinge = ["-", hinge[2], "+", hinge[0]]

                if len(hinge) == 4:
                    var = hinge[1]
                elif len(hinge) == 3:
                    var = hinge[0]

                if "-" in var:
                    tmp_var = var.split("-")[1]
                    scaler = scaler_params[tmp_var]
                else:
                    scaler = scaler_params[var]

                num = 0
                if len(hinge) == 4:
                    num = float(hinge[2] + hinge[3])
                elif len(hinge) == 3:
                    num = float(hinge[1] + hinge[2])

                if hinge[0][0] == "-":
                    scaled_coef *= -1
                    limits[1] = num * np.sqrt(scaler[1]) + scaler[0]
                else:
                    num *= -1
                    limits[0] = num * np.sqrt(scaler[1]) + scaler[0]
                coef, offset = self._orig_scale(scaled_coef, scaler, num)
                hinge = [var, *limits, coef, offset]

                return hinge

    def _orig_scale(self, scaled_coef, scaler, num):
        s_mean = scaler[0]
        s_std = np.sqrt(scaler[1])
        offset = -scaled_coef * (num + s_mean / s_std)
        coef = scaled_coef / s_std
        return coef, offset

    def _get_interval_data(self, df):
        grouped = df.groupby(["y_var", "x_var"])
        interval_data = []
        for name, group in grouped:
            intervals = group.loc[:, ["x_min", "x_max"]].values
            limits = sorted(set(np.ravel(intervals)))
            new_intervals = np.reshape(
                sorted(limits + limits[1:-1]), (len(limits) - 1, 2)
            )
            for lim in new_intervals:
                rows = group.loc[
                    (group["x_min"] <= lim[0]) & (group["x_max"] >= lim[1]),
                    ["coefficient", "offset"],
                ].sum(axis=0)
                interval_data.append(
                    [*name, *lim, *rows, *group[df.columns[6:]].iloc[0].values]
                )

        return pd.DataFrame(interval_data, columns=df.columns)

    def get_coefficient_table(self, min_value=np.NINF, max_value=np.inf):
        """
        Get a coefficient table.

        Parameters:
            min_value (optional): The minimum value of the variables.
            max_value (optional): The maximum value of the variables.

        Returns:
            Table : DataFrame.\
                Achieve a table with information of coefficients and \
                intercept corresponding to each feature variables. We could \
                also obtain the min and max values of each feature variables.
        """
        check_is_fitted(self, "model")
        from pyearth.export import export_sympy_term_expressions

        if self.scaling:
            scaler_params = dict(
                zip(
                    self.input_features,
                    list(zip(self.scalerObj.mean_, self.scalerObj.var_)),
                )
            )
        else:
            scaler_params = dict(
                zip(
                    self.input_features,
                    list(
                        zip(
                            np.zeros(len(self.input_features)),
                            np.ones(len(self.input_features)),
                        )
                    ),
                )
            )
        hinges = export_sympy_term_expressions(self.model)
        coefs = self.model.coef_[0]
        hinges = list(zip(hinges, coefs))
        y_var = "y"
        hinges = [
            [y_var] + self._get_hinge(h, scaler_params, min_value, max_value) + [None]
            for h in hinges
        ]
        hinge_coef = pd.DataFrame(
            hinges,
            columns=[
                "y_var",
                "x_var",
                "x_min",
                "x_max",
                "coefficient",
                "offset",
                "intercept",
            ],
        )
        hinge_coef["intercept"] = hinge_coef.loc[
            hinge_coef["x_var"] == "intercept", "coefficient"
        ].item()
        hinge_coef.drop(
            hinge_coef.loc[hinge_coef["x_var"] == "intercept"].index, inplace=True
        )
        res_tbl = self._get_interval_data(hinge_coef)
        res_tbl["reg_num"] = 1
        return res_tbl

    def get_optimization_table(self, param_data, min_value=np.NINF, max_value=np.inf):
        """
        Get an optimization table.
        
        Parameters:
            param_data (dict): The observed variable and its value. \
                Example: {feature_01: value_01} \
                where ``feature_01 = 'F1'`` and ``value_01 = 10``.
            min_value (optional): the minimum value of the variables.
            max_value (optional): the maximum value of the variables.

        Returns:
            Table : DataFrame. 
                Achieve a table with information of coefficients and intercept \
                corresponding to each feature variables after MERGING with an \
                observed variable. We could also obtain the min and max values \
                of each feature variables.
        """
        check_is_fitted(self, "model")
        df_raw = pd.DataFrame.from_dict(param_data, orient="index")
        param_data = df_raw.copy()
        param_data.columns = ["x_val"]

        mars_to_opt = pd.DataFrame()
        df_model = self.get_coefficient_table(min_value, max_value)
        df_model = (
            df_model.merge(param_data, how="left", left_on="x_var", right_index=True)
            .sort_values(by="reg_num")
            .reset_index(drop=True)
        )
        bad_rows = df_model.loc[
            (df_model["x_val"].notna())
            & (
                (df_model["x_val"] < df_model["x_min"])
                | ((df_model["x_val"] >= df_model["x_max"]))
            )
        ]
        df_model.drop(bad_rows.index, inplace=True)
        df_model.loc[df_model["x_val"].notna(), "offset"] += (
            df_model["coefficient"] * df_model["x_val"]
        )
        df_model["offset_r"] = df_model.loc[df_model["x_val"].notna(), "offset"].sum()
        df_model["intercept"] = df_model["intercept"] + df_model["offset_r"]
        df_model.drop("offset_r", inplace=True, axis=1)
        df_model = df_model.loc[(df_model["x_val"]).isna()]
        df_model = df_model.sort_values(by=["reg_num", "x_var"])
        df_model.drop("reg_num", axis=1, inplace=True)
        df_model.drop("x_val", axis=1, inplace=True)
        df_model["running_intercept"] = 0
        mars_to_opt = pd.concat([mars_to_opt, df_model], axis=0)
        return mars_to_opt

    def get_optimization_json(self, param_data, min_value=np.NINF, max_value=np.inf):
        """
        Get an optimization table in json format. 
        
        Parameters:
            param_data: The observed variable and its value. Dictionary type. \
                Example: {feature_01: value_01} \
                where ``feature_01 = 'F1'`` and ``value_01 = 10``. 
            min_value (optional): the minimum value of the variables.
            max_value (optional): the maximum value of the variables.

        Returns:
            json form.
            Achieve a table with information of coefficients and intercept corresponding \
            to each feature variables after MERGING with an observed variable. We could \
            also obtain the min and max values of each feature variables.
        """
        check_is_fitted(self, "model")

        mars_to_opt = self.get_optimization_table(param_data, min_value, max_value)
        import json

        mars_to_opt_df = json.loads(mars_to_opt.reset_index().to_json())
        dicts = []
        for index in list(mars_to_opt_df["index"].keys()):
            dicts.append(
                {
                    "y_var": mars_to_opt_df["y_var"][index],
                    "x_var": mars_to_opt_df["x_var"][index],
                    "x_min": mars_to_opt_df["x_min"][index],
                    "x_max": mars_to_opt_df["x_max"][index],
                    "coefficient": mars_to_opt_df["coefficient"][index],
                    "offset": mars_to_opt_df["offset"][index],
                    "intercept": mars_to_opt_df["intercept"][index],
                    "running_intercept": mars_to_opt_df["running_intercept"][index],
                }
            )
        mars_to_opt_dicts = {"ModelToOptimization": dicts}
        return mars_to_opt_dicts
