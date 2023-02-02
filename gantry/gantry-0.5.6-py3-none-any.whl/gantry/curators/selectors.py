from enum import Enum
from typing import List, Optional, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal  # type: ignore

from pydantic import BaseModel, root_validator, validator

# Database constraint
MAX_NAME_LEN = 255
TIME_COLUMN_NAME = "__time"


class DruidDimensionOrderingDirections(str, Enum):
    """
    Direction to order results from Druid
    https://druid.apache.org/docs/latest/querying/limitspec.html
    """

    ASCENDING = "ascending"
    DESCENDING = "descending"


class SamplingMethod(str, Enum):
    uniform = "uniform"
    ordered = "ordered"
    stratified = "stratified"


class StratificationMode(str, Enum):
    strict = "strict"
    proportional = "proportional"
    balanced = "balanced"


class Filter(BaseModel):
    field: str


class BoundsFilter(Filter):
    upper: Optional[Union[float, int]] = None
    lower: Optional[Union[float, int]] = None

    @root_validator
    def validate_bounds(cls, values):
        if values["upper"] is None and values["lower"] is None:
            raise ValueError("Must have either an upper or lower bound")
        return values


class EqualsFilter(Filter):
    equals: Union[float, int]


class ContainsFilter(Filter):
    contains: str


ALL_FILTERS_T = Union[BoundsFilter, EqualsFilter, ContainsFilter]


class Sampler(BaseModel):
    pass


class UniformSampler(Sampler):
    sample: Literal[SamplingMethod.uniform] = SamplingMethod.uniform


class OrderedSampler(Sampler):
    sample: Literal[SamplingMethod.ordered] = SamplingMethod.ordered
    field: str
    sort: Literal[
        DruidDimensionOrderingDirections.ASCENDING, DruidDimensionOrderingDirections.DESCENDING
    ]


class StratifiedSampler(Sampler):
    field: str
    sample: Literal[SamplingMethod.stratified] = SamplingMethod.stratified
    mode: Literal[
        StratificationMode.strict, StratificationMode.proportional, StratificationMode.balanced
    ] = StratificationMode.proportional


ALL_METHODS_T = Union[OrderedSampler, UniformSampler, StratifiedSampler]


class Selector(BaseModel):
    method: ALL_METHODS_T = OrderedSampler(
        sample=SamplingMethod.ordered,
        field=TIME_COLUMN_NAME,
        sort=DruidDimensionOrderingDirections.DESCENDING,
    )
    limit: int
    filters: List[ALL_FILTERS_T] = []

    @validator("limit")
    def validate_limit(cls, value):
        if value <= 0:
            raise ValueError("Limit must be strictly positive")

        return value
