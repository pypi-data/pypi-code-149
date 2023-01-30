# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'MaintenanceScope',
    'Visibility',
]


class MaintenanceScope(str, Enum):
    """
    Gets or sets maintenanceScope of the configuration
    """
    ALL = "All"
    HOST = "Host"
    RESOURCE = "Resource"
    IN_RESOURCE = "InResource"
    OS_IMAGE = "OSImage"
    EXTENSION = "Extension"
    IN_GUEST_PATCH = "InGuestPatch"
    SQLDB = "SQLDB"
    SQL_MANAGED_INSTANCE = "SQLManagedInstance"


class Visibility(str, Enum):
    """
    Gets or sets the visibility of the configuration
    """
    CUSTOM = "Custom"
    PUBLIC = "Public"
