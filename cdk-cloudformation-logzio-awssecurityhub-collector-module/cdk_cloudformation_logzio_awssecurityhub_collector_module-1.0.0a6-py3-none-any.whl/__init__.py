'''
# logzio-awssecurityhub-collector-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `logzio::awsSecurityHub::collector::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type logzio::awsSecurityHub::collector::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name logzio::awsSecurityHub::collector::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/logzio-awsSecurityHub-collector-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `logzio::awsSecurityHub::collector::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-awssecurityhub-collector-module+v1.0.0).
* Issues related to `logzio::awsSecurityHub::collector::MODULE` should be reported to the [publisher](undefined).

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


class CfnCollectorModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModule",
):
    '''A CloudFormation ``logzio::awsSecurityHub::collector::MODULE``.

    :cloudformationResource: logzio::awsSecurityHub::collector::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnCollectorModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCollectorModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``logzio::awsSecurityHub::collector::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5155e207815ed1615aa95dd68a96526198cb78900d1e7fe5d45deabdd1fe050)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCollectorModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCollectorModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCollectorModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCollectorModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnCollectorModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCollectorModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type logzio::awsSecurityHub::collector::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCollectorModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCollectorModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCollectorModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__143cd96396d31cbf48bbcdfddd7effcc849db3c609f9177a5248bd8cda958d4d)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCollectorModulePropsParameters"]:
        '''
        :schema: CfnCollectorModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCollectorModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCollectorModulePropsResources"]:
        '''
        :schema: CfnCollectorModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "logzio_listener": "logzioListener",
        "logzio_log_level": "logzioLogLevel",
        "logzio_operations_token": "logzioOperationsToken",
    },
)
class CfnCollectorModulePropsParameters:
    def __init__(
        self,
        *,
        logzio_listener: typing.Optional[typing.Union["CfnCollectorModulePropsParametersLogzioListener", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_log_level: typing.Optional[typing.Union["CfnCollectorModulePropsParametersLogzioLogLevel", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_operations_token: typing.Optional[typing.Union["CfnCollectorModulePropsParametersLogzioOperationsToken", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param logzio_listener: Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.
        :param logzio_log_level: Log level for the function.
        :param logzio_operations_token: Your Logz.io operations token.

        :schema: CfnCollectorModulePropsParameters
        '''
        if isinstance(logzio_listener, dict):
            logzio_listener = CfnCollectorModulePropsParametersLogzioListener(**logzio_listener)
        if isinstance(logzio_log_level, dict):
            logzio_log_level = CfnCollectorModulePropsParametersLogzioLogLevel(**logzio_log_level)
        if isinstance(logzio_operations_token, dict):
            logzio_operations_token = CfnCollectorModulePropsParametersLogzioOperationsToken(**logzio_operations_token)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e283d576bc136810d682a791396f1c30882dfb14788d1a8b796629bd0e1fe326)
            check_type(argname="argument logzio_listener", value=logzio_listener, expected_type=type_hints["logzio_listener"])
            check_type(argname="argument logzio_log_level", value=logzio_log_level, expected_type=type_hints["logzio_log_level"])
            check_type(argname="argument logzio_operations_token", value=logzio_operations_token, expected_type=type_hints["logzio_operations_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if logzio_listener is not None:
            self._values["logzio_listener"] = logzio_listener
        if logzio_log_level is not None:
            self._values["logzio_log_level"] = logzio_log_level
        if logzio_operations_token is not None:
            self._values["logzio_operations_token"] = logzio_operations_token

    @builtins.property
    def logzio_listener(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsParametersLogzioListener"]:
        '''Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.

        :schema: CfnCollectorModulePropsParameters#logzioListener
        '''
        result = self._values.get("logzio_listener")
        return typing.cast(typing.Optional["CfnCollectorModulePropsParametersLogzioListener"], result)

    @builtins.property
    def logzio_log_level(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsParametersLogzioLogLevel"]:
        '''Log level for the function.

        :schema: CfnCollectorModulePropsParameters#logzioLogLevel
        '''
        result = self._values.get("logzio_log_level")
        return typing.cast(typing.Optional["CfnCollectorModulePropsParametersLogzioLogLevel"], result)

    @builtins.property
    def logzio_operations_token(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsParametersLogzioOperationsToken"]:
        '''Your Logz.io operations token.

        :schema: CfnCollectorModulePropsParameters#logzioOperationsToken
        '''
        result = self._values.get("logzio_operations_token")
        return typing.cast(typing.Optional["CfnCollectorModulePropsParametersLogzioOperationsToken"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsParametersLogzioListener",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCollectorModulePropsParametersLogzioListener:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io listener with port 8070/8071. For example https://listener.logz.io:8071.

        :param description: 
        :param type: 

        :schema: CfnCollectorModulePropsParametersLogzioListener
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d485acc4d27ce340ec98fbd729f3b03d7e624f3f5dde68cc1ad17c6d7db25f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioListener#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioListener#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsParametersLogzioListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsParametersLogzioLogLevel",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCollectorModulePropsParametersLogzioLogLevel:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Log level for the function.

        :param description: 
        :param type: 

        :schema: CfnCollectorModulePropsParametersLogzioLogLevel
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada302ea964e2a76a5b5a88dceac385a7bc2a681382982174e9a256f499fc0a6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioLogLevel#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioLogLevel#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsParametersLogzioLogLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsParametersLogzioOperationsToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCollectorModulePropsParametersLogzioOperationsToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io operations token.

        :param description: 
        :param type: 

        :schema: CfnCollectorModulePropsParametersLogzioOperationsToken
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41d2f6f580402150fd75d718fdb13ae5b590706effea19dcbb9f07dae9cfb275)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioOperationsToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCollectorModulePropsParametersLogzioOperationsToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsParametersLogzioOperationsToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "event_rule": "eventRule",
        "lambda_iam_role": "lambdaIamRole",
        "lambda_permissions": "lambdaPermissions",
        "logzio_security_hub_collector": "logzioSecurityHubCollector",
    },
)
class CfnCollectorModulePropsResources:
    def __init__(
        self,
        *,
        event_rule: typing.Optional[typing.Union["CfnCollectorModulePropsResourcesEventRule", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_iam_role: typing.Optional[typing.Union["CfnCollectorModulePropsResourcesLambdaIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_permissions: typing.Optional[typing.Union["CfnCollectorModulePropsResourcesLambdaPermissions", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_security_hub_collector: typing.Optional[typing.Union["CfnCollectorModulePropsResourcesLogzioSecurityHubCollector", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param event_rule: 
        :param lambda_iam_role: 
        :param lambda_permissions: 
        :param logzio_security_hub_collector: 

        :schema: CfnCollectorModulePropsResources
        '''
        if isinstance(event_rule, dict):
            event_rule = CfnCollectorModulePropsResourcesEventRule(**event_rule)
        if isinstance(lambda_iam_role, dict):
            lambda_iam_role = CfnCollectorModulePropsResourcesLambdaIamRole(**lambda_iam_role)
        if isinstance(lambda_permissions, dict):
            lambda_permissions = CfnCollectorModulePropsResourcesLambdaPermissions(**lambda_permissions)
        if isinstance(logzio_security_hub_collector, dict):
            logzio_security_hub_collector = CfnCollectorModulePropsResourcesLogzioSecurityHubCollector(**logzio_security_hub_collector)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd494023be6260cbe03da3def3b42cad21eb5fb786f03ff80d45dd9dbf2a133)
            check_type(argname="argument event_rule", value=event_rule, expected_type=type_hints["event_rule"])
            check_type(argname="argument lambda_iam_role", value=lambda_iam_role, expected_type=type_hints["lambda_iam_role"])
            check_type(argname="argument lambda_permissions", value=lambda_permissions, expected_type=type_hints["lambda_permissions"])
            check_type(argname="argument logzio_security_hub_collector", value=logzio_security_hub_collector, expected_type=type_hints["logzio_security_hub_collector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if event_rule is not None:
            self._values["event_rule"] = event_rule
        if lambda_iam_role is not None:
            self._values["lambda_iam_role"] = lambda_iam_role
        if lambda_permissions is not None:
            self._values["lambda_permissions"] = lambda_permissions
        if logzio_security_hub_collector is not None:
            self._values["logzio_security_hub_collector"] = logzio_security_hub_collector

    @builtins.property
    def event_rule(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsResourcesEventRule"]:
        '''
        :schema: CfnCollectorModulePropsResources#eventRule
        '''
        result = self._values.get("event_rule")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResourcesEventRule"], result)

    @builtins.property
    def lambda_iam_role(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsResourcesLambdaIamRole"]:
        '''
        :schema: CfnCollectorModulePropsResources#lambdaIamRole
        '''
        result = self._values.get("lambda_iam_role")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResourcesLambdaIamRole"], result)

    @builtins.property
    def lambda_permissions(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsResourcesLambdaPermissions"]:
        '''
        :schema: CfnCollectorModulePropsResources#lambdaPermissions
        '''
        result = self._values.get("lambda_permissions")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResourcesLambdaPermissions"], result)

    @builtins.property
    def logzio_security_hub_collector(
        self,
    ) -> typing.Optional["CfnCollectorModulePropsResourcesLogzioSecurityHubCollector"]:
        '''
        :schema: CfnCollectorModulePropsResources#logzioSecurityHubCollector
        '''
        result = self._values.get("logzio_security_hub_collector")
        return typing.cast(typing.Optional["CfnCollectorModulePropsResourcesLogzioSecurityHubCollector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResourcesEventRule",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCollectorModulePropsResourcesEventRule:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCollectorModulePropsResourcesEventRule
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61e643b128cbeb233f3c39e7d0705a4dc41be7e42bd0dc4af1aaf38c44300370)
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
        :schema: CfnCollectorModulePropsResourcesEventRule#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCollectorModulePropsResourcesEventRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResourcesEventRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResourcesLambdaIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCollectorModulePropsResourcesLambdaIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCollectorModulePropsResourcesLambdaIamRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c4d35f152955eeeafb17d9ceb3bca7d24f76967b2f87a2ad26e84778ab0d52d)
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
        :schema: CfnCollectorModulePropsResourcesLambdaIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCollectorModulePropsResourcesLambdaIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResourcesLambdaIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResourcesLambdaPermissions",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCollectorModulePropsResourcesLambdaPermissions:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCollectorModulePropsResourcesLambdaPermissions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea5797a18f15cc9a30231ab4e7b44e6ada8d320dc10577c88b1cb11d346faa26)
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
        :schema: CfnCollectorModulePropsResourcesLambdaPermissions#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCollectorModulePropsResourcesLambdaPermissions#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResourcesLambdaPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awssecurityhub-collector-module.CfnCollectorModulePropsResourcesLogzioSecurityHubCollector",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCollectorModulePropsResourcesLogzioSecurityHubCollector:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCollectorModulePropsResourcesLogzioSecurityHubCollector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f24a5c72535413b3126dc3986350c0128d646e58ffcb9318eff63fd6cf8d2fb1)
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
        :schema: CfnCollectorModulePropsResourcesLogzioSecurityHubCollector#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCollectorModulePropsResourcesLogzioSecurityHubCollector#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectorModulePropsResourcesLogzioSecurityHubCollector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCollectorModule",
    "CfnCollectorModuleProps",
    "CfnCollectorModulePropsParameters",
    "CfnCollectorModulePropsParametersLogzioListener",
    "CfnCollectorModulePropsParametersLogzioLogLevel",
    "CfnCollectorModulePropsParametersLogzioOperationsToken",
    "CfnCollectorModulePropsResources",
    "CfnCollectorModulePropsResourcesEventRule",
    "CfnCollectorModulePropsResourcesLambdaIamRole",
    "CfnCollectorModulePropsResourcesLambdaPermissions",
    "CfnCollectorModulePropsResourcesLogzioSecurityHubCollector",
]

publication.publish()

def _typecheckingstub__d5155e207815ed1615aa95dd68a96526198cb78900d1e7fe5d45deabdd1fe050(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnCollectorModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCollectorModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143cd96396d31cbf48bbcdfddd7effcc849db3c609f9177a5248bd8cda958d4d(
    *,
    parameters: typing.Optional[typing.Union[CfnCollectorModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCollectorModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e283d576bc136810d682a791396f1c30882dfb14788d1a8b796629bd0e1fe326(
    *,
    logzio_listener: typing.Optional[typing.Union[CfnCollectorModulePropsParametersLogzioListener, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_log_level: typing.Optional[typing.Union[CfnCollectorModulePropsParametersLogzioLogLevel, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_operations_token: typing.Optional[typing.Union[CfnCollectorModulePropsParametersLogzioOperationsToken, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d485acc4d27ce340ec98fbd729f3b03d7e624f3f5dde68cc1ad17c6d7db25f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada302ea964e2a76a5b5a88dceac385a7bc2a681382982174e9a256f499fc0a6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d2f6f580402150fd75d718fdb13ae5b590706effea19dcbb9f07dae9cfb275(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd494023be6260cbe03da3def3b42cad21eb5fb786f03ff80d45dd9dbf2a133(
    *,
    event_rule: typing.Optional[typing.Union[CfnCollectorModulePropsResourcesEventRule, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_iam_role: typing.Optional[typing.Union[CfnCollectorModulePropsResourcesLambdaIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_permissions: typing.Optional[typing.Union[CfnCollectorModulePropsResourcesLambdaPermissions, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_security_hub_collector: typing.Optional[typing.Union[CfnCollectorModulePropsResourcesLogzioSecurityHubCollector, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e643b128cbeb233f3c39e7d0705a4dc41be7e42bd0dc4af1aaf38c44300370(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4d35f152955eeeafb17d9ceb3bca7d24f76967b2f87a2ad26e84778ab0d52d(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5797a18f15cc9a30231ab4e7b44e6ada8d320dc10577c88b1cb11d346faa26(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f24a5c72535413b3126dc3986350c0128d646e58ffcb9318eff63fd6cf8d2fb1(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
