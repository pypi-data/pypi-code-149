# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetMaintenanceConfigurationResult',
    'AwaitableGetMaintenanceConfigurationResult',
    'get_maintenance_configuration',
    'get_maintenance_configuration_output',
]

@pulumi.output_type
class GetMaintenanceConfigurationResult:
    """
    Maintenance configuration record type
    """
    def __init__(__self__, extension_properties=None, id=None, location=None, maintenance_scope=None, name=None, namespace=None, tags=None, type=None):
        if extension_properties and not isinstance(extension_properties, dict):
            raise TypeError("Expected argument 'extension_properties' to be a dict")
        pulumi.set(__self__, "extension_properties", extension_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_scope and not isinstance(maintenance_scope, str):
            raise TypeError("Expected argument 'maintenance_scope' to be a str")
        pulumi.set(__self__, "maintenance_scope", maintenance_scope)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="extensionProperties")
    def extension_properties(self) -> Optional[Mapping[str, str]]:
        """
        Gets or sets extensionProperties of the maintenanceConfiguration. This is for future use only and would be a set of key value pairs for additional information e.g. whether to follow SDP etc.
        """
        return pulumi.get(self, "extension_properties")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Gets or sets location of the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceScope")
    def maintenance_scope(self) -> Optional[str]:
        """
        Gets or sets maintenanceScope of the configuration. It represent the impact area of the maintenance
        """
        return pulumi.get(self, "maintenance_scope")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        Gets or sets namespace of the resource e.g. Microsoft.Maintenance or Microsoft.Sql
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Gets or sets tags of the resource
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource
        """
        return pulumi.get(self, "type")


class AwaitableGetMaintenanceConfigurationResult(GetMaintenanceConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMaintenanceConfigurationResult(
            extension_properties=self.extension_properties,
            id=self.id,
            location=self.location,
            maintenance_scope=self.maintenance_scope,
            name=self.name,
            namespace=self.namespace,
            tags=self.tags,
            type=self.type)


def get_maintenance_configuration(resource_group_name: Optional[str] = None,
                                  resource_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMaintenanceConfigurationResult:
    """
    Maintenance configuration record type


    :param str resource_group_name: Resource Group Name
    :param str resource_name: Resource Identifier
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:maintenance/v20200401:getMaintenanceConfiguration', __args__, opts=opts, typ=GetMaintenanceConfigurationResult).value

    return AwaitableGetMaintenanceConfigurationResult(
        extension_properties=__ret__.extension_properties,
        id=__ret__.id,
        location=__ret__.location,
        maintenance_scope=__ret__.maintenance_scope,
        name=__ret__.name,
        namespace=__ret__.namespace,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_maintenance_configuration)
def get_maintenance_configuration_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                         resource_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMaintenanceConfigurationResult]:
    """
    Maintenance configuration record type


    :param str resource_group_name: Resource Group Name
    :param str resource_name: Resource Identifier
    """
    ...
