# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccessRights',
    'DefaultAction',
    'EndPointProvisioningState',
    'EntityStatus',
    'FilterType',
    'KeySource',
    'ManagedServiceIdentityType',
    'NetworkRuleIPAction',
    'PrivateLinkConnectionStatus',
    'SkuName',
    'SkuTier',
]


class AccessRights(str, Enum):
    MANAGE = "Manage"
    SEND = "Send"
    LISTEN = "Listen"


class DefaultAction(str, Enum):
    """
    Default Action for Network Rule Set
    """
    ALLOW = "Allow"
    DENY = "Deny"


class EndPointProvisioningState(str, Enum):
    """
    Provisioning state of the Private Endpoint Connection.
    """
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"


class EntityStatus(str, Enum):
    """
    Enumerates the possible values for the status of a messaging entity.
    """
    ACTIVE = "Active"
    DISABLED = "Disabled"
    RESTORING = "Restoring"
    SEND_DISABLED = "SendDisabled"
    RECEIVE_DISABLED = "ReceiveDisabled"
    CREATING = "Creating"
    DELETING = "Deleting"
    RENAMING = "Renaming"
    UNKNOWN = "Unknown"


class FilterType(str, Enum):
    """
    Filter type that is evaluated against a BrokeredMessage.
    """
    SQL_FILTER = "SqlFilter"
    CORRELATION_FILTER = "CorrelationFilter"


class KeySource(str, Enum):
    """
    Enumerates the possible value of keySource for Encryption
    """
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class NetworkRuleIPAction(str, Enum):
    """
    The IP Filter Action
    """
    ALLOW = "Allow"


class PrivateLinkConnectionStatus(str, Enum):
    """
    Status of the connection.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class SkuName(str, Enum):
    """
    Name of this SKU.
    """
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class SkuTier(str, Enum):
    """
    The billing tier of this particular SKU.
    """
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
