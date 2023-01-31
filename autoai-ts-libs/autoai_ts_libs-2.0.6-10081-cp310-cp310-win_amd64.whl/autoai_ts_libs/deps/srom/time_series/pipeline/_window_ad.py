import inspect
import inspect
import logging

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import TimeTensorTransformer
from autoai_ts_libs.deps.srom.time_series.utils.anomaly import (
    contextual_score,
    chi_square_score,
    q_score,
    adaptive_window_score,
    window_score,
)
from autoai_ts_libs.deps.srom.pipeline.anomaly_pipeline import AnomalyPipeline


LOGGER = logging.getLogger(__name__)

class WindowAD(Pipeline):
    """
    This extends iid outlier detection to time series by applying windowing techniques.

    Parameters
    ----------
    steps (list, required): list of steps to perform on the WindowAD pipeline, in sklearn format
    feature_columns (list, required): list of indices of feature columns
    target_columns (list, required): list of indices of target columns
    lookback_win (int or string, optional): integer of lookback window, or 'auto'
    pred_win (int, optional): the prediction window to be used, default is 0.
    time_column (string, optional): string value of time column name
    store_lookback_history (bool, optional): should be set to True if predict() is going to be used on continuous\
                data which is related to the train data, to append the lookback history, default is False
    distance_metric (string, optional): the distance metric to be used at the final estimator stage of the pipeline
    observation_window (int, optional): the observation window to be used by WindowAD. Default is 10
    scoring_method (string, optional): the scoring method to be used for post processing. Choose between\
                ['iid','Chi-Square','Q-Score','Sliding-Window','Contextual-Anomaly']. Default is 'iid'.
    scoring_threshold (int, optional): scoring threshold to use for predictions to be classified as anomalous
    """

    def __init__(
            self,
            steps,
            *,
            feature_columns=None,
            target_columns=None,
            lookback_win=None,
            pred_win=0,
            time_column=None,
            store_lookback_history=True,
            distance_metric='mse',
            observation_window=10,
            scoring_method="iid",
            scoring_threshold=10,
            scoring_noise_adjustment=None,
            reverse_windowing=False,
    ):
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.time_column = time_column
        self.store_lookback_history = store_lookback_history
        self.distance_metric = distance_metric
        self.observation_window = observation_window
        self.scoring_method = scoring_method
        self.scoring_threshold = scoring_threshold
        self.steps = steps
        self.scoring_noise_adjustment = scoring_noise_adjustment
        self.reverse_windowing = reverse_windowing
        super(WindowAD, self).__init__(steps=steps)

    def _store_lookback_history_X(self, X):
        """Utility function : it must be called from fit() or its method called out of fit()

        Args:
            X ([np.array]): Input to store lookback history from

        Raises:
            Exception: Lookback information is not stored inside model
        """
        if self.store_lookback_history:
            if self.lookback_win > 0:
                self.lookback_data_X_ = X[-self.lookback_win:, :]
            else:
                self.lookback_data_X_ = None
        else:
            raise Exception("Lookback information is not stored inside model")

    def _add_lookback_history_to_X(self, X):
        """Predict or Anomaly Score

        Args:
            X ([np.array]): data

        Raises:
            Exception: Lookback information is not stored inside model

        Returns:
            [np.array]: X after lookback history is added
        """
        if not isinstance(X, (np.generic, np.ndarray)):
            raise Exception("X needs to be a numpy array")
        if self.store_lookback_history:
            if X is None:
                if self.lookback_win > 0:
                    return self.lookback_data_X_.copy()
                else:
                    return X
            else:
                if self.lookback_win > 0:
                    new_X = np.concatenate([self.lookback_data_X_, X])
                    return new_X
                else:
                    return X
        else:
            raise Exception("Lookback information is not stored inside model")

    def _set_steps_for_fit(self):
        """
        Must be called from fit only
        """
        step_params = [
            "lookback_win",
            "target_columns",
            "feature_columns",
            "time_column",
        ]

        for step in self.steps:
            params = {}
            for param in step_params:
                if param in step[1].get_params().keys():
                    params[param] = getattr(self, param)
            if len(params) != 0:
                step[1].set_params(**params)

        # dealing with Flatten and pred_win
        # pred_win needs to be set to 0 so that there is no delay between the feature array and target array,
        # else there will be a mismatch
        for step in self.steps:
            if (
                    isinstance(step[1], TimeTensorTransformer)
                    and "pred_win" in step[1].get_params().keys()
            ):
                step[1].set_params(pred_win=0)

    def _forward_fit_data_transformation(self, X, y=None):
        """This must be called from fit only.

        Args:
            X (np.array): Input to pass through forward fit transformation
            y (np.array, optional): Labels. Defaults to None.

        Returns:
            np.array: Transformed data
        """

        Xt = X
        yt = y
        for _, transformer in self.steps[:-1]:
            if hasattr(transformer, "fit_transform"):
                res = transformer.fit_transform(Xt, yt)
            else:
                res = transformer.fit(Xt, yt).transform(Xt)

            if isinstance(res, tuple):
                x_res = res[0]
                yt = res[1]
            else:
                x_res = res

            Xt = x_res

        return Xt

    def _validate_estimator(self):
        """
        Check if estimator contains 'anomaly score' as a function, else raise exception. Internal function.
        """
        check_op = getattr(self.steps[-1][1], "anomaly_score", None)
        check_dec_op = getattr(self.steps[-1][1], "decision_function", None)
        if not (check_op and callable(check_op)):
            if not (check_dec_op and callable(check_dec_op)):
                raise Exception(
                    "The Estimator does not have decision_function or an anomaly_score function"
                )
            else:
                self.anomaly_function = self.steps[-1][1].decision_function
        else:
            self.anomaly_function = self.steps[-1][1].anomaly_score

    def set_anomaly_scoring_params(self, scoring_method, scoring_threshold):
        """
        Method to store the scoring parameters, in the case where model is already fit,
        but scoring is performed with different parameters on the pretrained model.

        Args:
            scoring_method (string): Scoring method to use to predict and score
            scoring threshold (float): numerical value to use as scoring threshold while post processing
        """
        self.scoring_method = scoring_method
        self.scoring_threshold = scoring_threshold

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

        # init the parameter of each component
        self._validate_estimator()
        self._set_steps_for_fit()

        self.train_shape_ = X.shape

        if self.store_lookback_history:
            self._store_lookback_history_X(X)

        Xt = self._forward_fit_data_transformation(X, y)
        self.steps[-1][1].fit(Xt)

        # now we pass the X to trained pipeline and generate the training
        # anomaly score
        # training_error = len(X)
        anomaly_score = self.anomaly_function(Xt)
        if len(anomaly_score.shape) == 1:
            anomaly_score = anomaly_score.reshape(-1, 1)
        if len(anomaly_score) != self.train_shape_[0]:
            dummy = np.full(
                (
                    self.train_shape_[0] - anomaly_score.shape[0],
                    anomaly_score.shape[1],
                ),
                np.NaN,
            )
            self.training_error_ = np.concatenate((dummy, anomaly_score))
        else:
            self.training_error_ = anomaly_score

        return self

    def _forward_data_transformation(self, X, is_lookback_appended, lookback_win):
        """
        Utility function
        Since this is windowing, data must be coming in some sequence
        Either X can be same as training data or X can be new samples

        Args:
            X (np.array): Input to pass through forward data transformation
            is_lookback_appended (np.boolean): Denotes whether lookback is already appended to X
            lookback_win (float): The lookback window used in forward data transformation

        Returns:
            np.array: Transformed data
        """

        Xt = X.copy()
        for _, transformer in self.steps[:-1]:
            params = {}

            if "is_lookback_appended" in inspect.signature(transformer.transform).parameters:
                params["is_lookback_appended"] = is_lookback_appended
            if "lookback_win" in inspect.signature(transformer.transform).parameters:
                params["lookback_win"] = lookback_win

            if len(params) > 0:
                res = transformer.transform(Xt, **params)
            else:
                res = transformer.transform(Xt)

            if isinstance(res, tuple):
                x_res = res[0]
            else:
                x_res = res

            Xt = x_res

        return Xt

    def _predict_batch(self, X, prediction_type="batch"):
        if prediction_type not in ["batch", "training"]:
            return None
        if X is not None:
            if self.scoring_method == "iid":  # Point Anomaly

                is_lookback_appended = False
                lookback_win = 0
                X_shape = X.shape
                X = self._forward_data_transformation(
                    X, is_lookback_appended, lookback_win
                )
                predictions = self.steps[-1][1].predict(X)
                start_index = 0
                if len(predictions.shape) == 1:
                    predictions = predictions.reshape(-1, 1)
                if len(predictions) != X_shape[0]:
                    dummy = np.full(
                        (
                            X_shape[0] - predictions.shape[0],
                            predictions.shape[1],
                        ),
                        np.NaN,
                    )
                    predictions = np.concatenate((dummy, predictions))
                return predictions[start_index:]
            else:
                # here we call decision_function and then
                if self.scoring_method == "Contextual-Anomaly":
                    """
                    this place anomaly_score return the
                    We shd align the output with other methods like
                    1 and -1
                    """
                    score_ = self.anomaly_score(
                        X, return_threshold=False, prediction_type=prediction_type
                    )
                    score_[score_ > 0] = -1
                    score_[score_ != -1] = 1
                    return score_

                else:
                    """
                    we need to generate the label
                    """
                    score_, threshold_ = self.anomaly_score(
                        X, return_threshold=True, prediction_type=prediction_type
                    )
                    score_[score_ > threshold_] = -1
                    score_[score_ != -1] = 1
                    return score_
        else:
            return self._predict_empty_test(
                X, prediction_type=prediction_type, start_index=0
            )

    def _predict_recent(self, X, prediction_type="recent"):
        if X is not None:
            if self.scoring_method == "iid":  # Point Anomaly

                is_lookback_appended = False
                lookback_win = 0

                if self.store_lookback_history:
                    # we add the lookback window
                    old_X_shape = X.shape
                    X = self._add_lookback_history_to_X(X)
                    is_lookback_appended = True
                    lookback_win = X.shape[0] - old_X_shape[0]

                X = self._forward_data_transformation(
                    X, is_lookback_appended, lookback_win
                )
                predictions = self.steps[-1][1].predict(X)

                start_index = -1
                return predictions[start_index:]
            else:
                # here we call decision_function and then
                """
                    we need to generate the label
                    """
                score_, threshold_ = self.anomaly_score(
                    X, return_threshold=True, prediction_type=prediction_type
                )
                if self.scoring_method == "Contextual-Anomaly":
                    threshold_ = 0
                score_[score_ > threshold_] = -1
                score_[score_ != -1] = 1
                return score_
        else:
            return self._predict_empty_test(
                X, prediction_type=prediction_type, start_index=-1
            )

    def _predict_sliding(self, X, prediction_type="sliding"):
        if X is not None:
            X_shape = X.shape
            if self.scoring_method == "iid":  # Point Anomaly

                is_lookback_appended = False
                lookback_win = 0

                if self.store_lookback_history:
                    # we add the lookback window
                    old_X_shape = X.shape
                    X = self._add_lookback_history_to_X(X)
                    is_lookback_appended = True
                    lookback_win = X.shape[0] - old_X_shape[0]

                X = self._forward_data_transformation(
                    X, is_lookback_appended, lookback_win
                )
                predictions = self.steps[-1][1].predict(X)

                start_index = -X_shape[0]
                return predictions[start_index:]
            else:
                # here we call decision_function and then
                """
                we need to generate the label
                """
                score_, threshold_ = self.anomaly_score(
                    X, return_threshold=True, prediction_type=prediction_type
                )
                if score_.shape != threshold_.shape:
                    if score_.ndim == 2 and score_.shape[1] == 1:
                        score_ = score_.reshape((-1))
                if self.scoring_method == "Contextual-Anomaly":
                    threshold_ = 0
                score_[score_ > threshold_] = -1
                score_[score_ != -1] = 1
                return score_
        else:
            X_shape = (0)
            return self._predict_empty_test(
                X, prediction_type=prediction_type, start_index=-X_shape[0]
            )

    def _predict_empty_test(self, X, prediction_type, start_index):
        if self.scoring_method == "Contextual-Anomaly":
            """
            this place anomaly_score return the
            We shd align the output with other methods like
            1 and -1
            """
            score_ = self.training_error_.copy()
            score_[score_ > 0] = -1
            score_[score_ != -1] = 1
            return score_
        else:
            score_ = self.training_error_.copy()
            if self.scoring_method == "iid":
                return score_[start_index:]
            else:
                score_, threshold_ = self.anomaly_score(
                    X=X, return_threshold=True, prediction_type=prediction_type
                )
                if len(score_.shape) > 1:
                    score_ = score_.reshape(-1)
                    if len(threshold_.shape) > 1:
                        threshold_ = threshold_.reshape(-1)
                score_[score_ > threshold_] = -1
                score_[score_ != -1] = 1
                return score_

    def _get_threshold(self, anomaly_scores):
        Ap = AnomalyPipeline()
        x = anomaly_scores[~np.isnan(anomaly_scores)]
        a_threshold = np.max(x)
        if self.scoring_method in ['otsu','otsu_label', 'otsu_oneshot_label']:
            a_threshold = Ap._otsu_threshold(x)
        elif self.scoring_method in ['contamination','contamination_oneshot_label','contamination_label']:
            a_threshold = Ap._contamination_threshold(x, self.scoring_threshold)
        elif self.scoring_method in ['adaptivecontamination','adaptivecontamination_label','adaptivecontamination_oneshot_label']:
            a_threshold = Ap._adaptive_contamination_threshold(x, self.scoring_threshold)
        elif self.scoring_method in ['qfunction','qfunction_oneshot_label','qfunction_label']:
            a_threshold = Ap._qfunction_threshold(x, self.scoring_threshold)
        elif self.scoring_method in ['medianabsolutedev','medianabsolutedev_label','medianabsolutedev_oneshot_label']:
            a_threshold = Ap._medianabsolutedev_threshold(x, self.scoring_threshold)
        elif self.scoring_method in ['std','std_oneshot_label','std_label']:
            a_threshold = Ap._std_threshold(x, self.scoring_threshold)
        elif self.scoring_method in ['max','max_oneshot_label','max_label']:
            a_threshold = Ap._max_threshold(x, self.scoring_threshold)
        return a_threshold

    def _predict_anomaly_label(self, X, prediction_type):
        """_summary_

        Args:
            anomaly_score (_type_): real value score : train + test
            test_len (_type_): last test_len score in anomaly_score are from test
        """
        test_len = len(X)
        anomaly_score = self.anomaly_score(X, prediction_type=prediction_type)
        if test_len > len(anomaly_score):
            raise Exception('Wrong value')
        
        if anomaly_score.ndim == 1:
            anomaly_score = anomaly_score.reshape(-1,1)
        
        ad_labels = np.ones(test_len)
        # too narrow difference we do not apply AD score
        if self.scoring_noise_adjustment is None or np.nanmax(anomaly_score) > self.scoring_noise_adjustment:
            if '_oneshot' in self.scoring_method:
                # static threshold
                ad_threshold = self._get_threshold(self.training_error_)
                for i in range(test_len):
                    if ad_threshold < anomaly_score[i]:
                        ad_labels[i] = -1
            else:
                reference_score = np.concatenate((self.training_error_,anomaly_score))
                if self.reverse_windowing:
                    reference_score = self._adjust_anomaly_score(reference_score)  # added a line to adjust the window size
                for i in range(test_len):
                    current_timepoint = len(reference_score) - test_len + i + 1
                    # obtain label at time point len(anomaly_score) - (i + test_len)
                    tmp_reference_score = reference_score[:current_timepoint]
                    #print(i, len(tmp_reference_score), len(self.training_error_))
                    ad_threshold = self._get_threshold(tmp_reference_score)
                    # the above function you can write
                    # added following extra condition to get rid of a case where signal is too clean and no noise
                    if ad_threshold < anomaly_score[i]:
                        ad_labels[i] = -1
            
        if len(ad_labels.shape)==1:
            ad_labels = ad_labels.reshape(-1,1)
        return ad_labels
        
    def _adjust_anomaly_score(self, scores):
        """
        Utility function for the adjustment
        """
        window_size = self.lookback_win
        unwindowed_length = (window_size - 1) + len(scores)
        mapped = np.full(shape=(unwindowed_length, window_size), fill_value=np.nan)
        mapped[:len(scores), 0] = scores[:,0]
        
        for w in range(1, window_size):
            mapped[:, w] = np.roll(mapped[:, 0], w)
            
        return np.nanmean(mapped, axis=1)[window_size-1:]


    def predict(self, X, prediction_type="recent"):
        """
        This is a predict function
        X is considered as a training data if prediction_type = batch or training

        when prediction type = iid
            1. add last window to current X
            2. now we obtained window X
            3. We apply the predict call of the underlying pipelines

        otherwise it is considered as time series
            1. the anomaly score coming from adjacent time point
               will be analyzed joinly

        Output: must match with input length
        """
        if "_label" in self.scoring_method:
            return self._predict_anomaly_label(X, prediction_type=prediction_type)
        elif prediction_type == "recent":
            score = self._predict_recent(X, prediction_type=prediction_type)
        elif prediction_type == "sliding":
            score = self._predict_sliding(X, prediction_type=prediction_type)
        elif prediction_type == "batch" or prediction_type == "training":
            score = self._predict_batch(X, prediction_type=prediction_type)
        else:
            raise Exception("Unsupported prediction type")
        return score

    def anomaly_score(self, X, return_threshold=False, prediction_type="recent"):
        """
        anomaly score
            batch and training does not append the data
            rest append the lookback window data to given X (this is in sync with )

         Args:
            X (np.array): Test data to predict on
            return_threshold (np.boolean): Returns anomaly threshold if set to True else does not
            prediction_type (string): Prediction type to use to perform prediction among ["batch", "training", "sliding", "recent"]

        Returns:
            np.array: Transformed data
        """
        if prediction_type not in ["batch", "training", "sliding", "recent"]:
            raise Exception("Not supported...")
        if X is not None:

            is_lookback_appended = False
            lookback_win = 0
            X_shape = X.shape

            if self.store_lookback_history:
                if prediction_type not in ["training", "batch"]:
                    # we add the lookback window
                    old_X_shape = X.shape
                    X = self._add_lookback_history_to_X(X)
                    is_lookback_appended = True
                    lookback_win = X.shape[0] - old_X_shape[0]

            # the new X and old X mush be of same length
            Xt = self._forward_data_transformation(
                X.copy(), is_lookback_appended, lookback_win
            )
            anomaly_score = self.anomaly_function(Xt)
        else:
            anomaly_score = self.training_error_.copy()
            X_shape = self.training_error_.shape

        # now we have anomaly score, these score we can tread as iid (if scoring method is iid)
        # else we post process as follow
        if self.scoring_method not in ["iid", "Contextual-Anomaly"] and '_label' not in self.scoring_method:
            if prediction_type not in ["batch", "training"]:
                if anomaly_score is not None:
                    anomaly_score = np.concatenate(
                        (self.training_error_, anomaly_score.reshape(-1, 1),)
                    )
                else:
                    anomaly_score = self.training_error_.copy()
            anomaly_score = self._post_process_anomaly(anomaly_score, return_threshold)
        elif self.scoring_method == "Contextual-Anomaly":
            # post processing is required here
            # we shd send the anomaly_score as similar as other anomaly score
            # it will be 0 for no anomaly and anomaly_severity for the other cases
            # if we fix this, then its very easy for us to align all the code in predict
            score = self._post_process_anomaly(anomaly_score, return_threshold)
            score = pd.DataFrame(score)
            if X is not None:
                output = pd.DataFrame(
                    0, index=range(len(X)), columns=["Score"], dtype="float"
                )
            else:
                output = pd.DataFrame(
                    0, index=range(len(anomaly_score)), columns=["Score"], dtype="float"
                )
            for row in score.itertuples(index=False):
                output.loc[row[0]: row[1], "Score"] = row[2]
            anomaly_score = output["Score"].values
        elif "_label" in self.scoring_method:
            if len(anomaly_score.shape)==1:
                anomaly_score = anomaly_score.reshape(-1,1)

        # Check if lengths are equal
        if return_threshold and self.scoring_method not in ["iid", "Contextual-Anomaly"]:
            threshold_ = anomaly_score[1]
            anomaly_score = anomaly_score[0]
        if prediction_type in ['batch', 'training']:
            if len(anomaly_score.shape) == 1:
                anomaly_score = anomaly_score.reshape(-1, 1)
                if return_threshold and self.scoring_method not in ["iid", "Contextual-Anomaly"]:
                    threshold_ = threshold_.reshape(-1, 1)
            if len(anomaly_score) != X_shape[0]:
                dummy = np.full(
                    (
                        X_shape[0] - anomaly_score.shape[0],
                        anomaly_score.shape[1],
                    ),
                    np.NaN,
                )
                anomaly_score = np.concatenate((dummy, anomaly_score))
                if return_threshold and self.scoring_method not in ["iid", "Contextual-Anomaly"]:
                    threshold_ = np.concatenate((dummy, threshold_))

        # What score to be returned
        start_index = 0
        if prediction_type == "recent":
            start_index = -1
        elif prediction_type == "sliding":
            start_index = -X_shape[0]
        else:
            pass
        if return_threshold:
            if self.scoring_method == "iid":
                return (anomaly_score[start_index:], anomaly_score[start_index:])
            elif self.scoring_method == "Contextual-Anomaly":
                return (anomaly_score[start_index:], np.zeros(anomaly_score.shape))
            else:
                return (
                    anomaly_score[start_index:, ],
                    threshold_[start_index:, ],
                )
        return anomaly_score[
               start_index:,
               ]

    def _post_process_anomaly(self, anomaly_score, return_threshold):
        if return_threshold:
            if self.scoring_method == "Chi-Square":
                return chi_square_score(
                    anomaly_score, self.observation_window, self.scoring_threshold
                )
            elif self.scoring_method == "Q-Score":
                return q_score(
                    anomaly_score, self.observation_window, self.scoring_threshold
                )
            elif self.scoring_method == "Sliding-Window":
                return window_score(
                    anomaly_score, self.observation_window, self.scoring_threshold
                )
            elif self.scoring_method == "Adaptive-Sliding-Window":
                return adaptive_window_score(
                    anomaly_score, self.observation_window, self.scoring_threshold
                )
            elif self.scoring_method == "Contextual-Anomaly":
                return contextual_score(
                    anomaly_score,
                    scoring_threshold=self.scoring_threshold,
                    observation_window=self.observation_window,
                )
            else:
                raise Exception("Wrong option for scoring method")
        else:
            if self.scoring_method == "Chi-Square":
                return chi_square_score(
                    anomaly_score, self.observation_window, self.scoring_threshold
                )[0]
            elif self.scoring_method == "Q-Score":
                return q_score(
                    anomaly_score, self.observation_window, self.scoring_threshold
                )[0]
            elif self.scoring_method == "Sliding-Window":
                return window_score(
                    anomaly_score, self.observation_window, self.scoring_threshold
                )[0]
            elif self.scoring_method == "Adaptive-Sliding-Window":
                return adaptive_window_score(
                    anomaly_score, self.observation_window, self.scoring_threshold
                )[0]
            elif self.scoring_method == "Contextual-Anomaly":
                return contextual_score(
                    anomaly_score,
                    scoring_threshold=self.scoring_threshold,
                    observation_window=self.observation_window,
                )
            else:
                raise Exception("Wrong option for scoring method")

