# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: evaluation
   :synopsis: Evaluation of the models obtained from Failure Prediction Analysis pipeline.

.. moduleauthor:: SROM Team
"""
from datetime import timedelta
import logging

LOGGER = logging.getLogger(__name__)

import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.failure_prediction.time_sample import time_sampling, process_time_interval


def FPA_evaluate(
    FPA_result,
    failure_table,
    soft_pred_window_delta,
    topk_list,
    failure_asset_id,
    failure_date,
    pred_window,
):

    """
    Creates a Top K evaluation table from the results obtained by the model. This table gives \
    statistical computation of the performance by the model and will be used later to visualize \
    the results. The statistical values computed are: \
        - Failures recorded in ground truth (P) \
        - Assets failed in Test Data (X) \
        - Size of test data \
        - Expected failure instances in Test data \
        - Top K \
        - Failure prediction we made (A) \
        - Assets model predict that it is going to fail (Y) \
        - Time threshold \
        - Prediction we made are correct (B) \
        - Assets model correctly predict (Z) \
        - Failures our model actually captures? (Q) \
        - Adjusted Failures recorded in ground truth? (P_) \
        Please refer to the Failure Prediction Analysis for more information on the significance \
        of these attributes: \
        https://github.ibm.com/srom/docs/blob/master/workbooks/failure_prediction_analysis/Failure_Prediction_Analysis.ipynb
    
    Parameters:
        FPA_result (pandas dataframe, required): Dataframe containing these attributes- \
                ['asset_id', 'datetime','target_label','prob'] which is returned after training.
        failure_table (pandas dataframe, required): Table having the asset failure information.
        soft_pred_window_delta (int, required): Creates a soft threshold for the prediction window \
                (ignore incorrect classifications by the model within this threshold).
        topk_list (list of integers, required): List with values used to find top k assets. \
        failure_asset_id (string, required): Column name for asset-id in failure data table.
        failure_date (string, required): Column name for date in failure data table.
        pred_window (int, required): The window for labelling assets as failures in target label \
                generation.
    
    Returns:
        Dataframe: Contains the Top K analysis of the results.
    """
    top_k_table = []
    failure_table.rename(columns={failure_asset_id: "asset_id"}, inplace=True)

    # How many failures are recorded in ground truth? (P)
    P = len(failure_table)

    # How many assets failed in Test Data (X)
    X = len(failure_table["asset_id"].unique())

    pred_result_count = len(FPA_result)

    exp_failure = len(FPA_result[FPA_result["target_label"] == 1])

    soft_pred_window_delta = process_time_interval(soft_pred_window_delta)
    pred_window = process_time_interval(pred_window)

    for topk in topk_list:
        p = (
            FPA_result.sort_values(["datetime", "prob"], ascending=False)
            .groupby("datetime")
            .head(topk)
        )

        # A - Since we are making topk predictions everyday, A is the top-k predictions for all days
        # How many failure prediction we made (A)
        A = len(p)

        # Y- How many assets model predict that it is going to fail (Y)
        Y = len(p["asset_id"].unique())

        # the threshold to ignore the incorrect predictions by the model in some duration of target
        # label generation

        time_threshold = [pred_window]

        for i in range(3):
            time_threshold.append(time_threshold[i] + soft_pred_window_delta)

        # looping over different thresholds and getting top k results.
        for time_th in time_threshold:
            if "pandas.tseries.offsets" in str(type(time_th)):
                time_th = time_th.delta
            result_df = pd.merge(p, failure_table, how="left", on=["asset_id"])
            result_df = result_df.loc[
                (
                    pd.to_datetime(result_df[failure_date])
                    - pd.to_datetime(result_df["datetime"])
                    <= time_th
                )
            ]
            result_df = result_df.loc[
                (
                    pd.to_datetime(result_df[failure_date])
                    > pd.to_datetime(result_df["datetime"])
                )
            ]

            # B- How many prediction we made are correct (B)
            B = len(result_df)

            # Z - How many assets model correctly predict (Z)
            Z = len(result_df["asset_id"].unique())

            # Q - How many failures our model actually captures? (Q)
            result_fail_df = (
                result_df.groupby(["asset_id", failure_date])
                .size()
                .reset_index()
                .rename(columns={0: "count"})
            )
            Q = len(result_fail_df)

            # Adjusted analysis: Accounting for missing values in the Sensor data.
            # Insufficient data for prediction.
            result_df = pd.merge(FPA_result, failure_table, how="left", on=["asset_id"])
            result_df = result_df.loc[
                (
                    pd.to_datetime(result_df[failure_date])
                    - pd.to_datetime(result_df["datetime"])
                    <= time_th
                )
            ]
            result_df = result_df.loc[
                (
                    pd.to_datetime(result_df[failure_date])
                    > pd.to_datetime(result_df["datetime"])
                )
            ]

            # distinct_assets_adjusted = len(result_df['asset_id'].unique())

            result_fail_df = (
                result_df.groupby(["asset_id", failure_date])
                .size()
                .reset_index()
                .rename(columns={0: "count"})
            )

            # P1 - How many failures can be actually be captured with the sensor available? (P1)
            P1 = len(result_fail_df)

            top_k_table.append(
                [
                    P,
                    X,
                    pred_result_count,
                    exp_failure,
                    topk,
                    A,
                    Y,
                    str(time_th),
                    B,
                    Z,
                    Q,
                    P1,
                ]
            )

    df = pd.DataFrame(top_k_table)
    df.columns = [
        "Failures recorded in ground truth (P)",
        "Assets failed in Test Data (X)",
        "Size of test data",
        "Expected failure instances in Test data",
        "Top K",
        "Failure prediction we made (A)",
        "Assets model predict that it is going to fail (Y)",
        "Time threshold",
        "Prediction we made are correct (B)",
        "Assets model correctly predict (Z)",
        "Failures our model actually captures? (Q)",
        "Adjusted Failures recorded in ground truth? (P_)",
    ]
    return df


def plot_daily_eval(result_eval, save_png=True, out_file="daily_eval"):
    """
    Plots the results of the models on the basis of Daily evaluation criteria. \
    Prints the results in the Jupiter Notebook as markdown to show a 'Report' format. \
    The results can also be saved as a png.

    Parameters:
        result_eval (dataframe obtained from autoai_ts_libs.deps.srom.failure_prediction.evaluation.FPA_evaluate, required): \
                This table contains the Top K analysis of the model.
        save_png (Boolean, optional): Whether to save the png of the results in working directory or not.
        out_file (string, optional): Name of the save file.
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError as _:
        LOGGER.warning(
            "Cannot import matplotlib.pyplot. Drawing of plots will not be possible."
        )

    try:
        from IPython.display import display, Markdown
    except ImportError:
        print("Please install IPython dependencies to use this module.")

    if out_file is None:
        out_file = "daily_eval"

    display(Markdown("### Prediction based Evaluation"))
    display(
        Markdown(
            "Calculating the model's performance to find how many correct predictions \
    are made out of the total number of predictions made by the model."
        )
    )

    grouped_df = result_eval[
        [
            "Time threshold",
            "Top K",
            "Failure prediction we made (A)",
            "Prediction we made are correct (B)",
        ]
    ].groupby("Time threshold")

    time_th = 0
    for key, item in grouped_df:
        time_th += 1

    try:
        if time_th <= 2:
            f, ax = plt.subplots(
                1, 2, figsize=(13, 5 * (time_th + 1) // 2), sharey=False
            )
    #         if topk == 1:
    #             ax[0, 1].axis('off')
    except:
        raise ValueError("Choose Top K value atleast 2.")

    else:
        f, ax = plt.subplots(
            (time_th + 1) // 2, 2, figsize=(13, 5 * (time_th + 1) // 2), sharey=False
        )
        if time_th % 2 != 0:
            ax[-1, -1].axis("off")
    x = 0
    y = 0

    for key, item in grouped_df:
        # print grouped_df.get_group(key), "\n\n"
        topk = list(map(str, list(grouped_df.get_group(key)["Top K"])))
        topk_acc = [
            round(
                float(
                    list(
                        grouped_df.get_group(key)["Prediction we made are correct (B)"]
                    )[i]
                )
                * 100
                / float(
                    list(grouped_df.get_group(key)["Failure prediction we made (A)"])[i]
                ),
                3,
            )
            for i in range(len(grouped_df.get_group(key)))
        ]
        topk_list = [
            ("Top " + topk[i] + " assets: \n Accuracy= " + str(topk_acc[i]) + "%")
            for i in range(len(topk))
        ]
        # print topk_list
        result = ["Failure prediction (A)", "Correct Predictions (B)"]

        N = len(grouped_df.get_group(key))
        A = [
            (
                list(grouped_df.get_group(key)["Failure prediction we made (A)"])[i]
                - list(grouped_df.get_group(key)["Prediction we made are correct (B)"])[
                    i
                ]
            )
            for i in range(N)
        ]
        B = list(grouped_df.get_group(key)["Prediction we made are correct (B)"])
        ind = np.arange(N)  # the x locations for the groups
        width = 0.85  # the width of the bars: can also be len(x) sequence

        ax[x, y].bar(ind, A, width, color="#D3D3D3")
        ax[x, y].bar(ind, B, width, color="#4682B4", bottom=A)
        plt.sca(ax[x, y])
        plt.ylabel("Prediction count")
        plt.title(str(key) + " days prior Prediction")
        plt.xticks(ind, topk_list)
        plt.yticks(np.arange(0, max(A) + max(B), 1000))
        plt.ylim([0, 1.5 * max(A)])
        l1 = mpatches.Patch(color="#D3D3D3", label="Failure prediction we made (A)")
        l2 = mpatches.Patch(color="#4682B4", label="Prediction we made are correct (B)")
        ax[x, y].legend(loc="upper left", handles=[l1, l2])

        if x == 1:
            y += 1
            x = 0
        else:
            x += 1

        if save_png:
            f.savefig(out_file + "_" + str(key) + ".png")

    plt.show()


def FPA_evaluate_multiclass(
    FPA_result,
    failure_table,
    soft_pred_window_delta,
    topk_list,
    failure_asset_id,
    failure_date,
    failure_id,
    pred_window,
    failid,
):

    """
    Creates a Top K evaluation table from the results obtained by the model. This table gives \
    statistical computation of the performance by the model and will be used later to visualize \
    the results. The statistical values computed are: \
        - Failures recorded in ground truth (P) \
        - Assets failed in Test Data (X) \
        - Size of test data \
        - Expected failure instances in Test data \
        - Top K \
        - Failure prediction we made (A) \
        - Assets model predict that it is going to fail (Y) \
        - Time threshold \
        - Prediction we made are correct (B) \
        - Assets model correctly predict (Z) \
        - Failures our model actually captures? (Q) \
        - Adjusted Failures recorded in ground truth? (P_) \
        Please refer to the Failure Prediction Analysis for more information on the significance \
        of these attributes: \
        https://github.ibm.com/srom/docs/blob/master/workbooks/experimental/failure_prediction/Failure_Prediction_Analysis_Multiclass.ipynb
    
    Parameters:
        FPA_result (pandas dataframe, required): Dataframe containing these attributes- \
                ['asset_id', 'datetime','target_label','prob'] which is returned after training.
        failure_table (pandas dataframe, required): Table having the asset failure information.
        soft_pred_window_delta (int, required): Creates a soft threshold for the prediction window \
                (ignore incorrect classifications by the model within this threshold).
        topk_list (list of integers, required): List with values used to find top k assets.
        failure_asset_id (string, required): Column name for asset-id in failure data table.
        failure_date (string, required): Column name for date in failure data table.
        failure_id (string, required): Column name for column with failure id.
        pred_window (int, required): The window for labelling assets as failures in target label \
                generation.
        failid (int): Failure id of interest.
    Returns:
        Dataframe: Contains the Top K analysis of the results.
    """
    top_k_table = []
    failure_table.rename(columns={failure_asset_id: "asset_id"}, inplace=True)

    # Filter down to failures corresponding to that failure id of interest

    failure_table = failure_table[failure_table[failure_id] == failid]

    # How many failures are recorded in ground truth for this failure id? (P)
    P = len(failure_table)

    # How many assets failed in Test Data (X)
    X = len(failure_table["asset_id"].unique())

    pred_result_count = len(FPA_result)

    # exp_failure has to change
    exp_failure = len(FPA_result[FPA_result["target_label_" + str(failid)] == 1])

    soft_pred_window_delta = process_time_interval(soft_pred_window_delta)
    pred_window = process_time_interval(pred_window)

    for topk in topk_list:
        p = (
            FPA_result.sort_values(["datetime", "prob_" + str(failid)], ascending=False)
            .groupby("datetime")
            .head(topk)
        )

        # A - Since we are making topk predictions everyday, A is the top-k predictions for all days
        # How many failure prediction we made (A)
        A = len(p)

        # Y- How many assets model predict that it is going to fail (Y)
        Y = len(p["asset_id"].unique())

        # the threshold to ignore the incorrect predictions by the model in some duration of target
        # label generation

        time_threshold = [pred_window]

        for i in range(3):
            time_threshold.append(time_threshold[i] + soft_pred_window_delta)

        # looping over different thresholds and getting top k results.
        for time_th in time_threshold:
            if "pandas.tseries.offsets" in str(type(time_th)):
                time_th = time_th.delta
            result_df = pd.merge(p, failure_table, how="left", on=["asset_id"])
            result_df = result_df.loc[
                (
                    pd.to_datetime(result_df[failure_date])
                    - pd.to_datetime(result_df["datetime"])
                    <= time_th
                )
            ]
            result_df = result_df.loc[
                (
                    pd.to_datetime(result_df[failure_date])
                    > pd.to_datetime(result_df["datetime"])
                )
            ]

            # B- How many prediction we made are correct (B)
            B = len(result_df)

            # Z - How many assets model correctly predict (Z)
            Z = len(result_df["asset_id"].unique())

            # Q - How many failures our model actually captures? (Q)
            result_fail_df = (
                result_df.groupby(["asset_id", failure_date])
                .size()
                .reset_index()
                .rename(columns={0: "count"})
            )
            Q = len(result_fail_df)

            # Adjusted analysis: Accounting for missing values in the Sensor data.
            # Insufficient data for prediction.
            result_df = pd.merge(FPA_result, failure_table, how="left", on=["asset_id"])
            result_df = result_df.loc[
                (
                    pd.to_datetime(result_df[failure_date])
                    - pd.to_datetime(result_df["datetime"])
                    <= time_th
                )
            ]
            result_df = result_df.loc[
                (
                    pd.to_datetime(result_df[failure_date])
                    > pd.to_datetime(result_df["datetime"])
                )
            ]

            # distinct_assets_adjusted = len(result_df['asset_id'].unique())

            result_fail_df = (
                result_df.groupby(["asset_id", failure_date])
                .size()
                .reset_index()
                .rename(columns={0: "count"})
            )

            # P1 - How many failures can be actually be captured with the sensor available? (P1)
            P1 = len(result_fail_df)

            top_k_table.append(
                [
                    P,
                    X,
                    pred_result_count,
                    exp_failure,
                    topk,
                    A,
                    Y,
                    str(time_th),
                    B,
                    Z,
                    Q,
                    P1,
                ]
            )

    df = pd.DataFrame(top_k_table)
    df.columns = [
        "Failures recorded in ground truth (P)",
        "Assets failed in Test Data (X)",
        "Size of test data",
        "Expected failure instances in Test data",
        "Top K",
        "Failure prediction we made (A)",
        "Assets model predict that it is going to fail (Y)",
        "Time threshold",
        "Prediction we made are correct (B)",
        "Assets model correctly predict (Z)",
        "Failures our model actually captures? (Q)",
        "Adjusted Failures recorded in ground truth? (P_)",
    ]
    return df


def plot_asset_eval(result_eval, save_png=True, out_file=None):
    """
    Plots the results of the models on the basis of Asset evaluation criteria. \
    Prints the results in the Jupiter Notebook as markdown to show a 'Report' format. \
    The results can also be saved as a png.

    Parameters:
        result_eval ( dataframe obtained from autoai_ts_libs.deps.srom.failure_prediction.evaluation.FPA_evaluate, required): \
                This table contains the Top K analysis of the model.
        save_png (Boolean, optional): Whether to save the png of the results in working directory or not.
        out_file (string, optional): Name of the save file.
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError as _:
        LOGGER.warning(
            "Cannot import matplotlib.pyplot. Drawing of plots will not be possible."
        )

    try:
        from IPython.display import display, Markdown
    except ImportError:
        print("Please install IPython dependencies to use this module.")

    if out_file is None:
        out_file = "asset_eval"

    display(Markdown("### Asset based Evaluation"))
    display(
        Markdown(
            "Evaluating the accuracy of the model based on number of correctly \
    identified failed assets. By 'identifying failed assets', we mean that unique identification \
    of failing assets during the test duration."
        )
    )

    grouped_df = result_eval[
        [
            "Time threshold",
            "Top K",
            "Assets failed in Test Data (X)",
            "Assets model predict that it is going to fail (Y)",
            "Assets model correctly predict (Z)",
        ]
    ].groupby("Time threshold")

    for key, item in grouped_df:
        N = len(grouped_df.get_group(key))
        topk = list(map(str, list(grouped_df.get_group(key)["Top K"])))
        topk_pre = [
            round(
                float(
                    list(
                        grouped_df.get_group(key)["Assets model correctly predict (Z)"]
                    )[i]
                )
                / float(
                    list(
                        grouped_df.get_group(key)[
                            "Assets model predict that it is going to fail (Y)"
                        ]
                    )[i]
                ),
                3,
            )
            for i in range(N)
        ]
        topk_rec = [
            round(
                float(
                    list(
                        grouped_df.get_group(key)["Assets model correctly predict (Z)"]
                    )[i]
                )
                / float(
                    list(grouped_df.get_group(key)["Assets failed in Test Data (X)"])[i]
                ),
                3,
            )
            for i in range(N)
        ]
        topk_list_pre = [
            ("Top " + topk[i] + " assets: \n Precision= " + str(topk_pre[i]))
            for i in range(len(topk))
        ]
        topk_list_rec = [
            ("Top " + topk[i] + " assets: \n Recall=" + str(topk_rec[i]))
            for i in range(len(topk))
        ]
        result_pre = [
            "Top " + str(key) + " Predicted Assets (Y)",
            "Assets model correctly predicts (Z)",
        ]
        result_rec = [
            "Assets failed in Test Data (X)",
            "Assets model correctly predicts (Z)",
        ]

        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4), sharey=False)

        # Precision plot
        A = [
            (
                list(
                    grouped_df.get_group(key)[
                        "Assets model predict that it is going to fail (Y)"
                    ]
                )[i]
                - list(grouped_df.get_group(key)["Assets model correctly predict (Z)"])[
                    i
                ]
            )
            for i in range(N)
        ]
        B = list(grouped_df.get_group(key)["Assets model correctly predict (Z)"])
        ind = np.arange(N)  # the x locations for the groups
        width = 0.85  # the width of the bars: can also be len(x) sequence

        ax1.bar(ind, A, width, color="#D3D3D3")
        ax1.bar(ind, B, width, color="#4682B4", bottom=A)
        ax1.set_ylabel("Assets")
        plt.sca(ax1)
        plt.xticks(ind, topk_list_pre)
        plt.yticks(np.arange(0, max(A) + max(B) + 100, 100))
        plt.ylim([0, 1.5 * (max(A) + max(B))])

        l1 = mpatches.Patch(color="#D3D3D3", label="Predicted Assets (Y)")
        l2 = mpatches.Patch(
            color="#4682B4", label="Assets model correctly predicts (Z)"
        )
        ax1.legend(loc="upper left", handles=[l1, l2])
        ax1.set_title("Precision")

        # Recall plot
        A = [
            (
                list(grouped_df.get_group(key)["Assets failed in Test Data (X)"])[i]
                - list(grouped_df.get_group(key)["Assets model correctly predict (Z)"])[
                    i
                ]
            )
            for i in range(N)
        ]
        B = list(grouped_df.get_group(key)["Assets model correctly predict (Z)"])
        ind = np.arange(N)  # the x locations for the groups
        width = 0.85  # the width of the bars: can also be len(x) sequence

        ax2.bar(ind, A, width, color="#D3D3D3")
        ax2.bar(ind, B, width, color="#e84d60", bottom=A)
        ax2.set_ylabel("Assets")
        plt.sca(ax2)
        plt.xticks(ind, topk_list_rec)
        plt.yticks(np.arange(0, max(A) + max(B), 100))
        plt.ylim([0, (max(A) + max(B))])
        l1 = mpatches.Patch(color="#D3D3D3", label="Assets failed in Test Data (X)")
        l2 = mpatches.Patch(
            color="#e84d60", label="Assets model correctly predicts (Z)"
        )
        ax2.legend(loc="upper left", handles=[l1, l2])
        ax2.set_title("Recall")

        display(Markdown("#### " + str(key) + " days prediction"))
        plt.show()
        if save_png:
            f.savefig(out_file + "_" + str(key) + ".png")


def plot_failure_eval(result_eval, save_png=True, out_file=None):
    """
    Plots the results of the models on the basis of Failure evaluation criteria. \
    Prints the results in the Jupiter Notebook as markdown to show a 'Report' format. \
    The results can also be saved as a png.

    Parameters:
        result_eval ( dataframe obtained from autoai_ts_libs.deps.srom.failure_prediction.evaluation.FPA_evaluate, required): \
        This table contains the Top K analysis of the model.
        save_png (Boolean, optional): Whether to save the png of the results in working directory or not.
        out_file (string, optional): Name of the save file.
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError as _:
        LOGGER.warning(
            "Cannot import matplotlib.pyplot. Drawing of plots will not be possible."
        )

    try:
        from IPython.display import display, Markdown
    except ImportError:
        print("Please install IPython dependencies to use this module.")

    if out_file is None:
        out_file = "failure_eval"

    display(Markdown("### Failure level Evaluation"))
    display(
        Markdown(
            " Evaluating the model's performance based on accuracy of total number of predicted failures. \
    That is, how many failures are we actually capturing even if an asset fails more than once in the test period."
        )
    )

    grouped_df = result_eval[
        [
            "Time threshold",
            "Top K",
            "Failures recorded in ground truth (P)",
            "Failures our model actually captures? (Q)",
            "Adjusted Failures recorded in ground truth? (P_)",
        ]
    ].groupby("Time threshold")

    for key, item in grouped_df:
        N = len(grouped_df.get_group(key))
        topk = list(map(str, list(grouped_df.get_group(key)["Top K"])))
        topk_ = [
            round(
                float(
                    list(
                        grouped_df.get_group(key)[
                            "Failures our model actually captures? (Q)"
                        ]
                    )[i]
                )
                / float(
                    list(
                        grouped_df.get_group(key)[
                            "Failures recorded in ground truth (P)"
                        ]
                    )[i]
                ),
                3,
            )
            for i in range(N)
        ]
        topk_adj = [
            round(
                float(
                    list(
                        grouped_df.get_group(key)[
                            "Failures our model actually captures? (Q)"
                        ]
                    )[i]
                )
                / float(
                    list(
                        grouped_df.get_group(key)[
                            "Adjusted Failures recorded in ground truth? (P_)"
                        ]
                    )[i]
                ),
                3,
            )
            for i in range(N)
        ]
        topk_list = [
            (
                "Top "
                + topk[i]
                + " assets: \n \
                    Recall= "
                + str(topk_[i])
            )
            for i in range(len(topk))
        ]
        topk_list_adj = [
            (
                "Top "
                + topk[i]
                + " assets: \n\
                         Adj Recall="
                + str(topk_adj[i])
            )
            for i in range(len(topk))
        ]

        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4), sharey=False)

        # Precision plot
        A = [
            (
                list(
                    grouped_df.get_group(key)["Failures recorded in ground truth (P)"]
                )[i]
                - list(
                    grouped_df.get_group(key)[
                        "Failures our model actually captures? (Q)"
                    ]
                )[i]
            )
            for i in range(N)
        ]
        B = list(grouped_df.get_group(key)["Failures our model actually captures? (Q)"])
        ind = np.arange(N)  # the x locations for the groups
        width = 0.85  # the width of the bars: can also be len(x) sequence

        ax1.bar(ind, A, width, color="#D3D3D3")
        ax1.bar(ind, B, width, color="#4682B4", bottom=A)
        ax1.set_ylabel("Failure count")
        plt.sca(ax1)
        plt.xticks(ind, topk_list)
        plt.yticks(np.arange(0, max(A) + max(B) + 100, 100))
        plt.ylim([0, 1.5 * (max(A) + max(B))])
        l1 = mpatches.Patch(
            color="#D3D3D3", label="Failures recorded in ground truth (P)"
        )
        l2 = mpatches.Patch(color="#4682B4", label="Failures actually captured(Q)")
        ax1.legend(loc="upper left", handles=[l1, l2])
        ax1.set_title("Failure Recall")

        # Recall plot
        A = [
            (
                list(
                    grouped_df.get_group(key)[
                        "Adjusted Failures recorded in ground truth? (P_)"
                    ]
                )[i]
                - list(
                    grouped_df.get_group(key)[
                        "Failures our model actually captures? (Q)"
                    ]
                )[i]
            )
            for i in range(N)
        ]
        B = list(grouped_df.get_group(key)["Failures our model actually captures? (Q)"])
        ind = np.arange(N)  # the x locations for the groups
        width = 0.85  # the width of the bars: can also be len(x) sequence

        ax2.bar(ind, A, width, color="#D3D3D3")
        ax2.bar(ind, B, width, color="#e84d60", bottom=A)
        ax2.set_ylabel("Failure count")
        plt.sca(ax2)
        plt.xticks(ind, topk_list_adj)
        plt.yticks(np.arange(0, max(A) + max(B), 10))
        plt.ylim([0, (max(A) + max(B))])

        l1 = mpatches.Patch(
            color="#D3D3D3", label="Adjusted Failures recorded in ground truth (P_)"
        )
        l2 = mpatches.Patch(color="#e84d60", label="Failures actually captured(Q)")
        ax2.legend(loc="upper left", handles=[l1, l2])
        ax2.set_title("Adjusted Failure Recall")

        display(Markdown("####  " + str(key) + " days prediction"))
        plt.show()
        if save_png:
            f.savefig(out_file + "_" + str(key) + ".png")


