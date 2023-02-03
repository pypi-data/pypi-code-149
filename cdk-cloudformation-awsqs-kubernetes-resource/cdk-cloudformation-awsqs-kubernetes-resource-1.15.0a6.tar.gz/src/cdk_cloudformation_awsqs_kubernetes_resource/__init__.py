'''
# awsqs-kubernetes-resource

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `AWSQS::Kubernetes::Resource` v1.15.0.

## Description

Applys a YAML manifest to the specified Kubernetes cluster

## References

* [Documentation](https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/README.md)
* [Source](https://github.com/aws-quickstart/quickstart-amazon-eks.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name AWSQS::Kubernetes::Resource \
  --publisher-id 408988dff9e863704bcc72e7e13f8d645cee8311 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-Kubernetes-Resource \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `AWSQS::Kubernetes::Resource`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fawsqs-kubernetes-resource+v1.15.0).
* Issues related to `AWSQS::Kubernetes::Resource` should be reported to the [publisher](https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/README.md).

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


class CfnResource(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-resource.CfnResource",
):
    '''A CloudFormation ``AWSQS::Kubernetes::Resource``.

    :cloudformationResource: AWSQS::Kubernetes::Resource
    :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        manifest: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWSQS::Kubernetes::Resource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: Name of the EKS cluster.
        :param manifest: Text representation of the kubernetes yaml manifests to apply to the cluster.
        :param namespace: Kubernetes namespace.
        :param url: Url to the kubernetes yaml manifests to apply to the cluster. Urls starting with s3:// will be fetched using an authenticated S3 read.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cacb8c9ae58171af8df797e08c0bf7bf64d468df423a48a18863b16c6d21717d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceProps(
            cluster_name=cluster_name, manifest=manifest, namespace=namespace, url=url
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCfnId")
    def attr_cfn_id(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.CfnId``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCfnId"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.Name``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceVersion")
    def attr_resource_version(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.ResourceVersion``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrSelfLink")
    def attr_self_link(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.SelfLink``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSelfLink"))

    @builtins.property
    @jsii.member(jsii_name="attrUid")
    def attr_uid(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Resource.Uid``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUid"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnResourceProps":
        '''Resource props.'''
        return typing.cast("CfnResourceProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-resource.CfnResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "manifest": "manifest",
        "namespace": "namespace",
        "url": "url",
    },
)
class CfnResourceProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        manifest: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Applys a YAML manifest to the specified Kubernetes cluster.

        :param cluster_name: Name of the EKS cluster.
        :param manifest: Text representation of the kubernetes yaml manifests to apply to the cluster.
        :param namespace: Kubernetes namespace.
        :param url: Url to the kubernetes yaml manifests to apply to the cluster. Urls starting with s3:// will be fetched using an authenticated S3 read.

        :schema: CfnResourceProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ae1778818011846aea6427e24048051c6ca2473c660682662204c6d5f176008)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
        }
        if manifest is not None:
            self._values["manifest"] = manifest
        if namespace is not None:
            self._values["namespace"] = namespace
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Name of the EKS cluster.

        :schema: CfnResourceProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def manifest(self) -> typing.Optional[builtins.str]:
        '''Text representation of the kubernetes yaml manifests to apply to the cluster.

        :schema: CfnResourceProps#Manifest
        '''
        result = self._values.get("manifest")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Kubernetes namespace.

        :schema: CfnResourceProps#Namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Url to the kubernetes yaml manifests to apply to the cluster.

        Urls starting with s3:// will be fetched using an authenticated S3 read.

        :schema: CfnResourceProps#Url
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnResource",
    "CfnResourceProps",
]

publication.publish()

def _typecheckingstub__cacb8c9ae58171af8df797e08c0bf7bf64d468df423a48a18863b16c6d21717d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_name: builtins.str,
    manifest: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae1778818011846aea6427e24048051c6ca2473c660682662204c6d5f176008(
    *,
    cluster_name: builtins.str,
    manifest: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
