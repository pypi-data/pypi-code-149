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
    'GetADLSGen2FileSystemDataSetResult',
    'AwaitableGetADLSGen2FileSystemDataSetResult',
    'get_adls_gen2_file_system_data_set',
    'get_adls_gen2_file_system_data_set_output',
]

@pulumi.output_type
class GetADLSGen2FileSystemDataSetResult:
    """
    An ADLS Gen 2 file system data set.
    """
    def __init__(__self__, data_set_id=None, file_system=None, id=None, kind=None, name=None, resource_group=None, storage_account_name=None, subscription_id=None, type=None):
        if data_set_id and not isinstance(data_set_id, str):
            raise TypeError("Expected argument 'data_set_id' to be a str")
        pulumi.set(__self__, "data_set_id", data_set_id)
        if file_system and not isinstance(file_system, str):
            raise TypeError("Expected argument 'file_system' to be a str")
        pulumi.set(__self__, "file_system", file_system)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group and not isinstance(resource_group, str):
            raise TypeError("Expected argument 'resource_group' to be a str")
        pulumi.set(__self__, "resource_group", resource_group)
        if storage_account_name and not isinstance(storage_account_name, str):
            raise TypeError("Expected argument 'storage_account_name' to be a str")
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> str:
        """
        Unique id for identifying a data set resource
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="fileSystem")
    def file_system(self) -> str:
        """
        The file system name.
        """
        return pulumi.get(self, "file_system")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of data set.
        Expected value is 'AdlsGen2FileSystem'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> str:
        """
        Resource group of storage account
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> str:
        """
        Storage account name of the source data set
        """
        return pulumi.get(self, "storage_account_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        Subscription id of storage account
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetADLSGen2FileSystemDataSetResult(GetADLSGen2FileSystemDataSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetADLSGen2FileSystemDataSetResult(
            data_set_id=self.data_set_id,
            file_system=self.file_system,
            id=self.id,
            kind=self.kind,
            name=self.name,
            resource_group=self.resource_group,
            storage_account_name=self.storage_account_name,
            subscription_id=self.subscription_id,
            type=self.type)


def get_adls_gen2_file_system_data_set(account_name: Optional[str] = None,
                                       data_set_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       share_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetADLSGen2FileSystemDataSetResult:
    """
    An ADLS Gen 2 file system data set.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetName'] = data_set_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datashare/v20181101preview:getADLSGen2FileSystemDataSet', __args__, opts=opts, typ=GetADLSGen2FileSystemDataSetResult).value

    return AwaitableGetADLSGen2FileSystemDataSetResult(
        data_set_id=__ret__.data_set_id,
        file_system=__ret__.file_system,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        resource_group=__ret__.resource_group,
        storage_account_name=__ret__.storage_account_name,
        subscription_id=__ret__.subscription_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_adls_gen2_file_system_data_set)
def get_adls_gen2_file_system_data_set_output(account_name: Optional[pulumi.Input[str]] = None,
                                              data_set_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              share_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetADLSGen2FileSystemDataSetResult]:
    """
    An ADLS Gen 2 file system data set.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    ...