def plot_eval(result_eval, plot_type=all, save_png=True, out_file=None):
    """
    Plots the results of the models on the basis of Daily, Asset or Failure evaluation criteria. \
    Prints the results in the Jupiter Notebook as markdown to show a 'Report' format. \
    The results can also be saved as a png.
    
    Parameters:
        result_eval (dataframe obtained from autoai_ts_libs.deps.srom.failure_prediction.evaluation.FPA_evaluate, required): \
                    This table contains the Top K analysis of the model.
        plot_type (string, required): String to call a certain type of evaluation plot. \
                    types - ['all','daily','asset','failure']; default: 'all'.
        save_png (Boolean, optional): Whether to save the png of the results in working directory or not.
        out_file (string, optional): Name of the save file.
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError as _:
        LOGGER.warning(
            "Cannot import matplotlib.pyplot. Drawing of plots will not be possible."
        )

    try:
        from IPython.display import display, Markdown
    except ImportError:
        print("Please install IPython dependencies to use this module.")

    if plot_type == "daily":
        plot_daily_eval(result_eval, save_png, out_file)
    elif plot_type == "asset":
        plot_asset_eval(result_eval, save_png, out_file)
    elif plot_type == "failure":
        plot_failure_eval(result_eval, save_png, out_file)
    elif plot_type == "all":
        plot_daily_eval(result_eval, save_png, out_file)
        plot_asset_eval(result_eval, save_png, out_file)
        plot_failure_eval(result_eval, save_png, out_file)


def plot_probability_graph(
    FPA_result,
    failure_table,
    failure_asset_id,
    failure_date,
    alert_win=None,
    asset_limit=100,
    asset_per_column=3,
    alert_res=None,
    only_failing=True,
):
    """
    Plots the plobability of failure for all assets as a function of time with failure points \
    and alert windows.

    Parameters:
        FPA_result (pandas dataframe, required): The result table obtained from model training \
                    containing the the 'asset_id', 'datetime', 'target_label' and 'prob'.
        failure_table (pandas dataframe, required): Table containing the failure_id and date \
                    for each asset.
        failure_asset_id (string, required): Column name in the failure_table containing asset_id.
        failure_date (string, required): Column name in the failure_table containing the datetime.
        alert_win (int/dict, optional): Value for the interval for which alert window needs to be \
                    created. \
                    - If the 'datetime' column in FPA_result table is in datetime format, then pass \
                    a dict with this format.--> {'weeks': 0, \
                                                'days': 1, \
                                                'hours': 0, \
                                                'minutes': 0, \
                                                'seconds': 0} \
                    - If the 'datetime' column in FPA_result table is in int, then pass an int signifying the \
                    records to highlight in alert window. \
        asset_limit (int, optional): Number of plots for assets to be plotted. \
        asset_per_column (int, optional): Number of asset plots per row.
        alert_res (int, optional): Resolution for the alerts.
        only_failing (boolean, optional): Plot only those assets which fail atleast once.
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError as _:
        LOGGER.warning(
            "Cannot import matplotlib.pyplot. Drawing of plots will not be possible."
        )

    try:
        from IPython.display import display, Markdown
    except ImportError:
        print("Please install IPython dependencies to use this module.")

    # initializing plot
    asset_count = len(FPA_result["asset_id"].unique())
    plot_count = 0
    fig = plt.figure(figsize=(20, int(asset_count / asset_per_column) * 5), dpi=50)
    failure_table = failure_table.dropna()

    # for each asset, plot new graph
    for name, grp in FPA_result.groupby("asset_id"):
        if only_failing:
            if (
                len(
                    list(
                        failure_table[failure_table[failure_asset_id] == name][
                            failure_date
                        ]
                    )
                )
                < 1
            ):
                continue
        max_datetime = grp.loc[grp.datetime.idxmax(), "datetime"]

        x = grp["datetime"]
        y = grp["prob"]
        ax = fig.add_subplot(
            int(asset_count / asset_per_column) + 1, asset_per_column, plot_count + 1
        )
        plot_count += 1
        ax.plot(
            x,
            y,
            label="Probability of failure",
            marker="o",
            linewidth=0.5,
            markersize=4,
        )
        ax.set_title(str(name), fontsize=16, ha="center")
        plt.figure()
        for fail_date in list(
            failure_table[failure_table[failure_asset_id] == name][failure_date]
        ):
            ax.plot([fail_date, fail_date], [min(y), max(y)], label="Alert", color="r")
            if alert_win is not None:
                if isinstance(alert_win, dict):
                    if isinstance(fail_date, pd._libs.tslib.Timestamp):

                        # initializing any missing keys as 0
                        interval_keys = ["weeks", "days", "hours", "minutes", "seconds"]
                        for key in interval_keys:
                            if key not in alert_win.keys():
                                alert_win[key] = 0
                            else:
                                continue

                        weeks = alert_win["weeks"]
                        days = alert_win["days"]
                        hours = alert_win["hours"]
                        minutes = alert_win["minutes"]
                        seconds = alert_win["seconds"]
                        alert_datetime_precise = fail_date - timedelta(
                            weeks=weeks,
                            days=days,
                            hours=hours,
                            minutes=minutes,
                            seconds=seconds,
                        )
                        if alert_res is None:
                            alert_res = {
                                "weeks": 0,
                                "days": 1,
                                "hours": 0,
                                "minutes": 0,
                                "seconds": 0,
                            }

                        alert_datetime = time_sampling(
                            alert_datetime_precise, fail_date, alert_res
                        )
                        alert_datetime_list = list(alert_datetime["timestamp"])
                        for t, datetime in enumerate(alert_datetime_list):
                            _alpha = (0.3) / len(alert_datetime_list)
                            ax.plot(
                                [datetime, datetime],
                                [min(y), max(y)],
                                label="Alert",
                                color="orange",
                                alpha=t * _alpha + 0.15,
                            )
                    else:
                        raise Exception(
                            'The datetime column in "FPA_result" table is \
                                         not in datetime format whereas "alert_win" \
                                         provided is a dict. Provide a int value for alert_win.'
                        )

                elif isinstance(alert_win, int):
                    if isinstance(fail_date, int):
                        alert_datetime_list = range(fail_date - alert_win, fail_date)
                        for t, datetime in enumerate(alert_datetime_list):
                            _alpha = (0.4) / len(alert_datetime_list)
                            ax.plot(
                                [datetime, datetime],
                                [min(y), max(y)],
                                label="Alert",
                                color="orange",
                                alpha=t * _alpha + 0.1,
                            )
                    else:
                        raise Exception(
                            'The datetime column in "FPA_result" table is \
                                         not in datetime format whereas "alert_win" \
                                         provided is a dict. Provide a int value for alert_win.'
                        )

        if plot_count + 1 >= asset_limit:
            break

    fig.tight_layout()
