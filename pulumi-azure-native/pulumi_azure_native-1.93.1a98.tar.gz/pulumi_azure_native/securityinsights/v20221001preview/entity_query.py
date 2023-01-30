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

__all__ = ['EntityQueryArgs', 'EntityQuery']

@pulumi.input_type
class EntityQueryArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[Union[str, 'CustomEntityQueryKind']],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 entity_query_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EntityQuery resource.
        :param pulumi.Input[Union[str, 'CustomEntityQueryKind']] kind: the entity query kind
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] entity_query_id: entity query ID
        """
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if entity_query_id is not None:
            pulumi.set(__self__, "entity_query_id", entity_query_id)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[str, 'CustomEntityQueryKind']]:
        """
        the entity query kind
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[Union[str, 'CustomEntityQueryKind']]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="entityQueryId")
    def entity_query_id(self) -> Optional[pulumi.Input[str]]:
        """
        entity query ID
        """
        return pulumi.get(self, "entity_query_id")

    @entity_query_id.setter
    def entity_query_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_query_id", value)


warnings.warn("""Please use one of the variants: ActivityCustomEntityQuery.""", DeprecationWarning)


class EntityQuery(pulumi.CustomResource):
    warnings.warn("""Please use one of the variants: ActivityCustomEntityQuery.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 entity_query_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'CustomEntityQueryKind']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Specific entity query.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] entity_query_id: entity query ID
        :param pulumi.Input[Union[str, 'CustomEntityQueryKind']] kind: the entity query kind
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EntityQueryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specific entity query.

        :param str resource_name: The name of the resource.
        :param EntityQueryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EntityQueryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 entity_query_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'CustomEntityQueryKind']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""EntityQuery is deprecated: Please use one of the variants: ActivityCustomEntityQuery.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EntityQueryArgs.__new__(EntityQueryArgs)

            __props__.__dict__["entity_query_id"] = entity_query_id
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:EntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:EntityQuery")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EntityQuery, __self__).__init__(
            'azure-native:securityinsights/v20221001preview:EntityQuery',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EntityQuery':
        """
        Get an existing EntityQuery resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EntityQueryArgs.__new__(EntityQueryArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return EntityQuery(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        the entity query kind
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

