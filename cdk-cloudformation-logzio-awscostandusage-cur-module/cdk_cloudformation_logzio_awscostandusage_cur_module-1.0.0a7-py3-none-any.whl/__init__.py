'''
# logzio-awscostandusage-cur-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Logzio::awsCostAndUsage::cur::MODULE` v1.0.0.

## Description

Schema for Module Fragment of type Logzio::awsCostAndUsage::cur::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Logzio::awsCostAndUsage::cur::MODULE \
  --publisher-id 8a9caf0628707da0ff455be490fd366079c8223e \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/8a9caf0628707da0ff455be490fd366079c8223e/Logzio-awsCostAndUsage-cur-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Logzio::awsCostAndUsage::cur::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Flogzio-awscostandusage-cur-module+v1.0.0).
* Issues related to `Logzio::awsCostAndUsage::cur::MODULE` should be reported to the [publisher](undefined).

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


class CfnCurModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModule",
):
    '''A CloudFormation ``Logzio::awsCostAndUsage::cur::MODULE``.

    :cloudformationResource: Logzio::awsCostAndUsage::cur::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnCurModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCurModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Logzio::awsCostAndUsage::cur::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49905357161a97d5745462d13062e78f3049e60b2f40276176763617721af9dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCurModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnCurModuleProps":
        '''Resource props.'''
        return typing.cast("CfnCurModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnCurModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnCurModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnCurModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type Logzio::awsCostAndUsage::cur::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnCurModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnCurModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnCurModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d88db912f3425964ee978994d793518be04e409a976ba1a7534b8b08a8407184)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnCurModulePropsParameters"]:
        '''
        :schema: CfnCurModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnCurModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnCurModulePropsResources"]:
        '''
        :schema: CfnCurModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnCurModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_watch_event_schedule_expression": "cloudWatchEventScheduleExpression",
        "lambda_memory_size": "lambdaMemorySize",
        "lambda_timeout": "lambdaTimeout",
        "logzio_token": "logzioToken",
        "logzio_url": "logzioUrl",
        "report_additional_schema_elements": "reportAdditionalSchemaElements",
        "report_name": "reportName",
        "report_prefix": "reportPrefix",
        "report_time_unit": "reportTimeUnit",
        "s3_bucket_name": "s3BucketName",
    },
)
class CfnCurModulePropsParameters:
    def __init__(
        self,
        *,
        cloud_watch_event_schedule_expression: typing.Optional[typing.Union["CfnCurModulePropsParametersCloudWatchEventScheduleExpression", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_memory_size: typing.Optional[typing.Union["CfnCurModulePropsParametersLambdaMemorySize", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_timeout: typing.Optional[typing.Union["CfnCurModulePropsParametersLambdaTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_token: typing.Optional[typing.Union["CfnCurModulePropsParametersLogzioToken", typing.Dict[builtins.str, typing.Any]]] = None,
        logzio_url: typing.Optional[typing.Union["CfnCurModulePropsParametersLogzioUrl", typing.Dict[builtins.str, typing.Any]]] = None,
        report_additional_schema_elements: typing.Optional[typing.Union["CfnCurModulePropsParametersReportAdditionalSchemaElements", typing.Dict[builtins.str, typing.Any]]] = None,
        report_name: typing.Optional[typing.Union["CfnCurModulePropsParametersReportName", typing.Dict[builtins.str, typing.Any]]] = None,
        report_prefix: typing.Optional[typing.Union["CfnCurModulePropsParametersReportPrefix", typing.Dict[builtins.str, typing.Any]]] = None,
        report_time_unit: typing.Optional[typing.Union["CfnCurModulePropsParametersReportTimeUnit", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket_name: typing.Optional[typing.Union["CfnCurModulePropsParametersS3BucketName", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_watch_event_schedule_expression: The scheduling expression that determines when and how often the Lambda function runs. We recommend to start with 10 hour rate.
        :param lambda_memory_size: The amount of memory available to the function at runtime. Increasing the function memory also increases its CPU allocation. The value can be multiple of 1 MB. Minimum value is 128 MB and Maximum value is 10240 MB. We recommend to start with 1024 MB.
        :param lambda_timeout: The amount of time that Lambda allows a function to run before stopping it. Minimum value is 1 second and Maximum value is 900 seconds. We recommend to start with 300 seconds (5 minutes).
        :param logzio_token: Your Logz.io logs token. (Can be retrieved from the Manage Token page.).
        :param logzio_url: The Logz.io listener URL fot your region. (For more details, see the regions page: https://docs.logz.io/user-guide/accounts/account-region.html).
        :param report_additional_schema_elements: Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase report size and might affect performance. AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.), or DON'T INCLUDE otherwise.
        :param report_name: The name of report that you want to create. The name must be unique, is case sensitive and can't include spaces.
        :param report_prefix: The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.
        :param report_time_unit: The granularity of the line items in the report. (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.)
        :param s3_bucket_name: The name for the bucket which will contain the report files. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-), and must follow Amazon S3 bucket restrictions and limitations.

        :schema: CfnCurModulePropsParameters
        '''
        if isinstance(cloud_watch_event_schedule_expression, dict):
            cloud_watch_event_schedule_expression = CfnCurModulePropsParametersCloudWatchEventScheduleExpression(**cloud_watch_event_schedule_expression)
        if isinstance(lambda_memory_size, dict):
            lambda_memory_size = CfnCurModulePropsParametersLambdaMemorySize(**lambda_memory_size)
        if isinstance(lambda_timeout, dict):
            lambda_timeout = CfnCurModulePropsParametersLambdaTimeout(**lambda_timeout)
        if isinstance(logzio_token, dict):
            logzio_token = CfnCurModulePropsParametersLogzioToken(**logzio_token)
        if isinstance(logzio_url, dict):
            logzio_url = CfnCurModulePropsParametersLogzioUrl(**logzio_url)
        if isinstance(report_additional_schema_elements, dict):
            report_additional_schema_elements = CfnCurModulePropsParametersReportAdditionalSchemaElements(**report_additional_schema_elements)
        if isinstance(report_name, dict):
            report_name = CfnCurModulePropsParametersReportName(**report_name)
        if isinstance(report_prefix, dict):
            report_prefix = CfnCurModulePropsParametersReportPrefix(**report_prefix)
        if isinstance(report_time_unit, dict):
            report_time_unit = CfnCurModulePropsParametersReportTimeUnit(**report_time_unit)
        if isinstance(s3_bucket_name, dict):
            s3_bucket_name = CfnCurModulePropsParametersS3BucketName(**s3_bucket_name)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce241f1dbe9c2db5b90a074e6fb67b6b9061f330906a6eef6bee78fc7b38731)
            check_type(argname="argument cloud_watch_event_schedule_expression", value=cloud_watch_event_schedule_expression, expected_type=type_hints["cloud_watch_event_schedule_expression"])
            check_type(argname="argument lambda_memory_size", value=lambda_memory_size, expected_type=type_hints["lambda_memory_size"])
            check_type(argname="argument lambda_timeout", value=lambda_timeout, expected_type=type_hints["lambda_timeout"])
            check_type(argname="argument logzio_token", value=logzio_token, expected_type=type_hints["logzio_token"])
            check_type(argname="argument logzio_url", value=logzio_url, expected_type=type_hints["logzio_url"])
            check_type(argname="argument report_additional_schema_elements", value=report_additional_schema_elements, expected_type=type_hints["report_additional_schema_elements"])
            check_type(argname="argument report_name", value=report_name, expected_type=type_hints["report_name"])
            check_type(argname="argument report_prefix", value=report_prefix, expected_type=type_hints["report_prefix"])
            check_type(argname="argument report_time_unit", value=report_time_unit, expected_type=type_hints["report_time_unit"])
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloud_watch_event_schedule_expression is not None:
            self._values["cloud_watch_event_schedule_expression"] = cloud_watch_event_schedule_expression
        if lambda_memory_size is not None:
            self._values["lambda_memory_size"] = lambda_memory_size
        if lambda_timeout is not None:
            self._values["lambda_timeout"] = lambda_timeout
        if logzio_token is not None:
            self._values["logzio_token"] = logzio_token
        if logzio_url is not None:
            self._values["logzio_url"] = logzio_url
        if report_additional_schema_elements is not None:
            self._values["report_additional_schema_elements"] = report_additional_schema_elements
        if report_name is not None:
            self._values["report_name"] = report_name
        if report_prefix is not None:
            self._values["report_prefix"] = report_prefix
        if report_time_unit is not None:
            self._values["report_time_unit"] = report_time_unit
        if s3_bucket_name is not None:
            self._values["s3_bucket_name"] = s3_bucket_name

    @builtins.property
    def cloud_watch_event_schedule_expression(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersCloudWatchEventScheduleExpression"]:
        '''The scheduling expression that determines when and how often the Lambda function runs.

        We recommend to start with 10 hour rate.

        :schema: CfnCurModulePropsParameters#CloudWatchEventScheduleExpression
        '''
        result = self._values.get("cloud_watch_event_schedule_expression")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersCloudWatchEventScheduleExpression"], result)

    @builtins.property
    def lambda_memory_size(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersLambdaMemorySize"]:
        '''The amount of memory available to the function at runtime.

        Increasing the function memory also increases its CPU allocation. The value can be multiple of 1 MB. Minimum value is 128 MB and Maximum value is 10240 MB. We recommend to start with 1024 MB.

        :schema: CfnCurModulePropsParameters#LambdaMemorySize
        '''
        result = self._values.get("lambda_memory_size")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersLambdaMemorySize"], result)

    @builtins.property
    def lambda_timeout(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersLambdaTimeout"]:
        '''The amount of time that Lambda allows a function to run before stopping it.

        Minimum value is 1 second and Maximum value is 900 seconds. We recommend to start with 300 seconds (5 minutes).

        :schema: CfnCurModulePropsParameters#LambdaTimeout
        '''
        result = self._values.get("lambda_timeout")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersLambdaTimeout"], result)

    @builtins.property
    def logzio_token(self) -> typing.Optional["CfnCurModulePropsParametersLogzioToken"]:
        '''Your Logz.io logs token. (Can be retrieved from the Manage Token page.).

        :schema: CfnCurModulePropsParameters#LogzioToken
        '''
        result = self._values.get("logzio_token")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersLogzioToken"], result)

    @builtins.property
    def logzio_url(self) -> typing.Optional["CfnCurModulePropsParametersLogzioUrl"]:
        '''The Logz.io listener URL fot your region. (For more details, see the regions page:  https://docs.logz.io/user-guide/accounts/account-region.html).

        :schema: CfnCurModulePropsParameters#LogzioURL
        '''
        result = self._values.get("logzio_url")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersLogzioUrl"], result)

    @builtins.property
    def report_additional_schema_elements(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersReportAdditionalSchemaElements"]:
        '''Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase report size and might affect performance.

        AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.), or DON'T INCLUDE otherwise.

        :schema: CfnCurModulePropsParameters#ReportAdditionalSchemaElements
        '''
        result = self._values.get("report_additional_schema_elements")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersReportAdditionalSchemaElements"], result)

    @builtins.property
    def report_name(self) -> typing.Optional["CfnCurModulePropsParametersReportName"]:
        '''The name of report that you want to create.

        The name must be unique, is case sensitive and can't include spaces.

        :schema: CfnCurModulePropsParameters#ReportName
        '''
        result = self._values.get("report_name")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersReportName"], result)

    @builtins.property
    def report_prefix(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersReportPrefix"]:
        '''The prefix that AWS adds to the report name when AWS delivers the report.

        Your prefix can't include spaces.

        :schema: CfnCurModulePropsParameters#ReportPrefix
        '''
        result = self._values.get("report_prefix")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersReportPrefix"], result)

    @builtins.property
    def report_time_unit(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersReportTimeUnit"]:
        '''The granularity of the line items in the report.

        (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.)

        :schema: CfnCurModulePropsParameters#ReportTimeUnit
        '''
        result = self._values.get("report_time_unit")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersReportTimeUnit"], result)

    @builtins.property
    def s3_bucket_name(
        self,
    ) -> typing.Optional["CfnCurModulePropsParametersS3BucketName"]:
        '''The name for the bucket which will contain the report files.

        The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-), and must follow Amazon S3 bucket restrictions and limitations.

        :schema: CfnCurModulePropsParameters#S3BucketName
        '''
        result = self._values.get("s3_bucket_name")
        return typing.cast(typing.Optional["CfnCurModulePropsParametersS3BucketName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersCloudWatchEventScheduleExpression",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersCloudWatchEventScheduleExpression:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The scheduling expression that determines when and how often the Lambda function runs.

        We recommend to start with 10 hour rate.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersCloudWatchEventScheduleExpression
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0feaf4ac3cd6962ae22503a3fcf334412ba16a2bfe06451c9088eaf129c2b14)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersCloudWatchEventScheduleExpression#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersCloudWatchEventScheduleExpression#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersCloudWatchEventScheduleExpression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersLambdaMemorySize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersLambdaMemorySize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The amount of memory available to the function at runtime.

        Increasing the function memory also increases its CPU allocation. The value can be multiple of 1 MB. Minimum value is 128 MB and Maximum value is 10240 MB. We recommend to start with 1024 MB.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersLambdaMemorySize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce772b739e22f167bb25b494bba5fd06b6b30b0e33d4a6777b49a16360bd55e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLambdaMemorySize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLambdaMemorySize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersLambdaMemorySize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersLambdaTimeout",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersLambdaTimeout:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The amount of time that Lambda allows a function to run before stopping it.

        Minimum value is 1 second and Maximum value is 900 seconds. We recommend to start with 300 seconds (5 minutes).

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersLambdaTimeout
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f8686218e3b10abbb0b6d5d8d4f3c4b4d98fb97d39c6cbc57fb6800adc8cdbd)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLambdaTimeout#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLambdaTimeout#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersLambdaTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersLogzioToken",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersLogzioToken:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Your Logz.io logs token. (Can be retrieved from the Manage Token page.).

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersLogzioToken
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eac6ea62f5728d34f4c5957016f5b7d49c5164afcb755578604ed91bc76e3a87)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLogzioToken#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLogzioToken#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersLogzioToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersLogzioUrl",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersLogzioUrl:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Logz.io listener URL fot your region. (For more details, see the regions page:  https://docs.logz.io/user-guide/accounts/account-region.html).

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersLogzioUrl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__243dbd12337fe1dea600f2963507e29e8ed5da2be8230488345789656baeb02e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLogzioUrl#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersLogzioUrl#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersLogzioUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersReportAdditionalSchemaElements",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersReportAdditionalSchemaElements:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose INCLUDE if you want AWS to include additional details about individual resources IDs in the report (This might significantly increase report size and might affect performance.

        AWS Lambda can run for up to 15 minutes with up to 10240 MB, and the process time for the whole file must end within this timeframe.), or DON'T INCLUDE otherwise.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersReportAdditionalSchemaElements
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59570924c8bc62c3364bd80d2acb3ca27e14b8410be4aba8720f78dc6cf9d2d8)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportAdditionalSchemaElements#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportAdditionalSchemaElements#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersReportAdditionalSchemaElements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersReportName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersReportName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The name of report that you want to create.

        The name must be unique, is case sensitive and can't include spaces.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersReportName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3366dfab43ab1076e5a863af2308fa652cd492791ac96dd9eecef46c06b8a15)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersReportName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersReportPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersReportPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The prefix that AWS adds to the report name when AWS delivers the report.

        Your prefix can't include spaces.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersReportPrefix
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77e0b632a92dd2ff09ae0a995636c355944909baf81d5d2cd620744bde6bc213)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersReportPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersReportTimeUnit",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersReportTimeUnit:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The granularity of the line items in the report.

        (Enabling hourly reports does not mean that a new report is generated every hour. It means that data in the report is aggregated with a granularity of one hour.)

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersReportTimeUnit
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11bf4aacae136a32153f5ce2901776770a8a01da5f8bee67788886bdb198f8a9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportTimeUnit#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersReportTimeUnit#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersReportTimeUnit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsParametersS3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnCurModulePropsParametersS3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The name for the bucket which will contain the report files.

        The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-), and must follow Amazon S3 bucket restrictions and limitations.

        :param description: 
        :param type: 

        :schema: CfnCurModulePropsParametersS3BucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5e5a49ba8c46d057a4c5453df7f1da93fd555fd72384b80a1efd7a1febf50e3)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersS3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnCurModulePropsParametersS3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsParametersS3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "cur": "cur",
        "event_rule": "eventRule",
        "iam_role": "iamRole",
        "lambda_function": "lambdaFunction",
        "lambda_permission": "lambdaPermission",
        "s3_bucket": "s3Bucket",
        "s3_bucket_policy": "s3BucketPolicy",
    },
)
class CfnCurModulePropsResources:
    def __init__(
        self,
        *,
        cur: typing.Optional[typing.Union["CfnCurModulePropsResourcesCur", typing.Dict[builtins.str, typing.Any]]] = None,
        event_rule: typing.Optional[typing.Union["CfnCurModulePropsResourcesEventRule", typing.Dict[builtins.str, typing.Any]]] = None,
        iam_role: typing.Optional[typing.Union["CfnCurModulePropsResourcesIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_function: typing.Optional[typing.Union["CfnCurModulePropsResourcesLambdaFunction", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_permission: typing.Optional[typing.Union["CfnCurModulePropsResourcesLambdaPermission", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket: typing.Optional[typing.Union["CfnCurModulePropsResourcesS3Bucket", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket_policy: typing.Optional[typing.Union["CfnCurModulePropsResourcesS3BucketPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cur: 
        :param event_rule: 
        :param iam_role: 
        :param lambda_function: 
        :param lambda_permission: 
        :param s3_bucket: 
        :param s3_bucket_policy: 

        :schema: CfnCurModulePropsResources
        '''
        if isinstance(cur, dict):
            cur = CfnCurModulePropsResourcesCur(**cur)
        if isinstance(event_rule, dict):
            event_rule = CfnCurModulePropsResourcesEventRule(**event_rule)
        if isinstance(iam_role, dict):
            iam_role = CfnCurModulePropsResourcesIamRole(**iam_role)
        if isinstance(lambda_function, dict):
            lambda_function = CfnCurModulePropsResourcesLambdaFunction(**lambda_function)
        if isinstance(lambda_permission, dict):
            lambda_permission = CfnCurModulePropsResourcesLambdaPermission(**lambda_permission)
        if isinstance(s3_bucket, dict):
            s3_bucket = CfnCurModulePropsResourcesS3Bucket(**s3_bucket)
        if isinstance(s3_bucket_policy, dict):
            s3_bucket_policy = CfnCurModulePropsResourcesS3BucketPolicy(**s3_bucket_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a865c7008fe0d7e00136667abf6f007fda47632af99cac613e00523dc024468)
            check_type(argname="argument cur", value=cur, expected_type=type_hints["cur"])
            check_type(argname="argument event_rule", value=event_rule, expected_type=type_hints["event_rule"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
            check_type(argname="argument lambda_permission", value=lambda_permission, expected_type=type_hints["lambda_permission"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument s3_bucket_policy", value=s3_bucket_policy, expected_type=type_hints["s3_bucket_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cur is not None:
            self._values["cur"] = cur
        if event_rule is not None:
            self._values["event_rule"] = event_rule
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if lambda_function is not None:
            self._values["lambda_function"] = lambda_function
        if lambda_permission is not None:
            self._values["lambda_permission"] = lambda_permission
        if s3_bucket is not None:
            self._values["s3_bucket"] = s3_bucket
        if s3_bucket_policy is not None:
            self._values["s3_bucket_policy"] = s3_bucket_policy

    @builtins.property
    def cur(self) -> typing.Optional["CfnCurModulePropsResourcesCur"]:
        '''
        :schema: CfnCurModulePropsResources#CUR
        '''
        result = self._values.get("cur")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesCur"], result)

    @builtins.property
    def event_rule(self) -> typing.Optional["CfnCurModulePropsResourcesEventRule"]:
        '''
        :schema: CfnCurModulePropsResources#EventRule
        '''
        result = self._values.get("event_rule")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesEventRule"], result)

    @builtins.property
    def iam_role(self) -> typing.Optional["CfnCurModulePropsResourcesIamRole"]:
        '''
        :schema: CfnCurModulePropsResources#IAMRole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesIamRole"], result)

    @builtins.property
    def lambda_function(
        self,
    ) -> typing.Optional["CfnCurModulePropsResourcesLambdaFunction"]:
        '''
        :schema: CfnCurModulePropsResources#LambdaFunction
        '''
        result = self._values.get("lambda_function")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesLambdaFunction"], result)

    @builtins.property
    def lambda_permission(
        self,
    ) -> typing.Optional["CfnCurModulePropsResourcesLambdaPermission"]:
        '''
        :schema: CfnCurModulePropsResources#LambdaPermission
        '''
        result = self._values.get("lambda_permission")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesLambdaPermission"], result)

    @builtins.property
    def s3_bucket(self) -> typing.Optional["CfnCurModulePropsResourcesS3Bucket"]:
        '''
        :schema: CfnCurModulePropsResources#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesS3Bucket"], result)

    @builtins.property
    def s3_bucket_policy(
        self,
    ) -> typing.Optional["CfnCurModulePropsResourcesS3BucketPolicy"]:
        '''
        :schema: CfnCurModulePropsResources#S3BucketPolicy
        '''
        result = self._values.get("s3_bucket_policy")
        return typing.cast(typing.Optional["CfnCurModulePropsResourcesS3BucketPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesCur",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesCur:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesCur
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4724cf106ca53d9f9574ed66dbdf30b900cb506256ca53d6a82daf59fc6645)
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
        :schema: CfnCurModulePropsResourcesCur#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesCur#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesCur(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesEventRule",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesEventRule:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesEventRule
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e439b4ac2e01d3f5050c355c7967b32d5b612c73ece62a89e57b9faa12d4b626)
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
        :schema: CfnCurModulePropsResourcesEventRule#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesEventRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesEventRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesIamRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesIamRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesIamRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__361cd29084788acafc689cb5ce803f0f1d0ce9656086e3244fac8689adf56c16)
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
        :schema: CfnCurModulePropsResourcesIamRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesIamRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesLambdaFunction",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesLambdaFunction:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesLambdaFunction
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f5cb2393915fa5b00903ffa13ea6e1960fdd9b9d5afe1b1f3a215901086afe9)
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
        :schema: CfnCurModulePropsResourcesLambdaFunction#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesLambdaFunction#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesLambdaFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesLambdaPermission",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesLambdaPermission:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesLambdaPermission
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b11436164fda76519f713e9ba4b509c397f0cfdb0ef5ec149bfa8a934e365281)
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
        :schema: CfnCurModulePropsResourcesLambdaPermission#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesLambdaPermission#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesLambdaPermission(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesS3Bucket",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesS3Bucket:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesS3Bucket
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e76e7af767c363f590dfc507073825718c8188a0f5d98154904be8d7682c974)
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
        :schema: CfnCurModulePropsResourcesS3Bucket#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesS3Bucket#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesS3Bucket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/logzio-awscostandusage-cur-module.CfnCurModulePropsResourcesS3BucketPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnCurModulePropsResourcesS3BucketPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnCurModulePropsResourcesS3BucketPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1360a4811c164cbe5d92eade0f4a7821eb63f8dbe4e5bfc6b1afe341f35d039)
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
        :schema: CfnCurModulePropsResourcesS3BucketPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnCurModulePropsResourcesS3BucketPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCurModulePropsResourcesS3BucketPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCurModule",
    "CfnCurModuleProps",
    "CfnCurModulePropsParameters",
    "CfnCurModulePropsParametersCloudWatchEventScheduleExpression",
    "CfnCurModulePropsParametersLambdaMemorySize",
    "CfnCurModulePropsParametersLambdaTimeout",
    "CfnCurModulePropsParametersLogzioToken",
    "CfnCurModulePropsParametersLogzioUrl",
    "CfnCurModulePropsParametersReportAdditionalSchemaElements",
    "CfnCurModulePropsParametersReportName",
    "CfnCurModulePropsParametersReportPrefix",
    "CfnCurModulePropsParametersReportTimeUnit",
    "CfnCurModulePropsParametersS3BucketName",
    "CfnCurModulePropsResources",
    "CfnCurModulePropsResourcesCur",
    "CfnCurModulePropsResourcesEventRule",
    "CfnCurModulePropsResourcesIamRole",
    "CfnCurModulePropsResourcesLambdaFunction",
    "CfnCurModulePropsResourcesLambdaPermission",
    "CfnCurModulePropsResourcesS3Bucket",
    "CfnCurModulePropsResourcesS3BucketPolicy",
]

publication.publish()

def _typecheckingstub__49905357161a97d5745462d13062e78f3049e60b2f40276176763617721af9dc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnCurModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCurModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88db912f3425964ee978994d793518be04e409a976ba1a7534b8b08a8407184(
    *,
    parameters: typing.Optional[typing.Union[CfnCurModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnCurModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce241f1dbe9c2db5b90a074e6fb67b6b9061f330906a6eef6bee78fc7b38731(
    *,
    cloud_watch_event_schedule_expression: typing.Optional[typing.Union[CfnCurModulePropsParametersCloudWatchEventScheduleExpression, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_memory_size: typing.Optional[typing.Union[CfnCurModulePropsParametersLambdaMemorySize, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_timeout: typing.Optional[typing.Union[CfnCurModulePropsParametersLambdaTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_token: typing.Optional[typing.Union[CfnCurModulePropsParametersLogzioToken, typing.Dict[builtins.str, typing.Any]]] = None,
    logzio_url: typing.Optional[typing.Union[CfnCurModulePropsParametersLogzioUrl, typing.Dict[builtins.str, typing.Any]]] = None,
    report_additional_schema_elements: typing.Optional[typing.Union[CfnCurModulePropsParametersReportAdditionalSchemaElements, typing.Dict[builtins.str, typing.Any]]] = None,
    report_name: typing.Optional[typing.Union[CfnCurModulePropsParametersReportName, typing.Dict[builtins.str, typing.Any]]] = None,
    report_prefix: typing.Optional[typing.Union[CfnCurModulePropsParametersReportPrefix, typing.Dict[builtins.str, typing.Any]]] = None,
    report_time_unit: typing.Optional[typing.Union[CfnCurModulePropsParametersReportTimeUnit, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket_name: typing.Optional[typing.Union[CfnCurModulePropsParametersS3BucketName, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0feaf4ac3cd6962ae22503a3fcf334412ba16a2bfe06451c9088eaf129c2b14(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce772b739e22f167bb25b494bba5fd06b6b30b0e33d4a6777b49a16360bd55e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8686218e3b10abbb0b6d5d8d4f3c4b4d98fb97d39c6cbc57fb6800adc8cdbd(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eac6ea62f5728d34f4c5957016f5b7d49c5164afcb755578604ed91bc76e3a87(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__243dbd12337fe1dea600f2963507e29e8ed5da2be8230488345789656baeb02e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59570924c8bc62c3364bd80d2acb3ca27e14b8410be4aba8720f78dc6cf9d2d8(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3366dfab43ab1076e5a863af2308fa652cd492791ac96dd9eecef46c06b8a15(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77e0b632a92dd2ff09ae0a995636c355944909baf81d5d2cd620744bde6bc213(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11bf4aacae136a32153f5ce2901776770a8a01da5f8bee67788886bdb198f8a9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e5a49ba8c46d057a4c5453df7f1da93fd555fd72384b80a1efd7a1febf50e3(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a865c7008fe0d7e00136667abf6f007fda47632af99cac613e00523dc024468(
    *,
    cur: typing.Optional[typing.Union[CfnCurModulePropsResourcesCur, typing.Dict[builtins.str, typing.Any]]] = None,
    event_rule: typing.Optional[typing.Union[CfnCurModulePropsResourcesEventRule, typing.Dict[builtins.str, typing.Any]]] = None,
    iam_role: typing.Optional[typing.Union[CfnCurModulePropsResourcesIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_function: typing.Optional[typing.Union[CfnCurModulePropsResourcesLambdaFunction, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_permission: typing.Optional[typing.Union[CfnCurModulePropsResourcesLambdaPermission, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket: typing.Optional[typing.Union[CfnCurModulePropsResourcesS3Bucket, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket_policy: typing.Optional[typing.Union[CfnCurModulePropsResourcesS3BucketPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4724cf106ca53d9f9574ed66dbdf30b900cb506256ca53d6a82daf59fc6645(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e439b4ac2e01d3f5050c355c7967b32d5b612c73ece62a89e57b9faa12d4b626(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__361cd29084788acafc689cb5ce803f0f1d0ce9656086e3244fac8689adf56c16(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f5cb2393915fa5b00903ffa13ea6e1960fdd9b9d5afe1b1f3a215901086afe9(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b11436164fda76519f713e9ba4b509c397f0cfdb0ef5ec149bfa8a934e365281(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e76e7af767c363f590dfc507073825718c8188a0f5d98154904be8d7682c974(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1360a4811c164cbe5d92eade0f4a7821eb63f8dbe4e5bfc6b1afe341f35d039(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
