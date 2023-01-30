# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListStorageAccountKeysResult',
    'AwaitableListStorageAccountKeysResult',
    'list_storage_account_keys',
    'list_storage_account_keys_output',
]

@pulumi.output_type
class ListStorageAccountKeysResult:
    def __init__(__self__, user_storage_key=None):
        if user_storage_key and not isinstance(user_storage_key, str):
            raise TypeError("Expected argument 'user_storage_key' to be a str")
        pulumi.set(__self__, "user_storage_key", user_storage_key)

    @property
    @pulumi.getter(name="userStorageKey")
    def user_storage_key(self) -> str:
        return pulumi.get(self, "user_storage_key")


class AwaitableListStorageAccountKeysResult(ListStorageAccountKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListStorageAccountKeysResult(
            user_storage_key=self.user_storage_key)


def list_storage_account_keys(resource_group_name: Optional[str] = None,
                              workspace_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListStorageAccountKeysResult:
    """
    API Version: 2021-01-01.


    :param str resource_group_name: Name of the resource group in which workspace is located.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices:listStorageAccountKeys', __args__, opts=opts, typ=ListStorageAccountKeysResult).value

    return AwaitableListStorageAccountKeysResult(
        user_storage_key=__ret__.user_storage_key)


@_utilities.lift_output_func(list_storage_account_keys)
def list_storage_account_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                     workspace_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListStorageAccountKeysResult]:
    """
    API Version: 2021-01-01.


    :param str resource_group_name: Name of the resource group in which workspace is located.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
