# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: cusum_changepoint
   :synopsis: CUSUM based offline change points.

.. moduleauthor:: SROM Team
"""
import copy
import logging
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.cusum import CUSUM

LOGGER = logging.getLogger(__name__)


class ChangePointDetectionCUSUM(BaseEstimator, TransformerMixin):
    """
    ChangePointDetectionCUSUM class provides the change point detection by using CUSUM method. \
    It also combine the change point detected from multiple attributes as traditional cusum is \
    univariate.
    """

    def __init__(
        self,
        base_learner=CUSUM(),
        feature_column=None,
        date_column=None,
        window_range=30,
        threshold_index="q75",
        num_feature_choice=2,
        num_change_point=1,
    ):
        """
        Initialize ChangePointDetectionCUSUM with provided \
        feature_column, date_column, window_range, threshold_index, \
        num_feature_choice and num_change_point.

        Parameters:
            feature_column (list of String): List feature name.
            date_column (list of String): List of the date column.
            window_range (Int): The range of windows.
            threshold_index (String): 'q75': 75th quartile. \
                    'max': maximum of the difference values. \
                    '|min|': absolute value of the minimum of the difference values.
            num_feature_choice (Int): Number of features deciding the change point.
            num_change_point (Int): Number of change points.
        """
        self.feature_column = feature_column
        self.date_column = date_column
        self.threshold_index = threshold_index
        self.num_feature_choice = num_feature_choice
        self.num_change_point = num_change_point
        self.window_range = window_range
        self.base_learner = base_learner

    def fit(self, X=None):
        """
        Parameters:
            X (pandas dataframe or numpy array, required): Defaults to None.

        Returns:
            self: Trained instance of LOFNearestNeighborAnomalyModel.
        """
        return self

    def transform(self, X):
        """
        Achieve the change point detection.

        Parameters:
            X: data.

        Returns:
            The change point.
        """

        tmp_x = X[self.feature_column + self.date_column].dropna()
        original_index = np.array(list(tmp_x.index))
        tmp_x = tmp_x.reset_index()

        if len(tmp_x) < self.num_change_point:
            X.loc[:, "change_point"] = 0
            return X["change_point"]

        try:
            # Create a list of range
            list_range = []
            list_change_point = []

            for feature_ind in range(len(self.feature_column)):
                if self.threshold_index == "q75":
                    threshold, _ = np.percentile(
                        tmp_x[self.feature_column[feature_ind]].dropna().values,
                        [75, 25],
                    )
                if self.threshold_index == "max":
                    threshold = np.max(
                        tmp_x[self.feature_column[feature_ind]].dropna().diff()
                    )
                if self.threshold_index == "|min|":
                    threshold = np.abs(
                        np.min(tmp_x[self.feature_column[feature_ind]].dropna().diff())
                    )

                cusum_srom = copy.deepcopy(self.base_learner)
                cusum_srom.threshold = threshold
                cusum_srom.fit(tmp_x[self.feature_column[feature_ind]].dropna().values)
                transformed_df = cusum_srom.predict(
                    tmp_x[self.feature_column[feature_ind]].dropna().values
                )

                tmp_x_2 = np.where(transformed_df == 1)[0]
                list_change_point.append(tmp_x_2)

                length_list = len(
                    tmp_x[self.feature_column[feature_ind]].dropna().values
                )

                for t_ind, _ in enumerate(tmp_x_2):
                    list_range.append(
                        list(
                            range(
                                max(tmp_x_2[t_ind] - self.window_range, 0),
                                min(tmp_x_2[t_ind] + self.window_range, length_list),
                            )
                        )
                    )

            list_point = [[] for i in range(len(list_range))]
            change_point = []

            for cp_index, _ in enumerate(list_change_point):
                for list_index, _ in enumerate(list_range):
                    intersect_tmp_x_2 = list(
                        set(list(list_change_point[cp_index]))
                        & set(list_range[list_index])
                    )
                    if intersect_tmp_x_2:
                        list_point[list_index].append(max(intersect_tmp_x_2))

                for list_index in range(len(list_range)):
                    if len(list_point[list_index]) >= self.num_feature_choice:
                        change_point.append(max(list_point[list_index]))

            change_point = list(set(change_point))

            X.loc[:, "change_point"] = 0
            X.loc[original_index[np.array(change_point)], "change_point"] = 1
            return X["change_point"]
        except Exception as ex:
            # raise a warning message, but continue
            LOGGER.warning(ex)

        X.loc[:, "change_point"] = 0
        return X["change_point"]

    def predict(self, X, y=None):
        """
        Predict is no-op here
        """
        pass
