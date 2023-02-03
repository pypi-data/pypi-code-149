'''
# atlassian-opsgenie-integration

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Atlassian::Opsgenie::Integration` v1.0.1.

## Description

Opsgenie Integration Resource definition

## References

* [Source](https://github.com/opsgenie/opsgenie-cloudformation-resources)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Atlassian::Opsgenie::Integration \
  --publisher-id 4fb8713ab4ce2587ce74e0559d7661bb6e01e72b \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/4fb8713ab4ce2587ce74e0559d7661bb6e01e72b/Atlassian-Opsgenie-Integration \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Atlassian::Opsgenie::Integration`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fatlassian-opsgenie-integration+v1.0.1).
* Issues related to `Atlassian::Opsgenie::Integration` should be reported to the [publisher](https://github.com/opsgenie/opsgenie-cloudformation-resources).

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


class CfnIntegration(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-integration.CfnIntegration",
):
    '''A CloudFormation ``Atlassian::Opsgenie::Integration``.

    :cloudformationResource: Atlassian::Opsgenie::Integration
    :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        enabled: builtins.bool,
        integration_type: builtins.str,
        name: builtins.str,
        opsgenie_api_endpoint: builtins.str,
        opsgenie_api_key: builtins.str,
        allow_configuration_access: typing.Optional[builtins.bool] = None,
        allow_delete_access: typing.Optional[builtins.bool] = None,
        allow_read_access: typing.Optional[builtins.bool] = None,
        allow_write_access: typing.Optional[builtins.bool] = None,
        owner_team_id: typing.Optional[builtins.str] = None,
        owner_team_name: typing.Optional[builtins.str] = None,
        responders: typing.Optional[typing.Sequence[typing.Union["RespondersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``Atlassian::Opsgenie::Integration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param enabled: Integration status, default is true.
        :param integration_type: Integration types, only api integration types supported.
        :param name: Integration name.
        :param opsgenie_api_endpoint: 
        :param opsgenie_api_key: 
        :param allow_configuration_access: This parameter is for allowing or restricting the configuration access.
        :param allow_delete_access: This parameter is for configuring the delete access of integration.
        :param allow_read_access: This parameter is for configuring the read access of integration.
        :param allow_write_access: This parameter is for configuring the write access of integration.
        :param owner_team_id: Id of the integration owner team.
        :param owner_team_name: Name of the integration owner team.
        :param responders: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d0fbcf69f663c7639d8da5f14c5686a399e861a681d04db9e7ac31b94aa587)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIntegrationProps(
            enabled=enabled,
            integration_type=integration_type,
            name=name,
            opsgenie_api_endpoint=opsgenie_api_endpoint,
            opsgenie_api_key=opsgenie_api_key,
            allow_configuration_access=allow_configuration_access,
            allow_delete_access=allow_delete_access,
            allow_read_access=allow_read_access,
            allow_write_access=allow_write_access,
            owner_team_id=owner_team_id,
            owner_team_name=owner_team_name,
            responders=responders,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIntegrationApiKey")
    def attr_integration_api_key(self) -> builtins.str:
        '''Attribute ``Atlassian::Opsgenie::Integration.IntegrationApiKey``.

        :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationApiKey"))

    @builtins.property
    @jsii.member(jsii_name="attrIntegrationId")
    def attr_integration_id(self) -> builtins.str:
        '''Attribute ``Atlassian::Opsgenie::Integration.IntegrationId``.

        :link: https://github.com/opsgenie/opsgenie-cloudformation-resources
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnIntegrationProps":
        '''Resource props.'''
        return typing.cast("CfnIntegrationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-integration.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "integration_type": "integrationType",
        "name": "name",
        "opsgenie_api_endpoint": "opsgenieApiEndpoint",
        "opsgenie_api_key": "opsgenieApiKey",
        "allow_configuration_access": "allowConfigurationAccess",
        "allow_delete_access": "allowDeleteAccess",
        "allow_read_access": "allowReadAccess",
        "allow_write_access": "allowWriteAccess",
        "owner_team_id": "ownerTeamId",
        "owner_team_name": "ownerTeamName",
        "responders": "responders",
    },
)
class CfnIntegrationProps:
    def __init__(
        self,
        *,
        enabled: builtins.bool,
        integration_type: builtins.str,
        name: builtins.str,
        opsgenie_api_endpoint: builtins.str,
        opsgenie_api_key: builtins.str,
        allow_configuration_access: typing.Optional[builtins.bool] = None,
        allow_delete_access: typing.Optional[builtins.bool] = None,
        allow_read_access: typing.Optional[builtins.bool] = None,
        allow_write_access: typing.Optional[builtins.bool] = None,
        owner_team_id: typing.Optional[builtins.str] = None,
        owner_team_name: typing.Optional[builtins.str] = None,
        responders: typing.Optional[typing.Sequence[typing.Union["RespondersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Opsgenie Integration Resource definition.

        :param enabled: Integration status, default is true.
        :param integration_type: Integration types, only api integration types supported.
        :param name: Integration name.
        :param opsgenie_api_endpoint: 
        :param opsgenie_api_key: 
        :param allow_configuration_access: This parameter is for allowing or restricting the configuration access.
        :param allow_delete_access: This parameter is for configuring the delete access of integration.
        :param allow_read_access: This parameter is for configuring the read access of integration.
        :param allow_write_access: This parameter is for configuring the write access of integration.
        :param owner_team_id: Id of the integration owner team.
        :param owner_team_name: Name of the integration owner team.
        :param responders: 

        :schema: CfnIntegrationProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bed5ba4c21413884ff1d76b73592c4da7551f19b156a79bc206cb7d020b1af09)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument integration_type", value=integration_type, expected_type=type_hints["integration_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument opsgenie_api_endpoint", value=opsgenie_api_endpoint, expected_type=type_hints["opsgenie_api_endpoint"])
            check_type(argname="argument opsgenie_api_key", value=opsgenie_api_key, expected_type=type_hints["opsgenie_api_key"])
            check_type(argname="argument allow_configuration_access", value=allow_configuration_access, expected_type=type_hints["allow_configuration_access"])
            check_type(argname="argument allow_delete_access", value=allow_delete_access, expected_type=type_hints["allow_delete_access"])
            check_type(argname="argument allow_read_access", value=allow_read_access, expected_type=type_hints["allow_read_access"])
            check_type(argname="argument allow_write_access", value=allow_write_access, expected_type=type_hints["allow_write_access"])
            check_type(argname="argument owner_team_id", value=owner_team_id, expected_type=type_hints["owner_team_id"])
            check_type(argname="argument owner_team_name", value=owner_team_name, expected_type=type_hints["owner_team_name"])
            check_type(argname="argument responders", value=responders, expected_type=type_hints["responders"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
            "integration_type": integration_type,
            "name": name,
            "opsgenie_api_endpoint": opsgenie_api_endpoint,
            "opsgenie_api_key": opsgenie_api_key,
        }
        if allow_configuration_access is not None:
            self._values["allow_configuration_access"] = allow_configuration_access
        if allow_delete_access is not None:
            self._values["allow_delete_access"] = allow_delete_access
        if allow_read_access is not None:
            self._values["allow_read_access"] = allow_read_access
        if allow_write_access is not None:
            self._values["allow_write_access"] = allow_write_access
        if owner_team_id is not None:
            self._values["owner_team_id"] = owner_team_id
        if owner_team_name is not None:
            self._values["owner_team_name"] = owner_team_name
        if responders is not None:
            self._values["responders"] = responders

    @builtins.property
    def enabled(self) -> builtins.bool:
        '''Integration status, default is true.

        :schema: CfnIntegrationProps#Enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def integration_type(self) -> builtins.str:
        '''Integration types, only api integration types supported.

        :schema: CfnIntegrationProps#IntegrationType
        '''
        result = self._values.get("integration_type")
        assert result is not None, "Required property 'integration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Integration name.

        :schema: CfnIntegrationProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_endpoint(self) -> builtins.str:
        '''
        :schema: CfnIntegrationProps#OpsgenieApiEndpoint
        '''
        result = self._values.get("opsgenie_api_endpoint")
        assert result is not None, "Required property 'opsgenie_api_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opsgenie_api_key(self) -> builtins.str:
        '''
        :schema: CfnIntegrationProps#OpsgenieApiKey
        '''
        result = self._values.get("opsgenie_api_key")
        assert result is not None, "Required property 'opsgenie_api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_configuration_access(self) -> typing.Optional[builtins.bool]:
        '''This parameter is for allowing or restricting the configuration access.

        :schema: CfnIntegrationProps#AllowConfigurationAccess
        '''
        result = self._values.get("allow_configuration_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_delete_access(self) -> typing.Optional[builtins.bool]:
        '''This parameter is for configuring the delete access of integration.

        :schema: CfnIntegrationProps#AllowDeleteAccess
        '''
        result = self._values.get("allow_delete_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_read_access(self) -> typing.Optional[builtins.bool]:
        '''This parameter is for configuring the read access of integration.

        :schema: CfnIntegrationProps#AllowReadAccess
        '''
        result = self._values.get("allow_read_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_write_access(self) -> typing.Optional[builtins.bool]:
        '''This parameter is for configuring the write access of integration.

        :schema: CfnIntegrationProps#AllowWriteAccess
        '''
        result = self._values.get("allow_write_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def owner_team_id(self) -> typing.Optional[builtins.str]:
        '''Id of the integration owner team.

        :schema: CfnIntegrationProps#OwnerTeamId
        '''
        result = self._values.get("owner_team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_team_name(self) -> typing.Optional[builtins.str]:
        '''Name of the integration owner team.

        :schema: CfnIntegrationProps#OwnerTeamName
        '''
        result = self._values.get("owner_team_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def responders(self) -> typing.Optional[typing.List["RespondersProperty"]]:
        '''
        :schema: CfnIntegrationProps#Responders
        '''
        result = self._values.get("responders")
        return typing.cast(typing.Optional[typing.List["RespondersProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/atlassian-opsgenie-integration.RespondersProperty",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "username": "username"},
)
class RespondersProperty:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Responder name if available.
        :param type: Responder type.
        :param username: Responder username, if responder type is user.

        :schema: respondersProperty
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46046992fabe103a414110ecff972be12bb47d4439cc831b018d5d06135727e5)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Responder name if available.

        :schema: respondersProperty#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Responder type.

        :schema: respondersProperty#type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Responder username, if responder type is user.

        :schema: respondersProperty#username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RespondersProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnIntegration",
    "CfnIntegrationProps",
    "RespondersProperty",
]

publication.publish()

def _typecheckingstub__64d0fbcf69f663c7639d8da5f14c5686a399e861a681d04db9e7ac31b94aa587(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    enabled: builtins.bool,
    integration_type: builtins.str,
    name: builtins.str,
    opsgenie_api_endpoint: builtins.str,
    opsgenie_api_key: builtins.str,
    allow_configuration_access: typing.Optional[builtins.bool] = None,
    allow_delete_access: typing.Optional[builtins.bool] = None,
    allow_read_access: typing.Optional[builtins.bool] = None,
    allow_write_access: typing.Optional[builtins.bool] = None,
    owner_team_id: typing.Optional[builtins.str] = None,
    owner_team_name: typing.Optional[builtins.str] = None,
    responders: typing.Optional[typing.Sequence[typing.Union[RespondersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bed5ba4c21413884ff1d76b73592c4da7551f19b156a79bc206cb7d020b1af09(
    *,
    enabled: builtins.bool,
    integration_type: builtins.str,
    name: builtins.str,
    opsgenie_api_endpoint: builtins.str,
    opsgenie_api_key: builtins.str,
    allow_configuration_access: typing.Optional[builtins.bool] = None,
    allow_delete_access: typing.Optional[builtins.bool] = None,
    allow_read_access: typing.Optional[builtins.bool] = None,
    allow_write_access: typing.Optional[builtins.bool] = None,
    owner_team_id: typing.Optional[builtins.str] = None,
    owner_team_name: typing.Optional[builtins.str] = None,
    responders: typing.Optional[typing.Sequence[typing.Union[RespondersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46046992fabe103a414110ecff972be12bb47d4439cc831b018d5d06135727e5(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
