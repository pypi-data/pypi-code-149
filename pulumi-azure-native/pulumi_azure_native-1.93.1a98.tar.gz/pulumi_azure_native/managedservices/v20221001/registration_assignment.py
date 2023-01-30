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
from ._inputs import *

__all__ = ['RegistrationAssignmentArgs', 'RegistrationAssignment']

@pulumi.input_type
class RegistrationAssignmentArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 properties: Optional[pulumi.Input['RegistrationAssignmentPropertiesArgs']] = None,
                 registration_assignment_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RegistrationAssignment resource.
        :param pulumi.Input[str] scope: The scope of the resource.
        :param pulumi.Input['RegistrationAssignmentPropertiesArgs'] properties: The properties of a registration assignment.
        :param pulumi.Input[str] registration_assignment_id: The GUID of the registration assignment.
        """
        pulumi.set(__self__, "scope", scope)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if registration_assignment_id is not None:
            pulumi.set(__self__, "registration_assignment_id", registration_assignment_id)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope of the resource.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['RegistrationAssignmentPropertiesArgs']]:
        """
        The properties of a registration assignment.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['RegistrationAssignmentPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="registrationAssignmentId")
    def registration_assignment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The GUID of the registration assignment.
        """
        return pulumi.get(self, "registration_assignment_id")

    @registration_assignment_id.setter
    def registration_assignment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registration_assignment_id", value)


class RegistrationAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['RegistrationAssignmentPropertiesArgs']]] = None,
                 registration_assignment_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The registration assignment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RegistrationAssignmentPropertiesArgs']] properties: The properties of a registration assignment.
        :param pulumi.Input[str] registration_assignment_id: The GUID of the registration assignment.
        :param pulumi.Input[str] scope: The scope of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegistrationAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The registration assignment.

        :param str resource_name: The name of the resource.
        :param RegistrationAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegistrationAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['RegistrationAssignmentPropertiesArgs']]] = None,
                 registration_assignment_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegistrationAssignmentArgs.__new__(RegistrationAssignmentArgs)

            __props__.__dict__["properties"] = properties
            __props__.__dict__["registration_assignment_id"] = registration_assignment_id
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managedservices:RegistrationAssignment"), pulumi.Alias(type_="azure-native:managedservices/v20180601preview:RegistrationAssignment"), pulumi.Alias(type_="azure-native:managedservices/v20190401preview:RegistrationAssignment"), pulumi.Alias(type_="azure-native:managedservices/v20190601:RegistrationAssignment"), pulumi.Alias(type_="azure-native:managedservices/v20190901:RegistrationAssignment"), pulumi.Alias(type_="azure-native:managedservices/v20200201preview:RegistrationAssignment"), pulumi.Alias(type_="azure-native:managedservices/v20220101preview:RegistrationAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RegistrationAssignment, __self__).__init__(
            'azure-native:managedservices/v20221001:RegistrationAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegistrationAssignment':
        """
        Get an existing RegistrationAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegistrationAssignmentArgs.__new__(RegistrationAssignmentArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return RegistrationAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the registration assignment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.RegistrationAssignmentPropertiesResponse']:
        """
        The properties of a registration assignment.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The metadata for the registration assignment resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the Azure resource (Microsoft.ManagedServices/registrationAssignments).
        """
        return pulumi.get(self, "type")

