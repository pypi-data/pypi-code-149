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
    'GetRouteFilterResult',
    'AwaitableGetRouteFilterResult',
    'get_route_filter',
    'get_route_filter_output',
]

@pulumi.output_type
class GetRouteFilterResult:
    """
    Route Filter Resource.
    """
    def __init__(__self__, etag=None, id=None, ipv6_peerings=None, location=None, name=None, peerings=None, provisioning_state=None, rules=None, tags=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv6_peerings and not isinstance(ipv6_peerings, list):
            raise TypeError("Expected argument 'ipv6_peerings' to be a list")
        pulumi.set(__self__, "ipv6_peerings", ipv6_peerings)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peerings and not isinstance(peerings, list):
            raise TypeError("Expected argument 'peerings' to be a list")
        pulumi.set(__self__, "peerings", peerings)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv6Peerings")
    def ipv6_peerings(self) -> Sequence['outputs.ExpressRouteCircuitPeeringResponse']:
        """
        A collection of references to express route circuit ipv6 peerings.
        """
        return pulumi.get(self, "ipv6_peerings")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def peerings(self) -> Sequence['outputs.ExpressRouteCircuitPeeringResponse']:
        """
        A collection of references to express route circuit peerings.
        """
        return pulumi.get(self, "peerings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the route filter resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.RouteFilterRuleResponse']]:
        """
        Collection of RouteFilterRules contained within a route filter.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetRouteFilterResult(GetRouteFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteFilterResult(
            etag=self.etag,
            id=self.id,
            ipv6_peerings=self.ipv6_peerings,
            location=self.location,
            name=self.name,
            peerings=self.peerings,
            provisioning_state=self.provisioning_state,
            rules=self.rules,
            tags=self.tags,
            type=self.type)


def get_route_filter(expand: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     route_filter_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteFilterResult:
    """
    Route Filter Resource.


    :param str expand: Expands referenced express route bgp peering resources.
    :param str resource_group_name: The name of the resource group.
    :param str route_filter_name: The name of the route filter.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['routeFilterName'] = route_filter_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20200401:getRouteFilter', __args__, opts=opts, typ=GetRouteFilterResult).value

    return AwaitableGetRouteFilterResult(
        etag=__ret__.etag,
        id=__ret__.id,
        ipv6_peerings=__ret__.ipv6_peerings,
        location=__ret__.location,
        name=__ret__.name,
        peerings=__ret__.peerings,
        provisioning_state=__ret__.provisioning_state,
        rules=__ret__.rules,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_route_filter)
def get_route_filter_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            route_filter_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteFilterResult]:
    """
    Route Filter Resource.


    :param str expand: Expands referenced express route bgp peering resources.
    :param str resource_group_name: The name of the resource group.
    :param str route_filter_name: The name of the route filter.
    """
    ...
