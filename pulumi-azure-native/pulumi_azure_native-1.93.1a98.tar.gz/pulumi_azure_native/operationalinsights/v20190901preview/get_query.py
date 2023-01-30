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
    'GetQueryResult',
    'AwaitableGetQueryResult',
    'get_query',
    'get_query_output',
]

@pulumi.output_type
class GetQueryResult:
    """
    A Log Analytics QueryPack-Query definition.
    """
    def __init__(__self__, author=None, body=None, description=None, display_name=None, id=None, name=None, properties=None, related=None, system_data=None, tags=None, time_created=None, time_modified=None, type=None):
        if author and not isinstance(author, str):
            raise TypeError("Expected argument 'author' to be a str")
        pulumi.set(__self__, "author", author)
        if body and not isinstance(body, str):
            raise TypeError("Expected argument 'body' to be a str")
        pulumi.set(__self__, "body", body)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if related and not isinstance(related, dict):
            raise TypeError("Expected argument 'related' to be a dict")
        pulumi.set(__self__, "related", related)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_modified and not isinstance(time_modified, str):
            raise TypeError("Expected argument 'time_modified' to be a str")
        pulumi.set(__self__, "time_modified", time_modified)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def author(self) -> str:
        """
        Object Id of user creating the query.
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def body(self) -> str:
        """
        Body of the query.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the query.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Unique display name for your query within the Query Pack.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Any:
        """
        Additional properties that can be set for the query.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def related(self) -> Optional['outputs.LogAnalyticsQueryPackQueryPropertiesResponseRelated']:
        """
        The related metadata items for the function.
        """
        return pulumi.get(self, "related")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Sequence[str]]]:
        """
        Tags associated with the query.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        Creation Date for the Log Analytics Query, in ISO 8601 format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> str:
        """
        Last modified date of the Log Analytics Query, in ISO 8601 format.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetQueryResult(GetQueryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQueryResult(
            author=self.author,
            body=self.body,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            properties=self.properties,
            related=self.related,
            system_data=self.system_data,
            tags=self.tags,
            time_created=self.time_created,
            time_modified=self.time_modified,
            type=self.type)


def get_query(id: Optional[str] = None,
              query_pack_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQueryResult:
    """
    A Log Analytics QueryPack-Query definition.


    :param str id: The id of a specific query defined in the Log Analytics QueryPack
    :param str query_pack_name: The name of the Log Analytics QueryPack resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['queryPackName'] = query_pack_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights/v20190901preview:getQuery', __args__, opts=opts, typ=GetQueryResult).value

    return AwaitableGetQueryResult(
        author=__ret__.author,
        body=__ret__.body,
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        related=__ret__.related,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        time_created=__ret__.time_created,
        time_modified=__ret__.time_modified,
        type=__ret__.type)


@_utilities.lift_output_func(get_query)
def get_query_output(id: Optional[pulumi.Input[str]] = None,
                     query_pack_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQueryResult]:
    """
    A Log Analytics QueryPack-Query definition.


    :param str id: The id of a specific query defined in the Log Analytics QueryPack
    :param str query_pack_name: The name of the Log Analytics QueryPack resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
