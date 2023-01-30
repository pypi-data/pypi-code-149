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

__all__ = ['JitNetworkAccessPolicyArgs', 'JitNetworkAccessPolicy']

@pulumi.input_type
class JitNetworkAccessPolicyArgs:
    def __init__(__self__, *,
                 asc_location: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 virtual_machines: pulumi.Input[Sequence[pulumi.Input['JitNetworkAccessPolicyVirtualMachineArgs']]],
                 jit_network_access_policy_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input['JitNetworkAccessRequestArgs']]]] = None):
        """
        The set of arguments for constructing a JitNetworkAccessPolicy resource.
        :param pulumi.Input[str] asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['JitNetworkAccessPolicyVirtualMachineArgs']]] virtual_machines: Configurations for Microsoft.Compute/virtualMachines resource type.
        :param pulumi.Input[str] jit_network_access_policy_name: Name of a Just-in-Time access configuration policy.
        :param pulumi.Input[str] kind: Kind of the resource
        """
        pulumi.set(__self__, "asc_location", asc_location)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_machines", virtual_machines)
        if jit_network_access_policy_name is not None:
            pulumi.set(__self__, "jit_network_access_policy_name", jit_network_access_policy_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if requests is not None:
            pulumi.set(__self__, "requests", requests)

    @property
    @pulumi.getter(name="ascLocation")
    def asc_location(self) -> pulumi.Input[str]:
        """
        The location where ASC stores the data of the subscription. can be retrieved from Get locations
        """
        return pulumi.get(self, "asc_location")

    @asc_location.setter
    def asc_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "asc_location", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(self) -> pulumi.Input[Sequence[pulumi.Input['JitNetworkAccessPolicyVirtualMachineArgs']]]:
        """
        Configurations for Microsoft.Compute/virtualMachines resource type.
        """
        return pulumi.get(self, "virtual_machines")

    @virtual_machines.setter
    def virtual_machines(self, value: pulumi.Input[Sequence[pulumi.Input['JitNetworkAccessPolicyVirtualMachineArgs']]]):
        pulumi.set(self, "virtual_machines", value)

    @property
    @pulumi.getter(name="jitNetworkAccessPolicyName")
    def jit_network_access_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of a Just-in-Time access configuration policy.
        """
        return pulumi.get(self, "jit_network_access_policy_name")

    @jit_network_access_policy_name.setter
    def jit_network_access_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "jit_network_access_policy_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JitNetworkAccessRequestArgs']]]]:
        return pulumi.get(self, "requests")

    @requests.setter
    def requests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JitNetworkAccessRequestArgs']]]]):
        pulumi.set(self, "requests", value)


warnings.warn("""Version 2015-06-01-preview will be removed in v2 of the provider.""", DeprecationWarning)


class JitNetworkAccessPolicy(pulumi.CustomResource):
    warnings.warn("""Version 2015-06-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asc_location: Optional[pulumi.Input[str]] = None,
                 jit_network_access_policy_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JitNetworkAccessRequestArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_machines: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JitNetworkAccessPolicyVirtualMachineArgs']]]]] = None,
                 __props__=None):
        """
        Create a JitNetworkAccessPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
        :param pulumi.Input[str] jit_network_access_policy_name: Name of a Just-in-Time access configuration policy.
        :param pulumi.Input[str] kind: Kind of the resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JitNetworkAccessPolicyVirtualMachineArgs']]]] virtual_machines: Configurations for Microsoft.Compute/virtualMachines resource type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JitNetworkAccessPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a JitNetworkAccessPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param JitNetworkAccessPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JitNetworkAccessPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asc_location: Optional[pulumi.Input[str]] = None,
                 jit_network_access_policy_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 requests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JitNetworkAccessRequestArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_machines: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JitNetworkAccessPolicyVirtualMachineArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""JitNetworkAccessPolicy is deprecated: Version 2015-06-01-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JitNetworkAccessPolicyArgs.__new__(JitNetworkAccessPolicyArgs)

            if asc_location is None and not opts.urn:
                raise TypeError("Missing required property 'asc_location'")
            __props__.__dict__["asc_location"] = asc_location
            __props__.__dict__["jit_network_access_policy_name"] = jit_network_access_policy_name
            __props__.__dict__["kind"] = kind
            __props__.__dict__["requests"] = requests
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if virtual_machines is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machines'")
            __props__.__dict__["virtual_machines"] = virtual_machines
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:JitNetworkAccessPolicy"), pulumi.Alias(type_="azure-native:security/v20200101:JitNetworkAccessPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(JitNetworkAccessPolicy, __self__).__init__(
            'azure-native:security/v20150601preview:JitNetworkAccessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JitNetworkAccessPolicy':
        """
        Get an existing JitNetworkAccessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JitNetworkAccessPolicyArgs.__new__(JitNetworkAccessPolicyArgs)

        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["requests"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machines"] = None
        return JitNetworkAccessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location where the resource is stored
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state of the Just-in-Time policy.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def requests(self) -> pulumi.Output[Optional[Sequence['outputs.JitNetworkAccessRequestResponse']]]:
        return pulumi.get(self, "requests")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(self) -> pulumi.Output[Sequence['outputs.JitNetworkAccessPolicyVirtualMachineResponse']]:
        """
        Configurations for Microsoft.Compute/virtualMachines resource type.
        """
        return pulumi.get(self, "virtual_machines")

