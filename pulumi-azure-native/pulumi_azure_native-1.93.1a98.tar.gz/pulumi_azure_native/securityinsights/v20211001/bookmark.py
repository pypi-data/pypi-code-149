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

__all__ = ['BookmarkArgs', 'Bookmark']

@pulumi.input_type
class BookmarkArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 query: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 bookmark_id: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input['UserInfoArgs']] = None,
                 event_time: Optional[pulumi.Input[str]] = None,
                 incident_info: Optional[pulumi.Input['IncidentInfoArgs']] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 query_end_time: Optional[pulumi.Input[str]] = None,
                 query_result: Optional[pulumi.Input[str]] = None,
                 query_start_time: Optional[pulumi.Input[str]] = None,
                 updated: Optional[pulumi.Input[str]] = None,
                 updated_by: Optional[pulumi.Input['UserInfoArgs']] = None):
        """
        The set of arguments for constructing a Bookmark resource.
        :param pulumi.Input[str] display_name: The display name of the bookmark
        :param pulumi.Input[str] query: The query of the bookmark.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] bookmark_id: Bookmark ID
        :param pulumi.Input[str] created: The time the bookmark was created
        :param pulumi.Input['UserInfoArgs'] created_by: Describes a user that created the bookmark
        :param pulumi.Input[str] event_time: The bookmark event time
        :param pulumi.Input['IncidentInfoArgs'] incident_info: Describes an incident that relates to bookmark
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels relevant to this bookmark
        :param pulumi.Input[str] notes: The notes of the bookmark
        :param pulumi.Input[str] query_end_time: The end time for the query
        :param pulumi.Input[str] query_result: The query result of the bookmark.
        :param pulumi.Input[str] query_start_time: The start time for the query
        :param pulumi.Input[str] updated: The last time the bookmark was updated
        :param pulumi.Input['UserInfoArgs'] updated_by: Describes a user that updated the bookmark
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "query", query)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if bookmark_id is not None:
            pulumi.set(__self__, "bookmark_id", bookmark_id)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if event_time is not None:
            pulumi.set(__self__, "event_time", event_time)
        if incident_info is not None:
            pulumi.set(__self__, "incident_info", incident_info)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if query_end_time is not None:
            pulumi.set(__self__, "query_end_time", query_end_time)
        if query_result is not None:
            pulumi.set(__self__, "query_result", query_result)
        if query_start_time is not None:
            pulumi.set(__self__, "query_start_time", query_start_time)
        if updated is not None:
            pulumi.set(__self__, "updated", updated)
        if updated_by is not None:
            pulumi.set(__self__, "updated_by", updated_by)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the bookmark
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def query(self) -> pulumi.Input[str]:
        """
        The query of the bookmark.
        """
        return pulumi.get(self, "query")

    @query.setter
    def query(self, value: pulumi.Input[str]):
        pulumi.set(self, "query", value)

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
    @pulumi.getter(name="bookmarkId")
    def bookmark_id(self) -> Optional[pulumi.Input[str]]:
        """
        Bookmark ID
        """
        return pulumi.get(self, "bookmark_id")

    @bookmark_id.setter
    def bookmark_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bookmark_id", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the bookmark was created
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input['UserInfoArgs']]:
        """
        Describes a user that created the bookmark
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input['UserInfoArgs']]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> Optional[pulumi.Input[str]]:
        """
        The bookmark event time
        """
        return pulumi.get(self, "event_time")

    @event_time.setter
    def event_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_time", value)

    @property
    @pulumi.getter(name="incidentInfo")
    def incident_info(self) -> Optional[pulumi.Input['IncidentInfoArgs']]:
        """
        Describes an incident that relates to bookmark
        """
        return pulumi.get(self, "incident_info")

    @incident_info.setter
    def incident_info(self, value: Optional[pulumi.Input['IncidentInfoArgs']]):
        pulumi.set(self, "incident_info", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of labels relevant to this bookmark
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        The notes of the bookmark
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="queryEndTime")
    def query_end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The end time for the query
        """
        return pulumi.get(self, "query_end_time")

    @query_end_time.setter
    def query_end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_end_time", value)

    @property
    @pulumi.getter(name="queryResult")
    def query_result(self) -> Optional[pulumi.Input[str]]:
        """
        The query result of the bookmark.
        """
        return pulumi.get(self, "query_result")

    @query_result.setter
    def query_result(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_result", value)

    @property
    @pulumi.getter(name="queryStartTime")
    def query_start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The start time for the query
        """
        return pulumi.get(self, "query_start_time")

    @query_start_time.setter
    def query_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_start_time", value)

    @property
    @pulumi.getter
    def updated(self) -> Optional[pulumi.Input[str]]:
        """
        The last time the bookmark was updated
        """
        return pulumi.get(self, "updated")

    @updated.setter
    def updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated", value)

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[pulumi.Input['UserInfoArgs']]:
        """
        Describes a user that updated the bookmark
        """
        return pulumi.get(self, "updated_by")

    @updated_by.setter
    def updated_by(self, value: Optional[pulumi.Input['UserInfoArgs']]):
        pulumi.set(self, "updated_by", value)


