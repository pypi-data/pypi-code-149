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
from ._enums import *
from ._inputs import *

__all__ = ['EndpointInitArgs', 'Endpoint']

@pulumi.input_type
class EndpointInitArgs:
    def __init__(__self__, *,
                 endpoint_type: pulumi.Input[str],
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 always_serve: Optional[pulumi.Input[Union[str, 'AlwaysServe']]] = None,
                 custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPropertiesCustomHeadersArgs']]]] = None,
                 endpoint_location: Optional[pulumi.Input[str]] = None,
                 endpoint_monitor_status: Optional[pulumi.Input[Union[str, 'EndpointMonitorStatus']]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 endpoint_status: Optional[pulumi.Input[Union[str, 'EndpointStatus']]] = None,
                 geo_mapping: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 min_child_endpoints: Optional[pulumi.Input[float]] = None,
                 min_child_endpoints_i_pv4: Optional[pulumi.Input[float]] = None,
                 min_child_endpoints_i_pv6: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[float]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPropertiesSubnetsArgs']]]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a Endpoint resource.
        :param pulumi.Input[str] endpoint_type: The type of the Traffic Manager endpoint to be created or updated.
        :param pulumi.Input[str] profile_name: The name of the Traffic Manager profile.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'AlwaysServe']] always_serve: If Always Serve is enabled, probing for endpoint health will be disabled and endpoints will be included in the traffic routing method.
        :param pulumi.Input[Sequence[pulumi.Input['EndpointPropertiesCustomHeadersArgs']]] custom_headers: List of custom headers.
        :param pulumi.Input[str] endpoint_location: Specifies the location of the external or nested endpoints when using the 'Performance' traffic routing method.
        :param pulumi.Input[Union[str, 'EndpointMonitorStatus']] endpoint_monitor_status: The monitoring status of the endpoint.
        :param pulumi.Input[str] endpoint_name: The name of the Traffic Manager endpoint to be created or updated.
        :param pulumi.Input[Union[str, 'EndpointStatus']] endpoint_status: The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] geo_mapping: The list of countries/regions mapped to this endpoint when using the 'Geographic' traffic routing method. Please consult Traffic Manager Geographic documentation for a full list of accepted values.
        :param pulumi.Input[str] id: Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
        :param pulumi.Input[float] min_child_endpoints: The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        :param pulumi.Input[float] min_child_endpoints_i_pv4: The minimum number of IPv4 (DNS record type A) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        :param pulumi.Input[float] min_child_endpoints_i_pv6: The minimum number of IPv6 (DNS record type AAAA) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        :param pulumi.Input[str] name: The name of the resource
        :param pulumi.Input[float] priority: The priority of this endpoint when using the 'Priority' traffic routing method. Possible values are from 1 to 1000, lower values represent higher priority. This is an optional parameter.  If specified, it must be specified on all endpoints, and no two endpoints can share the same priority value.
        :param pulumi.Input[Sequence[pulumi.Input['EndpointPropertiesSubnetsArgs']]] subnets: The list of subnets, IP addresses, and/or address ranges mapped to this endpoint when using the 'Subnet' traffic routing method. An empty list will match all ranges not covered by other endpoints.
        :param pulumi.Input[str] target: The fully-qualified DNS name or IP address of the endpoint. Traffic Manager returns this value in DNS responses to direct traffic to this endpoint.
        :param pulumi.Input[str] target_resource_id: The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type 'ExternalEndpoints'.
        :param pulumi.Input[str] type: The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
        :param pulumi.Input[float] weight: The weight of this endpoint when using the 'Weighted' traffic routing method. Possible values are from 1 to 1000.
        """
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if always_serve is not None:
            pulumi.set(__self__, "always_serve", always_serve)
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if endpoint_location is not None:
            pulumi.set(__self__, "endpoint_location", endpoint_location)
        if endpoint_monitor_status is not None:
            pulumi.set(__self__, "endpoint_monitor_status", endpoint_monitor_status)
        if endpoint_name is not None:
            pulumi.set(__self__, "endpoint_name", endpoint_name)
        if endpoint_status is not None:
            pulumi.set(__self__, "endpoint_status", endpoint_status)
        if geo_mapping is not None:
            pulumi.set(__self__, "geo_mapping", geo_mapping)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if min_child_endpoints is not None:
            pulumi.set(__self__, "min_child_endpoints", min_child_endpoints)
        if min_child_endpoints_i_pv4 is not None:
            pulumi.set(__self__, "min_child_endpoints_i_pv4", min_child_endpoints_i_pv4)
        if min_child_endpoints_i_pv6 is not None:
            pulumi.set(__self__, "min_child_endpoints_i_pv6", min_child_endpoints_i_pv6)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if target_resource_id is not None:
            pulumi.set(__self__, "target_resource_id", target_resource_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The type of the Traffic Manager endpoint to be created or updated.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        The name of the Traffic Manager profile.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="alwaysServe")
    def always_serve(self) -> Optional[pulumi.Input[Union[str, 'AlwaysServe']]]:
        """
        If Always Serve is enabled, probing for endpoint health will be disabled and endpoints will be included in the traffic routing method.
        """
        return pulumi.get(self, "always_serve")

    @always_serve.setter
    def always_serve(self, value: Optional[pulumi.Input[Union[str, 'AlwaysServe']]]):
        pulumi.set(self, "always_serve", value)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPropertiesCustomHeadersArgs']]]]:
        """
        List of custom headers.
        """
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPropertiesCustomHeadersArgs']]]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter(name="endpointLocation")
    def endpoint_location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the location of the external or nested endpoints when using the 'Performance' traffic routing method.
        """
        return pulumi.get(self, "endpoint_location")

    @endpoint_location.setter
    def endpoint_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_location", value)

    @property
    @pulumi.getter(name="endpointMonitorStatus")
    def endpoint_monitor_status(self) -> Optional[pulumi.Input[Union[str, 'EndpointMonitorStatus']]]:
        """
        The monitoring status of the endpoint.
        """
        return pulumi.get(self, "endpoint_monitor_status")

    @endpoint_monitor_status.setter
    def endpoint_monitor_status(self, value: Optional[pulumi.Input[Union[str, 'EndpointMonitorStatus']]]):
        pulumi.set(self, "endpoint_monitor_status", value)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Traffic Manager endpoint to be created or updated.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter(name="endpointStatus")
    def endpoint_status(self) -> Optional[pulumi.Input[Union[str, 'EndpointStatus']]]:
        """
        The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method.
        """
        return pulumi.get(self, "endpoint_status")

    @endpoint_status.setter
    def endpoint_status(self, value: Optional[pulumi.Input[Union[str, 'EndpointStatus']]]):
        pulumi.set(self, "endpoint_status", value)

    @property
    @pulumi.getter(name="geoMapping")
    def geo_mapping(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of countries/regions mapped to this endpoint when using the 'Geographic' traffic routing method. Please consult Traffic Manager Geographic documentation for a full list of accepted values.
        """
        return pulumi.get(self, "geo_mapping")

    @geo_mapping.setter
    def geo_mapping(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "geo_mapping", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="minChildEndpoints")
    def min_child_endpoints(self) -> Optional[pulumi.Input[float]]:
        """
        The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints")

    @min_child_endpoints.setter
    def min_child_endpoints(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_child_endpoints", value)

    @property
    @pulumi.getter(name="minChildEndpointsIPv4")
    def min_child_endpoints_i_pv4(self) -> Optional[pulumi.Input[float]]:
        """
        The minimum number of IPv4 (DNS record type A) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints_i_pv4")

    @min_child_endpoints_i_pv4.setter
    def min_child_endpoints_i_pv4(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_child_endpoints_i_pv4", value)

    @property
    @pulumi.getter(name="minChildEndpointsIPv6")
    def min_child_endpoints_i_pv6(self) -> Optional[pulumi.Input[float]]:
        """
        The minimum number of IPv6 (DNS record type AAAA) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints_i_pv6")

    @min_child_endpoints_i_pv6.setter
    def min_child_endpoints_i_pv6(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_child_endpoints_i_pv6", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[float]]:
        """
        The priority of this endpoint when using the 'Priority' traffic routing method. Possible values are from 1 to 1000, lower values represent higher priority. This is an optional parameter.  If specified, it must be specified on all endpoints, and no two endpoints can share the same priority value.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPropertiesSubnetsArgs']]]]:
        """
        The list of subnets, IP addresses, and/or address ranges mapped to this endpoint when using the 'Subnet' traffic routing method. An empty list will match all ranges not covered by other endpoints.
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPropertiesSubnetsArgs']]]]):
        pulumi.set(self, "subnets", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        The fully-qualified DNS name or IP address of the endpoint. Traffic Manager returns this value in DNS responses to direct traffic to this endpoint.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type 'ExternalEndpoints'.
        """
        return pulumi.get(self, "target_resource_id")

    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_resource_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[float]]:
        """
        The weight of this endpoint when using the 'Weighted' traffic routing method. Possible values are from 1 to 1000.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "weight", value)


class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 always_serve: Optional[pulumi.Input[Union[str, 'AlwaysServe']]] = None,
                 custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointPropertiesCustomHeadersArgs']]]]] = None,
                 endpoint_location: Optional[pulumi.Input[str]] = None,
                 endpoint_monitor_status: Optional[pulumi.Input[Union[str, 'EndpointMonitorStatus']]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 endpoint_status: Optional[pulumi.Input[Union[str, 'EndpointStatus']]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 geo_mapping: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 min_child_endpoints: Optional[pulumi.Input[float]] = None,
                 min_child_endpoints_i_pv4: Optional[pulumi.Input[float]] = None,
                 min_child_endpoints_i_pv6: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[float]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointPropertiesSubnetsArgs']]]]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        Class representing a Traffic Manager endpoint.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'AlwaysServe']] always_serve: If Always Serve is enabled, probing for endpoint health will be disabled and endpoints will be included in the traffic routing method.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointPropertiesCustomHeadersArgs']]]] custom_headers: List of custom headers.
        :param pulumi.Input[str] endpoint_location: Specifies the location of the external or nested endpoints when using the 'Performance' traffic routing method.
        :param pulumi.Input[Union[str, 'EndpointMonitorStatus']] endpoint_monitor_status: The monitoring status of the endpoint.
        :param pulumi.Input[str] endpoint_name: The name of the Traffic Manager endpoint to be created or updated.
        :param pulumi.Input[Union[str, 'EndpointStatus']] endpoint_status: The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method.
        :param pulumi.Input[str] endpoint_type: The type of the Traffic Manager endpoint to be created or updated.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] geo_mapping: The list of countries/regions mapped to this endpoint when using the 'Geographic' traffic routing method. Please consult Traffic Manager Geographic documentation for a full list of accepted values.
        :param pulumi.Input[str] id: Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
        :param pulumi.Input[float] min_child_endpoints: The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        :param pulumi.Input[float] min_child_endpoints_i_pv4: The minimum number of IPv4 (DNS record type A) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        :param pulumi.Input[float] min_child_endpoints_i_pv6: The minimum number of IPv6 (DNS record type AAAA) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        :param pulumi.Input[str] name: The name of the resource
        :param pulumi.Input[float] priority: The priority of this endpoint when using the 'Priority' traffic routing method. Possible values are from 1 to 1000, lower values represent higher priority. This is an optional parameter.  If specified, it must be specified on all endpoints, and no two endpoints can share the same priority value.
        :param pulumi.Input[str] profile_name: The name of the Traffic Manager profile.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointPropertiesSubnetsArgs']]]] subnets: The list of subnets, IP addresses, and/or address ranges mapped to this endpoint when using the 'Subnet' traffic routing method. An empty list will match all ranges not covered by other endpoints.
        :param pulumi.Input[str] target: The fully-qualified DNS name or IP address of the endpoint. Traffic Manager returns this value in DNS responses to direct traffic to this endpoint.
        :param pulumi.Input[str] target_resource_id: The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type 'ExternalEndpoints'.
        :param pulumi.Input[str] type: The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
        :param pulumi.Input[float] weight: The weight of this endpoint when using the 'Weighted' traffic routing method. Possible values are from 1 to 1000.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EndpointInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a Traffic Manager endpoint.

        :param str resource_name: The name of the resource.
        :param EndpointInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 always_serve: Optional[pulumi.Input[Union[str, 'AlwaysServe']]] = None,
                 custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointPropertiesCustomHeadersArgs']]]]] = None,
                 endpoint_location: Optional[pulumi.Input[str]] = None,
                 endpoint_monitor_status: Optional[pulumi.Input[Union[str, 'EndpointMonitorStatus']]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 endpoint_status: Optional[pulumi.Input[Union[str, 'EndpointStatus']]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 geo_mapping: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 min_child_endpoints: Optional[pulumi.Input[float]] = None,
                 min_child_endpoints_i_pv4: Optional[pulumi.Input[float]] = None,
                 min_child_endpoints_i_pv6: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[float]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointPropertiesSubnetsArgs']]]]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 target_resource_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EndpointInitArgs.__new__(EndpointInitArgs)

            __props__.__dict__["always_serve"] = always_serve
            __props__.__dict__["custom_headers"] = custom_headers
            __props__.__dict__["endpoint_location"] = endpoint_location
            __props__.__dict__["endpoint_monitor_status"] = endpoint_monitor_status
            __props__.__dict__["endpoint_name"] = endpoint_name
            __props__.__dict__["endpoint_status"] = endpoint_status
            if endpoint_type is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_type'")
            __props__.__dict__["endpoint_type"] = endpoint_type
            __props__.__dict__["geo_mapping"] = geo_mapping
            __props__.__dict__["id"] = id
            __props__.__dict__["min_child_endpoints"] = min_child_endpoints
            __props__.__dict__["min_child_endpoints_i_pv4"] = min_child_endpoints_i_pv4
            __props__.__dict__["min_child_endpoints_i_pv6"] = min_child_endpoints_i_pv6
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["target"] = target
            __props__.__dict__["target_resource_id"] = target_resource_id
            __props__.__dict__["type"] = type
            __props__.__dict__["weight"] = weight
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:Endpoint"), pulumi.Alias(type_="azure-native:network/v20151101:Endpoint"), pulumi.Alias(type_="azure-native:network/v20170301:Endpoint"), pulumi.Alias(type_="azure-native:network/v20170501:Endpoint"), pulumi.Alias(type_="azure-native:network/v20180201:Endpoint"), pulumi.Alias(type_="azure-native:network/v20180301:Endpoint"), pulumi.Alias(type_="azure-native:network/v20180401:Endpoint"), pulumi.Alias(type_="azure-native:network/v20180801:Endpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Endpoint, __self__).__init__(
            'azure-native:network/v20220401preview:Endpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Endpoint':
        """
        Get an existing Endpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EndpointInitArgs.__new__(EndpointInitArgs)

        __props__.__dict__["always_serve"] = None
        __props__.__dict__["custom_headers"] = None
        __props__.__dict__["endpoint_location"] = None
        __props__.__dict__["endpoint_monitor_status"] = None
        __props__.__dict__["endpoint_status"] = None
        __props__.__dict__["geo_mapping"] = None
        __props__.__dict__["min_child_endpoints"] = None
        __props__.__dict__["min_child_endpoints_i_pv4"] = None
        __props__.__dict__["min_child_endpoints_i_pv6"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["target"] = None
        __props__.__dict__["target_resource_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["weight"] = None
        return Endpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alwaysServe")
    def always_serve(self) -> pulumi.Output[Optional[str]]:
        """
        If Always Serve is enabled, probing for endpoint health will be disabled and endpoints will be included in the traffic routing method.
        """
        return pulumi.get(self, "always_serve")

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> pulumi.Output[Optional[Sequence['outputs.EndpointPropertiesResponseCustomHeaders']]]:
        """
        List of custom headers.
        """
        return pulumi.get(self, "custom_headers")

    @property
    @pulumi.getter(name="endpointLocation")
    def endpoint_location(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the location of the external or nested endpoints when using the 'Performance' traffic routing method.
        """
        return pulumi.get(self, "endpoint_location")

    @property
    @pulumi.getter(name="endpointMonitorStatus")
    def endpoint_monitor_status(self) -> pulumi.Output[Optional[str]]:
        """
        The monitoring status of the endpoint.
        """
        return pulumi.get(self, "endpoint_monitor_status")

    @property
    @pulumi.getter(name="endpointStatus")
    def endpoint_status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method.
        """
        return pulumi.get(self, "endpoint_status")

    @property
    @pulumi.getter(name="geoMapping")
    def geo_mapping(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of countries/regions mapped to this endpoint when using the 'Geographic' traffic routing method. Please consult Traffic Manager Geographic documentation for a full list of accepted values.
        """
        return pulumi.get(self, "geo_mapping")

    @property
    @pulumi.getter(name="minChildEndpoints")
    def min_child_endpoints(self) -> pulumi.Output[Optional[float]]:
        """
        The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints")

    @property
    @pulumi.getter(name="minChildEndpointsIPv4")
    def min_child_endpoints_i_pv4(self) -> pulumi.Output[Optional[float]]:
        """
        The minimum number of IPv4 (DNS record type A) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints_i_pv4")

    @property
    @pulumi.getter(name="minChildEndpointsIPv6")
    def min_child_endpoints_i_pv6(self) -> pulumi.Output[Optional[float]]:
        """
        The minimum number of IPv6 (DNS record type AAAA) endpoints that must be available in the child profile in order for the parent profile to be considered available. Only applicable to endpoint of type 'NestedEndpoints'.
        """
        return pulumi.get(self, "min_child_endpoints_i_pv6")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[float]]:
        """
        The priority of this endpoint when using the 'Priority' traffic routing method. Possible values are from 1 to 1000, lower values represent higher priority. This is an optional parameter.  If specified, it must be specified on all endpoints, and no two endpoints can share the same priority value.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence['outputs.EndpointPropertiesResponseSubnets']]]:
        """
        The list of subnets, IP addresses, and/or address ranges mapped to this endpoint when using the 'Subnet' traffic routing method. An empty list will match all ranges not covered by other endpoints.
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[str]]:
        """
        The fully-qualified DNS name or IP address of the endpoint. Traffic Manager returns this value in DNS responses to direct traffic to this endpoint.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure Resource URI of the of the endpoint. Not applicable to endpoints of type 'ExternalEndpoints'.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[float]]:
        """
        The weight of this endpoint when using the 'Weighted' traffic routing method. Possible values are from 1 to 1000.
        """
        return pulumi.get(self, "weight")

