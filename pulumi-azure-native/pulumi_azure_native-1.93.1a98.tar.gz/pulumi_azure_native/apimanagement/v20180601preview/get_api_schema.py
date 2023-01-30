# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetApiSchemaResult',
    'AwaitableGetApiSchemaResult',
    'get_api_schema',
    'get_api_schema_output',
]

@pulumi.output_type
class GetApiSchemaResult:
    """
    Schema Contract details.
    """
    def __init__(__self__, content_type=None, id=None, name=None, type=None, value=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        """
        Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml).
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Json escaped string defining the document representing the Schema.
        """
        return pulumi.get(self, "value")


class AwaitableGetApiSchemaResult(GetApiSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiSchemaResult(
            content_type=self.content_type,
            id=self.id,
            name=self.name,
            type=self.type,
            value=self.value)


def get_api_schema(api_id: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   schema_id: Optional[str] = None,
                   service_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiSchemaResult:
    """
    Schema Contract details.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str resource_group_name: The name of the resource group.
    :param str schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['schemaId'] = schema_id
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20180601preview:getApiSchema', __args__, opts=opts, typ=GetApiSchemaResult).value

    return AwaitableGetApiSchemaResult(
        content_type=__ret__.content_type,
        id=__ret__.id,
        name=__ret__.name,
        type=__ret__.type,
        value=__ret__.value)


@_utilities.lift_output_func(get_api_schema)
def get_api_schema_output(api_id: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          schema_id: Optional[pulumi.Input[str]] = None,
                          service_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiSchemaResult]:
    """
    Schema Contract details.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str resource_group_name: The name of the resource group.
    :param str schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
    :param str service_name: The name of the API Management service.
    """
    ...
