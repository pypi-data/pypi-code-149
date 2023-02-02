'''
# freyraim-impactapi-apigateway-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::ImpactApi::ApiGateway::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type FreyrAIM::ImpactApi::ApiGateway::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::ImpactApi::ApiGateway::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-ImpactApi-ApiGateway-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::ImpactApi::ApiGateway::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-impactapi-apigateway-module+v1.0.0).
* Issues related to `FreyrAIM::ImpactApi::ApiGateway::MODULE` should be reported to the [publisher](undefined).

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


class CfnApiGatewayModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModule",
):
    '''A CloudFormation ``FreyrAIM::ImpactApi::ApiGateway::MODULE``.

    :cloudformationResource: FreyrAIM::ImpactApi::ApiGateway::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnApiGatewayModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnApiGatewayModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::ImpactApi::ApiGateway::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ecd21f18442d18918f1c40ff88b214e5644703a4a3f382b1775a6f62a82543c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiGatewayModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnApiGatewayModuleProps":
        '''Resource props.'''
        return typing.cast("CfnApiGatewayModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnApiGatewayModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnApiGatewayModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnApiGatewayModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::ImpactApi::ApiGateway::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnApiGatewayModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnApiGatewayModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnApiGatewayModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__857638919cdf25de4435e37800597cc0da2d4ee6aa3914199912f48b59eceaae)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnApiGatewayModulePropsParameters"]:
        '''
        :schema: CfnApiGatewayModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnApiGatewayModulePropsResources"]:
        '''
        :schema: CfnApiGatewayModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={"env_name": "envName", "function_name": "functionName"},
)
class CfnApiGatewayModulePropsParameters:
    def __init__(
        self,
        *,
        env_name: typing.Optional[typing.Union["CfnApiGatewayModulePropsParametersEnvName", typing.Dict[builtins.str, typing.Any]]] = None,
        function_name: typing.Optional[typing.Union["CfnApiGatewayModulePropsParametersFunctionName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param env_name: The environment name.
        :param function_name: The lambda function`s name.

        :schema: CfnApiGatewayModulePropsParameters
        '''
        if isinstance(env_name, dict):
            env_name = CfnApiGatewayModulePropsParametersEnvName(**env_name)
        if isinstance(function_name, dict):
            function_name = CfnApiGatewayModulePropsParametersFunctionName(**function_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ff3b535f319e77d135541773b29b8f87e5b8ba13082e5d4d77b55c5ed13cc43)
            check_type(argname="argument env_name", value=env_name, expected_type=type_hints["env_name"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if env_name is not None:
            self._values["env_name"] = env_name
        if function_name is not None:
            self._values["function_name"] = function_name

    @builtins.property
    def env_name(self) -> typing.Optional["CfnApiGatewayModulePropsParametersEnvName"]:
        '''The environment name.

        :schema: CfnApiGatewayModulePropsParameters#EnvName
        '''
        result = self._values.get("env_name")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsParametersEnvName"], result)

    @builtins.property
    def function_name(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsParametersFunctionName"]:
        '''The lambda function`s name.

        :schema: CfnApiGatewayModulePropsParameters#FunctionName
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsParametersFunctionName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsParametersEnvName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnApiGatewayModulePropsParametersEnvName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The environment name.

        :param description: 
        :param type: 

        :schema: CfnApiGatewayModulePropsParametersEnvName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0af95ba0e4929c94f0cda30d23265b71d4d3f75be4052b4920ca32cc2fcbd518)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnApiGatewayModulePropsParametersEnvName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnApiGatewayModulePropsParametersEnvName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsParametersEnvName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsParametersFunctionName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnApiGatewayModulePropsParametersFunctionName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The lambda function`s name.

        :param description: 
        :param type: 

        :schema: CfnApiGatewayModulePropsParametersFunctionName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30f7de159e4310f8a5238bb7ef9bab8c2b58dfe6c98b10230e6de3efe3a20167)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnApiGatewayModulePropsParametersFunctionName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnApiGatewayModulePropsParametersFunctionName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsParametersFunctionName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "api_gateway_cloud_watch_logs_account": "apiGatewayCloudWatchLogsAccount",
        "api_gateway_cloud_watch_logs_role": "apiGatewayCloudWatchLogsRole",
        "classifier_resource": "classifierResource",
        "deployment_doc_content_post": "deploymentDocContentPost",
        "doc_content_post_method": "docContentPostMethod",
        "doc_content_resource": "docContentResource",
        "impact_api": "impactApi",
        "lambda_permission": "lambdaPermission",
    },
)
class CfnApiGatewayModulePropsResources:
    def __init__(
        self,
        *,
        api_gateway_cloud_watch_logs_account: typing.Optional[typing.Union["CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        api_gateway_cloud_watch_logs_role: typing.Optional[typing.Union["CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole", typing.Dict[builtins.str, typing.Any]]] = None,
        classifier_resource: typing.Optional[typing.Union["CfnApiGatewayModulePropsResourcesClassifierResource", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_doc_content_post: typing.Optional[typing.Union["CfnApiGatewayModulePropsResourcesDeploymentDocContentPost", typing.Dict[builtins.str, typing.Any]]] = None,
        doc_content_post_method: typing.Optional[typing.Union["CfnApiGatewayModulePropsResourcesDocContentPostMethod", typing.Dict[builtins.str, typing.Any]]] = None,
        doc_content_resource: typing.Optional[typing.Union["CfnApiGatewayModulePropsResourcesDocContentResource", typing.Dict[builtins.str, typing.Any]]] = None,
        impact_api: typing.Optional[typing.Union["CfnApiGatewayModulePropsResourcesImpactApi", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_permission: typing.Optional[typing.Union["CfnApiGatewayModulePropsResourcesLambdaPermission", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param api_gateway_cloud_watch_logs_account: 
        :param api_gateway_cloud_watch_logs_role: 
        :param classifier_resource: 
        :param deployment_doc_content_post: 
        :param doc_content_post_method: 
        :param doc_content_resource: 
        :param impact_api: 
        :param lambda_permission: 

        :schema: CfnApiGatewayModulePropsResources
        '''
        if isinstance(api_gateway_cloud_watch_logs_account, dict):
            api_gateway_cloud_watch_logs_account = CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount(**api_gateway_cloud_watch_logs_account)
        if isinstance(api_gateway_cloud_watch_logs_role, dict):
            api_gateway_cloud_watch_logs_role = CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole(**api_gateway_cloud_watch_logs_role)
        if isinstance(classifier_resource, dict):
            classifier_resource = CfnApiGatewayModulePropsResourcesClassifierResource(**classifier_resource)
        if isinstance(deployment_doc_content_post, dict):
            deployment_doc_content_post = CfnApiGatewayModulePropsResourcesDeploymentDocContentPost(**deployment_doc_content_post)
        if isinstance(doc_content_post_method, dict):
            doc_content_post_method = CfnApiGatewayModulePropsResourcesDocContentPostMethod(**doc_content_post_method)
        if isinstance(doc_content_resource, dict):
            doc_content_resource = CfnApiGatewayModulePropsResourcesDocContentResource(**doc_content_resource)
        if isinstance(impact_api, dict):
            impact_api = CfnApiGatewayModulePropsResourcesImpactApi(**impact_api)
        if isinstance(lambda_permission, dict):
            lambda_permission = CfnApiGatewayModulePropsResourcesLambdaPermission(**lambda_permission)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52ca297fde4a8a8abfd71a68bdcd558c0053f61b5d38733cf71c4755edc5c219)
            check_type(argname="argument api_gateway_cloud_watch_logs_account", value=api_gateway_cloud_watch_logs_account, expected_type=type_hints["api_gateway_cloud_watch_logs_account"])
            check_type(argname="argument api_gateway_cloud_watch_logs_role", value=api_gateway_cloud_watch_logs_role, expected_type=type_hints["api_gateway_cloud_watch_logs_role"])
            check_type(argname="argument classifier_resource", value=classifier_resource, expected_type=type_hints["classifier_resource"])
            check_type(argname="argument deployment_doc_content_post", value=deployment_doc_content_post, expected_type=type_hints["deployment_doc_content_post"])
            check_type(argname="argument doc_content_post_method", value=doc_content_post_method, expected_type=type_hints["doc_content_post_method"])
            check_type(argname="argument doc_content_resource", value=doc_content_resource, expected_type=type_hints["doc_content_resource"])
            check_type(argname="argument impact_api", value=impact_api, expected_type=type_hints["impact_api"])
            check_type(argname="argument lambda_permission", value=lambda_permission, expected_type=type_hints["lambda_permission"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_gateway_cloud_watch_logs_account is not None:
            self._values["api_gateway_cloud_watch_logs_account"] = api_gateway_cloud_watch_logs_account
        if api_gateway_cloud_watch_logs_role is not None:
            self._values["api_gateway_cloud_watch_logs_role"] = api_gateway_cloud_watch_logs_role
        if classifier_resource is not None:
            self._values["classifier_resource"] = classifier_resource
        if deployment_doc_content_post is not None:
            self._values["deployment_doc_content_post"] = deployment_doc_content_post
        if doc_content_post_method is not None:
            self._values["doc_content_post_method"] = doc_content_post_method
        if doc_content_resource is not None:
            self._values["doc_content_resource"] = doc_content_resource
        if impact_api is not None:
            self._values["impact_api"] = impact_api
        if lambda_permission is not None:
            self._values["lambda_permission"] = lambda_permission

    @builtins.property
    def api_gateway_cloud_watch_logs_account(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount"]:
        '''
        :schema: CfnApiGatewayModulePropsResources#ApiGatewayCloudWatchLogsAccount
        '''
        result = self._values.get("api_gateway_cloud_watch_logs_account")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount"], result)

    @builtins.property
    def api_gateway_cloud_watch_logs_role(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole"]:
        '''
        :schema: CfnApiGatewayModulePropsResources#ApiGatewayCloudWatchLogsRole
        '''
        result = self._values.get("api_gateway_cloud_watch_logs_role")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole"], result)

    @builtins.property
    def classifier_resource(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsResourcesClassifierResource"]:
        '''
        :schema: CfnApiGatewayModulePropsResources#ClassifierResource
        '''
        result = self._values.get("classifier_resource")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResourcesClassifierResource"], result)

    @builtins.property
    def deployment_doc_content_post(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsResourcesDeploymentDocContentPost"]:
        '''
        :schema: CfnApiGatewayModulePropsResources#DeploymentDocContentPost
        '''
        result = self._values.get("deployment_doc_content_post")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResourcesDeploymentDocContentPost"], result)

    @builtins.property
    def doc_content_post_method(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsResourcesDocContentPostMethod"]:
        '''
        :schema: CfnApiGatewayModulePropsResources#DocContentPostMethod
        '''
        result = self._values.get("doc_content_post_method")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResourcesDocContentPostMethod"], result)

    @builtins.property
    def doc_content_resource(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsResourcesDocContentResource"]:
        '''
        :schema: CfnApiGatewayModulePropsResources#DocContentResource
        '''
        result = self._values.get("doc_content_resource")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResourcesDocContentResource"], result)

    @builtins.property
    def impact_api(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsResourcesImpactApi"]:
        '''
        :schema: CfnApiGatewayModulePropsResources#ImpactApi
        '''
        result = self._values.get("impact_api")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResourcesImpactApi"], result)

    @builtins.property
    def lambda_permission(
        self,
    ) -> typing.Optional["CfnApiGatewayModulePropsResourcesLambdaPermission"]:
        '''
        :schema: CfnApiGatewayModulePropsResources#LambdaPermission
        '''
        result = self._values.get("lambda_permission")
        return typing.cast(typing.Optional["CfnApiGatewayModulePropsResourcesLambdaPermission"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7e7d8d00be7d1f1f7ccd221c7d2a05fda4bd062411b35ad57d4c100e093dc1a)
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
        :schema: CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79786ecb52d8c64defc38dbf4c0eac2b2e528e00e92a429d29e1be51cb701dbf)
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
        :schema: CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResourcesClassifierResource",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiGatewayModulePropsResourcesClassifierResource:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiGatewayModulePropsResourcesClassifierResource
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0db0dd8cf62190c3882973b433c8e0b2eda49223b7b70b970ea7557a0badabad)
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
        :schema: CfnApiGatewayModulePropsResourcesClassifierResource#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiGatewayModulePropsResourcesClassifierResource#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResourcesClassifierResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResourcesDeploymentDocContentPost",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiGatewayModulePropsResourcesDeploymentDocContentPost:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiGatewayModulePropsResourcesDeploymentDocContentPost
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77a1e149abc8923ce8daca1b23fbf668585c288180fa7f8b536eb78ef276a67a)
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
        :schema: CfnApiGatewayModulePropsResourcesDeploymentDocContentPost#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiGatewayModulePropsResourcesDeploymentDocContentPost#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResourcesDeploymentDocContentPost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResourcesDocContentPostMethod",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiGatewayModulePropsResourcesDocContentPostMethod:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiGatewayModulePropsResourcesDocContentPostMethod
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de296a7b87e55164d6c526c186da9f6a048c1349eb714e15b76eec0ed37c7cfa)
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
        :schema: CfnApiGatewayModulePropsResourcesDocContentPostMethod#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiGatewayModulePropsResourcesDocContentPostMethod#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResourcesDocContentPostMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResourcesDocContentResource",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiGatewayModulePropsResourcesDocContentResource:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiGatewayModulePropsResourcesDocContentResource
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b51840f861bc5cfa402763ccd65d44b257a990a126f7097cd0273510624173db)
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
        :schema: CfnApiGatewayModulePropsResourcesDocContentResource#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiGatewayModulePropsResourcesDocContentResource#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResourcesDocContentResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResourcesImpactApi",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiGatewayModulePropsResourcesImpactApi:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiGatewayModulePropsResourcesImpactApi
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e746a8cabb32de51067a5f97b38f37ae4f79b7fb3da437ed8e8efcf5544bffd3)
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
        :schema: CfnApiGatewayModulePropsResourcesImpactApi#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiGatewayModulePropsResourcesImpactApi#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResourcesImpactApi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apigateway-module.CfnApiGatewayModulePropsResourcesLambdaPermission",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiGatewayModulePropsResourcesLambdaPermission:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiGatewayModulePropsResourcesLambdaPermission
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4d07177b2867b1297bc0002ed6a031f9e1bcfa07091625fc05615882ac8c8b2)
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
        :schema: CfnApiGatewayModulePropsResourcesLambdaPermission#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiGatewayModulePropsResourcesLambdaPermission#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayModulePropsResourcesLambdaPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApiGatewayModule",
    "CfnApiGatewayModuleProps",
    "CfnApiGatewayModulePropsParameters",
    "CfnApiGatewayModulePropsParametersEnvName",
    "CfnApiGatewayModulePropsParametersFunctionName",
    "CfnApiGatewayModulePropsResources",
    "CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount",
    "CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole",
    "CfnApiGatewayModulePropsResourcesClassifierResource",
    "CfnApiGatewayModulePropsResourcesDeploymentDocContentPost",
    "CfnApiGatewayModulePropsResourcesDocContentPostMethod",
    "CfnApiGatewayModulePropsResourcesDocContentResource",
    "CfnApiGatewayModulePropsResourcesImpactApi",
    "CfnApiGatewayModulePropsResourcesLambdaPermission",
]

publication.publish()

def _typecheckingstub__9ecd21f18442d18918f1c40ff88b214e5644703a4a3f382b1775a6f62a82543c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnApiGatewayModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnApiGatewayModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__857638919cdf25de4435e37800597cc0da2d4ee6aa3914199912f48b59eceaae(
    *,
    parameters: typing.Optional[typing.Union[CfnApiGatewayModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnApiGatewayModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ff3b535f319e77d135541773b29b8f87e5b8ba13082e5d4d77b55c5ed13cc43(
    *,
    env_name: typing.Optional[typing.Union[CfnApiGatewayModulePropsParametersEnvName, typing.Dict[builtins.str, typing.Any]]] = None,
    function_name: typing.Optional[typing.Union[CfnApiGatewayModulePropsParametersFunctionName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0af95ba0e4929c94f0cda30d23265b71d4d3f75be4052b4920ca32cc2fcbd518(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f7de159e4310f8a5238bb7ef9bab8c2b58dfe6c98b10230e6de3efe3a20167(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52ca297fde4a8a8abfd71a68bdcd558c0053f61b5d38733cf71c4755edc5c219(
    *,
    api_gateway_cloud_watch_logs_account: typing.Optional[typing.Union[CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    api_gateway_cloud_watch_logs_role: typing.Optional[typing.Union[CfnApiGatewayModulePropsResourcesApiGatewayCloudWatchLogsRole, typing.Dict[builtins.str, typing.Any]]] = None,
    classifier_resource: typing.Optional[typing.Union[CfnApiGatewayModulePropsResourcesClassifierResource, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_doc_content_post: typing.Optional[typing.Union[CfnApiGatewayModulePropsResourcesDeploymentDocContentPost, typing.Dict[builtins.str, typing.Any]]] = None,
    doc_content_post_method: typing.Optional[typing.Union[CfnApiGatewayModulePropsResourcesDocContentPostMethod, typing.Dict[builtins.str, typing.Any]]] = None,
    doc_content_resource: typing.Optional[typing.Union[CfnApiGatewayModulePropsResourcesDocContentResource, typing.Dict[builtins.str, typing.Any]]] = None,
    impact_api: typing.Optional[typing.Union[CfnApiGatewayModulePropsResourcesImpactApi, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_permission: typing.Optional[typing.Union[CfnApiGatewayModulePropsResourcesLambdaPermission, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e7d8d00be7d1f1f7ccd221c7d2a05fda4bd062411b35ad57d4c100e093dc1a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79786ecb52d8c64defc38dbf4c0eac2b2e528e00e92a429d29e1be51cb701dbf(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0db0dd8cf62190c3882973b433c8e0b2eda49223b7b70b970ea7557a0badabad(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77a1e149abc8923ce8daca1b23fbf668585c288180fa7f8b536eb78ef276a67a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de296a7b87e55164d6c526c186da9f6a048c1349eb714e15b76eec0ed37c7cfa(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51840f861bc5cfa402763ccd65d44b257a990a126f7097cd0273510624173db(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e746a8cabb32de51067a5f97b38f37ae4f79b7fb3da437ed8e8efcf5544bffd3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d07177b2867b1297bc0002ed6a031f9e1bcfa07091625fc05615882ac8c8b2(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
