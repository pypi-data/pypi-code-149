'''
# aqua-enterprise-enforcer

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Aqua::Enterprise::Enforcer` v1.6.0.

## Description

A resource provider for Aqua Enterprise Enforcer.

## References

* [Source](https://github.com/aquasecurity/aqua-helm.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Aqua::Enterprise::Enforcer \
  --publisher-id 4f06bc39af5f4b984dd46ad17f10316e6258d9fa \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/4f06bc39af5f4b984dd46ad17f10316e6258d9fa/Aqua-Enterprise-Enforcer \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Aqua::Enterprise::Enforcer`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Faqua-enterprise-enforcer+v1.6.0).
* Issues related to `Aqua::Enterprise::Enforcer` should be reported to the [publisher](https://github.com/aquasecurity/aqua-helm.git).

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


class CfnEnforcer(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/aqua-enterprise-enforcer.CfnEnforcer",
):
    '''A CloudFormation ``Aqua::Enterprise::Enforcer``.

    :cloudformationResource: Aqua::Enterprise::Enforcer
    :link: https://github.com/aquasecurity/aqua-helm.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_id: typing.Optional[builtins.str] = None,
        kube_config: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        time_out: typing.Optional[jsii.Number] = None,
        value_override_url: typing.Optional[builtins.str] = None,
        values: typing.Any = None,
        value_yaml: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        vpc_configuration: typing.Optional[typing.Union["CfnEnforcerPropsVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Aqua::Enterprise::Enforcer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_id: EKS cluster name.
        :param kube_config: Secrets Manager ARN for kubeconfig file.
        :param name: Name for the helm release.
        :param namespace: Namespace to use with helm. Created if doesn't exist and default will be used if not provided
        :param role_arn: IAM to use with EKS cluster authentication, if not resource execution role will be used.
        :param time_out: Timeout for resource provider. Default 60 mins
        :param value_override_url: Custom Value Yaml file can optionally be specified.
        :param values: Custom Values can optionally be specified.
        :param value_yaml: String representation of a values.yaml file.
        :param version: Version can be specified, if not latest will be used.
        :param vpc_configuration: For network connectivity to Cluster inside VPC.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07cd63ecd41d21af25bca63ce4d52aec9441c949f942cdc5efec1c11f655b2a6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnforcerProps(
            cluster_id=cluster_id,
            kube_config=kube_config,
            name=name,
            namespace=namespace,
            role_arn=role_arn,
            time_out=time_out,
            value_override_url=value_override_url,
            values=values,
            value_yaml=value_yaml,
            version=version,
            vpc_configuration=vpc_configuration,
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
        '''Attribute ``Aqua::Enterprise::Enforcer.ID``.

        :link: https://github.com/aquasecurity/aqua-helm.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnEnforcerProps":
        '''Resource props.'''
        return typing.cast("CfnEnforcerProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/aqua-enterprise-enforcer.CfnEnforcerProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_id": "clusterId",
        "kube_config": "kubeConfig",
        "name": "name",
        "namespace": "namespace",
        "role_arn": "roleArn",
        "time_out": "timeOut",
        "value_override_url": "valueOverrideUrl",
        "values": "values",
        "value_yaml": "valueYaml",
        "version": "version",
        "vpc_configuration": "vpcConfiguration",
    },
)
class CfnEnforcerProps:
    def __init__(
        self,
        *,
        cluster_id: typing.Optional[builtins.str] = None,
        kube_config: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        time_out: typing.Optional[jsii.Number] = None,
        value_override_url: typing.Optional[builtins.str] = None,
        values: typing.Any = None,
        value_yaml: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        vpc_configuration: typing.Optional[typing.Union["CfnEnforcerPropsVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''A resource provider for Aqua Enterprise Enforcer.

        :param cluster_id: EKS cluster name.
        :param kube_config: Secrets Manager ARN for kubeconfig file.
        :param name: Name for the helm release.
        :param namespace: Namespace to use with helm. Created if doesn't exist and default will be used if not provided
        :param role_arn: IAM to use with EKS cluster authentication, if not resource execution role will be used.
        :param time_out: Timeout for resource provider. Default 60 mins
        :param value_override_url: Custom Value Yaml file can optionally be specified.
        :param values: Custom Values can optionally be specified.
        :param value_yaml: String representation of a values.yaml file.
        :param version: Version can be specified, if not latest will be used.
        :param vpc_configuration: For network connectivity to Cluster inside VPC.

        :schema: CfnEnforcerProps
        '''
        if isinstance(vpc_configuration, dict):
            vpc_configuration = CfnEnforcerPropsVpcConfiguration(**vpc_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49f800441bc6d4dacc2effd799ac7354ce8280837e3585304a9de2d49154302)
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument kube_config", value=kube_config, expected_type=type_hints["kube_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument time_out", value=time_out, expected_type=type_hints["time_out"])
            check_type(argname="argument value_override_url", value=value_override_url, expected_type=type_hints["value_override_url"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument value_yaml", value=value_yaml, expected_type=type_hints["value_yaml"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if kube_config is not None:
            self._values["kube_config"] = kube_config
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if time_out is not None:
            self._values["time_out"] = time_out
        if value_override_url is not None:
            self._values["value_override_url"] = value_override_url
        if values is not None:
            self._values["values"] = values
        if value_yaml is not None:
            self._values["value_yaml"] = value_yaml
        if version is not None:
            self._values["version"] = version
        if vpc_configuration is not None:
            self._values["vpc_configuration"] = vpc_configuration

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''EKS cluster name.

        :schema: CfnEnforcerProps#ClusterID
        '''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kube_config(self) -> typing.Optional[builtins.str]:
        '''Secrets Manager ARN for kubeconfig file.

        :schema: CfnEnforcerProps#KubeConfig
        '''
        result = self._values.get("kube_config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name for the helm release.

        :schema: CfnEnforcerProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to use with helm.

        Created if doesn't exist and default will be used if not provided

        :schema: CfnEnforcerProps#Namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''IAM to use with EKS cluster authentication, if not resource execution role will be used.

        :schema: CfnEnforcerProps#RoleArn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_out(self) -> typing.Optional[jsii.Number]:
        '''Timeout for resource provider.

        Default 60 mins

        :schema: CfnEnforcerProps#TimeOut
        '''
        result = self._values.get("time_out")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value_override_url(self) -> typing.Optional[builtins.str]:
        '''Custom Value Yaml file can optionally be specified.

        :schema: CfnEnforcerProps#ValueOverrideURL
        '''
        result = self._values.get("value_override_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Any:
        '''Custom Values can optionally be specified.

        :schema: CfnEnforcerProps#Values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Any, result)

    @builtins.property
    def value_yaml(self) -> typing.Optional[builtins.str]:
        '''String representation of a values.yaml file.

        :schema: CfnEnforcerProps#ValueYaml
        '''
        result = self._values.get("value_yaml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version can be specified, if not latest will be used.

        :schema: CfnEnforcerProps#Version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_configuration(self) -> typing.Optional["CfnEnforcerPropsVpcConfiguration"]:
        '''For network connectivity to Cluster inside VPC.

        :schema: CfnEnforcerProps#VPCConfiguration
        '''
        result = self._values.get("vpc_configuration")
        return typing.cast(typing.Optional["CfnEnforcerPropsVpcConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnforcerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/aqua-enterprise-enforcer.CfnEnforcerPropsVpcConfiguration",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class CfnEnforcerPropsVpcConfiguration:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''For network connectivity to Cluster inside VPC.

        :param security_group_ids: Specify one or more security groups.
        :param subnet_ids: Specify one or more subnets.

        :schema: CfnEnforcerPropsVpcConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dec2eaac30acbf4d39c0bd8d3318cfec2fb750f56e7bdcf2f4caa39a2a673e13)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more security groups.

        :schema: CfnEnforcerPropsVpcConfiguration#SecurityGroupIds
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more subnets.

        :schema: CfnEnforcerPropsVpcConfiguration#SubnetIds
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnforcerPropsVpcConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnforcer",
    "CfnEnforcerProps",
    "CfnEnforcerPropsVpcConfiguration",
]

publication.publish()

def _typecheckingstub__07cd63ecd41d21af25bca63ce4d52aec9441c949f942cdc5efec1c11f655b2a6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_id: typing.Optional[builtins.str] = None,
    kube_config: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    time_out: typing.Optional[jsii.Number] = None,
    value_override_url: typing.Optional[builtins.str] = None,
    values: typing.Any = None,
    value_yaml: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[CfnEnforcerPropsVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49f800441bc6d4dacc2effd799ac7354ce8280837e3585304a9de2d49154302(
    *,
    cluster_id: typing.Optional[builtins.str] = None,
    kube_config: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    time_out: typing.Optional[jsii.Number] = None,
    value_override_url: typing.Optional[builtins.str] = None,
    values: typing.Any = None,
    value_yaml: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[CfnEnforcerPropsVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec2eaac30acbf4d39c0bd8d3318cfec2fb750f56e7bdcf2f4caa39a2a673e13(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
