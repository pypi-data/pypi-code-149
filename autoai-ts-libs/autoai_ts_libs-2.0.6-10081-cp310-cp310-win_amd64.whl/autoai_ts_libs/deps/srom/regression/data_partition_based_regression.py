# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: data_partition_based_regression
   :synopsis: Contains PartitionRegressor class.

.. moduleauthor:: SROM Team
"""
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.base import clone
import pandas as pd
from sklearn.utils.validation import check_is_fitted


class PartitionRegressor(BaseEstimator, RegressorMixin):
    """
    A partition regressor uses a partition_model, such as a decision tree, \
    to partition the data, and then uses a regression_model, such as linear \
    regression, to regress the target variable against regression_feaures \
    in each of the previously determined partitioned spaces.

    Parameters:
        partition_model: Method to partition the feature space based on \
            DecisionTreeRegressor(). Alternatively, KMeans(), \
            GaussianMixture() may be used.
        regression_model: Fit a regression model to the data residing in each \
            partitioned space (or a leaf node, in the case of a decision tree). \
            Currently, linear models such as Linear regression, HuberRegressor(), \
            TheilSenRegressor, RANSACRegressor() may be used.
        partition_features: Features to be used in the partition model. These may \
            have a  partial, a complete or no overlap with regression_features.
        regression_features: Features to be used in the regression model. These may \
            have a partial, a complete or no overlap with partition_features.
        scaling: Used for scaling features prior to partitioning and regression modeling. \
            Default is True. If True, the intercept and coefficients are scaled back in the \
            final regression model.

    
    Attributes:
        input_features: List of features when "fit" is performed.
        scalerObj: Scaling object. Default is standard scaling.
    
    Notes:
        If partition_features = None, it will take in all the features by default.
        If regression_features = None, it will take in all the features by default.

    See also, DecisionTreeRegressor, GaussianMixture, KMeans.

    """

    def __init__(
        self,
        partition_model=DecisionTreeRegressor(),
        regression_model=LinearRegression(),
        partition_model_predict_function="apply",
        partition_features=None,
        regression_features=None,
        scaling=True,
    ):
        self.partition_model = partition_model
        self.regression_model = regression_model
        self.partition_features = partition_features
        self.regression_features = regression_features
        self.scaling = scaling
        self.partition_model_predict_function = partition_model_predict_function

    def set_params(self, **kwarg):
        if "partition_model_predict_function" in kwarg.keys():
            self.partition_model_predict_function = kwarg[
                "partition_model_predict_function"
            ]

        model_param = {}
        for d_item in kwarg:
            if "partition_model__" in d_item:
                model_param[d_item.split("partition_model__")[1]] = kwarg[d_item]
        self.partition_model.set_params(**model_param)

        model_param = {}
        for d_item in kwarg:
            if "regression_model__" in d_item:
                model_param[d_item.split("regression_model__")[1]] = kwarg[d_item]
        self.regression_model.set_params(**model_param)
        return self

    def get_params(self, deep=False):
        model_param = {}
        model_param[
            "partition_model_predict_function"
        ] = self.partition_model_predict_function
        model_param["partition_model"] = self.partition_model
        model_param["regression_model"] = self.regression_model
        if deep:
            for item in self.partition_model.get_params().keys():
                model_param[
                    "partition_model__" + item
                ] = self.partition_model.get_params()[item]
            for item in self.regression_model.get_params().keys():
                model_param[
                    "regression_model__" + item
                ] = self.regression_model.get_params()[item]
        return model_param

    def fit(self, X, y):
        """
        Build a partition regressor from the training set (X,y).

        Parameters:
            X: Array-like or sparse matrix, shape = [n_samples, n_features] \
                The training input samples. Internally, it will be converted to \
                ``dtype=np.float32`` and if a sparse matrix is provided to a \
                sparse ``csc_matrix``.

            y: Array-like, shape = [n_samples] or [n_samples, n_outputs] \
                The target values (real numbers). Use ``dtype=np.float64`` and \
                ``order='C'`` for maximum efficiency.

        Returns:
            self : object.

        """
        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

        if not isinstance(y, pd.Series):
            if y.ndim == 2:
                y = y.ravel()
            y = pd.Series(y)

        if self.partition_features is None:
            self.partition_features = list(X.columns)

        if self.regression_features is None:
            self.regression_features = list(X.columns)

        if self.scaling:
            from sklearn.preprocessing import StandardScaler

            self.scalerObj = StandardScaler()
            self.input_features = list(X.columns)
            X = self.scalerObj.fit_transform(X)
            X = pd.DataFrame(X)
            X.columns = self.input_features

        self.partition_model.fit(X[self.partition_features], y)

        # Lam added
        self.partition_model.non_int = list(range(len(self.partition_features)))

        partition_model_output = self.partition_model.__getattribute__(
            self.partition_model_predict_function
        )(X[self.partition_features])
        partitions = list(set(partition_model_output))
        self.regression_models = {}
        for partition in partitions:
            # collect the subset of samples and build models
            x_id = np.where(partition_model_output == partition)[0]
            tmpX = X.iloc[x_id, :]
            tmpy = y.iloc[x_id]
            tmp_part_mdl = clone(self.regression_model)
            tmp_part_mdl.fit(tmpX[self.regression_features], tmpy)
            self.regression_models[partition] = tmp_part_mdl
        return self

    def predict(self, X):

        """
        Predict regression value for X.

        Parameters:
            X : array-like or sparse matrix of shape = [n_samples, n_features] \
                The input samples. Internally, it will be converted to \
                ``dtype=np.float32`` and if a sparse matrix is provided \
                to a sparse ``csr_matrix``.
        
        Returns:
            self: object

        """
        check_is_fitted(self, "partition_model")
        check_is_fitted(self, "regression_models")

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

        if self.scaling:
            X = self.scalerObj.transform(X)
            X = pd.DataFrame(X)
            X.columns = self.input_features

        final_out = []
        partition_model_output = self.partition_model.__getattribute__(
            self.partition_model_predict_function
        )(X[self.partition_features])
        X = X[self.regression_features].values
        for pred_ind, pred_out in enumerate(partition_model_output):
            final_out.append(
                self.regression_models[pred_out].predict(X[pred_ind].reshape(1, -1))[0]
            )
        return np.array(final_out)

    def predict_proba(self, X):
        """
        Predict class probabilities of the input samples X.

        The predicted class probability is the fraction of samples of the same \
        class in a leaf.

        Parameters:
            X : Array-like or sparse matrix of shape = [n_samples, n_features] \
                The input samples. Internally, it will be converted to \
                ``dtype=np.float32`` and if a sparse matrix is provided \
                to a sparse ``csr_matrix``.

        Returns:
            self: object

        """
        check_is_fitted(self, "partition_model")
        check_is_fitted(self, "regression_models")

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

        if self.scaling:
            X = self.scalerObj.transform(X)
            X = pd.DataFrame(X)
            X.columns = self.input_features

        final_out = []
        partition_model_output = self.partition_model.__getattribute__(
            self.partition_model_predict_function
        )(X[self.partition_features])
        X = X[self.regression_features].values
        for pred_ind, pred_out in enumerate(partition_model_output):
            final_out.append(
                self.regression_models[pred_out].predict_proba(
                    X[pred_ind].reshape(1, -1)
                )[0]
            )
        return np.array(final_out)

    def predict_partition(self, X):

        check_is_fitted(self, "partition_model")

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

        if self.scaling:
            X = self.scalerObj.transform(X)
            X = pd.DataFrame(X)
            X.columns = self.input_features

        partition_model_output = self.partition_model.__getattribute__(
            self.partition_model_predict_function
        )(X[self.partition_features])
        return partition_model_output

    def generate_error_per_leaf(self, X, y):
        """
        Compute prediction error (R-sq, MAE, MSE etc.) for each \
        partitioned space, or a leaf if the partition_model is a \
        DecisionTreeRegressor().

        Parameters:
            X: Array-like or sparse matrix, shape = [n_samples, n_features] \
               The training input samples. Internally, it will be converted to \
               ``dtype=np.float32`` and if a sparse matrix is provided \
               to a sparse ``csc_matrix``.
            y: Array-like, shape = [n_samples] or [n_samples, n_outputs] \
               The target values (real numbers). Use ``dtype=np.float64`` and \
               ``order='C'`` for maximum efficiency.

        Returns:
            self: object
        """

        check_is_fitted(self, "partition_model")
        check_is_fitted(self, "regression_models")

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X, columns=["tmpclm_" + str(i) for i in range(X.shape[1])])

        if not isinstance(y, pd.Series):
            y = pd.Series(y)

        if self.scaling:
            X = self.scalerObj.transform(X)
            X = pd.DataFrame(X)
            X.columns = self.input_features

        predict_y = self.predict(X)
        predict_part = self.predict_partition(X)
        tmpDb = pd.DataFrame([predict_y, predict_part, y]).transpose()
        tmpDb.columns = ["predicted", "leaf", "real"]
        tmpDb["error"] = np.abs(tmpDb["predicted"] - tmpDb["real"])
        tmpDb = tmpDb[["leaf", "error"]]
        result = tmpDb.groupby("leaf").describe()
        return result

    def _get_decision_nodes(self, regtree_DTmodel, x_var):
        decision_nodes = []
        tree = regtree_DTmodel.tree_
        thresholds = tree.threshold.copy()
        for i in range(len(tree.feature)):
            feature = tree.feature[i]
            if feature != -2:
                f_index = regtree_DTmodel.non_int[feature]
                if self.scaling:
                    tmp_f_index = self.input_features.index(
                        self.partition_features[f_index]
                    )
                    thresholds[i] *= np.sqrt(self.scalerObj.var_[tmp_f_index])
                    thresholds[i] += self.scalerObj.mean_[tmp_f_index]
                decision_nodes.append([x_var[f_index], thresholds[i]])
        return pd.DataFrame(decision_nodes)

    def _get_regression_model_coefficient(self, reg_model):
        if reg_model.__class__.__name__ == "RANSACRegressor":
            return reg_model.estimator_.coef_
        else:
            return reg_model.coef_

    def _get_regression_model_intercept(self, reg_model):
        if reg_model.__class__.__name__ == "RANSACRegressor":
            return reg_model.estimator_.intercept_
        else:
            return reg_model.intercept_

    def _get_terms(self, reg_model):
        if self.scaling:
            # add here - based on regression features
            map_index = []
            for item in self.regression_features:
                map_index.append(self.input_features.index(item))
            coefficients = self._get_regression_model_coefficient(reg_model) / np.sqrt(
                self.scalerObj.var_[map_index]
            )
            var_intercepts = (
                -self._get_regression_model_coefficient(reg_model)
                / np.sqrt(self.scalerObj.var_[map_index])
                * self.scalerObj.mean_[map_index]
            )
            intercept = self._get_regression_model_intercept(reg_model) + np.sum(
                var_intercepts
            )
            return intercept, coefficients
        else:
            return (
                self._get_regression_model_intercept(reg_model),
                self._get_regression_model_coefficient(reg_model),
            )

    def _make_regression_rows(self, reg_model, x_var, y_var, min_value, max_value):
        intercept, coefficients = self._get_terms(reg_model)
        df = pd.DataFrame(columns=["y_var", "reg_num"])
        df["x_var"] = x_var
        df["x_min"] = min_value
        df["x_max"] = max_value
        df["coefficient"] = coefficients
        df["intercept"] = intercept
        df["y_var"] = y_var
        return df

    def _update_reg_tree_tbl(self, DT_model, x_var):
        left = DT_model.tree_.children_left
        right = DT_model.tree_.children_right
        threshold = DT_model.tree_.threshold

        features = []
        for item in DT_model.tree_.feature:
            if item != -2:
                features.append(x_var[item])
            else:
                features.append("L")
        # features = [x_var[i] for i in DT_model.tree_.feature]

        decision_nodes = self._get_decision_nodes(DT_model, x_var)

        # get ids of child nodes
        idx = np.argwhere(left == -1)[:, 0]

        def recurse(left, right, child, lineage=None):
            if lineage is None:
                lineage = [child]
            if child in left:
                parent = np.where(left == child)[0].item()
                split = "l"
            else:
                parent = np.where(right == child)[0].item()
                split = "r"

            lineage.append((parent, split, threshold[parent], features[parent]))

            if parent == 0:
                lineage.reverse()
                return lineage
            else:
                return recurse(left, right, parent, lineage)

        index_dv = pd.DataFrame(list(np.where(left > 0))).T
        decision_nodes = pd.concat([decision_nodes, index_dv], axis=1)
        decision_nodes.columns = ["x_var", "threshold", "ind"]
        decision_nodes = decision_nodes.set_index("ind")
        tree_map = {}
        for n in decision_nodes.index:
            tree_map[n] = {}
            tree_map[n]["min"] = []
            tree_map[n]["max"] = []

        for i in idx:
            tree_sum = recurse(left, right, i)
            for j in range(len(tree_sum) - 1):
                decision_ind = tree_sum[j][0]
                if tree_sum[j][1] == "l":
                    tree_map[decision_ind]["max"].append(i)
                else:
                    tree_map[decision_ind]["min"].append(i)
        return tree_map, decision_nodes

    def get_coefficient_table(self, min_value=np.NINF, max_value=np.inf):
        """
        Get a coefficient table.

        Parameters:
            min_value (optional): The minimum value of the variables.
            max_value (optional): The maximum value of the variables.
    
        Returns:
            Table : DataFrame.
                Achieve a table with information of coefficients and intercept \
                corresponding to each feature variables. We could also obtain the \
                min and max values of each feature variables. 
        """
        check_is_fitted(self, "partition_model")
        check_is_fitted(self, "regression_models")

        df_model = pd.DataFrame()
        for reg_model_key in self.regression_models.keys():
            reg_model = self.regression_models[reg_model_key]
            df_part = self._make_regression_rows(
                reg_model, self.regression_features, "target", min_value, max_value
            )
            df_part["reg_num"] = reg_model_key
            df_model = pd.concat([df_model, df_part])
        tree_map, decision_nodes = self._update_reg_tree_tbl(
            self.partition_model, self.partition_features
        )
        regtree_spec_tbl = df_model.copy()
        for n in tree_map.keys():
            var = decision_nodes.loc[n, "x_var"]
            val = decision_nodes.loc[n, "threshold"]
            regtree_spec_tbl.loc[
                (regtree_spec_tbl["reg_num"].isin(tree_map[n]["min"]))
                & (regtree_spec_tbl["x_var"] == var),
                "x_min",
            ] = val
            regtree_spec_tbl.loc[
                (regtree_spec_tbl["reg_num"].isin(tree_map[n]["max"]))
                & (regtree_spec_tbl["x_var"] == var),
                "x_max",
            ] = val
        return regtree_spec_tbl

    def get_optimization_table(self, param_data, min_value=np.NINF, max_value=np.inf):
        """
        Get an optimization table. 
        
        Parameters:
            param_data (Dictionary): The observed variable and its value. \
                Example: {feature_01: value_01} \
                where ``feature_01 = 'F1'`` and ``value_01 = 10``.
            min_value: The minimum value of the variables (optional)
            max_value: The maximum value of the variables (optional)

        Returns:
            Table : DataFrame. 
                Achieve a table with information of coefficients and intercept \
                corresponding to each feature variables after MERGING with an \
                observed variable. We could also obtain the min and max values \
                of each feature variables.
        """
        check_is_fitted(self, "partition_model")
        check_is_fitted(self, "regression_models")

        df_raw = pd.DataFrame.from_dict(param_data, orient="index")
        param_data = df_raw.copy()
        param_data.columns = ["x_val"]

        regtree_to_opt = pd.DataFrame()
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
        bad_reg = bad_rows["reg_num"]
        df_model = df_model.loc[(-df_model["reg_num"].isin(bad_reg))]
        df_model.loc[df_model["x_val"].notna(), "offset"] = (
            df_model["coefficient"] * df_model["x_val"]
        )
        df_model = df_model.join(
            df_model.groupby("reg_num")["offset"].sum(), on="reg_num", rsuffix="_r"
        )
        df_model.drop("offset", inplace=True, axis=1)
        df_model["intercept"] = df_model["intercept"] + df_model["offset_r"]
        df_model.drop("offset_r", inplace=True, axis=1)
        df_model = df_model.loc[(df_model["x_val"]).isna()]

        df_model = df_model.sort_values(by=["reg_num", "x_var"])
        df_model["reg_num"] = df_model["reg_num"].astype(int)
        df_model.drop("x_val", axis=1, inplace=True)
        df_model["running_intercept"] = 0
        regtree_to_opt = pd.concat([regtree_to_opt, df_model], axis=0)
        return regtree_to_opt

    def get_optimization_json(self, param_data, min_value=np.NINF, max_value=np.inf):
        """
        Get an optimization table in json format. 
        
        Parameters:
            param_data: The observed variable and its value. Dictionary type. \
                Example: {feature_01: value_01} \
                where ``feature_01 = 'F1'`` and ``value_01 = 10``.
            min_value(optional): The minimum value of the variables.
            max_value(optional): The maximum value of the variables.

        Returns:
            json form.
            Achieve a table with information of coefficients and intercept \
            corresponding to each feature variables after MERGING with an observed \
            variable. We could also obtain the min and max values of each feature variables. 
        """
        check_is_fitted(self, "partition_model")
        check_is_fitted(self, "regression_models")

        regtree_to_opt = self.get_optimization_table(param_data, min_value, max_value)
        import json

        regtree_to_opt_df = json.loads(regtree_to_opt.reset_index().to_json())
        dicts = []
        for index in list(regtree_to_opt_df["index"].keys()):
            dicts.append(
                {
                    "y_var": regtree_to_opt_df["y_var"][index],
                    "reg_num": regtree_to_opt_df["reg_num"][index],
                    "x_var": regtree_to_opt_df["x_var"][index],
                    "x_min": regtree_to_opt_df["x_min"][index],
                    "x_max": regtree_to_opt_df["x_max"][index],
                    "coefficient": regtree_to_opt_df["coefficient"][index],
                    "intercept": regtree_to_opt_df["intercept"][index],
                    "running_intercept": regtree_to_opt_df["running_intercept"][index],
                }
            )
        regtree_to_opt_dicts = {"ModelToOptimization": dicts}
        return regtree_to_opt_dicts
