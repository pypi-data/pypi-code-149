'''
# paloaltonetworks-cloudngfw-ngfw

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `PaloAltoNetworks::CloudNGFW::NGFW` v1.0.0.

## Description

A Firewall resource offers Palo Alto Networks next-generation firewall capabilities with built-in resiliency, scalability, and life-cycle management.

## References

* [Source](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name PaloAltoNetworks::CloudNGFW::NGFW \
  --publisher-id 4e4cf7d0eb3aa7334767bc17a1dbec7e8279d078 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/4e4cf7d0eb3aa7334767bc17a1dbec7e8279d078/PaloAltoNetworks-CloudNGFW-NGFW \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `PaloAltoNetworks::CloudNGFW::NGFW`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fpaloaltonetworks-cloudngfw-ngfw+v1.0.0).
* Issues related to `PaloAltoNetworks::CloudNGFW::NGFW` should be reported to the [publisher](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git).

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


class CfnNgfw(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/paloaltonetworks-cloudngfw-ngfw.CfnNgfw",
):
    '''A CloudFormation ``PaloAltoNetworks::CloudNGFW::NGFW``.

    :cloudformationResource: PaloAltoNetworks::CloudNGFW::NGFW
    :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        endpoint_mode: "CfnNgfwPropsEndpointMode",
        firewall_name: builtins.str,
        log_destination_configs: typing.Sequence[typing.Union["LogProfileConfig", typing.Dict[builtins.str, typing.Any]]],
        programmatic_access_token: builtins.str,
        subnet_mappings: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        app_id_version: typing.Optional[builtins.str] = None,
        automatic_upgrade_app_id_version: typing.Optional[builtins.bool] = None,
        cloud_watch_metric_namespace: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        rule_stack_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''Create a new ``PaloAltoNetworks::CloudNGFW::NGFW``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_mode: 
        :param firewall_name: 
        :param log_destination_configs: 
        :param programmatic_access_token: 
        :param subnet_mappings: 
        :param vpc_id: 
        :param app_id_version: 
        :param automatic_upgrade_app_id_version: 
        :param cloud_watch_metric_namespace: 
        :param description: 
        :param rule_stack_name: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a44e34122d63b2e649e1a0cf59f5d48094ce3838d16dfa68e3cc9200b395326e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNgfwProps(
            endpoint_mode=endpoint_mode,
            firewall_name=firewall_name,
            log_destination_configs=log_destination_configs,
            programmatic_access_token=programmatic_access_token,
            subnet_mappings=subnet_mappings,
            vpc_id=vpc_id,
            app_id_version=app_id_version,
            automatic_upgrade_app_id_version=automatic_upgrade_app_id_version,
            cloud_watch_metric_namespace=cloud_watch_metric_namespace,
            description=description,
            rule_stack_name=rule_stack_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnNgfwProps":
        '''Resource props.'''
        return typing.cast("CfnNgfwProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/paloaltonetworks-cloudngfw-ngfw.CfnNgfwProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_mode": "endpointMode",
        "firewall_name": "firewallName",
        "log_destination_configs": "logDestinationConfigs",
        "programmatic_access_token": "programmaticAccessToken",
        "subnet_mappings": "subnetMappings",
        "vpc_id": "vpcId",
        "app_id_version": "appIdVersion",
        "automatic_upgrade_app_id_version": "automaticUpgradeAppIdVersion",
        "cloud_watch_metric_namespace": "cloudWatchMetricNamespace",
        "description": "description",
        "rule_stack_name": "ruleStackName",
        "tags": "tags",
    },
)
class CfnNgfwProps:
    def __init__(
        self,
        *,
        endpoint_mode: "CfnNgfwPropsEndpointMode",
        firewall_name: builtins.str,
        log_destination_configs: typing.Sequence[typing.Union["LogProfileConfig", typing.Dict[builtins.str, typing.Any]]],
        programmatic_access_token: builtins.str,
        subnet_mappings: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        app_id_version: typing.Optional[builtins.str] = None,
        automatic_upgrade_app_id_version: typing.Optional[builtins.bool] = None,
        cloud_watch_metric_namespace: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        rule_stack_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Any]] = None,
    ) -> None:
        '''A Firewall resource offers Palo Alto Networks next-generation firewall capabilities with built-in resiliency, scalability, and life-cycle management.

        :param endpoint_mode: 
        :param firewall_name: 
        :param log_destination_configs: 
        :param programmatic_access_token: 
        :param subnet_mappings: 
        :param vpc_id: 
        :param app_id_version: 
        :param automatic_upgrade_app_id_version: 
        :param cloud_watch_metric_namespace: 
        :param description: 
        :param rule_stack_name: 
        :param tags: 

        :schema: CfnNgfwProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__babd383745f46351db16da77dd426a0238262cf070da922071ca55f3a80af00b)
            check_type(argname="argument endpoint_mode", value=endpoint_mode, expected_type=type_hints["endpoint_mode"])
            check_type(argname="argument firewall_name", value=firewall_name, expected_type=type_hints["firewall_name"])
            check_type(argname="argument log_destination_configs", value=log_destination_configs, expected_type=type_hints["log_destination_configs"])
            check_type(argname="argument programmatic_access_token", value=programmatic_access_token, expected_type=type_hints["programmatic_access_token"])
            check_type(argname="argument subnet_mappings", value=subnet_mappings, expected_type=type_hints["subnet_mappings"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument app_id_version", value=app_id_version, expected_type=type_hints["app_id_version"])
            check_type(argname="argument automatic_upgrade_app_id_version", value=automatic_upgrade_app_id_version, expected_type=type_hints["automatic_upgrade_app_id_version"])
            check_type(argname="argument cloud_watch_metric_namespace", value=cloud_watch_metric_namespace, expected_type=type_hints["cloud_watch_metric_namespace"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument rule_stack_name", value=rule_stack_name, expected_type=type_hints["rule_stack_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_mode": endpoint_mode,
            "firewall_name": firewall_name,
            "log_destination_configs": log_destination_configs,
            "programmatic_access_token": programmatic_access_token,
            "subnet_mappings": subnet_mappings,
            "vpc_id": vpc_id,
        }
        if app_id_version is not None:
            self._values["app_id_version"] = app_id_version
        if automatic_upgrade_app_id_version is not None:
            self._values["automatic_upgrade_app_id_version"] = automatic_upgrade_app_id_version
        if cloud_watch_metric_namespace is not None:
            self._values["cloud_watch_metric_namespace"] = cloud_watch_metric_namespace
        if description is not None:
            self._values["description"] = description
        if rule_stack_name is not None:
            self._values["rule_stack_name"] = rule_stack_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def endpoint_mode(self) -> "CfnNgfwPropsEndpointMode":
        '''
        :schema: CfnNgfwProps#EndpointMode
        '''
        result = self._values.get("endpoint_mode")
        assert result is not None, "Required property 'endpoint_mode' is missing"
        return typing.cast("CfnNgfwPropsEndpointMode", result)

    @builtins.property
    def firewall_name(self) -> builtins.str:
        '''
        :schema: CfnNgfwProps#FirewallName
        '''
        result = self._values.get("firewall_name")
        assert result is not None, "Required property 'firewall_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_destination_configs(self) -> typing.List["LogProfileConfig"]:
        '''
        :schema: CfnNgfwProps#LogDestinationConfigs
        '''
        result = self._values.get("log_destination_configs")
        assert result is not None, "Required property 'log_destination_configs' is missing"
        return typing.cast(typing.List["LogProfileConfig"], result)

    @builtins.property
    def programmatic_access_token(self) -> builtins.str:
        '''
        :schema: CfnNgfwProps#ProgrammaticAccessToken
        '''
        result = self._values.get("programmatic_access_token")
        assert result is not None, "Required property 'programmatic_access_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_mappings(self) -> typing.List[builtins.str]:
        '''
        :schema: CfnNgfwProps#SubnetMappings
        '''
        result = self._values.get("subnet_mappings")
        assert result is not None, "Required property 'subnet_mappings' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''
        :schema: CfnNgfwProps#VpcId
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_id_version(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnNgfwProps#AppIdVersion
        '''
        result = self._values.get("app_id_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automatic_upgrade_app_id_version(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnNgfwProps#AutomaticUpgradeAppIdVersion
        '''
        result = self._values.get("automatic_upgrade_app_id_version")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cloud_watch_metric_namespace(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnNgfwProps#CloudWatchMetricNamespace
        '''
        result = self._values.get("cloud_watch_metric_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnNgfwProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_stack_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnNgfwProps#RuleStackName
        '''
        result = self._values.get("rule_stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[typing.Any]]:
        '''
        :schema: CfnNgfwProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNgfwProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/paloaltonetworks-cloudngfw-ngfw.CfnNgfwPropsEndpointMode"
)
class CfnNgfwPropsEndpointMode(enum.Enum):
    '''
    :schema: CfnNgfwPropsEndpointMode
    '''

    SERVICE_MANAGED = "SERVICE_MANAGED"
    '''ServiceManaged.'''
    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    '''CustomerManaged.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/paloaltonetworks-cloudngfw-ngfw.LogProfileConfig",
    jsii_struct_bases=[],
    name_mapping={
        "log_destination": "logDestination",
        "log_destination_type": "logDestinationType",
        "log_type": "logType",
    },
)
class LogProfileConfig:
    def __init__(
        self,
        *,
        log_destination: builtins.str,
        log_destination_type: "LogProfileConfigLogDestinationType",
        log_type: "LogProfileConfigLogType",
    ) -> None:
        '''Add Log profile config.

        :param log_destination: 
        :param log_destination_type: 
        :param log_type: 

        :schema: LogProfileConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecbd3e688630265a99392f1db06e9897764a78868a0e014666ab1b1ec9468311)
            check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
            check_type(argname="argument log_destination_type", value=log_destination_type, expected_type=type_hints["log_destination_type"])
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_destination": log_destination,
            "log_destination_type": log_destination_type,
            "log_type": log_type,
        }

    @builtins.property
    def log_destination(self) -> builtins.str:
        '''
        :schema: LogProfileConfig#LogDestination
        '''
        result = self._values.get("log_destination")
        assert result is not None, "Required property 'log_destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_destination_type(self) -> "LogProfileConfigLogDestinationType":
        '''
        :schema: LogProfileConfig#LogDestinationType
        '''
        result = self._values.get("log_destination_type")
        assert result is not None, "Required property 'log_destination_type' is missing"
        return typing.cast("LogProfileConfigLogDestinationType", result)

    @builtins.property
    def log_type(self) -> "LogProfileConfigLogType":
        '''
        :schema: LogProfileConfig#LogType
        '''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast("LogProfileConfigLogType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/paloaltonetworks-cloudngfw-ngfw.LogProfileConfigLogDestinationType"
)
class LogProfileConfigLogDestinationType(enum.Enum):
    '''
    :schema: LogProfileConfigLogDestinationType
    '''

    S3 = "S3"
    '''S3.'''
    CLOUD_WATCH_LOGS = "CLOUD_WATCH_LOGS"
    '''CloudWatchLogs.'''
    KINESIS_DATA_FIREHOSE = "KINESIS_DATA_FIREHOSE"
    '''KinesisDataFirehose.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/paloaltonetworks-cloudngfw-ngfw.LogProfileConfigLogType"
)
class LogProfileConfigLogType(enum.Enum):
    '''
    :schema: LogProfileConfigLogType
    '''

    TRAFFIC = "TRAFFIC"
    '''TRAFFIC.'''
    DECRYPTION = "DECRYPTION"
    '''DECRYPTION.'''
    THREAT = "THREAT"
    '''THREAT.'''


__all__ = [
    "CfnNgfw",
    "CfnNgfwProps",
    "CfnNgfwPropsEndpointMode",
    "LogProfileConfig",
    "LogProfileConfigLogDestinationType",
    "LogProfileConfigLogType",
]

publication.publish()

def _typecheckingstub__a44e34122d63b2e649e1a0cf59f5d48094ce3838d16dfa68e3cc9200b395326e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    endpoint_mode: CfnNgfwPropsEndpointMode,
    firewall_name: builtins.str,
    log_destination_configs: typing.Sequence[typing.Union[LogProfileConfig, typing.Dict[builtins.str, typing.Any]]],
    programmatic_access_token: builtins.str,
    subnet_mappings: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    app_id_version: typing.Optional[builtins.str] = None,
    automatic_upgrade_app_id_version: typing.Optional[builtins.bool] = None,
    cloud_watch_metric_namespace: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    rule_stack_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__babd383745f46351db16da77dd426a0238262cf070da922071ca55f3a80af00b(
    *,
    endpoint_mode: CfnNgfwPropsEndpointMode,
    firewall_name: builtins.str,
    log_destination_configs: typing.Sequence[typing.Union[LogProfileConfig, typing.Dict[builtins.str, typing.Any]]],
    programmatic_access_token: builtins.str,
    subnet_mappings: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    app_id_version: typing.Optional[builtins.str] = None,
    automatic_upgrade_app_id_version: typing.Optional[builtins.bool] = None,
    cloud_watch_metric_namespace: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    rule_stack_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Any]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecbd3e688630265a99392f1db06e9897764a78868a0e014666ab1b1ec9468311(
    *,
    log_destination: builtins.str,
    log_destination_type: LogProfileConfigLogDestinationType,
    log_type: LogProfileConfigLogType,
) -> None:
    """Type checking stubs"""
    pass
