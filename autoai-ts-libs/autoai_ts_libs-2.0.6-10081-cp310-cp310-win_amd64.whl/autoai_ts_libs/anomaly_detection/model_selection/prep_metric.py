import numpy as np

from autoai_ts_libs.deps.srom.anomaly_detection.metrics import (
    f1_score_with_time_column,
    accuracy_score_with_time_column,
    balanced_accuracy_score_with_time_column,
    precision_score_with_time_column,
    recall_score_with_time_column,
    roc_auc_score_with_time_column,
)
from sklearn.metrics import (
    make_scorer,
    f1_score,
    precision_score,
    recall_score,
    accuracy_score,
    balanced_accuracy_score,
    roc_auc_score,
    average_precision_score,
)

from autoai_ts_libs.anomaly_detection.utils.metrics import (
    score_with_time_column,
    get_pa_metric,
    pr_auc_score,
)

from autoai_ts_libs.anomaly_detection.estimators.constants import ANOMALY, NON_ANOMALY

def get_scorer_(
    scoring="f1", time_column=None,
):
    if time_column is not None and time_column != -1:
        if scoring == "f1":
            return make_scorer(f1_score_with_time_column, time_column=time_column)
        elif scoring == "f1_pa":
            return make_scorer(
                score_with_time_column(
                    get_pa_metric(f1_score, K=0.2), time_column=time_column
                ),
                pos_label=ANOMALY,
            )
        elif scoring == "accuracy":
            return make_scorer(accuracy_score_with_time_column, time_column=time_column)
        elif scoring == "balanced_accuracy":
            return make_scorer(
                balanced_accuracy_score_with_time_column, time_column=time_column
            )
        elif scoring == "precision":
            return make_scorer(
                precision_score_with_time_column, time_column=time_column
            )
        elif scoring == "recall":
            return make_scorer(recall_score_with_time_column, time_column=time_column)
        elif scoring == "roc_auc":
            return make_scorer(
                roc_auc_score_with_time_column,
                needs_threshold=True,
                time_column=time_column,
            )
        elif scoring == "average_precision":
            return make_scorer(
                score_with_time_column(
                    average_precision_score, time_column=time_column,
                ),
                needs_threshold=True,
            )
        elif scoring == "pr_auc":
            return make_scorer(
                score_with_time_column(pr_auc_score, time_column=time_column,),
                needs_threshold=True,
            )
        else:
            raise ValueError(f"Scoring method {scoring} not supported.")
    else:
        if scoring == "f1":
            return make_scorer(f1_score, pos_label=ANOMALY)
        elif scoring == "f1_macro":
            return make_scorer(f1_score, pos_label=ANOMALY, average="macro")
        elif scoring == "f1_micro":
            return make_scorer(f1_score, pos_label=ANOMALY, average="micro")
        elif scoring == "f1_weighted":
            return make_scorer(f1_score, pos_label=ANOMALY, average="weighted")
        elif scoring == "f1_pa":
            return make_scorer(get_pa_metric(f1_score, K=0.2), pos_label=ANOMALY)
        elif scoring == "precision":
            return make_scorer(precision_score, pos_label=ANOMALY)
        elif scoring == "recall":
            return make_scorer(recall_score, pos_label=ANOMALY)
        elif scoring == "accuracy":
            return make_scorer(accuracy_score)
        elif scoring == "balanced_accuracy":
            return make_scorer(balanced_accuracy_score)
        elif scoring == "roc_auc":
            return make_scorer(roc_auc_score, needs_threshold=True)
        elif scoring == "average_precision":
            return make_scorer(
                average_precision_score, needs_threshold=True, pos_label=ANOMALY
            )
        elif scoring == "pr_auc":
            return make_scorer(pr_auc_score, needs_threshold=True, pos_label=ANOMALY)
        else:
            raise ValueError(f"Scoring method {scoring} not supported.")

