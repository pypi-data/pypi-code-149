"""
This defines some constants used for various time series use cases.
"""

# Standard
import enum


class PredictionTypes(enum.Enum):
    Sliding = "sliding"
    Batch = "batch"
