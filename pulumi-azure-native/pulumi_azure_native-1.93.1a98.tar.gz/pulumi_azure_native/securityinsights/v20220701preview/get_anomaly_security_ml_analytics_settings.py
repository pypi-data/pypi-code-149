# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetAnomalySecurityMLAnalyticsSettingsResult',
    'AwaitableGetAnomalySecurityMLAnalyticsSettingsResult',
    'get_anomaly_security_ml_analytics_settings',
    'get_anomaly_security_ml_analytics_settings_output',
]

@pulumi.output_type
class GetAnomalySecurityMLAnalyticsSettingsResult:
    """
    Represents Anomaly Security ML Analytics Settings
    """
    def __init__(__self__, anomaly_settings_version=None, anomaly_version=None, customizable_observations=None, description=None, display_name=None, enabled=None, etag=None, frequency=None, id=None, is_default_settings=None, kind=None, last_modified_utc=None, name=None, required_data_connectors=None, settings_definition_id=None, settings_status=None, system_data=None, tactics=None, techniques=None, type=None):
        if anomaly_settings_version and not isinstance(anomaly_settings_version, int):
            raise TypeError("Expected argument 'anomaly_settings_version' to be a int")
        pulumi.set(__self__, "anomaly_settings_version", anomaly_settings_version)
        if anomaly_version and not isinstance(anomaly_version, str):
            raise TypeError("Expected argument 'anomaly_version' to be a str")
        pulumi.set(__self__, "anomaly_version", anomaly_version)
        if customizable_observations and not isinstance(customizable_observations, dict):
            raise TypeError("Expected argument 'customizable_observations' to be a dict")
        pulumi.set(__self__, "customizable_observations", customizable_observations)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if frequency and not isinstance(frequency, str):
            raise TypeError("Expected argument 'frequency' to be a str")
        pulumi.set(__self__, "frequency", frequency)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_default_settings and not isinstance(is_default_settings, bool):
            raise TypeError("Expected argument 'is_default_settings' to be a bool")
        pulumi.set(__self__, "is_default_settings", is_default_settings)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if last_modified_utc and not isinstance(last_modified_utc, str):
            raise TypeError("Expected argument 'last_modified_utc' to be a str")
        pulumi.set(__self__, "last_modified_utc", last_modified_utc)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if required_data_connectors and not isinstance(required_data_connectors, list):
            raise TypeError("Expected argument 'required_data_connectors' to be a list")
        pulumi.set(__self__, "required_data_connectors", required_data_connectors)
        if settings_definition_id and not isinstance(settings_definition_id, str):
            raise TypeError("Expected argument 'settings_definition_id' to be a str")
        pulumi.set(__self__, "settings_definition_id", settings_definition_id)
        if settings_status and not isinstance(settings_status, str):
            raise TypeError("Expected argument 'settings_status' to be a str")
        pulumi.set(__self__, "settings_status", settings_status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tactics and not isinstance(tactics, list):
            raise TypeError("Expected argument 'tactics' to be a list")
        pulumi.set(__self__, "tactics", tactics)
        if techniques and not isinstance(techniques, list):
            raise TypeError("Expected argument 'techniques' to be a list")
        pulumi.set(__self__, "techniques", techniques)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="anomalySettingsVersion")
    def anomaly_settings_version(self) -> Optional[int]:
        """
        The anomaly settings version of the Anomaly security ml analytics settings that dictates whether job version gets updated or not.
        """
        return pulumi.get(self, "anomaly_settings_version")

    @property
    @pulumi.getter(name="anomalyVersion")
    def anomaly_version(self) -> str:
        """
        The anomaly version of the AnomalySecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "anomaly_version")

    @property
    @pulumi.getter(name="customizableObservations")
    def customizable_observations(self) -> Optional[Any]:
        """
        The customizable observations of the AnomalySecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "customizable_observations")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the SecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name for settings created by this SecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Determines whether this settings is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def frequency(self) -> str:
        """
        The frequency that this SecurityMLAnalyticsSettings will be run.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDefaultSettings")
    def is_default_settings(self) -> bool:
        """
        Determines whether this anomaly security ml analytics settings is a default settings
        """
        return pulumi.get(self, "is_default_settings")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of security ML analytics settings
        Expected value is 'Anomaly'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> str:
        """
        The last time that this SecurityMLAnalyticsSettings has been modified.
        """
        return pulumi.get(self, "last_modified_utc")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requiredDataConnectors")
    def required_data_connectors(self) -> Optional[Sequence['outputs.SecurityMLAnalyticsSettingsDataSourceResponse']]:
        """
        The required data sources for this SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "required_data_connectors")

    @property
    @pulumi.getter(name="settingsDefinitionId")
    def settings_definition_id(self) -> Optional[str]:
        """
        The anomaly settings definition Id
        """
        return pulumi.get(self, "settings_definition_id")

    @property
    @pulumi.getter(name="settingsStatus")
    def settings_status(self) -> str:
        """
        The anomaly SecurityMLAnalyticsSettings status
        """
        return pulumi.get(self, "settings_status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tactics(self) -> Optional[Sequence[str]]:
        """
        The tactics of the SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "tactics")

    @property
    @pulumi.getter
    def techniques(self) -> Optional[Sequence[str]]:
        """
        The techniques of the SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "techniques")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAnomalySecurityMLAnalyticsSettingsResult(GetAnomalySecurityMLAnalyticsSettingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAnomalySecurityMLAnalyticsSettingsResult(
            anomaly_settings_version=self.anomaly_settings_version,
            anomaly_version=self.anomaly_version,
            customizable_observations=self.customizable_observations,
            description=self.description,
            display_name=self.display_name,
            enabled=self.enabled,
            etag=self.etag,
            frequency=self.frequency,
            id=self.id,
            is_default_settings=self.is_default_settings,
            kind=self.kind,
            last_modified_utc=self.last_modified_utc,
            name=self.name,
            required_data_connectors=self.required_data_connectors,
            settings_definition_id=self.settings_definition_id,
            settings_status=self.settings_status,
            system_data=self.system_data,
            tactics=self.tactics,
            techniques=self.techniques,
            type=self.type)


def get_anomaly_security_ml_analytics_settings(resource_group_name: Optional[str] = None,
                                               settings_resource_name: Optional[str] = None,
                                               workspace_name: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAnomalySecurityMLAnalyticsSettingsResult:
    """
    Represents Anomaly Security ML Analytics Settings


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str settings_resource_name: Security ML Analytics Settings resource name
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['settingsResourceName'] = settings_resource_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20220701preview:getAnomalySecurityMLAnalyticsSettings', __args__, opts=opts, typ=GetAnomalySecurityMLAnalyticsSettingsResult).value

    return AwaitableGetAnomalySecurityMLAnalyticsSettingsResult(
        anomaly_settings_version=__ret__.anomaly_settings_version,
        anomaly_version=__ret__.anomaly_version,
        customizable_observations=__ret__.customizable_observations,
        description=__ret__.description,
        display_name=__ret__.display_name,
        enabled=__ret__.enabled,
        etag=__ret__.etag,
        frequency=__ret__.frequency,
        id=__ret__.id,
        is_default_settings=__ret__.is_default_settings,
        kind=__ret__.kind,
        last_modified_utc=__ret__.last_modified_utc,
        name=__ret__.name,
        required_data_connectors=__ret__.required_data_connectors,
        settings_definition_id=__ret__.settings_definition_id,
        settings_status=__ret__.settings_status,
        system_data=__ret__.system_data,
        tactics=__ret__.tactics,
        techniques=__ret__.techniques,
        type=__ret__.type)


@_utilities.lift_output_func(get_anomaly_security_ml_analytics_settings)
def get_anomaly_security_ml_analytics_settings_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                      settings_resource_name: Optional[pulumi.Input[str]] = None,
                                                      workspace_name: Optional[pulumi.Input[str]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAnomalySecurityMLAnalyticsSettingsResult]:
    """
    Represents Anomaly Security ML Analytics Settings


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str settings_resource_name: Security ML Analytics Settings resource name
    :param str workspace_name: The name of the workspace.
    """
    ...
