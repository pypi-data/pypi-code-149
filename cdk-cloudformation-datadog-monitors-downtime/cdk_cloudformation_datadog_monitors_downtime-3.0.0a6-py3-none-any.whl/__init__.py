'''
# datadog-monitors-downtime

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Datadog::Monitors::Downtime` v3.0.0.

## Description

Datadog Monitors Downtime 3.0.0

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Datadog::Monitors::Downtime \
  --publisher-id 7171b96e5d207b947eb72ca9ce05247c246de623 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/7171b96e5d207b947eb72ca9ce05247c246de623/Datadog-Monitors-Downtime \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Datadog::Monitors::Downtime`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fdatadog-monitors-downtime+v3.0.0).
* Issues related to `Datadog::Monitors::Downtime` should be reported to the [publisher](undefined).

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


class CfnDowntime(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/datadog-monitors-downtime.CfnDowntime",
):
    '''A CloudFormation ``Datadog::Monitors::Downtime``.

    :cloudformationResource: Datadog::Monitors::Downtime
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope_: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        scope: typing.Sequence[builtins.str],
        disabled: typing.Optional[builtins.bool] = None,
        end: typing.Optional[jsii.Number] = None,
        message: typing.Optional[builtins.str] = None,
        monitor_id: typing.Optional[jsii.Number] = None,
        monitor_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        start: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``Datadog::Monitors::Downtime``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param scope: The scope(s) to which the downtime applies.
        :param disabled: Whether or not this downtime is disabled.
        :param end: POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely (i.e. until you cancel it).
        :param message: Message on the downtime.
        :param monitor_id: A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.
        :param monitor_tags: A comma-separated list of monitor tags, to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags.
        :param start: POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.
        :param timezone: The timezone for the downtime.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__401b47c4e5e781ce81560cef6085e141285dc5ae53879fedb7a3d3e375b987ad)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDowntimeProps(
            scope=scope,
            disabled=disabled,
            end=end,
            message=message,
            monitor_id=monitor_id,
            monitor_tags=monitor_tags,
            start=start,
            timezone=timezone,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrActive")
    def attr_active(self) -> _aws_cdk_ceddda9d.IResolvable:
        '''Attribute ``Datadog::Monitors::Downtime.Active``.

        :link: http://unknown-url
        '''
        return typing.cast(_aws_cdk_ceddda9d.IResolvable, jsii.get(self, "attrActive"))

    @builtins.property
    @jsii.member(jsii_name="attrCanceled")
    def attr_canceled(self) -> jsii.Number:
        '''Attribute ``Datadog::Monitors::Downtime.Canceled``.

        :link: http://unknown-url
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCanceled"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatorId")
    def attr_creator_id(self) -> jsii.Number:
        '''Attribute ``Datadog::Monitors::Downtime.CreatorId``.

        :link: http://unknown-url
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreatorId"))

    @builtins.property
    @jsii.member(jsii_name="attrDowntimeType")
    def attr_downtime_type(self) -> jsii.Number:
        '''Attribute ``Datadog::Monitors::Downtime.DowntimeType``.

        :link: http://unknown-url
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDowntimeType"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> jsii.Number:
        '''Attribute ``Datadog::Monitors::Downtime.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrParentId")
    def attr_parent_id(self) -> jsii.Number:
        '''Attribute ``Datadog::Monitors::Downtime.ParentId``.

        :link: http://unknown-url
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrParentId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdaterId")
    def attr_updater_id(self) -> jsii.Number:
        '''Attribute ``Datadog::Monitors::Downtime.UpdaterId``.

        :link: http://unknown-url
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrUpdaterId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDowntimeProps":
        '''Resource props.'''
        return typing.cast("CfnDowntimeProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-monitors-downtime.CfnDowntimeProps",
    jsii_struct_bases=[],
    name_mapping={
        "scope": "scope",
        "disabled": "disabled",
        "end": "end",
        "message": "message",
        "monitor_id": "monitorId",
        "monitor_tags": "monitorTags",
        "start": "start",
        "timezone": "timezone",
    },
)
class CfnDowntimeProps:
    def __init__(
        self,
        *,
        scope: typing.Sequence[builtins.str],
        disabled: typing.Optional[builtins.bool] = None,
        end: typing.Optional[jsii.Number] = None,
        message: typing.Optional[builtins.str] = None,
        monitor_id: typing.Optional[jsii.Number] = None,
        monitor_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        start: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Datadog Monitors Downtime 3.0.0.

        :param scope: The scope(s) to which the downtime applies.
        :param disabled: Whether or not this downtime is disabled.
        :param end: POSIX timestamp to end the downtime. If not provided, the downtime is in effect indefinitely (i.e. until you cancel it).
        :param message: Message on the downtime.
        :param monitor_id: A single monitor to which the downtime applies. If not provided, the downtime applies to all monitors.
        :param monitor_tags: A comma-separated list of monitor tags, to which the downtime applies. The resulting downtime applies to monitors that match ALL provided monitor tags.
        :param start: POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created.
        :param timezone: The timezone for the downtime.

        :schema: CfnDowntimeProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc9758a4ea882bbedf1786d023260c8d3059e66155da2abe67683f21106408ca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument monitor_id", value=monitor_id, expected_type=type_hints["monitor_id"])
            check_type(argname="argument monitor_tags", value=monitor_tags, expected_type=type_hints["monitor_tags"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scope": scope,
        }
        if disabled is not None:
            self._values["disabled"] = disabled
        if end is not None:
            self._values["end"] = end
        if message is not None:
            self._values["message"] = message
        if monitor_id is not None:
            self._values["monitor_id"] = monitor_id
        if monitor_tags is not None:
            self._values["monitor_tags"] = monitor_tags
        if start is not None:
            self._values["start"] = start
        if timezone is not None:
            self._values["timezone"] = timezone

    @builtins.property
    def scope(self) -> typing.List[builtins.str]:
        '''The scope(s) to which the downtime applies.

        :schema: CfnDowntimeProps#Scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def disabled(self) -> typing.Optional[builtins.bool]:
        '''Whether or not this downtime is disabled.

        :schema: CfnDowntimeProps#Disabled
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def end(self) -> typing.Optional[jsii.Number]:
        '''POSIX timestamp to end the downtime.

        If not provided, the downtime is in effect indefinitely (i.e. until you cancel it).

        :schema: CfnDowntimeProps#End
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Message on the downtime.

        :schema: CfnDowntimeProps#Message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitor_id(self) -> typing.Optional[jsii.Number]:
        '''A single monitor to which the downtime applies.

        If not provided, the downtime applies to all monitors.

        :schema: CfnDowntimeProps#MonitorId
        '''
        result = self._values.get("monitor_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitor_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of monitor tags, to which the downtime applies.

        The resulting downtime applies to monitors that match ALL provided monitor tags.

        :schema: CfnDowntimeProps#MonitorTags
        '''
        result = self._values.get("monitor_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def start(self) -> typing.Optional[jsii.Number]:
        '''POSIX timestamp to start the downtime.

        If not provided, the downtime starts the moment it is created.

        :schema: CfnDowntimeProps#Start
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone for the downtime.

        :schema: CfnDowntimeProps#Timezone
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDowntimeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDowntime",
    "CfnDowntimeProps",
]

publication.publish()

def _typecheckingstub__401b47c4e5e781ce81560cef6085e141285dc5ae53879fedb7a3d3e375b987ad(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    scope: typing.Sequence[builtins.str],
    disabled: typing.Optional[builtins.bool] = None,
    end: typing.Optional[jsii.Number] = None,
    message: typing.Optional[builtins.str] = None,
    monitor_id: typing.Optional[jsii.Number] = None,
    monitor_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    start: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc9758a4ea882bbedf1786d023260c8d3059e66155da2abe67683f21106408ca(
    *,
    scope: typing.Sequence[builtins.str],
    disabled: typing.Optional[builtins.bool] = None,
    end: typing.Optional[jsii.Number] = None,
    message: typing.Optional[builtins.str] = None,
    monitor_id: typing.Optional[jsii.Number] = None,
    monitor_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    start: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
