'''
# freyraim-impactapi-apihandle-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `FreyrAIM::ImpactApi::ApiHandle::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type FreyrAIM::ImpactApi::ApiHandle::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name FreyrAIM::ImpactApi::ApiHandle::MODULE \
  --publisher-id 1f3a049eb4a792395c6609688da1c941f63d5698 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/1f3a049eb4a792395c6609688da1c941f63d5698/FreyrAIM-ImpactApi-ApiHandle-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `FreyrAIM::ImpactApi::ApiHandle::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ffreyraim-impactapi-apihandle-module+v1.0.0).
* Issues related to `FreyrAIM::ImpactApi::ApiHandle::MODULE` should be reported to the [publisher](undefined).

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


class CfnApiHandleModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModule",
):
    '''A CloudFormation ``FreyrAIM::ImpactApi::ApiHandle::MODULE``.

    :cloudformationResource: FreyrAIM::ImpactApi::ApiHandle::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnApiHandleModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnApiHandleModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``FreyrAIM::ImpactApi::ApiHandle::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33b0f31a43f7c36af2d7abafabe99a5a23905f53223cafffacd7f12dbf5578c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiHandleModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnApiHandleModuleProps":
        '''Resource props.'''
        return typing.cast("CfnApiHandleModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnApiHandleModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnApiHandleModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnApiHandleModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type FreyrAIM::ImpactApi::ApiHandle::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnApiHandleModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnApiHandleModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnApiHandleModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8688ad30268eb6ef245745337f73ab957bc456276697ca4159b8a0173d21e947)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnApiHandleModulePropsParameters"]:
        '''
        :schema: CfnApiHandleModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnApiHandleModulePropsResources"]:
        '''
        :schema: CfnApiHandleModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_name": "endpointName",
        "function_name": "functionName",
        "image_uri": "imageUri",
        "similarity_url": "similarityUrl",
    },
)
class CfnApiHandleModulePropsParameters:
    def __init__(
        self,
        *,
        endpoint_name: typing.Optional[typing.Union["CfnApiHandleModulePropsParametersEndpointName", typing.Dict[builtins.str, typing.Any]]] = None,
        function_name: typing.Optional[typing.Union["CfnApiHandleModulePropsParametersFunctionName", typing.Dict[builtins.str, typing.Any]]] = None,
        image_uri: typing.Optional[typing.Union["CfnApiHandleModulePropsParametersImageUri", typing.Dict[builtins.str, typing.Any]]] = None,
        similarity_url: typing.Optional[typing.Union["CfnApiHandleModulePropsParametersSimilarityUrl", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param endpoint_name: The endpoint name.
        :param function_name: The lambda function`s name.
        :param image_uri: The lambda function`s Image URI.
        :param similarity_url: The similarity url.

        :schema: CfnApiHandleModulePropsParameters
        '''
        if isinstance(endpoint_name, dict):
            endpoint_name = CfnApiHandleModulePropsParametersEndpointName(**endpoint_name)
        if isinstance(function_name, dict):
            function_name = CfnApiHandleModulePropsParametersFunctionName(**function_name)
        if isinstance(image_uri, dict):
            image_uri = CfnApiHandleModulePropsParametersImageUri(**image_uri)
        if isinstance(similarity_url, dict):
            similarity_url = CfnApiHandleModulePropsParametersSimilarityUrl(**similarity_url)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5c850fd1c11065722aa795f30fd59d95d4d6bdb14f20920345110b3e66f0d66)
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            check_type(argname="argument similarity_url", value=similarity_url, expected_type=type_hints["similarity_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if function_name is not None:
            self._values["function_name"] = function_name
        if image_uri is not None:
            self._values["image_uri"] = image_uri
        if similarity_url is not None:
            self._values["similarity_url"] = similarity_url

    @builtins.property
    def endpoint_name(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsParametersEndpointName"]:
        '''The endpoint name.

        :schema: CfnApiHandleModulePropsParameters#EndpointName
        '''
        result = self._values.get("endpoint_name")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsParametersEndpointName"], result)

    @builtins.property
    def function_name(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsParametersFunctionName"]:
        '''The lambda function`s name.

        :schema: CfnApiHandleModulePropsParameters#FunctionName
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsParametersFunctionName"], result)

    @builtins.property
    def image_uri(self) -> typing.Optional["CfnApiHandleModulePropsParametersImageUri"]:
        '''The lambda function`s Image URI.

        :schema: CfnApiHandleModulePropsParameters#ImageUri
        '''
        result = self._values.get("image_uri")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsParametersImageUri"], result)

    @builtins.property
    def similarity_url(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsParametersSimilarityUrl"]:
        '''The similarity url.

        :schema: CfnApiHandleModulePropsParameters#SimilarityUrl
        '''
        result = self._values.get("similarity_url")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsParametersSimilarityUrl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsParametersEndpointName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnApiHandleModulePropsParametersEndpointName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The endpoint name.

        :param description: 
        :param type: 

        :schema: CfnApiHandleModulePropsParametersEndpointName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2d11219db43d3569c64ea33f14b9d79a00a9312325cee3643dbc15e930da04b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnApiHandleModulePropsParametersEndpointName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnApiHandleModulePropsParametersEndpointName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsParametersEndpointName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsParametersFunctionName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnApiHandleModulePropsParametersFunctionName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The lambda function`s name.

        :param description: 
        :param type: 

        :schema: CfnApiHandleModulePropsParametersFunctionName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96a9332a554d442cb12965b139411c1da26fb69a4e05b70761df4ea313b38498)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnApiHandleModulePropsParametersFunctionName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnApiHandleModulePropsParametersFunctionName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsParametersFunctionName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsParametersImageUri",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnApiHandleModulePropsParametersImageUri:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The lambda function`s Image URI.

        :param description: 
        :param type: 

        :schema: CfnApiHandleModulePropsParametersImageUri
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23947d112031669e68ff4e449f84219cdd5ff2fd4c93b9f84af89f7f41c32083)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnApiHandleModulePropsParametersImageUri#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnApiHandleModulePropsParametersImageUri#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsParametersImageUri(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsParametersSimilarityUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnApiHandleModulePropsParametersSimilarityUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The similarity url.

        :param description: 
        :param type: 

        :schema: CfnApiHandleModulePropsParametersSimilarityUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1840fb4b877acd8b231981e4926a50acf0bfff87b83a621cf6172fa1ffd5cc13)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnApiHandleModulePropsParametersSimilarityUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnApiHandleModulePropsParametersSimilarityUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsParametersSimilarityUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "api_gateway_cloud_watch_logs_account": "apiGatewayCloudWatchLogsAccount",
        "api_gateway_cloud_watch_logs_role": "apiGatewayCloudWatchLogsRole",
        "classifier_resource": "classifierResource",
        "deployment_doc_content_post": "deploymentDocContentPost",
        "doc_content_post_method": "docContentPostMethod",
        "doc_content_resource": "docContentResource",
        "impact_api": "impactApi",
        "impact_api_handle_lambda_function": "impactApiHandleLambdaFunction",
        "lambda_function_create_role": "lambdaFunctionCreateRole",
        "lambda_permission": "lambdaPermission",
    },
)
class CfnApiHandleModulePropsResources:
    def __init__(
        self,
        *,
        api_gateway_cloud_watch_logs_account: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        api_gateway_cloud_watch_logs_role: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole", typing.Dict[builtins.str, typing.Any]]] = None,
        classifier_resource: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesClassifierResource", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_doc_content_post: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesDeploymentDocContentPost", typing.Dict[builtins.str, typing.Any]]] = None,
        doc_content_post_method: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesDocContentPostMethod", typing.Dict[builtins.str, typing.Any]]] = None,
        doc_content_resource: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesDocContentResource", typing.Dict[builtins.str, typing.Any]]] = None,
        impact_api: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesImpactApi", typing.Dict[builtins.str, typing.Any]]] = None,
        impact_api_handle_lambda_function: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_function_create_role: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_permission: typing.Optional[typing.Union["CfnApiHandleModulePropsResourcesLambdaPermission", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param api_gateway_cloud_watch_logs_account: 
        :param api_gateway_cloud_watch_logs_role: 
        :param classifier_resource: 
        :param deployment_doc_content_post: 
        :param doc_content_post_method: 
        :param doc_content_resource: 
        :param impact_api: 
        :param impact_api_handle_lambda_function: 
        :param lambda_function_create_role: 
        :param lambda_permission: 

        :schema: CfnApiHandleModulePropsResources
        '''
        if isinstance(api_gateway_cloud_watch_logs_account, dict):
            api_gateway_cloud_watch_logs_account = CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount(**api_gateway_cloud_watch_logs_account)
        if isinstance(api_gateway_cloud_watch_logs_role, dict):
            api_gateway_cloud_watch_logs_role = CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole(**api_gateway_cloud_watch_logs_role)
        if isinstance(classifier_resource, dict):
            classifier_resource = CfnApiHandleModulePropsResourcesClassifierResource(**classifier_resource)
        if isinstance(deployment_doc_content_post, dict):
            deployment_doc_content_post = CfnApiHandleModulePropsResourcesDeploymentDocContentPost(**deployment_doc_content_post)
        if isinstance(doc_content_post_method, dict):
            doc_content_post_method = CfnApiHandleModulePropsResourcesDocContentPostMethod(**doc_content_post_method)
        if isinstance(doc_content_resource, dict):
            doc_content_resource = CfnApiHandleModulePropsResourcesDocContentResource(**doc_content_resource)
        if isinstance(impact_api, dict):
            impact_api = CfnApiHandleModulePropsResourcesImpactApi(**impact_api)
        if isinstance(impact_api_handle_lambda_function, dict):
            impact_api_handle_lambda_function = CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction(**impact_api_handle_lambda_function)
        if isinstance(lambda_function_create_role, dict):
            lambda_function_create_role = CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole(**lambda_function_create_role)
        if isinstance(lambda_permission, dict):
            lambda_permission = CfnApiHandleModulePropsResourcesLambdaPermission(**lambda_permission)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0612911254d065beb91e02d21508271141a2a91af14b41200733bb0ad8450f6)
            check_type(argname="argument api_gateway_cloud_watch_logs_account", value=api_gateway_cloud_watch_logs_account, expected_type=type_hints["api_gateway_cloud_watch_logs_account"])
            check_type(argname="argument api_gateway_cloud_watch_logs_role", value=api_gateway_cloud_watch_logs_role, expected_type=type_hints["api_gateway_cloud_watch_logs_role"])
            check_type(argname="argument classifier_resource", value=classifier_resource, expected_type=type_hints["classifier_resource"])
            check_type(argname="argument deployment_doc_content_post", value=deployment_doc_content_post, expected_type=type_hints["deployment_doc_content_post"])
            check_type(argname="argument doc_content_post_method", value=doc_content_post_method, expected_type=type_hints["doc_content_post_method"])
            check_type(argname="argument doc_content_resource", value=doc_content_resource, expected_type=type_hints["doc_content_resource"])
            check_type(argname="argument impact_api", value=impact_api, expected_type=type_hints["impact_api"])
            check_type(argname="argument impact_api_handle_lambda_function", value=impact_api_handle_lambda_function, expected_type=type_hints["impact_api_handle_lambda_function"])
            check_type(argname="argument lambda_function_create_role", value=lambda_function_create_role, expected_type=type_hints["lambda_function_create_role"])
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
        if impact_api_handle_lambda_function is not None:
            self._values["impact_api_handle_lambda_function"] = impact_api_handle_lambda_function
        if lambda_function_create_role is not None:
            self._values["lambda_function_create_role"] = lambda_function_create_role
        if lambda_permission is not None:
            self._values["lambda_permission"] = lambda_permission

    @builtins.property
    def api_gateway_cloud_watch_logs_account(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount"]:
        '''
        :schema: CfnApiHandleModulePropsResources#ApiGatewayCloudWatchLogsAccount
        '''
        result = self._values.get("api_gateway_cloud_watch_logs_account")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount"], result)

    @builtins.property
    def api_gateway_cloud_watch_logs_role(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole"]:
        '''
        :schema: CfnApiHandleModulePropsResources#ApiGatewayCloudWatchLogsRole
        '''
        result = self._values.get("api_gateway_cloud_watch_logs_role")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole"], result)

    @builtins.property
    def classifier_resource(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesClassifierResource"]:
        '''
        :schema: CfnApiHandleModulePropsResources#ClassifierResource
        '''
        result = self._values.get("classifier_resource")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesClassifierResource"], result)

    @builtins.property
    def deployment_doc_content_post(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesDeploymentDocContentPost"]:
        '''
        :schema: CfnApiHandleModulePropsResources#DeploymentDocContentPost
        '''
        result = self._values.get("deployment_doc_content_post")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesDeploymentDocContentPost"], result)

    @builtins.property
    def doc_content_post_method(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesDocContentPostMethod"]:
        '''
        :schema: CfnApiHandleModulePropsResources#DocContentPostMethod
        '''
        result = self._values.get("doc_content_post_method")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesDocContentPostMethod"], result)

    @builtins.property
    def doc_content_resource(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesDocContentResource"]:
        '''
        :schema: CfnApiHandleModulePropsResources#DocContentResource
        '''
        result = self._values.get("doc_content_resource")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesDocContentResource"], result)

    @builtins.property
    def impact_api(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesImpactApi"]:
        '''
        :schema: CfnApiHandleModulePropsResources#ImpactApi
        '''
        result = self._values.get("impact_api")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesImpactApi"], result)

    @builtins.property
    def impact_api_handle_lambda_function(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction"]:
        '''
        :schema: CfnApiHandleModulePropsResources#ImpactApiHandleLambdaFunction
        '''
        result = self._values.get("impact_api_handle_lambda_function")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction"], result)

    @builtins.property
    def lambda_function_create_role(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole"]:
        '''
        :schema: CfnApiHandleModulePropsResources#LambdaFunctionCreateRole
        '''
        result = self._values.get("lambda_function_create_role")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole"], result)

    @builtins.property
    def lambda_permission(
        self,
    ) -> typing.Optional["CfnApiHandleModulePropsResourcesLambdaPermission"]:
        '''
        :schema: CfnApiHandleModulePropsResources#LambdaPermission
        '''
        result = self._values.get("lambda_permission")
        return typing.cast(typing.Optional["CfnApiHandleModulePropsResourcesLambdaPermission"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__855c7d79586203faf8deb9026ee4afe636ef21611e721e62ec2ffb751bbc0979)
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
        :schema: CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ae171034654512d35f8155b7dd856e373a6b457d16650c7dc9a2400a684adbd)
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
        :schema: CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesClassifierResource",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesClassifierResource:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesClassifierResource
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d421dd9f0d31b178f07d207f5c566139c1f2306247601afeb7848b33280586ed)
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
        :schema: CfnApiHandleModulePropsResourcesClassifierResource#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesClassifierResource#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesClassifierResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesDeploymentDocContentPost",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesDeploymentDocContentPost:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesDeploymentDocContentPost
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d86751ddd66ad3423d84018ce44c77448a5a6b0396fa4cbe00d45611ab1e10a)
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
        :schema: CfnApiHandleModulePropsResourcesDeploymentDocContentPost#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesDeploymentDocContentPost#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesDeploymentDocContentPost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesDocContentPostMethod",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesDocContentPostMethod:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesDocContentPostMethod
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a61ebfca25b3ef1833ab4d0bce71350c5aaaf02100b3d734efc334c9954cdca)
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
        :schema: CfnApiHandleModulePropsResourcesDocContentPostMethod#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesDocContentPostMethod#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesDocContentPostMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesDocContentResource",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesDocContentResource:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesDocContentResource
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6e96a0295d99768b1a790f5adc61f3af45377f0f596d8a24e8b82f4b1ed5b4d)
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
        :schema: CfnApiHandleModulePropsResourcesDocContentResource#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesDocContentResource#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesDocContentResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesImpactApi",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesImpactApi:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesImpactApi
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03f486c14e7141162bd9349793a730e1ca1d15412c3b3aee8d3fde0a9d96dac1)
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
        :schema: CfnApiHandleModulePropsResourcesImpactApi#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesImpactApi#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesImpactApi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e91852e11642fb993231a63c6fe7d191b9d86abf5ff4d32ee930334fba4d61f)
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
        :schema: CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7f4794f0f75aa47d373fa7aca7caafbcda560a8714157aa53a813219413c5ab)
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
        :schema: CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/freyraim-impactapi-apihandle-module.CfnApiHandleModulePropsResourcesLambdaPermission",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnApiHandleModulePropsResourcesLambdaPermission:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnApiHandleModulePropsResourcesLambdaPermission
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f639547fd57fee41a4578e8d8595ec348af40a4cc8b652af254b0474f18495fc)
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
        :schema: CfnApiHandleModulePropsResourcesLambdaPermission#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnApiHandleModulePropsResourcesLambdaPermission#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiHandleModulePropsResourcesLambdaPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApiHandleModule",
    "CfnApiHandleModuleProps",
    "CfnApiHandleModulePropsParameters",
    "CfnApiHandleModulePropsParametersEndpointName",
    "CfnApiHandleModulePropsParametersFunctionName",
    "CfnApiHandleModulePropsParametersImageUri",
    "CfnApiHandleModulePropsParametersSimilarityUrl",
    "CfnApiHandleModulePropsResources",
    "CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount",
    "CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole",
    "CfnApiHandleModulePropsResourcesClassifierResource",
    "CfnApiHandleModulePropsResourcesDeploymentDocContentPost",
    "CfnApiHandleModulePropsResourcesDocContentPostMethod",
    "CfnApiHandleModulePropsResourcesDocContentResource",
    "CfnApiHandleModulePropsResourcesImpactApi",
    "CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction",
    "CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole",
    "CfnApiHandleModulePropsResourcesLambdaPermission",
]

publication.publish()

def _typecheckingstub__33b0f31a43f7c36af2d7abafabe99a5a23905f53223cafffacd7f12dbf5578c7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnApiHandleModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnApiHandleModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8688ad30268eb6ef245745337f73ab957bc456276697ca4159b8a0173d21e947(
    *,
    parameters: typing.Optional[typing.Union[CfnApiHandleModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnApiHandleModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c850fd1c11065722aa795f30fd59d95d4d6bdb14f20920345110b3e66f0d66(
    *,
    endpoint_name: typing.Optional[typing.Union[CfnApiHandleModulePropsParametersEndpointName, typing.Dict[builtins.str, typing.Any]]] = None,
    function_name: typing.Optional[typing.Union[CfnApiHandleModulePropsParametersFunctionName, typing.Dict[builtins.str, typing.Any]]] = None,
    image_uri: typing.Optional[typing.Union[CfnApiHandleModulePropsParametersImageUri, typing.Dict[builtins.str, typing.Any]]] = None,
    similarity_url: typing.Optional[typing.Union[CfnApiHandleModulePropsParametersSimilarityUrl, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2d11219db43d3569c64ea33f14b9d79a00a9312325cee3643dbc15e930da04b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96a9332a554d442cb12965b139411c1da26fb69a4e05b70761df4ea313b38498(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23947d112031669e68ff4e449f84219cdd5ff2fd4c93b9f84af89f7f41c32083(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1840fb4b877acd8b231981e4926a50acf0bfff87b83a621cf6172fa1ffd5cc13(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0612911254d065beb91e02d21508271141a2a91af14b41200733bb0ad8450f6(
    *,
    api_gateway_cloud_watch_logs_account: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    api_gateway_cloud_watch_logs_role: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesApiGatewayCloudWatchLogsRole, typing.Dict[builtins.str, typing.Any]]] = None,
    classifier_resource: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesClassifierResource, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_doc_content_post: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesDeploymentDocContentPost, typing.Dict[builtins.str, typing.Any]]] = None,
    doc_content_post_method: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesDocContentPostMethod, typing.Dict[builtins.str, typing.Any]]] = None,
    doc_content_resource: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesDocContentResource, typing.Dict[builtins.str, typing.Any]]] = None,
    impact_api: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesImpactApi, typing.Dict[builtins.str, typing.Any]]] = None,
    impact_api_handle_lambda_function: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesImpactApiHandleLambdaFunction, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_function_create_role: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesLambdaFunctionCreateRole, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_permission: typing.Optional[typing.Union[CfnApiHandleModulePropsResourcesLambdaPermission, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__855c7d79586203faf8deb9026ee4afe636ef21611e721e62ec2ffb751bbc0979(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ae171034654512d35f8155b7dd856e373a6b457d16650c7dc9a2400a684adbd(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d421dd9f0d31b178f07d207f5c566139c1f2306247601afeb7848b33280586ed(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d86751ddd66ad3423d84018ce44c77448a5a6b0396fa4cbe00d45611ab1e10a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a61ebfca25b3ef1833ab4d0bce71350c5aaaf02100b3d734efc334c9954cdca(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6e96a0295d99768b1a790f5adc61f3af45377f0f596d8a24e8b82f4b1ed5b4d(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f486c14e7141162bd9349793a730e1ca1d15412c3b3aee8d3fde0a9d96dac1(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e91852e11642fb993231a63c6fe7d191b9d86abf5ff4d32ee930334fba4d61f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f4794f0f75aa47d373fa7aca7caafbcda560a8714157aa53a813219413c5ab(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f639547fd57fee41a4578e8d8595ec348af40a4cc8b652af254b0474f18495fc(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
