# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AzureSkuName',
    'AzureSkuTier',
    'BlobStorageEventType',
    'ClusterNetworkAccessFlag',
    'ClusterPrincipalRole',
    'Compression',
    'DataConnectionKind',
    'DatabasePrincipalRole',
    'DatabaseRouting',
    'DefaultPrincipalsModificationKind',
    'EngineType',
    'EventGridDataFormat',
    'EventHubDataFormat',
    'IdentityType',
    'IotHubDataFormat',
    'Kind',
    'PrincipalType',
    'PublicIPType',
    'PublicNetworkAccess',
]


class AzureSkuName(str, Enum):
    """
    SKU name.
    """
    DEV_NO_SL_A_STANDARD_D11_V2 = "Dev(No SLA)_Standard_D11_v2"
    DEV_NO_SL_A_STANDARD_E2A_V4 = "Dev(No SLA)_Standard_E2a_v4"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_D32D_V4 = "Standard_D32d_v4"
    STANDARD_D16D_V5 = "Standard_D16d_v5"
    STANDARD_D32D_V5 = "Standard_D32d_v5"
    STANDARD_DS13_V2_1_T_B_PS = "Standard_DS13_v2+1TB_PS"
    STANDARD_DS13_V2_2_T_B_PS = "Standard_DS13_v2+2TB_PS"
    STANDARD_DS14_V2_3_T_B_PS = "Standard_DS14_v2+3TB_PS"
    STANDARD_DS14_V2_4_T_B_PS = "Standard_DS14_v2+4TB_PS"
    STANDARD_L4S = "Standard_L4s"
    STANDARD_L8S = "Standard_L8s"
    STANDARD_L16S = "Standard_L16s"
    STANDARD_L8S_V2 = "Standard_L8s_v2"
    STANDARD_L16S_V2 = "Standard_L16s_v2"
    STANDARD_E64I_V3 = "Standard_E64i_v3"
    STANDARD_E80IDS_V4 = "Standard_E80ids_v4"
    STANDARD_E2A_V4 = "Standard_E2a_v4"
    STANDARD_E4A_V4 = "Standard_E4a_v4"
    STANDARD_E8A_V4 = "Standard_E8a_v4"
    STANDARD_E16A_V4 = "Standard_E16a_v4"
    STANDARD_E8AS_V4_1_T_B_PS = "Standard_E8as_v4+1TB_PS"
    STANDARD_E8AS_V4_2_T_B_PS = "Standard_E8as_v4+2TB_PS"
    STANDARD_E16AS_V4_3_T_B_PS = "Standard_E16as_v4+3TB_PS"
    STANDARD_E16AS_V4_4_T_B_PS = "Standard_E16as_v4+4TB_PS"
    STANDARD_E8AS_V5_1_T_B_PS = "Standard_E8as_v5+1TB_PS"
    STANDARD_E8AS_V5_2_T_B_PS = "Standard_E8as_v5+2TB_PS"
    STANDARD_E16AS_V5_3_T_B_PS = "Standard_E16as_v5+3TB_PS"
    STANDARD_E16AS_V5_4_T_B_PS = "Standard_E16as_v5+4TB_PS"
    STANDARD_E2ADS_V5 = "Standard_E2ads_v5"
    STANDARD_E4ADS_V5 = "Standard_E4ads_v5"
    STANDARD_E8ADS_V5 = "Standard_E8ads_v5"
    STANDARD_E16ADS_V5 = "Standard_E16ads_v5"
    STANDARD_E8S_V4_1_T_B_PS = "Standard_E8s_v4+1TB_PS"
    STANDARD_E8S_V4_2_T_B_PS = "Standard_E8s_v4+2TB_PS"
    STANDARD_E16S_V4_3_T_B_PS = "Standard_E16s_v4+3TB_PS"
    STANDARD_E16S_V4_4_T_B_PS = "Standard_E16s_v4+4TB_PS"
    STANDARD_E8S_V5_1_T_B_PS = "Standard_E8s_v5+1TB_PS"
    STANDARD_E8S_V5_2_T_B_PS = "Standard_E8s_v5+2TB_PS"
    STANDARD_E16S_V5_3_T_B_PS = "Standard_E16s_v5+3TB_PS"
    STANDARD_E16S_V5_4_T_B_PS = "Standard_E16s_v5+4TB_PS"


class AzureSkuTier(str, Enum):
    """
    SKU tier.
    """
    BASIC = "Basic"
    STANDARD = "Standard"


class BlobStorageEventType(str, Enum):
    """
    The name of blob storage event type to process.
    """
    MICROSOFT_STORAGE_BLOB_CREATED = "Microsoft.Storage.BlobCreated"
    MICROSOFT_STORAGE_BLOB_RENAMED = "Microsoft.Storage.BlobRenamed"


class ClusterNetworkAccessFlag(str, Enum):
    """
    Whether or not to restrict outbound network access.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ClusterPrincipalRole(str, Enum):
    """
    Cluster principal role.
    """
    ALL_DATABASES_ADMIN = "AllDatabasesAdmin"
    ALL_DATABASES_VIEWER = "AllDatabasesViewer"


class Compression(str, Enum):
    """
    The event hub messages compression type
    """
    NONE = "None"
    G_ZIP = "GZip"


class DataConnectionKind(str, Enum):
    """
    Kind of the endpoint for the data connection
    """
    EVENT_HUB = "EventHub"
    EVENT_GRID = "EventGrid"
    IOT_HUB = "IotHub"


class DatabasePrincipalRole(str, Enum):
    """
    Database principal role.
    """
    ADMIN = "Admin"
    INGESTOR = "Ingestor"
    MONITOR = "Monitor"
    USER = "User"
    UNRESTRICTED_VIEWER = "UnrestrictedViewer"
    VIEWER = "Viewer"


class DatabaseRouting(str, Enum):
    """
    Indication for database routing information from the data connection, by default only database routing information is allowed
    """
    SINGLE = "Single"
    MULTI = "Multi"


class DefaultPrincipalsModificationKind(str, Enum):
    """
    The default principals modification kind
    """
    UNION = "Union"
    REPLACE = "Replace"
    NONE = "None"


class EngineType(str, Enum):
    """
    The engine type
    """
    V2 = "V2"
    V3 = "V3"


class EventGridDataFormat(str, Enum):
    """
    The data format of the message. Optionally the data format can be added to each message.
    """
    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"


class EventHubDataFormat(str, Enum):
    """
    The data format of the message. Optionally the data format can be added to each message.
    """
    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"


class IdentityType(str, Enum):
    """
    The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user-assigned identities. The type 'None' will remove all identities.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class IotHubDataFormat(str, Enum):
    """
    The data format of the message. Optionally the data format can be added to each message.
    """
    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"


class Kind(str, Enum):
    """
    Kind of the database
    """
    READ_WRITE = "ReadWrite"
    READ_ONLY_FOLLOWING = "ReadOnlyFollowing"


class PrincipalType(str, Enum):
    """
    Principal type.
    """
    APP = "App"
    GROUP = "Group"
    USER = "User"


class PublicIPType(str, Enum):
    """
    Indicates what public IP type to create - IPv4 (default), or DualStack (both IPv4 and IPv6)
    """
    I_PV4 = "IPv4"
    DUAL_STACK = "DualStack"


class PublicNetworkAccess(str, Enum):
    """
    Public network access to the cluster is enabled by default. When disabled, only private endpoint connection to the cluster is allowed
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
