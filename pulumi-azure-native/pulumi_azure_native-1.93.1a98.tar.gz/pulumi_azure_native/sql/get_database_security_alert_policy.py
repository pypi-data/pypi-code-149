# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetDatabaseSecurityAlertPolicyResult',
    'AwaitableGetDatabaseSecurityAlertPolicyResult',
    'get_database_security_alert_policy',
    'get_database_security_alert_policy_output',
]

@pulumi.output_type
class GetDatabaseSecurityAlertPolicyResult:
    """
    A database security alert policy.
    """
    def __init__(__self__, creation_time=None, disabled_alerts=None, email_account_admins=None, email_addresses=None, id=None, name=None, retention_days=None, state=None, storage_account_access_key=None, storage_endpoint=None, system_data=None, type=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if disabled_alerts and not isinstance(disabled_alerts, list):
            raise TypeError("Expected argument 'disabled_alerts' to be a list")
        pulumi.set(__self__, "disabled_alerts", disabled_alerts)
        if email_account_admins and not isinstance(email_account_admins, bool):
            raise TypeError("Expected argument 'email_account_admins' to be a bool")
        pulumi.set(__self__, "email_account_admins", email_account_admins)
        if email_addresses and not isinstance(email_addresses, list):
            raise TypeError("Expected argument 'email_addresses' to be a list")
        pulumi.set(__self__, "email_addresses", email_addresses)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if retention_days and not isinstance(retention_days, int):
            raise TypeError("Expected argument 'retention_days' to be a int")
        pulumi.set(__self__, "retention_days", retention_days)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_account_access_key and not isinstance(storage_account_access_key, str):
            raise TypeError("Expected argument 'storage_account_access_key' to be a str")
        pulumi.set(__self__, "storage_account_access_key", storage_account_access_key)
        if storage_endpoint and not isinstance(storage_endpoint, str):
            raise TypeError("Expected argument 'storage_endpoint' to be a str")
        pulumi.set(__self__, "storage_endpoint", storage_endpoint)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        Specifies the UTC creation time of the policy.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> Optional[Sequence[str]]:
        """
        Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action, Brute_Force
        """
        return pulumi.get(self, "disabled_alerts")

    @property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(self) -> Optional[bool]:
        """
        Specifies that the alert is sent to the account administrators.
        """
        return pulumi.get(self, "email_account_admins")

    @property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[Sequence[str]]:
        """
        Specifies an array of e-mail addresses to which the alert is sent.
        """
        return pulumi.get(self, "email_addresses")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[int]:
        """
        Specifies the number of days to keep in the Threat Detection audit logs.
        """
        return pulumi.get(self, "retention_days")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[str]:
        """
        Specifies the identifier key of the Threat Detection audit storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[str]:
        """
        Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs.
        """
        return pulumi.get(self, "storage_endpoint")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        SystemData of SecurityAlertPolicyResource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetDatabaseSecurityAlertPolicyResult(GetDatabaseSecurityAlertPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseSecurityAlertPolicyResult(
            creation_time=self.creation_time,
            disabled_alerts=self.disabled_alerts,
            email_account_admins=self.email_account_admins,
            email_addresses=self.email_addresses,
            id=self.id,
            name=self.name,
            retention_days=self.retention_days,
            state=self.state,
            storage_account_access_key=self.storage_account_access_key,
            storage_endpoint=self.storage_endpoint,
            system_data=self.system_data,
            type=self.type)


def get_database_security_alert_policy(database_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       security_alert_policy_name: Optional[str] = None,
                                       server_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseSecurityAlertPolicyResult:
    """
    A database security alert policy.
    API Version: 2020-11-01-preview.


    :param str database_name: The name of the  database for which the security alert policy is defined.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str security_alert_policy_name: The name of the security alert policy.
    :param str server_name: The name of the  server.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['securityAlertPolicyName'] = security_alert_policy_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql:getDatabaseSecurityAlertPolicy', __args__, opts=opts, typ=GetDatabaseSecurityAlertPolicyResult).value

    return AwaitableGetDatabaseSecurityAlertPolicyResult(
        creation_time=__ret__.creation_time,
        disabled_alerts=__ret__.disabled_alerts,
        email_account_admins=__ret__.email_account_admins,
        email_addresses=__ret__.email_addresses,
        id=__ret__.id,
        name=__ret__.name,
        retention_days=__ret__.retention_days,
        state=__ret__.state,
        storage_account_access_key=__ret__.storage_account_access_key,
        storage_endpoint=__ret__.storage_endpoint,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_database_security_alert_policy)
def get_database_security_alert_policy_output(database_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              security_alert_policy_name: Optional[pulumi.Input[str]] = None,
                                              server_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseSecurityAlertPolicyResult]:
    """
    A database security alert policy.
    API Version: 2020-11-01-preview.


    :param str database_name: The name of the  database for which the security alert policy is defined.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str security_alert_policy_name: The name of the security alert policy.
    :param str server_name: The name of the  server.
    """
    ...
