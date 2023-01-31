from re import A
import numpy as np
import math
from autoai_ts_libs.deps.srom.anomaly_detection.pipeline_utils import (
    DeviationbasedExtremeOutlier,
    LocalizedExtremeOutlier,
    TrendOutlier,
    VarianceOutlier,
    FlatLineOutlier,
    ExtremeOutlier,
    JitterOutlier,
    LevelShiftOutlier
)
from autoai_ts_libs.anomaly_detection.estimators.constants import SYNTHESIZED_ANOMALY
import logging

tslogger = logging.getLogger(__name__)

def get_anomaly_parameters():
    """
     Method to get anomaly parameters 
    """
    return {
        "Extreme" : {"anomaly_factor":[2,4,5]},
        "LocalizedExtreme" : {"anomaly_factor":[2,3]},
        "LevelShift" : {"anomaly_factor":[2,3]},
        "Deviation" : {"anomaly_factor":[2,3]},
        "Jitter" : {"outlier_factor":[2,3],"n_consecutive": [0.07,0.09,0.1]},
        "Trend" : {"anomaly_factor":[2,3], "n_consecutive": [0.07,0.1,0.11]},
        "Variance" : {"n_consecutive": [0.07,0.1,0.11]},
        "FlatLine" : {"n_consecutive": [0.07,0.09,0.1]}
    }


def get_cv_based_on_type(
    data,
    fold_type="Point",
    anomaly_type="Extreme",
    n_iteration=5,
    random_state=None,
    columns_to_ignore=None,
    anomaly_size=0.01,
):
    """_summary_

    Args:
        fold_type (str, optional): _description_. Defaults to 'Point'.
        anomaly_type (str, optional): _description_. Defaults to 'Extreme'.
        n_iteration (int, optional): _description_. Defaults to 10.
        random_state:
        columns_to_ignore: ignore time column
        anomaly_size: percentage of the data to be updated
    """
    tslogger.info(
        "== Perform %d times of %s cross validation for anomaly type: %s "
        % (n_iteration, fold_type, anomaly_type)
    )

    if len(data[1]) < 10 :
        raise ValueError(
            f"To generate anomalous for validation, the holdout data size : ({len(data[1])}) should be more than 9 data points."
        )
    
    params = get_anomaly_parameters()
    
    tslogger.info(f"\tIgnoring these columns {columns_to_ignore}")
    
    if fold_type == "Point" and anomaly_type == "LocalizedExtreme":
        return LocalizedExtremeOutlier(
            n_iteration=n_iteration,
            random_state=random_state,
            columns_to_ignore=columns_to_ignore,
            anomaly_size=anomaly_size,
            anomaly_factor=params[anomaly_type]["anomaly_factor"][0]
        )
    elif fold_type == "Segment" and anomaly_type == "LevelShift":
        return LevelShiftOutlier(
            n_iteration=n_iteration,
            random_state=random_state,
            columns_to_ignore=columns_to_ignore,
            anomaly_size=anomaly_size,
            anomaly_factor=params[anomaly_type]["anomaly_factor"][0]
        )
    elif fold_type == "Segment" and anomaly_type == "Variance":
        return VarianceOutlier(
            n_iteration=n_iteration,
            random_state=random_state,
            columns_to_ignore=columns_to_ignore,
            anomaly_size=anomaly_size,
            n_consecutive=math.ceil(len(data[1])*params[anomaly_type]["n_consecutive"][2])
        )
    elif fold_type == "Segment" and anomaly_type == "Trend":
        return TrendOutlier(
            n_iteration=n_iteration,
            random_state=random_state,
            columns_to_ignore=columns_to_ignore,
            anomaly_size=anomaly_size,
            anomaly_factor=params[anomaly_type]["anomaly_factor"][0],
            n_consecutive=math.ceil(len(data[1])*params[anomaly_type]["n_consecutive"][2])
        )
    else:
        raise ValueError(
            f"Unsupported cross-validation type {fold_type} {anomaly_type}"
        )


def recommend_cv(data, mode="default", **kwargs):
    """Return a list of anomaly generators used in the pipeline ranking process. The
    list returned depends on the provided mode.

    Args:
        data (nd.array): Training data, may be used to determine parameters or 
            recommend anomaly types
        mode (str, optional): Mode to use when recommending the list of anomaly 
            generators. Possible values and their descriptions are provided below.
            Defaults to "default".
            "default": All available anomaly generators
            "intelligent": Future placeholder for identifying good candidate anomaly
                generators based on inspection of the data.
            "empirical": Recommended set based on extensive experimentation.
        kwargs: additional keyword arguments pass to get_cv_based_on_type.

    Raises:
        ValueError: _description_
    """
    cv_list = []
    if mode == "default":
        for anom in SYNTHESIZED_ANOMALY:
            try:
                cv = get_cv_based_on_type(
                data, fold_type=anom["pattern"], anomaly_type=anom["type"], **kwargs
                )
                cv_list.append(cv)
            except ValueError:
                pass
        return cv_list
    elif mode == "intelligent":
        raise NotImplementedError(
            "The `intelligent` recommendation mode is not yet implemented."
        )
    elif mode == "empirical":
        # to be updated with a smaller list based on experiments
        for anom in SYNTHESIZED_ANOMALY:
            try:
                cv = get_cv_based_on_type(
                data, fold_type=anom["pattern"], anomaly_type=anom["type"], **kwargs
                )
                cv_list.append(cv)
            except ValueError:
                pass
        return cv_list
    else:
        raise ValueError(f"Unknown mode: {mode}")
