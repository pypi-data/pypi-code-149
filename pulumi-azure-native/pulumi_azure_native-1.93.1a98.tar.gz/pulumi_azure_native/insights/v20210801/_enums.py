# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ConditionOperator',
    'DimensionOperator',
    'Kind',
    'ManagedServiceIdentityType',
    'TimeAggregation',
]


class ConditionOperator(str, Enum):
    """
    The criteria operator. Relevant and required only for rules of the kind LogAlert.
    """
    EQUALS = "Equals"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"


class DimensionOperator(str, Enum):
    """
    Operator for dimension values
    """
    INCLUDE = "Include"
    EXCLUDE = "Exclude"


class Kind(str, Enum):
    """
    The kind of workbook. Only valid value is shared.
    """
    USER = "user"
    SHARED = "shared"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class TimeAggregation(str, Enum):
    """
    Aggregation type. Relevant and required only for rules of the kind LogAlert.
    """
    COUNT = "Count"
    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"
