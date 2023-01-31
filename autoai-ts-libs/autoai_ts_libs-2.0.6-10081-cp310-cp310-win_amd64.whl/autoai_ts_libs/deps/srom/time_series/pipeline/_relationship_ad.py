import inspect
import inspect
import logging

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.NMT_anomaly import NMT_anomaly
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


class RelationshipAD(Pipeline):
    """Relationship based anomaly detection pipeline. Finds anomalies in the relationship between the feature variables.

    Parameters
    ----------
        steps : list of pipeline steps
            List of ReconstructAD pipelines to be used.
        feature_columns : list, optional
            List of feature columns to be used
        target_columns : list, optional
            List of target columns to be used
        lookback_win : int, optional
            Lookback window used for prediction
        time_column : string/int, optional
            Column name of time column
        pred_win : int, optional
            Prediction window used for transformations
        store_lookback_history : boolean, optional
            Boolean value to decide if lookback window history should be stored. To be set to true if test data \
            is continuous from the train data
        distance_metric : string, optional
            unused : TODO
        observation_window : int, optional
            Observation window is used to compute anomaly scores by specified scoring_method. Defaults to 10.
        scoring_method : string, optional
            Anomaly scoring method to compute anomaly score in specified mathematical,
            or statistical method. The computed score is used to label anomalies by
            analyzing residuals computed. Defaults to Chi-Square.
        scoring_threshold : int, optional
            Scoring threhold is used to label computed anomaly score as anomaly or normal. Defaults to 10.
    """

    def __init__(
        self,
        steps,
        *,
        feature_columns=None,
        target_columns=None,
        lookback_win=None,
        time_column=None,
        pred_win=0,
        store_lookback_history=True,
        distance_metric=None,
        observation_window=10,
        scoring_method="iid",
        scoring_threshold=10,
        scoring_noise_adjustment=None,
        reverse_windowing=False,
    ):
        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.time_column = time_column
        self.pred_win = pred_win
        self.store_lookback_history = store_lookback_history
        self.observation_window = observation_window
        self.scoring_method = scoring_method
        self.scoring_threshold = scoring_threshold
        self.distance_metric = distance_metric
        self.steps = steps
        self.scoring_noise_adjustment = scoring_noise_adjustment
        self.reverse_windowing = reverse_windowing
        super(RelationshipAD, self).__init__(steps=steps)

    def set_anomaly_scoring_params(self, scoring_method, scoring_threshold):
        """
        This is a scoring threshold
        """
        self.scoring_method = scoring_method
        self.scoring_threshold = scoring_threshold

    def _store_lookback_history_X(self, X):
        """Stores lookback history for X based on the lookback window
        """
        if self.store_lookback_history:
            if self.lookback_win > 0:
                self.lookback_data_X = X[-self.lookback_win:, :]
            else:
                self.lookback_data_X = None
        else:
            raise Exception("Lookback information is not stored inside model")

    def _add_lookback_history_to_X(self, X):
        """Adds lookback history to X if lookback history is stored, only if test data is continuous from train data. \
        Set store_lookback_history to true if data is continuous across train and test
        """
        if self.store_lookback_history:
            if X is None:
                if self.lookback_win > 0:
                    return self.lookback_data_X.copy()
                else:
                    return X
            else:
                if self.lookback_win > 0:
                    new_X = np.concatenate([self.lookback_data_X, X])
                    return new_X
                else:
                    return X
        else:
            raise Exception("Lookback information is not stored inside model")

    def _forward_fit_data_transformation(self, X, y=None):
        """
        Internal function to get the time series data
        """
        Xt = X
        yt = y
        for _, transformer in self.steps[:-1]:
            if hasattr(transformer, "fit_transform"):
                res = transformer.fit_transform(Xt, yt)
            else:
                res = transformer.fit(Xt, yt).transform(Xt)

            if isinstance(res, tuple):
                if isinstance(self.steps[-1][1], NMT_anomaly):
                    x_res = res
                else:
                    x_res = res[0]  # yt = res[1]
            else:
                x_res = res

            Xt = x_res

        return Xt

    def _forward_data_transformation(self, X, is_lookback_appended, lookback_win):
        """
        Internal function to get the time series data
        """
        # now call the anomaly score generation, which generate the anomaly score
        Xt = X
        res = []
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
                if isinstance(self.steps[-1][1], NMT_anomaly):
                    x_res = res
                else:
                    x_res = res[0]
            else:
                x_res = res

            Xt = x_res

        return Xt

    def _set_steps_for_fit(self):
        """
        Must be called from fit only
        """
        step_params = [
            "lookback_win",
            "target_columns",
            "feature_columns",
            "time_column",
            "distance_metric",
        ]

        for step in self.steps:
            params = {}
            for param in step_params:
                if param in step[1].get_params().keys():
                    if getattr(self, param) is not None:
                        params[param] = getattr(self, param)
            if len(params) != 0:
                step[1].set_params(**params)

        # dealing with Flatten and pred_win
        for step in self.steps:
            if (
                isinstance(step[1], TimeTensorTransformer)
                and "pred_win" in step[1].get_params().keys()
            ):
                step[1].set_params(pred_win=0)

    def _validate_estimator(self):
        """
        Check if estimator contains 'anomaly score' as a function, else raise exception. Internal function.
        """
        check_op = getattr(self.steps[-1][1], "anomaly_score", None)
        if not (check_op and callable(check_op)):
            raise Exception("The Estimator does not have anomaly_score function")

    def fit(self, X, y=None):
        """
        """
        self.train_shape_ = X.shape
        self._validate_estimator()
        self._set_steps_for_fit()
        Xt = X.copy()
        if self.store_lookback_history:
            self._store_lookback_history_X(Xt)

        # do the windowing here and then call X
        Xt = self._forward_fit_data_transformation(Xt)
        if isinstance(self.steps[-1][1], NMT_anomaly):
            self.steps[-1][1].fit(Xt, y)
            anomaly_score = self.steps[-1][1].anomaly_score(Xt)

        else:
            self.steps[-1][1].fit(Xt, y)
            anomaly_score = self.steps[-1][1].anomaly_score(Xt)
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
                for i in range(test_len):
                    current_timepoint = len(reference_score) - test_len + i + 1
                    # obtain label at time point len(anomaly_score) - (i + test_len)
                    tmp_reference_score = reference_score[:current_timepoint]
                    #print(i, len(tmp_reference_score), len(self.training_error_))
                    ad_threshold = self._get_threshold(tmp_reference_score)
                    # the above function you can write
                    # added following extra condition to get rid of a case where signal is too clean and no noise
                    if ad_threshold < np.nanmax(anomaly_score[i]):
                        ad_labels[i] = -1
            
        if len(ad_labels.shape)==1:
            ad_labels = ad_labels.reshape(-1,1)
        return ad_labels


    def _predict_batch(self, X, prediction_type="batch"):
        if prediction_type not in ["batch", "training"]:
            return None
        if X is not None:
            if self.scoring_method == "iid":  # Point Anomaly

                is_lookback_appended = False
                lookback_win = 0

                X = self._forward_data_transformation(
                    X, is_lookback_appended, lookback_win
                )
                predictions = self.steps[-1][1].predict(X)
                start_index = 0
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
                if hasattr(self.steps[-1][1], "sliding_window_size"):
                    if self.steps[-1][1].sliding_window_size > X.shape[0]:
                        self.steps[-1][1].sliding_window_size = X.shape[0] - 1
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
                if hasattr(self.steps[-1][1], "sliding_window_size"):
                    if self.steps[-1][1].sliding_window_size > X.shape[0]:
                        self.steps[-1][1].sliding_window_size = X.shape[0] - 1
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
                if self.scoring_method == "Contextual-Anomaly":
                    threshold_ = 0
                score_[score_ > threshold_] = -1
                score_[score_ != -1] = 1
                return score_
        else:
            X_shape = 0
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

    def anomaly_score(self, X, return_threshold=False, prediction_type="recent"):
        """
        anomaly score
            batch and training does not append the data
            rest append the lookback window data to given X (this is in sync with )
        """
        if prediction_type not in ["batch", "training", "sliding", "recent"]:
            raise Exception("Not supported...")
        if X is not None:
            X_shape = X.shape
            is_lookback_appended = False
            lookback_win = 0
            # add the lookback window
            if self.store_lookback_history:
                if prediction_type not in ["training", "batch"]:
                    # we add the lookback window
                    old_X_shape = X.shape
                    X = self._add_lookback_history_to_X(X)
                    is_lookback_appended = True
                    lookback_win = X.shape[0] - old_X_shape[0]

            Xt = self._forward_data_transformation(
                X.copy(), is_lookback_appended, lookback_win
            )
            if hasattr(self.steps[-1][1], "sliding_window"):
                if self.steps[-1][1].sliding_window < Xt.shape[0]:
                    self.steps[-1][1].sliding_window = Xt.shape[0] - 1
            anomaly_score = self.steps[-1][1].anomaly_score(Xt)
        else:
            X_shape = 0
            anomaly_score = self.training_error_.copy()

            # now we have anomaly score, these score we can tread as iid (if scoring method is iid)
            # else we post process as follow
        if self.scoring_method not in ["iid", "Contextual-Anomaly"] and '_label' not in self.scoring_method:
            if prediction_type not in ["batch", "training"]:
                if anomaly_score.ndim == 1:
                    anomaly_score = np.concatenate(
                        (self.training_error_, anomaly_score.reshape(-1, 1),)
                    )
                else:
                    anomaly_score = np.concatenate(
                        (self.training_error_, anomaly_score,)
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
                output.loc[row[0] : row[1], "Score"] = row[2]
            anomaly_score = output["Score"].values
        elif "_label" in self.scoring_method:
            if len(anomaly_score.shape)==1:
                anomaly_score = anomaly_score.reshape(-1,1)

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
                    anomaly_score[0][start_index:,],
                    anomaly_score[1][start_index:,],
                )
        return anomaly_score[
            start_index:,
        ]

    def _post_process_anomaly(self, anomaly_score, return_threshold):
        if return_threshold:
            # check dim of anomaly_score, if greater than 1, do for each dim and return
            #  only support IID? We dont know how it works
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
