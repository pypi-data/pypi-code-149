'''
# freyraim-impactapi-lambdafunction-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::ImpactApi::LambdaFunction::MODULE` v1.2.0.

## Description

Schema for Module Fragment of type FreyrAIM::ImpactApi::LambdaFunction::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::ImpactApi::LambdaFunction::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-ImpactApi-LambdaFunction-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::ImpactApi::LambdaFunction::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-impactapi-lambdafunction-module+v1.2.0).
* Issues related to `FreyrAIM::ImpactApi::LambdaFunction::MODULE` should be reported to the [publisher](undefined).

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


class CfnLambdaFunctionModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModule",
):
    '''A CloudFormation ``FreyrAIM::ImpactApi::LambdaFunction::MODULE``.

    :cloudformationResource: FreyrAIM::ImpactApi::LambdaFunction::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::ImpactApi::LambdaFunction::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f20ab14acfc3d675aeffec2b31df4bd576d72945dc87b2b950fe1e1dfe50ac6f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLambdaFunctionModuleProps(
            parameters=parameters, resources=resources
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnLambdaFunctionModuleProps":
        '''Resource props.'''
        return typing.cast("CfnLambdaFunctionModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnLambdaFunctionModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::ImpactApi::LambdaFunction::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnLambdaFunctionModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnLambdaFunctionModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnLambdaFunctionModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1237c215fe79458a5e439e7ea310d77bfee279185487f9abc5d598c98f2784a1)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnLambdaFunctionModulePropsParameters"]:
        '''
        :schema: CfnLambdaFunctionModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnLambdaFunctionModulePropsResources"]:
        '''
        :schema: CfnLambdaFunctionModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "elb_bucket_name": "elbBucketName",
        "endpoint_name": "endpointName",
        "env_name": "envName",
        "function_name": "functionName",
        "image_digest": "imageDigest",
        "image_name": "imageName",
        "vpc_id": "vpcId",
    },
)
class CfnLambdaFunctionModulePropsParameters:
    def __init__(
        self,
        *,
        elb_bucket_name: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParametersElbBucketName", typing.Dict[builtins.str, typing.Any]]] = None,
        endpoint_name: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParametersEndpointName", typing.Dict[builtins.str, typing.Any]]] = None,
        env_name: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
        function_name: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParametersFunctionName", typing.Dict[builtins.str, typing.Any]]] = None,
        image_digest: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParametersImageDigest", typing.Dict[builtins.str, typing.Any]]] = None,
        image_name: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParametersImageName", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_id: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsParametersVpcId", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_bucket_name: The ELB logs bucket name.
        :param endpoint_name: The endpoint name.
        :param env_name: The environment name.
        :param function_name: The lambda function`s name.
        :param image_digest: The ImageDigest.
        :param image_name: The image`s name.
        :param vpc_id: Vpc-ID.

        :schema: CfnLambdaFunctionModulePropsParameters
        '''
        if isinstance(elb_bucket_name, dict):
            elb_bucket_name = CfnLambdaFunctionModulePropsParametersElbBucketName(**elb_bucket_name)
        if isinstance(endpoint_name, dict):
            endpoint_name = CfnLambdaFunctionModulePropsParametersEndpointName(**endpoint_name)
        if isinstance(env_name, dict):
            env_name = CfnLambdaFunctionModulePropsParametersEnvName(**env_name)
        if isinstance(function_name, dict):
            function_name = CfnLambdaFunctionModulePropsParametersFunctionName(**function_name)
        if isinstance(image_digest, dict):
            image_digest = CfnLambdaFunctionModulePropsParametersImageDigest(**image_digest)
        if isinstance(image_name, dict):
            image_name = CfnLambdaFunctionModulePropsParametersImageName(**image_name)
        if isinstance(vpc_id, dict):
            vpc_id = CfnLambdaFunctionModulePropsParametersVpcId(**vpc_id)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4b615c6cd7f47836a6ed2a0692f358382174a1d8c8ce7da1f6df1d0381aa4da)
            check_type(argname="argument elb_bucket_name", value=elb_bucket_name, expected_type=type_hints["elb_bucket_name"])
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument image_digest", value=image_digest, expected_type=type_hints["image_digest"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if elb_bucket_name is not None:
            self._values["elb_bucket_name"] = elb_bucket_name
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if env_name is not None:
            self._values["env_name"] = env_name
        if function_name is not None:
            self._values["function_name"] = function_name
        if image_digest is not None:
            self._values["image_digest"] = image_digest
        if image_name is not None:
            self._values["image_name"] = image_name
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def elb_bucket_name(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsParametersElbBucketName"]:
        '''The ELB logs bucket name.

        :schema: CfnLambdaFunctionModulePropsParameters#ELBBucketName
        '''
        result = self._values.get("elb_bucket_name")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsParametersElbBucketName"], result)

    @builtins.property
    def endpoint_name(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsParametersEndpointName"]:
        '''The endpoint name.

        :schema: CfnLambdaFunctionModulePropsParameters#EndpointName
        '''
        result = self._values.get("endpoint_name")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsParametersEndpointName"], result)

    @builtins.property
    def env_name(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsParametersEnvName"]:
        '''The environment name.

        :schema: CfnLambdaFunctionModulePropsParameters#EnvName
        '''
        result = self._values.get("env_name")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsParametersEnvName"], result)

    @builtins.property
    def function_name(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsParametersFunctionName"]:
        '''The lambda function`s name.

        :schema: CfnLambdaFunctionModulePropsParameters#FunctionName
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsParametersFunctionName"], result)

    @builtins.property
    def image_digest(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsParametersImageDigest"]:
        '''The ImageDigest.

        :schema: CfnLambdaFunctionModulePropsParameters#ImageDigest
        '''
        result = self._values.get("image_digest")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsParametersImageDigest"], result)

    @builtins.property
    def image_name(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsParametersImageName"]:
        '''The image`s name.

        :schema: CfnLambdaFunctionModulePropsParameters#ImageName
        '''
        result = self._values.get("image_name")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsParametersImageName"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional["CfnLambdaFunctionModulePropsParametersVpcId"]:
        '''Vpc-ID.

        :schema: CfnLambdaFunctionModulePropsParameters#VpcID
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsParametersVpcId"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsParametersElbBucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLambdaFunctionModulePropsParametersElbBucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The ELB logs bucket name.

        :param description: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsParametersElbBucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9c93f0b38d2ea3bff3b1ad5cf6f57cb8dc2f4da65c8b9e7a40d4621601914dc)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersElbBucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersElbBucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsParametersElbBucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsParametersEndpointName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLambdaFunctionModulePropsParametersEndpointName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The endpoint name.

        :param description: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsParametersEndpointName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7304ae2633dacaaace00f7d9184f0d42a8b03374ad67bf57b20e5d13a12bdeaf)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersEndpointName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersEndpointName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsParametersEndpointName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsParametersEnvName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLambdaFunctionModulePropsParametersEnvName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsParametersEnvName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6982856028fd648bc551e8f08c8a3dc2df289ece95ad86e47df56f47d14b5e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersEnvName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersEnvName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsParametersEnvName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsParametersFunctionName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLambdaFunctionModulePropsParametersFunctionName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The lambda function`s name.

        :param description: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsParametersFunctionName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__159b2c1f699019f12bc700ffeeb70c65a76f2198acabdfe89ecb94d236ebe841)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersFunctionName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersFunctionName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsParametersFunctionName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsParametersImageDigest",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLambdaFunctionModulePropsParametersImageDigest:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The ImageDigest.

        :param description: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsParametersImageDigest
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__374730cea82dd17de55592b0539f612e1ef8ab4956a8984d4cebef14ad9ce30f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersImageDigest#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersImageDigest#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsParametersImageDigest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsParametersImageName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLambdaFunctionModulePropsParametersImageName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The image`s name.

        :param description: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsParametersImageName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be954b8163afd0abc83ed2ed02cee40a29baf9ddd63f270553519f25bb203bc7)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersImageName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersImageName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsParametersImageName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsParametersVpcId",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLambdaFunctionModulePropsParametersVpcId:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Vpc-ID.

        :param description: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsParametersVpcId
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dac9eab38f3094a8bf484f678ef7587c9d89dcb1838ea3f7c502ce4c3d570f0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersVpcId#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLambdaFunctionModulePropsParametersVpcId#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsParametersVpcId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "elb_bucket": "elbBucket",
        "elb_bucket_policy": "elbBucketPolicy",
        "impact_api_handle_lambda_function": "impactApiHandleLambdaFunction",
        "impact_classify_ec2_instance": "impactClassifyEc2Instance",
        "lambda_function_create_role": "lambdaFunctionCreateRole",
        "listener1": "listener1",
        "listener2": "listener2",
        "listener3": "listener3",
        "listener_rule1": "listenerRule1",
        "listener_rule2": "listenerRule2",
        "listener_rule3": "listenerRule3",
        "load_balancer1": "loadBalancer1",
        "target_group1": "targetGroup1",
        "target_group2": "targetGroup2",
        "target_group3": "targetGroup3",
    },
)
class CfnLambdaFunctionModulePropsResources:
    def __init__(
        self,
        *,
        elb_bucket: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesElbBucket", typing.Dict[builtins.str, typing.Any]]] = None,
        elb_bucket_policy: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesElbBucketPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        impact_api_handle_lambda_function: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction", typing.Dict[builtins.str, typing.Any]]] = None,
        impact_classify_ec2_instance: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_function_create_role: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole", typing.Dict[builtins.str, typing.Any]]] = None,
        listener1: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesListener1", typing.Dict[builtins.str, typing.Any]]] = None,
        listener2: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesListener2", typing.Dict[builtins.str, typing.Any]]] = None,
        listener3: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesListener3", typing.Dict[builtins.str, typing.Any]]] = None,
        listener_rule1: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesListenerRule1", typing.Dict[builtins.str, typing.Any]]] = None,
        listener_rule2: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesListenerRule2", typing.Dict[builtins.str, typing.Any]]] = None,
        listener_rule3: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesListenerRule3", typing.Dict[builtins.str, typing.Any]]] = None,
        load_balancer1: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesLoadBalancer1", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group1: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesTargetGroup1", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group2: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesTargetGroup2", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group3: typing.Optional[typing.Union["CfnLambdaFunctionModulePropsResourcesTargetGroup3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_bucket: 
        :param elb_bucket_policy: 
        :param impact_api_handle_lambda_function: 
        :param impact_classify_ec2_instance: 
        :param lambda_function_create_role: 
        :param listener1: 
        :param listener2: 
        :param listener3: 
        :param listener_rule1: 
        :param listener_rule2: 
        :param listener_rule3: 
        :param load_balancer1: 
        :param target_group1: 
        :param target_group2: 
        :param target_group3: 

        :schema: CfnLambdaFunctionModulePropsResources
        '''
        if isinstance(elb_bucket, dict):
            elb_bucket = CfnLambdaFunctionModulePropsResourcesElbBucket(**elb_bucket)
        if isinstance(elb_bucket_policy, dict):
            elb_bucket_policy = CfnLambdaFunctionModulePropsResourcesElbBucketPolicy(**elb_bucket_policy)
        if isinstance(impact_api_handle_lambda_function, dict):
            impact_api_handle_lambda_function = CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction(**impact_api_handle_lambda_function)
        if isinstance(impact_classify_ec2_instance, dict):
            impact_classify_ec2_instance = CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance(**impact_classify_ec2_instance)
        if isinstance(lambda_function_create_role, dict):
            lambda_function_create_role = CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole(**lambda_function_create_role)
        if isinstance(listener1, dict):
            listener1 = CfnLambdaFunctionModulePropsResourcesListener1(**listener1)
        if isinstance(listener2, dict):
            listener2 = CfnLambdaFunctionModulePropsResourcesListener2(**listener2)
        if isinstance(listener3, dict):
            listener3 = CfnLambdaFunctionModulePropsResourcesListener3(**listener3)
        if isinstance(listener_rule1, dict):
            listener_rule1 = CfnLambdaFunctionModulePropsResourcesListenerRule1(**listener_rule1)
        if isinstance(listener_rule2, dict):
            listener_rule2 = CfnLambdaFunctionModulePropsResourcesListenerRule2(**listener_rule2)
        if isinstance(listener_rule3, dict):
            listener_rule3 = CfnLambdaFunctionModulePropsResourcesListenerRule3(**listener_rule3)
        if isinstance(load_balancer1, dict):
            load_balancer1 = CfnLambdaFunctionModulePropsResourcesLoadBalancer1(**load_balancer1)
        if isinstance(target_group1, dict):
            target_group1 = CfnLambdaFunctionModulePropsResourcesTargetGroup1(**target_group1)
        if isinstance(target_group2, dict):
            target_group2 = CfnLambdaFunctionModulePropsResourcesTargetGroup2(**target_group2)
        if isinstance(target_group3, dict):
            target_group3 = CfnLambdaFunctionModulePropsResourcesTargetGroup3(**target_group3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4b26ea420948d848edec1ede67c6db51a59f5676dc151e8c313ce6352fa0e4f)
            check_type(argname="argument elb_bucket", value=elb_bucket, expected_type=type_hints["elb_bucket"])
            check_type(argname="argument elb_bucket_policy", value=elb_bucket_policy, expected_type=type_hints["elb_bucket_policy"])
            check_type(argname="argument impact_api_handle_lambda_function", value=impact_api_handle_lambda_function, expected_type=type_hints["impact_api_handle_lambda_function"])
            check_type(argname="argument impact_classify_ec2_instance", value=impact_classify_ec2_instance, expected_type=type_hints["impact_classify_ec2_instance"])
            check_type(argname="argument lambda_function_create_role", value=lambda_function_create_role, expected_type=type_hints["lambda_function_create_role"])
            check_type(argname="argument listener1", value=listener1, expected_type=type_hints["listener1"])
            check_type(argname="argument listener2", value=listener2, expected_type=type_hints["listener2"])
            check_type(argname="argument listener3", value=listener3, expected_type=type_hints["listener3"])
            check_type(argname="argument listener_rule1", value=listener_rule1, expected_type=type_hints["listener_rule1"])
            check_type(argname="argument listener_rule2", value=listener_rule2, expected_type=type_hints["listener_rule2"])
            check_type(argname="argument listener_rule3", value=listener_rule3, expected_type=type_hints["listener_rule3"])
            check_type(argname="argument load_balancer1", value=load_balancer1, expected_type=type_hints["load_balancer1"])
            check_type(argname="argument target_group1", value=target_group1, expected_type=type_hints["target_group1"])
            check_type(argname="argument target_group2", value=target_group2, expected_type=type_hints["target_group2"])
            check_type(argname="argument target_group3", value=target_group3, expected_type=type_hints["target_group3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if elb_bucket is not None:
            self._values["elb_bucket"] = elb_bucket
        if elb_bucket_policy is not None:
            self._values["elb_bucket_policy"] = elb_bucket_policy
        if impact_api_handle_lambda_function is not None:
            self._values["impact_api_handle_lambda_function"] = impact_api_handle_lambda_function
        if impact_classify_ec2_instance is not None:
            self._values["impact_classify_ec2_instance"] = impact_classify_ec2_instance
        if lambda_function_create_role is not None:
            self._values["lambda_function_create_role"] = lambda_function_create_role
        if listener1 is not None:
            self._values["listener1"] = listener1
        if listener2 is not None:
            self._values["listener2"] = listener2
        if listener3 is not None:
            self._values["listener3"] = listener3
        if listener_rule1 is not None:
            self._values["listener_rule1"] = listener_rule1
        if listener_rule2 is not None:
            self._values["listener_rule2"] = listener_rule2
        if listener_rule3 is not None:
            self._values["listener_rule3"] = listener_rule3
        if load_balancer1 is not None:
            self._values["load_balancer1"] = load_balancer1
        if target_group1 is not None:
            self._values["target_group1"] = target_group1
        if target_group2 is not None:
            self._values["target_group2"] = target_group2
        if target_group3 is not None:
            self._values["target_group3"] = target_group3

    @builtins.property
    def elb_bucket(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesElbBucket"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#ELBBucket
        '''
        result = self._values.get("elb_bucket")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesElbBucket"], result)

    @builtins.property
    def elb_bucket_policy(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesElbBucketPolicy"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#ELBBucketPolicy
        '''
        result = self._values.get("elb_bucket_policy")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesElbBucketPolicy"], result)

    @builtins.property
    def impact_api_handle_lambda_function(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#ImpactApiHandleLambdaFunction
        '''
        result = self._values.get("impact_api_handle_lambda_function")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction"], result)

    @builtins.property
    def impact_classify_ec2_instance(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#ImpactClassifyEC2Instance
        '''
        result = self._values.get("impact_classify_ec2_instance")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance"], result)

    @builtins.property
    def lambda_function_create_role(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#LambdaFunctionCreateRole
        '''
        result = self._values.get("lambda_function_create_role")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole"], result)

    @builtins.property
    def listener1(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesListener1"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#Listener1
        '''
        result = self._values.get("listener1")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesListener1"], result)

    @builtins.property
    def listener2(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesListener2"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#Listener2
        '''
        result = self._values.get("listener2")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesListener2"], result)

    @builtins.property
    def listener3(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesListener3"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#Listener3
        '''
        result = self._values.get("listener3")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesListener3"], result)

    @builtins.property
    def listener_rule1(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesListenerRule1"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#ListenerRule1
        '''
        result = self._values.get("listener_rule1")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesListenerRule1"], result)

    @builtins.property
    def listener_rule2(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesListenerRule2"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#ListenerRule2
        '''
        result = self._values.get("listener_rule2")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesListenerRule2"], result)

    @builtins.property
    def listener_rule3(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesListenerRule3"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#ListenerRule3
        '''
        result = self._values.get("listener_rule3")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesListenerRule3"], result)

    @builtins.property
    def load_balancer1(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesLoadBalancer1"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#LoadBalancer1
        '''
        result = self._values.get("load_balancer1")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesLoadBalancer1"], result)

    @builtins.property
    def target_group1(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesTargetGroup1"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#TargetGroup1
        '''
        result = self._values.get("target_group1")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesTargetGroup1"], result)

    @builtins.property
    def target_group2(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesTargetGroup2"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#TargetGroup2
        '''
        result = self._values.get("target_group2")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesTargetGroup2"], result)

    @builtins.property
    def target_group3(
        self,
    ) -> typing.Optional["CfnLambdaFunctionModulePropsResourcesTargetGroup3"]:
        '''
        :schema: CfnLambdaFunctionModulePropsResources#TargetGroup3
        '''
        result = self._values.get("target_group3")
        return typing.cast(typing.Optional["CfnLambdaFunctionModulePropsResourcesTargetGroup3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesElbBucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesElbBucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesElbBucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__356be9abb24d3211e9f0bea5ae25927fb3a49308c563cdf5eb7c8e42d863a81a)
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
        :schema: CfnLambdaFunctionModulePropsResourcesElbBucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesElbBucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesElbBucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesElbBucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesElbBucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesElbBucketPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dacbd6d7c6569e5b27238fed29efd1c9415c78e156c1e5d95399a5c754dca3ff)
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
        :schema: CfnLambdaFunctionModulePropsResourcesElbBucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesElbBucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesElbBucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b5241c3f687ff5584d301d17dacae17c864e4d42fc14825e5a8cabbf64f2634)
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
        :schema: CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f650ddac833f911b7a5a14fce2f87a453b58ff5c31bfd949acacb428d2c7429)
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
        :schema: CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb35551ff3e3736a1101880d2a542116088aca3b6993c69b0417581e9e7dbab)
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
        :schema: CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesListener1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesListener1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesListener1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18b3313673c7ebef6c6cfb173fdd01de7d92ced44d3303049ed9a72fe39a421a)
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
        :schema: CfnLambdaFunctionModulePropsResourcesListener1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesListener1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesListener1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesListener2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesListener2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesListener2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6592a15de949e8630d30f7df48735a7f66ae74b86144aeddbaf18fb477ea4af)
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
        :schema: CfnLambdaFunctionModulePropsResourcesListener2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesListener2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesListener2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesListener3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesListener3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesListener3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94760880429a7725a9418591ddf3a02b80f09dea1a204d53cde2e84a83c0e9d6)
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
        :schema: CfnLambdaFunctionModulePropsResourcesListener3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesListener3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesListener3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesListenerRule1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesListenerRule1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d6f14b64c5171a9b12847dd46ea988bbeb00527d990b78509fd84815f2ee4f)
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
        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesListenerRule1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesListenerRule2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesListenerRule2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3acb2abbdf382729461a5f0b0b085ff0ea0e9aea82faf293910eccd55a04aa58)
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
        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesListenerRule2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesListenerRule3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesListenerRule3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac485ded8764df4034aa0ed44c98b327f095e77d28bcabe647725df05170d33)
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
        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesListenerRule3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesListenerRule3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesLoadBalancer1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesLoadBalancer1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesLoadBalancer1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bbff7f05c621850ac0bc6b6a72b99a39f9f114c985dfe472d426863e532dc05)
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
        :schema: CfnLambdaFunctionModulePropsResourcesLoadBalancer1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesLoadBalancer1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesLoadBalancer1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesTargetGroup1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesTargetGroup1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6986888c79b066d325862a2ed862b99cd0a9dfeb465fd990557b41639f5d75f3)
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
        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesTargetGroup1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesTargetGroup2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesTargetGroup2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b868fc407eb78083c4648cbc262497b65573789c8be673f82c4f18dda8152bcd)
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
        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesTargetGroup2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-lambdafunction-module.CfnLambdaFunctionModulePropsResourcesTargetGroup3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLambdaFunctionModulePropsResourcesTargetGroup3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c5546e7ef61a8aa18d01dac797d8a9a20a91e06421c5482a647d31cc5bb8414)
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
        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLambdaFunctionModulePropsResourcesTargetGroup3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLambdaFunctionModulePropsResourcesTargetGroup3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLambdaFunctionModule",
    "CfnLambdaFunctionModuleProps",
    "CfnLambdaFunctionModulePropsParameters",
    "CfnLambdaFunctionModulePropsParametersElbBucketName",
    "CfnLambdaFunctionModulePropsParametersEndpointName",
    "CfnLambdaFunctionModulePropsParametersEnvName",
    "CfnLambdaFunctionModulePropsParametersFunctionName",
    "CfnLambdaFunctionModulePropsParametersImageDigest",
    "CfnLambdaFunctionModulePropsParametersImageName",
    "CfnLambdaFunctionModulePropsParametersVpcId",
    "CfnLambdaFunctionModulePropsResources",
    "CfnLambdaFunctionModulePropsResourcesElbBucket",
    "CfnLambdaFunctionModulePropsResourcesElbBucketPolicy",
    "CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction",
    "CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance",
    "CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole",
    "CfnLambdaFunctionModulePropsResourcesListener1",
    "CfnLambdaFunctionModulePropsResourcesListener2",
    "CfnLambdaFunctionModulePropsResourcesListener3",
    "CfnLambdaFunctionModulePropsResourcesListenerRule1",
    "CfnLambdaFunctionModulePropsResourcesListenerRule2",
    "CfnLambdaFunctionModulePropsResourcesListenerRule3",
    "CfnLambdaFunctionModulePropsResourcesLoadBalancer1",
    "CfnLambdaFunctionModulePropsResourcesTargetGroup1",
    "CfnLambdaFunctionModulePropsResourcesTargetGroup2",
    "CfnLambdaFunctionModulePropsResourcesTargetGroup3",
]

publication.publish()

def _typecheckingstub__f20ab14acfc3d675aeffec2b31df4bd576d72945dc87b2b950fe1e1dfe50ac6f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1237c215fe79458a5e439e7ea310d77bfee279185487f9abc5d598c98f2784a1(
    *,
    parameters: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b615c6cd7f47836a6ed2a0692f358382174a1d8c8ce7da1f6df1d0381aa4da(
    *,
    elb_bucket_name: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParametersElbBucketName, typing.Dict[builtins.str, typing.Any]]] = None,
    endpoint_name: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParametersEndpointName, typing.Dict[builtins.str, typing.Any]]] = None,
    env_name: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
    function_name: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParametersFunctionName, typing.Dict[builtins.str, typing.Any]]] = None,
    image_digest: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParametersImageDigest, typing.Dict[builtins.str, typing.Any]]] = None,
    image_name: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParametersImageName, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_id: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsParametersVpcId, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9c93f0b38d2ea3bff3b1ad5cf6f57cb8dc2f4da65c8b9e7a40d4621601914dc(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7304ae2633dacaaace00f7d9184f0d42a8b03374ad67bf57b20e5d13a12bdeaf(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6982856028fd648bc551e8f08c8a3dc2df289ece95ad86e47df56f47d14b5e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159b2c1f699019f12bc700ffeeb70c65a76f2198acabdfe89ecb94d236ebe841(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__374730cea82dd17de55592b0539f612e1ef8ab4956a8984d4cebef14ad9ce30f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be954b8163afd0abc83ed2ed02cee40a29baf9ddd63f270553519f25bb203bc7(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dac9eab38f3094a8bf484f678ef7587c9d89dcb1838ea3f7c502ce4c3d570f0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b26ea420948d848edec1ede67c6db51a59f5676dc151e8c313ce6352fa0e4f(
    *,
    elb_bucket: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesElbBucket, typing.Dict[builtins.str, typing.Any]]] = None,
    elb_bucket_policy: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesElbBucketPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    impact_api_handle_lambda_function: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesImpactApiHandleLambdaFunction, typing.Dict[builtins.str, typing.Any]]] = None,
    impact_classify_ec2_instance: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesImpactClassifyEc2Instance, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_function_create_role: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesLambdaFunctionCreateRole, typing.Dict[builtins.str, typing.Any]]] = None,
    listener1: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesListener1, typing.Dict[builtins.str, typing.Any]]] = None,
    listener2: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesListener2, typing.Dict[builtins.str, typing.Any]]] = None,
    listener3: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesListener3, typing.Dict[builtins.str, typing.Any]]] = None,
    listener_rule1: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesListenerRule1, typing.Dict[builtins.str, typing.Any]]] = None,
    listener_rule2: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesListenerRule2, typing.Dict[builtins.str, typing.Any]]] = None,
    listener_rule3: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesListenerRule3, typing.Dict[builtins.str, typing.Any]]] = None,
    load_balancer1: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesLoadBalancer1, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group1: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesTargetGroup1, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group2: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesTargetGroup2, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group3: typing.Optional[typing.Union[CfnLambdaFunctionModulePropsResourcesTargetGroup3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__356be9abb24d3211e9f0bea5ae25927fb3a49308c563cdf5eb7c8e42d863a81a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dacbd6d7c6569e5b27238fed29efd1c9415c78e156c1e5d95399a5c754dca3ff(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5241c3f687ff5584d301d17dacae17c864e4d42fc14825e5a8cabbf64f2634(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f650ddac833f911b7a5a14fce2f87a453b58ff5c31bfd949acacb428d2c7429(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb35551ff3e3736a1101880d2a542116088aca3b6993c69b0417581e9e7dbab(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18b3313673c7ebef6c6cfb173fdd01de7d92ced44d3303049ed9a72fe39a421a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6592a15de949e8630d30f7df48735a7f66ae74b86144aeddbaf18fb477ea4af(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94760880429a7725a9418591ddf3a02b80f09dea1a204d53cde2e84a83c0e9d6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d6f14b64c5171a9b12847dd46ea988bbeb00527d990b78509fd84815f2ee4f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3acb2abbdf382729461a5f0b0b085ff0ea0e9aea82faf293910eccd55a04aa58(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac485ded8764df4034aa0ed44c98b327f095e77d28bcabe647725df05170d33(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bbff7f05c621850ac0bc6b6a72b99a39f9f114c985dfe472d426863e532dc05(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6986888c79b066d325862a2ed862b99cd0a9dfeb465fd990557b41639f5d75f3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b868fc407eb78083c4648cbc262497b65573789c8be673f82c4f18dda8152bcd(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c5546e7ef61a8aa18d01dac797d8a9a20a91e06421c5482a647d31cc5bb8414(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
