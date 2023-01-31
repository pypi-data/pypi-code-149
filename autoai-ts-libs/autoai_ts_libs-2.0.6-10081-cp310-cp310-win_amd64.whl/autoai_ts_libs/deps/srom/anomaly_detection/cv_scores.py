# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


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


def _just_score_anomaly(
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
    return_prediction=False,
    pos_label=-1,
    error_score="raise-deprecating",
):

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

    # call predict function and get the ground truth
    if return_prediction:
        prediction_for_split_ = estimator.predict(trainX)
        if pos_label is not None:
            prediction_for_split_ = np.where(prediction_for_split_==pos_label)[0]

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
        ret.append(_num_samples(testX))
    if return_times:
        ret.extend([fit_time, score_time])
    if return_parameters:
        ret.append(parameters)
    if return_estimator:
        ret.append(estimator)
    if return_prediction:
        ret.append(prediction_for_split_)
    return ret


def cross_validate_anomaly(
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
    return_prediction=False,
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
        delayed(_just_score_anomaly)(
            estimator, # i removed clone, as we just assume given model is already trained
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
            return_prediction=return_prediction,
            error_score=error_score,
        )
        for train, test in cv.split(X, y, groups)
    )

    zipped_scores = list(zip(*scores))
    if return_train_score:
        train_scores = zipped_scores.pop(0)
        train_scores = _aggregate_score_dicts(train_scores)
    if return_prediction:
        test_predictions = zipped_scores.pop()
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

    if return_prediction:
        ret["test_predictions"] = np.array(test_predictions)

    return ret


def cross_validate_score_anomaly(
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
    cv_results = cross_validate_anomaly(
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

# To use the code
'''    
from sklearn.datasets import make_classification
X, y = make_classification(100)
X = X[:, 0:2]

from autoai_ts_libs.deps.srom.anomaly_detection.pipeline_utils import ExtremeOutlierKFold
aCV = ExtremeOutlierKFold(n_iteration=2, random_state=42)

from autoai_ts_libs.deps.srom.anomaly_detection.generalized_anomaly_model import GeneralizedAnomalyModel
from sklearn.ensemble import IsolationForest
mdl = IsolationForest()
mdl.fit(X)

# ideal usage
# split X : Train, Test
# train mdl on Train
# apply cross_validate_score_anomaly(trained_model_mdl, Test, CVObject, scoring='')

from autoai_ts_libs.deps.srom.anomaly_detection.cv_scores import cross_validate_score_anomaly
cross_validate_score_anomaly(mdl, X, cv=aCV, scoring='accuracy')
cross_validate_score_anomaly(mdl, X, cv=aCV, scoring='f1')
# scoring='f1'

from autoai_ts_libs.deps.srom.anomaly_detection.cv_scores import cross_validate_anomaly
cross_validate_anomaly(mdl, X, cv=aCV, scoring={'score':'accuracy'},return_prediction=True)
'''
