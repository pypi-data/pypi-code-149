from sklearn.model_selection import KFold
from sklearn.utils.validation import _num_samples
import numpy as np

class TrainKFold(KFold):
    """TrainK-Folds validator
    Provides same train/test indices to split data in train/test sets. Split
    dataset into k consecutive folds (without shuffling by default).
    Each fold is then used for training and testing.
    Parameters
    ----------
    n_splits : int, default=5
        Number of folds. Must be at least 2.
        .. versionchanged:: 0.22
            ``n_splits`` default value changed from 3 to 5.
    shuffle : bool, default=False
        Whether to shuffle the data before splitting into batches.
        Note that the samples within each split will not be shuffled.
    random_state : int, RandomState instance or None, default=None
        When `shuffle` is True, `random_state` affects the ordering of the
        indices, which controls the randomness of each fold. Otherwise, this
        parameter has no effect.
        Pass an int for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.
    Examples
    --------
    >>> import numpy as np
    >>> from autoai_ts_libs.deps.srom.model_selection import TrainKFold
    >>> X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
    >>> y = np.array([1, 2, 3, 4])
    >>> kf = KFold(n_splits=2)
    >>> kf.get_n_splits(X)
    2
    >>> print(kf)
    TrainKFold(n_splits=2, random_state=None, shuffle=False)
    >>> for train_index, test_index in kf.split(X):
    ...     print("TRAIN:", train_index, "TEST:", test_index)
    ...     X_train, X_test = X[train_index], X[test_index]
    ...     y_train, y_test = y[train_index], y[test_index]
    TRAIN: [2 3] TEST: [2 3]
    TRAIN: [0 1] TEST: [0 1]
    Notes
    -----
    The first ``n_samples % n_splits`` folds have size
    ``n_samples // n_splits + 1``, other folds have size
    ``n_samples // n_splits``, where ``n_samples`` is the number of samples.
    Randomized CV splitters may return different results for each call of
    split. You can make the results identical by setting `random_state`
    to an integer.
    """
    
    def __init__(self, n_splits, *, shuffle=False, random_state=None):
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state

    def split(self, X, y=None, groups=None):
        """_summary_

        Args:
            X (_type_): _description_
            y (_type_, optional): _description_. Defaults to None.
            groups (_type_, optional): _description_. Defaults to None.

        Yields:
            _type_: _description_
        """
        
        if self.n_splits == 1:
            n_samples = _num_samples(X)
            indices = np.arange(n_samples)
            yield indices, indices
        else:
            for train_index, _ in super(TrainKFold, self).split(X, y, groups):
                yield train_index, train_index
                
                
# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: time_series_splits
   :synopsis: Contains classes for splitting data.

