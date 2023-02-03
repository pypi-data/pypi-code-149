'''
# logzio-autodeploymentlogzio-cloudwatch-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `logzio::autoDeploymentLogzio::CloudWatch::MODULE` v2.2.0.

## Description

Schema for Module Fragment of type logzio::autoDeploymentLogzio::CloudWatch::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name logzio::autoDeploymentLogzio::CloudWatch::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/logzio-autoDeploymentLogzio-CloudWatch-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `logzio::autoDeploymentLogzio::CloudWatch::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-autodeploymentlogzio-cloudwatch-module+v2.2.0).
* Issues related to `logzio::autoDeploymentLogzio::CloudWatch::MODULE` should be reported to the [publisher](undefined).

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


class CfnCloudWatchModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModule",
):
    '''A CloudFormation ``logzio::autoDeploymentLogzio::CloudWatch::MODULE``.

    :cloudformationResource: logzio::autoDeploymentLogzio::CloudWatch::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnCloudWatchModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCloudWatchModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``logzio::autoDeploymentLogzio::CloudWatch::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__770a118549e3e120f2996e1becb3ca87514bb079d75a3fde61cfb2ab61f6d3d4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCloudWatchModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCloudWatchModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCloudWatchModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCloudWatchModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnCloudWatchModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCloudWatchModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type logzio::autoDeploymentLogzio::CloudWatch::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCloudWatchModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCloudWatchModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCloudWatchModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d06ce3e5ef50ecfdb322476f1e341f16460f89bac28650fea6769e41a046e2d)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCloudWatchModulePropsParameters"]:
        '''
        :schema: CfnCloudWatchModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCloudWatchModulePropsResources"]:
        '''
        :schema: CfnCloudWatchModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "log_group": "logGroup",
        "logzio_compress": "logzioCompress",
        "logzio_enrich": "logzioEnrich",
        "logzio_format": "logzioFormat",
        "logzio_listener_url": "logzioListenerUrl",
        "logzio_send_all": "logzioSendAll",
        "logzio_token": "logzioToken",
        "logzio_type": "logzioType",
    },
)
class CfnCloudWatchModulePropsParameters:
    def __init__(
        self,
        *,
        log_group: typing.Optional[typing.Union["CfnCloudWatchModulePropsParametersLogGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_compress: typing.Optional[typing.Union["CfnCloudWatchModulePropsParametersLogzioCompress", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_enrich: typing.Optional[typing.Union["CfnCloudWatchModulePropsParametersLogzioEnrich", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_format: typing.Optional[typing.Union["CfnCloudWatchModulePropsParametersLogzioFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_listener_url: typing.Optional[typing.Union["CfnCloudWatchModulePropsParametersLogzioListenerUrl", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_send_all: typing.Optional[typing.Union["CfnCloudWatchModulePropsParametersLogzioSendAll", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_token: typing.Optional[typing.Union["CfnCloudWatchModulePropsParametersLogzioToken", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_type: typing.Optional[typing.Union["CfnCloudWatchModulePropsParametersLogzioType", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param log_group: CloudWatch Log Group name from where you want to send logs.
        :param logzio_compress: If true, the Lambda will send compressed logs. If false, the Lambda will send uncompressed logs.
        :param logzio_enrich: Enriches the CloudWatch events with custom properties at ship time. The format is ``key1=value1;key2=value2``. By default is empty.
        :param logzio_format: JSON or text. If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.
        :param logzio_listener_url: The Logz.io listener URL for your region. You can find explanations here: https://docs.logz.io/user-guide/accounts/account-region.html.
        :param logzio_send_all: By default, we do not send logs of type START, END, REPORT. Choose true to send all log types.
        :param logzio_token: Logz.io account token.
        :param logzio_type: The log type you'll use with this Lambda. Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :schema: CfnCloudWatchModulePropsParameters
        '''
        if isinstance(log_group, dict):
            log_group = CfnCloudWatchModulePropsParametersLogGroup(**log_group)
        if isinstance(logzio_compress, dict):
            logzio_compress = CfnCloudWatchModulePropsParametersLogzioCompress(**logzio_compress)
        if isinstance(logzio_enrich, dict):
            logzio_enrich = CfnCloudWatchModulePropsParametersLogzioEnrich(**logzio_enrich)
        if isinstance(logzio_format, dict):
            logzio_format = CfnCloudWatchModulePropsParametersLogzioFormat(**logzio_format)
        if isinstance(logzio_listener_url, dict):
            logzio_listener_url = CfnCloudWatchModulePropsParametersLogzioListenerUrl(**logzio_listener_url)
        if isinstance(logzio_send_all, dict):
            logzio_send_all = CfnCloudWatchModulePropsParametersLogzioSendAll(**logzio_send_all)
        if isinstance(logzio_token, dict):
            logzio_token = CfnCloudWatchModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_type, dict):
            logzio_type = CfnCloudWatchModulePropsParametersLogzioType(**logzio_type)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5e257cc94c302700fa083aa448d83c408cc5f530d840ba7007f213196faf62)
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument logzio_compress", value=logzio_compress, expected_type=type_hints["logzio_compress"])
            check_type(argname="argument logzio_enrich", value=logzio_enrich, expected_type=type_hints["logzio_enrich"])
            check_type(argname="argument logzio_format", value=logzio_format, expected_type=type_hints["logzio_format"])
            check_type(argname="argument logzio_listener_url", value=logzio_listener_url, expected_type=type_hints["logzio_listener_url"])
            check_type(argname="argument logzio_send_all", value=logzio_send_all, expected_type=type_hints["logzio_send_all"])
            check_type(argname="argument logzio_token", value=logzio_token, expected_type=type_hints["logzio_token"])
            check_type(argname="argument logzio_type", value=logzio_type, expected_type=type_hints["logzio_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if log_group is not None:
            self._values["log_group"] = log_group
        if logzio_compress is not None:
            self._values["logzio_compress"] = logzio_compress
        if logzio_enrich is not None:
            self._values["logzio_enrich"] = logzio_enrich
        if logzio_format is not None:
            self._values["logzio_format"] = logzio_format
        if logzio_listener_url is not None:
            self._values["logzio_listener_url"] = logzio_listener_url
        if logzio_send_all is not None:
            self._values["logzio_send_all"] = logzio_send_all
        if logzio_token is not None:
            self._values["logzio_token"] = logzio_token
        if logzio_type is not None:
            self._values["logzio_type"] = logzio_type

    @builtins.property
    def log_group(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogGroup"]:
        '''CloudWatch Log Group name from where you want to send logs.

        :schema: CfnCloudWatchModulePropsParameters#LogGroup
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogGroup"], result)

    @builtins.property
    def logzio_compress(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioCompress"]:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :schema: CfnCloudWatchModulePropsParameters#LogzioCompress
        '''
        result = self._values.get("logzio_compress")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioCompress"], result)

    @builtins.property
    def logzio_enrich(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioEnrich"]:
        '''Enriches the CloudWatch events with custom properties at ship time.

        The format is ``key1=value1;key2=value2``. By default is empty.

        :schema: CfnCloudWatchModulePropsParameters#LogzioEnrich
        '''
        result = self._values.get("logzio_enrich")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioEnrich"], result)

    @builtins.property
    def logzio_format(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioFormat"]:
        '''JSON or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :schema: CfnCloudWatchModulePropsParameters#LogzioFormat
        '''
        result = self._values.get("logzio_format")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioFormat"], result)

    @builtins.property
    def logzio_listener_url(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioListenerUrl"]:
        '''The Logz.io listener URL for your region. You can find explanations here: https://docs.logz.io/user-guide/accounts/account-region.html.

        :schema: CfnCloudWatchModulePropsParameters#LogzioListenerUrl
        '''
        result = self._values.get("logzio_listener_url")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioListenerUrl"], result)

    @builtins.property
    def logzio_send_all(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioSendAll"]:
        '''By default, we do not send logs of type START, END, REPORT.

        Choose true to send all log types.

        :schema: CfnCloudWatchModulePropsParameters#LogzioSendAll
        '''
        result = self._values.get("logzio_send_all")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioSendAll"], result)

    @builtins.property
    def logzio_token(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioToken"]:
        '''Logz.io account token.

        :schema: CfnCloudWatchModulePropsParameters#LogzioToken
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_type(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsParametersLogzioType"]:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :schema: CfnCloudWatchModulePropsParameters#LogzioType
        '''
        result = self._values.get("logzio_type")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsParametersLogzioType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogGroup",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogGroup:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CloudWatch Log Group name from where you want to send logs.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e3f6a154cb82a8dc2899a9d4da00b5c839f5a01235319c8237b371d75da801)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogGroup#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogGroup#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioCompress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioCompress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioCompress
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__490094719a6ed7c8d8365c7e217ff1fb062f651e79381d98ca13f6d3e68ab5f8)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioCompress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioCompress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioCompress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioEnrich",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioEnrich:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Enriches the CloudWatch events with custom properties at ship time.

        The format is ``key1=value1;key2=value2``. By default is empty.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioEnrich
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a543cd285a584d7f04fa704b19dfa2e7be785f4bd4236834475ba3c737fde5e0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioEnrich#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioEnrich#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioEnrich(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioFormat",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioFormat:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''JSON or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioFormat
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23aefaf01d6ebe041220043197aea20150e46ad4e09ec8c37da3b455bc0b5853)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioFormat#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioFormat#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioListenerUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioListenerUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Logz.io listener URL for your region. You can find explanations here: https://docs.logz.io/user-guide/accounts/account-region.html.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioListenerUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08fa50b579fbdb9a091dfabaf3b2460babb0e0bb41b84d6777ce706da2793bde)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioListenerUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioListenerUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioListenerUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioSendAll",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioSendAll:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''By default, we do not send logs of type START, END, REPORT.

        Choose true to send all log types.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioSendAll
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3feed91b1a00f6c4ce539d588b265b62f288ca3b320ce1898dd8bd76ad7c399f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioSendAll#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioSendAll#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioSendAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Logz.io account token.

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioToken
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf3bc0b2a2bfb5249b39e84e3ae4401794010ca7afdaaf77993bebefc8b99ea1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsParametersLogzioType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCloudWatchModulePropsParametersLogzioType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :param description: 
        :param type: 

        :schema: CfnCloudWatchModulePropsParametersLogzioType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e9b22433bff8b92cb2e21864de970fdf00b0c328312ea830e76720fb6253d9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCloudWatchModulePropsParametersLogzioType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsParametersLogzioType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "lambda_iam_role": "lambdaIamRole",
        "lambda_permission": "lambdaPermission",
        "logzio_cloudwatch_logs_lambda": "logzioCloudwatchLogsLambda",
        "logzio_subscription_filter": "logzioSubscriptionFilter",
    },
)
class CfnCloudWatchModulePropsResources:
    def __init__(
        self,
        *,
        lambda_iam_role: typing.Optional[typing.Union["CfnCloudWatchModulePropsResourcesLambdaIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_permission: typing.Optional[typing.Union["CfnCloudWatchModulePropsResourcesLambdaPermission", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_cloudwatch_logs_lambda: typing.Optional[typing.Union["CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_subscription_filter: typing.Optional[typing.Union["CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param lambda_iam_role: 
        :param lambda_permission: 
        :param logzio_cloudwatch_logs_lambda: 
        :param logzio_subscription_filter: 

        :schema: CfnCloudWatchModulePropsResources
        '''
        if isinstance(lambda_iam_role, dict):
            lambda_iam_role = CfnCloudWatchModulePropsResourcesLambdaIamRole(**lambda_iam_role)
        if isinstance(lambda_permission, dict):
            lambda_permission = CfnCloudWatchModulePropsResourcesLambdaPermission(**lambda_permission)
        if isinstance(logzio_cloudwatch_logs_lambda, dict):
            logzio_cloudwatch_logs_lambda = CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda(**logzio_cloudwatch_logs_lambda)
        if isinstance(logzio_subscription_filter, dict):
            logzio_subscription_filter = CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter(**logzio_subscription_filter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e06cf0d137ca27c841f8fcdac90a913fb142e6ebd167f344b137cf9c9d7d8430)
            check_type(argname="argument lambda_iam_role", value=lambda_iam_role, expected_type=type_hints["lambda_iam_role"])
            check_type(argname="argument lambda_permission", value=lambda_permission, expected_type=type_hints["lambda_permission"])
            check_type(argname="argument logzio_cloudwatch_logs_lambda", value=logzio_cloudwatch_logs_lambda, expected_type=type_hints["logzio_cloudwatch_logs_lambda"])
            check_type(argname="argument logzio_subscription_filter", value=logzio_subscription_filter, expected_type=type_hints["logzio_subscription_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lambda_iam_role is not None:
            self._values["lambda_iam_role"] = lambda_iam_role
        if lambda_permission is not None:
            self._values["lambda_permission"] = lambda_permission
        if logzio_cloudwatch_logs_lambda is not None:
            self._values["logzio_cloudwatch_logs_lambda"] = logzio_cloudwatch_logs_lambda
        if logzio_subscription_filter is not None:
            self._values["logzio_subscription_filter"] = logzio_subscription_filter

    @builtins.property
    def lambda_iam_role(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsResourcesLambdaIamRole"]:
        '''
        :schema: CfnCloudWatchModulePropsResources#lambdaIamRole
        '''
        result = self._values.get("lambda_iam_role")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResourcesLambdaIamRole"], result)

    @builtins.property
    def lambda_permission(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsResourcesLambdaPermission"]:
        '''
        :schema: CfnCloudWatchModulePropsResources#LambdaPermission
        '''
        result = self._values.get("lambda_permission")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResourcesLambdaPermission"], result)

    @builtins.property
    def logzio_cloudwatch_logs_lambda(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda"]:
        '''
        :schema: CfnCloudWatchModulePropsResources#LogzioCloudwatchLogsLambda
        '''
        result = self._values.get("logzio_cloudwatch_logs_lambda")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda"], result)

    @builtins.property
    def logzio_subscription_filter(
        self,
    ) -> typing.Optional["CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter"]:
        '''
        :schema: CfnCloudWatchModulePropsResources#LogzioSubscriptionFilter
        '''
        result = self._values.get("logzio_subscription_filter")
        return typing.cast(typing.Optional["CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResourcesLambdaIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudWatchModulePropsResourcesLambdaIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudWatchModulePropsResourcesLambdaIamRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a619244511675fcb7729b0e92c3ac66647ff16ba4efca64d5efd2549793819)
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
        :schema: CfnCloudWatchModulePropsResourcesLambdaIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLambdaIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResourcesLambdaIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResourcesLambdaPermission",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudWatchModulePropsResourcesLambdaPermission:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudWatchModulePropsResourcesLambdaPermission
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbdf880b7765b51dfe5c7e0184565cc49ac82356e72e4b63c67c522dbd86320a)
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
        :schema: CfnCloudWatchModulePropsResourcesLambdaPermission#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLambdaPermission#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResourcesLambdaPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f7ef978ad8f0f98de8269edb273d98d1f4fb29a646252b322512712a9eb875e)
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
        :schema: CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-autodeploymentlogzio-cloudwatch-module.CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__962c7d50fd509e4e5321c8663254896f8f7d3464d0309139f1fea0156268477c)
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
        :schema: CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCloudWatchModule",
    "CfnCloudWatchModuleProps",
    "CfnCloudWatchModulePropsParameters",
    "CfnCloudWatchModulePropsParametersLogGroup",
    "CfnCloudWatchModulePropsParametersLogzioCompress",
    "CfnCloudWatchModulePropsParametersLogzioEnrich",
    "CfnCloudWatchModulePropsParametersLogzioFormat",
    "CfnCloudWatchModulePropsParametersLogzioListenerUrl",
    "CfnCloudWatchModulePropsParametersLogzioSendAll",
    "CfnCloudWatchModulePropsParametersLogzioToken",
    "CfnCloudWatchModulePropsParametersLogzioType",
    "CfnCloudWatchModulePropsResources",
    "CfnCloudWatchModulePropsResourcesLambdaIamRole",
    "CfnCloudWatchModulePropsResourcesLambdaPermission",
    "CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda",
    "CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter",
]

publication.publish()

def _typecheckingstub__770a118549e3e120f2996e1becb3ca87514bb079d75a3fde61cfb2ab61f6d3d4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnCloudWatchModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCloudWatchModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d06ce3e5ef50ecfdb322476f1e341f16460f89bac28650fea6769e41a046e2d(
    *,
    parameters: typing.Optional[typing.Union[CfnCloudWatchModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCloudWatchModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5e257cc94c302700fa083aa448d83c408cc5f530d840ba7007f213196faf62(
    *,
    log_group: typing.Optional[typing.Union[CfnCloudWatchModulePropsParametersLogGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_compress: typing.Optional[typing.Union[CfnCloudWatchModulePropsParametersLogzioCompress, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_enrich: typing.Optional[typing.Union[CfnCloudWatchModulePropsParametersLogzioEnrich, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_format: typing.Optional[typing.Union[CfnCloudWatchModulePropsParametersLogzioFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_listener_url: typing.Optional[typing.Union[CfnCloudWatchModulePropsParametersLogzioListenerUrl, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_send_all: typing.Optional[typing.Union[CfnCloudWatchModulePropsParametersLogzioSendAll, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_token: typing.Optional[typing.Union[CfnCloudWatchModulePropsParametersLogzioToken, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_type: typing.Optional[typing.Union[CfnCloudWatchModulePropsParametersLogzioType, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e3f6a154cb82a8dc2899a9d4da00b5c839f5a01235319c8237b371d75da801(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__490094719a6ed7c8d8365c7e217ff1fb062f651e79381d98ca13f6d3e68ab5f8(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a543cd285a584d7f04fa704b19dfa2e7be785f4bd4236834475ba3c737fde5e0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23aefaf01d6ebe041220043197aea20150e46ad4e09ec8c37da3b455bc0b5853(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08fa50b579fbdb9a091dfabaf3b2460babb0e0bb41b84d6777ce706da2793bde(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3feed91b1a00f6c4ce539d588b265b62f288ca3b320ce1898dd8bd76ad7c399f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3bc0b2a2bfb5249b39e84e3ae4401794010ca7afdaaf77993bebefc8b99ea1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e9b22433bff8b92cb2e21864de970fdf00b0c328312ea830e76720fb6253d9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e06cf0d137ca27c841f8fcdac90a913fb142e6ebd167f344b137cf9c9d7d8430(
    *,
    lambda_iam_role: typing.Optional[typing.Union[CfnCloudWatchModulePropsResourcesLambdaIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_permission: typing.Optional[typing.Union[CfnCloudWatchModulePropsResourcesLambdaPermission, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_cloudwatch_logs_lambda: typing.Optional[typing.Union[CfnCloudWatchModulePropsResourcesLogzioCloudwatchLogsLambda, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_subscription_filter: typing.Optional[typing.Union[CfnCloudWatchModulePropsResourcesLogzioSubscriptionFilter, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a619244511675fcb7729b0e92c3ac66647ff16ba4efca64d5efd2549793819(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbdf880b7765b51dfe5c7e0184565cc49ac82356e72e4b63c67c522dbd86320a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f7ef978ad8f0f98de8269edb273d98d1f4fb29a646252b322512712a9eb875e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__962c7d50fd509e4e5321c8663254896f8f7d3464d0309139f1fea0156268477c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
