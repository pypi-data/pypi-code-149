'''
# awsqs-kubernetes-get

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `AWSQS::Kubernetes::Get` v1.13.0.

## Description

Fetches data from a kubernetes cluster using jsonpath expressions.

## References

* [Documentation](https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/README.md)
* [Source](https://github.com/aws-quickstart/quickstart-amazon-eks.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name AWSQS::Kubernetes::Get \
  --publisher-id 408988dff9e863704bcc72e7e13f8d645cee8311 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-Kubernetes-Get \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `AWSQS::Kubernetes::Get`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fawsqs-kubernetes-get+v1.13.0).
* Issues related to `AWSQS::Kubernetes::Get` should be reported to the [publisher](https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/README.md).

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


class CfnGet(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-get.CfnGet",
):
    '''A CloudFormation ``AWSQS::Kubernetes::Get``.

    :cloudformationResource: AWSQS::Kubernetes::Get
    :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        json_path: builtins.str,
        name: builtins.str,
        namespace: builtins.str,
        retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWSQS::Kubernetes::Get``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: Name of the EKS cluster to query.
        :param json_path: Jsonpath expression to filter the output.
        :param name: Name of the kubernetes resource to query, should contain kind. Eg.: pod/nginx
        :param namespace: Kubernetes namespace containing the resource.
        :param retries: How many times to retry a request. This provides a mechanism to wait for resources to be created before proceeding. Interval between retries is 60 seconds.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea48087fc7cdbc95d0b64d04b37574b7cc6d9acac16f085e8a11a398146391ea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGetProps(
            cluster_name=cluster_name,
            json_path=json_path,
            name=name,
            namespace=namespace,
            retries=retries,
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
        '''Attribute ``AWSQS::Kubernetes::Get.Id``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrResponse")
    def attr_response(self) -> builtins.str:
        '''Attribute ``AWSQS::Kubernetes::Get.Response``.

        :link: https://github.com/aws-quickstart/quickstart-amazon-eks.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResponse"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnGetProps":
        '''Resource props.'''
        return typing.cast("CfnGetProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-kubernetes-get.CfnGetProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "json_path": "jsonPath",
        "name": "name",
        "namespace": "namespace",
        "retries": "retries",
    },
)
class CfnGetProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        json_path: builtins.str,
        name: builtins.str,
        namespace: builtins.str,
        retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Fetches data from a kubernetes cluster using jsonpath expressions.

        :param cluster_name: Name of the EKS cluster to query.
        :param json_path: Jsonpath expression to filter the output.
        :param name: Name of the kubernetes resource to query, should contain kind. Eg.: pod/nginx
        :param namespace: Kubernetes namespace containing the resource.
        :param retries: How many times to retry a request. This provides a mechanism to wait for resources to be created before proceeding. Interval between retries is 60 seconds.

        :schema: CfnGetProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb3b7ad6d5a3f4da46826ce169372e8caa8352df426e7221f386800aefe37f8)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument json_path", value=json_path, expected_type=type_hints["json_path"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "json_path": json_path,
            "name": name,
            "namespace": namespace,
        }
        if retries is not None:
            self._values["retries"] = retries

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Name of the EKS cluster to query.

        :schema: CfnGetProps#ClusterName
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def json_path(self) -> builtins.str:
        '''Jsonpath expression to filter the output.

        :schema: CfnGetProps#JsonPath
        '''
        result = self._values.get("json_path")
        assert result is not None, "Required property 'json_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the kubernetes resource to query, should contain kind.

        Eg.: pod/nginx

        :schema: CfnGetProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''Kubernetes namespace containing the resource.

        :schema: CfnGetProps#Namespace
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''How many times to retry a request.

        This provides a mechanism to wait for resources to be created before proceeding. Interval between retries is 60 seconds.

        :schema: CfnGetProps#Retries
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGet",
    "CfnGetProps",
]

publication.publish()

def _typecheckingstub__ea48087fc7cdbc95d0b64d04b37574b7cc6d9acac16f085e8a11a398146391ea(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_name: builtins.str,
    json_path: builtins.str,
    name: builtins.str,
    namespace: builtins.str,
    retries: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb3b7ad6d5a3f4da46826ce169372e8caa8352df426e7221f386800aefe37f8(
    *,
    cluster_name: builtins.str,
    json_path: builtins.str,
    name: builtins.str,
    namespace: builtins.str,
    retries: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