.. moduleauthor:: SROM Team
"""
import logging
import numpy as np
import pandas as pd
import random
from sklearn.model_selection._split import _BaseKFold
from sklearn.utils import indexable
from sklearn.utils.validation import _num_samples

LOGGER = logging.getLogger(__name__)


class TimeSeriesADSplit(_BaseKFold):
    """
    Time Series cross-validator for anomaly detection.

    Provides train/test indices to split time series data samples that \
    are observed at fixed time intervals, in train/test sets. In each split, \
    test indices must be higher than before, and thus shuffling in cross \
    validator is inappropriate. It treats the samples as normal behavior until \
    it hits a label corresponding to anomaly.
    Note that this can be applied only in cases where there is only 1 anomalous \
    label per row. So the K folds will have training data sampled from the normal \
    behavior and test data from anomalous. \
    In the kth split, it returns first k folds as train set and the (k+1)th fold as test set. \
    Note that unlike standard cross-validation methods, successive training sets are \
    supersets of those that come before them. Read more in the :ref:`User Guide <cross_validation>`.
    
    Parameters:
        n_splits (int, default=3): Number of splits. Must be at least 1.
    """

    def __init__(self, n_splits=3):
        super(TimeSeriesADSplit, self).__init__(
            n_splits, shuffle=False, random_state=None
        )

    def split(self, X, y, groups=None, prefailure_window=0):
        """
        Generate indices to split data into training and test set.

        Parameters:
            X (array-like, shape (n_samples, n_features)): Training data, \
                n_samples is the number of samples and n_features is the \
                number of features.
            y (array-like, shape (n_samples,)): n_samples is the number of samples.
            groups (array-like, with shape (n_samples,), optional): Always ignored, \
                exists for compatibility.
        Returns:
            train (ndarray): The training set indices for that split.
            test (ndarray): The testing set indices for that split.
        """
        result = indexable(X, y, groups)
        X, y, groups = result[0], result[1], result[2]
        n_samples = _num_samples(X)
        n_splits = self.n_splits
        n_folds = n_splits
        if n_folds > n_samples:
            raise ValueError(
                (
                    "Cannot have number of folds ={0} greater"
                    " than the number of samples: {1}."
                ).format(n_folds, n_samples)
            )
        indices = np.arange(n_samples)
        dummy_train_start, test_start = ADTrainTestSplit.ad_train_test_split(
            X, y, prefailure_window=prefailure_window
        )
        # the dataset has normal behavior data till the start of the test data
        train_size = test_start // n_folds
        train_starts = list(range(0, test_start, train_size))
        test_size = (n_samples - test_start) // n_folds
        test_starts = list(
            range(test_start + (n_samples - test_start) % n_folds, n_samples, test_size)
        )
        for i, dummy_item in enumerate(test_starts):
            yield (
                indices[train_starts[i] : train_starts[i] + train_size],
                indices[test_starts[i] : test_starts[i] + test_size],
            )


class ADTrainTestSplit(object):
    """
    Some algorithms for anomaly detection need the training data \
    to be only corresponding to normal behavior and test data \
    can be a combination of normal and anomalous.
    """

    def __init__(self):
        pass

    @classmethod
    def ad_train_test_split(cls, X, y, prefailure_window=0):
        """
        Parameters:
            X (pandas dataframe): Contains dataset of features.
            y (pandas series): Contains labels indicating anomaly.
            prefailure_window: This parameters indicates the amount 
                of time steps to include in test data before the \
                first failure.

        Returns: 
            <description>
        """
        y = y.astype(int)
        if isinstance(y, pd.Series):
            y = y.values
        first_anomalous_index = next(i for i in range(len(y)) if y[i] == 1)
        # go back prefailure_window number of time steps to get the first sample for test data
        first_test_index = first_anomalous_index - prefailure_window
        if first_test_index >= 0:
            return 0, first_test_index
        else:
            raise BaseException(
                "prefailure window is set to a value higher than \
            number of prefailure samples in the data"
            )


# added new stuff, let us quickly add the test cases around this


class TimeSeriesSlidingSplit(_BaseKFold):
    """
    This class is for sliding window based time series cross validation. \
    Size of training(training_len) and testing window(test_len) is given. \
    Training window for Fold 1 start at observation zero. \
    Training window for Fold 2 start at zero + training_len, and so one. \
    time_gap is used to skip the number of observations in between training \
    and test window.
    """

    def __init__(self, training_len=10, test_len=4, time_gap=0, n_splits=-1):
        self.n_splits = n_splits
        self.training_len = training_len
        self.test_len = test_len
        self.time_gap = time_gap

        if training_len < test_len:
            raise ValueError(
                "Cannot have length of training window={0} greater than the testing window: {1}.".format(
                    self.training_len, self.test_len
                )
            )

    def split(self, X, y=None, groups=None):
        indexable_results = indexable(X, y, groups)
        X, y, groups = indexable_results[0], indexable_results[1], indexable_results[2]
        n_samples = _num_samples(X)

        if (self.training_len + self.test_len + self.time_gap) > n_samples:
            raise ValueError(
                "Cannot have (training_len + test_len + time_gap)={0} greater than the number of samples: {1}.".format(
                    self.training_len + self.test_len + self.time_gap, n_samples
                )
            )

        indices = np.arange(n_samples)
        test_size = self.test_len
        test_starts = range(self.training_len, n_samples - self.time_gap, test_size)

        for test_start in test_starts:
            yield (
                indices[test_start - self.training_len : test_start],
                indices[
                    test_start + self.time_gap : test_start + test_size + self.time_gap
                ],
            )


class TimeSeriesKFoldSlidingSplit(_BaseKFold):
    """
    This class is for sliding window based time series cross \
    validation. It uses the idea presented in scikit learn based \
    TimeSeriesSpilt. The size of training window for scikit learn's \
    KFold for time series increase from one fold to another. \
    The modified method use sliding window to maintain the length of \
    training window equal for all folds.
    """

    def __init__(self, n_splits=3):
        self.n_splits = n_splits

    def split(self, X, y=None, groups=None):
        indexable_results = indexable(X, y, groups)
        X, y, groups = indexable_results[0], indexable_results[1], indexable_results[2]
        n_samples = _num_samples(X)
        n_splits = self.n_splits
        n_folds = n_splits + 1

        if n_folds > n_samples:
            raise ValueError(
                "Cannot have number of folds ={0} greater than the number of samples: {1}.".format(
                    n_folds, n_samples
                )
            )

        indices = np.arange(n_samples)
        test_size = n_samples // n_folds
        test_starts = range(test_size + n_samples % n_folds, n_samples, test_size)
        start_index = -test_size

        for test_start in test_starts:
            start_index = start_index + test_size
            yield (
                indices[start_index:test_start],
                indices[test_start : test_start + test_size],
            )


class TimeSeriesTrainTestSplit(_BaseKFold):
    """
    This class is for splitting time series into two part - \
    training and testing. \
    n_test_size is the number of datapoints selected from \
    the end of time series as the test data point.
    """

    def __init__(self, n_test_size=10):
        self.n_splits = 1
        self.n_test_size = n_test_size

    def split(self, X, y=None, groups=None):
        indexable_results = indexable(X, y, groups)
        X, y, groups = indexable_results[0], indexable_results[1], indexable_results[2]
        n_samples = _num_samples(X)

        if self.n_test_size > n_samples:
            raise ValueError(
                "Cannot have size of test data = {0} greater than the number of samples: {1}.".format(
                    self.n_test_size, n_samples
                )
            )

        if n_samples - self.n_test_size < self.n_test_size:
            LOGGER.warning("method should use more training data than testing data")

        indices = np.arange(n_samples)
        test_starts = [n_samples - self.n_test_size]

        for test_start in test_starts:
            yield (indices[0:test_start], indices[test_start:n_samples])


class TimeSeriesPredictionSplit(_BaseKFold):
    """
    This class is for time series prediction cross validation \
    number of prediction to be make(n_prediction) and number \
    of steps ahead prediction(prediction_step) is given.
    """

    def __init__(self, n_splits=4, prediction_step=5):
        self.n_splits = n_splits
        self.n_prediction = n_splits
        self.prediction_step = prediction_step

    def split(self, X, y=None, groups=None):
        indexable_results = indexable(X, y, groups)
        X, y, groups = indexable_results[0], indexable_results[1], indexable_results[2]
        n_samples = _num_samples(X)

        if self.n_prediction > n_samples:
            raise ValueError(
                "Cannot have (n_prediction)={0} greater than the number of samples: {1}.".format(
                    self.n_prediction, n_samples
                )
            )

        indices = np.arange(n_samples)
        test_starts = range(
            n_samples - self.n_prediction - self.prediction_step + 1,
            n_samples - self.prediction_step + 1,
            1,
        )

        for test_start in test_starts:
            yield (
                indices[0:test_start],
                indices[test_start : test_start + self.prediction_step],
            )


class TimeSeriesTumblingWindowSplit(_BaseKFold):
    """
    This class is for time series Rolling cross validation \
    number of rolling to be make(n_splits) and size of rolling \
    (split_size) is given.
    """

    def __init__(self, n_splits=4, split_size=5):
        self.n_splits = n_splits
        self.split_size = split_size

    def split(self, X, y=None, groups=None):
        indexable_results = indexable(X, y, groups)
        X, y, groups = indexable_results[0], indexable_results[1], indexable_results[2]
        n_samples = _num_samples(X)

        if (self.n_splits * self.split_size) >= n_samples:
            raise ValueError(
                "Cannot have (n_splits*split_size)={0} greater than the number of samples: {1}.".format(
                    (self.n_splits * self.split_size), n_samples
                )
            )

        indices = np.arange(n_samples)
        test_starts = range(
            n_samples - (self.n_splits * self.split_size), n_samples, self.split_size
        )

        for test_start in test_starts:
            yield (
                indices[0:test_start],
                indices[test_start : test_start + self.split_size],
            )


class RandomTimeSeriesForecastSplit(_BaseKFold):
    """
    This class is for time series one time forecast evaluation for random cross validation \
    n_splits : number of prediction to be make \
    pred_win : number of steps ahead prediction.
    seed : due to randomness, we like to set seed
    """

    def __init__(self, n_splits=10, pred_win=1, random_state=42):
        super().__init__(n_splits, shuffle=False, random_state=random_state)
        self.pred_win = pred_win

    def split(self, X, y=None, groups=None):
        indexable_results = indexable(X, y, groups)
        X, y, groups = indexable_results[0], indexable_results[1], indexable_results[2]
        n_samples = _num_samples(X)

        if self.pred_win > n_samples:
            raise ValueError(
                "Cannot have (pred_win)={0} greater than the number of samples: {1}.".format(
                    self.pred_win, n_samples
                )
            )

        if (n_samples - self.pred_win - max(0, n_samples // 2)) < self.n_splits:
            raise ValueError("Time Series is too short for the given parameters")

        indices = np.arange(n_samples)

        random.seed(self.random_state)
        test_starts = random.sample(
            range(max(0, n_samples // 2), n_samples - self.pred_win), self.n_splits
        )

        for test_start in test_starts:
            yield (
                indices[0:test_start],
                indices[test_start : test_start + self.pred_win],
            )
