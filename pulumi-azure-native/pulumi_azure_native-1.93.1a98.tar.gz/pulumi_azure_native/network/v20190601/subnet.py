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

__all__ = ['SubnetInitArgs', 'Subnet']

@pulumi.input_type
class SubnetInitArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_network_name: pulumi.Input[str],
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delegations: Optional[pulumi.Input[Sequence[pulumi.Input['DelegationArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_gateway: Optional[pulumi.Input['SubResourceArgs']] = None,
                 network_security_group: Optional[pulumi.Input['NetworkSecurityGroupArgs']] = None,
                 private_endpoint_network_policies: Optional[pulumi.Input[str]] = None,
                 private_link_service_network_policies: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_navigation_links: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceNavigationLinkArgs']]]] = None,
                 route_table: Optional[pulumi.Input['RouteTableArgs']] = None,
                 service_association_links: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAssociationLinkArgs']]]] = None,
                 service_endpoint_policies: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPolicyArgs']]]] = None,
                 service_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPropertiesFormatArgs']]]] = None,
                 subnet_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Subnet resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] virtual_network_name: The name of the virtual network.
        :param pulumi.Input[str] address_prefix: The address prefix for the subnet.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] address_prefixes: List of address prefixes for the subnet.
        :param pulumi.Input[Sequence[pulumi.Input['DelegationArgs']]] delegations: Gets an array of references to the delegations on the subnet.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input['SubResourceArgs'] nat_gateway: Nat gateway associated with this subnet.
        :param pulumi.Input['NetworkSecurityGroupArgs'] network_security_group: The reference of the NetworkSecurityGroup resource.
        :param pulumi.Input[str] private_endpoint_network_policies: Enable or Disable apply network policies on private end point in the subnet.
        :param pulumi.Input[str] private_link_service_network_policies: Enable or Disable apply network policies on private link service in the subnet.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the resource.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceNavigationLinkArgs']]] resource_navigation_links: Gets an array of references to the external resources using subnet.
        :param pulumi.Input['RouteTableArgs'] route_table: The reference of the RouteTable resource.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceAssociationLinkArgs']]] service_association_links: Gets an array of references to services injecting into this subnet.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPolicyArgs']]] service_endpoint_policies: An array of service endpoint policies.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPropertiesFormatArgs']]] service_endpoints: An array of service endpoints.
        :param pulumi.Input[str] subnet_name: The name of the subnet.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_network_name", virtual_network_name)
        if address_prefix is not None:
            pulumi.set(__self__, "address_prefix", address_prefix)
        if address_prefixes is not None:
            pulumi.set(__self__, "address_prefixes", address_prefixes)
        if delegations is not None:
            pulumi.set(__self__, "delegations", delegations)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nat_gateway is not None:
            pulumi.set(__self__, "nat_gateway", nat_gateway)
        if network_security_group is not None:
            pulumi.set(__self__, "network_security_group", network_security_group)
        if private_endpoint_network_policies is not None:
            pulumi.set(__self__, "private_endpoint_network_policies", private_endpoint_network_policies)
        if private_link_service_network_policies is not None:
            pulumi.set(__self__, "private_link_service_network_policies", private_link_service_network_policies)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_navigation_links is not None:
            pulumi.set(__self__, "resource_navigation_links", resource_navigation_links)
        if route_table is not None:
            pulumi.set(__self__, "route_table", route_table)
        if service_association_links is not None:
            pulumi.set(__self__, "service_association_links", service_association_links)
        if service_endpoint_policies is not None:
            pulumi.set(__self__, "service_endpoint_policies", service_endpoint_policies)
        if service_endpoints is not None:
            pulumi.set(__self__, "service_endpoints", service_endpoints)
        if subnet_name is not None:
            pulumi.set(__self__, "subnet_name", subnet_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualNetworkName")
    def virtual_network_name(self) -> pulumi.Input[str]:
        """
        The name of the virtual network.
        """
        return pulumi.get(self, "virtual_network_name")

    @virtual_network_name.setter
    def virtual_network_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_network_name", value)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The address prefix for the subnet.
        """
        return pulumi.get(self, "address_prefix")

    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_prefix", value)

    @property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of address prefixes for the subnet.
        """
        return pulumi.get(self, "address_prefixes")

    @address_prefixes.setter
    def address_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "address_prefixes", value)

    @property
    @pulumi.getter
    def delegations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DelegationArgs']]]]:
        """
        Gets an array of references to the delegations on the subnet.
        """
        return pulumi.get(self, "delegations")

    @delegations.setter
    def delegations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DelegationArgs']]]]):
        pulumi.set(self, "delegations", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        Nat gateway associated with this subnet.
        """
        return pulumi.get(self, "nat_gateway")

    @nat_gateway.setter
    def nat_gateway(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "nat_gateway", value)

    @property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[pulumi.Input['NetworkSecurityGroupArgs']]:
        """
        The reference of the NetworkSecurityGroup resource.
        """
        return pulumi.get(self, "network_security_group")

    @network_security_group.setter
    def network_security_group(self, value: Optional[pulumi.Input['NetworkSecurityGroupArgs']]):
        pulumi.set(self, "network_security_group", value)

    @property
    @pulumi.getter(name="privateEndpointNetworkPolicies")
    def private_endpoint_network_policies(self) -> Optional[pulumi.Input[str]]:
        """
        Enable or Disable apply network policies on private end point in the subnet.
        """
        return pulumi.get(self, "private_endpoint_network_policies")

    @private_endpoint_network_policies.setter
    def private_endpoint_network_policies(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_network_policies", value)

    @property
    @pulumi.getter(name="privateLinkServiceNetworkPolicies")
    def private_link_service_network_policies(self) -> Optional[pulumi.Input[str]]:
        """
        Enable or Disable apply network policies on private link service in the subnet.
        """
        return pulumi.get(self, "private_link_service_network_policies")

    @private_link_service_network_policies.setter
    def private_link_service_network_policies(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_service_network_policies", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="resourceNavigationLinks")
    def resource_navigation_links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceNavigationLinkArgs']]]]:
        """
        Gets an array of references to the external resources using subnet.
        """
        return pulumi.get(self, "resource_navigation_links")

    @resource_navigation_links.setter
    def resource_navigation_links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceNavigationLinkArgs']]]]):
        pulumi.set(self, "resource_navigation_links", value)

    @property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> Optional[pulumi.Input['RouteTableArgs']]:
        """
        The reference of the RouteTable resource.
        """
        return pulumi.get(self, "route_table")

    @route_table.setter
    def route_table(self, value: Optional[pulumi.Input['RouteTableArgs']]):
        pulumi.set(self, "route_table", value)

    @property
    @pulumi.getter(name="serviceAssociationLinks")
    def service_association_links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAssociationLinkArgs']]]]:
        """
        Gets an array of references to services injecting into this subnet.
        """
        return pulumi.get(self, "service_association_links")

    @service_association_links.setter
    def service_association_links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAssociationLinkArgs']]]]):
        pulumi.set(self, "service_association_links", value)

    @property
    @pulumi.getter(name="serviceEndpointPolicies")
    def service_endpoint_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPolicyArgs']]]]:
        """
        An array of service endpoint policies.
        """
        return pulumi.get(self, "service_endpoint_policies")

    @service_endpoint_policies.setter
    def service_endpoint_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPolicyArgs']]]]):
        pulumi.set(self, "service_endpoint_policies", value)

    @property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPropertiesFormatArgs']]]]:
        """
        An array of service endpoints.
        """
        return pulumi.get(self, "service_endpoints")

    @service_endpoints.setter
    def service_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceEndpointPropertiesFormatArgs']]]]):
        pulumi.set(self, "service_endpoints", value)

    @property
    @pulumi.getter(name="subnetName")
    def subnet_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the subnet.
        """
        return pulumi.get(self, "subnet_name")

    @subnet_name.setter
    def subnet_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_name", value)


class Subnet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delegations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DelegationArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_gateway: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 network_security_group: Optional[pulumi.Input[pulumi.InputType['NetworkSecurityGroupArgs']]] = None,
                 private_endpoint_network_policies: Optional[pulumi.Input[str]] = None,
                 private_link_service_network_policies: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_navigation_links: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceNavigationLinkArgs']]]]] = None,
                 route_table: Optional[pulumi.Input[pulumi.InputType['RouteTableArgs']]] = None,
                 service_association_links: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceAssociationLinkArgs']]]]] = None,
                 service_endpoint_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPolicyArgs']]]]] = None,
                 service_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPropertiesFormatArgs']]]]] = None,
                 subnet_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Subnet in a virtual network resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_prefix: The address prefix for the subnet.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] address_prefixes: List of address prefixes for the subnet.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DelegationArgs']]]] delegations: Gets an array of references to the delegations on the subnet.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] nat_gateway: Nat gateway associated with this subnet.
        :param pulumi.Input[pulumi.InputType['NetworkSecurityGroupArgs']] network_security_group: The reference of the NetworkSecurityGroup resource.
        :param pulumi.Input[str] private_endpoint_network_policies: Enable or Disable apply network policies on private end point in the subnet.
        :param pulumi.Input[str] private_link_service_network_policies: Enable or Disable apply network policies on private link service in the subnet.
        :param pulumi.Input[str] provisioning_state: The provisioning state of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceNavigationLinkArgs']]]] resource_navigation_links: Gets an array of references to the external resources using subnet.
        :param pulumi.Input[pulumi.InputType['RouteTableArgs']] route_table: The reference of the RouteTable resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceAssociationLinkArgs']]]] service_association_links: Gets an array of references to services injecting into this subnet.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPolicyArgs']]]] service_endpoint_policies: An array of service endpoint policies.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPropertiesFormatArgs']]]] service_endpoints: An array of service endpoints.
        :param pulumi.Input[str] subnet_name: The name of the subnet.
        :param pulumi.Input[str] virtual_network_name: The name of the virtual network.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubnetInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Subnet in a virtual network resource.

        :param str resource_name: The name of the resource.
        :param SubnetInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubnetInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delegations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DelegationArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nat_gateway: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 network_security_group: Optional[pulumi.Input[pulumi.InputType['NetworkSecurityGroupArgs']]] = None,
                 private_endpoint_network_policies: Optional[pulumi.Input[str]] = None,
                 private_link_service_network_policies: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_navigation_links: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceNavigationLinkArgs']]]]] = None,
                 route_table: Optional[pulumi.Input[pulumi.InputType['RouteTableArgs']]] = None,
                 service_association_links: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceAssociationLinkArgs']]]]] = None,
                 service_endpoint_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPolicyArgs']]]]] = None,
                 service_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceEndpointPropertiesFormatArgs']]]]] = None,
                 subnet_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubnetInitArgs.__new__(SubnetInitArgs)

            __props__.__dict__["address_prefix"] = address_prefix
            __props__.__dict__["address_prefixes"] = address_prefixes
            __props__.__dict__["delegations"] = delegations
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["nat_gateway"] = nat_gateway
            __props__.__dict__["network_security_group"] = network_security_group
            __props__.__dict__["private_endpoint_network_policies"] = private_endpoint_network_policies
            __props__.__dict__["private_link_service_network_policies"] = private_link_service_network_policies
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_navigation_links"] = resource_navigation_links
            __props__.__dict__["route_table"] = route_table
            __props__.__dict__["service_association_links"] = service_association_links
            __props__.__dict__["service_endpoint_policies"] = service_endpoint_policies
            __props__.__dict__["service_endpoints"] = service_endpoints
            __props__.__dict__["subnet_name"] = subnet_name
            if virtual_network_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_network_name'")
            __props__.__dict__["virtual_network_name"] = virtual_network_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["ip_configuration_profiles"] = None
            __props__.__dict__["ip_configurations"] = None
            __props__.__dict__["private_endpoints"] = None
            __props__.__dict__["purpose"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:Subnet"), pulumi.Alias(type_="azure-native:network/v20150501preview:Subnet"), pulumi.Alias(type_="azure-native:network/v20150615:Subnet"), pulumi.Alias(type_="azure-native:network/v20160330:Subnet"), pulumi.Alias(type_="azure-native:network/v20160601:Subnet"), pulumi.Alias(type_="azure-native:network/v20160901:Subnet"), pulumi.Alias(type_="azure-native:network/v20161201:Subnet"), pulumi.Alias(type_="azure-native:network/v20170301:Subnet"), pulumi.Alias(type_="azure-native:network/v20170601:Subnet"), pulumi.Alias(type_="azure-native:network/v20170801:Subnet"), pulumi.Alias(type_="azure-native:network/v20170901:Subnet"), pulumi.Alias(type_="azure-native:network/v20171001:Subnet"), pulumi.Alias(type_="azure-native:network/v20171101:Subnet"), pulumi.Alias(type_="azure-native:network/v20180101:Subnet"), pulumi.Alias(type_="azure-native:network/v20180201:Subnet"), pulumi.Alias(type_="azure-native:network/v20180401:Subnet"), pulumi.Alias(type_="azure-native:network/v20180601:Subnet"), pulumi.Alias(type_="azure-native:network/v20180701:Subnet"), pulumi.Alias(type_="azure-native:network/v20180801:Subnet"), pulumi.Alias(type_="azure-native:network/v20181001:Subnet"), pulumi.Alias(type_="azure-native:network/v20181101:Subnet"), pulumi.Alias(type_="azure-native:network/v20181201:Subnet"), pulumi.Alias(type_="azure-native:network/v20190201:Subnet"), pulumi.Alias(type_="azure-native:network/v20190401:Subnet"), pulumi.Alias(type_="azure-native:network/v20190701:Subnet"), pulumi.Alias(type_="azure-native:network/v20190801:Subnet"), pulumi.Alias(type_="azure-native:network/v20190901:Subnet"), pulumi.Alias(type_="azure-native:network/v20191101:Subnet"), pulumi.Alias(type_="azure-native:network/v20191201:Subnet"), pulumi.Alias(type_="azure-native:network/v20200301:Subnet"), pulumi.Alias(type_="azure-native:network/v20200401:Subnet"), pulumi.Alias(type_="azure-native:network/v20200501:Subnet"), pulumi.Alias(type_="azure-native:network/v20200601:Subnet"), pulumi.Alias(type_="azure-native:network/v20200701:Subnet"), pulumi.Alias(type_="azure-native:network/v20200801:Subnet"), pulumi.Alias(type_="azure-native:network/v20201101:Subnet"), pulumi.Alias(type_="azure-native:network/v20210201:Subnet"), pulumi.Alias(type_="azure-native:network/v20210301:Subnet"), pulumi.Alias(type_="azure-native:network/v20210501:Subnet"), pulumi.Alias(type_="azure-native:network/v20210801:Subnet"), pulumi.Alias(type_="azure-native:network/v20220101:Subnet"), pulumi.Alias(type_="azure-native:network/v20220501:Subnet"), pulumi.Alias(type_="azure-native:network/v20220701:Subnet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Subnet, __self__).__init__(
            'azure-native:network/v20190601:Subnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Subnet':
        """
        Get an existing Subnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubnetInitArgs.__new__(SubnetInitArgs)

        __props__.__dict__["address_prefix"] = None
        __props__.__dict__["address_prefixes"] = None
        __props__.__dict__["delegations"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["ip_configuration_profiles"] = None
        __props__.__dict__["ip_configurations"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["nat_gateway"] = None
        __props__.__dict__["network_security_group"] = None
        __props__.__dict__["private_endpoint_network_policies"] = None
        __props__.__dict__["private_endpoints"] = None
        __props__.__dict__["private_link_service_network_policies"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["purpose"] = None
        __props__.__dict__["resource_navigation_links"] = None
        __props__.__dict__["route_table"] = None
        __props__.__dict__["service_association_links"] = None
        __props__.__dict__["service_endpoint_policies"] = None
        __props__.__dict__["service_endpoints"] = None
        return Subnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The address prefix for the subnet.
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of address prefixes for the subnet.
        """
        return pulumi.get(self, "address_prefixes")

    @property
    @pulumi.getter
    def delegations(self) -> pulumi.Output[Optional[Sequence['outputs.DelegationResponse']]]:
        """
        Gets an array of references to the delegations on the subnet.
        """
        return pulumi.get(self, "delegations")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="ipConfigurationProfiles")
    def ip_configuration_profiles(self) -> pulumi.Output[Sequence['outputs.IPConfigurationProfileResponse']]:
        """
        Array of IP configuration profiles which reference this subnet.
        """
        return pulumi.get(self, "ip_configuration_profiles")

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Output[Sequence['outputs.IPConfigurationResponse']]:
        """
        Gets an array of references to the network interface IP configurations using subnet.
        """
        return pulumi.get(self, "ip_configurations")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natGateway")
    def nat_gateway(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        Nat gateway associated with this subnet.
        """
        return pulumi.get(self, "nat_gateway")

    @property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> pulumi.Output[Optional['outputs.NetworkSecurityGroupResponse']]:
        """
        The reference of the NetworkSecurityGroup resource.
        """
        return pulumi.get(self, "network_security_group")

    @property
    @pulumi.getter(name="privateEndpointNetworkPolicies")
    def private_endpoint_network_policies(self) -> pulumi.Output[Optional[str]]:
        """
        Enable or Disable apply network policies on private end point in the subnet.
        """
        return pulumi.get(self, "private_endpoint_network_policies")

    @property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointResponse']]:
        """
        An array of references to private endpoints.
        """
        return pulumi.get(self, "private_endpoints")

    @property
    @pulumi.getter(name="privateLinkServiceNetworkPolicies")
    def private_link_service_network_policies(self) -> pulumi.Output[Optional[str]]:
        """
        Enable or Disable apply network policies on private link service in the subnet.
        """
        return pulumi.get(self, "private_link_service_network_policies")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[str]:
        """
        A read-only string identifying the intention of use for this subnet based on delegations and other user-defined properties.
        """
        return pulumi.get(self, "purpose")

    @property
    @pulumi.getter(name="resourceNavigationLinks")
    def resource_navigation_links(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceNavigationLinkResponse']]]:
        """
        Gets an array of references to the external resources using subnet.
        """
        return pulumi.get(self, "resource_navigation_links")

    @property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> pulumi.Output[Optional['outputs.RouteTableResponse']]:
        """
        The reference of the RouteTable resource.
        """
        return pulumi.get(self, "route_table")

    @property
    @pulumi.getter(name="serviceAssociationLinks")
    def service_association_links(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceAssociationLinkResponse']]]:
        """
        Gets an array of references to services injecting into this subnet.
        """
        return pulumi.get(self, "service_association_links")

    @property
    @pulumi.getter(name="serviceEndpointPolicies")
    def service_endpoint_policies(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceEndpointPolicyResponse']]]:
        """
        An array of service endpoint policies.
        """
        return pulumi.get(self, "service_endpoint_policies")

    @property
    @pulumi.getter(name="serviceEndpoints")
    def service_endpoints(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceEndpointPropertiesFormatResponse']]]:
        """
        An array of service endpoints.
        """
        return pulumi.get(self, "service_endpoints")

