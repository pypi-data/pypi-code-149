from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from model.config.core import config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    new_vars_with_na = [
        var
        for var in config.model_config.features
        if validated_data[var].isnull().sum() > 0
    ]

    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    relevant_data = input_data[config.model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleMobileDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class MobileDataInputSchema(BaseModel):
    battery_power: Optional[int]
    blue: Optional[int]
    clock_speed: Optional[float]
    dual_sim: Optional[int]
    fc: Optional[int]
    four_g: Optional[int]
    int_memory: Optional[int]
    m_dep: Optional[float]
    mobile_wt: Optional[int]
    n_cores: Optional[int]
    pc: Optional[int]
    px_height: Optional[int]
    px_width: Optional[int]
    ram: Optional[int]
    sc_h: Optional[int]
    sc_w: Optional[int]
    talk_time: Optional[int]
    three_g: Optional[int]
    touch_screen: Optional[int]
    wifi: Optional[int]


class MultipleMobileDataInputs(BaseModel):
    inputs: List[MobileDataInputSchema]
