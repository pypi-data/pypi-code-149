'''
# datadog-integrations-aws

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Datadog::Integrations::AWS` v2.3.0.

## Description

Datadog AWS Integration 2.2.1

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Datadog::Integrations::AWS \
  --publisher-id 7171b96e5d207b947eb72ca9ce05247c246de623 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/7171b96e5d207b947eb72ca9ce05247c246de623/Datadog-Integrations-AWS \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Datadog::Integrations::AWS`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fdatadog-integrations-aws+v2.3.0).
* Issues related to `Datadog::Integrations::AWS` should be reported to the [publisher](undefined).

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


class CfnAws(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/datadog-integrations-aws.CfnAws",
):
    '''A CloudFormation ``Datadog::Integrations::AWS``.

    :cloudformationResource: Datadog::Integrations::AWS
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_key_id: typing.Optional[builtins.str] = None,
        account_id: typing.Optional[builtins.str] = None,
        account_specific_namespace_rules: typing.Any = None,
        cspm_resource_collection: typing.Optional[builtins.bool] = None,
        external_id_secret_name: typing.Optional[builtins.str] = None,
        filter_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_collection: typing.Optional[builtins.bool] = None,
        resource_collection: typing.Optional[builtins.bool] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``Datadog::Integrations::AWS``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param access_key_id: If your AWS account is a GovCloud or China account, enter the corresponding Access Key ID.
        :param account_id: Your AWS Account ID without dashes.
        :param account_specific_namespace_rules: An object (in the form {"namespace1":true/false, "namespace2":true/false}) that enables or disables metric collection for specific AWS namespaces for this AWS account only.
        :param cspm_resource_collection: Enable the compliance and security posture management Datadog product. This will enable collecting information on your AWS resources and providing security validation.
        :param external_id_secret_name: The name of the AWS SecretsManager secret created in your account to hold this integration's ``external_id``. Defaults to ``DatadogIntegrationExternalID``. Cannot be referenced from created resource. Default: DatadogIntegrationExternalID`. Cannot be referenced from created resource.
        :param filter_tags: The array of EC2 tags (in the form key:value) defines a filter that Datadog uses when collecting metrics from EC2.
        :param host_tags: Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.
        :param metrics_collection: Enable the infrastructure monitoring Datadog product for this AWS Account. This will enable collecting all AWS metrics in your account.
        :param resource_collection: Enable collecting information on your AWS resources for use in Datadog products such as Network Process Monitoring.
        :param role_name: Your Datadog role delegation name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8830a640e4df2067924874a59e6d390baa2617c42aad50b1203219db7d6fe81a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAwsProps(
            access_key_id=access_key_id,
            account_id=account_id,
            account_specific_namespace_rules=account_specific_namespace_rules,
            cspm_resource_collection=cspm_resource_collection,
            external_id_secret_name=external_id_secret_name,
            filter_tags=filter_tags,
            host_tags=host_tags,
            metrics_collection=metrics_collection,
            resource_collection=resource_collection,
            role_name=role_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIntegrationID")
    def attr_integration_id(self) -> builtins.str:
        '''Attribute ``Datadog::Integrations::AWS.IntegrationID``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationID"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnAwsProps":
        '''Resource props.'''
        return typing.cast("CfnAwsProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/datadog-integrations-aws.CfnAwsProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_key_id": "accessKeyId",
        "account_id": "accountId",
        "account_specific_namespace_rules": "accountSpecificNamespaceRules",
        "cspm_resource_collection": "cspmResourceCollection",
        "external_id_secret_name": "externalIdSecretName",
        "filter_tags": "filterTags",
        "host_tags": "hostTags",
        "metrics_collection": "metricsCollection",
        "resource_collection": "resourceCollection",
        "role_name": "roleName",
    },
)
class CfnAwsProps:
    def __init__(
        self,
        *,
        access_key_id: typing.Optional[builtins.str] = None,
        account_id: typing.Optional[builtins.str] = None,
        account_specific_namespace_rules: typing.Any = None,
        cspm_resource_collection: typing.Optional[builtins.bool] = None,
        external_id_secret_name: typing.Optional[builtins.str] = None,
        filter_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_collection: typing.Optional[builtins.bool] = None,
        resource_collection: typing.Optional[builtins.bool] = None,
        role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Datadog AWS Integration 2.2.1.

        :param access_key_id: If your AWS account is a GovCloud or China account, enter the corresponding Access Key ID.
        :param account_id: Your AWS Account ID without dashes.
        :param account_specific_namespace_rules: An object (in the form {"namespace1":true/false, "namespace2":true/false}) that enables or disables metric collection for specific AWS namespaces for this AWS account only.
        :param cspm_resource_collection: Enable the compliance and security posture management Datadog product. This will enable collecting information on your AWS resources and providing security validation.
        :param external_id_secret_name: The name of the AWS SecretsManager secret created in your account to hold this integration's ``external_id``. Defaults to ``DatadogIntegrationExternalID``. Cannot be referenced from created resource. Default: DatadogIntegrationExternalID`. Cannot be referenced from created resource.
        :param filter_tags: The array of EC2 tags (in the form key:value) defines a filter that Datadog uses when collecting metrics from EC2.
        :param host_tags: Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.
        :param metrics_collection: Enable the infrastructure monitoring Datadog product for this AWS Account. This will enable collecting all AWS metrics in your account.
        :param resource_collection: Enable collecting information on your AWS resources for use in Datadog products such as Network Process Monitoring.
        :param role_name: Your Datadog role delegation name.

        :schema: CfnAwsProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43439c00d9be4cf1962f105015e4a84d7c2028cd1f85427390e822315830bd53)
            check_type(argname="argument access_key_id", value=access_key_id, expected_type=type_hints["access_key_id"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument account_specific_namespace_rules", value=account_specific_namespace_rules, expected_type=type_hints["account_specific_namespace_rules"])
            check_type(argname="argument cspm_resource_collection", value=cspm_resource_collection, expected_type=type_hints["cspm_resource_collection"])
            check_type(argname="argument external_id_secret_name", value=external_id_secret_name, expected_type=type_hints["external_id_secret_name"])
            check_type(argname="argument filter_tags", value=filter_tags, expected_type=type_hints["filter_tags"])
            check_type(argname="argument host_tags", value=host_tags, expected_type=type_hints["host_tags"])
            check_type(argname="argument metrics_collection", value=metrics_collection, expected_type=type_hints["metrics_collection"])
            check_type(argname="argument resource_collection", value=resource_collection, expected_type=type_hints["resource_collection"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_key_id is not None:
            self._values["access_key_id"] = access_key_id
        if account_id is not None:
            self._values["account_id"] = account_id
        if account_specific_namespace_rules is not None:
            self._values["account_specific_namespace_rules"] = account_specific_namespace_rules
        if cspm_resource_collection is not None:
            self._values["cspm_resource_collection"] = cspm_resource_collection
        if external_id_secret_name is not None:
            self._values["external_id_secret_name"] = external_id_secret_name
        if filter_tags is not None:
            self._values["filter_tags"] = filter_tags
        if host_tags is not None:
            self._values["host_tags"] = host_tags
        if metrics_collection is not None:
            self._values["metrics_collection"] = metrics_collection
        if resource_collection is not None:
            self._values["resource_collection"] = resource_collection
        if role_name is not None:
            self._values["role_name"] = role_name

    @builtins.property
    def access_key_id(self) -> typing.Optional[builtins.str]:
        '''If your AWS account is a GovCloud or China account, enter the corresponding Access Key ID.

        :schema: CfnAwsProps#AccessKeyID
        '''
        result = self._values.get("access_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Your AWS Account ID without dashes.

        :schema: CfnAwsProps#AccountID
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_specific_namespace_rules(self) -> typing.Any:
        '''An object (in the form {"namespace1":true/false, "namespace2":true/false}) that enables or disables metric collection for specific AWS namespaces for this AWS account only.

        :schema: CfnAwsProps#AccountSpecificNamespaceRules
        '''
        result = self._values.get("account_specific_namespace_rules")
        return typing.cast(typing.Any, result)

    @builtins.property
    def cspm_resource_collection(self) -> typing.Optional[builtins.bool]:
        '''Enable the compliance and security posture management Datadog product.

        This will enable collecting information on your AWS resources and providing security validation.

        :schema: CfnAwsProps#CSPMResourceCollection
        '''
        result = self._values.get("cspm_resource_collection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def external_id_secret_name(self) -> typing.Optional[builtins.str]:
        '''The name of the AWS SecretsManager secret created in your account to hold this integration's ``external_id``.

        Defaults to ``DatadogIntegrationExternalID``. Cannot be referenced from created resource.

        :default: DatadogIntegrationExternalID`. Cannot be referenced from created resource.

        :schema: CfnAwsProps#ExternalIDSecretName
        '''
        result = self._values.get("external_id_secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The array of EC2 tags (in the form key:value) defines a filter that Datadog uses when collecting metrics from EC2.

        :schema: CfnAwsProps#FilterTags
        '''
        result = self._values.get("filter_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def host_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.

        :schema: CfnAwsProps#HostTags
        '''
        result = self._values.get("host_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_collection(self) -> typing.Optional[builtins.bool]:
        '''Enable the infrastructure monitoring Datadog product for this AWS Account.

        This will enable collecting all AWS metrics in your account.

        :schema: CfnAwsProps#MetricsCollection
        '''
        result = self._values.get("metrics_collection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def resource_collection(self) -> typing.Optional[builtins.bool]:
        '''Enable collecting information on your AWS resources for use in Datadog products such as Network Process Monitoring.

        :schema: CfnAwsProps#ResourceCollection
        '''
        result = self._values.get("resource_collection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''Your Datadog role delegation name.

        :schema: CfnAwsProps#RoleName
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAwsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAws",
    "CfnAwsProps",
]

publication.publish()

def _typecheckingstub__8830a640e4df2067924874a59e6d390baa2617c42aad50b1203219db7d6fe81a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_key_id: typing.Optional[builtins.str] = None,
    account_id: typing.Optional[builtins.str] = None,
    account_specific_namespace_rules: typing.Any = None,
    cspm_resource_collection: typing.Optional[builtins.bool] = None,
    external_id_secret_name: typing.Optional[builtins.str] = None,
    filter_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    host_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_collection: typing.Optional[builtins.bool] = None,
    resource_collection: typing.Optional[builtins.bool] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43439c00d9be4cf1962f105015e4a84d7c2028cd1f85427390e822315830bd53(
    *,
    access_key_id: typing.Optional[builtins.str] = None,
    account_id: typing.Optional[builtins.str] = None,
    account_specific_namespace_rules: typing.Any = None,
    cspm_resource_collection: typing.Optional[builtins.bool] = None,
    external_id_secret_name: typing.Optional[builtins.str] = None,
    filter_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    host_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    metrics_collection: typing.Optional[builtins.bool] = None,
    resource_collection: typing.Optional[builtins.bool] = None,
    role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
