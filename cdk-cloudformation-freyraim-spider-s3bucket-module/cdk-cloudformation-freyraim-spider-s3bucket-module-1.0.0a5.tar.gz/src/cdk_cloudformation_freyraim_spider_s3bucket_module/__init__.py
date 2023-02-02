'''
# freyraim-spider-s3bucket-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::Spider::S3Bucket::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type FreyrAIM::Spider::S3Bucket::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::Spider::S3Bucket::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-Spider-S3Bucket-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::Spider::S3Bucket::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-spider-s3bucket-module+v1.0.0).
* Issues related to `FreyrAIM::Spider::S3Bucket::MODULE` should be reported to the [publisher](undefined).

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


class CfnS3BucketModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-spider-s3bucket-module.CfnS3BucketModule",
):
    '''A CloudFormation ``FreyrAIM::Spider::S3Bucket::MODULE``.

    :cloudformationResource: FreyrAIM::Spider::S3Bucket::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnS3BucketModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnS3BucketModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::Spider::S3Bucket::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea889969a894e99ab79609742b141a506754a9b597863d501cc58493e45628bf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnS3BucketModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnS3BucketModuleProps":
        '''Resource props.'''
        return typing.cast("CfnS3BucketModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-s3bucket-module.CfnS3BucketModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnS3BucketModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnS3BucketModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnS3BucketModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::Spider::S3Bucket::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnS3BucketModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnS3BucketModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnS3BucketModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a930a3b48dcf8f12182a9a0c91b14c62a4c477182ae1c37a87dfb2c2b947995b)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnS3BucketModulePropsParameters"]:
        '''
        :schema: CfnS3BucketModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnS3BucketModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnS3BucketModulePropsResources"]:
        '''
        :schema: CfnS3BucketModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnS3BucketModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3BucketModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-s3bucket-module.CfnS3BucketModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"env_name": "envName"},
)
class CfnS3BucketModulePropsParameters:
    def __init__(
        self,
        *,
        env_name: typing.Optional[typing.Union["CfnS3BucketModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param env_name: The environment name.

        :schema: CfnS3BucketModulePropsParameters
        '''
        if isinstance(env_name, dict):
            env_name = CfnS3BucketModulePropsParametersEnvName(**env_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__049052f82676ddf7cd5ef8d3218ffb0224fb528dbb9eaef094004edceb911458)
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if env_name is not None:
            self._values["env_name"] = env_name

    @builtins.property
    def env_name(self) -> typing.Optional["CfnS3BucketModulePropsParametersEnvName"]:
        '''The environment name.

        :schema: CfnS3BucketModulePropsParameters#EnvName
        '''
        result = self._values.get("env_name")
        return typing.cast(typing.Optional["CfnS3BucketModulePropsParametersEnvName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3BucketModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-s3bucket-module.CfnS3BucketModulePropsParametersEnvName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnS3BucketModulePropsParametersEnvName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnS3BucketModulePropsParametersEnvName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7154cf6887146b5a91d35bd7084fc847d7782db487436ce33094dbb42d5dbe04)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnS3BucketModulePropsParametersEnvName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnS3BucketModulePropsParametersEnvName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3BucketModulePropsParametersEnvName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-s3bucket-module.CfnS3BucketModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"s3_bucket": "s3Bucket", "s3_bucket_policy": "s3BucketPolicy"},
)
class CfnS3BucketModulePropsResources:
    def __init__(
        self,
        *,
        s3_bucket: typing.Optional[typing.Union["CfnS3BucketModulePropsResourcesS3Bucket", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket_policy: typing.Optional[typing.Union["CfnS3BucketModulePropsResourcesS3BucketPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_bucket: 
        :param s3_bucket_policy: 

        :schema: CfnS3BucketModulePropsResources
        '''
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnS3BucketModulePropsResourcesS3Bucket(**s3_bucket)
        if isinstance(s3_bucket_policy, dict):
            s3_bucket_policy = CfnS3BucketModulePropsResourcesS3BucketPolicy(**s3_bucket_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b7d56b1b302e00fddf2d4dbb17339a25e57fa2379df3bea07eb99c532a72700)
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument s3_bucket_policy", value=s3_bucket_policy, expected_type=type_hints["s3_bucket_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket
        if s3_bucket_policy is not None:
            self._values["s3_bucket_policy"] = s3_bucket_policy

    @builtins.property
    def s3_bucket(self) -> typing.Optional["CfnS3BucketModulePropsResourcesS3Bucket"]:
        '''
        :schema: CfnS3BucketModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnS3BucketModulePropsResourcesS3Bucket"], result)

    @builtins.property
    def s3_bucket_policy(
        self,
    ) -> typing.Optional["CfnS3BucketModulePropsResourcesS3BucketPolicy"]:
        '''
        :schema: CfnS3BucketModulePropsResources#S3BucketPolicy
        '''
        result = self._values.get("s3_bucket_policy")
        return typing.cast(typing.Optional["CfnS3BucketModulePropsResourcesS3BucketPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3BucketModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-s3bucket-module.CfnS3BucketModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnS3BucketModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnS3BucketModulePropsResourcesS3Bucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d5e3160996f660efb87bcbe169e866b6df84d8f5d1007bde29827682f88ca8)
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
        :schema: CfnS3BucketModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3BucketModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3BucketModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-s3bucket-module.CfnS3BucketModulePropsResourcesS3BucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnS3BucketModulePropsResourcesS3BucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnS3BucketModulePropsResourcesS3BucketPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c89599f2305c9752e952f06468ee5c9c481f66d00c8ac4cf28da8f9f7051723)
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
        :schema: CfnS3BucketModulePropsResourcesS3BucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3BucketModulePropsResourcesS3BucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3BucketModulePropsResourcesS3BucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnS3BucketModule",
    "CfnS3BucketModuleProps",
    "CfnS3BucketModulePropsParameters",
    "CfnS3BucketModulePropsParametersEnvName",
    "CfnS3BucketModulePropsResources",
    "CfnS3BucketModulePropsResourcesS3Bucket",
    "CfnS3BucketModulePropsResourcesS3BucketPolicy",
]

publication.publish()

def _typecheckingstub__ea889969a894e99ab79609742b141a506754a9b597863d501cc58493e45628bf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnS3BucketModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnS3BucketModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a930a3b48dcf8f12182a9a0c91b14c62a4c477182ae1c37a87dfb2c2b947995b(
    *,
    parameters: typing.Optional[typing.Union[CfnS3BucketModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnS3BucketModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049052f82676ddf7cd5ef8d3218ffb0224fb528dbb9eaef094004edceb911458(
    *,
    env_name: typing.Optional[typing.Union[CfnS3BucketModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7154cf6887146b5a91d35bd7084fc847d7782db487436ce33094dbb42d5dbe04(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b7d56b1b302e00fddf2d4dbb17339a25e57fa2379df3bea07eb99c532a72700(
    *,
    s3_bucket: typing.Optional[typing.Union[CfnS3BucketModulePropsResourcesS3Bucket, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket_policy: typing.Optional[typing.Union[CfnS3BucketModulePropsResourcesS3BucketPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d5e3160996f660efb87bcbe169e866b6df84d8f5d1007bde29827682f88ca8(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c89599f2305c9752e952f06468ee5c9c481f66d00c8ac4cf28da8f9f7051723(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
