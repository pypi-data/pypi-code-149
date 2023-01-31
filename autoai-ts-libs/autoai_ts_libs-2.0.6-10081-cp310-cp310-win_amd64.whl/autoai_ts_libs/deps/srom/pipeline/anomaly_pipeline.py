# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: anomaly_pipeline
   :synopsis: Anomaly Pipeline Functionality.

.. moduleauthor:: SROM Team
"""
import logging
import multiprocessing
import warnings
import numpy as np
import pandas as pd
import math
from scipy import stats
from scipy.special import erfcinv
from scipy.stats import median_abs_deviation

from sklearn.model_selection import PredefinedSplit
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.anomaly_detection.anomaly_score_evaluation import AnomalyScoreEvaluator
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.utils.pipeline_utils import check_custom_stage_random_state

from autoai_ts_libs.deps.srom.anomaly_detection.unsupervised_anomaly_score_evaluation import (
    unsupervised_anomaly_cross_val_score,
)

LOGGER = logging.getLogger(__name__)


def custom_loss_func(ground_truth, predictions):
    """
    Create new evaluator.
    Creates a scorer from anomaly evaluator object.
    """
    ase = AnomalyScoreEvaluator("average", "anomaly_f1", 5, 0.5)
    return ase.score(predictions, ground_truth)


class AnomalyPipeline(SROMPipeline):
    """
    AnomalyPipeline Class.
    contamination : float in (0., 0.5), optional (default=-1)
    anomaly_threshold_method: string : "default", "contamination", "adaptivecontamination", "qfunction",
                                        "std", "medianabsolutedev", "robustqfunction", "otsu"
    std_threshold : float : used when anomaly_threshold_method = default or std
    contamination : float : used when anomaly_threshold_method = contamination
    qfunction_threshold : float : used when anomaly_threshold_method = qfunction
    medianabsolutedev_threshold : float : used when anomaly_threshold_method = medianabsolutedev
    """

    # init method
    def __init__(
        self,
        anomaly_threshold_method="default",
        std_threshold=2.0,
        contamination=0.05,
        qfunction_threshold=0.95,
        medianabsolutedev_threshold=2.5,
        adaptivecontamination_threshold=0.05,

    ):
        # as time progress, many similar looking threshold will disappear and will be consolidated into single
        super(AnomalyPipeline, self).__init__()
        self.cv = None
        self.__anomaly_scorer_obj = None
        self.__best_thresholds = None
        self.contamination = contamination
        self.anomaly_threshold_method = anomaly_threshold_method
        self.std_threshold = std_threshold
        self.qfunction_threshold = qfunction_threshold
        self.medianabsolutedev_threshold = medianabsolutedev_threshold
        self.adaptivecontamination_threshold = adaptivecontamination_threshold

    def set_best_thresholds(self, best_thresholds):
        """
        set_best_thresholds function is used to set the value for best thresholds. \
        best_thresholds can be None or ndarray of int/float.

        Parameters:
            best_thresholds (ndarray or None): numpy array of thresholds.

        Raises:
            TypeError: If best_thresholds is other than None or numpy.ndarray \
                of int/float.
        """
        if best_thresholds is None or (
            isinstance(best_thresholds, np.ndarray)
            and best_thresholds.size > 0
            and all(isinstance(x, (int, float)) for x in best_thresholds.tolist())
        ):
            self.__best_thresholds = best_thresholds
        else:
            raise TypeError(
                "best_threshold should be None or numpy.ndarray of int/float"
            )

    def get_best_thresholds(self):
        """
        get_best_thresholds returns best thresholds of anomaly pipeline.

        Returns:
            None if no threshold is set else numpy.ndarray of thresholds.
        """
        return self.__best_thresholds

    # since overwrite the scoring method to provide a callable function
    def set_scoring(
        self,
        scoring=None,
        scoring_method="average",
        scoring_metric="anomaly_f1",
        scoring_topk_param=5,
        score_validation=0.5,
    ):
        """
        set_scoring is used to set the scoring to evaluate the model.

        Parameters:
            scoring (string, callable, list/tuple, dict or None): Default is None. \
                A single string or a callable to evaluate the predictions on the test set.
            scoring_method (String): Default is 'average'. Possible values: 'average' or 'topk'.
            scoring_metric (String): Default is 'anomaly_f1'. Possible values: 'roc_auc', \
                'anomaly_f1', 'anomaly_acc', 'pr_auc'.
            scoring_topk_param (integer): Default is 5. Positive, > 0 applicable when \
                scoring_method is 'top-k'.
            score_validation (integer): Default is 0.5. Possible values between 0 and 1.
        """
        if scoring:
            self.__anomaly_scorer_obj = None
            super(AnomalyPipeline, self).set_scoring(scoring)
        else:
            # an internal object for scoring
            self.__anomaly_scorer_obj = AnomalyScoreEvaluator(
                scoring_method, scoring_metric, scoring_topk_param, score_validation
            )

            # pass the new scorer objects
            from sklearn.metrics import make_scorer

            # scorer for cross validation
            anomaly_scorer = make_scorer(custom_loss_func, greater_is_better=True)
            super(AnomalyPipeline, self).set_scoring(anomaly_scorer)

    def _train_unsupervised_model(
        self,
        trainX,
        exectype,
        n_jobs,
        pre_dispatch,
        verbosity,
        param_grid,
        max_eval_time_minute,
        num_option_per_pipeline,
        random_state,
        total_execution_time=10,
    ):
        """
        helper method for training unsupervised model
        """
        if exectype in ["spark_node_random_search", "spark_node_complete_search"]:
            if self.scoring is None:
                self.set_scoring("em_score")
            self.set_cross_val_score(unsupervised_anomaly_cross_val_score)
            self.best_estimator, self.best_score = super(AnomalyPipeline, self).execute(
                X=trainX,
                exectype=exectype,
                n_jobs=n_jobs,
                pre_dispatch=pre_dispatch,
                verbosity=verbosity,
                param_grid=param_grid,
                max_eval_time_minute=max_eval_time_minute,
                num_option_per_pipeline=num_option_per_pipeline,
                random_state=random_state,
                total_execution_time=total_execution_time,
            )
        else:
            raise Exception(
                "training of unsupervised model is not supported for " + exectype
            )

        # the following function will train the model and generate the anomaly score
        self._generate_anomaly_threshold_for_unsupervised_modeling(trainX)

    def _generate_anomaly_threshold_for_unsupervised_modeling(self, trainX):

        # discover best threshold by calling generate_stats
        # there is a possibility that the following tmp_gen_threshold may not
        # guarrentee that it will generate any anomaly label
        # this depends on how your training data is distrubuted
        if self.anomaly_threshold_method == "contamination":
            if 0.0 < self.contamination <= 0.5:
                decision_scores_ = self._train_and_score(trainX)
                tmp_gen_threshold = [
                    np.percentile(decision_scores_, 100 * (1 - self.contamination))
                ]
            else:
                raise Exception(
                    "The value of contamination should be between 0. to 0.5, excluding 0"
                )
        elif self.anomaly_threshold_method == "adaptivecontamination":
            if 0.0 < self.adaptivecontamination_threshold <= 0.5:
                decision_scores_ = self._train_and_score(trainX)
                tmp_gen_threshold = [
                    np.float_(self._get_anomaly_threshold_based_on_grubbs(
                        decision_scores_,
                        0.05,
                        int(len(decision_scores_) * self.adaptivecontamination_threshold),
                    ))
                ]
            else:
                raise Exception(
                    "The value of contamination should be between 0. to 0.5, excluding 0"
                )
        elif self.anomaly_threshold_method == "qfunction":
            tmp_mean_x, tmp_std_x = self.generate_base_anomaly_score_statistics(
                trainX, robust=False
            )
            self.train_mean = tmp_mean_x
            self.train_std = tmp_std_x

            if self.qfunction_threshold > 0:
                from scipy.special import erfcinv

                tmp_gen_threshold = [
                    m + ((erfcinv(2.0 * self.qfunction_threshold) * math.sqrt(2)) * s)
                    for m, s in zip(self.train_mean, self.train_std)
                ]
        elif self.anomaly_threshold_method == "medianabsolutedev":
            tmp_median_x, tmp_mad_x = self.generate_base_anomaly_score_statistics(
                trainX, robust=True
            )
            self.train_median = tmp_median_x
            self.train_mad = tmp_mad_x
            tmp_gen_threshold = [self.medianabsolutedev_threshold]
            if self.medianabsolutedev_threshold > 0:
                tmp_gen_threshold = [
                    m + ((self.medianabsolutedev_threshold * (s)) / 0.6745)
                    for m, s in zip(self.train_median, self.train_mad)
                ]
        elif self.anomaly_threshold_method == "otsu":
            decision_scores_ = self._train_and_score(trainX)
            tmp_gen_threshold = [self._otsu_threshold(decision_scores_)]
        elif (
            self.anomaly_threshold_method == "default"
            or self.anomaly_threshold_method == "std"
        ):
            if self.std_threshold > 0:
                tmp_mean_x, tmp_std_x = self.generate_base_anomaly_score_statistics(
                    trainX
                )
                self.train_mean = tmp_mean_x
                self.train_std = tmp_std_x
                tmp_gen_threshold = [
                    m + self.std_threshold * (s) for m, s in zip(tmp_mean_x, tmp_std_x)
                ]
            else:
                raise Exception(
                    "The value of contamination should be between 0. to 0.5, excluding 0"
                )
        else:
            raise Exception("Wrong anomaly_threshold_method option")

        # use contamination based technique to make sure some samples in the
        # given dataset is tagged as an anomaly

        # once it is discovered, call set_best_thresholds
        tmp_gen_threshold = np.array(tmp_gen_threshold)
        self.set_best_thresholds(tmp_gen_threshold)

    def _check_validation_label(self, validy):
        """
        This function to ensure that user pass 0 and 1 value in validy
        """
        unique_val = np.unique(validy)
        if len(unique_val) != 2:
            raise Exception(
                "validy must have some samples from positive and negative classes"
            )
        if 0 not in unique_val or 1 not in unique_val:
            raise Exception("validy must have 0 and 1 class labels")

    def execute(
        self,
        trainX,
        validX,
        validy,
        exectype="single_node_complete_search",
        n_jobs=multiprocessing.cpu_count(),
        pre_dispatch="2*n_jobs",
        verbosity="low",
        param_grid=None,
        max_eval_time_minute=5,
        num_option_per_pipeline=10,
        random_state=None,
        total_execution_time=10,
    ):
        """
        Parameter:
            trainX (pandas dataframe or numpy array): The dataset to be used for model selection. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.
            validX (pandas dataframe or numpy array): The pre-failure dataset to be used for \
                prediction of model accuracy.
            validy (pandas dataframe or numpy array): Label for pre-failure data. Can be pandas \
                dataframe or numpy array.
            exectype (String): Default value is "single_node_complete_search". \
                "spark": Executes the pipeline on a Spark cluster. \
                "single_node" or "single_node_complete_search": Executes the pipeline \
                    for all parameter samples on single node. \
                "single_node_random_search": Executes the pipeline for random parameter \
                    samples on single node. \
                "spark_node_random_search": Executes the pipeline for random parameter \
                    samples on spark. \
                "spark_node_complete_search": Executes the pipeline for all parameter \
                    samples on spark. \
            n_jobs (integer, optional): Default value is multiprocessing.cpu_count(). \
                Number of parallel jobs. Only required for \
                "single_node_random_search"/"single_node_complete_search".
            pre_dispatch (:integer:string, optional): Default value is "2*n_jobs". \
                Controls the number of jobs that get dispatched during parallel execution. \
                Reducing this number can be useful to avoid an explosion of memory consumption \
                when more jobs get dispatched than CPUs can process.
            verbosity (String, optional): Default value is "low". Possible values: "low", \
                "medium", "high".
            param_grid (dict): Default is {}. Dictionary with parameter names(string) as keys and \
                lists of parameter settings to try as values, or a list of such dictionaries, in \
                which case the grids spanned by each dictionary in the list are explored.
            num_option_per_pipeline (integer): Default is 10. Number of parameter settings that are \
                sampled. This parameter is applicable for "spark_node_random_search" and \
                "single_node_random_search" exectype.
            max_eval_time_minute (integer): In minutes. Default is 5. Maximum timeout for execution \
                of pipelines with unique parameter grid combination. This parameter is applicable for \
                "spark_node_random_search" and "spark_node_complete_search" exectype.
            random_state (int or None) = None,
            total_execution_time (integer, minute) = 10

        Returns:
            Anomaly pipeline instance.
        """

        # check what type of anomaly model user is training
        # start with isolating code
        # this is to raise a warning that user will see different results
        check_custom_stage_random_state(self.stages)

        if random_state is None:
            warnings.warn(
                "random_state argument not set, setting it to 42.", category=UserWarning
            )
            random_state = 42

        if validX is None and validy is None:
            LOGGER.info("Running Unsupervised Anomaly Model")
            self.execution_model = "un-supervised"
            self._train_unsupervised_model(
                trainX,
                exectype,
                n_jobs,
                pre_dispatch,
                verbosity,
                param_grid,
                max_eval_time_minute,
                total_execution_time,
                num_option_per_pipeline,
                random_state,
            )
            return self
        else:
            # Reset variable
            LOGGER.info("Running semi-supervised Anomaly Model")
            self.execution_model = "semi-supervised"
            self.set_best_thresholds(None)
            self._check_validation_label(validy)

            # initialize the default scoring - for anomaly scorer
            if self.scoring is None:
                self.set_scoring()

            # if user has not provided any CV, which is always the case for anomaly class of problem
            if self.cv is None:
                anomaly_lbl = self._get_anomaly_db_label(
                    trainX.shape[0], validX.shape[0]
                )
                self._set_train_validation_cv(anomaly_lbl)
            anomaly_db = self._get_anomaly_db(trainX, validX, validy, self.label_column)

            # we prepared our cross validator, dataset and now call it
            self.best_estimator, self.best_score = super(AnomalyPipeline, self).execute(
                X=anomaly_db,
                exectype=exectype,
                n_jobs=n_jobs,
                pre_dispatch=pre_dispatch,
                verbosity=verbosity,
                param_grid=param_grid,
                max_eval_time_minute=max_eval_time_minute,
                num_option_per_pipeline=num_option_per_pipeline,
                random_state=random_state,
            )

            # retrain the best estimators on training data only, as fixed for anomaly
            if self.best_estimator:
                self.best_estimator.fit(trainX)
                if self.__anomaly_scorer_obj:
                    self.score(validX, validy)
                    self.set_best_thresholds(
                        self.__anomaly_scorer_obj.get_best_thresholds()
                    )
                else:
                    LOGGER.warning(
                        "Please set threshold using set_best_thresholds() before"
                        " calling predict()."
                    )

            return self

    def _get_anomaly_db(self, X_train, X_test, y_test, class_label):
        """
        Get the anomaly db.
        """
        # no of class in label column
        no_of_class = len(np.unique(y_test))
        if no_of_class < 2:
            # raise error if number of class is less than 2
            raise ValueError(
                "The number of classes has to be greater than one; got %d"
                " class" % no_of_class
            )
        train_db = pd.concat([X_train, X_test], axis=0)
        if class_label is not None and class_label in train_db.columns:
            del train_db[class_label]
            train_db[class_label] = list(np.zeros(X_train.shape[0])) + list(y_test)
        else:
            train_db["srom_anomaly_label"] = list(np.zeros(X_train.shape[0])) + list(
                y_test
            )
            self.label_column = "srom_anomaly_label"
        return train_db

    @staticmethod
    def _get_anomaly_db_label(X_train_row_count, X_test_row_count):
        """
        Get the anomaly db label.

        Parameters:
            X_train_row_count (integer): Number of samples in train data.
            X_test_row_count (integer): Number of samples in test data.
        """
        tmp_lbl = list(np.zeros(X_train_row_count) - 1)
        tmp_lbl.extend(np.ones(X_test_row_count))
        return tmp_lbl

    # train validation cv - internal method
    def _set_train_validation_cv(self, tmp_lbl):
        anomaly_cv = PredefinedSplit(tmp_lbl)
        external_cv = list(anomaly_cv.split())
        super(AnomalyPipeline, self).set_cross_validation(external_cv)

    def predict(self, X, **kwargs):
        """
        Predict the class labels. 0 = normal, 1 = anomaly.

        Parameters:
            X (pandas dataframe or numpy array): Input samples to be \
                used for prediction.
            kwargs (dict): Dictionary of optional parameters.

        Returns:
            Predicted scores in an array of shape = [n_samples] or [n_samples, n_outputs].

        Raises:
            Exception:
                1. If best_estimator is none.
                2. If best_thresholds is none.
        """
        if self.best_estimator is None:
            raise Exception("Train the model first by calling execute/fit method.")
        best_thresholds = self.get_best_thresholds()
        anomaly_score = self.best_estimator.predict(X)

        if best_thresholds is not None:
            is_an_anomaly = anomaly_score > best_thresholds
            is_not_an_anomaly = anomaly_score <= best_thresholds
            anomaly_score[is_an_anomaly] = -1
            anomaly_score[is_not_an_anomaly] = 1
        else:
            raise Exception("No thresholds set.")
        try:
            anomaly_score = anomaly_score.astype(int, errors="ignore")
        except Exception as ex:
            if isinstance(anomaly_score, np.ndarray):
                anomaly_score = pd.DataFrame(anomaly_score).astype(int, errors="ignore")
            else:
                LOGGER.exception(ex)
                raise ex
        return anomaly_score.values

    def predict_proba(self, X):
        """
        Parameters:
            X (pandas dataframe or numpy array): Test samples.

        Returns:
            Returns anomaly scores.

        Raises:
            Exception:
                If best_estimator is None.
        """
        if self.best_estimator is None:
            raise Exception("Train the model first by calling execute/fit method.")
        return self.best_estimator.predict(X)

    # score method
    def score(self, X, y):
        """
        Parameters:
            X (pandas dataframe or numpy array): Test samples.
            y (pandas dataframe or numpy array): Ground truth values.

        Returns:
            Performance metric value.
        """
        if self.best_estimator and self.__anomaly_scorer_obj:
            ret_val = self.__anomaly_scorer_obj.score(self.best_estimator.predict(X), y)
            return ret_val
        if self.execution_model == "un-supervised":
            if self.best_estimator and self.scoring:
                from sklearn.metrics import SCORERS as sklearn_score_mapping

                if self.scoring in sklearn_score_mapping:
                    pred_val = self.predict(X)
                    return sklearn_score_mapping[self.scoring]._score_func(
                        y, pred_val, **sklearn_score_mapping[self.scoring]._kwargs
                    )
                else:
                    raise Exception(
                        "scoring should be string : https://scikit-learn.org/stable/modules/model_evaluation.html"
                    )
            else:
                raise Exception(
                    "Either best_estimator is not set or scoring is not set"
                )

        return super(AnomalyPipeline, self).score(X, y)

    def __str__(self):
        return (
            self.__class__.__name__
            + "(Pipeline Id="
            + str(self.pipeline_id)
            + ", Stages="
            + str(self.stages)
            + ", Id Column="
            + str(self.id_column)
            + ", Time Column="
            + str(self.time_column)
            + ", Label Column="
            + str(self.label_column)
            + ", Label Prefix="
            + str(self.label_prefix)
            + ", Cross Validation="
            + str(self.cv)
            + ", Scoring="
            + str(self.scoring)
            + ", Best Estimator="
            + str(self.best_estimator)
            + ", Best Score="
            + str(self.best_score)
            + ", Best Thresholds="
            + str(self.__best_thresholds)
            + ")"
        )

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def _train_and_score(self, trainX):
        if not self.best_estimator:
            raise Exception("best_estimator not found. Please execute the pipeline.")

        # train the model
        self.best_estimator.fit(trainX)
        # generate score
        tmp_anomaly_score = self.best_estimator.predict(trainX)
        return tmp_anomaly_score

    def generate_base_anomaly_score_statistics(self, trainX, robust=False):
        """
        Generate mean and standard deviation of anomaly score.

        Parameters:
            trainX (pandas dataframe): The dataset to be used for model selection. \
                shape = [n_samples, n_features] \
                where n_samples is the number of samples and n_features is the number of features.

        Returns (Tuple):
            Return two lists, first list is of mean anomaly score and second list of \
            standard deviation of anomaly score.
        """
        tmp_anomaly_score = self._train_and_score(trainX)
        # check is tmp_anomaly_score does not generate a class label, else
        # the user has configured the pipeline in wrong way
        if len(tmp_anomaly_score.shape) == 1:
            tmp_anomaly_score = tmp_anomaly_score.reshape(-1, 1)
            if len(np.unique(tmp_anomaly_score) <= 2):
                raise Exception("Seems like anomaly score is label not a real value")

        if len(tmp_anomaly_score) < 6:
            raise Exception(
                "Cannot Generate Statistics for single record, requiered atleast 6 records"
            )

        if robust:
            anomaly_median = np.median(tmp_anomaly_score, axis=0)
            diff = np.sum((tmp_anomaly_score - anomaly_median) ** 2, axis=-1)
            med_abs_deviation = np.array([np.median(diff)])
            return anomaly_median.tolist(), med_abs_deviation.tolist()
        else:
            anomaly_mean = np.nanmean(tmp_anomaly_score, 0)
            anomaly_std = np.nanstd(tmp_anomaly_score, 0)
            return anomaly_mean.tolist(), anomaly_std.tolist()

    def _grubbs_stat(self, y):
        std_dev = np.std(y)
        avg_y = np.mean(y)
        abs_val_minus_avg = abs(y - avg_y)
        max_of_deviations = max(abs_val_minus_avg)
        max_ind = np.argmax(abs_val_minus_avg)
        Gcal = max_of_deviations / std_dev
        return Gcal, max_ind

    def _calculate_critical_value(self, size, alpha):
        t_dist = stats.t.ppf(1 - alpha / (2 * size), size - 2)
        numerator = (size - 1) * np.sqrt(np.square(t_dist))
        denominator = np.sqrt(size) * np.sqrt(size - 2 + np.square(t_dist))
        critical_value = numerator / denominator
        return critical_value

    def _check_G_values(self, Gs, Gc):
        if Gs > Gc:
            return True
        return False

    def _get_anomaly_threshold_based_on_grubbs(self, input_series, alpha, max_outliers):
        for _ in range(max_outliers):
            Gcritical = self._calculate_critical_value(len(input_series), alpha)
            Gstat, max_index = self._grubbs_stat(input_series)
            if self._check_G_values(Gstat, Gcritical):
                input_series = np.delete(input_series, max_index)
            else:
                break
        return max(input_series.flatten())

    def _otsu_threshold(self, x, is_normalized=False, bins_num=256):
        rng = np.random.RandomState(10)
        counts, bin_centers = np.histogram(x, bins=bins_num)
        bin_mids = (bin_centers[:-1] + bin_centers[1:]) / 2.0
        if is_normalized:
            hist = np.divide(counts.ravel(), counts.max())
        weight1 = np.cumsum(counts)
        weight2 = np.cumsum(counts[::-1])[::-1]
        mean1 = np.cumsum(counts * bin_mids) / weight1
        mean2 = (np.cumsum((counts * bin_mids)[::-1]) / weight2[::-1])[::-1]
        variance12 = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2
        idx = np.argmax(variance12)
        threshold = bin_mids[:-1][idx]
        return threshold

    def _max_threshold(self, x, factor=1.1):
        return np.nanmax(x)*factor

    def _contamination_threshold(self, x, confidence_percentile=0.05):
        return np.nanpercentile(x, (1-confidence_percentile)*100)
    
    def _adaptive_contamination_threshold(self, x, confidence_score=0.05):
        x = x[~np.isnan(x)]
        a_threshold = self._get_anomaly_threshold_based_on_grubbs(
                    x, 0.05, int(len(x) * confidence_score)
                )
        return a_threshold
    
    def _qfunction_threshold(self, x, confidence_score=0.01):
        x = x[~np.isnan(x)]
        tmp_mean_x = np.nanmean(x)
        tmp_std_x = np.nanstd(x)
        a_threshold = tmp_mean_x + ((erfcinv(2.0 * confidence_score) * math.sqrt(2)) * tmp_std_x)
        return a_threshold
    
    def _medianabsolutedev_threshold(self, x, threshold=2.5):
        x = x[~np.isnan(x)]
        tmp_median_x = np.median(x)
        tmp_mad_x = median_abs_deviation(x)
        a_threshold = tmp_median_x + ((threshold * (tmp_mad_x)) / 0.6745)
        return a_threshold
    
    def _std_threshold(self, x, threshold=1.0):
        x = x[~np.isnan(x)]
        a_threshold = np.mean(x) + threshold * np.std(x)
        return a_threshold
