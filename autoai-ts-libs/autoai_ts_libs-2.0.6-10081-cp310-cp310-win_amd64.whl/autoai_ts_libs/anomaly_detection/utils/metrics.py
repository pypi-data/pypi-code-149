from typing import Tuple, Optional, Callable

import numpy as np

from autoai_ts_libs.anomaly_detection.estimators.constants import ANOMALY, NON_ANOMALY
from sklearn.metrics import auc, precision_recall_curve


def point_adjustment(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    threshold: Optional[float] = None,
    K: float = 0,
):
    """Perform the point adjustment procedure according to: 

    Kim, Siwon, Kukjin Choi, Hyun-Soo Choi, Byunghan Lee, and Sungroh Yoon. 
    "Towards a rigorous evaluation of time-series anomaly detection." In 
    Proceedings of the AAAI Conference on Artificial Intelligence, vol. 36, 
    no. 7, pp. 7194-7201. 2022.

    https://arxiv.org/abs/2109.05257

    Essentially adjusts predicted labels such that if we correctly label a point in an
    anomaly window we get all points in that window correctly labeled.

    Args:
        y_true (np.ndarray): Ground truth values of anomalies 
        y_pred (np.ndarray): Predicted anomalies or scores
        threshold (float, optional): If provided, used to threshold y_pred to create labels. 
            Defaults to None.
        K (float): Set this to a value in [0, 1] for PA%K functionality. Defaults to 0. 
            Original PA method.


    If threshold is None, then assume y_pred contains predicted labels. Otherwise threshold is 
    used to deterrmine labels assuming y_pred is the output score (non-negative, larger means more 
    anomalous)

    Assumes y_true, y_pred are column vectors (i.e., shape is length 2, with the shape of second dimension equal to 1)
    """
    debug = False

    if threshold is not None:
        labels = np.where(y_pred > threshold, ANOMALY, NON_ANOMALY)
    else:
        labels = y_pred

    y_adjusted = np.zeros_like(y_pred)

    assert (
        y_pred.shape == y_true.shape
    ), "Expecting y_true and y_pred to have identical shape"

    assert (
        len(y_pred.shape) == 2 and y_pred.shape[1] == 1
    ), "Expecting y_true input to have a second dimension of length one"

    # get anomaly periods
    anomaly_start, anomaly_end = get_anomaly_periods(y_true)

    if debug:
        print("Input", y_true, y_pred)
        print("Anomaly start:", anomaly_start)
        print("Anomaly end:", anomaly_end)
    num_anomalies = len(anomaly_start)

    j = 0  # anomaly period counter
    for i in range(y_pred.shape[0]):
        # advance to the next anomaly
        while (j < num_anomalies) and (anomaly_end[j] < i):
            j += 1

        # adjust index i
        if y_pred[i] == ANOMALY:
            y_adjusted[i] = ANOMALY
        elif (
            (j < num_anomalies)
            and (anomaly_start[j] <= i)
            and (i <= anomaly_end[j])
            and (
                np.sum(y_pred[anomaly_start[j] : anomaly_end[j] + 1] == ANOMALY)
                / (anomaly_end[j] - anomaly_start[j] + 1)
                > K
            )
        ):
            # if there is an anomaly window containing i, and we declared an anomaly anywhere
            # in this window, then set i to ANOMALY
            y_adjusted[i] = ANOMALY
        else:
            y_adjusted[i] = NON_ANOMALY

    return y_adjusted


def get_anomaly_periods(y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Returns the start and end indices for anomalous periods.

    Args:
        y (np.ndarray): Anomaly label data
    Returns:
        Tuple[np.ndarray, np.ndarray]: Tuple of two nd.arrays, the first indicates
            the start of the anomalies, the second indicates the end, they should 
            be identical lengths.
            The indices are inclusive of the anomaly periods.

    > get_anomaly_periods([-1, 1, -1, -1, 1])
        (array([0, 2]), array([0, 3]))

    > get_anomaly_periods([1, 1, -1, -1, 1])
        (array([2]), array([3]))

    > get_anomaly_periods([-1, -1, -1, -1, -1])
        (array([0]), array([4]))
    """

    if len(y.shape) > 1 and y.shape[1] > 1:
        raise ValueError(
            "Input should be 1-dimensional or 2-dimension with second dimension of size 1."
        )

    if len(y.shape) > 1:
        y_ = y[:, 0]
    else:
        y_ = y

    y_true_diff = np.diff(y_)
    anomaly_start = np.where(y_true_diff == (ANOMALY - NON_ANOMALY))[0] + 1
    anomaly_end = np.where(y_true_diff == (NON_ANOMALY - ANOMALY))[0]
    if y_[0] == ANOMALY:
        anomaly_start = np.hstack(([0], anomaly_start))
    if y_[-1] == ANOMALY:
        anomaly_end = np.hstack(([anomaly_end, len(y) - 1]))

    return anomaly_start, anomaly_end


def get_pa_metric(metric: Callable, **pa_kwargs) -> Callable:
    """Convenience function to return a new metric function which first applies 
    the point adjustment procedure to the y_pred data.

    Args:
        metric (Callable): A metric function, e.g., f1_score

    Returns:
        Callable: Returns wrapped metric so that the point adjustment mechanism
        is first applied to y_pred
    """

    def _helper(y_true: np.ndarray, y_pred: np.ndarray, **kwargs):
        y_pred_ = point_adjustment(y_true, y_pred, **pa_kwargs)
        return metric(y_true, y_pred_, **kwargs)

    return _helper


def score_with_time_column(score_func: Callable, time_column: int,) -> Callable:
    """ Handle time column when included in input data

    Args:
        y_true (np.ndarray): _description_
        y_pred (np.ndarray): _description_
        time_column (int): index of time column
        score_func (Callable): _description_

    Returns:
        np.ndarray: Score resulting from using score_func on the provided data without the time columns
    """

    def new_score_func(y_true: np.ndarray, y_pred: np.ndarray, **kwargs):
        y_true_ = y_true[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
        y_pred_ = y_pred[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
        return score_func(y_true_, y_pred_, **kwargs)

    return new_score_func


def pr_auc_score(
    y_true: np.ndarray, scores: np.ndarray, pos_label=ANOMALY, **kwargs
) -> float:
    """ Compute PR-AUC using PR curve and AUC in sequence.

    Args:
        y_true (np.ndarray): True labels
        scores (np.ndarray): scores
        pos_label (_type_, optional): The label of the positive class. Defaults to ANOMALY.

    Returns:
        np.ndarray: 
    """
    precision, recall, _ = precision_recall_curve(
        y_true, scores, pos_label=pos_label, **kwargs
    )

    return auc(recall, precision)

