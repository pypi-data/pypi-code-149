"""
Block implementation that wraps srom.anomaly_detection.cv_scores.cross_validate_score_anomaly
"""
from srom.anomaly_detection.cv_scores import (
    cross_validate_score_anomaly as cross_validate_anomaly_score,
)


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

    return cross_validate_anomaly_score(
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
        error_score=error_score,
    )
