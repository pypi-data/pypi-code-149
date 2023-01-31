# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import types
import sys
from autoai_ts_libs.deps.srom.utils.no_op import NoOp
from autoai_ts_libs.deps.srom.feature_engineering.model_based_feature_generator import ModelbasedFeatureGenerator
from autoai_ts_libs.deps.srom.feature_selection.variance_based_feature_selection import (
    LowVarianceFeatureElimination,
)
from autoai_ts_libs.deps.srom.regression.data_partition_based_regression import PartitionRegressor
from autoai_ts_libs.deps.srom.regression.gaussian_mixture_regressor import GaussianMixtureRegressor

CONFIG_CLASSES = [
    ModelbasedFeatureGenerator,
    NoOp,
    LowVarianceFeatureElimination,
    PartitionRegressor,
    GaussianMixtureRegressor
]

def replace_lithops_class(estimator):
    """
    """
    CONFIG_LST = [cls.__name__ for cls in CONFIG_CLASSES]
    for step_idx,step in enumerate(estimator.steps):    
        target_class = step[1].__class__
        if target_class.__name__ in CONFIG_LST:
            srom_cls_idx = CONFIG_LST.index(target_class.__name__)
            srom_cls = CONFIG_CLASSES[srom_cls_idx]
            estimator.steps[step_idx][1].__class__ = srom_cls

    return estimator

def replace_lithops_classes(estimators):
    """
    """
    CONFIG_LST = [cls.__name__ for cls in CONFIG_CLASSES]
    for (idx,estimator) in enumerate(estimators):
        for step_idx,step in enumerate(estimator.steps):    
            target_class = step[1].__class__
            if target_class.__name__ in CONFIG_LST:
                srom_cls_idx = CONFIG_LST.index(target_class.__name__)
                srom_cls = CONFIG_CLASSES[srom_cls_idx]
                estimators[idx].steps[step_idx][1].__class__ = srom_cls

    return estimators

def replace_srom_classes(stages):
    """
    """
    tmp_module = types.ModuleType('tmp_module', 'Module created for srom classes')
    for stage_idx,stage in enumerate(stages):
        for dag_idx,dag_step in enumerate(stage):
            target_class = dag_step[1].__class__
            if target_class in CONFIG_CLASSES:
                dummy_class = type(target_class.__name__, target_class.__bases__, dict(target_class.__dict__))
                setattr(tmp_module, dummy_class.__name__, dummy_class)
                dag_step[1].__class__ = dummy_class
                new_est = [dag_step[0],dag_step[1]]
                stages[stage_idx][dag_idx] = tuple(new_est) 
            
    sys.modules["tmp_module"] = tmp_module
    return stages
