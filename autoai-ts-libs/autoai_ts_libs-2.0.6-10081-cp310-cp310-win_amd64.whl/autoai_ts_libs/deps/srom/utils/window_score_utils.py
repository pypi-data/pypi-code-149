# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


""" A utility file ; scoring utility """
import math
import numpy as np


def get_window_accuracy(predicted, ground_truth, window):
    """
    Get the Accuracy :
    Args:
        predicted: list of prediction
        ground_truth: list of ground truth
        window: the length of window for testing
    """
    predicted_index = [i for i, e in enumerate(predicted) if e == 1]
    ground_truth_index = [i for i, e in enumerate(ground_truth) if e == 1]

    range_window_ground_truth = []
    for i, _ in enumerate(ground_truth_index):
        range_ground_truth_index = list(
            range(max(ground_truth_index[i] - window, 0), ground_truth_index[i] + 1)
        )
        range_window_ground_truth = list(
            set(range_window_ground_truth) | set(range_ground_truth_index)
        )

    range_window_predicted = []
    for i, _ in enumerate(predicted_index):
        range_predicted_index = list(
            range(
                predicted_index[i], min(predicted_index[i] + window + 1, len(predicted))
            )
        )
        range_window_predicted = list(
            set(range_window_predicted) | set(range_predicted_index)
        )

    num1 = len(list(set(range_window_ground_truth) & set(range_window_predicted)))
    num2 = len(list(set(range_window_ground_truth) | set(range_window_predicted)))

    if num2 == 0:
        return np.NaN

    accuracy = num1 * 1.0 / num2
    return accuracy


def get_window_precision(predicted, ground_truth, window):
    """
    Get the Precision :
    Args:
        predicted: list of prediction
        ground_truth: list of ground truth
        window: the length of window for testing
    """

    predicted_index = [i for i, e in enumerate(predicted) if e == 1]
    if not predicted_index:
        return np.NaN
    ground_truth_index = [i for i, e in enumerate(ground_truth) if e == 1]

    range_window_ground_truth = []
    for i, _ in enumerate(ground_truth_index):
        range_ground_truth_index = list(
            range(max(ground_truth_index[i] - window, 0), ground_truth_index[i] + 1)
        )
        range_window_ground_truth = list(
            set(range_window_ground_truth) | set(range_ground_truth_index)
        )

    precision_list = list(set(predicted_index) & set(range_window_ground_truth))
    precision_score = 1.0 * len(precision_list) / len(predicted_index)

    return precision_score


def get_window_recall(predicted, ground_truth, window):
    """
    Get the Recall :
    Args:
        predicted: list of prediction
        ground_truth: list of ground truth
        window: the length of window for testing
    """
    predicted_index = [i for i, e in enumerate(predicted) if e == 1]
    ground_truth_index = [i for i, e in enumerate(ground_truth) if e == 1]

    if not ground_truth_index:
        return np.NaN

    range_window_predicted = []
    for i, _ in enumerate(predicted_index):
        range_predicted_index = list(
            range(
                predicted_index[i], min(predicted_index[i] + window + 1, len(predicted))
            )
        )
        range_window_predicted = list(
            set(range_window_predicted) | set(range_predicted_index)
        )

    recall_list = list(set(ground_truth_index) & set(range_window_predicted))
    recall_score = 1.0 * len(recall_list) / len(ground_truth_index)
    return recall_score


def get_window_f1_score(predicted, ground_truth, window):
    """
    Get the f1 score :
    Args:
        predicted: list of prediction
        ground_truth: list of ground truth
        window: the length of window for testing
    """
    precision = get_window_precision(predicted, ground_truth, window)
    recall = get_window_recall(predicted, ground_truth, window)
    f1_score = np.NaN
    if (precision + recall) > 0:
        f1_score = 2.0 * (precision * recall) / (precision + recall)
    elif (precision + recall) == 0 or precision == 0 or recall == 0:
        f1_score = 0
    return f1_score


def get_missed_failures(predicted, ground_truth, window):
    """
    Internal Helper function to get the failures that are missed
    """
    predicted_index = [i for i, e in enumerate(predicted) if e == 1]
    ground_truth_index = [i for i, e in enumerate(ground_truth) if e == 1]

    final_range_window_ground_truth = []
    for i, _ in enumerate(ground_truth_index):
        range_ground_truth_index = list(
            range(
                max(ground_truth_index[i] - window, 0),
                min(ground_truth_index[i] + window + 1, len(ground_truth)),
            )
        )
        range_window_ground_truth = list(
            set(predicted_index) & set(range_ground_truth_index)
        )
        if not range_window_ground_truth:
            final_range_window_ground_truth.append(ground_truth_index[i])

    return list(set(final_range_window_ground_truth))


def get_change_point_weight(predicted, ground_truth, window):
    """
    Internal Helper function to detect the weight
    """
    predicted_index = [i for i, e in enumerate(predicted) if e == 1]
    ground_truth_index = [i for i, e in enumerate(ground_truth) if e == 1]

    # eliminate the some of the predicted index that maps to same failures.
    eliminated_change_point = []
    for i, _ in enumerate(ground_truth_index):
        range_ground_truth_index = list(
            range(max(ground_truth_index[i] - window, 0), ground_truth_index[i] + 1)
        )
        range_window_ground_truth = list(
            set(predicted_index) & set(range_ground_truth_index)
        )
        if len(range_window_ground_truth) > 1:
            ignore_first_change = min(range_window_ground_truth)
            for item in range_window_ground_truth:
                if item != ignore_first_change:
                    eliminated_change_point.append(item)

    forward_weight = []
    for i, _ in enumerate(predicted_index):
        range_predicted_index = list(
            range(
                predicted_index[i], min(predicted_index[i] + window + 1, len(predicted))
            )
        )
        range_window_truth = list(set(ground_truth_index) & set(range_predicted_index))
        if range_window_truth:
            forward_weight.append(min(range_window_truth))
        else:
            forward_weight.append(np.NaN)

    backward_weight = []
    for i, _ in enumerate(predicted_index):
        range_predicted_index = list(
            range(max(predicted_index[i] - window, 0), predicted_index[i] + 1)
        )
        range_window_truth = list(set(ground_truth_index) & set(range_predicted_index))
        if range_window_truth:
            backward_weight.append(min(range_window_truth))
        else:
            backward_weight.append(np.NaN)

    weight_contribution = []
    for i, _ in enumerate(predicted_index):
        if predicted_index[i] not in eliminated_change_point:
            if np.isnan(forward_weight[i]):
                if not np.isnan(backward_weight[i]):
                    x = backward_weight[i] - predicted_index[i]
                    weight_contribution.append(2.0 * (1.0 / (1.0 + math.exp(-x))) - 1.0)
                else:
                    weight_contribution.append(np.NaN)
            else:
                x = forward_weight[i] - predicted_index[i]
                weight_contribution.append(2.0 * (1.0 / (1.0 + math.exp(-x))) - 1.0)
        else:
            weight_contribution.append(np.NaN)
    return weight_contribution


def anomaly_score(predicted, ground_truth, window, false_negative_importance=0.1):
    """
    Get the Anomaly Score :
    Args:
        predicted: list of prediction
        ground_truth: list of ground truth
        window: the length of window for testing
        false_negative_importance: as name suggests, value between 0-1
    """
    influence_score = get_change_point_weight(predicted, ground_truth, window)
    missed_failure = get_missed_failures(predicted, ground_truth, window)
    average_score = np.nansum(influence_score) + (
        len(missed_failure) * (-1) * false_negative_importance
    )
    return average_score
