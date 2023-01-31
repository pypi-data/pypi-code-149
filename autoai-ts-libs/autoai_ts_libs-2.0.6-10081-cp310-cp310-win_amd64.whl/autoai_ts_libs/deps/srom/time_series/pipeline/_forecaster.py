import logging

import numpy as np
from sklearn.metrics._scorer import neg_mean_absolute_error_scorer
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.preprocessing.transformer import DualTransformer, XYScaler
from autoai_ts_libs.deps.srom.preprocessing.ts_column_transformer import TSColumnTransformer
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import TargetTransformer
from autoai_ts_libs.deps.srom.time_series.models.base import StateSpaceEstimator
from autoai_ts_libs.deps.srom.utils.estimator_utils import check_model_type_is_dl
from autoai_ts_libs.deps.srom.utils.time_series_utils import get_max_lookback

LOGGER = logging.getLogger(__name__)


class Forecaster(Pipeline):
    """
    Class which wraps sklearn's pipeline to accomodate transformers
    which modify both X and y. This transformation is required in
    Time Series modelling tasks.

    Parameters
    ----------
        steps (list of tuples): This is the list of tuples storing items
            in the pipeline. For eg.
                steps =  [('log', Log(...)),
                            ('xgboost', Xgboost(...))]
        feature_columns : (numpy array)
            feature indices
        target_columns : (numpy array)
            target indices
        lookback_win : (int, optional, default = 5)
            Look-back window for the model.
        pred_win : (int, optional, default = 1)
            Look-ahead window for the model.
        time_column : (int, optional, default = -1)
            time column index
        store_lookback_history : (Bool, optional, default = False)
            whether to store the lookback window in the attribute lookback_data_X

        This is a bare minimum class, we need
        where steps are coming from autoai_ts_libs.deps.srom dag and other parameters we expect to be obtained from the
        time series pipelines
    """

    def __init__(
        self,
        steps,
        *,
        feature_columns=None,
        target_columns=None,
        time_column=None,
        id_column=None,
        lookback_win=None,
        pred_win=None,
        store_lookback_history=False,
        scoring=neg_mean_absolute_error_scorer,
        pred_interval_regressor=None,
    ):
        self.steps = steps
        self.id_column = id_column
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.time_column = time_column
        self.store_lookback_history = store_lookback_history
        self.scoring = scoring
        self.pred_interval_regressor = pred_interval_regressor

    def set_scoring(self, scoring):
        """
        Set the scoring mechanism.
        """
        self.scoring = scoring

    def _check_X(self, X):
        """This method return X, after conversion to appropriate columns"""

        if isinstance(X, (np.ndarray, np.generic)):
            X = X.copy()
            if X.dtype != "object":
                X = X.astype(object)
            clm_for_float_conversion = list(
                set(self.feature_columns + self.target_columns)
            )
            X[:, clm_for_float_conversion] = X[:, clm_for_float_conversion].astype(
                float
            )

        return X

    def _store_lookback_history_X(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Raises:
            Exception: [description]
        """
        if self.store_lookback_history:
            max_lookback = get_max_lookback(self.lookback_win)
            if max_lookback > 0:
                self.lookback_data_X = X[-max_lookback:, :].copy()
            else:
                self.lookback_data_X = None
        else:
            raise Exception("Lookback information is not stored inside model")

    def _add_lookback_history_to_X(self, X):
        """[summary]

        Args:
            X ([type]): [description]

        Raises:
            Exception: [description]

        Returns:
            [type]: [description]
        """
        if self.store_lookback_history:
            max_lookback = get_max_lookback(self.lookback_win)
            if X is None:
                if max_lookback > 0:
                    return self.lookback_data_X.copy()
                else:
                    return X
            else:
                if max_lookback > 0:
                    new_X = np.concatenate([self.lookback_data_X, X])
                    return new_X
                else:
                    return X
        else:
            raise Exception("Lookback information is not stored inside model")

    def _forward_fit_data_transformation(self, X, y=None):
        """This function is called during fit call

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        Xt = X
        yt = y
        step_pos = 0
        for transformer_name, transformer in self.steps[:-1]:
            if hasattr(transformer, "fit_transform"):
                res = transformer.fit_transform(Xt, yt)
            elif isinstance(transformer, XYScaler):
                res = transformer.fit(Xt, yt).transform(Xt, yt)
            else:
                res = transformer.fit(Xt, yt).transform(Xt)

            if isinstance(res, tuple):
                x_res = res[0]
                yt = res[1]
            else:
                x_res = res

            if isinstance(transformer, (TSColumnTransformer, FeatureUnion)):
                # for all subsequence call
                for step in self.steps[step_pos + 1 : -1]:
                    if (
                        "feature_columns" in step[1].get_params()
                        and "lookback_win" in step[1].get_params()
                    ):
                        feature_columns = getattr(step[1], "feature_columns")
                        fc_len = len(feature_columns)
                        feature_columns = feature_columns + [
                            Xt.shape[1] + i for i in range(x_res.shape[1] - Xt.shape[1])
                        ]
                        setattr(step[1], "feature_columns", feature_columns)
                        lookback_win = getattr(step[1], "lookback_win")
                        if isinstance(lookback_win, list):
                            lookback_win = lookback_win + [
                                1 for i in range(x_res.shape[1] - Xt.shape[1])
                            ]
                        else:
                            lookback_win = ([lookback_win] * fc_len) + [
                                1 for i in range(x_res.shape[1] - Xt.shape[1])
                            ]
                        setattr(step[1], "lookback_win", lookback_win)

                """
                # adding condition to modify StateSpaceEstimator
                if isinstance(self.steps[-1][1], StateSpaceEstimator):
                    target_columns = getattr(self.steps[-1][1], "target_columns")
                    target_columns = target_columns + [
                        Xt.shape[1] + i for i in range(x_res.shape[1] - Xt.shape[1])
                    ]
                    setattr(self.steps[-1][1], "target_columns", target_columns)
                """

            if x_res.shape[1] < Xt.shape[1]:
                # i want to capture a logging that a component has reduce
                # number of columns and any use of featue column may result in
                # index violation
                LOGGER.info(
                    "Applying %s has reduced the number of columns. It may results in violation",
                    str(transformer_name),
                )

            Xt = x_res
            step_pos += 1
        return Xt, yt

    def _forward_data_transformation(self, X, y=None):
        """Calling this method once all component are fitted

        Args:
            X ([type]): [description]
            y ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        Xt = X
        yt = y
        res = []
        for _, transformer in self.steps[:-1]:
            res = transformer.transform(Xt)

            if isinstance(res, tuple):
                x_res = res[0]
                yt = res[1]
            else:
                x_res = res

            Xt = x_res

        return Xt, yt

    def _inverse_data_transformation(self, y=None):
        y_pred = y
        # process in revese order
        for _, transformer in self.steps[-2::-1]:
            # we now do all check we want to do
            if isinstance(transformer, TargetTransformer):
                if self.pred_win == 1:
                    # y_pred = y_pred.reshape(-1, len(self.target_columns))
                    y_pred = transformer.inverse_transform(y_pred)
                    y_pred = y_pred.reshape(-1, len(self.target_columns))
                else:
                    y_pred = transformer.inverse_transform(y_pred)
                    _c = []
                    c_steps = int(len(y_pred) / len(self.target_columns))
                    for c_step in range(c_steps):
                        start_idx = c_step * len(self.target_columns)
                        end_idx = start_idx + len(self.target_columns)
                        col_pred = y_pred[start_idx:end_idx]
                        row_pred = np.transpose(col_pred)
                        _c.append(row_pred.flatten())
                    y_pred = np.array(_c)
            elif isinstance(transformer, DualTransformer):
                y_pred = transformer.inverse_transform(y_pred)
            else:
                pass
        return y_pred

    def _get_fit_X_y(self, X, y=None):
        """
        This method create an srom estimator object and then call its fit

        This is an utility function to get the prepared Xt and yt
        """

        if self.lookback_win is None and not isinstance(
            self.steps[-1][1], StateSpaceEstimator
        ):
            raise Exception("Set the lookback window")

        self._set_steps_for_fit()

        # only data transform if model is instance of StateSpaceEstimator
        if isinstance(self.steps[-1][1], StateSpaceEstimator):
            # transform data based on transformers
            Xt, yt = self._forward_fit_data_transformation(X, y)
        else:
            # stores lookback window
            if self.store_lookback_history:
                self._store_lookback_history_X(X)

            # transform data based on transformers
            Xt, yt = self._forward_fit_data_transformation(X, y)

        return Xt, yt

    def _set_steps_for_fit(self):
        """
        Sets time series params for step components
        """
        step_params = [
            "feature_columns",
            "target_columns",
            "lookback_win",
            "pred_win",
            "time_column",
            "id_column",
        ]

        for step in self.steps:
            params = {}
            for param in step_params:
                if param in step[1].get_params().keys():
                    params[param] = getattr(self, param)
            if len(params) != 0:
                # we push responsibility back to the classifier
                step[1].set_params(**params)

    def fit(self, X, y=None):
        """
        This method create an srom estimator object and then call its fit

        Important steps:
        feature_columns attribute need to pass to the respecting object of steps

        for each step in self.steps:
            get its parameter
            set some of its parameter such as feature_columns, target_columns
            this one need little bit co-ordination across different method such as
            flatten etc
        """
        # this is for this pipeline
        X = self._check_X(X)
        if self.lookback_win is None and not isinstance(
            self.steps[-1][1], StateSpaceEstimator
        ):
            raise Exception("Set the lookback window to integer value")

        # ## Commenting out the following block to
        # if self.lookback_win is not None and isinstance(
        #     self.steps[-1][1], StateSpaceEstimator
        # ):
        #     raise Exception("Lookback window has no meaning")

        # set timeseries parameters in components in steps
        self._set_steps_for_fit()

        # only data transform if model is instance of StateSpaceEstimator
        if isinstance(self.steps[-1][1], StateSpaceEstimator):
            # transform data based on transformers
            Xt, yt = self._forward_fit_data_transformation(X, y)
        else:
            # stores lookback window
            if self.store_lookback_history:
                self._store_lookback_history_X(X)

            # transform data based on transformers
            Xt, yt = self._forward_fit_data_transformation(X, y)
            post_shape = Xt.shape

            #  The model params will
            # automatically  be updated for input dimension in the case of DL models.
            # The models considered as Deep Learning are in the list
            # MODEL_TYPES_SUPPORTED_FOR_DEEP_LEARNING
            # update train pipelines with params
            if hasattr(self.steps[-1][1], "set_params") and callable(
                getattr(self.steps[-1][1], "set_params")
            ):
                # update input and output dimension of the Deep learning models
                if (
                    "input_dimension" in self.steps[-1][1].get_params()
                    and "output_dimension" in self.steps[-1][1].get_params()
                    and check_model_type_is_dl(self.steps[-1][1])
                ):

                    # get estimator input dim
                    in_dim = self.steps[-1][1].get_params()["input_dimension"]
                    new_in_dim = None
                    new_out_dim = None

                    if len(in_dim) > 1:
                        # in case of models where input shape is defined like (6,10) (keras)
                        new_in_dim = (post_shape[1], post_shape[2])
                    else:
                        # in case of models where input shape is defined like (6,) (keras)
                        new_in_dim = (post_shape[1],)

                    if "output_type" in self.steps[-1][1].get_params():
                        if self.steps[-1][1].get_params()["output_type"] == "flatten":
                            new_out_dim = self.pred_win * len(self.target_columns)
                            yt = yt.reshape(Xt.shape[0], new_out_dim)
                        elif (
                            self.steps[-1][1].get_params()["output_type"]
                            == "structured"
                        ):
                            new_out_dim = (self.pred_win, len(self.target_columns))
                        else:
                            raise Exception("Output Dimension is not set properly")
                    else:
                        new_out_dim = self.pred_win * len(self.target_columns)

                    self.steps[-1][1].set_params(input_dimension=new_in_dim)
                    self.steps[-1][1].set_params(output_dimension=new_out_dim)

        #self.steps[-1][1].fit(Xt, yt)
        if self.pred_interval_regressor:
            from sklearn.base import clone
            self.pred_interval_regressor.estimator = clone(self.steps[-1][1])
            self.pred_interval_regressor.fit(Xt, yt)
        else:
            self.steps[-1][1].fit(Xt, yt)

        return self

    def _get_predict_X(self, X, prediction_type="forecast"):
        """This method discover what is feeded inside the final steps of the model

        Args:
            X ([type]): [description]
            prediction_type (str, optional): [description]. Defaults to "forecast".

        Raises:
            Exception: [description]

        Returns:
            [type]: [description]
        """
        X = self._check_X(X)

        # adding looking back window to X
        if isinstance(self.steps[-1][1], StateSpaceEstimator):
            # this is a type of estimator that do not break the time series into tabular
            Xt, _ = self._forward_data_transformation(X)

        else:
            if self.store_lookback_history:
                if prediction_type != "training":
                    X = self._add_lookback_history_to_X(X)

            if prediction_type == "forecast":
                max_lookback = get_max_lookback(self.lookback_win)
                if (X.shape[0] - max_lookback) < 0:
                    raise Exception(
                        "lookback window cannot be greater than the data-set size."
                    )

                X = X[
                    (X.shape[0] - max_lookback) :,
                ]
                if self.pred_win > 0:
                    dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                    X = np.concatenate((X, dummy))
            elif prediction_type == "rolling":
                # Then pad the series so we can get the output prediction for
                # all time points, not just those we also have targets for
                if self.pred_win > 0:
                    dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                    X = np.concatenate((X, dummy))

            Xt, _ = self._forward_data_transformation(X)
        return Xt

    def predict(self, X, prediction_type="forecast"):
        """
        This method call the predict of an srom estimator
        """

        # this is for this pipeline
        X = self._check_X(X)

        # adding looking back window to X
        if isinstance(self.steps[-1][1], StateSpaceEstimator):
            # this is a type of estimator that do not break the time series into tabular
            Xt, _ = self._forward_data_transformation(X)
            y_pred = self.steps[-1][1].predict(Xt, prediction_type=prediction_type)
            y_pred = self._inverse_data_transformation(y_pred)
        else:
            if self.store_lookback_history:
                if prediction_type != "training":
                    X = self._add_lookback_history_to_X(X)

            if prediction_type == "forecast":
                max_lookback = get_max_lookback(self.lookback_win)
                if (X.shape[0] - max_lookback) < 0:
                    raise Exception(
                        "lookback window cannot be greater than the data-set size."
                    )

                X = X[
                    (X.shape[0] - max_lookback) :,
                ]
                if self.pred_win > 0:
                    dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                    X = np.concatenate((X, dummy))
            elif prediction_type == "rolling":
                # Then pad the series so we can get the output prediction for
                # all time points, not just those we also have targets for
                if self.pred_win > 0:
                    dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                    X = np.concatenate((X, dummy))

            Xt, _ = self._forward_data_transformation(X)
            if self.pred_interval_regressor:
                y_pred, _ = self.pred_interval_regressor.predict(Xt, alpha=0.05)
            else:
                y_pred = self.steps[-1][1].predict(Xt)

            y_pred = y_pred.reshape(Xt.shape[0], -1)
            # convert structure output to the flatten output
            # this one we will keep and update as time pass
            if "output_type" in self.steps[-1][1].get_params():
                if self.steps[-1][1].get_params()["output_type"] in [
                    "structured",
                    "flatten",
                ]:
                    y_pred = y_pred.reshape(Xt.shape[0], -1)
            else:
                y_pred = self._inverse_data_transformation(y_pred)

        if prediction_type == "forecast":
            y_pred = y_pred.reshape(-1, len(self.target_columns))

        return y_pred

    def predict_interval(self, X, prediction_type="forecast"):
        """
        This method call the predict of an srom estimator
        """

        # this is for this pipeline
        X = self._check_X(X)

        # adding looking back window to X
        if isinstance(self.steps[-1][1], StateSpaceEstimator):
            # this is a type of estimator that do not break the time series into tabular
            Xt, _ = self._forward_data_transformation(X)
            y_pred = self.steps[-1][1].predict(Xt, prediction_type=prediction_type)
            y_pred = self._inverse_data_transformation(y_pred)
        else:
            if self.store_lookback_history:
                if prediction_type != "training":
                    X = self._add_lookback_history_to_X(X)

            if prediction_type == "forecast":
                max_lookback = get_max_lookback(self.lookback_win)
                if (X.shape[0] - max_lookback) < 0:
                    raise Exception(
                        "lookback window cannot be greater than the data-set size."
                    )

                X = X[
                    (X.shape[0] - max_lookback) :,
                ]
                if self.pred_win > 0:
                    dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                    X = np.concatenate((X, dummy))
            elif prediction_type == "rolling":
                # Then pad the series so we can get the output prediction for
                # all time points, not just those we also have targets for
                if self.pred_win > 0:
                    dummy = np.full((self.pred_win, X.shape[1]), 0.0)
                    X = np.concatenate((X, dummy))

            Xt, _ = self._forward_data_transformation(X)
            y_pred, y_pis = self.pred_interval_regressor.predict(Xt, alpha=0.05)

            y_pis_lower = y_pis[:,0]
            y_pis_higher = y_pis[:,1]

            y_pred = y_pred.reshape(Xt.shape[0], -1)
            y_pis_lower = y_pis_lower.reshape(Xt.shape[0], -1)
            y_pis_higher = y_pis_higher.reshape(Xt.shape[0], -1)
            # convert structure output to the flatten output
            # this one we will keep and update as time pass
            if "output_type" in self.steps[-1][1].get_params():
                if self.steps[-1][1].get_params()["output_type"] in [
                    "structured",
                    "flatten",
                ]:
                    y_pred = y_pred.reshape(Xt.shape[0], -1)
                    y_pis_lower = y_pis_lower.reshape(Xt.shape[0], -1)
                    y_pis_higher = y_pis_higher.reshape(Xt.shape[0], -1)
            else:
                y_pred = self._inverse_data_transformation(y_pred)
                y_pis_lower = self._inverse_data_transformation(y_pis_lower)
                y_pis_higher = self._inverse_data_transformation(y_pis_higher)

        if prediction_type == "forecast":
            y_pred = y_pred.reshape(-1, len(self.target_columns))
            y_pis_lower = y_pis_lower.reshape(-1, len(self.target_columns))
            y_pis_higher = y_pis_higher.reshape(-1, len(self.target_columns))

        return np.hstack([y_pis_lower, y_pred, y_pis_higher])

    def score(self, X, y=None, sample_weight=None):
        """
        Similar to `score` method in sklearn.pipeline.Pipeline.
        The input and return params of the transformers have been modified
        to incorporate X and y transformation.

        Parameters
        ----------
            X : {array-like, sparse matrix} of shape (n_samples, n_features)
                The training input samples. Sparse matrices are accepted only if
                they are supported by the base estimator.
            y : array-like of shape (n_samples,)
                The target values (class labels in classification, real numbers in
                regression).
            sample_weight : array-like of shape (n_samples,), default=None
                Sample weights. If None, then samples are equally weighted.
                Note that this is supported only if the base estimator supports
                sample weighting.
        Returns
        -------
            score : float
        """

        # this is for this pipeline
        X = self._check_X(X)

        def _generate_ground_truth(X):
            new_X = X[:, self.target_columns].copy()
            n = new_X.shape[0]
            return np.hstack(
                new_X[i : 1 + n + i - self.pred_win : 1]
                for i in range(0, self.pred_win)
            )

        # _generate_ground_truth_approach2 should also work
        y_gt = _generate_ground_truth(X)

        if not self.store_lookback_history:
            max_lookback = get_max_lookback(self.lookback_win)
            y_gt = y_gt[max_lookback:]

        score_params = {}
        if sample_weight is not None:
            score_params["sample_weight"] = sample_weight

        # ??? evaluation vs sliding???
        y_pred = self.predict(X, prediction_type="sliding")

        if sample_weight is not None:
            return self.scoring._sign * self.scoring._score_func(
                y_gt, y_pred, sample_weight=sample_weight, **self.scoring._kwargs
            )
        else:
            return self.scoring._sign * self.scoring._score_func(
                y_gt, y_pred, **self.scoring._kwargs
            )

