'''
# zmk-iam-lambdabasicrole-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `zmk::IAM::LambdaBasicRole::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type zmk::IAM::LambdaBasicRole::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name zmk::IAM::LambdaBasicRole::MODULE \
  --publisher-id 926aa6a6595e13ea95b60697274c934dbd591182 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/926aa6a6595e13ea95b60697274c934dbd591182/zmk-IAM-LambdaBasicRole-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `zmk::IAM::LambdaBasicRole::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fzmk-iam-lambdabasicrole-module+v1.0.0).
* Issues related to `zmk::IAM::LambdaBasicRole::MODULE` should be reported to the [publisher](undefined).

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


class CfnLambdaBasicRoleModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/zmk-iam-lambdabasicrole-module.CfnLambdaBasicRoleModule",
):
    '''A CloudFormation ``zmk::IAM::LambdaBasicRole::MODULE``.

    :cloudformationResource: zmk::IAM::LambdaBasicRole::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resources: typing.Optional[typing.Union["CfnLambdaBasicRoleModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``zmk::IAM::LambdaBasicRole::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d2edb0aa968efb2bbf67029def1ba2073dda7bb7f7501d8f72d38de00140f28)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLambdaBasicRoleModuleProps(resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnLambdaBasicRoleModuleProps":
        '''Resource props.'''
        return typing.cast("CfnLambdaBasicRoleModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/zmk-iam-lambdabasicrole-module.CfnLambdaBasicRoleModuleProps",
    jsii_struct_bases=[],
    name_mapping={"resources": "resources"},
)
class CfnLambdaBasicRoleModuleProps:
    def __init__(
        self,
        *,
        resources: typing.Optional[typing.Union["CfnLambdaBasicRoleModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type zmk::IAM::LambdaBasicRole::MODULE.

        :param resources: 

        :schema: CfnLambdaBasicRoleModuleProps
        '''
        if isinstance(resources, dict):
            resources = CfnLambdaBasicRoleModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0806cb6cb88c8d0459fc2d5d8ef0ff0e2e74a7afef8bb237469079c2bbf8087)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def resources(self) -> typing.Optional["CfnLambdaBasicRoleModulePropsResources"]:
        '''
        :schema: CfnLambdaBasicRoleModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnLambdaBasicRoleModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaBasicRoleModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/zmk-iam-lambdabasicrole-module.CfnLambdaBasicRoleModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"iam_role": "iamRole"},
)
class CfnLambdaBasicRoleModulePropsResources:
    def __init__(
        self,
        *,
        iam_role: typing.Optional[typing.Union["CfnLambdaBasicRoleModulePropsResourcesIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param iam_role: 

        :schema: CfnLambdaBasicRoleModulePropsResources
        '''
        if isinstance(iam_role, dict):
            iam_role = CfnLambdaBasicRoleModulePropsResourcesIamRole(**iam_role)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55e9650c9e9e0e349c71c7678652259ddd792448986dee786d79f61cbeda004e)
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if iam_role is not None:
            self._values["iam_role"] = iam_role

    @builtins.property
    def iam_role(
        self,
    ) -> typing.Optional["CfnLambdaBasicRoleModulePropsResourcesIamRole"]:
        '''
        :schema: CfnLambdaBasicRoleModulePropsResources#IAMRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnLambdaBasicRoleModulePropsResourcesIamRole"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaBasicRoleModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/zmk-iam-lambdabasicrole-module.CfnLambdaBasicRoleModulePropsResourcesIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaBasicRoleModulePropsResourcesIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaBasicRoleModulePropsResourcesIamRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3531114c378c0c9a4181bc0eb9fecde4ce574466e9ff8e67005145edcaaa5be6)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnLambdaBasicRoleModulePropsResourcesIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaBasicRoleModulePropsResourcesIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaBasicRoleModulePropsResourcesIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLambdaBasicRoleModule",
    "CfnLambdaBasicRoleModuleProps",
    "CfnLambdaBasicRoleModulePropsResources",
    "CfnLambdaBasicRoleModulePropsResourcesIamRole",
]

publication.publish()

def _typecheckingstub__2d2edb0aa968efb2bbf67029def1ba2073dda7bb7f7501d8f72d38de00140f28(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resources: typing.Optional[typing.Union[CfnLambdaBasicRoleModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0806cb6cb88c8d0459fc2d5d8ef0ff0e2e74a7afef8bb237469079c2bbf8087(
    *,
    resources: typing.Optional[typing.Union[CfnLambdaBasicRoleModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55e9650c9e9e0e349c71c7678652259ddd792448986dee786d79f61cbeda004e(
    *,
    iam_role: typing.Optional[typing.Union[CfnLambdaBasicRoleModulePropsResourcesIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3531114c378c0c9a4181bc0eb9fecde4ce574466e9ff8e67005145edcaaa5be6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
