# function to pass
from autoai_ts_libs.deps.srom.anomaly_detection.cv_scores import cross_validate_score_anomaly, cross_validate_anomaly


def synthetic_repeated_validation(
    estimator, X, scoring, cv, n_jobs=None,
):
    """_summary_

    Args:
        estimator (_type_): _description_
        X (_type_): _description_
        scoring (_type_): _description_
        cv (_type_): _description_

    Returns:
        _type_: _description_
    """
    # call the cross validate function and get the parameter
    return cross_validate_anomaly(
        estimator=estimator, X=X, scoring=scoring, cv=cv, n_jobs=n_jobs,return_prediction=True
    )

