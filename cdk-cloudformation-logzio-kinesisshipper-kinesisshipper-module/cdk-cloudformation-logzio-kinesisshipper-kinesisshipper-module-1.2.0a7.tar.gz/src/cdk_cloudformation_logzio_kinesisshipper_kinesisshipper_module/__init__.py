'''
# logzio-kinesisshipper-kinesisshipper-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Logzio::KinesisShipper::KinesisShipper::MODULE` v1.2.0.

## Description

Schema for Module Fragment of type Logzio::KinesisShipper::KinesisShipper::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Logzio::KinesisShipper::KinesisShipper::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/Logzio-KinesisShipper-KinesisShipper-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Logzio::KinesisShipper::KinesisShipper::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-kinesisshipper-kinesisshipper-module+v1.2.0).
* Issues related to `Logzio::KinesisShipper::KinesisShipper::MODULE` should be reported to the [publisher](undefined).

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


class CfnKinesisShipperModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModule",
):
    '''A CloudFormation ``Logzio::KinesisShipper::KinesisShipper::MODULE``.

    :cloudformationResource: Logzio::KinesisShipper::KinesisShipper::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnKinesisShipperModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Logzio::KinesisShipper::KinesisShipper::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba88c40e6c27cf492c17753994ec92c0c7116088c57aabfeef9e28f288a1c6ac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKinesisShipperModuleProps(
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
    def props(self) -> "CfnKinesisShipperModuleProps":
        '''Resource props.'''
        return typing.cast("CfnKinesisShipperModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnKinesisShipperModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnKinesisShipperModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type Logzio::KinesisShipper::KinesisShipper::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnKinesisShipperModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnKinesisShipperModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnKinesisShipperModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1846119ad587f0f61cfbc68e2f4660f516ae197a20e9f7cf98b53eb6fa3e8c52)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnKinesisShipperModulePropsParameters"]:
        '''
        :schema: CfnKinesisShipperModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnKinesisShipperModulePropsResources"]:
        '''
        :schema: CfnKinesisShipperModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "kinesis_stream": "kinesisStream",
        "kinesis_stream_batch_size": "kinesisStreamBatchSize",
        "kinesis_stream_starting_position": "kinesisStreamStartingPosition",
        "logzio_compress": "logzioCompress",
        "logzio_format": "logzioFormat",
        "logzio_messages_array": "logzioMessagesArray",
        "logzio_region": "logzioRegion",
        "logzio_token": "logzioToken",
        "logzio_type": "logzioType",
        "logzio_url": "logzioUrl",
    },
)
class CfnKinesisShipperModulePropsParameters:
    def __init__(
        self,
        *,
        kinesis_stream: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersKinesisStream", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_stream_batch_size: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_stream_starting_position: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_compress: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersLogzioCompress", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_format: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersLogzioFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_messages_array: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersLogzioMessagesArray", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_region: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersLogzioRegion", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_token: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersLogzioToken", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_type: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersLogzioType", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_url: typing.Optional[typing.Union["CfnKinesisShipperModulePropsParametersLogzioUrl", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param kinesis_stream: Enter a Kinesis stream to listen for updates on.
        :param kinesis_stream_batch_size: The largest number of records that will be read from your stream at once.
        :param kinesis_stream_starting_position: The position in the stream to start reading from. For more information, see ShardIteratorType in the Amazon Kinesis API Reference.
        :param logzio_compress: If true, the Lambda will send compressed logs. If false, the Lambda will send uncompressed logs.
        :param logzio_format: json or text. If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.
        :param logzio_messages_array: Set this ENV variable to split the a record into multiple logs based on a field containing an array of messages. For more information see https://github.com/logzio/logzio_aws_serverless/blob/master/python3/kinesis/parse-json-array.md. Note: This option would work only if you set FORMAT to json.
        :param logzio_region: Two-letter region code, or blank for US East (Northern Virginia). This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the Regions and URLs at https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls table
        :param logzio_token: The token of the account you want to ship to. Can be found at https://app.logz.io/#/dashboard/settings/general
        :param logzio_type: The log type you'll use with this Lambda. Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type
        :param logzio_url: Deprecated. Use LogzioREGION instead

        :schema: CfnKinesisShipperModulePropsParameters
        '''
        if isinstance(kinesis_stream, dict):
            kinesis_stream = CfnKinesisShipperModulePropsParametersKinesisStream(**kinesis_stream)
        if isinstance(kinesis_stream_batch_size, dict):
            kinesis_stream_batch_size = CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize(**kinesis_stream_batch_size)
        if isinstance(kinesis_stream_starting_position, dict):
            kinesis_stream_starting_position = CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition(**kinesis_stream_starting_position)
        if isinstance(logzio_compress, dict):
            logzio_compress = CfnKinesisShipperModulePropsParametersLogzioCompress(**logzio_compress)
        if isinstance(logzio_format, dict):
            logzio_format = CfnKinesisShipperModulePropsParametersLogzioFormat(**logzio_format)
        if isinstance(logzio_messages_array, dict):
            logzio_messages_array = CfnKinesisShipperModulePropsParametersLogzioMessagesArray(**logzio_messages_array)
        if isinstance(logzio_region, dict):
            logzio_region = CfnKinesisShipperModulePropsParametersLogzioRegion(**logzio_region)
        if isinstance(logzio_token, dict):
            logzio_token = CfnKinesisShipperModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_type, dict):
            logzio_type = CfnKinesisShipperModulePropsParametersLogzioType(**logzio_type)
        if isinstance(logzio_url, dict):
            logzio_url = CfnKinesisShipperModulePropsParametersLogzioUrl(**logzio_url)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be5f03060577c131f9ff20ba9e5df8072156d4abd2780c4df3a2c8653b547499)
            check_type(argname="argument kinesis_stream", value=kinesis_stream, expected_type=type_hints["kinesis_stream"])
            check_type(argname="argument kinesis_stream_batch_size", value=kinesis_stream_batch_size, expected_type=type_hints["kinesis_stream_batch_size"])
            check_type(argname="argument kinesis_stream_starting_position", value=kinesis_stream_starting_position, expected_type=type_hints["kinesis_stream_starting_position"])
            check_type(argname="argument logzio_compress", value=logzio_compress, expected_type=type_hints["logzio_compress"])
            check_type(argname="argument logzio_format", value=logzio_format, expected_type=type_hints["logzio_format"])
            check_type(argname="argument logzio_messages_array", value=logzio_messages_array, expected_type=type_hints["logzio_messages_array"])
            check_type(argname="argument logzio_region", value=logzio_region, expected_type=type_hints["logzio_region"])
            check_type(argname="argument logzio_token", value=logzio_token, expected_type=type_hints["logzio_token"])
            check_type(argname="argument logzio_type", value=logzio_type, expected_type=type_hints["logzio_type"])
            check_type(argname="argument logzio_url", value=logzio_url, expected_type=type_hints["logzio_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if kinesis_stream is not None:
            self._values["kinesis_stream"] = kinesis_stream
        if kinesis_stream_batch_size is not None:
            self._values["kinesis_stream_batch_size"] = kinesis_stream_batch_size
        if kinesis_stream_starting_position is not None:
            self._values["kinesis_stream_starting_position"] = kinesis_stream_starting_position
        if logzio_compress is not None:
            self._values["logzio_compress"] = logzio_compress
        if logzio_format is not None:
            self._values["logzio_format"] = logzio_format
        if logzio_messages_array is not None:
            self._values["logzio_messages_array"] = logzio_messages_array
        if logzio_region is not None:
            self._values["logzio_region"] = logzio_region
        if logzio_token is not None:
            self._values["logzio_token"] = logzio_token
        if logzio_type is not None:
            self._values["logzio_type"] = logzio_type
        if logzio_url is not None:
            self._values["logzio_url"] = logzio_url

    @builtins.property
    def kinesis_stream(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStream"]:
        '''Enter a Kinesis stream to listen for updates on.

        :schema: CfnKinesisShipperModulePropsParameters#KinesisStream
        '''
        result = self._values.get("kinesis_stream")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStream"], result)

    @builtins.property
    def kinesis_stream_batch_size(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize"]:
        '''The largest number of records that will be read from your stream at once.

        :schema: CfnKinesisShipperModulePropsParameters#KinesisStreamBatchSize
        '''
        result = self._values.get("kinesis_stream_batch_size")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize"], result)

    @builtins.property
    def kinesis_stream_starting_position(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition"]:
        '''The position in the stream to start reading from.

        For more information, see ShardIteratorType in the Amazon Kinesis API Reference.

        :schema: CfnKinesisShipperModulePropsParameters#KinesisStreamStartingPosition
        '''
        result = self._values.get("kinesis_stream_starting_position")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition"], result)

    @builtins.property
    def logzio_compress(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioCompress"]:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :schema: CfnKinesisShipperModulePropsParameters#LogzioCOMPRESS
        '''
        result = self._values.get("logzio_compress")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioCompress"], result)

    @builtins.property
    def logzio_format(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioFormat"]:
        '''json or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :schema: CfnKinesisShipperModulePropsParameters#LogzioFORMAT
        '''
        result = self._values.get("logzio_format")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioFormat"], result)

    @builtins.property
    def logzio_messages_array(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioMessagesArray"]:
        '''Set this ENV variable to split the a record into multiple logs based on a field containing an array of messages.

        For more information see https://github.com/logzio/logzio_aws_serverless/blob/master/python3/kinesis/parse-json-array.md. Note: This option would work only if you set FORMAT to json.

        :schema: CfnKinesisShipperModulePropsParameters#LogzioMessagesArray
        '''
        result = self._values.get("logzio_messages_array")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioMessagesArray"], result)

    @builtins.property
    def logzio_region(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioRegion"]:
        '''Two-letter region code, or blank for US East (Northern Virginia).

        This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the Regions and URLs at https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls table

        :schema: CfnKinesisShipperModulePropsParameters#LogzioREGION
        '''
        result = self._values.get("logzio_region")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioRegion"], result)

    @builtins.property
    def logzio_token(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioToken"]:
        '''The token of the account you want to ship to.

        Can be found at https://app.logz.io/#/dashboard/settings/general

        :schema: CfnKinesisShipperModulePropsParameters#LogzioTOKEN
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_type(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioType"]:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :schema: CfnKinesisShipperModulePropsParameters#LogzioTYPE
        '''
        result = self._values.get("logzio_type")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioType"], result)

    @builtins.property
    def logzio_url(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsParametersLogzioUrl"]:
        '''Deprecated.

        Use LogzioREGION instead

        :schema: CfnKinesisShipperModulePropsParameters#LogzioURL
        '''
        result = self._values.get("logzio_url")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsParametersLogzioUrl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersKinesisStream:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Enter a Kinesis stream to listen for updates on.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersKinesisStream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe11575b61431e352ab757d4ddc131585cddf57410c3b8226d79004f0c4c1f6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStream#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStream#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The largest number of records that will be read from your stream at once.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d42f65000f24d44f19a7b0bd162c9d77bf0e96ffab0bb7b8ff4d85a80191142)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The position in the stream to start reading from.

        For more information, see ShardIteratorType in the Amazon Kinesis API Reference.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8da2bb88b2188bf8e5ec1fb95680638880925b507d69eb7a543714fdcbc27ee)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioCompress",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioCompress:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''If true, the Lambda will send compressed logs.

        If false, the Lambda will send uncompressed logs.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioCompress
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__644eccbd5c4897ff0c5fc1b2497fbc5281119e6e2ce3d35ad403b0fad1865c0e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioCompress#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioCompress#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioCompress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioFormat",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioFormat:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''json or text.

        If json, the lambda function will attempt to parse the message field as JSON and populate the event data with the parsed fields.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioFormat
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c357b7c9b8a0f4df8bdaa8eedbffef38ab29887e80c81a70fe254936be68fa4f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioFormat#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioFormat#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioMessagesArray",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioMessagesArray:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set this ENV variable to split the a record into multiple logs based on a field containing an array of messages.

        For more information see https://github.com/logzio/logzio_aws_serverless/blob/master/python3/kinesis/parse-json-array.md. Note: This option would work only if you set FORMAT to json.

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioMessagesArray
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2027fd2688c56d248177420d76f02829ce9b029f47ef26ebff3f17612c0cb17c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioMessagesArray#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioMessagesArray#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioMessagesArray(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Two-letter region code, or blank for US East (Northern Virginia).

        This determines your listener URL (where you're shipping the logs to) and API URL. You can find your region code in the Regions and URLs at https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls table

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioRegion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abb1555fcac945b483d8dbb49aa3b79d34c4c7d131a1fe956117f714f2d0a243)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The token of the account you want to ship to.

        Can be found at https://app.logz.io/#/dashboard/settings/general

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioToken
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b80e22e9385edf116bfcb9b085af05827bf2fc469a30595e7a9f893384f8cd7)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The log type you'll use with this Lambda.

        Please note that you should create a new Lambda for each log type you use. This can be a built-in log type, or your custom log type

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b4460c81da11229ede35829078bbad1d2bb29a9d100d6811f861e1834c1d9e3)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsParametersLogzioUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnKinesisShipperModulePropsParametersLogzioUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Deprecated.

        Use LogzioREGION instead

        :param description: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsParametersLogzioUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4998085d19cf921f410b9d26aea4eb5129f7c6f1ee256f0b291d1cd614c9770e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnKinesisShipperModulePropsParametersLogzioUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsParametersLogzioUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "logzio_kinesis_lambda": "logzioKinesisLambda",
        "logzio_kinesis_lambda_kinesis_stream": "logzioKinesisLambdaKinesisStream",
        "logzio_kinesis_lambda_role": "logzioKinesisLambdaRole",
    },
)
class CfnKinesisShipperModulePropsResources:
    def __init__(
        self,
        *,
        logzio_kinesis_lambda: typing.Optional[typing.Union["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_kinesis_lambda_kinesis_stream: typing.Optional[typing.Union["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_kinesis_lambda_role: typing.Optional[typing.Union["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param logzio_kinesis_lambda: 
        :param logzio_kinesis_lambda_kinesis_stream: 
        :param logzio_kinesis_lambda_role: 

        :schema: CfnKinesisShipperModulePropsResources
        '''
        if isinstance(logzio_kinesis_lambda, dict):
            logzio_kinesis_lambda = CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda(**logzio_kinesis_lambda)
        if isinstance(logzio_kinesis_lambda_kinesis_stream, dict):
            logzio_kinesis_lambda_kinesis_stream = CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream(**logzio_kinesis_lambda_kinesis_stream)
        if isinstance(logzio_kinesis_lambda_role, dict):
            logzio_kinesis_lambda_role = CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole(**logzio_kinesis_lambda_role)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__245c1ea1efc5e2062940a21ff2830c7afad8c4d41bd4950e9a6e66d00c4f1c88)
            check_type(argname="argument logzio_kinesis_lambda", value=logzio_kinesis_lambda, expected_type=type_hints["logzio_kinesis_lambda"])
            check_type(argname="argument logzio_kinesis_lambda_kinesis_stream", value=logzio_kinesis_lambda_kinesis_stream, expected_type=type_hints["logzio_kinesis_lambda_kinesis_stream"])
            check_type(argname="argument logzio_kinesis_lambda_role", value=logzio_kinesis_lambda_role, expected_type=type_hints["logzio_kinesis_lambda_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if logzio_kinesis_lambda is not None:
            self._values["logzio_kinesis_lambda"] = logzio_kinesis_lambda
        if logzio_kinesis_lambda_kinesis_stream is not None:
            self._values["logzio_kinesis_lambda_kinesis_stream"] = logzio_kinesis_lambda_kinesis_stream
        if logzio_kinesis_lambda_role is not None:
            self._values["logzio_kinesis_lambda_role"] = logzio_kinesis_lambda_role

    @builtins.property
    def logzio_kinesis_lambda(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda"]:
        '''
        :schema: CfnKinesisShipperModulePropsResources#LogzioKinesisLambda
        '''
        result = self._values.get("logzio_kinesis_lambda")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda"], result)

    @builtins.property
    def logzio_kinesis_lambda_kinesis_stream(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream"]:
        '''
        :schema: CfnKinesisShipperModulePropsResources#LogzioKinesisLambdaKinesisStream
        '''
        result = self._values.get("logzio_kinesis_lambda_kinesis_stream")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream"], result)

    @builtins.property
    def logzio_kinesis_lambda_role(
        self,
    ) -> typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole"]:
        '''
        :schema: CfnKinesisShipperModulePropsResources#LogzioKinesisLambdaRole
        '''
        result = self._values.get("logzio_kinesis_lambda_role")
        return typing.cast(typing.Optional["CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9526c3ece3bc9ca71f720f0e0796c9eacf71b7438753e3860756d224e0d7c26e)
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
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069abb743869d0e2acd508b5a8272ed99f8003c89334d773338f8f1692c84254)
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
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-kinesisshipper-kinesisshipper-module.CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f68d9d362767f3e07e17b0f56d2522bfee2ddda55eb66721ac035b822b658f4)
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
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnKinesisShipperModule",
    "CfnKinesisShipperModuleProps",
    "CfnKinesisShipperModulePropsParameters",
    "CfnKinesisShipperModulePropsParametersKinesisStream",
    "CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize",
    "CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition",
    "CfnKinesisShipperModulePropsParametersLogzioCompress",
    "CfnKinesisShipperModulePropsParametersLogzioFormat",
    "CfnKinesisShipperModulePropsParametersLogzioMessagesArray",
    "CfnKinesisShipperModulePropsParametersLogzioRegion",
    "CfnKinesisShipperModulePropsParametersLogzioToken",
    "CfnKinesisShipperModulePropsParametersLogzioType",
    "CfnKinesisShipperModulePropsParametersLogzioUrl",
    "CfnKinesisShipperModulePropsResources",
    "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda",
    "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream",
    "CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole",
]

publication.publish()

def _typecheckingstub__ba88c40e6c27cf492c17753994ec92c0c7116088c57aabfeef9e28f288a1c6ac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnKinesisShipperModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1846119ad587f0f61cfbc68e2f4660f516ae197a20e9f7cf98b53eb6fa3e8c52(
    *,
    parameters: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnKinesisShipperModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be5f03060577c131f9ff20ba9e5df8072156d4abd2780c4df3a2c8653b547499(
    *,
    kinesis_stream: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersKinesisStream, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_stream_batch_size: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersKinesisStreamBatchSize, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_stream_starting_position: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersKinesisStreamStartingPosition, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_compress: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersLogzioCompress, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_format: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersLogzioFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_messages_array: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersLogzioMessagesArray, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_region: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersLogzioRegion, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_token: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersLogzioToken, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_type: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersLogzioType, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_url: typing.Optional[typing.Union[CfnKinesisShipperModulePropsParametersLogzioUrl, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe11575b61431e352ab757d4ddc131585cddf57410c3b8226d79004f0c4c1f6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d42f65000f24d44f19a7b0bd162c9d77bf0e96ffab0bb7b8ff4d85a80191142(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8da2bb88b2188bf8e5ec1fb95680638880925b507d69eb7a543714fdcbc27ee(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__644eccbd5c4897ff0c5fc1b2497fbc5281119e6e2ce3d35ad403b0fad1865c0e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c357b7c9b8a0f4df8bdaa8eedbffef38ab29887e80c81a70fe254936be68fa4f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2027fd2688c56d248177420d76f02829ce9b029f47ef26ebff3f17612c0cb17c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abb1555fcac945b483d8dbb49aa3b79d34c4c7d131a1fe956117f714f2d0a243(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b80e22e9385edf116bfcb9b085af05827bf2fc469a30595e7a9f893384f8cd7(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b4460c81da11229ede35829078bbad1d2bb29a9d100d6811f861e1834c1d9e3(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4998085d19cf921f410b9d26aea4eb5129f7c6f1ee256f0b291d1cd614c9770e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__245c1ea1efc5e2062940a21ff2830c7afad8c4d41bd4950e9a6e66d00c4f1c88(
    *,
    logzio_kinesis_lambda: typing.Optional[typing.Union[CfnKinesisShipperModulePropsResourcesLogzioKinesisLambda, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_kinesis_lambda_kinesis_stream: typing.Optional[typing.Union[CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaKinesisStream, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_kinesis_lambda_role: typing.Optional[typing.Union[CfnKinesisShipperModulePropsResourcesLogzioKinesisLambdaRole, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9526c3ece3bc9ca71f720f0e0796c9eacf71b7438753e3860756d224e0d7c26e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069abb743869d0e2acd508b5a8272ed99f8003c89334d773338f8f1692c84254(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f68d9d362767f3e07e17b0f56d2522bfee2ddda55eb66721ac035b822b658f4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
