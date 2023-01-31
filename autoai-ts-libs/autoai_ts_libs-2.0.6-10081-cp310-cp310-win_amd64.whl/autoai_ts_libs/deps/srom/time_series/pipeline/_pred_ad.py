import copy
import logging

import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.time_series.pipeline import Forecaster
from autoai_ts_libs.deps.srom.time_series.utils.anomaly import (
    contextual_score,
    chi_square_score,
    q_score,
    adaptive_window_score,
    window_score,
)
from autoai_ts_libs.deps.srom.pipeline.anomaly_pipeline import AnomalyPipeline

LOGGER = logging.getLogger(__name__)

class PredAD(Forecaster):
    """
    Predicaion base anomaly detector. Uses prediction from forecasting estimators to predict anomalous
    observation.

    DAG is a directed acyclic graph. It is defined with multiple options in consequitive steps which are all to be \
    executed in combinations with each other. It is meant as an explorative graph to execute all paths to find the best.

    Parameters
    ----------
        steps : list of tuples
            This is the list of tuples that define stages in forecasting pipeline. For eg.
                steps =  [('log', Log(...)),
                            ('xgboost', Xgboost(...))]
        feature_columns : numpy array
            Feature indices in the input data.
        target_columns : numpy array
            Target indices in the input data.
        lookback_win : int, optional
            Look-back window used by the forecasting model. It is used to retain history from
            train data for future (test) data. Defaults to 5.
        pred_win : int, optional
            Look-ahead window used by the forecasting model. Defaults to 1.
        time_column : int, optional
            Time column index in the input data. Defaults to -1.
        store_lookback_history : boolean, optional
            Whether to retain the lookback window from train data for future (test) data. Defaults to False.
        distance_metric : string, optional
            Metric to compute residual of forecasting model predictions. Defaults to None.
        observation_window : int, optional
            Observation window is used to compute anomaly scores by specified scoring_method. Defaults to 10.
        scoring_method : string, optional
            Anomaly scoring method to compute anomaly score in specified mathematical,
            or statistical method. The computed score is used to label anomalies by
            analyzing residuals computed. Defaults to Chi-Square.
        scoring_threshold : int, optional
            Scoring threhold is used to label computed anomaly score as anomaly or normal. Defaults to 10.


    Example use case
        Prediction Based Anomaly Detection Pipeline
        User has a time series of length 150
        He decided to train using initial 100 data point (call fit X[:100])
        Now he want to detect anomaly any where starting from point 100 onward
        he call multiple time the predict
        predict(X[100])       --> +1 if anomaly is not detected at time 100
        predict(X[100:101])   --> +1 if anomaly is not detected at time 101
        predict(X[100:102])   --> -1 if anomaly is detected at time 102


        Scoring method and Scoring threshold
        Chi-Square --> int (10)
        Q-Score --> float (0.00001)
        Window-Threhsold --> int (4)

        Different method will have different need of observation window; which is good?

    Example
    -------
    .. code-block:: python

        import pandas as pd
        from sklearn.linear_model import LinearRegression

        from autoai_ts_libs.deps.srom.time_series.pipeline import PredAD
        from autoai_ts_libs.deps.srom.preprocessing.ts_transformer import Flatten
        from autoai_ts_libs.deps.srom.utils.data_utils import load_seasonal_trend
        from autoai_ts_libs.deps.srom.time_series.utils.types import AnomalyScoringPredictionType

        df = load_seasonal_trend()
        toypipeline = PredAD(steps=[("flatten", Flatten()),
                                    ("linearregression", LinearRegression())
                                ],
                            lookback_win=6,
                            feature_columns=[0],
                            target_columns=[0],
                            pred_win=1)
        toypipeline.fit(df.values)
        anomaly_scores, _ = toypipeline.anomaly_score(
                X=None, prediction_type=AnomalyScoringPredictionType.BATCH.value, return_threshold=True,
            )
    """

    def __init__(
            self,
            steps,
            *,
            feature_columns=None,
            target_columns=None,
            lookback_win=None,
            pred_win=1,
            time_column=None,
            store_lookback_history=False,
            distance_metric="mse",
            observation_window=10,
            scoring_method="Chi-Square",
            scoring_threshold=10,
            scoring_noise_adjustment=None,
            reverse_windowing=False,
    ):
        super(PredAD, self).__init__(
            steps,
            feature_columns=feature_columns,
            target_columns=target_columns,
            lookback_win=lookback_win,
            pred_win=pred_win,
            time_column=time_column,
            store_lookback_history=store_lookback_history,
        )
        self.distance_metric = distance_metric
        self.observation_window = observation_window
        self.scoring_method = scoring_method
        self.scoring_threshold = scoring_threshold
        self.EPSILON = 1e-10
        self.scoring_noise_adjustment = scoring_noise_adjustment
        self.reverse_windowing = reverse_windowing
        """float: constant used to clip computed residuals for anomaly scores."""

    def _generate_ground_truth(self, X, target_columns, pred_win):
        """
        This is internal method to generate the ground truth of the data
        """
        new_X = X[:, target_columns].copy()
        n = new_X.shape[0]
        for i in range(0, pred_win):
            if i ==0:
                x = new_X[i: 1 + n + i - pred_win: 1]
            else:
                x =np.hstack((x,new_X[i: 1 + n + i - pred_win: 1]))
        return x

    def _compute_residuals(self, predictions, ground_truth, distance_metric='mse'):
        # groud truth does not take into the lookback so we need to adjust it now
        ground_truth = ground_truth[ground_truth.shape[0] - predictions.shape[0]:, :]

        train_squared_error_ = []
        if distance_metric == 'mse':
            if len(self.target_columns) == 1:
                # this is mse
                train_squared_error_ = (ground_truth - predictions) ** 2
                train_squared_error_[train_squared_error_ < self.EPSILON] = self.EPSILON
            else:
                # this is smape
                train_squared_error_ = np.mean(
                    2.0 * np.abs(ground_truth - predictions) / (
                                (np.abs(ground_truth) + np.abs(predictions)) + self.EPSILON),
                    axis=1,
                )
                train_squared_error_ = train_squared_error_.reshape(-1, 1)
        elif distance_metric == 'euclidean':
            train_squared_error_ = np.linalg.norm(ground_truth - predictions,axis=1)
            if (len(train_squared_error_.shape)==1):
                train_squared_error_ = train_squared_error_.reshape(-1,1)
        else:
            raise Exception("Allowed distance metrics in PredAD are ['mse']")

        return train_squared_error_

    def fit(self, X, y=None):
        """Fit the predAD model.
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Training data.
        y : Ignored
            Not used, present for API consistency by convention.
        """

        # fit the time series model
        super(PredAD, self).fit(X, y)

        # store some usefulmetric that will be used
        # passing training will store appending the lookback window
        # the predition will not be made for initial lookback window records
        ans = super(PredAD, self).predict(X, prediction_type="training")

        # reshape the model output
        if ans.ndim == 1:
            ans = ans.reshape(-1, 1)

        # this is the ground truth
        gt_ans = self._generate_ground_truth(X, self.target_columns, self.pred_win)
        #print (gt_ans, ans)

        train_squared_error_ = self._compute_residuals(ans, gt_ans, distance_metric=self.distance_metric)

        # we now have training error
        # print(len(X), len(train_squared_error_))
        if len(train_squared_error_) != len(X):
            if train_squared_error_.ndim == 2:
                dummy = np.full(
                    (
                        X.shape[0] - train_squared_error_.shape[0],
                        train_squared_error_.shape[1],
                    ),
                    np.NaN,
                )
                self.training_error_ = np.concatenate((dummy, train_squared_error_))
            else:
                dummy = np.full(X.shape[0] - train_squared_error_.shape[0], np.NaN)
                self.training_error_ = np.concatenate((dummy, train_squared_error_))
        else:
            self.training_error_ = train_squared_error_

        # making sure the error
        if self.training_error_.ndim == 1:
            self.training_error_ = self.training_error_.reshape(-1,1)

        return self


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
        
        #print (anomaly_score.shape, self.training_error_.shape)

        if anomaly_score.ndim == 1:
            anomaly_score = anomaly_score.reshape(-1,1)
        
        ad_labels = np.ones(test_len)
        
        if self.scoring_noise_adjustment is None or np.nanmax(anomaly_score) > self.scoring_noise_adjustment:
            if '_oneshot' in self.scoring_method:
                # static threshold
                ad_threshold = self._get_threshold(self.training_error_)
                for i in range(test_len):
                    if ad_threshold < anomaly_score[i]:
                        ad_labels[i] = -1
            elif '_traintestshot' in self.scoring_method:
                reference_score = np.concatenate((self.training_error_,anomaly_score))
                ad_threshold = self._get_threshold(reference_score)
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
                    if ad_threshold < np.max(anomaly_score[i]):
                        ad_labels[i] = -1
                
        if len(ad_labels.shape)==1:
            ad_labels = ad_labels.reshape(-1,1)
        return ad_labels


    def predict(self, X, prediction_type="recent"):
        """
        Predict the labels (1 inlier, -1 outlier) of X according to the
        fitted model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The data matrix.
        prediction_type : string, optional
            One of recent, stream, training, batch. training is used internally during fit. Defaults to recent.

        Returns
        -------
        score_ : ndarray of shape (n_samples,)
            Returns -1 for anomalies/outliers and +1 for inliers.

        """
        if "_label" in self.scoring_method:
            return self._predict_anomaly_label(X, prediction_type=prediction_type)

        score_, threshold_ = self.anomaly_score(
            X, return_threshold=True, prediction_type=prediction_type
        )
        if isinstance(threshold_, np.ndarray):
            threshold_ = threshold_.reshape(score_.shape)

        if self.scoring_method == "Contextual-Anomaly":
            score_[score_ > 0] = -1
            score_[score_ != -1] = 1
            return score_
        score_[score_ > threshold_] = -1
        score_[score_ != -1] = 1
        return score_

    def prediction_error(self, X, append_training_error=False):
        """
        This function is used to compute residuals(errors) for given data using the trained
        forecasting model. In addition, it can be used to compare performance of
        forecasting models.

        Parameters
        -------
        X : array-like of shape (n_samples, n_features)
            The data matrix.
        append_training_error : boolean
            Flag to append previously computed training residuals to currently
            computed test residuals.

        Returns
        -------
        all_error_ : numpy ndarray
            computed errors for provided data(X). Shape varies as per flag append_training_error.
        """
        ans = super(PredAD, self).predict(X, prediction_type="sliding")
        #print (ans)
        if ans.ndim == 1:
            ans = ans.reshape(-1, 1)
        gt_ans = self._generate_ground_truth(X, self.target_columns, self.pred_win)
        #print(gt_ans)
        gt_ans = gt_ans[gt_ans.shape[0] - ans.shape[0]:, :]

        #print (ans, gt_ans)
        test_squared_error_ = self._compute_residuals(ans, gt_ans, distance_metric=self.distance_metric)

        if test_squared_error_.ndim == 1:
            test_squared_error_ = test_squared_error_.reshape(-1,1)

        if append_training_error:
            all_error_ = np.concatenate((self.training_error_, test_squared_error_))
        else:
            all_error_ = test_squared_error_
        return all_error_

    def set_anomaly_scoring_params(
            self, observation_window, scoring_method, scoring_threshold
    ):
        """
        Method to update anomaly scoring method attributes to experiment
        different anomaly scores. This is useful to identify a suitable anomaly
        scoring metric for the selected forecasting model.

        Parameters
        -------
        observation_window : int
            Observation window is used to compute anomaly scores by specified scoring_method.
        scoring_method : string
            Anomaly scoring method to compute anomaly score in specified mathematical,
            or statistical method. The computed score is used to label anomalies by
            analyzing residuals computed.
        scoring_threshold : int
            Scoring threhold is used to label computed anomaly score as anomaly or normal.
        """
        self.observation_window = observation_window
        self.scoring_method = scoring_method
        self.scoring_threshold = scoring_threshold

    def anomaly_score(self, X, return_threshold=False, prediction_type="recent"):
        """
        This method computes anomaly scores for provided input data(X).

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Test samples.
        return_threshold : boolean, optional
            whether to return the threshold. Defaults to False
        prediction_type : string, optional
            One of recent, stream, training, batch. training is used internally during fit. Defaults to recent.

        Returns
        -------
        anomaly_score : list
            anomaly_score with threshold depending upon the parameters passed.
        """
        if prediction_type not in ["training", "batch"]:
            all_error_ = self.prediction_error(X, append_training_error=True)
        else:
            if X is not None:
                raise Exception(
                    "X is not used but passed, check the prediction_type argument"
                )
            all_error_ = copy.deepcopy(self.training_error_)

        # generate the anomaly score based on
        if self.scoring_method == "iid":
            anomaly_score = all_error_
            anomaly_threshold = all_error_
        elif self.scoring_method == "Chi-Square":
            anomaly_score, anomaly_threshold = self._chisquare_score(
                all_error_, self.observation_window
            )
        elif self.scoring_method == "Q-Score":
            anomaly_score, anomaly_threshold = self._Q_score(
                all_error_, self.observation_window
            )
        elif self.scoring_method == "Sliding-Window":
            anomaly_score, anomaly_threshold = self._window_threshold(
                all_error_, self.observation_window
            )
        elif self.scoring_method == "Adaptive-Sliding-Window":
            anomaly_score, anomaly_threshold = self._adaptive_window_threshold(
                all_error_, self.observation_window
            )
        elif self.scoring_method == "Contextual-Anomaly":
            anomaly_result = self._contextual_anomaly(
                all_error_, self.observation_window
            )
            score = pd.DataFrame(anomaly_result)
            output = pd.DataFrame(
                0, index=range(len(all_error_)), columns=["Score"], dtype="float"
            )
            for row in score.itertuples(index=False):
                output.loc[row[0]: row[1], "Score"] = row[2]
            anomaly_score, anomaly_threshold = output.to_numpy(), np.zeros(output.shape)
        else:
            anomaly_score = all_error_
        # squared error must be of same lenght as X
        start_index = 0
        if prediction_type == "recent":
            start_index = -1
        elif prediction_type == "sliding":
            start_index = -X.shape[0]
        else:
            pass
        if return_threshold:
            return (
                anomaly_score[start_index:, ],
                anomaly_threshold[start_index:, ],
            )
        return anomaly_score[
               start_index:,
               ]

    def _chisquare_score(self, train_test_errors, observation_window):
        """
        This method provide the most recent c_score we we can make decision
        We shd externamize this
        We can externalize these method now
        """
        return chi_square_score(
            train_test_errors, observation_window, self.scoring_threshold
        )

    def _Q_score(self, train_test_errors, observation_window):
        return q_score(train_test_errors, observation_window, self.scoring_threshold)

    def _adaptive_window_threshold(self, train_test_errors, observation_window):
        return adaptive_window_score(
            train_test_errors, observation_window, self.scoring_threshold
        )

    def _window_threshold(self, train_test_errors, observation_window):
        return window_score(
            train_test_errors, observation_window, self.scoring_threshold
        )

    def _contextual_anomaly(self, train_test_errors, observation_window=None):
        # this is a place where venky shd put his code
        # output is
        # anomaly_start, anomaly_end, score
        return contextual_score(train_test_errors, observation_window)
