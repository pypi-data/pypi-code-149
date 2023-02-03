'''
# org-test-sample-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `ORG::TEST::SAMPLE::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type ORG::TEST::SAMPLE::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name ORG::TEST::SAMPLE::MODULE \
  --publisher-id 5b05ef5a51fcbc931d63aafe139bec8a97389a21 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/5b05ef5a51fcbc931d63aafe139bec8a97389a21/ORG-TEST-SAMPLE-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `ORG::TEST::SAMPLE::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Forg-test-sample-module+v1.0.0).
* Issues related to `ORG::TEST::SAMPLE::MODULE` should be reported to the [publisher](undefined).

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


class CfnSampleModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/org-test-sample-module.CfnSampleModule",
):
    '''A CloudFormation ``ORG::TEST::SAMPLE::MODULE``.

    :cloudformationResource: ORG::TEST::SAMPLE::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnSampleModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnSampleModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``ORG::TEST::SAMPLE::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab166c89ca59635b1a67444ea3b3cc9ec2ad19ffa6a7698c681101765caa2dec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSampleModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnSampleModuleProps":
        '''Resource props.'''
        return typing.cast("CfnSampleModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/org-test-sample-module.CfnSampleModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnSampleModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnSampleModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnSampleModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type ORG::TEST::SAMPLE::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnSampleModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnSampleModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnSampleModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57696c7ef34618517a2715ca0c625da78d1162762d3fd4f5415a1c6a83672ab1)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnSampleModulePropsParameters"]:
        '''
        :schema: CfnSampleModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnSampleModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnSampleModulePropsResources"]:
        '''
        :schema: CfnSampleModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnSampleModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSampleModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/org-test-sample-module.CfnSampleModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName"},
)
class CfnSampleModulePropsParameters:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[typing.Union["CfnSampleModulePropsParametersBucketName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Name for the bucket.

        :schema: CfnSampleModulePropsParameters
        '''
        if isinstance(bucket_name, dict):
            bucket_name = CfnSampleModulePropsParametersBucketName(**bucket_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4a1f82001e9662f199d97999f2fbe025f682dc57c3a146d8077eeec5765da8b)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name

    @builtins.property
    def bucket_name(
        self,
    ) -> typing.Optional["CfnSampleModulePropsParametersBucketName"]:
        '''Name for the bucket.

        :schema: CfnSampleModulePropsParameters#BucketName
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional["CfnSampleModulePropsParametersBucketName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSampleModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/org-test-sample-module.CfnSampleModulePropsParametersBucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnSampleModulePropsParametersBucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name for the bucket.

        :param description: 
        :param type: 

        :schema: CfnSampleModulePropsParametersBucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ed01f875a8a475dac05aa11bc17bda96a3dd975fb3876e8b2eb17117c0b26d0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnSampleModulePropsParametersBucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnSampleModulePropsParametersBucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSampleModulePropsParametersBucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/org-test-sample-module.CfnSampleModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"s3_bucket": "s3Bucket"},
)
class CfnSampleModulePropsResources:
    def __init__(
        self,
        *,
        s3_bucket: typing.Optional[typing.Union["CfnSampleModulePropsResourcesS3Bucket", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_bucket: 

        :schema: CfnSampleModulePropsResources
        '''
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnSampleModulePropsResourcesS3Bucket(**s3_bucket)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8e86663739320fcf69e1c0a94c4a805256fe61c821124843bd77296254f85ab)
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket

    @builtins.property
    def s3_bucket(self) -> typing.Optional["CfnSampleModulePropsResourcesS3Bucket"]:
        '''
        :schema: CfnSampleModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnSampleModulePropsResourcesS3Bucket"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSampleModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/org-test-sample-module.CfnSampleModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnSampleModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnSampleModulePropsResourcesS3Bucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bb301fd77ae2dd14551310497841c6924e9ab9ad5d833372b7113c72cb7c5bf)
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
        :schema: CfnSampleModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnSampleModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSampleModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSampleModule",
    "CfnSampleModuleProps",
    "CfnSampleModulePropsParameters",
    "CfnSampleModulePropsParametersBucketName",
    "CfnSampleModulePropsResources",
    "CfnSampleModulePropsResourcesS3Bucket",
]

publication.publish()

def _typecheckingstub__ab166c89ca59635b1a67444ea3b3cc9ec2ad19ffa6a7698c681101765caa2dec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnSampleModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnSampleModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57696c7ef34618517a2715ca0c625da78d1162762d3fd4f5415a1c6a83672ab1(
    *,
    parameters: typing.Optional[typing.Union[CfnSampleModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnSampleModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a1f82001e9662f199d97999f2fbe025f682dc57c3a146d8077eeec5765da8b(
    *,
    bucket_name: typing.Optional[typing.Union[CfnSampleModulePropsParametersBucketName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed01f875a8a475dac05aa11bc17bda96a3dd975fb3876e8b2eb17117c0b26d0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8e86663739320fcf69e1c0a94c4a805256fe61c821124843bd77296254f85ab(
    *,
    s3_bucket: typing.Optional[typing.Union[CfnSampleModulePropsResourcesS3Bucket, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bb301fd77ae2dd14551310497841c6924e9ab9ad5d833372b7113c72cb7c5bf(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
