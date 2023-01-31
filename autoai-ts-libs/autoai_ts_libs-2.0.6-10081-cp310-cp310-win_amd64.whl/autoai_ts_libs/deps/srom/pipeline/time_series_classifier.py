# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: time_series_classification
   :synopsis: Contains TimeSeriesClassificationPipeline class.

.. moduleauthor:: SROM Team
"""

from sklearn.metrics._scorer import neg_mean_absolute_error_scorer
from sklearn.model_selection import GroupKFold

# # srom pipeline
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.time_series.pipeline import Classifier


class TimeSeriesClassificationPipeline(SROMPipeline):
    """
    An abstraction built to be used by time series classification pipeline.

    The BaseTS pipeline is being built to abstract methods and variables which are involved \
    in pipeline path parsing, data transformation and providing the Cross-Validator with the \
    right data to fit the best estimator.
    """

    def __init__(
        self,
        feature_columns,
        target_columns,
        time_column=None,
        id_column=None,
        lookback_win=None,
        pred_win=None,
        skip_observation=0,
    ):
        super(TimeSeriesClassificationPipeline, self).__init__()

        self.feature_columns = feature_columns
        self.target_columns = target_columns
        self.lookback_win = lookback_win
        self.pred_win = pred_win
        self.time_column = time_column
        self.id_column = id_column
        self.skip_observation = skip_observation

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

        if self.scoring is None:
            super(TimeSeriesClassificationPipeline, self).set_scoring(
                neg_mean_absolute_error_scorer
            )

        # cross validator object
        if self.cv is None or self.cv == 1:
            self.cv = GroupKFold(
                n_splits=2
            )  # TODO: k-fold cross-validation requires at least one train/test split by setting n_splits=2 or more
        # set pipeline type to Forecast
        self.set_pipeline_type_for_path(Classifier)
        self.set_pipeline_init_param_for_path(
            {
                "feature_columns": self.feature_columns,
                "target_columns": self.target_columns,
                "lookback_win": self.lookback_win,
                "pred_win": self.pred_win,
                "skip_observation": self.skip_observation,
                "time_column": self.time_column,
                "id_column": self.id_column,
            }
        )
