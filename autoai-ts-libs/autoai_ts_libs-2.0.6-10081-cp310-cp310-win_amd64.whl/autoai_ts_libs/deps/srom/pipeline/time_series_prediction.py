# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: time_series_prediction
   :synopsis: Contains TimeSeriesPredictionPipeline class.

.. moduleauthor:: SROM Team
"""
from abc import abstractmethod
from itertools import compress

from sklearn.metrics._regression import mean_absolute_error
from sklearn.pipeline import Pipeline
from autoai_ts_libs.deps.srom.model_selection import TimeSeriesTrainTestSplit

# # srom pipeline
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.time_series.utils.scorer import make_ts_scorer
from autoai_ts_libs.deps.srom.time_series.pipeline import Forecaster
import numpy as np
import pandas as pd


class TimeSeriesPredictionPipeline(SROMPipeline):
    """
    An abstraction built to be used by time series prediction pipeline \
    and prediction based anomaly detection pipelines (for now). It should \
    be used for other such time series pipeline built in the future.

    The BaseTS pipeline is being built to abstract methods and variables which are involved \
    in pipeline path parsing, data transformation and providing the Cross-Validator with the \
    right data to fit the best estimator.
    """

    # @TODO: Implement functionality to use variable `time_column`

    def __init__(
        self,
        feature_columns,
        target_columns,
        lookback_win=None,
        pred_win=None,
        time_column=None,
        store_lookback_history=True,
    ):
        super(TimeSeriesPredictionPipeline, self).__init__()

        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.store_lookback_history = store_lookback_history
        self.time_column = time_column

        # Overwriting SROM pipeline's CV
        self.cv = None
        self.scoring = None
        self.best_estimator = None
        self.best_score = None
        self._init_execution_params()

    def add_stages(self, stages):
        """
        Adds a set of graph nodes in a list of list format. \
        Appends to the existing graph by adding another set \
        of nodes from start to end.
        """
        self._sromgraph.add_stages(stages)

    def _init_execution_params(self):
        """
        """

        if not isinstance(self.pred_win, int):
            raise Exception("prediction window should be integer")

        if isinstance(self.lookback_win, list):
            if len(self.lookback_win) != len(self.feature_columns):
                raise Exception(
                    "length of lookback window and feature columns must be identical"
                )

        if self.scoring is None:
            # an internal object for scoring
            neg_mean_absolute_error_scorer = make_ts_scorer(
                mean_absolute_error, greater_is_better=False
            )
            super(TimeSeriesPredictionPipeline, self).set_scoring(
                neg_mean_absolute_error_scorer
            )

        # cross validator object
        if self.cv is None or self.cv == 1:
            self.cv = TimeSeriesTrainTestSplit()

        # set pipeline type to Forecast
        self.set_pipeline_type_for_path(Forecaster)
        self.set_pipeline_init_param_for_path(
            {
                "feature_columns": self.feature_columns,
                "target_columns": self.target_columns,
                "lookback_win": self.lookback_win,
                "pred_win": self.pred_win,
                "store_lookback_history": self.store_lookback_history,
                "time_column": self.time_column,
            }
        )

    def add_input_meta_data(
        self, time_column=None, id_column=None, label_column=None, label_prefix=None
    ):
        raise NotImplementedError(
            "Method add_input_meta_data is not supported for Time Series Pipeline."
        )

    def _specialdatatransforms(self, X, y):
        """Ignore the parent class

        Args:
            X ([type]): [description]
            y ([type]): [description]

        Returns:
            [type]: [description]
        """
        if isinstance(X, pd.DataFrame):
            return np.array(X), y
        if isinstance(X, (np.ndarray, np.generic)):
            return X, y
        else:
            raise ValueError("X is not an instance of numpy array")

