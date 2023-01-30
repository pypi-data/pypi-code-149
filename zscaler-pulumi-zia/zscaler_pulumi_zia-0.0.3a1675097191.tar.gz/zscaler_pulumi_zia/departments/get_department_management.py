# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetDepartmentManagementResult',
    'AwaitableGetDepartmentManagementResult',
    'get_department_management',
    'get_department_management_output',
]

@pulumi.output_type
class GetDepartmentManagementResult:
    """
    A collection of values returned by getDepartmentManagement.
    """
    def __init__(__self__, comments=None, deleted=None, id=None, idp_id=None, name=None):
        if comments and not isinstance(comments, str):
            raise TypeError("Expected argument 'comments' to be a str")
        pulumi.set(__self__, "comments", comments)
        if deleted and not isinstance(deleted, bool):
            raise TypeError("Expected argument 'deleted' to be a bool")
        pulumi.set(__self__, "deleted", deleted)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if idp_id and not isinstance(idp_id, int):
            raise TypeError("Expected argument 'idp_id' to be a int")
        pulumi.set(__self__, "idp_id", idp_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def comments(self) -> str:
        return pulumi.get(self, "comments")

    @property
    @pulumi.getter
    def deleted(self) -> bool:
        return pulumi.get(self, "deleted")

    @property
    @pulumi.getter
    def id(self) -> int:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idpId")
    def idp_id(self) -> int:
        return pulumi.get(self, "idp_id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")


class AwaitableGetDepartmentManagementResult(GetDepartmentManagementResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDepartmentManagementResult(
            comments=self.comments,
            deleted=self.deleted,
            id=self.id,
            idp_id=self.idp_id,
            name=self.name)


def get_department_management(name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDepartmentManagementResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('zia:Departments/getDepartmentManagement:getDepartmentManagement', __args__, opts=opts, typ=GetDepartmentManagementResult).value

    return AwaitableGetDepartmentManagementResult(
        comments=__ret__.comments,
        deleted=__ret__.deleted,
        id=__ret__.id,
        idp_id=__ret__.idp_id,
        name=__ret__.name)


@_utilities.lift_output_func(get_department_management)
def get_department_management_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDepartmentManagementResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
