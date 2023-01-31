# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: cv_scores
   :synopsis: cv_scores.

.. moduleauthor:: SROM Team
"""

import numpy as np
import random
from random import sample
import math
import numbers
import time
import warnings
from traceback import format_exception_only

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

from sklearn.model_selection._validation import _score, _aggregate_score_dicts
from sklearn.metrics._scorer import _check_multimetric_scoring
from sklearn.metrics import check_scoring
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
                test_scores = dict(zip(scorer.keys(), [error_score,] * n_scorers))
                if return_train_score:
                    train_scores = dict(zip(scorer.keys(), [error_score,] * n_scorers))
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
            # estimator, trainX, testX, scorer, is_multimetric
            estimator,
            trainX,
            testX,
            scorer,
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
    if callable(scoring):
        scorers = {"score": check_scoring(estimator, scoring=scoring)}
    else:
        scorers = _check_multimetric_scoring(estimator, scoring=scoring)

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
