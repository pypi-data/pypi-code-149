# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import copy
from autoai_ts_libs.deps.srom.utils.estimator_utils import check_model_type_is_dl


def deeper_copy(option, model_type="regression"):
    """
    Utility for deep copying models or any other object which works with copy.deepcopy()
    """
    # checking if the function input is tuple or model. (for SROM_pipeline.set_stages())
    if isinstance(option, tuple):
        taskname = option[0]
        model = option[1]
    else:
        model = option

    # checking model type and doing clone/deep copy
    if "keras.engine" in str(type(model)):
        from tensorflow.keras.models import clone_model

        model_copy = clone_model(model)
        model_copy.set_weights(model.get_weights())
        model_copy.compile(model.optimizer, model.loss)

    elif (
        "keras.wrappers" in str(type(model)) or check_model_type_is_dl(model)
    ) and hasattr(model, "model_"):
        # if object type is keras wrapper and it has already been trained, then it
        # should be cloned. Otherwise normal deep copy works.
        from tensorflow.keras.models import clone_model

        original_model = model.model_
        model_copy = clone_model(original_model)
        model_copy.set_weights(original_model.get_weights())
        model_copy.compile(original_model.optimizer, original_model.loss)
        # wrap model back in keras regressor
        from scikeras.wrappers import (
            KerasClassifier,
            KerasRegressor,
        )

        def wrap_model():
            return model_copy

        if model_type == "regression":
            model_copy = KerasRegressor(build_fn=wrap_model)
        elif model_type == "classification":
            model_copy = KerasClassifier(build_fn=wrap_model)

    else:
        # deep copy in all other cases
        model_copy = copy.deepcopy(model)

    # return the new copy in the original form
    if isinstance(option, tuple):
        return (taskname, model_copy)
    else:
        return model_copy
