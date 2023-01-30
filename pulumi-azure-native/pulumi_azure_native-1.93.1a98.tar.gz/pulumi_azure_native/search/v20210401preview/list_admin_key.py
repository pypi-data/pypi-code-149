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
    'ListAdminKeyResult',
    'AwaitableListAdminKeyResult',
    'list_admin_key',
    'list_admin_key_output',
]

@pulumi.output_type
class ListAdminKeyResult:
    """
    Response containing the primary and secondary admin API keys for a given Azure Cognitive Search service.
    """
    def __init__(__self__, primary_key=None, secondary_key=None):
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        The primary admin API key of the search service.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        The secondary admin API key of the search service.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListAdminKeyResult(ListAdminKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAdminKeyResult(
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_admin_key(resource_group_name: Optional[str] = None,
                   search_service_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAdminKeyResult:
    """
    Response containing the primary and secondary admin API keys for a given Azure Cognitive Search service.


    :param str resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str search_service_name: The name of the Azure Cognitive Search service associated with the specified resource group.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['searchServiceName'] = search_service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:search/v20210401preview:listAdminKey', __args__, opts=opts, typ=ListAdminKeyResult).value

    return AwaitableListAdminKeyResult(
        primary_key=__ret__.primary_key,
        secondary_key=__ret__.secondary_key)


@_utilities.lift_output_func(list_admin_key)
def list_admin_key_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                          search_service_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAdminKeyResult]:
    """
    Response containing the primary and secondary admin API keys for a given Azure Cognitive Search service.


    :param str resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str search_service_name: The name of the Azure Cognitive Search service associated with the specified resource group.
    """
    ...
