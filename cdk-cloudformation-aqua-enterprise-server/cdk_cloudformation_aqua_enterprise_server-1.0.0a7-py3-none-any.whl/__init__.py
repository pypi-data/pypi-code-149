'''
# aqua-enterprise-server

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `Aqua::Enterprise::Server` v1.0.0.

## Description

A resource provider for Aqua Enterprise Server.

## References

* [Source](https://github.com/aquasecurity/aqua-helm.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name Aqua::Enterprise::Server \
  --publisher-id 4f06bc39af5f4b984dd46ad17f10316e6258d9fa \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/4f06bc39af5f4b984dd46ad17f10316e6258d9fa/Aqua-Enterprise-Server \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `Aqua::Enterprise::Server`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Faqua-enterprise-server+v1.0.0).
* Issues related to `Aqua::Enterprise::Server` should be reported to the [publisher](https://github.com/aquasecurity/aqua-helm.git).

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


class CfnServer(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/aqua-enterprise-server.CfnServer",
):
    '''A CloudFormation ``Aqua::Enterprise::Server``.

    :cloudformationResource: Aqua::Enterprise::Server
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
        vpc_configuration: typing.Optional[typing.Union["CfnServerPropsVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``Aqua::Enterprise::Server``.

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
            type_hints = typing.get_type_hints(_typecheckingstub__062ed8f8b2cfd789839fb3712c4b9dc438fe7fd7121ddba62bdc713f6e9489e9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServerProps(
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
        '''Attribute ``Aqua::Enterprise::Server.ID``.

        :link: https://github.com/aquasecurity/aqua-helm.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnServerProps":
        '''Resource props.'''
        return typing.cast("CfnServerProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/aqua-enterprise-server.CfnServerProps",
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
class CfnServerProps:
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
        vpc_configuration: typing.Optional[typing.Union["CfnServerPropsVpcConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''A resource provider for Aqua Enterprise Server.

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

        :schema: CfnServerProps
        '''
        if isinstance(vpc_configuration, dict):
            vpc_configuration = CfnServerPropsVpcConfiguration(**vpc_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c420195ba4e82699d95c66226d3102dfebeccf8efb87a841ec219c8b05d8b81)
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

        :schema: CfnServerProps#ClusterID
        '''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kube_config(self) -> typing.Optional[builtins.str]:
        '''Secrets Manager ARN for kubeconfig file.

        :schema: CfnServerProps#KubeConfig
        '''
        result = self._values.get("kube_config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name for the helm release.

        :schema: CfnServerProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace to use with helm.

        Created if doesn't exist and default will be used if not provided

        :schema: CfnServerProps#Namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''IAM to use with EKS cluster authentication, if not resource execution role will be used.

        :schema: CfnServerProps#RoleArn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_out(self) -> typing.Optional[jsii.Number]:
        '''Timeout for resource provider.

        Default 60 mins

        :schema: CfnServerProps#TimeOut
        '''
        result = self._values.get("time_out")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value_override_url(self) -> typing.Optional[builtins.str]:
        '''Custom Value Yaml file can optionally be specified.

        :schema: CfnServerProps#ValueOverrideURL
        '''
        result = self._values.get("value_override_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Any:
        '''Custom Values can optionally be specified.

        :schema: CfnServerProps#Values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Any, result)

    @builtins.property
    def value_yaml(self) -> typing.Optional[builtins.str]:
        '''String representation of a values.yaml file.

        :schema: CfnServerProps#ValueYaml
        '''
        result = self._values.get("value_yaml")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version can be specified, if not latest will be used.

        :schema: CfnServerProps#Version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_configuration(self) -> typing.Optional["CfnServerPropsVpcConfiguration"]:
        '''For network connectivity to Cluster inside VPC.

        :schema: CfnServerProps#VPCConfiguration
        '''
        result = self._values.get("vpc_configuration")
        return typing.cast(typing.Optional["CfnServerPropsVpcConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/aqua-enterprise-server.CfnServerPropsVpcConfiguration",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class CfnServerPropsVpcConfiguration:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''For network connectivity to Cluster inside VPC.

        :param security_group_ids: Specify one or more security groups.
        :param subnet_ids: Specify one or more subnets.

        :schema: CfnServerPropsVpcConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f3dd125a9cccf6e23b97fa6d5c141fabafcf2a1a5c6ae99f6ca6b3c3c7ddd4)
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

        :schema: CfnServerPropsVpcConfiguration#SecurityGroupIds
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more subnets.

        :schema: CfnServerPropsVpcConfiguration#SubnetIds
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerPropsVpcConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnServer",
    "CfnServerProps",
    "CfnServerPropsVpcConfiguration",
]

publication.publish()

def _typecheckingstub__062ed8f8b2cfd789839fb3712c4b9dc438fe7fd7121ddba62bdc713f6e9489e9(
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
    vpc_configuration: typing.Optional[typing.Union[CfnServerPropsVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c420195ba4e82699d95c66226d3102dfebeccf8efb87a841ec219c8b05d8b81(
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
    vpc_configuration: typing.Optional[typing.Union[CfnServerPropsVpcConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f3dd125a9cccf6e23b97fa6d5c141fabafcf2a1a5c6ae99f6ca6b3c3c7ddd4(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
