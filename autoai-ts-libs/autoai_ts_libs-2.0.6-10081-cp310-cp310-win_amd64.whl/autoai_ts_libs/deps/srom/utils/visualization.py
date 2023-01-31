# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import itertools
import numpy as np


def plot_confusion_matrix(cm, classes, title="Confusion matrix", cmap=None):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    import matplotlib.pyplot as plt

    if not cmap:
        cmap = plt.cm.Blues

    # Normalized Confusion Matrix
    cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 7))

    img = ax1.imshow(cm, interpolation="nearest", cmap=cmap)
    ax1.set_title("Confusion matrix, without normalization")
    plt.colorbar(img, ax=ax1, fraction=0.046, pad=0.04)
    tick_marks = np.arange(len(classes))
    ax1.set_xticks(tick_marks)
    ax1.set_xticklabels(classes)
    ax1.set_yticks(tick_marks)
    ax1.set_yticklabels(classes)
    plt.setp(ax1.get_xticklabels(), rotation=-45)

    fmt = "d"
    thresh = cm.max() / 2.0
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        ax1.text(
            j,
            i,
            format(cm[i, j], fmt),
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black",
        )

    ax1.set_ylabel("True label")
    ax1.set_xlabel("Predicted label")

    img = ax2.imshow(cm_norm, interpolation="nearest", cmap=cmap)
    ax2.set_title("Normalized confusion matrix")
    plt.colorbar(img, ax=ax2, fraction=0.046, pad=0.04)

    tick_marks = np.arange(len(classes))
    ax2.set_xticks(tick_marks)
    ax2.set_xticklabels(classes)
    ax2.set_yticks(tick_marks)
    ax2.set_yticklabels(classes)
    plt.setp(ax2.get_xticklabels(), rotation=-45)

    fmt = ".2f"
    thresh = cm_norm.max() / 2.0
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        ax2.text(
            j,
            i,
            format(cm_norm[i, j], fmt),
            horizontalalignment="center",
            color="white" if cm_norm[i, j] > thresh else "black",
        )

    ax2.set_ylabel("True label")
    ax2.set_xlabel("Predicted label")

    plt.tight_layout()


def plot_ts_train_test(
    train_time,
    y_train,
    y_pred_train=[],
    test_time=[],
    y_test=[],
    y_pred_test=[],
    pred_col="red",
    org_col="black",
    divide_col="orange",
    title="Timeseries Plot",
    ylabel="Feature",
):
    import matplotlib.pyplot as plt

    # making sure these arrays are iterable
    train_time = list(train_time)
    y_train = list(y_train)
    y_pred_train = list(y_pred_train)
    test_time = list(test_time)
    y_test = list(y_test)
    y_pred_test = list(y_pred_test)

    plt.figure(figsize=(20, 3))

    # by default, one plot is added
    plt.plot(train_time, y_train, c=org_col)

    # plotting predicted part in train
    if y_pred_train:
        plt.plot(train_time, y_pred_train, c=pred_col)

    # plotting ground truth in test
    if test_time and y_test:
        plt.plot(test_time, y_test, c=org_col)

    # plotting predicted in test
    if test_time and y_pred_test:
        plt.plot(test_time, y_pred_test, c=pred_col)

    # plotting the orange line to split train and test
    if test_time:

        all_points = (
            list(y_train) + list(y_pred_train) + list(y_test) + list(y_pred_test)
        )
        max_val = max(all_points)
        min_val = min(all_points)
        plot_height = list(np.linspace(max_val, min_val).ravel())

        train_partition_array = [max(train_time) for i in plot_height]
        plt.plot(train_partition_array, plot_height, c=divide_col)

    # Add title
    plt.title(title)

    plt.xlabel("Distribution over time")
    plt.ylabel(ylabel)
    t = len(train_time + test_time)
    plt.xticks(
        [
            v
            for i, v in enumerate(train_time + test_time)
            if i in range(0, t, int(t / 5))
        ]
    )
