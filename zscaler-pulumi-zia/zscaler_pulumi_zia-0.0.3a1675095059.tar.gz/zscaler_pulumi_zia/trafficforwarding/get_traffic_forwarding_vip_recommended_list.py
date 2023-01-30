# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetTrafficForwardingVIPRecommendedListResult',
    'AwaitableGetTrafficForwardingVIPRecommendedListResult',
    'get_traffic_forwarding_vip_recommended_list',
    'get_traffic_forwarding_vip_recommended_list_output',
]

@pulumi.output_type
class GetTrafficForwardingVIPRecommendedListResult:
    """
    A collection of values returned by getTrafficForwardingVIPRecommendedList.
    """
    def __init__(__self__, geo_override=None, id=None, lists=None, required_count=None, routable_ip=None, source_ip=None):
        if geo_override and not isinstance(geo_override, bool):
            raise TypeError("Expected argument 'geo_override' to be a bool")
        pulumi.set(__self__, "geo_override", geo_override)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lists and not isinstance(lists, list):
            raise TypeError("Expected argument 'lists' to be a list")
        pulumi.set(__self__, "lists", lists)
        if required_count and not isinstance(required_count, int):
            raise TypeError("Expected argument 'required_count' to be a int")
        pulumi.set(__self__, "required_count", required_count)
        if routable_ip and not isinstance(routable_ip, bool):
            raise TypeError("Expected argument 'routable_ip' to be a bool")
        pulumi.set(__self__, "routable_ip", routable_ip)
        if source_ip and not isinstance(source_ip, str):
            raise TypeError("Expected argument 'source_ip' to be a str")
        pulumi.set(__self__, "source_ip", source_ip)

    @property
    @pulumi.getter(name="geoOverride")
    def geo_override(self) -> Optional[bool]:
        return pulumi.get(self, "geo_override")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def lists(self) -> Sequence['outputs.GetTrafficForwardingVIPRecommendedListListResult']:
        return pulumi.get(self, "lists")

    @property
    @pulumi.getter(name="requiredCount")
    def required_count(self) -> Optional[int]:
        return pulumi.get(self, "required_count")

    @property
    @pulumi.getter(name="routableIp")
    def routable_ip(self) -> Optional[bool]:
        return pulumi.get(self, "routable_ip")

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[str]:
        """
        (String) The public source IP address.
        """
        return pulumi.get(self, "source_ip")


class AwaitableGetTrafficForwardingVIPRecommendedListResult(GetTrafficForwardingVIPRecommendedListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrafficForwardingVIPRecommendedListResult(
            geo_override=self.geo_override,
            id=self.id,
            lists=self.lists,
            required_count=self.required_count,
            routable_ip=self.routable_ip,
            source_ip=self.source_ip)


def get_traffic_forwarding_vip_recommended_list(geo_override: Optional[bool] = None,
                                                required_count: Optional[int] = None,
                                                routable_ip: Optional[bool] = None,
                                                source_ip: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrafficForwardingVIPRecommendedListResult:
    """
    Use the **zia_gre_vip_recommended_list** data source to get information about a list of recommended GRE tunnel virtual IP addresses (VIPs), based on source IP address or latitude/longitude coordinates.


    :param str source_ip: (String) The public source IP address.
    """
    __args__ = dict()
    __args__['geoOverride'] = geo_override
    __args__['requiredCount'] = required_count
    __args__['routableIp'] = routable_ip
    __args__['sourceIp'] = source_ip
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('zia:TrafficForwarding/getTrafficForwardingVIPRecommendedList:getTrafficForwardingVIPRecommendedList', __args__, opts=opts, typ=GetTrafficForwardingVIPRecommendedListResult).value

    return AwaitableGetTrafficForwardingVIPRecommendedListResult(
        geo_override=__ret__.geo_override,
        id=__ret__.id,
        lists=__ret__.lists,
        required_count=__ret__.required_count,
        routable_ip=__ret__.routable_ip,
        source_ip=__ret__.source_ip)


@_utilities.lift_output_func(get_traffic_forwarding_vip_recommended_list)
def get_traffic_forwarding_vip_recommended_list_output(geo_override: Optional[pulumi.Input[Optional[bool]]] = None,
                                                       required_count: Optional[pulumi.Input[Optional[int]]] = None,
                                                       routable_ip: Optional[pulumi.Input[Optional[bool]]] = None,
                                                       source_ip: Optional[pulumi.Input[Optional[str]]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrafficForwardingVIPRecommendedListResult]:
    """
    Use the **zia_gre_vip_recommended_list** data source to get information about a list of recommended GRE tunnel virtual IP addresses (VIPs), based on source IP address or latitude/longitude coordinates.


    :param str source_ip: (String) The public source IP address.
    """
    ...
