'''
# alexa-ask-skill

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Alexa::ASK::Skill`.

---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This package is deprecated. Please use @aws-cdk/alexa-ask instead

---


## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Alexa::ASK::Skill \
  --publisher-id undefined \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/Alexa-ASK-Skill \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Alexa::ASK::Skill`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Falexa-ask-skill).
* Issues related to `Alexa::ASK::Skill` should be reported to the [publisher](undefined).

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


@jsii.data_type(
    jsii_type="@cdk-cloudformation/alexa-ask-skill.AuthenticationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "refresh_token": "refreshToken",
    },
)
class AuthenticationConfiguration:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        refresh_token: builtins.str,
    ) -> None:
        '''
        :param client_id: 
        :param client_secret: 
        :param refresh_token: 

        :stability: deprecated
        :schema: AuthenticationConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cb79a88fffa5894b69aba27a08e485828ba35ce645d2860dda9ffc4eab7b06e)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''
        :stability: deprecated
        :schema: AuthenticationConfiguration#ClientId
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''
        :stability: deprecated
        :schema: AuthenticationConfiguration#ClientSecret
        '''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def refresh_token(self) -> builtins.str:
        '''
        :stability: deprecated
        :schema: AuthenticationConfiguration#RefreshToken
        '''
        result = self._values.get("refresh_token")
        assert result is not None, "Required property 'refresh_token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthenticationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnSkill(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/alexa-ask-skill.CfnSkill",
):
    '''A CloudFormation ``Alexa::ASK::Skill``.

    :cloudformationResource: Alexa::ASK::Skill
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authentication_configuration: typing.Union[AuthenticationConfiguration, typing.Dict[builtins.str, typing.Any]],
        skill_package: typing.Union["SkillPackage", typing.Dict[builtins.str, typing.Any]],
        vendor_id: builtins.str,
    ) -> None:
        '''Create a new ``Alexa::ASK::Skill``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authentication_configuration: 
        :param skill_package: 
        :param vendor_id: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253ee7921693e8436805fbaff1fc132c784aeb7a2365ace5417b43df4d45ec78)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSkillProps(
            authentication_configuration=authentication_configuration,
            skill_package=skill_package,
            vendor_id=vendor_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``Alexa::ASK::Skill.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnSkillProps":
        '''Resource props.'''
        return typing.cast("CfnSkillProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/alexa-ask-skill.CfnSkillProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_configuration": "authenticationConfiguration",
        "skill_package": "skillPackage",
        "vendor_id": "vendorId",
    },
)
class CfnSkillProps:
    def __init__(
        self,
        *,
        authentication_configuration: typing.Union[AuthenticationConfiguration, typing.Dict[builtins.str, typing.Any]],
        skill_package: typing.Union["SkillPackage", typing.Dict[builtins.str, typing.Any]],
        vendor_id: builtins.str,
    ) -> None:
        '''(deprecated) Resource Type definition for Alexa::ASK::Skill.

        :param authentication_configuration: 
        :param skill_package: 
        :param vendor_id: 

        :stability: deprecated
        :schema: CfnSkillProps
        '''
        if isinstance(authentication_configuration, dict):
            authentication_configuration = AuthenticationConfiguration(**authentication_configuration)
        if isinstance(skill_package, dict):
            skill_package = SkillPackage(**skill_package)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60247b7a1c9c5197f4cc9072f52ea71b5ae99d00222ee649838d07cb56f0413f)
            check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
            check_type(argname="argument skill_package", value=skill_package, expected_type=type_hints["skill_package"])
            check_type(argname="argument vendor_id", value=vendor_id, expected_type=type_hints["vendor_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_configuration": authentication_configuration,
            "skill_package": skill_package,
            "vendor_id": vendor_id,
        }

    @builtins.property
    def authentication_configuration(self) -> AuthenticationConfiguration:
        '''
        :stability: deprecated
        :schema: CfnSkillProps#AuthenticationConfiguration
        '''
        result = self._values.get("authentication_configuration")
        assert result is not None, "Required property 'authentication_configuration' is missing"
        return typing.cast(AuthenticationConfiguration, result)

    @builtins.property
    def skill_package(self) -> "SkillPackage":
        '''
        :stability: deprecated
        :schema: CfnSkillProps#SkillPackage
        '''
        result = self._values.get("skill_package")
        assert result is not None, "Required property 'skill_package' is missing"
        return typing.cast("SkillPackage", result)

    @builtins.property
    def vendor_id(self) -> builtins.str:
        '''
        :stability: deprecated
        :schema: CfnSkillProps#VendorId
        '''
        result = self._values.get("vendor_id")
        assert result is not None, "Required property 'vendor_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSkillProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/alexa-ask-skill.Overrides",
    jsii_struct_bases=[],
    name_mapping={"manifest": "manifest"},
)
class Overrides:
    def __init__(self, *, manifest: typing.Any = None) -> None:
        '''
        :param manifest: 

        :stability: deprecated
        :schema: Overrides
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c367c66d878fb56e54bbb04180afac2e95cef5f84012b3efba08b0f858fa1074)
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if manifest is not None:
            self._values["manifest"] = manifest

    @builtins.property
    def manifest(self) -> typing.Any:
        '''
        :stability: deprecated
        :schema: Overrides#Manifest
        '''
        result = self._values.get("manifest")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Overrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/alexa-ask-skill.SkillPackage",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket": "s3Bucket",
        "s3_key": "s3Key",
        "overrides": "overrides",
        "s3_bucket_role": "s3BucketRole",
        "s3_object_version": "s3ObjectVersion",
    },
)
class SkillPackage:
    def __init__(
        self,
        *,
        s3_bucket: builtins.str,
        s3_key: builtins.str,
        overrides: typing.Optional[typing.Union[Overrides, typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket_role: typing.Optional[builtins.str] = None,
        s3_object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_bucket: 
        :param s3_key: 
        :param overrides: 
        :param s3_bucket_role: 
        :param s3_object_version: 

        :stability: deprecated
        :schema: SkillPackage
        '''
        if isinstance(overrides, dict):
            overrides = Overrides(**overrides)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b56cb641b00be0c44e3959d218008aaebfff342cb3fae0beb2bfa861058a498)
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
            check_type(argname="argument s3_bucket_role", value=s3_bucket_role, expected_type=type_hints["s3_bucket_role"])
            check_type(argname="argument s3_object_version", value=s3_object_version, expected_type=type_hints["s3_object_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_bucket": s3_bucket,
            "s3_key": s3_key,
        }
        if overrides is not None:
            self._values["overrides"] = overrides
        if s3_bucket_role is not None:
            self._values["s3_bucket_role"] = s3_bucket_role
        if s3_object_version is not None:
            self._values["s3_object_version"] = s3_object_version

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''
        :stability: deprecated
        :schema: SkillPackage#S3Bucket
        '''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_key(self) -> builtins.str:
        '''
        :stability: deprecated
        :schema: SkillPackage#S3Key
        '''
        result = self._values.get("s3_key")
        assert result is not None, "Required property 's3_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overrides(self) -> typing.Optional[Overrides]:
        '''
        :stability: deprecated
        :schema: SkillPackage#Overrides
        '''
        result = self._values.get("overrides")
        return typing.cast(typing.Optional[Overrides], result)

    @builtins.property
    def s3_bucket_role(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: SkillPackage#S3BucketRole
        '''
        result = self._values.get("s3_bucket_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_object_version(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: SkillPackage#S3ObjectVersion
        '''
        result = self._values.get("s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SkillPackage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthenticationConfiguration",
    "CfnSkill",
    "CfnSkillProps",
    "Overrides",
    "SkillPackage",
]

publication.publish()

def _typecheckingstub__6cb79a88fffa5894b69aba27a08e485828ba35ce645d2860dda9ffc4eab7b06e(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    refresh_token: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253ee7921693e8436805fbaff1fc132c784aeb7a2365ace5417b43df4d45ec78(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authentication_configuration: typing.Union[AuthenticationConfiguration, typing.Dict[builtins.str, typing.Any]],
    skill_package: typing.Union[SkillPackage, typing.Dict[builtins.str, typing.Any]],
    vendor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60247b7a1c9c5197f4cc9072f52ea71b5ae99d00222ee649838d07cb56f0413f(
    *,
    authentication_configuration: typing.Union[AuthenticationConfiguration, typing.Dict[builtins.str, typing.Any]],
    skill_package: typing.Union[SkillPackage, typing.Dict[builtins.str, typing.Any]],
    vendor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c367c66d878fb56e54bbb04180afac2e95cef5f84012b3efba08b0f858fa1074(
    *,
    manifest: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b56cb641b00be0c44e3959d218008aaebfff342cb3fae0beb2bfa861058a498(
    *,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
    overrides: typing.Optional[typing.Union[Overrides, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket_role: typing.Optional[builtins.str] = None,
    s3_object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
