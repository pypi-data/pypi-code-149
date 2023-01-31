"""
Block implementation that wraps srom.anomaly_detection.cv_scores.cross_validate_anomaly
"""

# First Party
from srom.anomaly_detection.cv_scores import (
    cross_validate_anomaly as cross_validate_score,
)


def cross_validate_anomaly(
    estimator,
    X,
    y=None,
    groups=None,
    scoring=None,
    cv=None,
    n_jobs=None,
    verbose=0,
    fit_params=None,
    pre_dispatch="2*n_jobs",
    return_train_score=False,
    return_estimator=False,
    return_prediction=False,
    error_score="raise-deprecating",
):

    return cross_validate_score(
        estimator=estimator,
        X=X,
        y=y,
        groups=groups,
        scoring=scoring,
        cv=cv,
        n_jobs=n_jobs,
        verbose=verbose,
        fit_params=fit_params,
        pre_dispatch=pre_dispatch,
        return_train_score=return_train_score,
        return_estimator=return_estimator,
        return_prediction=return_prediction,
        error_score=error_score,
    )
