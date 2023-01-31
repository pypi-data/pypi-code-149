# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Backing class for SROM's non-linear optimization implementation.
It's main role is generating minimal bounding constraints given
a input grid for control variables."""

import numpy as np

from typing import Dict, List
from .constraints import MinBoundFunctor, MaxBoundFunctor


class NLOptimizer:
    """Backing code for SROM Non-linear optimizer/"""

    def __init__(
        self,
        piplines_dict: Dict,
        param_grid: Dict[str, np.arange],
        control_vars: List[str],
    ):
        self.pipelines_dict = piplines_dict
        self.control_vars = control_vars
        self.param_grid = param_grid
        self.constraints = []
        self._buildminmaxbounds()

    def _buildminmaxbounds(self):
        for function in self._minbounds(self.control_vars):
            self.constraints.append(function)
        for function in self._maxbounds(self.control_vars):
            self.constraints.append(function)

    # x_i > x_min for all i
    def _minbounds(self, names: List[str]):
        for name in names:
            yield MinBoundFunctor(name, names, self.param_grid)

    # x_i < x_max for_all i
    def _maxbounds(self, names: List[str]):
        for name in names:
            yield MaxBoundFunctor(name, names, self.param_grid)
