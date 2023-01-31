# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: pipeline utils
   :synopsis: pipeline utils.

.. moduleauthor:: SROM Team
"""


import numpy as np
import pandas as pd
import random
from random import sample
import math
import numbers
import time
import warnings
from traceback import format_exception_only
from sklearn.model_selection._split import _BaseKFold

# from sklearn.pipeline import Pipeline
# from autoai_ts_libs.deps.srom.imputation.utils import cross_val_score_impute

import sklearn.model_selection._validation
from sklearn.utils.validation import _is_arraylike, _num_samples
from sklearn.utils import _safe_indexing
import scipy.sparse as sp


def _index_param_value(X, v, indices):
    """Private helper function for parameter value indexing."""
    if not _is_arraylike(v) or _num_samples(v) != _num_samples(X):
        # pass through: skip indexing
        return v
    if sp.issparse(v):
        v = v.tocsr()
    return _safe_indexing(v, indices)


sklearn.model_selection._validation._index_param_value = _index_param_value

from sklearn.metrics import check_scoring

# from sklearn.metrics.scorer import _check_multimetric_scoring
from sklearn.utils import indexable
from sklearn.model_selection._split import check_cv
from sklearn.base import is_classifier, clone
from sklearn.exceptions import FitFailedWarning
from joblib import logger

try:
    from sklearn.utils._joblib import (
        Parallel,
        delayed,
    )  # _joblib is not supported in scikit-learn 0.19.2
except ModuleNotFoundError:
    from joblib import Parallel, delayed


def _aggregate_score_dicts(scores):
    return {key: np.asarray([score[key] for score in scores]) for key in scores[0]}


def _multimetric_score(estimator, X_test, y_test, scorers):
    """Return a dict of score for multimetric scoring"""
    scores = {}

    for name, scorer in scorers.items():
        if y_test is None:
            score = scorer(estimator, X_test)
        else:
            score = scorer(estimator, X_test, y_test)

        if hasattr(score, "item"):
            try:
                # e.g. unwrap memmapped scalars
                score = score.item()
            except ValueError:
                # non-scalar?
                pass
        scores[name] = score

        if not isinstance(score, numbers.Number):
            raise ValueError(
                "scoring must return a number, got %s (%s) "
                "instead. (scorer=%s)" % (str(score), type(score), name)
            )
    return scores


def _score(estimator, X_test, y_test, scorer, is_multimetric=False):
    """
    Internal method work as a helper method to get the score.
    """
    if is_multimetric:
        return _multimetric_score(estimator, X_test, y_test, scorer)
    else:
        if y_test is None:
            score = scorer(estimator, X_test)
        else:
            score = scorer(estimator, X_test, y_test)

        if hasattr(score, "item"):
            try:
                # e.g. unwrap memmapped scalars
                score = score.item()
            except ValueError:
                # non-scalar?
                pass

        if not isinstance(score, numbers.Number):
            raise ValueError(
                "scoring must return a number, got %s (%s) "
                "instead. (scorer=%r)" % (str(score), type(score), scorer)
            )
    return score


def _check_multimetric_scoring(estimator, scoring=None):
    if callable(scoring) or scoring is None or isinstance(scoring, str):
        scorers = {"score": check_scoring(estimator, scoring=scoring)}
        return scorers, False
    else:
        err_msg_generic = (
            "scoring should either be a single string or "
            "callable for single metric evaluation or a "
            "list/tuple of strings or a dict of scorer name "
            "mapped to the callable for multiple metric "
            "evaluation. Got %s of type %s" % (repr(scoring), type(scoring))
        )

        if isinstance(scoring, (list, tuple, set)):
            err_msg = (
                "The list/tuple elements must be unique "
                "strings of predefined scorers. "
            )
            invalid = False
            try:
                keys = set(scoring)
            except TypeError:
                invalid = True
            if invalid:
                raise ValueError(err_msg)

            if len(keys) != len(scoring):
                raise ValueError(
                    err_msg + "Duplicate elements were found in"
                    " the given list. %r" % repr(scoring)
                )
            elif len(keys) > 0:
                if not all(isinstance(k, str) for k in keys):
                    if any(callable(k) for k in keys):
                        raise ValueError(
                            err_msg + "One or more of the elements were "
                            "callables. Use a dict of score name "
                            "mapped to the scorer callable. "
                            "Got %r" % repr(scoring)
                        )
                    else:
                        raise ValueError(
                            err_msg + "Non-string types were found in "
                            "the given list. Got %r" % repr(scoring)
                        )
                scorers = {
                    scorer: check_scoring(estimator, scoring=scorer)
                    for scorer in scoring
                }
            else:
                raise ValueError(err_msg + "Empty list was given. %r" % repr(scoring))

        elif isinstance(scoring, dict):
            keys = set(scoring)
            if not all(isinstance(k, str) for k in keys):
                raise ValueError(
                    "Non-string types were found in the keys of "
                    "the given dict. scoring=%r" % repr(scoring)
                )
            if len(keys) == 0:
                raise ValueError("An empty dict was passed. %r" % repr(scoring))
            scorers = {
                key: check_scoring(estimator, scoring=scorer)
                for key, scorer in scoring.items()
            }
        else:
            raise ValueError(err_msg_generic)
        return scorers, True


class ImputationKFold(_BaseKFold):
    """
    K-Folds cross-validator object for multivariate Imputation Work (both non time series and time series)
    Split the multi-variate dataset into k randomly selected folds of the
    missing values (with the selection of the missing controlled by the random_state.
    Each fold has two equally shaped data (same size): where some of the entry in
    training data is marked as missing, and validation data has those values.
    This data preparation for imputation is based on missing completely at random
    (MCAR) concept and IID. over time.  No consideration consecutive missing.
    The MCAR and IID assumptions imply that the missing pattern is completely independent from
    the missing, observed values and the time (or the index of observed value).
    To generate MCAR patterns of missing data, we randomly sample a subset of the entries in X
    to be missing, assuming that each entry is equally likely to be chosen.
    """

    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        impute_size=0.1,
        missing_value=np.NaN,
        first_nullable=False,
        last_nullable=False,
        enable_debug=False,
        return_index=False,
        columns_to_ignore=None,
    ):
        """
        Parameters
        ----------
        n_splits (int) : default=10
            The number of iterations to be performed. Must be at least 3
            it is assigned to n_splits an internal variable
        random_state (int) : None
            Generate random pseudo sequences over different iteration
        impute_size (int or float): default=0.1
            The number of individual entries in data to be marked as missing. Set around 10\%
        missing_value (int or NaN): missing value indicator, default = None \
            The common way to indicate a missing value: Some occasion -1 or None.
        first_nullable (boolean):  whether we allow the first row being missing
        last_nullable (boolean):   whether we allow the last row being missing
        enable_debug (boolean):   flag enables recording of debugging information
        return_index (boolean): return index where to fill the NaNs
        columns_to_ignore (list of int): columns to ignore
        """
        self.impute_size = impute_size
        self.missing_value = missing_value
        self.random_state = random_state
        self.n_splits = n_iteration
        self.first_nullable = first_nullable
        self.last_nullable = last_nullable
        self.enable_debug = enable_debug
        self.return_index = return_index
        self.columns_to_ignore = columns_to_ignore

        if self.enable_debug:
            print(self.impute_size)
            print(self.missing_value)
            print(self.random_state)
            print(self.n_splits)
            print(self.first_nullable)
            print(self.last_nullable)

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """

        if not (X.ndim == 2 and X.shape[1] >= 1):
            raise ValueError("Expects a matrix as an input")

        impute_size = self.impute_size
        missing_value = self.missing_value
        random_state = self.random_state
        n_splits = self.n_splits
        first_nullable = self.first_nullable
        last_nullable = self.last_nullable

        # set the seed here
        random.seed(random_state)
        for _ in range(n_splits):
            data = X.copy()

            ## xy are the location where we can sample for artifical missing
            xy = np.where((~np.isnan(data)) & (data != missing_value))
            # xy = np.where(data != missing_value)

            init_idx = list(zip(xy[0], xy[1]))

            length = data.shape[0]
            removed_idx_list = []

            if first_nullable == False:
                removed_idx_list.append(0)

            if last_nullable == False:
                removed_idx_list.append(length - 1)

            if self.enable_debug:
                print("data:\n", data)
                print("removed index list: \n", removed_idx_list)
                print("xy:\n", xy)
                print("xy[0]:\n", xy[0])
                print("xy[1]:\n", xy[1])
                print("init_idx:\n", init_idx)

            tmp_idx = [x for x in init_idx if (x[0] not in removed_idx_list)]
            if self.columns_to_ignore:
                idx = [x for x in tmp_idx if (x[1] not in self.columns_to_ignore)]
            else:
                idx = tmp_idx

            # print(init_idx)
            # print(idx)

            if isinstance(impute_size, numbers.Integral):
                sampled_idx = sample(idx, impute_size)
            else:
                sampled_idx = sample(idx, int(math.ceil(impute_size * len(idx))))

            if self.enable_debug:
                print(sampled_idx)
                print(length)

            if self.return_index:
                yield sampled_idx, sampled_idx
            else:
                # This statement is not nessecary because the index is
                # purely sampled from the original indices
                # sampled_idx = [x for x in sampled_idx if (x[0] < length)]

                p_data = data.copy()
                # This is to ensure that p_data is a float.  If it is an integer, the
                # assignment to a specific location as missing would be failed if
                # missing_value is np.Nan
                p_data = p_data.astype(float)
                # set the missing values
                for item in sampled_idx:
                    p_data[item] = missing_value
                yield p_data, data


class MCARImputationKFold(_BaseKFold):
    """
    K-Folds cross-validator object for Imputation Work.

    Provides train and test data (not indices). Split dataset into k
    randomaly selected folds (with shuffling that is controllable by random_state).
    Each fold has two equally shaped data : where some of the entry in training
    data is marked as missing, and validation data has those value.

    This data preparation for imputation is based on missing completely at random
    (MCAR) concept. The MCAR assumption implies that the missing pattern is
    completely independent from both the missing and observed values. To generate
    MCAR patterns of missing data, we randomly sample a subset of the entries in X
    to be missing, assuming that each entry is equally likely to be chosen.

    """

    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        impute_size=0.1,
        missing_value=np.NaN,
        return_index=False,
        columns_to_ignore=None,
    ):
        """
        Parameters
        ----------

        n_iteration (int) : default=10
            Number of iteration to be performed. Must be at least 3. Due to naming convection
            it is assigned to n_splits an internal variable

        random_state (int) : None
            Generate randon pseudo sequences over different iteration

        impute_size (int or float): default=0.1
            Number of individual entry in data to be marked as missing. Set around 10\%

        missing_value (int or NaN): missing value indicator, default = None \
            The common way to indicate a missing value: Some occasion -1 or None.
            
        return_index (boolean): return index where to fill the NaNs
        columns_to_ignore (list of int): columns to ignore
        """
        self.impute_size = impute_size
        self.missing_value = missing_value
        self.random_state = random_state
        self.n_splits = n_iteration
        self.return_index = return_index
        self.columns_to_ignore = columns_to_ignore

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """

        # set the seed here
        random.seed(self.random_state)
        for _ in range(self.n_splits):
            data = X.copy()
            xy = np.where(data != self.missing_value)
            tmp_idx = list(zip(xy[0], xy[1]))

            if self.columns_to_ignore:
                idx = [x for x in tmp_idx if (x[1] not in self.columns_to_ignore)]
            else:
                idx = tmp_idx

            if isinstance(self.impute_size, numbers.Integral):
                sampled_idx = sample(idx, self.impute_size)
            else:
                sampled_idx = sample(idx, int(math.ceil(self.impute_size * len(idx))))

            if self.return_index:
                return sampled_idx, sampled_idx
            else:
                p_data = data.copy()
                # This is to ensure that p_data is a float.  If it is an integer, the
                # assignment to a specific location as missing would be failed if
                # missing_value is np.Nan
                p_data = p_data.astype(float)
                # set the missing values
                for item in sampled_idx:
                    p_data[item] = self.missing_value
                yield p_data, data


class MARImputationKFold(_BaseKFold):
    """
    K-Folds cross-validator object for Imputation Work.

    Provides train and test data (not indices). Split dataset into k
    randomaly selected folds (with shuffling that is controllable by random_state).
    Each fold has two equally shaped data : where some of the entry in training
    data is marked as missing, and validation data has those value.

    """

    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        impute_size=0.1,
        missing_value=np.NaN,
        return_index=False,
        columns_to_ignore=None,
    ):
        """
        Parameters
        ----------

            n_iteration (int) : default=10
                Number of iteration to be performed. Must be at least 3. Due to naming convection
                it is assigned to n_splits an internal variable

            random_state (int) : None
                Generate randon pseudo sequences over different iteration

            impute_size (int or float): default=0.1
                Number of individual entry in data to be marked as missing. Set around 10\%

            missing_value (int or NaN): missing value indicator, default = None \
                The common way to indicate a missing value: Some occasion -1 or None.
            return_index (boolean): return index where to fill the NaNs
            columns_to_ignore (list of int): columns to ignore
        """
        self.impute_size = impute_size
        self.missing_value = missing_value
        self.random_state = random_state
        self.n_splits = n_iteration
        self.return_index = return_index
        self.columns_to_ignore = columns_to_ignore

    def _generate_missing_mask_MAR(self, X, percent_missing=10):
        """
        Internal method to generate missing mask mar.
        """
        mask = np.zeros(X.shape)
        n_values_to_discard = int((percent_missing / 100) * X.shape[0])
        # for each affected column
        for col_affected in range(X.shape[1]):
            # select a random other column for missingness to depend on
            depends_on_col = np.random.choice(
                [c for c in range(X.shape[1]) if c != col_affected]
            )
            # pick a random percentile of values in other column
            if n_values_to_discard < X.shape[0]:
                discard_lower_start = np.random.randint(
                    0, X.shape[0] - n_values_to_discard
                )
            else:
                discard_lower_start = 0
            discard_idx = range(
                discard_lower_start, discard_lower_start + n_values_to_discard
            )
            values_to_discard = X[:, depends_on_col].argsort()[discard_idx]
            mask[values_to_discard, col_affected] = 1
        return mask

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """

        # set the seed here
        random.seed(self.random_state)
        for _ in range(self.n_splits):
            data = X.copy()
            sampled_idx = self._generate_missing_mask_MAR(data)

            if self.return_index:
                yield sampled_idx, sampled_idx
            else:
                p_data = data.copy()
                # This is to ensure that p_data is a float.  If it is an integer, the
                # assignment to a specific location as missing would be failed if
                # missing_value is np.Nan
                p_data = p_data.astype(float)
                # set the missing values
                for item in zip(*np.where(sampled_idx == 1)):
                    p_data[item] = self.missing_value
                yield p_data, data


