import numpy as np
from typing import List, Dict, TypedDict


class OutputVariableMetaData(TypedDict):
    min: float
    max: float


def scale_variable(observed_variable, min_val, max_val):
    if max_val == min_val:
        raise Exception("Division by zero error: Maximum and Minimum values are equal")
    return (observed_variable - min_val) / (max_val - min_val)


def scale_outputs(variables: List[str], variable_scales: Dict[str, OutputVariableMetaData]):
    assert all([variable_scales[k]['min'] < variable_scales[k]['max'] for k in variables]
               ), "Check that all min and max values in output variable meta data are correct"

    def _scale_outputs(model_outputs: np.ndarray, params=None) -> np.ndarray:

        scales = [[variable_scales[k]['min'], variable_scales[k]['max']] for k in variables]
        scaled_modelled = np.array([scale_variable(model_outputs[:, i], temp_min, temp_max) for i, [
            temp_min, temp_max] in enumerate(scales)]).transpose()
        return scaled_modelled

    return _scale_outputs