class Bookmark(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bookmark_id: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[pulumi.InputType['UserInfoArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 event_time: Optional[pulumi.Input[str]] = None,
                 incident_info: Optional[pulumi.Input[pulumi.InputType['IncidentInfoArgs']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 query_end_time: Optional[pulumi.Input[str]] = None,
                 query_result: Optional[pulumi.Input[str]] = None,
                 query_start_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 updated: Optional[pulumi.Input[str]] = None,
                 updated_by: Optional[pulumi.Input[pulumi.InputType['UserInfoArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a bookmark in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bookmark_id: Bookmark ID
        :param pulumi.Input[str] created: The time the bookmark was created
        :param pulumi.Input[pulumi.InputType['UserInfoArgs']] created_by: Describes a user that created the bookmark
        :param pulumi.Input[str] display_name: The display name of the bookmark
        :param pulumi.Input[str] event_time: The bookmark event time
        :param pulumi.Input[pulumi.InputType['IncidentInfoArgs']] incident_info: Describes an incident that relates to bookmark
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels relevant to this bookmark
        :param pulumi.Input[str] notes: The notes of the bookmark
        :param pulumi.Input[str] query: The query of the bookmark.
        :param pulumi.Input[str] query_end_time: The end time for the query
        :param pulumi.Input[str] query_result: The query result of the bookmark.
        :param pulumi.Input[str] query_start_time: The start time for the query
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] updated: The last time the bookmark was updated
        :param pulumi.Input[pulumi.InputType['UserInfoArgs']] updated_by: Describes a user that updated the bookmark
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BookmarkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a bookmark in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param BookmarkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BookmarkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bookmark_id: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[pulumi.InputType['UserInfoArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 event_time: Optional[pulumi.Input[str]] = None,
                 incident_info: Optional[pulumi.Input[pulumi.InputType['IncidentInfoArgs']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 query_end_time: Optional[pulumi.Input[str]] = None,
                 query_result: Optional[pulumi.Input[str]] = None,
                 query_start_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 updated: Optional[pulumi.Input[str]] = None,
                 updated_by: Optional[pulumi.Input[pulumi.InputType['UserInfoArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BookmarkArgs.__new__(BookmarkArgs)

            __props__.__dict__["bookmark_id"] = bookmark_id
            __props__.__dict__["created"] = created
            __props__.__dict__["created_by"] = created_by
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["event_time"] = event_time
            __props__.__dict__["incident_info"] = incident_info
            __props__.__dict__["labels"] = labels
            __props__.__dict__["notes"] = notes
            if query is None and not opts.urn:
                raise TypeError("Missing required property 'query'")
            __props__.__dict__["query"] = query
            __props__.__dict__["query_end_time"] = query_end_time
            __props__.__dict__["query_result"] = query_result
            __props__.__dict__["query_start_time"] = query_start_time
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["updated"] = updated
            __props__.__dict__["updated_by"] = updated_by
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20200101:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20221101:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:Bookmark"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:Bookmark")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Bookmark, __self__).__init__(
            'azure-native:securityinsights/v20211001:Bookmark',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Bookmark':
        """
        Get an existing Bookmark resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BookmarkArgs.__new__(BookmarkArgs)

        __props__.__dict__["created"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["event_time"] = None
        __props__.__dict__["incident_info"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["query"] = None
        __props__.__dict__["query_end_time"] = None
        __props__.__dict__["query_result"] = None
        __props__.__dict__["query_start_time"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated"] = None
        __props__.__dict__["updated_by"] = None
        return Bookmark(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[Optional[str]]:
        """
        The time the bookmark was created
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional['outputs.UserInfoResponse']]:
        """
        Describes a user that created the bookmark
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the bookmark
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> pulumi.Output[Optional[str]]:
        """
        The bookmark event time
        """
        return pulumi.get(self, "event_time")

    @property
    @pulumi.getter(name="incidentInfo")
    def incident_info(self) -> pulumi.Output[Optional['outputs.IncidentInfoResponse']]:
        """
        Describes an incident that relates to bookmark
        """
        return pulumi.get(self, "incident_info")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of labels relevant to this bookmark
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        The notes of the bookmark
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def query(self) -> pulumi.Output[str]:
        """
        The query of the bookmark.
        """
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="queryEndTime")
    def query_end_time(self) -> pulumi.Output[Optional[str]]:
        """
        The end time for the query
        """
        return pulumi.get(self, "query_end_time")

    @property
    @pulumi.getter(name="queryResult")
    def query_result(self) -> pulumi.Output[Optional[str]]:
        """
        The query result of the bookmark.
        """
        return pulumi.get(self, "query_result")

    @property
    @pulumi.getter(name="queryStartTime")
    def query_start_time(self) -> pulumi.Output[Optional[str]]:
        """
        The start time for the query
        """
        return pulumi.get(self, "query_start_time")

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

    @property
    @pulumi.getter
    def updated(self) -> pulumi.Output[Optional[str]]:
        """
        The last time the bookmark was updated
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[Optional['outputs.UserInfoResponse']]:
        """
        Describes a user that updated the bookmark
        """
        return pulumi.get(self, "updated_by")

