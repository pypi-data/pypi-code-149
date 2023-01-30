# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'MaintenanceScope',
    'RebootOptions',
    'TaskScope',
    'Visibility',
]


class MaintenanceScope(str, Enum):
    """
    Gets or sets maintenanceScope of the configuration
    """
    HOST = "Host"
    """
    This maintenance scope controls installation of azure platform updates i.e. services on physical nodes hosting customer VMs.
    """
    RESOURCE = "Resource"
    """
    This maintenance scope controls the default update maintenance of the Azure Resource
    """
    OS_IMAGE = "OSImage"
    """
    This maintenance scope controls os image installation on VM/VMSS
    """
    EXTENSION = "Extension"
    """
    This maintenance scope controls extension installation on VM/VMSS
    """
    IN_GUEST_PATCH = "InGuestPatch"
    """
    This maintenance scope controls installation of windows and linux packages on VM/VMSS
    """
    SQLDB = "SQLDB"
    """
    This maintenance scope controls installation of SQL server platform updates.
    """
    SQL_MANAGED_INSTANCE = "SQLManagedInstance"
    """
    This maintenance scope controls installation of SQL managed instance platform update.
    """


class RebootOptions(str, Enum):
    """
    Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed.
    """
    IF_REQUIRED = "IfRequired"
    NEVER = "Never"
    ALWAYS = "Always"


class TaskScope(str, Enum):
    """
    Global Task execute once when schedule trigger. Resource task execute for each VM.
    """
    GLOBAL_ = "Global"
    RESOURCE = "Resource"


class Visibility(str, Enum):
    """
    Gets or sets the visibility of the configuration. The default value is 'Custom'
    """
    CUSTOM = "Custom"
    """
    Only visible to users with permissions.
    """
    PUBLIC = "Public"
    """
    Visible to all users.
    """