class MNARImputationKFold(_BaseKFold):
    """
    K-Folds cross-validator object for Imputation Work.

    Provides train and test data (not indices). Split dataset into k
    randomaly selected folds (with shuffling that is controllable by random_state).
    Each fold has two equally shaped data : where some of the entry in training
    data is marked as missing, and validation data has those value.

    """

    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        impute_size=0.1,
        missing_value=np.NaN,
        return_index=False,
        columns_to_ignore=None,
    ):
        """
        Parameters
        ----------

        n_iteration (int) : default=10
            Number of iteration to be performed. Must be at least 3. Due to naming convection
            it is assigned to n_splits an internal variable

        random_state (int) : None
            Generate randon pseudo sequences over different iteration

        impute_size (int or float): default=0.1
            Number of individual entry in data to be marked as missing. Set around 10\%

        missing_value (int or NaN): missing value indicator, default = None \
            The common way to indicate a missing value: Some occasion -1 or None.

        return_index (boolean): return index where to fill the NaNs
        columns_to_ignore (list of int): columns to ignore
        """
        self.impute_size = impute_size
        self.missing_value = missing_value
        self.random_state = random_state
        self.n_splits = n_iteration
        self.return_index = return_index
        self.columns_to_ignore = columns_to_ignore


    def _generate_missing_mask_MNAR(self, X, percent_missing=10):
        """
        Internal method to generate missing mask mnar.
        """
        mask = np.zeros(X.shape)
        n_values_to_discard = int((percent_missing / 100) * X.shape[0])
        # for each affected column
        for col_affected in range(X.shape[1]):
            # pick a random percentile of values in other column
            if n_values_to_discard < X.shape[0]:
                discard_lower_start = np.random.randint(
                    0, X.shape[0] - n_values_to_discard
                )
            else:
                discard_lower_start = 0
            discard_idx = range(
                discard_lower_start, discard_lower_start + n_values_to_discard
            )
            values_to_discard = X[:, col_affected].argsort()[discard_idx]
            mask[values_to_discard, col_affected] = 1
        return mask

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """

        # set the seed here
        random.seed(self.random_state)
        for _ in range(self.n_splits):
            data = X.copy()
            sampled_idx = self._generate_missing_mask_MNAR(data)

            if self.return_index:
                yield sampled_idx, sampled_idx
            else:
                p_data = data.copy()
                # This is to ensure that p_data is a float.  If it is an integer, the
                # assignment to a specific location as missing would be failed if
                # missing_value is np.Nan
                p_data = p_data.astype(float)
                # set the missing values
                for item in zip(*np.where(sampled_idx == 1)):
                    p_data[item] = self.missing_value
                yield p_data, data


class TsIIDConsecutiveKFold(_BaseKFold):
    """
    K-Folds cross-validator object for univariate time series Imputation Work
    Provides train and test data.   Split a time series into k randomly selected folds of the
    missing values (with the selection of the missing controlled by the random_state.
    Each fold has two equally shaped data (same size of time series): where some of the entry in
    training data is marked as missing, and validation data has those values.
    This data preparation for imputation is based on missing completely at random
    (MCAR) concept and IID over time.  There is a consideration consecutive missing as fixed length.
    The MCAR and IID assumptions imply that the missing pattern is completely independent from
    the missing, observed values and the time (or the index of observed value).  The consecutive missing
    means that there is always two consecutive missing together
    To generate MCAR patterns of missing data, we randomly sample a subset of the entries in X
    to be missing, assuming that each entry is equally likely to be chosen.

    """

    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        impute_size=0.1,
        missing_value=np.NaN,
        n_consecutive=2,
        first_nullable: bool = False,
        last_nullable: bool = False,
        enable_debug: bool = False,
        return_index=False,
        columns_to_ignore=None,
    ):
        """
        Parameters
        ----------
        n_iteration (int) : default=10
            The number of iterations to be performed. Must be at least 3
            it is assigned to n_splits an internal variable
        random_state (int) : None
            Generate random pseudo sequences over different iteration
        impute_size (int or float): default=0.1
            The number of individual entries in data to be marked as missing. Set around 10\%
        missing_value (int or NaN): missing value indicator, default = None \
            The common way to indicate a missing value: Some occasion -1 or None.
        n_consecutive:  number of consectutive missing 
        first_nullable (boolean):  whether we allow the first record of the time series being missing
        last_nullable (boolean):   whether we allow the last record of the time series being missing
        enable_debug (boolean):   flag enables recording of debugging information
        return_index (boolean): return index where to fill the NaNs
        columns_to_ignore (list of int): columns to ignore
        """

        self.impute_size = impute_size
        self.missing_value = missing_value
        self.random_state = random_state
        self.n_splits = n_iteration
        self.n_consecutive = n_consecutive
        self.first_nullable = first_nullable
        self.last_nullable = last_nullable
        self.return_index = return_index
        self.columns_to_ignore = columns_to_ignore

        if enable_debug:
            print(self.impute_size)
            print(self.missing_value)
            print(self.random_state)
            print(self.n_splits)
            print(self.n_consecutive)
            print(self.first_nullable)
            print(self.last_nullable)

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """

        impute_size = self.impute_size
        missing_value = self.missing_value
        random_state = self.random_state
        n_splits = self.n_splits
        n_consecutive = self.n_consecutive
        first_nullable = self.first_nullable
        last_nullable = self.last_nullable

        """
        if not (X.ndim == 2 and X.shape[1] == 1):
            raise ValueError(
                "timeseries KFold expects a single-column matrix as an input"
            )
        """

        if n_consecutive < 2:
            raise ValueError("Expect the consecutive length at least 2")

        # set the seed here
        random.seed(random_state)
        for _ in range(n_splits):
            data = X.copy()

            xy = np.where((~np.isnan(data)) & (data != missing_value))
            # xy = np.where(data != missing_value)

            init_idx = list(zip(xy[0], xy[1]))

            length = data.shape[0]
            removed_idx_list = []

            if first_nullable == False:
                removed_idx_list.append(0)

            if last_nullable == False:
                for i in range(0, n_consecutive - 1):
                    removed_idx_list.append(length - 1 - i)
                removed_idx_list.append(length - n_consecutive)

            tmp_idx = [x for x in init_idx if (x[0] not in removed_idx_list)]
            if self.columns_to_ignore:
                idx = [x for x in tmp_idx if (x[1] not in self.columns_to_ignore)]
            else:
                idx = tmp_idx
            # print(init_idx)
            # print(idx)

            if isinstance(impute_size, numbers.Integral):

                n_samples = math.ceil(float(impute_size) / n_consecutive)

                init_sampled_idx = sample(idx, n_samples)
                sampled_idx = init_sampled_idx.copy()
                for i in range(1, n_consecutive):
                    sampled_idx_next = [(x[0] + i, x[1]) for x in init_sampled_idx]
                    sampled_idx = sampled_idx + sampled_idx_next
            else:
                init_sampled_idx = sample(
                    idx, int(math.ceil(impute_size * len(idx) / n_consecutive))
                )
                sampled_idx = init_sampled_idx.copy()

                for i in range(1, n_consecutive):
                    sampled_idx_next = [(x[0] + i, x[1]) for x in init_sampled_idx]
                    sampled_idx = sampled_idx + sampled_idx_next

            # print(init_sampled_idx)
            # print(length)
            # print(sampled_idx)
            # print(removed_idx_list)

            # Consider possibility that final elements of generated consecutive missing with
            # index beyond the length of the data could be out of bounds. This could happen if
            # the final consecutive missing sample happen at the end of the data

            if last_nullable == False:
                sampled_idx = [x for x in sampled_idx if (x[0] < length - 1)]
            else:
                sampled_idx = [x for x in sampled_idx if (x[0] < length)]

            if self.return_index:
                yield sampled_idx, sampled_idx
            else:
                p_data = data.copy()
                # This is to ensure that p_data is a float.  If it is an integer, the
                # assignment to a specific location as missing would be failed if
                # missing_value is np.Nan
                p_data = p_data.astype(float)
                # set the missing values
                for item in sampled_idx:
                    p_data[item] = missing_value
                yield p_data, data


def _missing_pattern_zipf_trunc(power_decay_rate, max_miss_duration):
    """
    Generate a missing pattern following the zipf distribution

    Args:

        power_decay_rate - The coefficient of zipf power
        max_miss_duration:  The maximum length of consecutive missing

    Returns:
        missing pattern follows the zipf
    """

    f = lambda x: pow(x, power_decay_rate)
    adjust_array = [1 / f(x) for x in range(1, max_miss_duration + 1)]
    adjust_sum = sum(adjust_array)

    probability_distribution = [x / adjust_sum for x in adjust_array]

    prob_dict = {
        i + 1: probability_distribution[i]
        for i in range(0, len(probability_distribution), 1)
    }

    missing_pattern = pd.DataFrame(
        list(prob_dict.items()), columns=["length", "percentage"]
    )

    missing_pattern = missing_pattern.sort_values(by="length")

    return missing_pattern


class TsVariableConsecutiveKFold(_BaseKFold):
    """
    K-Folds cross-validator object for univariate time series Imputation Work
    Provides train and test data.   Split a time series into k randomly selected folds of the
    missing values (with the selection of the missing controlled by the random_state.
    Each fold has two equally shaped data (same size of time series): where some of the entry in
    training data is marked as missing, and validation data has those values.
    This data preparation for imputation is based on missing completely at random
    (MCAR) concept and IID over time.  There is a consideration consecutive missing as fixed length.
    The MCAR and IID assumptions imply that the missing pattern is completely independent from
    the missing, observed values and the time (or the index of observed value).  The consecutive missing
    means that there is always two consecutive missing together
    To generate MCAR patterns of missing data, we randomly sample a subset of the entries in X
    to be missing, assuming that each entry is equally likely to be chosen.

    """

    def __init__(
        self,
        n_iteration=10,
        random_state=None,
        impute_size=0.1,
        missing_value=np.NaN,
        consecutive_dist=None,
        first_nullable: bool = False,
        last_nullable: bool = False,
        enable_debug: bool = False,
        return_index=False,
        columns_to_ignore=None,
    ):
        """
        Parameters
        ----------
        n_iteration (int) : default=10
            The number of iterations to be performed. Must be at least 3
            it is assigned to n_splits an internal variable
        random_state (int) : None
            Generate random pseudo sequences over different iteration
        impute_size (int or float): default=0.1
            The number of individual entries in data to be marked as missing. Set around 10\%
        missing_value (int or NaN): missing value indicator, default = None \
            The common way to indicate a missing value: Some occasion -1 or None.
        consecutive_dist:  the probability distribution of consectutive missing as a dataframe. For example:
                    
                    length 	percentage
                    1       0.646829
                    2     	0.228689
                    3 	    0.124482 
            
                It is a dataframe with two columns - missing length and percentage.  
                
        first_nullable (boolean):  whether we allow the first record of the time series being missing
        last_nullable (boolean):   whether we allow the last record of the time series being missing
        enable_debug (boolean):   flag enables recording of debugging information
        return_index (boolean): return index where to fill the NaNs
        columns_to_ignore (list of int): columns to ignore
        """
        self.impute_size = impute_size
        self.missing_value = missing_value
        self.random_state = random_state
        self.n_splits = n_iteration
        self.first_nullable = first_nullable
        self.last_nullable = last_nullable
        self.return_index = return_index
        self.columns_to_ignore = columns_to_ignore

        if consecutive_dist is None:
            self.consecutive_dist = _missing_pattern_zipf_trunc(1.5, 3)
        else:
            self.consecutive_dist = consecutive_dist

        if enable_debug:
            print(self.impute_size)
            print(self.missing_value)
            print(self.random_state)
            print(self.n_splits)
            print(self.consecutive_dist)
            print(self.first_nullable)
            print(self.last_nullable)

    def split(self, X, y=None, groups=None):
        """
        Parameters
        ----------
            X (numpy array): Input features.
            y(numpy array): Target feature.

        Returns
        --------
            Splitted train with externally added missing values and test sets with
            original values.
        """

        impute_size = self.impute_size
        missing_value = self.missing_value
        random_state = self.random_state
        n_splits = self.n_splits
        consecutive_dist = self.consecutive_dist
        first_nullable = self.first_nullable
        last_nullable = self.last_nullable

        if not (X.ndim == 2 and X.shape[1] == 1):
            raise ValueError(
                "timeseries KFold expects a single-column matrix as an input"
            )

        # set the seed here
        random.seed(random_state)
        for _ in range(n_splits):
            data = X.copy()
            xy = np.where((~np.isnan(data)) & (data != missing_value))
            # xy = np.where(data != missing_value)

            init_idx = list(zip(xy[0], xy[1]))

            length = data.shape[0]
            removed_idx_list = []

            if first_nullable == False:
                removed_idx_list.append(0)

            if last_nullable == False:
                removed_idx_list.append(length - 1)

            idx = [x for x in init_idx if (x[0] not in removed_idx_list)]
            # print(init_idx)
            # print(idx)

            avg_length = (
                consecutive_dist["length"] * consecutive_dist["percentage"]
            ).sum()

            if isinstance(impute_size, numbers.Integral):

                n_samples = math.ceil(float(impute_size) / avg_length)

                init_sampled_idx = sample(idx, n_samples)
                sampled_idx = init_sampled_idx.copy()

                init_sampled_idx = np.array(init_sampled_idx)

                # Choose the random object to ensure the repeatibility
                randomnp = np.random.default_rng(seed=random_state)

                lengths = randomnp.choice(
                    consecutive_dist["length"],
                    size=(n_samples),
                    p=consecutive_dist["percentage"],
                )

                for no, idx in enumerate(init_sampled_idx):
                    print("number: ", no, idx, lengths[no])

                    for i in range(lengths[no]):
                        sampled_idx.append((idx[0] + i, idx[1]))

            else:
                n_samples = int(math.ceil(impute_size * len(idx) / avg_length))
                init_sampled_idx = sample(idx, n_samples)

                sampled_idx = init_sampled_idx.copy()

                # Choose the random object to ensure the repeatibility
                randomnp = np.random.default_rng(seed=random_state)

                lengths = randomnp.choice(
                    consecutive_dist["length"],
                    size=(n_samples),
                    p=consecutive_dist["percentage"],
                )

                for no, idx in enumerate(init_sampled_idx):
                    if lengths[no] > 1:
                        for i in range(lengths[no]):
                            sampled_idx.append((idx[0] + i, idx[1]))

            # print(avg_length)
            # print(init_sampled_idx)
            # print(lengths)
            # print(random_state)

            # Consider possibility that final elements of generated consecutive missing with
            # index beyond the length of the data could be out of bounds. This could happen if
            # the final consecutive missing sample happen at the end of the data

            if last_nullable == False:
                sampled_idx = [x for x in sampled_idx if (x[0] < length - 1)]
            else:
                sampled_idx = [x for x in sampled_idx if (x[0] < length)]

            if self.return_index:
                yield sampled_idx, sampled_idx
            else:
                p_data = data.copy()
                # This is to ensure that p_data is a float.  If it is an integer, the
                # assignment to a specific location as missing would be failed if
                # missing_value is np.Nan
                p_data = p_data.astype(float)

                # print(sampled_idx)
                # print(p_data)

                # set the missing values
                for item in sampled_idx:
                    p_data[item] = missing_value
                yield p_data, data


def _fit_and_score_impute(
    estimator,
    X,
    y,
    scorer,
    trainX,
    testX,
    verbose,
    parameters,
    fit_params,
    return_train_score=False,
    return_parameters=False,
    return_n_test_samples=False,
    return_times=False,
    return_estimator=False,
    error_score="raise-deprecating",
):
    """
    Parameters
    ----------
        estimator: estimator.
        X(pandas.Dataframe or numpy array): array-like
        y(numpy array): array-like, optional, default: None
        groups : array-like, with shape (n_samples,), optional
        scoring : string, callable, list/tuple, dict or None, default: None
        cv: string, default: 'warn'
        n_jobs:  int or None, optional, default:None
        verbose: integer, optional
        fit_params: dict, optional
        pre_dispatch: int, or string, optional
        return_train_score: boolean, only supported False,
        return_estimator: boolean, default: False
        error_score:string default: 'raise-deprecating'

    Returns
    --------
        score.

    """
    if return_train_score or return_n_test_samples:
        raise ValueError(
            "True value is not supported for return_train_score and return_n_test_samples"
        )

    # Adjust length of sample weights
    fit_params = fit_params if fit_params is not None else {}
    fit_params = dict(
        [(k, _index_param_value(X, v, trainX)) for k, v in fit_params.items()]
    )

    train_scores = {}
    if parameters is not None:
        estimator.set_params(**parameters)

    start_time = time.time()

    is_multimetric = not callable(scorer)
    n_scorers = len(scorer.keys()) if is_multimetric else 1

    try:
        estimator.fit(trainX, **fit_params)
    except Exception as e:
        # Note fit time as time until error
        fit_time = time.time() - start_time
        score_time = 0.0
        if error_score == "raise":
            raise
        elif error_score == "raise-deprecating":
            warnings.warn(
                "From version 0.22, errors during fit will result "
                "in a cross validation score of NaN by default. Use "
                "error_score='raise' if you want an exception "
                "raised or error_score=np.nan to adopt the "
                "behavior from version 0.22.",
                FutureWarning,
            )
            raise
        elif isinstance(error_score, numbers.Number):
            if is_multimetric:
                test_scores = dict(zip(scorer.keys(), [error_score] * n_scorers))
                if return_train_score:
                    train_scores = dict(zip(scorer.keys(), [error_score] * n_scorers))
            else:
                test_scores = error_score
                if return_train_score:
                    train_scores = error_score
            warnings.warn(
                "Estimator fit failed. The score on this train-test"
                " partition for these parameters will be set to %f. "
                "Details: \n%s" % (error_score, format_exception_only(type(e), e)[0]),
                FitFailedWarning,
            )
        else:
            raise ValueError(
                "error_score must be the string 'raise' or a"
                " numeric value. (Hint: if using 'raise', please"
                " make sure that it has been spelled correctly.)"
            )
    else:
        fit_time = time.time() - start_time
        # _score will return dict if is_multimetric is True
        test_scores = _score(
            estimator, trainX, testX, scorer, is_multimetric=is_multimetric
        )
        score_time = time.time() - start_time - fit_time
        # if return_train_score:
        #    train_scores = _score(estimator, trainX, trainy, scorer,
        #                          is_multimetric)

    msg = ""
    if verbose > 2:
        if is_multimetric:
            for scorer_name, score in test_scores.items():
                msg += ", %s=%s" % (scorer_name, score)
        else:
            msg += ", score=%s" % test_scores
    if verbose > 1:
        total_time = score_time + fit_time
        end_msg = "%s, total=%s" % (msg, logger.short_format_time(total_time))
        print("[CV] %s %s" % ((64 - len(end_msg)) * ".", end_msg))

    ret = [train_scores, test_scores] if return_train_score else [test_scores]

    if return_n_test_samples:
        ret.append(-1)  # ret.append(_num_samples(testX))
    if return_times:
        ret.extend([fit_time, score_time])
    if return_parameters:
        ret.append(parameters)
    if return_estimator:
        ret.append(estimator)
    return ret


def cross_validate_impute(
    estimator,
    X,
    y=None,
    groups=None,
    scoring=None,
    cv="warn",
    n_jobs=None,
    verbose=0,
    fit_params=None,
    pre_dispatch="2*n_jobs",
    return_train_score=False,
    return_estimator=False,
    error_score="raise-deprecating",
):
    """
    Parameters
    ----------
        estimator: estimator.
        X(pandas.Dataframe or numpy array): array-like
        y(numpy array): array-like, optional, default: None
        groups : array-like, with shape (n_samples,), optional
        scoring : string, callable, list/tuple, dict or None, default: None
        cv: string, default: 'warn'
        n_jobs:  int or None, optional, default:None
        verbose: integer, optional
        fit_params: dict, optional
        pre_dispatch: int, or string, optional
        return_train_score: boolean, only supported False,
        return_estimator: boolean, default: False
        error_score:string default: 'raise-deprecating'

    Returns
    --------
        cross validation results.

    """

    X, y, groups = indexable(X, y, groups)
    cv = check_cv(cv, y, classifier=is_classifier(estimator))
    scorers, _ = _check_multimetric_scoring(estimator, scoring=scoring)

    # We clone the estimator to make sure that all the folds are
    # independent, and that it is pickle-able.
    parallel = Parallel(n_jobs=n_jobs, verbose=verbose, pre_dispatch=pre_dispatch)
    scores = parallel(
        delayed(_fit_and_score_impute)(
            clone(estimator),
            X,
            y,
            scorers,
            train,
            test,
            verbose,
            None,
            fit_params,
            return_train_score=return_train_score,
            return_times=True,
            return_estimator=return_estimator,
            error_score=error_score,
        )
        for train, test in cv.split(X, y, groups)
    )

    zipped_scores = list(zip(*scores))
    if return_train_score:
        train_scores = zipped_scores.pop(0)
        train_scores = _aggregate_score_dicts(train_scores)
    if return_estimator:
        fitted_estimators = zipped_scores.pop()
    test_scores, fit_times, score_times = zipped_scores
    test_scores = _aggregate_score_dicts(test_scores)

    ret = {}
    ret["fit_time"] = np.array(fit_times)
    ret["score_time"] = np.array(score_times)

    if return_estimator:
        ret["estimator"] = fitted_estimators

    for name in scorers:
        ret["test_%s" % name] = np.array(test_scores[name])
        if return_train_score:
            key = "train_%s" % name
            ret[key] = np.array(train_scores[name])

    return ret


def cross_val_score_impute(
    estimator,
    X,
    y=None,
    groups=None,
    scoring=None,
    cv="warn",
    n_jobs=None,
    verbose=0,
    fit_params=None,
    pre_dispatch="2*n_jobs",
    error_score="raise-deprecating",
):
    """
    Parameters
    ----------
        estimator: estimator.
        X(pandas.Dataframe or numpy array): array-like
        y(numpy array): array-like, optional, default: None
        groups : array-like, with shape (n_samples,), optional
        scoring : string, callable, list/tuple, dict or None, default: None
        cv: string, default: 'warn'
        n_jobs:  int or None, optional, default:None
        verbose: integer, optional
        fit_params: dict, optional
        pre_dispatch: int, or string, optional
        error_score:string default: 'raise-deprecating'

    Returns
    --------
        Array of scores of the estimator for each run of the cross validation.

    """

    scorer = check_scoring(estimator, scoring=scoring)
    cv_results = cross_validate_impute(
        estimator=estimator,
        X=X,
        y=y,
        groups=groups,
        scoring={"score": scorer},
        cv=cv,
        return_train_score=False,
        n_jobs=n_jobs,
        verbose=verbose,
        fit_params=fit_params,
        pre_dispatch=pre_dispatch,
        error_score=error_score,
    )
    return cv_results["test_score"]
