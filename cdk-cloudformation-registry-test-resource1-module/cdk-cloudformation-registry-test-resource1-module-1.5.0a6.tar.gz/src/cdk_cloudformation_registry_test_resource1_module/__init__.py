'''
# registry-test-resource1-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `REGISTRY::TEST::RESOURCE1::MODULE` v1.5.0.

---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This package is deprecated

---


## Description

Schema for Module Fragment of type REGISTRY::TEST::RESOURCE::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name REGISTRY::TEST::RESOURCE1::MODULE \
  --publisher-id 4686b5f994c8b12636b1af16ce88b8e2d2e75c8c \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/4686b5f994c8b12636b1af16ce88b8e2d2e75c8c/REGISTRY-TEST-RESOURCE1-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `REGISTRY::TEST::RESOURCE1::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fregistry-test-resource1-module+v1.5.0).
* Issues related to `REGISTRY::TEST::RESOURCE1::MODULE` should be reported to the [publisher](undefined).

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


class CfnResource1Module(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1Module",
):
    '''A CloudFormation ``REGISTRY::TEST::RESOURCE1::MODULE``.

    :cloudformationResource: REGISTRY::TEST::RESOURCE1::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnResource1ModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnResource1ModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``REGISTRY::TEST::RESOURCE1::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b932cbbc441e6cbbb32570150fa906bb787c9b0b67fc02474c1ee9b08f892927)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResource1ModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnResource1ModuleProps":
        '''Resource props.'''
        return typing.cast("CfnResource1ModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnResource1ModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnResource1ModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnResource1ModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(deprecated) Schema for Module Fragment of type REGISTRY::TEST::RESOURCE::MODULE.

        :param parameters: 
        :param resources: 

        :stability: deprecated
        :schema: CfnResource1ModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnResource1ModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnResource1ModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5349c4761216ba4a76605e664f3755f6c06ad134ad99c2bc5554e3896e56b4f4)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnResource1ModulePropsParameters"]:
        '''
        :stability: deprecated
        :schema: CfnResource1ModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnResource1ModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnResource1ModulePropsResources"]:
        '''
        :stability: deprecated
        :schema: CfnResource1ModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnResource1ModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName"},
)
class CfnResource1ModulePropsParameters:
    def __init__(
        self,
        *,
        bucket_name: typing.Optional[typing.Union["CfnResource1ModulePropsParametersBucketName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: (deprecated) Name for the bucket.

        :stability: deprecated
        :schema: CfnResource1ModulePropsParameters
        '''
        if isinstance(bucket_name, dict):
            bucket_name = CfnResource1ModulePropsParametersBucketName(**bucket_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999db82a8da370b9a02fa678899726813686138183ad1485a166272ac752e820)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name

    @builtins.property
    def bucket_name(
        self,
    ) -> typing.Optional["CfnResource1ModulePropsParametersBucketName"]:
        '''(deprecated) Name for the bucket.

        :stability: deprecated
        :schema: CfnResource1ModulePropsParameters#BucketName
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional["CfnResource1ModulePropsParametersBucketName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModulePropsParametersBucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnResource1ModulePropsParametersBucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(deprecated) Name for the bucket.

        :param description: 
        :param type: 

        :stability: deprecated
        :schema: CfnResource1ModulePropsParametersBucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba3ae83cee46c9a7857d3a5b62304157770952c6c4b24ff6321910379947665e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :stability: deprecated
        :schema: CfnResource1ModulePropsParametersBucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :stability: deprecated
        :schema: CfnResource1ModulePropsParametersBucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModulePropsParametersBucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={"s3_bucket": "s3Bucket"},
)
class CfnResource1ModulePropsResources:
    def __init__(
        self,
        *,
        s3_bucket: typing.Optional[typing.Union["CfnResource1ModulePropsResourcesS3Bucket", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_bucket: 

        :stability: deprecated
        :schema: CfnResource1ModulePropsResources
        '''
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnResource1ModulePropsResourcesS3Bucket(**s3_bucket)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b6dbc217a9d454557c8ae9fa43bfac8f48049522f8fdde82aed6266664d3ea)
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket

    @builtins.property
    def s3_bucket(self) -> typing.Optional["CfnResource1ModulePropsResourcesS3Bucket"]:
        '''
        :stability: deprecated
        :schema: CfnResource1ModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnResource1ModulePropsResourcesS3Bucket"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/registry-test-resource1-module.CfnResource1ModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnResource1ModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :stability: deprecated
        :schema: CfnResource1ModulePropsResourcesS3Bucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea018c5a52a4e196a502237519cdef04641b059f1c04a3285b1d12f8c69e592)
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
        :stability: deprecated
        :schema: CfnResource1ModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnResource1ModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResource1ModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnResource1Module",
    "CfnResource1ModuleProps",
    "CfnResource1ModulePropsParameters",
    "CfnResource1ModulePropsParametersBucketName",
    "CfnResource1ModulePropsResources",
    "CfnResource1ModulePropsResourcesS3Bucket",
]

publication.publish()

def _typecheckingstub__b932cbbc441e6cbbb32570150fa906bb787c9b0b67fc02474c1ee9b08f892927(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnResource1ModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnResource1ModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5349c4761216ba4a76605e664f3755f6c06ad134ad99c2bc5554e3896e56b4f4(
    *,
    parameters: typing.Optional[typing.Union[CfnResource1ModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnResource1ModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999db82a8da370b9a02fa678899726813686138183ad1485a166272ac752e820(
    *,
    bucket_name: typing.Optional[typing.Union[CfnResource1ModulePropsParametersBucketName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3ae83cee46c9a7857d3a5b62304157770952c6c4b24ff6321910379947665e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b6dbc217a9d454557c8ae9fa43bfac8f48049522f8fdde82aed6266664d3ea(
    *,
    s3_bucket: typing.Optional[typing.Union[CfnResource1ModulePropsResourcesS3Bucket, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea018c5a52a4e196a502237519cdef04641b059f1c04a3285b1d12f8c69e592(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
