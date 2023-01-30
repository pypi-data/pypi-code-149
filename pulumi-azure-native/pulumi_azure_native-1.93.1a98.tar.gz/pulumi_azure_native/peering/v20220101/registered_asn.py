# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['RegisteredAsnArgs', 'RegisteredAsn']

@pulumi.input_type
class RegisteredAsnArgs:
    def __init__(__self__, *,
                 peering_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 asn: Optional[pulumi.Input[int]] = None,
                 registered_asn_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RegisteredAsn resource.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[int] asn: The customer's ASN from which traffic originates.
        :param pulumi.Input[str] registered_asn_name: The name of the ASN.
        """
        pulumi.set(__self__, "peering_name", peering_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if asn is not None:
            pulumi.set(__self__, "asn", asn)
        if registered_asn_name is not None:
            pulumi.set(__self__, "registered_asn_name", registered_asn_name)

    @property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> pulumi.Input[str]:
        """
        The name of the peering.
        """
        return pulumi.get(self, "peering_name")

    @peering_name.setter
    def peering_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "peering_name", value)

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
    @pulumi.getter
    def asn(self) -> Optional[pulumi.Input[int]]:
        """
        The customer's ASN from which traffic originates.
        """
        return pulumi.get(self, "asn")

    @asn.setter
    def asn(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "asn", value)

    @property
    @pulumi.getter(name="registeredAsnName")
    def registered_asn_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ASN.
        """
        return pulumi.get(self, "registered_asn_name")

    @registered_asn_name.setter
    def registered_asn_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registered_asn_name", value)


class RegisteredAsn(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asn: Optional[pulumi.Input[int]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 registered_asn_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The customer's ASN that is registered by the peering service provider.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] asn: The customer's ASN from which traffic originates.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[str] registered_asn_name: The name of the ASN.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegisteredAsnArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The customer's ASN that is registered by the peering service provider.

        :param str resource_name: The name of the resource.
        :param RegisteredAsnArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegisteredAsnArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asn: Optional[pulumi.Input[int]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 registered_asn_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegisteredAsnArgs.__new__(RegisteredAsnArgs)

            __props__.__dict__["asn"] = asn
            if peering_name is None and not opts.urn:
                raise TypeError("Missing required property 'peering_name'")
            __props__.__dict__["peering_name"] = peering_name
            __props__.__dict__["registered_asn_name"] = registered_asn_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["peering_service_prefix_key"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:peering:RegisteredAsn"), pulumi.Alias(type_="azure-native:peering/v20200101preview:RegisteredAsn"), pulumi.Alias(type_="azure-native:peering/v20200401:RegisteredAsn"), pulumi.Alias(type_="azure-native:peering/v20201001:RegisteredAsn"), pulumi.Alias(type_="azure-native:peering/v20210101:RegisteredAsn"), pulumi.Alias(type_="azure-native:peering/v20210601:RegisteredAsn"), pulumi.Alias(type_="azure-native:peering/v20220601:RegisteredAsn"), pulumi.Alias(type_="azure-native:peering/v20221001:RegisteredAsn")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RegisteredAsn, __self__).__init__(
            'azure-native:peering/v20220101:RegisteredAsn',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegisteredAsn':
        """
        Get an existing RegisteredAsn resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegisteredAsnArgs.__new__(RegisteredAsnArgs)

        __props__.__dict__["asn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peering_service_prefix_key"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return RegisteredAsn(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def asn(self) -> pulumi.Output[Optional[int]]:
        """
        The customer's ASN from which traffic originates.
        """
        return pulumi.get(self, "asn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringServicePrefixKey")
    def peering_service_prefix_key(self) -> pulumi.Output[str]:
        """
        The peering service prefix key that is to be shared with the customer.
        """
        return pulumi.get(self, "peering_service_prefix_key")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

