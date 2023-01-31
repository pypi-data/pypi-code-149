# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import numpy as np
from sklearn.base import BaseEstimator


class BuildFnWrapper(object):
    def __init__(self, func):
        self.func = func

    @property
    def __call__(self):
        return self.func


def get_estimator_meta_attributes(est):
    "return estimator meta data"
    data = {}
    attrs = [
        "coef_",
        "intercept_",
        "alpha_",
        "lambda_",
        "sigma_",
        "tree_",
        "feature_importances_",
        "n_features_",
        "n_outputs_",
    ]
    for attr in attrs:
        if hasattr(est, attr):
            prop = getattr(est, attr)
            data[attr] = prop
            if isinstance(prop, np.ndarray):
                data[attr] = prop.tolist()
    if len(data) > 0:
        return data
    else:
        return None


# CODE from autoai_ts_libs.deps.srom_AUTOAI_TIMESERIES
# https://github.ibm.com/srom/srom_autoai_timeseries/blob/master/srom/utils/estimator_utils.py

# list of model types supported as deep learning models
# 1. Keras model - BaseWrapper


def check_model_type_is_dl(model):
    try:    
        from scikeras.wrappers import KerasRegressor, KerasClassifier
    except ImportError:
        return False
    
    for i in [KerasRegressor, KerasClassifier]:
        if isinstance(model, i):
            return True
    return False


def check_object_is_estimator(model):
    from scikeras.wrappers import KerasRegressor, KerasClassifier

    for i in [BaseEstimator, KerasRegressor, KerasClassifier]:
        if isinstance(model, i):
            return True
    return False
