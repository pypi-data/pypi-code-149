'''
# tf-ad-computer

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::AD::Computer` v1.0.0.

## Description

CloudFormation equivalent of ad_computer

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/ad/TF-AD-Computer/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::AD::Computer \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-AD-Computer \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::AD::Computer`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-ad-computer+v1.0.0).
* Issues related to `TF::AD::Computer` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/ad/TF-AD-Computer/docs/README.md).

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class CfnComputer(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-ad-computer.CfnComputer",
):
    '''A CloudFormation ``TF::AD::Computer``.

    :cloudformationResource: TF::AD::Computer
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        container: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        pre2_kname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``TF::AD::Computer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: 
        :param container: 
        :param description: 
        :param pre2_kname: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88232ac00a4fbefc60bd0b1cd5b7116a4facf441c512f3e8fa8507568bb152f3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComputerProps(
            name=name,
            container=container,
            description=description,
            pre2_kname=pre2_kname,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDn")
    def attr_dn(self) -> builtins.str:
        '''Attribute ``TF::AD::Computer.Dn``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDn"))

    @builtins.property
    @jsii.member(jsii_name="attrGuid")
    def attr_guid(self) -> builtins.str:
        '''Attribute ``TF::AD::Computer.Guid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGuid"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``TF::AD::Computer.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSid")
    def attr_sid(self) -> builtins.str:
        '''Attribute ``TF::AD::Computer.Sid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSid"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::AD::Computer.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnComputerProps":
        '''Resource props.'''
        return typing.cast("CfnComputerProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-ad-computer.CfnComputerProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "container": "container",
        "description": "description",
        "pre2_kname": "pre2Kname",
    },
)
class CfnComputerProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        container: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        pre2_kname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''CloudFormation equivalent of ad_computer.

        :param name: 
        :param container: 
        :param description: 
        :param pre2_kname: 

        :schema: CfnComputerProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b3f870e4b04bdf97ca105d312ee45654bee22fcc230b39c58124bcbdb54de9c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument pre2_kname", value=pre2_kname, expected_type=type_hints["pre2_kname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if container is not None:
            self._values["container"] = container
        if description is not None:
            self._values["description"] = description
        if pre2_kname is not None:
            self._values["pre2_kname"] = pre2_kname

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: CfnComputerProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnComputerProps#Container
        '''
        result = self._values.get("container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnComputerProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pre2_kname(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnComputerProps#Pre2kname
        '''
        result = self._values.get("pre2_kname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComputerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComputer",
    "CfnComputerProps",
]

publication.publish()

def _typecheckingstub__88232ac00a4fbefc60bd0b1cd5b7116a4facf441c512f3e8fa8507568bb152f3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    container: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    pre2_kname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b3f870e4b04bdf97ca105d312ee45654bee22fcc230b39c58124bcbdb54de9c(
    *,
    name: builtins.str,
    container: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    pre2_kname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
