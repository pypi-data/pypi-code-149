'''
# freyraim-spider-cloudfront-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::Spider::CloudFront::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type FreyrAIM::Spider::CloudFront::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::Spider::CloudFront::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-Spider-CloudFront-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::Spider::CloudFront::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-spider-cloudfront-module+v1.0.0).
* Issues related to `FreyrAIM::Spider::CloudFront::MODULE` should be reported to the [publisher](undefined).

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


class CfnCloudFrontModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-spider-cloudfront-module.CfnCloudFrontModule",
):
    '''A CloudFormation ``FreyrAIM::Spider::CloudFront::MODULE``.

    :cloudformationResource: FreyrAIM::Spider::CloudFront::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnCloudFrontModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCloudFrontModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::Spider::CloudFront::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e69d844e0505806b44ef1a2a92cdfa5cddd4565bf2f7acc3dad881c98610c24c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudFrontModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudFrontModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCloudFrontModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-cloudfront-module.CfnCloudFrontModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCloudFrontModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnCloudFrontModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCloudFrontModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::Spider::CloudFront::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCloudFrontModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCloudFrontModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCloudFrontModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6649fdb8e26356a4a2bdd4bb0952e4ca4ecd09d572bd93a281d6f07f94254619)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCloudFrontModulePropsParameters"]:
        '''
        :schema: CfnCloudFrontModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCloudFrontModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCloudFrontModulePropsResources"]:
        '''
        :schema: CfnCloudFrontModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCloudFrontModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFrontModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-cloudfront-module.CfnCloudFrontModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"env_name": "envName"},
)
class CfnCloudFrontModulePropsParameters:
    def __init__(
        self,
        *,
        env_name: typing.Optional[typing.Union["CfnCloudFrontModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param env_name: The environment name.

        :schema: CfnCloudFrontModulePropsParameters
        '''
        if isinstance(env_name, dict):
            env_name = CfnCloudFrontModulePropsParametersEnvName(**env_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b7f378752dcf00c8e7552ffa4fa532d8bfb9238d4586b5b3738d347ed2f45c)
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if env_name is not None:
            self._values["env_name"] = env_name

    @builtins.property
    def env_name(self) -> typing.Optional["CfnCloudFrontModulePropsParametersEnvName"]:
        '''The environment name.

        :schema: CfnCloudFrontModulePropsParameters#EnvName
        '''
        result = self._values.get("env_name")
        return typing.cast(typing.Optional["CfnCloudFrontModulePropsParametersEnvName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFrontModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-cloudfront-module.CfnCloudFrontModulePropsParametersEnvName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudFrontModulePropsParametersEnvName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnCloudFrontModulePropsParametersEnvName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33910190033a5ce9a0a0fc87ba106f7cfdba98ea36cd3c14129ed04dd7b19f29)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudFrontModulePropsParametersEnvName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudFrontModulePropsParametersEnvName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFrontModulePropsParametersEnvName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-cloudfront-module.CfnCloudFrontModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket": "s3Bucket",
        "s3_bucket_policy": "s3BucketPolicy",
        "spider_cloud_front": "spiderCloudFront",
    },
)
class CfnCloudFrontModulePropsResources:
    def __init__(
        self,
        *,
        s3_bucket: typing.Optional[typing.Union["CfnCloudFrontModulePropsResourcesS3Bucket", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket_policy: typing.Optional[typing.Union["CfnCloudFrontModulePropsResourcesS3BucketPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        spider_cloud_front: typing.Optional[typing.Union["CfnCloudFrontModulePropsResourcesSpiderCloudFront", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_bucket: 
        :param s3_bucket_policy: 
        :param spider_cloud_front: 

        :schema: CfnCloudFrontModulePropsResources
        '''
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnCloudFrontModulePropsResourcesS3Bucket(**s3_bucket)
        if isinstance(s3_bucket_policy, dict):
            s3_bucket_policy = CfnCloudFrontModulePropsResourcesS3BucketPolicy(**s3_bucket_policy)
        if isinstance(spider_cloud_front, dict):
            spider_cloud_front = CfnCloudFrontModulePropsResourcesSpiderCloudFront(**spider_cloud_front)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__441649bb9c153466e74389d059867b137682db5f5d2b80f1b043200d1f210b73)
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument s3_bucket_policy", value=s3_bucket_policy, expected_type=type_hints["s3_bucket_policy"])
            check_type(argname="argument spider_cloud_front", value=spider_cloud_front, expected_type=type_hints["spider_cloud_front"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket
        if s3_bucket_policy is not None:
            self._values["s3_bucket_policy"] = s3_bucket_policy
        if spider_cloud_front is not None:
            self._values["spider_cloud_front"] = spider_cloud_front

    @builtins.property
    def s3_bucket(self) -> typing.Optional["CfnCloudFrontModulePropsResourcesS3Bucket"]:
        '''
        :schema: CfnCloudFrontModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnCloudFrontModulePropsResourcesS3Bucket"], result)

    @builtins.property
    def s3_bucket_policy(
        self,
    ) -> typing.Optional["CfnCloudFrontModulePropsResourcesS3BucketPolicy"]:
        '''
        :schema: CfnCloudFrontModulePropsResources#S3BucketPolicy
        '''
        result = self._values.get("s3_bucket_policy")
        return typing.cast(typing.Optional["CfnCloudFrontModulePropsResourcesS3BucketPolicy"], result)

    @builtins.property
    def spider_cloud_front(
        self,
    ) -> typing.Optional["CfnCloudFrontModulePropsResourcesSpiderCloudFront"]:
        '''
        :schema: CfnCloudFrontModulePropsResources#SpiderCloudFront
        '''
        result = self._values.get("spider_cloud_front")
        return typing.cast(typing.Optional["CfnCloudFrontModulePropsResourcesSpiderCloudFront"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFrontModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-cloudfront-module.CfnCloudFrontModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudFrontModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudFrontModulePropsResourcesS3Bucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74a9ea0b6c984ef8c02f5987a097ddd7ab8b27a03f51d5ac6947cc5732e3fccb)
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
        :schema: CfnCloudFrontModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudFrontModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFrontModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-cloudfront-module.CfnCloudFrontModulePropsResourcesS3BucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudFrontModulePropsResourcesS3BucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudFrontModulePropsResourcesS3BucketPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2dfa0ba904bc2ac7711c8415523fe6da42dc040cc5dd264f01cfe525819ccd4)
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
        :schema: CfnCloudFrontModulePropsResourcesS3BucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudFrontModulePropsResourcesS3BucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFrontModulePropsResourcesS3BucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-spider-cloudfront-module.CfnCloudFrontModulePropsResourcesSpiderCloudFront",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudFrontModulePropsResourcesSpiderCloudFront:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudFrontModulePropsResourcesSpiderCloudFront
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d103e3f33cdd53336501265cc47b9fff9e6f2aeb7078e3b1eda140e597baef70)
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
        :schema: CfnCloudFrontModulePropsResourcesSpiderCloudFront#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudFrontModulePropsResourcesSpiderCloudFront#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudFrontModulePropsResourcesSpiderCloudFront(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCloudFrontModule",
    "CfnCloudFrontModuleProps",
    "CfnCloudFrontModulePropsParameters",
    "CfnCloudFrontModulePropsParametersEnvName",
    "CfnCloudFrontModulePropsResources",
    "CfnCloudFrontModulePropsResourcesS3Bucket",
    "CfnCloudFrontModulePropsResourcesS3BucketPolicy",
    "CfnCloudFrontModulePropsResourcesSpiderCloudFront",
]

publication.publish()

def _typecheckingstub__e69d844e0505806b44ef1a2a92cdfa5cddd4565bf2f7acc3dad881c98610c24c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnCloudFrontModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCloudFrontModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6649fdb8e26356a4a2bdd4bb0952e4ca4ecd09d572bd93a281d6f07f94254619(
    *,
    parameters: typing.Optional[typing.Union[CfnCloudFrontModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCloudFrontModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b7f378752dcf00c8e7552ffa4fa532d8bfb9238d4586b5b3738d347ed2f45c(
    *,
    env_name: typing.Optional[typing.Union[CfnCloudFrontModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33910190033a5ce9a0a0fc87ba106f7cfdba98ea36cd3c14129ed04dd7b19f29(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__441649bb9c153466e74389d059867b137682db5f5d2b80f1b043200d1f210b73(
    *,
    s3_bucket: typing.Optional[typing.Union[CfnCloudFrontModulePropsResourcesS3Bucket, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket_policy: typing.Optional[typing.Union[CfnCloudFrontModulePropsResourcesS3BucketPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    spider_cloud_front: typing.Optional[typing.Union[CfnCloudFrontModulePropsResourcesSpiderCloudFront, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74a9ea0b6c984ef8c02f5987a097ddd7ab8b27a03f51d5ac6947cc5732e3fccb(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2dfa0ba904bc2ac7711c8415523fe6da42dc040cc5dd264f01cfe525819ccd4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d103e3f33cdd53336501265cc47b9fff9e6f2aeb7078e3b1eda140e597baef70(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
