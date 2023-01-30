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
    'GetIntegrationAccountSchemaResult',
    'AwaitableGetIntegrationAccountSchemaResult',
    'get_integration_account_schema',
    'get_integration_account_schema_output',
]

@pulumi.output_type
class GetIntegrationAccountSchemaResult:
    """
    The integration account schema.
    """
    def __init__(__self__, changed_time=None, content=None, content_link=None, content_type=None, created_time=None, document_name=None, file_name=None, id=None, location=None, metadata=None, name=None, schema_type=None, tags=None, target_namespace=None, type=None):
        if changed_time and not isinstance(changed_time, str):
            raise TypeError("Expected argument 'changed_time' to be a str")
        pulumi.set(__self__, "changed_time", changed_time)
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if content_link and not isinstance(content_link, dict):
            raise TypeError("Expected argument 'content_link' to be a dict")
        pulumi.set(__self__, "content_link", content_link)
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if document_name and not isinstance(document_name, str):
            raise TypeError("Expected argument 'document_name' to be a str")
        pulumi.set(__self__, "document_name", document_name)
        if file_name and not isinstance(file_name, str):
            raise TypeError("Expected argument 'file_name' to be a str")
        pulumi.set(__self__, "file_name", file_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schema_type and not isinstance(schema_type, str):
            raise TypeError("Expected argument 'schema_type' to be a str")
        pulumi.set(__self__, "schema_type", schema_type)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_namespace and not isinstance(target_namespace, str):
            raise TypeError("Expected argument 'target_namespace' to be a str")
        pulumi.set(__self__, "target_namespace", target_namespace)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> str:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        The content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> 'outputs.ContentLinkResponse':
        """
        The content link.
        """
        return pulumi.get(self, "content_link")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        """
        The content type.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="documentName")
    def document_name(self) -> Optional[str]:
        """
        The document name.
        """
        return pulumi.get(self, "document_name")

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[str]:
        """
        The file name.
        """
        return pulumi.get(self, "file_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> str:
        """
        The schema type.
        """
        return pulumi.get(self, "schema_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> Optional[str]:
        """
        The target namespace of the schema.
        """
        return pulumi.get(self, "target_namespace")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIntegrationAccountSchemaResult(GetIntegrationAccountSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationAccountSchemaResult(
            changed_time=self.changed_time,
            content=self.content,
            content_link=self.content_link,
            content_type=self.content_type,
            created_time=self.created_time,
            document_name=self.document_name,
            file_name=self.file_name,
            id=self.id,
            location=self.location,
            metadata=self.metadata,
            name=self.name,
            schema_type=self.schema_type,
            tags=self.tags,
            target_namespace=self.target_namespace,
            type=self.type)


def get_integration_account_schema(integration_account_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   schema_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationAccountSchemaResult:
    """
    The integration account schema.


    :param str integration_account_name: The integration account name.
    :param str resource_group_name: The resource group name.
    :param str schema_name: The integration account schema name.
    """
    __args__ = dict()
    __args__['integrationAccountName'] = integration_account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['schemaName'] = schema_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:logic/v20190501:getIntegrationAccountSchema', __args__, opts=opts, typ=GetIntegrationAccountSchemaResult).value

    return AwaitableGetIntegrationAccountSchemaResult(
        changed_time=__ret__.changed_time,
        content=__ret__.content,
        content_link=__ret__.content_link,
        content_type=__ret__.content_type,
        created_time=__ret__.created_time,
        document_name=__ret__.document_name,
        file_name=__ret__.file_name,
        id=__ret__.id,
        location=__ret__.location,
        metadata=__ret__.metadata,
        name=__ret__.name,
        schema_type=__ret__.schema_type,
        tags=__ret__.tags,
        target_namespace=__ret__.target_namespace,
        type=__ret__.type)


@_utilities.lift_output_func(get_integration_account_schema)
def get_integration_account_schema_output(integration_account_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          schema_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIntegrationAccountSchemaResult]:
    """
    The integration account schema.


    :param str integration_account_name: The integration account name.
    :param str resource_group_name: The resource group name.
    :param str schema_name: The integration account schema name.
    """
    ...
