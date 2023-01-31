# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

"""
.. module:: transformation
   :synopsis: Failure prediction preprocessing module.

.. moduleauthor:: SROM Team
"""

import pandas as pd


# utility function
def single_asset_failure_info_extraction(input_params):
    asset_id, date_column, failure_type, df, counter_flag = input_params
    df = df[[asset_id, date_column, failure_type]]
    tmp_df_left = df.copy()
    tmp_df_right = df.copy()
    tmp_df = pd.merge(tmp_df_left, tmp_df_right, on=failure_type)
    tmp_df = tmp_df[tmp_df[date_column + "_x"] > tmp_df[date_column + "_y"]]
    del tmp_df[asset_id + "_y"]

    # generate the counter
    if counter_flag:
        first_failure_df = df[[asset_id, date_column, failure_type]].copy()
        first_failure_df = first_failure_df.groupby([asset_id, failure_type]).min()
        first_failure_df = first_failure_df.reset_index()
        first_failure_df.columns = [asset_id, date_column, failure_type]
        first_failure_df[failure_type + "_" + "failure_count"] = 1

        counter_df = tmp_df[
            [asset_id + "_x", failure_type, date_column + "_x", date_column + "_y"]
        ].copy()
        counter_df = counter_df.groupby(
            [asset_id + "_x", failure_type, date_column + "_x"]
        ).count()
        counter_df = counter_df.reset_index()
        counter_df.columns = [
            asset_id,
            failure_type,
            date_column,
            failure_type + "_failure_count",
        ]
        counter_df[failure_type + "_failure_count"] = (
            counter_df[failure_type + "_failure_count"] + 1
        )
        counter_df = pd.concat([first_failure_df, counter_df], axis=0)

    # generate max feature
    tmp_df = tmp_df.groupby([asset_id + "_x", failure_type, date_column + "_x"]).max()
    tmp_df = tmp_df.reset_index()
    cname = []
    for c_name in tmp_df.columns:
        if "_x" in c_name:
            cname.append(c_name.split("_x")[0])
        elif date_column + "_y" in c_name:
            cname.append("past_" + date_column)
        else:
            cname.append(c_name)
    tmp_df.columns = cname

    # merge the features with
    df = pd.merge(df, tmp_df, on=[asset_id, date_column, failure_type], how="left")
    if counter_flag:
        df = pd.merge(
            df, counter_df, on=[asset_id, date_column, failure_type], how="left"
        )
    return df


# prepare a failure table with relevant information
def generate_past_failure_records(df, asset_column, date_column, failure_type_column):
    from multiprocessing import cpu_count, Pool

    part = [
        (asset_column, date_column, failure_type_column, grp, True)
        for _, grp in df.groupby(asset_column)
    ]
    cores = cpu_count() - 1
    with Pool(cores) as p:
        resList = p.map(single_asset_failure_info_extraction, part)
    extractedFeatures = pd.concat(resList)

    part = [
        (asset_column, "past_" + date_column, failure_type_column, grp, False)
        for _, grp in extractedFeatures.groupby(asset_column)
    ]
    with Pool(cores) as p:
        resList = p.map(single_asset_failure_info_extraction, part)
    extractedFeatures_l1 = pd.concat(resList)

    final_df = pd.merge(
        extractedFeatures,
        extractedFeatures_l1,
        on=[asset_column, "past_" + date_column, failure_type_column],
    )
    return final_df


def generate_failure_centric_records(
    key_table,
    post_failure_table,
    asset_id,
    asset_date,
    failure_date,
    failure_type_column,
):
    tmp_df = pd.merge(key_table, post_failure_table, on=asset_id)
    tmp_df = tmp_df[tmp_df[asset_date] > tmp_df[failure_date]]
    PA = tmp_df.loc[
        tmp_df.groupby([asset_id, asset_date, failure_type_column])[
            failure_date
        ].idxmax()
    ]
    PA["age"] = PA["date"] - PA["failure_date"]
    PA["past_age"] = PA["failure_date"] - PA["past_failure_date"]
    PA = PA[
        [
            "age",
            "past_age",
            asset_id,
            asset_date,
            failure_type_column,
            failure_type_column + "_failure_count",
        ]
    ]
    generated_features_Db = pd.merge(
        key_table, PA, on=[asset_id, asset_date], how="left"
    )
    return generated_features_Db

