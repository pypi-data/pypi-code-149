# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccessMode',
    'Action',
    'ActiveRevisionsMode',
    'AppProtocol',
    'BindingType',
    'ClientCredentialMethod',
    'CookieExpirationConvention',
    'ExtendedLocationTypes',
    'ForwardProxyConvention',
    'IngressClientCertificateMode',
    'IngressTransportMethod',
    'LogLevel',
    'ManagedEnvironmentOutBoundType',
    'ManagedServiceIdentityType',
    'Scheme',
    'SkuName',
    'StorageType',
    'Type',
    'UnauthenticatedClientActionV2',
]


class AccessMode(str, Enum):
    """
    Access mode for storage
    """
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class Action(str, Enum):
    """
    Allow or Deny rules to determine for incoming IP. Note: Rules can only consist of ALL Allow or ALL Deny
    """
    ALLOW = "Allow"
    DENY = "Deny"


class ActiveRevisionsMode(str, Enum):
    """
    ActiveRevisionsMode controls how active revisions are handled for the Container app:
    <list><item>Multiple: multiple revisions can be active.</item><item>Single: Only one revision can be active at a time. Revision weights can not be used in this mode. If no value if provided, this is the default.</item></list>
    """
    MULTIPLE = "Multiple"
    SINGLE = "Single"


class AppProtocol(str, Enum):
    """
    Tells Dapr which protocol your application is using. Valid options are http and grpc. Default is http
    """
    HTTP = "http"
    GRPC = "grpc"


class BindingType(str, Enum):
    """
    Custom Domain binding type.
    """
    DISABLED = "Disabled"
    SNI_ENABLED = "SniEnabled"


class ClientCredentialMethod(str, Enum):
    """
    The method that should be used to authenticate the user.
    """
    CLIENT_SECRET_POST = "ClientSecretPost"


class CookieExpirationConvention(str, Enum):
    """
    The convention used when determining the session cookie's expiration.
    """
    FIXED_TIME = "FixedTime"
    IDENTITY_PROVIDER_DERIVED = "IdentityProviderDerived"


class ExtendedLocationTypes(str, Enum):
    """
    The type of the extended location.
    """
    CUSTOM_LOCATION = "CustomLocation"


class ForwardProxyConvention(str, Enum):
    """
    The convention used to determine the url of the request made.
    """
    NO_PROXY = "NoProxy"
    STANDARD = "Standard"
    CUSTOM = "Custom"


class IngressClientCertificateMode(str, Enum):
    """
    Client certificate mode for mTLS authentication. Ignore indicates server drops client certificate on forwarding. Accept indicates server forwards client certificate but does not require a client certificate. Require indicates server requires a client certificate.
    """
    IGNORE = "ignore"
    ACCEPT = "accept"
    REQUIRE = "require"


class IngressTransportMethod(str, Enum):
    """
    Ingress transport protocol
    """
    AUTO = "auto"
    HTTP = "http"
    HTTP2 = "http2"
    TCP = "tcp"


class LogLevel(str, Enum):
    """
    Sets the log level for the Dapr sidecar. Allowed values are debug, info, warn, error. Default is info.
    """
    INFO = "info"
    DEBUG = "debug"
    WARN = "warn"
    ERROR = "error"


class ManagedEnvironmentOutBoundType(str, Enum):
    """
    Outbound type for the cluster
    """
    LOAD_BALANCER = "LoadBalancer"
    USER_DEFINED_ROUTING = "UserDefinedRouting"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class Scheme(str, Enum):
    """
    Scheme to use for connecting to the host. Defaults to HTTP.
    """
    HTTP = "HTTP"
    HTTPS = "HTTPS"


class SkuName(str, Enum):
    """
    Name of the Sku.
    """
    CONSUMPTION = "Consumption"
    """
    Consumption SKU of Managed Environment.
    """
    PREMIUM = "Premium"
    """
    Premium SKU of Managed Environment.
    """


class StorageType(str, Enum):
    """
    Storage type for the volume. If not provided, use EmptyDir.
    """
    AZURE_FILE = "AzureFile"
    EMPTY_DIR = "EmptyDir"


class Type(str, Enum):
    """
    The type of probe.
    """
    LIVENESS = "Liveness"
    READINESS = "Readiness"
    STARTUP = "Startup"


class UnauthenticatedClientActionV2(str, Enum):
    """
    The action to take when an unauthenticated client attempts to access the app.
    """
    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"
    RETURN401 = "Return401"
    RETURN403 = "Return403"
