'''
# confluentcloud-iam-serviceaccount

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `ConfluentCloud::IAM::ServiceAccount` v1.0.0.

## Description

Service Account as defined in Confluent Cloud IAM v2 API.

## References

* [Source](https://github.com/JohnPreston/aws-cfn-confluentcloud-iam-serviceaccount)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name ConfluentCloud::IAM::ServiceAccount \
  --publisher-id 9331cf547939e23b9c7f24086db031317893be87 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/9331cf547939e23b9c7f24086db031317893be87/ConfluentCloud-IAM-ServiceAccount \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `ConfluentCloud::IAM::ServiceAccount`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fconfluentcloud-iam-serviceaccount+v1.0.0).
* Issues related to `ConfluentCloud::IAM::ServiceAccount` should be reported to the [publisher](https://github.com/JohnPreston/aws-cfn-confluentcloud-iam-serviceaccount).

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


class CfnServiceAccount(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/confluentcloud-iam-serviceaccount.CfnServiceAccount",
):
    '''A CloudFormation ``ConfluentCloud::IAM::ServiceAccount``.

    :cloudformationResource: ConfluentCloud::IAM::ServiceAccount
    :link: https://github.com/JohnPreston/aws-cfn-confluentcloud-iam-serviceaccount
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        confluent_cloud_credentials: typing.Union["ConfluentCloudApiSecrets", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``ConfluentCloud::IAM::ServiceAccount``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param confluent_cloud_credentials: 
        :param name: 
        :param description: The description associated with the Service Account.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a09c3fe050221266560e815bfca5ea271814888f6417ce1684f9eeec1be4958)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceAccountProps(
            confluent_cloud_credentials=confluent_cloud_credentials,
            name=name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceAccountId")
    def attr_service_account_id(self) -> builtins.str:
        '''Attribute ``ConfluentCloud::IAM::ServiceAccount.ServiceAccountId``.

        :link: https://github.com/JohnPreston/aws-cfn-confluentcloud-iam-serviceaccount
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceAccountId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnServiceAccountProps":
        '''Resource props.'''
        return typing.cast("CfnServiceAccountProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/confluentcloud-iam-serviceaccount.CfnServiceAccountProps",
    jsii_struct_bases=[],
    name_mapping={
        "confluent_cloud_credentials": "confluentCloudCredentials",
        "name": "name",
        "description": "description",
    },
)
class CfnServiceAccountProps:
    def __init__(
        self,
        *,
        confluent_cloud_credentials: typing.Union["ConfluentCloudApiSecrets", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Service Account as defined in Confluent Cloud IAM v2 API.

        :param confluent_cloud_credentials: 
        :param name: 
        :param description: The description associated with the Service Account.

        :schema: CfnServiceAccountProps
        '''
        if isinstance(confluent_cloud_credentials, dict):
            confluent_cloud_credentials = ConfluentCloudApiSecrets(**confluent_cloud_credentials)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de03a41780d38a34e3f6b607a3202eb0c01ae05d0c24a0b8d5dec58e224ac3c6)
            check_type(argname="argument confluent_cloud_credentials", value=confluent_cloud_credentials, expected_type=type_hints["confluent_cloud_credentials"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "confluent_cloud_credentials": confluent_cloud_credentials,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def confluent_cloud_credentials(self) -> "ConfluentCloudApiSecrets":
        '''
        :schema: CfnServiceAccountProps#ConfluentCloudCredentials
        '''
        result = self._values.get("confluent_cloud_credentials")
        assert result is not None, "Required property 'confluent_cloud_credentials' is missing"
        return typing.cast("ConfluentCloudApiSecrets", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: CfnServiceAccountProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description associated with the Service Account.

        :schema: CfnServiceAccountProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/confluentcloud-iam-serviceaccount.ConfluentCloudApiSecrets",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "api_secret": "apiSecret"},
)
class ConfluentCloudApiSecrets:
    def __init__(
        self,
        *,
        api_key: typing.Optional[builtins.str] = None,
        api_secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Confluent Cloud API Key.
        :param api_secret: Confluent Cloud API Secret.

        :schema: ConfluentCloudAPISecrets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d9a6c5f03a2272dffd9369eb2b488dd4e260cc4dc0729285c55a490bea0e6e)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_secret", value=api_secret, expected_type=type_hints["api_secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_key is not None:
            self._values["api_key"] = api_key
        if api_secret is not None:
            self._values["api_secret"] = api_secret

    @builtins.property
    def api_key(self) -> typing.Optional[builtins.str]:
        '''Confluent Cloud API Key.

        :schema: ConfluentCloudAPISecrets#ApiKey
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_secret(self) -> typing.Optional[builtins.str]:
        '''Confluent Cloud API Secret.

        :schema: ConfluentCloudAPISecrets#ApiSecret
        '''
        result = self._values.get("api_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfluentCloudApiSecrets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnServiceAccount",
    "CfnServiceAccountProps",
    "ConfluentCloudApiSecrets",
]

publication.publish()

def _typecheckingstub__2a09c3fe050221266560e815bfca5ea271814888f6417ce1684f9eeec1be4958(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    confluent_cloud_credentials: typing.Union[ConfluentCloudApiSecrets, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de03a41780d38a34e3f6b607a3202eb0c01ae05d0c24a0b8d5dec58e224ac3c6(
    *,
    confluent_cloud_credentials: typing.Union[ConfluentCloudApiSecrets, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d9a6c5f03a2272dffd9369eb2b488dd4e260cc4dc0729285c55a490bea0e6e(
    *,
    api_key: typing.Optional[builtins.str] = None,
    api_secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
