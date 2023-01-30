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
from ._enums import *

__all__ = ['DatabaseSecurityAlertPolicyArgs', 'DatabaseSecurityAlertPolicy']

@pulumi.input_type
class DatabaseSecurityAlertPolicyArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 state: pulumi.Input['SecurityAlertsPolicyState'],
                 disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email_account_admins: Optional[pulumi.Input[bool]] = None,
                 email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 security_alert_policy_name: Optional[pulumi.Input[str]] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatabaseSecurityAlertPolicy resource.
        :param pulumi.Input[str] database_name: The name of the  database for which the security alert policy is defined.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the  server.
        :param pulumi.Input['SecurityAlertsPolicyState'] state: Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disabled_alerts: Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action, Brute_Force
        :param pulumi.Input[bool] email_account_admins: Specifies that the alert is sent to the account administrators.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_addresses: Specifies an array of e-mail addresses to which the alert is sent.
        :param pulumi.Input[int] retention_days: Specifies the number of days to keep in the Threat Detection audit logs.
        :param pulumi.Input[str] security_alert_policy_name: The name of the security alert policy.
        :param pulumi.Input[str] storage_account_access_key: Specifies the identifier key of the Threat Detection audit storage account.
        :param pulumi.Input[str] storage_endpoint: Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs.
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        pulumi.set(__self__, "state", state)
        if disabled_alerts is not None:
            pulumi.set(__self__, "disabled_alerts", disabled_alerts)
        if email_account_admins is not None:
            pulumi.set(__self__, "email_account_admins", email_account_admins)
        if email_addresses is not None:
            pulumi.set(__self__, "email_addresses", email_addresses)
        if retention_days is not None:
            pulumi.set(__self__, "retention_days", retention_days)
        if security_alert_policy_name is not None:
            pulumi.set(__self__, "security_alert_policy_name", security_alert_policy_name)
        if storage_account_access_key is not None:
            pulumi.set(__self__, "storage_account_access_key", storage_account_access_key)
        if storage_endpoint is not None:
            pulumi.set(__self__, "storage_endpoint", storage_endpoint)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the  database for which the security alert policy is defined.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the  server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Input['SecurityAlertsPolicyState']:
        """
        Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: pulumi.Input['SecurityAlertsPolicyState']):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action, Brute_Force
        """
        return pulumi.get(self, "disabled_alerts")

    @disabled_alerts.setter
    def disabled_alerts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "disabled_alerts", value)

    @property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies that the alert is sent to the account administrators.
        """
        return pulumi.get(self, "email_account_admins")

    @email_account_admins.setter
    def email_account_admins(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "email_account_admins", value)

    @property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies an array of e-mail addresses to which the alert is sent.
        """
        return pulumi.get(self, "email_addresses")

    @email_addresses.setter
    def email_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "email_addresses", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the number of days to keep in the Threat Detection audit logs.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_days", value)

    @property
    @pulumi.getter(name="securityAlertPolicyName")
    def security_alert_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the security alert policy.
        """
        return pulumi.get(self, "security_alert_policy_name")

    @security_alert_policy_name.setter
    def security_alert_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_alert_policy_name", value)

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the identifier key of the Threat Detection audit storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @storage_account_access_key.setter
    def storage_account_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_access_key", value)

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs.
        """
        return pulumi.get(self, "storage_endpoint")

    @storage_endpoint.setter
    def storage_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_endpoint", value)


class DatabaseSecurityAlertPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email_account_admins: Optional[pulumi.Input[bool]] = None,
                 email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 security_alert_policy_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['SecurityAlertsPolicyState']] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A database security alert policy.
        API Version: 2020-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name of the  database for which the security alert policy is defined.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] disabled_alerts: Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action, Brute_Force
        :param pulumi.Input[bool] email_account_admins: Specifies that the alert is sent to the account administrators.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_addresses: Specifies an array of e-mail addresses to which the alert is sent.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[int] retention_days: Specifies the number of days to keep in the Threat Detection audit logs.
        :param pulumi.Input[str] security_alert_policy_name: The name of the security alert policy.
        :param pulumi.Input[str] server_name: The name of the  server.
        :param pulumi.Input['SecurityAlertsPolicyState'] state: Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.
        :param pulumi.Input[str] storage_account_access_key: Specifies the identifier key of the Threat Detection audit storage account.
        :param pulumi.Input[str] storage_endpoint: Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseSecurityAlertPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A database security alert policy.
        API Version: 2020-11-01-preview.

        :param str resource_name: The name of the resource.
        :param DatabaseSecurityAlertPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseSecurityAlertPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 disabled_alerts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email_account_admins: Optional[pulumi.Input[bool]] = None,
                 email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 security_alert_policy_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['SecurityAlertsPolicyState']] = None,
                 storage_account_access_key: Optional[pulumi.Input[str]] = None,
                 storage_endpoint: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseSecurityAlertPolicyArgs.__new__(DatabaseSecurityAlertPolicyArgs)

            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["disabled_alerts"] = disabled_alerts
            __props__.__dict__["email_account_admins"] = email_account_admins
            __props__.__dict__["email_addresses"] = email_addresses
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["retention_days"] = retention_days
            __props__.__dict__["security_alert_policy_name"] = security_alert_policy_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            if state is None and not opts.urn:
                raise TypeError("Missing required property 'state'")
            __props__.__dict__["state"] = state
            __props__.__dict__["storage_account_access_key"] = storage_account_access_key
            __props__.__dict__["storage_endpoint"] = storage_endpoint
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql/v20140401:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20180601preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20200202preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20200801preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20201101preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20210201preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20210501preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20210801preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20211101:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20211101preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20220201preview:DatabaseSecurityAlertPolicy"), pulumi.Alias(type_="azure-native:sql/v20220501preview:DatabaseSecurityAlertPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DatabaseSecurityAlertPolicy, __self__).__init__(
            'azure-native:sql:DatabaseSecurityAlertPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatabaseSecurityAlertPolicy':
        """
        Get an existing DatabaseSecurityAlertPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatabaseSecurityAlertPolicyArgs.__new__(DatabaseSecurityAlertPolicyArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["disabled_alerts"] = None
        __props__.__dict__["email_account_admins"] = None
        __props__.__dict__["email_addresses"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["retention_days"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["storage_account_access_key"] = None
        __props__.__dict__["storage_endpoint"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return DatabaseSecurityAlertPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Specifies the UTC creation time of the policy.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="disabledAlerts")
    def disabled_alerts(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action, Brute_Force
        """
        return pulumi.get(self, "disabled_alerts")

    @property
    @pulumi.getter(name="emailAccountAdmins")
    def email_account_admins(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies that the alert is sent to the account administrators.
        """
        return pulumi.get(self, "email_account_admins")

    @property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies an array of e-mail addresses to which the alert is sent.
        """
        return pulumi.get(self, "email_addresses")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the number of days to keep in the Threat Detection audit logs.
        """
        return pulumi.get(self, "retention_days")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageAccountAccessKey")
    def storage_account_access_key(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the identifier key of the Threat Detection audit storage account.
        """
        return pulumi.get(self, "storage_account_access_key")

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). This blob storage will hold all Threat Detection audit logs.
        """
        return pulumi.get(self, "storage_endpoint")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        SystemData of SecurityAlertPolicyResource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

