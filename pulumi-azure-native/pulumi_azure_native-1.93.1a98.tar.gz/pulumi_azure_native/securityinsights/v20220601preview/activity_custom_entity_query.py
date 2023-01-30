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

__all__ = ['ActivityCustomEntityQueryArgs', 'ActivityCustomEntityQuery']

@pulumi.input_type
class ActivityCustomEntityQueryArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 content: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entities_filter: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 entity_query_id: Optional[pulumi.Input[str]] = None,
                 input_entity_type: Optional[pulumi.Input[Union[str, 'EntityType']]] = None,
                 query_definitions: Optional[pulumi.Input['ActivityEntityQueriesPropertiesQueryDefinitionsArgs']] = None,
                 required_input_fields_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ActivityCustomEntityQuery resource.
        :param pulumi.Input[str] kind: The kind of the entity query that supports put request.
               Expected value is 'Activity'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] content: The entity query content to display in timeline
        :param pulumi.Input[str] description: The entity query description
        :param pulumi.Input[bool] enabled: Determines whether this activity is enabled or disabled.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] entities_filter: The query applied only to entities matching to all filters
        :param pulumi.Input[str] entity_query_id: entity query ID
        :param pulumi.Input[Union[str, 'EntityType']] input_entity_type: The type of the query's source entity
        :param pulumi.Input['ActivityEntityQueriesPropertiesQueryDefinitionsArgs'] query_definitions: The Activity query definitions
        :param pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[str]]]]] required_input_fields_sets: List of the fields of the source entity that are required to run the query
        :param pulumi.Input[str] template_name: The template id this activity was created from
        :param pulumi.Input[str] title: The entity query title
        """
        pulumi.set(__self__, "kind", 'Activity')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if entities_filter is not None:
            pulumi.set(__self__, "entities_filter", entities_filter)
        if entity_query_id is not None:
            pulumi.set(__self__, "entity_query_id", entity_query_id)
        if input_entity_type is not None:
            pulumi.set(__self__, "input_entity_type", input_entity_type)
        if query_definitions is not None:
            pulumi.set(__self__, "query_definitions", query_definitions)
        if required_input_fields_sets is not None:
            pulumi.set(__self__, "required_input_fields_sets", required_input_fields_sets)
        if template_name is not None:
            pulumi.set(__self__, "template_name", template_name)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the entity query that supports put request.
        Expected value is 'Activity'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
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
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        The entity query content to display in timeline
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The entity query description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether this activity is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="entitiesFilter")
    def entities_filter(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]:
        """
        The query applied only to entities matching to all filters
        """
        return pulumi.get(self, "entities_filter")

    @entities_filter.setter
    def entities_filter(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]):
        pulumi.set(self, "entities_filter", value)

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

    @property
    @pulumi.getter(name="inputEntityType")
    def input_entity_type(self) -> Optional[pulumi.Input[Union[str, 'EntityType']]]:
        """
        The type of the query's source entity
        """
        return pulumi.get(self, "input_entity_type")

    @input_entity_type.setter
    def input_entity_type(self, value: Optional[pulumi.Input[Union[str, 'EntityType']]]):
        pulumi.set(self, "input_entity_type", value)

    @property
    @pulumi.getter(name="queryDefinitions")
    def query_definitions(self) -> Optional[pulumi.Input['ActivityEntityQueriesPropertiesQueryDefinitionsArgs']]:
        """
        The Activity query definitions
        """
        return pulumi.get(self, "query_definitions")

    @query_definitions.setter
    def query_definitions(self, value: Optional[pulumi.Input['ActivityEntityQueriesPropertiesQueryDefinitionsArgs']]):
        pulumi.set(self, "query_definitions", value)

    @property
    @pulumi.getter(name="requiredInputFieldsSets")
    def required_input_fields_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[str]]]]]]:
        """
        List of the fields of the source entity that are required to run the query
        """
        return pulumi.get(self, "required_input_fields_sets")

    @required_input_fields_sets.setter
    def required_input_fields_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[str]]]]]]):
        pulumi.set(self, "required_input_fields_sets", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[str]]:
        """
        The template id this activity was created from
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The entity query title
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class ActivityCustomEntityQuery(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entities_filter: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 entity_query_id: Optional[pulumi.Input[str]] = None,
                 input_entity_type: Optional[pulumi.Input[Union[str, 'EntityType']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 query_definitions: Optional[pulumi.Input[pulumi.InputType['ActivityEntityQueriesPropertiesQueryDefinitionsArgs']]] = None,
                 required_input_fields_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents Activity entity query.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The entity query content to display in timeline
        :param pulumi.Input[str] description: The entity query description
        :param pulumi.Input[bool] enabled: Determines whether this activity is enabled or disabled.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] entities_filter: The query applied only to entities matching to all filters
        :param pulumi.Input[str] entity_query_id: entity query ID
        :param pulumi.Input[Union[str, 'EntityType']] input_entity_type: The type of the query's source entity
        :param pulumi.Input[str] kind: The kind of the entity query that supports put request.
               Expected value is 'Activity'.
        :param pulumi.Input[pulumi.InputType['ActivityEntityQueriesPropertiesQueryDefinitionsArgs']] query_definitions: The Activity query definitions
        :param pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[str]]]]] required_input_fields_sets: List of the fields of the source entity that are required to run the query
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] template_name: The template id this activity was created from
        :param pulumi.Input[str] title: The entity query title
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ActivityCustomEntityQueryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents Activity entity query.

        :param str resource_name: The name of the resource.
        :param ActivityCustomEntityQueryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ActivityCustomEntityQueryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 entities_filter: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 entity_query_id: Optional[pulumi.Input[str]] = None,
                 input_entity_type: Optional[pulumi.Input[Union[str, 'EntityType']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 query_definitions: Optional[pulumi.Input[pulumi.InputType['ActivityEntityQueriesPropertiesQueryDefinitionsArgs']]] = None,
                 required_input_fields_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ActivityCustomEntityQueryArgs.__new__(ActivityCustomEntityQueryArgs)

            __props__.__dict__["content"] = content
            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["entities_filter"] = entities_filter
            __props__.__dict__["entity_query_id"] = entity_query_id
            __props__.__dict__["input_entity_type"] = input_entity_type
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'Activity'
            __props__.__dict__["query_definitions"] = query_definitions
            __props__.__dict__["required_input_fields_sets"] = required_input_fields_sets
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["template_name"] = template_name
            __props__.__dict__["title"] = title
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["created_time_utc"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["last_modified_time_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:ActivityCustomEntityQuery"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:ActivityCustomEntityQuery")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ActivityCustomEntityQuery, __self__).__init__(
            'azure-native:securityinsights/v20220601preview:ActivityCustomEntityQuery',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ActivityCustomEntityQuery':
        """
        Get an existing ActivityCustomEntityQuery resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ActivityCustomEntityQueryArgs.__new__(ActivityCustomEntityQueryArgs)

        __props__.__dict__["content"] = None
        __props__.__dict__["created_time_utc"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["entities_filter"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["input_entity_type"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["last_modified_time_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["query_definitions"] = None
        __props__.__dict__["required_input_fields_sets"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["template_name"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        return ActivityCustomEntityQuery(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[str]]:
        """
        The entity query content to display in timeline
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[str]:
        """
        The time the activity was created
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The entity query description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines whether this activity is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="entitiesFilter")
    def entities_filter(self) -> pulumi.Output[Optional[Mapping[str, Sequence[str]]]]:
        """
        The query applied only to entities matching to all filters
        """
        return pulumi.get(self, "entities_filter")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="inputEntityType")
    def input_entity_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the query's source entity
        """
        return pulumi.get(self, "input_entity_type")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the entity query
        Expected value is 'Activity'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> pulumi.Output[str]:
        """
        The last time the activity was updated
        """
        return pulumi.get(self, "last_modified_time_utc")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="queryDefinitions")
    def query_definitions(self) -> pulumi.Output[Optional['outputs.ActivityEntityQueriesPropertiesResponseQueryDefinitions']]:
        """
        The Activity query definitions
        """
        return pulumi.get(self, "query_definitions")

    @property
    @pulumi.getter(name="requiredInputFieldsSets")
    def required_input_fields_sets(self) -> pulumi.Output[Optional[Sequence[Sequence[str]]]]:
        """
        List of the fields of the source entity that are required to run the query
        """
        return pulumi.get(self, "required_input_fields_sets")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[Optional[str]]:
        """
        The template id this activity was created from
        """
        return pulumi.get(self, "template_name")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        """
        The entity query title
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

