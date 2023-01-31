# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: rca
   :synopsis: This modules is used to send Root Cause \
        Analysis request to WML deployed models. The functions \
        in the file allow parsing the user's input request into \
        wml-consumable payload and the wml response is converted \
        to API response at the user's end.

.. moduleauthor:: SROM Team
"""


def predict_parser(df):
    """
    Local Parser function for users to convert their data in RCA \
    predict request format. Takes an episodic dataframe from the \
    user and sends it to the SROM Scoring Flask to send it to WML.

    Parameters:
        df (pandas DataFrame, required): User's input dataframe \
            for episodic time series.

    Returns:
        predict_request_values (list): Object that can be used as \
            the predict request object for srom scoring flask.
    """
    df_list = df.values.tolist()

    predict_request_values = []

    for episode in df_list:
        episode_id = episode[0]
        featuretimeseries = episode[1]

        feature_time_series = []

        feature_list = featuretimeseries.keys()
        for feature in feature_list:
            ts_data = featuretimeseries[feature]
            timestamp = list(ts_data.keys())
            timeseries = list(ts_data.values())
            feature_time_series.append(
                {"feature": feature, "timestamp": timestamp, "timeseries": timeseries}
            )

        predict_request_values.append(
            {"episode_id": episode_id, "featuretimeseries": feature_time_series}
        )

    return predict_request_values


def payload_parser(predict_request_values):
    """
    SROM Scoring flask function for data conversion. \
    Takes the predict request object from the users for \
    RCA and convert it to WML payload format.

    Parameters:
        predict_request_values (list, required): Object that \
            can be used as the predict request object for srom \
            scoring flask.

    Returns:
        wml_scoring_request (dict): payload object for scoring on WML.
    """
    wml_scoring_request = {"values": []}

    for episode in predict_request_values:
        episode_list = []
        episode_list.append(episode["episode_id"])
        featuretimeseries = episode["featuretimeseries"]

        feature_dict = {}
        for fts in featuretimeseries:
            feature = fts["feature"]
            timestamp = fts["timestamp"]
            timeseries = fts["timeseries"]

            timeseries_dict = {t: timeseries[i] for i, t in enumerate(timestamp)}
            feature_dict[feature] = timeseries_dict
        episode_list.append(feature_dict)

        wml_scoring_request["values"].append(episode_list)

    return wml_scoring_request


def response_parser(predict_response, value_key):
    """
    Scoring Flask function- takes the WML scoring response \
    and parses the content to be sent to the user.

    Parameters:
        predict_response (WML scoring response/dict, required): WML \
            scoring response.
        value_key (str, required): Key to access in the wml response.

    Returns:
        parsed wml response.
    """
    return [i[0] for i in predict_response[value_key]]


def episode_kpi_table(rca_predresponse):
    """
    Returns the list of episode_kpi after KPI scoring on WML.

    Parameters:
        rca_predresponse (list, required): Results returned \
            from Root Cause KPI scoring on WML.

    Returns:
        episode_id_list (list): List of episode-ids.
        pred_value (list): List of episode-wise predictions.
        pred_proba_value (list): List of episode-wise prediction probability. \
        feature_path_list (list): List of episode-wise feature table in \
            organized way. This can be later used for plotting tables. \
            The order of the features is from the most important feature \
            to the least important.
    """

    episode_kpi_list = rca_predresponse
    feature_path_list = []
    pred_proba_value = []
    pred_value = []
    episode_id_list = []

    for episode_kpi in episode_kpi_list:

        pred_value.append(episode_kpi["prediction"])
        pred_proba_value.append(episode_kpi["prediction_proba"])
        episode_id_list.append(episode_kpi["episode_id"])

        feature_path = [
            [
                "node_id",
                "feature",
                "feature importance",
                "feature description",
                "node threshold",
                "node value",
            ]
        ]

        for feature_kpi in episode_kpi["tree_path"]:
            feature_path.append(
                [
                    feature_kpi["treenode_id"],
                    feature_kpi["feature"],
                    feature_kpi["feature_imp"],
                    feature_kpi["feature_desc"],
                    feature_kpi["feature_decision_threshold"],
                    feature_kpi["record_feature_val"],
                ]
            )
        feature_path_list.append(feature_path)
    return episode_id_list, pred_value, pred_proba_value, feature_path_list
