"""
Forecasting blocks solve the problem of predicting future values of a
timeseries
"""

# Local
from ...toolkit.hoist_module_imports import hoist_module_imports
from . import (
    fctk_deepar_estimator,
    fctk_l2f,
    fctk_lightgbm_ray,
    fctk_random_forest,
    srom_mt2r,
    tspy_bats,
)

# Block classes hoisted to the top level
# NOTE: These must come after the module imports so that the block modules
#   themselves can be tracked cleanly for optional modules
hoist_module_imports(globals())
