import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.utils.validation import check_array, check_is_fitted
from sklearn.pipeline import FeatureUnion


class ExtendedColumnTransformer(ColumnTransformer):
    """It appends the data at the end of original X
    Args:
        ColumnTransformer ([type]): [description]
    Returns:
        [type]: [description]
    """

    def __init__(
        self,
        transformers,
        *,
        remainder="drop",
        sparse_threshold=0.3,
        n_jobs=None,
        transformer_weights=None,
        verbose=False
    ):
        super().__init__(
            transformers,
            remainder=remainder,
            sparse_threshold=sparse_threshold,
            n_jobs=n_jobs,
            transformer_weights=transformer_weights,
            verbose=verbose,
        )

    def fit_transform(self, X, y=None):
        """[summary]
        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.
        """
        tmpX = super(ExtendedColumnTransformer, self).fit_transform(X, y)
        self.n_features_ = X.shape[1]
        self.n_features_created_ = tmpX.shape[1]
        X = np.hstack((X, tmpX))
        return X

    def transform(self, X, y=None):
        """[summary]
        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.
        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "n_features_created_")
        check_is_fitted(self, "n_features_")
        tmpX = super(ExtendedColumnTransformer, self).transform(X)
        X = np.hstack((X, tmpX))
        return X


class TSColumnTransformer(BaseEstimator, TransformerMixin):
    """
    Base class for Time Series column Transformer.

    Args:
        time_column (optional, list): list of size 1 containing time column index
        feature_columns (optional, list): list containing feature column indices
        target_columns (optional, list): list containing target column indices
        replace (optional, Boolean): True to replace original columns after transformation
        remainder (optional, str): string denoting what to do with other columns-
            'drop': refers to dropping other columns not in feature and target column list
            'passthrough': allows to keep other columns
            source - https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html
        transform_target (optional, Boolean): True to transform target column as well
    """

    def __init__(
        self, time_column=[0], feature_columns=[0], replace=False,
    ):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            replace (bool, optional): [description]. Defaults to False.
        """
        self.time_column = time_column
        self.feature_columns = feature_columns
        self.replace = replace

    def _generate_fit_features(self, X):
        """
        Transforms the 2D data by applying features on specified columns.

        Args:
            X (2D numpy array): Input numpy array representing TS data

        Return:
            X_features (2D numpy array): Transformed TS data. Should be same shape as input X
        """

        # setting the value of transformed column information as feature columns
        # set the weight to be remember if any
        self.n_features_ = X.shape[1]
        Xt = X.copy()
        if not self.replace:
            self.n_features_created_ = len(self.feature_columns)
        else:
            self.n_features_created_ = 0
        return Xt

    def _generate_transform_features(self, X):
        """[summary]

        Args:
            X ([type]): [description]
        """
        return X.copy()

    def _extend_feature_cols(self, X, X_features):
        """
        Extends feature columns from the transformed dataset  into original
        thus extending the features to original data without replacement
        """
        X_features = X_features[:, self.feature_columns]
        X_tf = np.concatenate((X, X_features), axis=1)
        return X_tf

    def fit(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        X[:, self.feature_columns] = check_array(
            X[:, self.feature_columns], accept_sparse=True
        )
        self._generate_fit_features(X)
        return self

    def transform(self, X, y=None):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        check_is_fitted(self, "n_features_")
        check_is_fitted(self, "n_features_created_")

        # ignoring dtypes='numeric' to allow datetime
        X[:, self.feature_columns] = check_array(
            X[:, self.feature_columns], accept_sparse=True
        )

        if X.shape[1] != self.n_features_:
            raise ValueError(
                "Shape of input is different from what was seen" "in `fit`"
            )

        # finding moving means of only feature columns and letting other columns remain constant
        X_tf = self._generate_transform_features(X)

        # returned dataframe should be either replaced or extended by
        if not self.replace:
            X_tf = self._extend_feature_cols(X, X_tf)

        return X_tf

    def fit_transform(self, X, y=None):
        X[:, self.feature_columns] = check_array(
            X[:, self.feature_columns], accept_sparse=True
        )
        X_tf = self._generate_fit_features(X)

        # returned dataframe should be either replaced or extended by
        if not self.replace:
            X_tf = self._extend_feature_cols(X, X_tf)

        return X_tf


class TSColumnUnion(FeatureUnion):
    def __init__(
        self, transformer_list, time_column=[0], feature_columns=[0],
    ):
        """[summary]

        Args:
            transformer_list (list, required):
            time_column
            feature_columns (list, optional): [description]. Defaults to [0].
        """
        for tf in transformer_list:
            if isinstance(tf, tuple) and not isinstance(tf[1], TSColumnTransformer):
                raise TypeError(
                    "Each item in `transformer_list` should be a tuple and 2nd element should be an instance of `TSColumnTransformer` class."
                )

        self.time_column = time_column
        self.feature_columns = feature_columns
        super(TSColumnUnion, self).__init__(transformer_list=transformer_list)

    def set_params(self, **kwargs):
        super(TSColumnUnion, self).set_params(**kwargs)
        for user_params in kwargs:
            for param in self.get_params():
                if param.endswith("__" + str(user_params)) and hasattr(
                    self.get_params()[param.split("__")[0]], param.split("__")[1]
                ):
                    self.set_params(**{param: kwargs[user_params]})

    def fit_transform(self, X, y=None):
        """ """
        X_tf = X.copy()
        for i, tf in enumerate(self.transformer_list):
            X_tf_ = tf[1].fit_transform(X)
            X_tf = np.concatenate(
                (X_tf, X_tf_[:, -tf[1].n_features_created_ :]), axis=1
            )
        return X_tf

    def transform(self, X, y=None):
        """ """
        X_tf = X.copy()
        for i, tf in enumerate(self.transformer_list):
            X_tf_ = tf[1].transform(X)
            X_tf = np.concatenate(
                (X_tf, X_tf_[:, -tf[1].n_features_created_ :]), axis=1
            )
        return X_tf


class ExponentialSmoothing(TSColumnTransformer):
    """[summary]

    Args:
        TSColumnTransformer ([type]): [description]
    """

    def __init__(
        self, time_column=[0], feature_columns=[0], replace=False, alpha=0.9,
    ):
        """[summary]

        Args:
            feature_columns (list, optional): [description]. Defaults to [0].
            replace (bool, optional): [description]. Defaults to False.
        """
        super(ExponentialSmoothing, self).__init__(
            time_column=time_column, feature_columns=feature_columns, replace=replace,
        )

        self.alpha = alpha

    def _exponential_smoothening(self, x, _alpha, pre_calc=None):
        """Finds exponential smoothened elements in an array.

        Args:
            _alpha (float): value of exponential weightage.
            pre_calc (float): if pre computed value is given, it is weighted in with the first value.
        """

        res = np.zeros(len(x))

        # if first value is provided, use it in weighted calculation
        if pre_calc:
            res[0] = _alpha * x[0] + (1 - _alpha) * pre_calc
        else:
            res[0] = x[0]

        # for the rest of the values
        for i in range(1, len(x)):
            res[i] = _alpha * x[i] + (1 - _alpha) * res[i - 1]
        return res

    def _generate_fit_features(self, X):
        """
        Transforms the 2D data by applying exponential features on specified columns.

        Args:
            X (2D numpy array): Input numpy array representing TS data
            use_weighted (boolean):  True if pre-calculated weights to be used
            weights (1D array): Array containing the weights of pre-calculations for each feature.
                The weights array should contain same number of element as features in X (X.shape[1]).
                The features which are not in self.feature_columns are ignored.

        Return:
            X_features (2D numpy array): Transformed TS data. Should be same shape as input X
        """

        self.n_features_ = X.shape[1]

        X_features = np.transpose(
            np.array(
                [
                    self._exponential_smoothening(X[:, i], self.alpha)
                    if i in self.feature_columns
                    else X[:, i]
                    for i in range(X.shape[1])
                ]
            )
        )

        # make sure X_features.shape == X.shape

        if not self.replace:
            self.n_features_created_ = len(self.feature_columns)
        else:
            self.n_features_created_ = 0
        # Storing last rows values for moving mean of features
        self.weights = X_features[-1, :]
        return X_features

    def _generate_transform_features(self, X):
        """
        Transforms the 2D data by applying exponential features on specified columns.

        Args:
            X (2D numpy array): Input numpy array representing TS data
            use_weighted (boolean):  True if pre-calculated weights to be used
            weights (1D array): Array containing the weights of pre-calculations for each feature.
                The weights array should contain same number of element as features in X (X.shape[1]).
                The features which are not in self.feature_columns are ignored.

        Return:
            X_features (2D numpy array): Transformed TS data. Should be same shape as input X
        """
        X_features = np.transpose(
            np.array(
                [
                    self._exponential_smoothening(
                        X[:, i], self.alpha, pre_calc=self.weights[i]
                    )
                    if i in self.feature_columns
                    else X[:, i]
                    for i in range(X.shape[1])
                ]
            )
        )
        return X_features


# def moving_mean(x, prev_mean=0, prev_count=0):
#     """Finds moving mean of elements in an array.

#     Args:
#         x (array-type, numpy or pandas 1D array)
#         prev_mean(float): previous elements
#         prev_count(float): previous number of elements

#     Returns:
#         res: transformed x
#     """
#     res = np.zeros(len(x))

#     for i in range(len(x)):
#         res[i] = (x[i] + (prev_count * prev_mean)) / (prev_count + 1)
#         prev_count += 1
#         prev_mean = res[i]
#     return res


# class MovingMeanColumnTransformer(TSColumnTransformer):
#     """[summary]

#     Args:
#         TSColumnTransformer ([type]): [description]
#     """

#     def __init__(self, time_column=[0], feature_columns=[0], replace=False):
#         """[summary]

#         Args:
#             feature_columns (list, optional): [description]. Defaults to [0].
#             replace (bool, optional): [description]. Defaults to False.
#         """
#         super(MovingMeanColumnTransformer, self).__init__(
#             time_column=time_column, feature_columns=feature_columns, replace=replace
#         )

#         self.transformer_fn = moving_mean
#         self.prev_mean = None
#         self.prev_count = None

#     def fit(self, X, y=None):
#         """[summary]

#         Args:
#             X ([type]): [description]
#             y ([type], optional): [description]. Defaults to None.

#         Returns:
#             [type]: [description]
#         """
#         super(MovingMeanColumnTransformer, self).fit(X)

#         # finding moving means of only feature columns and letting other columns remain constant
#         X = np.transpose(
#             np.array(
#                 [
#                     self.transformer_fn(X[:, i])
#                     if i in self.feature_columns
#                     else X[:, i]
#                     for i in range(X.shape[1])
#                 ]
#             )
#         )
#         # Storing last rows values for moving mean of features
#         self.prev_mean = X[-1, :]
#         self.prev_count = len(X)

#     def transform(self, X, y=None, include_trained_weights=True):
#         """[summary]

#         Args:
#             X ([type]): [description]
#             y ([type], optional): [description]. Defaults to None.

#         Returns:
#             [type]: [description]
#         """
#         X = super(MovingMeanColumnTransformer, self).transform(X)

#         # if prev computed mean needs to be included in calculation
#         if include_trained_weights:

#             # include column wise means in calculations
#             X_tf = np.transpose(
#                 np.array(
#                     [
#                         self.transformer_fn(
#                             X[:, i],
#                             prev_mean=self.prev_mean[i],
#                             prev_count=self.prev_count[i],
#                         )
#                         for i in self.feature_columns
#                     ]
#                 )
#             )
#         else:
#             # if previous values are not to be included:
#             X_tf = np.transpose(
#                 np.array([self.transformer_fn(X[:, i]) for i in self.feature_columns])
#             )

#         # replace feature columns in original dataframe
#         if self.replace:
#             X_res = X
#             # add feature columns based on transformed X
#             for i, v in enumerate(self.feature_columns):
#                 X_res[:, v] = X_tf[:, i]

#         else:
#             # Concatenating original X and transformed X - column-wise
#             X_res = np.concatenate((X, X_tf), axis=1)

#         return X_res
