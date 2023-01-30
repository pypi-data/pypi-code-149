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
    'GetDedicatedCloudServiceResult',
    'AwaitableGetDedicatedCloudServiceResult',
    'get_dedicated_cloud_service',
    'get_dedicated_cloud_service_output',
]

@pulumi.output_type
class GetDedicatedCloudServiceResult:
    """
    Dedicated cloud service model
    """
    def __init__(__self__, gateway_subnet=None, id=None, is_account_onboarded=None, location=None, name=None, nodes=None, service_url=None, tags=None, type=None):
        if gateway_subnet and not isinstance(gateway_subnet, str):
            raise TypeError("Expected argument 'gateway_subnet' to be a str")
        pulumi.set(__self__, "gateway_subnet", gateway_subnet)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_account_onboarded and not isinstance(is_account_onboarded, str):
            raise TypeError("Expected argument 'is_account_onboarded' to be a str")
        pulumi.set(__self__, "is_account_onboarded", is_account_onboarded)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nodes and not isinstance(nodes, int):
            raise TypeError("Expected argument 'nodes' to be a int")
        pulumi.set(__self__, "nodes", nodes)
        if service_url and not isinstance(service_url, str):
            raise TypeError("Expected argument 'service_url' to be a str")
        pulumi.set(__self__, "service_url", service_url)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="gatewaySubnet")
    def gateway_subnet(self) -> str:
        """
        gateway Subnet for the account. It will collect the subnet address and always treat it as /28
        """
        return pulumi.get(self, "gateway_subnet")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAccountOnboarded")
    def is_account_onboarded(self) -> str:
        """
        indicates whether account onboarded or not in a given region
        """
        return pulumi.get(self, "is_account_onboarded")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Azure region
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        {dedicatedCloudServiceName}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nodes(self) -> int:
        """
        total nodes purchased
        """
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter(name="serviceURL")
    def service_url(self) -> str:
        """
        link to a service management web portal
        """
        return pulumi.get(self, "service_url")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The list of tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        {resourceProviderNamespace}/{resourceType}
        """
        return pulumi.get(self, "type")


class AwaitableGetDedicatedCloudServiceResult(GetDedicatedCloudServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDedicatedCloudServiceResult(
            gateway_subnet=self.gateway_subnet,
            id=self.id,
            is_account_onboarded=self.is_account_onboarded,
            location=self.location,
            name=self.name,
            nodes=self.nodes,
            service_url=self.service_url,
            tags=self.tags,
            type=self.type)


def get_dedicated_cloud_service(dedicated_cloud_service_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDedicatedCloudServiceResult:
    """
    Dedicated cloud service model


    :param str dedicated_cloud_service_name: dedicated cloud Service name
    :param str resource_group_name: The name of the resource group
    """
    __args__ = dict()
    __args__['dedicatedCloudServiceName'] = dedicated_cloud_service_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:vmwarecloudsimple/v20190401:getDedicatedCloudService', __args__, opts=opts, typ=GetDedicatedCloudServiceResult).value

    return AwaitableGetDedicatedCloudServiceResult(
        gateway_subnet=__ret__.gateway_subnet,
        id=__ret__.id,
        is_account_onboarded=__ret__.is_account_onboarded,
        location=__ret__.location,
        name=__ret__.name,
        nodes=__ret__.nodes,
        service_url=__ret__.service_url,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_dedicated_cloud_service)
def get_dedicated_cloud_service_output(dedicated_cloud_service_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDedicatedCloudServiceResult]:
    """
    Dedicated cloud service model


    :param str dedicated_cloud_service_name: dedicated cloud Service name
    :param str resource_group_name: The name of the resource group
    """
    ...
