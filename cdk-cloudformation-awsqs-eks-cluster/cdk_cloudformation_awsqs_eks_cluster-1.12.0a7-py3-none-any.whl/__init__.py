'''
# awsqs-eks-cluster

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `AWSQS::EKS::Cluster` v1.12.0.

## Description

A resource that creates Amazon Elastic Kubernetes Service (Amazon EKS) clusters.

## References

* [Documentation](https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider/blob/main/README.md)
* [Source](https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name AWSQS::EKS::Cluster \
  --publisher-id 408988dff9e863704bcc72e7e13f8d645cee8311 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-EKS-Cluster \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `AWSQS::EKS::Cluster`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fawsqs-eks-cluster+v1.12.0).
* Issues related to `AWSQS::EKS::Cluster` should be reported to the [publisher](https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider/blob/main/README.md).

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


class CfnCluster(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.CfnCluster",
):
    '''A CloudFormation ``AWSQS::EKS::Cluster``.

    :cloudformationResource: AWSQS::EKS::Cluster
    :link: https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resources_vpc_config: typing.Union["CfnClusterPropsResourcesVpcConfig", typing.Dict[builtins.str, typing.Any]],
        role_arn: builtins.str,
        enabled_cluster_logging_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        encryption_config: typing.Optional[typing.Sequence[typing.Union["EncryptionConfigEntry", typing.Dict[builtins.str, typing.Any]]]] = None,
        kubernetes_api_access: typing.Optional[typing.Union["CfnClusterPropsKubernetesApiAccess", typing.Dict[builtins.str, typing.Any]]] = None,
        kubernetes_network_config: typing.Optional[typing.Union["CfnClusterPropsKubernetesNetworkConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_role_name: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnClusterPropsTags", typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWSQS::EKS::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resources_vpc_config: An object that represents the virtual private cloud (VPC) configuration to use for an Amazon EKS cluster.
        :param role_arn: Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role. This provides permissions for Amazon EKS to call other AWS APIs.
        :param enabled_cluster_logging_types: Enables exporting of logs from the Kubernetes control plane to Amazon CloudWatch Logs. By default, logs from the cluster control plane are not exported to CloudWatch Logs. The valid log types are api, audit, authenticator, controllerManager, and scheduler.
        :param encryption_config: Encryption configuration for the cluster.
        :param kubernetes_api_access: 
        :param kubernetes_network_config: Network configuration for Amazon EKS cluster.
        :param lambda_role_name: Name of the AWS Identity and Access Management (IAM) role used for clusters that have the public endpoint disabled. this provides permissions for Lambda to be invoked and attach to the cluster VPC
        :param name: A unique name for your cluster.
        :param tags: 
        :param version: Desired Kubernetes version for your cluster. If you don't specify this value, the cluster uses the latest version from Amazon EKS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b40ebd6b5254b51eeb43ba9ec5ca4096b9f78ae75f2a3ffffab482b6e5e25ed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            resources_vpc_config=resources_vpc_config,
            role_arn=role_arn,
            enabled_cluster_logging_types=enabled_cluster_logging_types,
            encryption_config=encryption_config,
            kubernetes_api_access=kubernetes_api_access,
            kubernetes_network_config=kubernetes_network_config,
            lambda_role_name=lambda_role_name,
            name=name,
            tags=tags,
            version=version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Attribute ``AWSQS::EKS::Cluster.Arn``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCertificateAuthorityData")
    def attr_certificate_authority_data(self) -> builtins.str:
        '''Attribute ``AWSQS::EKS::Cluster.CertificateAuthorityData``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificateAuthorityData"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterSecurityGroupId")
    def attr_cluster_security_group_id(self) -> builtins.str:
        '''Attribute ``AWSQS::EKS::Cluster.ClusterSecurityGroupId``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterSecurityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="attrEncryptionConfigKeyArn")
    def attr_encryption_config_key_arn(self) -> builtins.str:
        '''Attribute ``AWSQS::EKS::Cluster.EncryptionConfigKeyArn``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEncryptionConfigKeyArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''Attribute ``AWSQS::EKS::Cluster.Endpoint``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrOIDCIssuerURL")
    def attr_oidc_issuer_url(self) -> builtins.str:
        '''Attribute ``AWSQS::EKS::Cluster.OIDCIssuerURL``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOIDCIssuerURL"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnClusterProps":
        '''Resource props.'''
        return typing.cast("CfnClusterProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "resources_vpc_config": "resourcesVpcConfig",
        "role_arn": "roleArn",
        "enabled_cluster_logging_types": "enabledClusterLoggingTypes",
        "encryption_config": "encryptionConfig",
        "kubernetes_api_access": "kubernetesApiAccess",
        "kubernetes_network_config": "kubernetesNetworkConfig",
        "lambda_role_name": "lambdaRoleName",
        "name": "name",
        "tags": "tags",
        "version": "version",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        resources_vpc_config: typing.Union["CfnClusterPropsResourcesVpcConfig", typing.Dict[builtins.str, typing.Any]],
        role_arn: builtins.str,
        enabled_cluster_logging_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        encryption_config: typing.Optional[typing.Sequence[typing.Union["EncryptionConfigEntry", typing.Dict[builtins.str, typing.Any]]]] = None,
        kubernetes_api_access: typing.Optional[typing.Union["CfnClusterPropsKubernetesApiAccess", typing.Dict[builtins.str, typing.Any]]] = None,
        kubernetes_network_config: typing.Optional[typing.Union["CfnClusterPropsKubernetesNetworkConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_role_name: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnClusterPropsTags", typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A resource that creates Amazon Elastic Kubernetes Service (Amazon EKS) clusters.

        :param resources_vpc_config: An object that represents the virtual private cloud (VPC) configuration to use for an Amazon EKS cluster.
        :param role_arn: Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role. This provides permissions for Amazon EKS to call other AWS APIs.
        :param enabled_cluster_logging_types: Enables exporting of logs from the Kubernetes control plane to Amazon CloudWatch Logs. By default, logs from the cluster control plane are not exported to CloudWatch Logs. The valid log types are api, audit, authenticator, controllerManager, and scheduler.
        :param encryption_config: Encryption configuration for the cluster.
        :param kubernetes_api_access: 
        :param kubernetes_network_config: Network configuration for Amazon EKS cluster.
        :param lambda_role_name: Name of the AWS Identity and Access Management (IAM) role used for clusters that have the public endpoint disabled. this provides permissions for Lambda to be invoked and attach to the cluster VPC
        :param name: A unique name for your cluster.
        :param tags: 
        :param version: Desired Kubernetes version for your cluster. If you don't specify this value, the cluster uses the latest version from Amazon EKS.

        :schema: CfnClusterProps
        '''
        if isinstance(resources_vpc_config, dict):
            resources_vpc_config = CfnClusterPropsResourcesVpcConfig(**resources_vpc_config)
        if isinstance(kubernetes_api_access, dict):
            kubernetes_api_access = CfnClusterPropsKubernetesApiAccess(**kubernetes_api_access)
        if isinstance(kubernetes_network_config, dict):
            kubernetes_network_config = CfnClusterPropsKubernetesNetworkConfig(**kubernetes_network_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4adb3cc45f1f20208ad8a2441c9d065e1e7d01599567c61801489d63bf7fee0d)
            check_type(argname="argument resources_vpc_config", value=resources_vpc_config, expected_type=type_hints["resources_vpc_config"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument enabled_cluster_logging_types", value=enabled_cluster_logging_types, expected_type=type_hints["enabled_cluster_logging_types"])
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            check_type(argname="argument kubernetes_api_access", value=kubernetes_api_access, expected_type=type_hints["kubernetes_api_access"])
            check_type(argname="argument kubernetes_network_config", value=kubernetes_network_config, expected_type=type_hints["kubernetes_network_config"])
            check_type(argname="argument lambda_role_name", value=lambda_role_name, expected_type=type_hints["lambda_role_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resources_vpc_config": resources_vpc_config,
            "role_arn": role_arn,
        }
        if enabled_cluster_logging_types is not None:
            self._values["enabled_cluster_logging_types"] = enabled_cluster_logging_types
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config
        if kubernetes_api_access is not None:
            self._values["kubernetes_api_access"] = kubernetes_api_access
        if kubernetes_network_config is not None:
            self._values["kubernetes_network_config"] = kubernetes_network_config
        if lambda_role_name is not None:
            self._values["lambda_role_name"] = lambda_role_name
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def resources_vpc_config(self) -> "CfnClusterPropsResourcesVpcConfig":
        '''An object that represents the virtual private cloud (VPC) configuration to use for an Amazon EKS cluster.

        :schema: CfnClusterProps#ResourcesVpcConfig
        '''
        result = self._values.get("resources_vpc_config")
        assert result is not None, "Required property 'resources_vpc_config' is missing"
        return typing.cast("CfnClusterPropsResourcesVpcConfig", result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role.

        This provides permissions for Amazon EKS to call other AWS APIs.

        :schema: CfnClusterProps#RoleArn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled_cluster_logging_types(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Enables exporting of logs from the Kubernetes control plane to Amazon CloudWatch Logs.

        By default, logs from the cluster control plane are not exported to CloudWatch Logs. The valid log types are api, audit, authenticator, controllerManager, and scheduler.

        :schema: CfnClusterProps#EnabledClusterLoggingTypes
        '''
        result = self._values.get("enabled_cluster_logging_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def encryption_config(
        self,
    ) -> typing.Optional[typing.List["EncryptionConfigEntry"]]:
        '''Encryption configuration for the cluster.

        :schema: CfnClusterProps#EncryptionConfig
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Optional[typing.List["EncryptionConfigEntry"]], result)

    @builtins.property
    def kubernetes_api_access(
        self,
    ) -> typing.Optional["CfnClusterPropsKubernetesApiAccess"]:
        '''
        :schema: CfnClusterProps#KubernetesApiAccess
        '''
        result = self._values.get("kubernetes_api_access")
        return typing.cast(typing.Optional["CfnClusterPropsKubernetesApiAccess"], result)

    @builtins.property
    def kubernetes_network_config(
        self,
    ) -> typing.Optional["CfnClusterPropsKubernetesNetworkConfig"]:
        '''Network configuration for Amazon EKS cluster.

        :schema: CfnClusterProps#KubernetesNetworkConfig
        '''
        result = self._values.get("kubernetes_network_config")
        return typing.cast(typing.Optional["CfnClusterPropsKubernetesNetworkConfig"], result)

    @builtins.property
    def lambda_role_name(self) -> typing.Optional[builtins.str]:
        '''Name of the AWS Identity and Access Management (IAM) role used for clusters that have the public endpoint disabled.

        this provides permissions for Lambda to be invoked and attach to the cluster VPC

        :schema: CfnClusterProps#LambdaRoleName
        '''
        result = self._values.get("lambda_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A unique name for your cluster.

        :schema: CfnClusterProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnClusterPropsTags"]]:
        '''
        :schema: CfnClusterProps#Tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["CfnClusterPropsTags"]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Desired Kubernetes version for your cluster.

        If you don't specify this value, the cluster uses the latest version from Amazon EKS.

        :schema: CfnClusterProps#Version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.CfnClusterPropsKubernetesApiAccess",
    jsii_struct_bases=[],
    name_mapping={"roles": "roles", "users": "users"},
)
class CfnClusterPropsKubernetesApiAccess:
    def __init__(
        self,
        *,
        roles: typing.Optional[typing.Sequence[typing.Union["KubernetesApiAccessEntry", typing.Dict[builtins.str, typing.Any]]]] = None,
        users: typing.Optional[typing.Sequence[typing.Union["KubernetesApiAccessEntry", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param roles: 
        :param users: 

        :schema: CfnClusterPropsKubernetesApiAccess
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef368ce519212a8dab9a03623ff59f00b4a6411b49e07a86d0320b7c51373174)
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if roles is not None:
            self._values["roles"] = roles
        if users is not None:
            self._values["users"] = users

    @builtins.property
    def roles(self) -> typing.Optional[typing.List["KubernetesApiAccessEntry"]]:
        '''
        :schema: CfnClusterPropsKubernetesApiAccess#Roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List["KubernetesApiAccessEntry"]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List["KubernetesApiAccessEntry"]]:
        '''
        :schema: CfnClusterPropsKubernetesApiAccess#Users
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List["KubernetesApiAccessEntry"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsKubernetesApiAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.CfnClusterPropsKubernetesNetworkConfig",
    jsii_struct_bases=[],
    name_mapping={"service_ipv4_cidr": "serviceIpv4Cidr"},
)
class CfnClusterPropsKubernetesNetworkConfig:
    def __init__(
        self,
        *,
        service_ipv4_cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Network configuration for Amazon EKS cluster.

        :param service_ipv4_cidr: Specify the range from which cluster services will receive IPv4 addresses.

        :schema: CfnClusterPropsKubernetesNetworkConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14bcf65e74c0fd3e4779f926b2f0ee58ca0073140b3b8fad1ab5d091b3a55ab4)
            check_type(argname="argument service_ipv4_cidr", value=service_ipv4_cidr, expected_type=type_hints["service_ipv4_cidr"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if service_ipv4_cidr is not None:
            self._values["service_ipv4_cidr"] = service_ipv4_cidr

    @builtins.property
    def service_ipv4_cidr(self) -> typing.Optional[builtins.str]:
        '''Specify the range from which cluster services will receive IPv4 addresses.

        :schema: CfnClusterPropsKubernetesNetworkConfig#ServiceIpv4Cidr
        '''
        result = self._values.get("service_ipv4_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsKubernetesNetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.CfnClusterPropsResourcesVpcConfig",
    jsii_struct_bases=[],
    name_mapping={
        "subnet_ids": "subnetIds",
        "endpoint_private_access": "endpointPrivateAccess",
        "endpoint_public_access": "endpointPublicAccess",
        "public_access_cidrs": "publicAccessCidrs",
        "security_group_ids": "securityGroupIds",
    },
)
class CfnClusterPropsResourcesVpcConfig:
    def __init__(
        self,
        *,
        subnet_ids: typing.Sequence[builtins.str],
        endpoint_private_access: typing.Optional[builtins.bool] = None,
        endpoint_public_access: typing.Optional[builtins.bool] = None,
        public_access_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''An object that represents the virtual private cloud (VPC) configuration to use for an Amazon EKS cluster.

        :param subnet_ids: Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.
        :param endpoint_private_access: Set this value to true to enable private access for your cluster's Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster's VPC use the private VPC endpoint. The default value for this parameter is false , which disables private access for your Kubernetes API server. If you disable private access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods.
        :param endpoint_public_access: Set this value to false to disable public access to your cluster's Kubernetes API server endpoint. If you disable public access, your cluster's Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is true , which enables public access for your Kubernetes API server.
        :param public_access_cidrs: The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is 0.0.0.0/0 . If you've disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that you specify the necessary CIDR blocks.
        :param security_group_ids: Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane. If you don't specify a security group, the default security group for your VPC is used.

        :schema: CfnClusterPropsResourcesVpcConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11ac0108fb0efc6d50e2fdea0b94adfafb18800239fde7223eb08e2c72c8477f)
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument endpoint_private_access", value=endpoint_private_access, expected_type=type_hints["endpoint_private_access"])
            check_type(argname="argument endpoint_public_access", value=endpoint_public_access, expected_type=type_hints["endpoint_public_access"])
            check_type(argname="argument public_access_cidrs", value=public_access_cidrs, expected_type=type_hints["public_access_cidrs"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_ids": subnet_ids,
        }
        if endpoint_private_access is not None:
            self._values["endpoint_private_access"] = endpoint_private_access
        if endpoint_public_access is not None:
            self._values["endpoint_public_access"] = endpoint_public_access
        if public_access_cidrs is not None:
            self._values["public_access_cidrs"] = public_access_cidrs
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Specify subnets for your Amazon EKS worker nodes.

        Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.

        :schema: CfnClusterPropsResourcesVpcConfig#SubnetIds
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def endpoint_private_access(self) -> typing.Optional[builtins.bool]:
        '''Set this value to true to enable private access for your cluster's Kubernetes API server endpoint.

        If you enable private access, Kubernetes API requests from within your cluster's VPC use the private VPC endpoint. The default value for this parameter is false , which disables private access for your Kubernetes API server. If you disable private access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods.

        :schema: CfnClusterPropsResourcesVpcConfig#EndpointPrivateAccess
        '''
        result = self._values.get("endpoint_private_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def endpoint_public_access(self) -> typing.Optional[builtins.bool]:
        '''Set this value to false to disable public access to your cluster's Kubernetes API server endpoint.

        If you disable public access, your cluster's Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is true , which enables public access for your Kubernetes API server.

        :schema: CfnClusterPropsResourcesVpcConfig#EndpointPublicAccess
        '''
        result = self._values.get("endpoint_public_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_access_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint.

        Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is 0.0.0.0/0 . If you've disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that you specify the necessary CIDR blocks.

        :schema: CfnClusterPropsResourcesVpcConfig#PublicAccessCidrs
        '''
        result = self._values.get("public_access_cidrs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane.

        If you don't specify a security group, the default security group for your VPC is used.

        :schema: CfnClusterPropsResourcesVpcConfig#SecurityGroupIds
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsResourcesVpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.CfnClusterPropsTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class CfnClusterPropsTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: 
        :param value: 

        :schema: CfnClusterPropsTags
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60468a10b110db1069fb738a2561253e332cc4225c24feaf4043b4eb522dcdc1)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''
        :schema: CfnClusterPropsTags#Key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''
        :schema: CfnClusterPropsTags#Value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.EncryptionConfigEntry",
    jsii_struct_bases=[],
    name_mapping={"provider": "provider", "resources": "resources"},
)
class EncryptionConfigEntry:
    def __init__(
        self,
        *,
        provider: typing.Optional[typing.Union["Provider", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''The encryption configuration for the cluster.

        :param provider: 
        :param resources: Specifies the resources to be encrypted. The only supported value is "secrets".

        :schema: EncryptionConfigEntry
        '''
        if isinstance(provider, dict):
            provider = Provider(**provider)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afaa1083364c6705e18393afb60b6628b74e37664afc11f25e86067680e95579)
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if provider is not None:
            self._values["provider"] = provider
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def provider(self) -> typing.Optional["Provider"]:
        '''
        :schema: EncryptionConfigEntry#Provider
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional["Provider"], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the resources to be encrypted.

        The only supported value is "secrets".

        :schema: EncryptionConfigEntry#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncryptionConfigEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.KubernetesApiAccessEntry",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "groups": "groups", "username": "username"},
)
class KubernetesApiAccessEntry:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param arn: 
        :param groups: 
        :param username: 

        :schema: KubernetesApiAccessEntry
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4000e7af0066e25a9e8dd58b1832bb6079179c9d786f756f8f7a74eed10bc0cd)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if groups is not None:
            self._values["groups"] = groups
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KubernetesApiAccessEntry#Arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: KubernetesApiAccessEntry#Groups
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''
        :schema: KubernetesApiAccessEntry#Username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesApiAccessEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-eks-cluster.Provider",
    jsii_struct_bases=[],
    name_mapping={"key_arn": "keyArn"},
)
class Provider:
    def __init__(self, *, key_arn: typing.Optional[builtins.str] = None) -> None:
        '''AWS Key Management Service (AWS KMS) customer master key (CMK).

        Either the ARN or the alias can be used.

        :param key_arn: Amazon Resource Name (ARN) or alias of the customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK.

        :schema: Provider
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4faa9b7e53ba458bdeae48f126c5b95748c407f7dc8c8fa505d174015f9c8f3)
            check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key_arn is not None:
            self._values["key_arn"] = key_arn

    @builtins.property
    def key_arn(self) -> typing.Optional[builtins.str]:
        '''Amazon Resource Name (ARN) or alias of the customer master key (CMK).

        The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK.

        :schema: Provider#KeyArn
        '''
        result = self._values.get("key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Provider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
    "CfnClusterPropsKubernetesApiAccess",
    "CfnClusterPropsKubernetesNetworkConfig",
    "CfnClusterPropsResourcesVpcConfig",
    "CfnClusterPropsTags",
    "EncryptionConfigEntry",
    "KubernetesApiAccessEntry",
    "Provider",
]

publication.publish()

def _typecheckingstub__6b40ebd6b5254b51eeb43ba9ec5ca4096b9f78ae75f2a3ffffab482b6e5e25ed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resources_vpc_config: typing.Union[CfnClusterPropsResourcesVpcConfig, typing.Dict[builtins.str, typing.Any]],
    role_arn: builtins.str,
    enabled_cluster_logging_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    encryption_config: typing.Optional[typing.Sequence[typing.Union[EncryptionConfigEntry, typing.Dict[builtins.str, typing.Any]]]] = None,
    kubernetes_api_access: typing.Optional[typing.Union[CfnClusterPropsKubernetesApiAccess, typing.Dict[builtins.str, typing.Any]]] = None,
    kubernetes_network_config: typing.Optional[typing.Union[CfnClusterPropsKubernetesNetworkConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_role_name: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnClusterPropsTags, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4adb3cc45f1f20208ad8a2441c9d065e1e7d01599567c61801489d63bf7fee0d(
    *,
    resources_vpc_config: typing.Union[CfnClusterPropsResourcesVpcConfig, typing.Dict[builtins.str, typing.Any]],
    role_arn: builtins.str,
    enabled_cluster_logging_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    encryption_config: typing.Optional[typing.Sequence[typing.Union[EncryptionConfigEntry, typing.Dict[builtins.str, typing.Any]]]] = None,
    kubernetes_api_access: typing.Optional[typing.Union[CfnClusterPropsKubernetesApiAccess, typing.Dict[builtins.str, typing.Any]]] = None,
    kubernetes_network_config: typing.Optional[typing.Union[CfnClusterPropsKubernetesNetworkConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_role_name: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnClusterPropsTags, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef368ce519212a8dab9a03623ff59f00b4a6411b49e07a86d0320b7c51373174(
    *,
    roles: typing.Optional[typing.Sequence[typing.Union[KubernetesApiAccessEntry, typing.Dict[builtins.str, typing.Any]]]] = None,
    users: typing.Optional[typing.Sequence[typing.Union[KubernetesApiAccessEntry, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14bcf65e74c0fd3e4779f926b2f0ee58ca0073140b3b8fad1ab5d091b3a55ab4(
    *,
    service_ipv4_cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ac0108fb0efc6d50e2fdea0b94adfafb18800239fde7223eb08e2c72c8477f(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    endpoint_private_access: typing.Optional[builtins.bool] = None,
    endpoint_public_access: typing.Optional[builtins.bool] = None,
    public_access_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60468a10b110db1069fb738a2561253e332cc4225c24feaf4043b4eb522dcdc1(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afaa1083364c6705e18393afb60b6628b74e37664afc11f25e86067680e95579(
    *,
    provider: typing.Optional[typing.Union[Provider, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4000e7af0066e25a9e8dd58b1832bb6079179c9d786f756f8f7a74eed10bc0cd(
    *,
    arn: typing.Optional[builtins.str] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4faa9b7e53ba458bdeae48f126c5b95748c407f7dc8c8fa505d174015f9c8f3(
    *,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
