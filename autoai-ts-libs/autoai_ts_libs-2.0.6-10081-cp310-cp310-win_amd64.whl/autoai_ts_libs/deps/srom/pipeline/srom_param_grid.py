# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


# -*- coding: utf-8 -*-
"""
    .. module:: srom_param_grid
       :synopsis: Contains classes related to Parameter Grid \
            which can be used with SROMPipeline. These classes are \
            used in performing exhaustive or randomized grid search.

    .. moduleauthor:: SROM Team
"""
import copy
import logging

LOGGER = logging.getLogger(__name__)


class SROMParamGrid(object):
    """
    SROMParamGrid class provides functionality to \
    operate and generate Parameter Grid.
    """

    def __init__(self, gridtype="empty"):
        """
        Initialize the SROMParamGrid with provided gridtype.
        Args:
            gridtype (String):
                "classification_fine_grid", "regression_fine_grid",
                "anomaly_detection_fine_grid" and "empty".
        """

        self.default_param_grid = {}

        if gridtype == "empty":
            self.default_param_grid = {}
        elif gridtype == "classification_fine_grid":
            from .hyper_params.classification_fine_grid import (
                PARAM_GRID as classification_fine_grid,
            )

            self.default_param_grid = copy.deepcopy(classification_fine_grid)
        elif gridtype == "regression_fine_grid":
            from .hyper_params.regression_fine_grid import (
                PARAM_GRID as regression_fine_grid,
            )

            self.default_param_grid = copy.deepcopy(regression_fine_grid)
        elif gridtype == "anomaly_detection_fine_grid":
            from .hyper_params.anomaly_detection_fine_grid import (
                PARAM_GRID as anomaly_detection_fine_grid,
            )

            self.default_param_grid = copy.deepcopy(anomaly_detection_fine_grid)
        elif gridtype == "survival_analysis_fine_grid":
            from .hyper_params.survival_analysis_fine_grid import (
                PARAM_GRID as survival_analysis_fine_grid,
            )

            self.default_param_grid = copy.deepcopy(survival_analysis_fine_grid)
        elif gridtype == "imbalanced_classification_fine_grid":
            from .hyper_params.imbalanced_fine_grid import (
                PARAM_GRID as imbalanced_classification_fine_grid,
            )

            self.default_param_grid = copy.deepcopy(imbalanced_classification_fine_grid)
        elif gridtype == "imputation_iid_grid":
            from .hyper_params.imputation_iid_grid import (
                PARAM_GRID as imputation_iid_grid,
            )

            self.default_param_grid = copy.deepcopy(imputation_iid_grid)
        elif gridtype == "imputation_time_series_grid":
            from .hyper_params.imputation_time_series_grid import (
                PARAM_GRID as imputation_time_series_grid,
            )

            self.default_param_grid = copy.deepcopy(imputation_time_series_grid)
        elif gridtype == "time_series_prediction_fine_grid":
            from .hyper_params.time_series_prediction_fine_grid import (
                PARAM_GRID as time_series_prediction_fine_grid,
            )

            self.default_param_grid = copy.deepcopy(time_series_prediction_fine_grid)
        else:
            error_msg = (
                'Wrong gridtype provided. Available types are "classification_fine_grid",'
                '"regression_fine_grid", "anomaly_detection_fine_grid" and "empty".'
            )
            LOGGER.error(error_msg)
            # if this is not created then, shall we generate SROMException
            # or SROMParamGridException to stop the execution

    def get_param(self, key):
        """
        Retrieve parameters by key.

        Parameters:
            Key (String).

        Returns:
            The list of parameters corresponding to key.
        """
        if key in self.default_param_grid:
            return self.default_param_grid[key]
        return {}

    def get_param_grid(self):
        """
        Retrieve parameter grid.

        Returns:
            The dict of parameter grid.
        """
        return self.default_param_grid

    def set_param(self, key, value):
        """
        Sets parameter value for the given key.

        Parameters:
            key (String).
            value: Value corresponding to key.
        """
        self.default_param_grid[key] = value

    def set_param_grid(self, key_value_dict):
        """
        Set parameter grid.

        Parameters:
            key_value_dict (dict): Dictionary of parameters.
        """
        self.default_param_grid = {}
        self.default_param_grid.update(key_value_dict)

    def __str__(self):
        return (
            self.__class__.__name__
            + "(Parameters="
            + str(self.default_param_grid)
            + ")"
        )

    def __repr__(self):
        return self.__str__()
