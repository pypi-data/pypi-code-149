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
    'GetInstancePoolResult',
    'AwaitableGetInstancePoolResult',
    'get_instance_pool',
    'get_instance_pool_output',
]

@pulumi.output_type
class GetInstancePoolResult:
    """
    An Azure SQL instance pool.
    """
    def __init__(__self__, id=None, license_type=None, location=None, name=None, sku=None, subnet_id=None, tags=None, type=None, v_cores=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if license_type and not isinstance(license_type, str):
            raise TypeError("Expected argument 'license_type' to be a str")
        pulumi.set(__self__, "license_type", license_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if v_cores and not isinstance(v_cores, int):
            raise TypeError("Expected argument 'v_cores' to be a int")
        pulumi.set(__self__, "v_cores", v_cores)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> str:
        """
        The license type. Possible values are 'LicenseIncluded' (price for SQL license is included) and 'BasePrice' (without SQL license price).
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The name and tier of the SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        Resource ID of the subnet to place this instance pool in.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> int:
        """
        Count of vCores belonging to this instance pool.
        """
        return pulumi.get(self, "v_cores")


class AwaitableGetInstancePoolResult(GetInstancePoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancePoolResult(
            id=self.id,
            license_type=self.license_type,
            location=self.location,
            name=self.name,
            sku=self.sku,
            subnet_id=self.subnet_id,
            tags=self.tags,
            type=self.type,
            v_cores=self.v_cores)


def get_instance_pool(instance_pool_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancePoolResult:
    """
    An Azure SQL instance pool.


    :param str instance_pool_name: The name of the instance pool to be retrieved.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['instancePoolName'] = instance_pool_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20220201preview:getInstancePool', __args__, opts=opts, typ=GetInstancePoolResult).value

    return AwaitableGetInstancePoolResult(
        id=__ret__.id,
        license_type=__ret__.license_type,
        location=__ret__.location,
        name=__ret__.name,
        sku=__ret__.sku,
        subnet_id=__ret__.subnet_id,
        tags=__ret__.tags,
        type=__ret__.type,
        v_cores=__ret__.v_cores)


@_utilities.lift_output_func(get_instance_pool)
def get_instance_pool_output(instance_pool_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancePoolResult]:
    """
    An Azure SQL instance pool.


    :param str instance_pool_name: The name of the instance pool to be retrieved.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
