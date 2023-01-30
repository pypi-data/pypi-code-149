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
    'GetTransformResult',
    'AwaitableGetTransformResult',
    'get_transform',
    'get_transform_output',
]

@pulumi.output_type
class GetTransformResult:
    """
    A Transform encapsulates the rules or instructions for generating desired outputs from input media, such as by transcoding or by extracting insights. After the Transform is created, it can be applied to input media by creating Jobs.
    """
    def __init__(__self__, created=None, description=None, id=None, last_modified=None, name=None, outputs=None, type=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outputs and not isinstance(outputs, list):
            raise TypeError("Expected argument 'outputs' to be a list")
        pulumi.set(__self__, "outputs", outputs)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The UTC date and time when the Transform was created, in 'YYYY-MM-DDThh:mm:ssZ' format.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        An optional verbose description of the Transform.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The UTC date and time when the Transform was last updated, in 'YYYY-MM-DDThh:mm:ssZ' format.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def outputs(self) -> Sequence['outputs.TransformOutputResponse']:
        """
        An array of one or more TransformOutputs that the Transform should generate.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetTransformResult(GetTransformResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransformResult(
            created=self.created,
            description=self.description,
            id=self.id,
            last_modified=self.last_modified,
            name=self.name,
            outputs=self.outputs,
            type=self.type)


def get_transform(account_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  transform_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransformResult:
    """
    A Transform encapsulates the rules or instructions for generating desired outputs from input media, such as by transcoding or by extracting insights. After the Transform is created, it can be applied to input media by creating Jobs.


    :param str account_name: The Media Services account name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    :param str transform_name: The Transform name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['transformName'] = transform_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20180601preview:getTransform', __args__, opts=opts, typ=GetTransformResult).value

    return AwaitableGetTransformResult(
        created=__ret__.created,
        description=__ret__.description,
        id=__ret__.id,
        last_modified=__ret__.last_modified,
        name=__ret__.name,
        outputs=__ret__.outputs,
        type=__ret__.type)


@_utilities.lift_output_func(get_transform)
def get_transform_output(account_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         transform_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransformResult]:
    """
    A Transform encapsulates the rules or instructions for generating desired outputs from input media, such as by transcoding or by extracting insights. After the Transform is created, it can be applied to input media by creating Jobs.


    :param str account_name: The Media Services account name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    :param str transform_name: The Transform name.
    """
    ...
