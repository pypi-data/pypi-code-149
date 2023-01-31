# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: ggm_changepoint
   :synopsis: GGM based offline change points.

.. moduleauthor:: SROM Team
"""
import logging
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.base import BaseEstimator, TransformerMixin
from autoai_ts_libs.deps.srom.anomaly_detection.gaussian_graphical_anomaly_model import (
    GaussianGraphicalModel
)
from autoai_ts_libs.deps.srom.anomaly_detection.algorithms.anomaly_graph_lasso import AnomalyGraphLasso
from autoai_ts_libs.deps.srom.utils.distance_metric_utils import compute_mahalanobis

LOGGER = logging.getLogger(__name__)


class ChangePointDetectionGGM(BaseEstimator, TransformerMixin):
    """
    ChangePointDetectionGGM class provides the change point detection by \
    using Gaussian Graphical Model method.
    """

    def __init__(
        self,
        base_learner=GaussianGraphicalModel(
            base_learner=AnomalyGraphLasso(alpha=0.2),
            distance_metric="Mahalanobis_Distance",
        ),
        feature_column=None,
        date_column=None,
        num_change_point=1,
    ):
        """
        Initialize ChangePointDetectionGGM with provided \
        feature_column, date_column, and num_change_point.
        
        Parameters:
            feature_column (list of String): List feature name.
            date_column (list of String): List of the date column.
            num_change_point (Int): Number of change points.
        """

        self.base_learner = base_learner
        self.feature_column = feature_column
        self.date_column = date_column
        self.num_change_point = num_change_point

    def fit(self, X):
        """
        Fit method is a no-op.
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

        # tmpX = X[self.feature_column+self.date_column].dropna().reset_index()

        tmp_x = X[self.feature_column + self.date_column].dropna()
        original_index = np.array(list(tmp_x.index))
        tmp_x = tmp_x.reset_index()

        if len(tmp_x) < self.num_change_point:
            X.loc[:, "change_point"] = 0
            return X["change_point"]

        try:
            trained_model = self.base_learner.fit(
                tmp_x[self.feature_column].dropna().values
            )
            # getting the precision matrix, covariance matrix and the mean from the GGM model.
            train_precision = trained_model.model_train.precision_
            train_mean = trained_model.mean_train
            distance = compute_mahalanobis(
                preprocessing.scale(tmp_x[self.feature_column].dropna().values),
                train_precision,
                train_mean,
            )
            sample_score = pd.DataFrame(
                [
                    list(range(tmp_x[self.feature_column].dropna().values.shape[0])),
                    list(distance),
                ]
            ).transpose()
            change_points = list(
                sample_score[1].argsort()[-1 * self.num_change_point :]
            )

            X.loc[:, "change_point"] = 0
            X.iloc[original_index[np.array(change_points)], "change_point"] = 1
            return X["change_point"]
        except Exception as ex:
            # raise a warning for user and continue
            LOGGER.warning(ex)

        X.loc[:, "change_point"] = 0
        return X["change_point"]

    def predict(self, X, y=None):
        """
        Predict method is no-op here.
        """
        pass
