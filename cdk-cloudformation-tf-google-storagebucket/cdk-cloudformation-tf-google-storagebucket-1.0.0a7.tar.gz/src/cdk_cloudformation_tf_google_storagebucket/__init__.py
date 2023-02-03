'''
# tf-google-storagebucket

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `TF::Google::StorageBucket` v1.0.0.

## Description

Creates a new bucket in Google cloud storage service (GCS).
Once a bucket has been created, its location can't be changed.

For more information see
[the official documentation](https://cloud.google.com/storage/docs/overview)
and
[API](https://cloud.google.com/storage/docs/json_api/v1/buckets).

**Note**: If the project id is not set on the resource or in the provider block it will be dynamically
determined which will require enabling the compute api.

## References

* [Documentation](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/google/TF-Google-StorageBucket/docs/README.md)
* [Source](https://github.com/iann0036/cfn-tf-custom-types.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name TF::Google::StorageBucket \
  --publisher-id e1238fdd31aee1839e14fb3fb2dac9db154dae29 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/e1238fdd31aee1839e14fb3fb2dac9db154dae29/TF-Google-StorageBucket \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `TF::Google::StorageBucket`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Ftf-google-storagebucket+v1.0.0).
* Issues related to `TF::Google::StorageBucket` should be reported to the [publisher](https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/google/TF-Google-StorageBucket/docs/README.md).

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
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.ActionDefinition",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "storage_class": "storageClass"},
)
class ActionDefinition:
    def __init__(
        self,
        *,
        type: builtins.str,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The type of the action of this Lifecycle Rule. Supported values include: ``Delete`` and ``SetStorageClass``.
        :param storage_class: The target `Storage Class <https://cloud.google.com/storage/docs/storage-classes>`_ of objects affected by this Lifecycle Rule. Supported values include: ``STANDARD``, ``MULTI_REGIONAL``, ``REGIONAL``, ``NEARLINE``, ``COLDLINE``, ``ARCHIVE``.

        :schema: ActionDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa6d59e9c697b677e5e31f9b7eb7e9dd7232347089b25ee242c9d75c0e117987)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the action of this Lifecycle Rule.

        Supported values include: ``Delete`` and ``SetStorageClass``.

        :schema: ActionDefinition#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''The target `Storage Class <https://cloud.google.com/storage/docs/storage-classes>`_ of objects affected by this Lifecycle Rule. Supported values include: ``STANDARD``, ``MULTI_REGIONAL``, ``REGIONAL``, ``NEARLINE``, ``COLDLINE``, ``ARCHIVE``.

        :schema: ActionDefinition#StorageClass
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnStorageBucket(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.CfnStorageBucket",
):
    '''A CloudFormation ``TF::Google::StorageBucket``.

    :cloudformationResource: TF::Google::StorageBucket
    :link: https://github.com/iann0036/cfn-tf-custom-types.git
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        bucket_policy_only: typing.Optional[builtins.bool] = None,
        cors: typing.Optional[typing.Sequence[typing.Union["CorsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_event_based_hold: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[typing.Sequence[typing.Union["EncryptionDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        force_destroy: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["LabelsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        lifecycle_rule: typing.Optional[typing.Sequence[typing.Union["LifecycleRuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        location: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Sequence[typing.Union["LoggingDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        project: typing.Optional[builtins.str] = None,
        requester_pays: typing.Optional[builtins.bool] = None,
        retention_policy: typing.Optional[typing.Sequence[typing.Union["RetentionPolicyDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        storage_class: typing.Optional[builtins.str] = None,
        uniform_bucket_level_access: typing.Optional[builtins.bool] = None,
        versioning: typing.Optional[typing.Sequence[typing.Union["VersioningDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        website: typing.Optional[typing.Sequence[typing.Union["WebsiteDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``TF::Google::StorageBucket``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the bucket.
        :param bucket_policy_only: Enables `Bucket Policy Only <https://cloud.google.com/storage/docs/bucket-policy-only>`_ access to a bucket. This field will be removed in the next major release of the provider.
        :param cors: 
        :param default_event_based_hold: 
        :param encryption: 
        :param force_destroy: When deleting a bucket, this boolean option will delete all contained objects. If you try to delete a bucket that contains objects, Terraform will fail that run.
        :param labels: A map of key/value label pairs to assign to the bucket.
        :param lifecycle_rule: 
        :param location: The `GCS location <https://cloud.google.com/storage/docs/bucket-locations>`_.
        :param logging: 
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        :param requester_pays: Enables `Requester Pays <https://cloud.google.com/storage/docs/requester-pays>`_ on a storage bucket.
        :param retention_policy: 
        :param storage_class: The `Storage Class <https://cloud.google.com/storage/docs/storage-classes>`_ of the new bucket. Supported values include: ``STANDARD``, ``MULTI_REGIONAL``, ``REGIONAL``, ``NEARLINE``, ``COLDLINE``, ``ARCHIVE``.
        :param uniform_bucket_level_access: Enables `Uniform bucket-level access <https://cloud.google.com/storage/docs/uniform-bucket-level-access>`_ access to a bucket.
        :param versioning: 
        :param website: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955975cb17a5edf68d3a4886331581e9e8e161ab156a95f548463e9ad1374bf5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStorageBucketProps(
            name=name,
            bucket_policy_only=bucket_policy_only,
            cors=cors,
            default_event_based_hold=default_event_based_hold,
            encryption=encryption,
            force_destroy=force_destroy,
            labels=labels,
            lifecycle_rule=lifecycle_rule,
            location=location,
            logging=logging,
            project=project,
            requester_pays=requester_pays,
            retention_policy=retention_policy,
            storage_class=storage_class,
            uniform_bucket_level_access=uniform_bucket_level_access,
            versioning=versioning,
            website=website,
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
        '''Attribute ``TF::Google::StorageBucket.Id``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSelfLink")
    def attr_self_link(self) -> builtins.str:
        '''Attribute ``TF::Google::StorageBucket.SelfLink``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSelfLink"))

    @builtins.property
    @jsii.member(jsii_name="attrTfcfnid")
    def attr_tfcfnid(self) -> builtins.str:
        '''Attribute ``TF::Google::StorageBucket.tfcfnid``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTfcfnid"))

    @builtins.property
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''Attribute ``TF::Google::StorageBucket.Url``.

        :link: https://github.com/iann0036/cfn-tf-custom-types.git
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnStorageBucketProps":
        '''Resource props.'''
        return typing.cast("CfnStorageBucketProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.CfnStorageBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "bucket_policy_only": "bucketPolicyOnly",
        "cors": "cors",
        "default_event_based_hold": "defaultEventBasedHold",
        "encryption": "encryption",
        "force_destroy": "forceDestroy",
        "labels": "labels",
        "lifecycle_rule": "lifecycleRule",
        "location": "location",
        "logging": "logging",
        "project": "project",
        "requester_pays": "requesterPays",
        "retention_policy": "retentionPolicy",
        "storage_class": "storageClass",
        "uniform_bucket_level_access": "uniformBucketLevelAccess",
        "versioning": "versioning",
        "website": "website",
    },
)
class CfnStorageBucketProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        bucket_policy_only: typing.Optional[builtins.bool] = None,
        cors: typing.Optional[typing.Sequence[typing.Union["CorsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_event_based_hold: typing.Optional[builtins.bool] = None,
        encryption: typing.Optional[typing.Sequence[typing.Union["EncryptionDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        force_destroy: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["LabelsDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        lifecycle_rule: typing.Optional[typing.Sequence[typing.Union["LifecycleRuleDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        location: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Sequence[typing.Union["LoggingDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        project: typing.Optional[builtins.str] = None,
        requester_pays: typing.Optional[builtins.bool] = None,
        retention_policy: typing.Optional[typing.Sequence[typing.Union["RetentionPolicyDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        storage_class: typing.Optional[builtins.str] = None,
        uniform_bucket_level_access: typing.Optional[builtins.bool] = None,
        versioning: typing.Optional[typing.Sequence[typing.Union["VersioningDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
        website: typing.Optional[typing.Sequence[typing.Union["WebsiteDefinition", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Creates a new bucket in Google cloud storage service (GCS).

        Once a bucket has been created, its location can't be changed.

        For more information see
        `the official documentation <https://cloud.google.com/storage/docs/overview>`_
        and
        `API <https://cloud.google.com/storage/docs/json_api/v1/buckets>`_.

        **Note**: If the project id is not set on the resource or in the provider block it will be dynamically
        determined which will require enabling the compute api.

        :param name: The name of the bucket.
        :param bucket_policy_only: Enables `Bucket Policy Only <https://cloud.google.com/storage/docs/bucket-policy-only>`_ access to a bucket. This field will be removed in the next major release of the provider.
        :param cors: 
        :param default_event_based_hold: 
        :param encryption: 
        :param force_destroy: When deleting a bucket, this boolean option will delete all contained objects. If you try to delete a bucket that contains objects, Terraform will fail that run.
        :param labels: A map of key/value label pairs to assign to the bucket.
        :param lifecycle_rule: 
        :param location: The `GCS location <https://cloud.google.com/storage/docs/bucket-locations>`_.
        :param logging: 
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used.
        :param requester_pays: Enables `Requester Pays <https://cloud.google.com/storage/docs/requester-pays>`_ on a storage bucket.
        :param retention_policy: 
        :param storage_class: The `Storage Class <https://cloud.google.com/storage/docs/storage-classes>`_ of the new bucket. Supported values include: ``STANDARD``, ``MULTI_REGIONAL``, ``REGIONAL``, ``NEARLINE``, ``COLDLINE``, ``ARCHIVE``.
        :param uniform_bucket_level_access: Enables `Uniform bucket-level access <https://cloud.google.com/storage/docs/uniform-bucket-level-access>`_ access to a bucket.
        :param versioning: 
        :param website: 

        :schema: CfnStorageBucketProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5466a6cce4e0d2cccc6056e2456f7ec990ef1baffa4c19e5eeeaa1a289c75ab5)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument bucket_policy_only", value=bucket_policy_only, expected_type=type_hints["bucket_policy_only"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument default_event_based_hold", value=default_event_based_hold, expected_type=type_hints["default_event_based_hold"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument lifecycle_rule", value=lifecycle_rule, expected_type=type_hints["lifecycle_rule"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument requester_pays", value=requester_pays, expected_type=type_hints["requester_pays"])
            check_type(argname="argument retention_policy", value=retention_policy, expected_type=type_hints["retention_policy"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument uniform_bucket_level_access", value=uniform_bucket_level_access, expected_type=type_hints["uniform_bucket_level_access"])
            check_type(argname="argument versioning", value=versioning, expected_type=type_hints["versioning"])
            check_type(argname="argument website", value=website, expected_type=type_hints["website"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if bucket_policy_only is not None:
            self._values["bucket_policy_only"] = bucket_policy_only
        if cors is not None:
            self._values["cors"] = cors
        if default_event_based_hold is not None:
            self._values["default_event_based_hold"] = default_event_based_hold
        if encryption is not None:
            self._values["encryption"] = encryption
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if labels is not None:
            self._values["labels"] = labels
        if lifecycle_rule is not None:
            self._values["lifecycle_rule"] = lifecycle_rule
        if location is not None:
            self._values["location"] = location
        if logging is not None:
            self._values["logging"] = logging
        if project is not None:
            self._values["project"] = project
        if requester_pays is not None:
            self._values["requester_pays"] = requester_pays
        if retention_policy is not None:
            self._values["retention_policy"] = retention_policy
        if storage_class is not None:
            self._values["storage_class"] = storage_class
        if uniform_bucket_level_access is not None:
            self._values["uniform_bucket_level_access"] = uniform_bucket_level_access
        if versioning is not None:
            self._values["versioning"] = versioning
        if website is not None:
            self._values["website"] = website

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the bucket.

        :schema: CfnStorageBucketProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_policy_only(self) -> typing.Optional[builtins.bool]:
        '''Enables `Bucket Policy Only <https://cloud.google.com/storage/docs/bucket-policy-only>`_ access to a bucket. This field will be removed in the next major release of the provider.

        :schema: CfnStorageBucketProps#BucketPolicyOnly
        '''
        result = self._values.get("bucket_policy_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cors(self) -> typing.Optional[typing.List["CorsDefinition"]]:
        '''
        :schema: CfnStorageBucketProps#Cors
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional[typing.List["CorsDefinition"]], result)

    @builtins.property
    def default_event_based_hold(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnStorageBucketProps#DefaultEventBasedHold
        '''
        result = self._values.get("default_event_based_hold")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption(self) -> typing.Optional[typing.List["EncryptionDefinition"]]:
        '''
        :schema: CfnStorageBucketProps#Encryption
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[typing.List["EncryptionDefinition"]], result)

    @builtins.property
    def force_destroy(self) -> typing.Optional[builtins.bool]:
        '''When deleting a bucket, this boolean option will delete all contained objects.

        If you try to delete a
        bucket that contains objects, Terraform will fail that run.

        :schema: CfnStorageBucketProps#ForceDestroy
        '''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List["LabelsDefinition"]]:
        '''A map of key/value label pairs to assign to the bucket.

        :schema: CfnStorageBucketProps#Labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List["LabelsDefinition"]], result)

    @builtins.property
    def lifecycle_rule(self) -> typing.Optional[typing.List["LifecycleRuleDefinition"]]:
        '''
        :schema: CfnStorageBucketProps#LifecycleRule
        '''
        result = self._values.get("lifecycle_rule")
        return typing.cast(typing.Optional[typing.List["LifecycleRuleDefinition"]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The `GCS location <https://cloud.google.com/storage/docs/bucket-locations>`_.

        :schema: CfnStorageBucketProps#Location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging(self) -> typing.Optional[typing.List["LoggingDefinition"]]:
        '''
        :schema: CfnStorageBucketProps#Logging
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[typing.List["LoggingDefinition"]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If it
        is not provided, the provider project is used.

        :schema: CfnStorageBucketProps#Project
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requester_pays(self) -> typing.Optional[builtins.bool]:
        '''Enables `Requester Pays <https://cloud.google.com/storage/docs/requester-pays>`_ on a storage bucket.

        :schema: CfnStorageBucketProps#RequesterPays
        '''
        result = self._values.get("requester_pays")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def retention_policy(
        self,
    ) -> typing.Optional[typing.List["RetentionPolicyDefinition"]]:
        '''
        :schema: CfnStorageBucketProps#RetentionPolicy
        '''
        result = self._values.get("retention_policy")
        return typing.cast(typing.Optional[typing.List["RetentionPolicyDefinition"]], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''The `Storage Class <https://cloud.google.com/storage/docs/storage-classes>`_ of the new bucket. Supported values include: ``STANDARD``, ``MULTI_REGIONAL``, ``REGIONAL``, ``NEARLINE``, ``COLDLINE``, ``ARCHIVE``.

        :schema: CfnStorageBucketProps#StorageClass
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uniform_bucket_level_access(self) -> typing.Optional[builtins.bool]:
        '''Enables `Uniform bucket-level access <https://cloud.google.com/storage/docs/uniform-bucket-level-access>`_ access to a bucket.

        :schema: CfnStorageBucketProps#UniformBucketLevelAccess
        '''
        result = self._values.get("uniform_bucket_level_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def versioning(self) -> typing.Optional[typing.List["VersioningDefinition"]]:
        '''
        :schema: CfnStorageBucketProps#Versioning
        '''
        result = self._values.get("versioning")
        return typing.cast(typing.Optional[typing.List["VersioningDefinition"]], result)

    @builtins.property
    def website(self) -> typing.Optional[typing.List["WebsiteDefinition"]]:
        '''
        :schema: CfnStorageBucketProps#Website
        '''
        result = self._values.get("website")
        return typing.cast(typing.Optional[typing.List["WebsiteDefinition"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStorageBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.ConditionDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "age": "age",
        "created_before": "createdBefore",
        "custom_time_before": "customTimeBefore",
        "days_since_custom_time": "daysSinceCustomTime",
        "days_since_noncurrent_time": "daysSinceNoncurrentTime",
        "matches_storage_class": "matchesStorageClass",
        "noncurrent_time_before": "noncurrentTimeBefore",
        "num_newer_versions": "numNewerVersions",
        "with_state": "withState",
    },
)
class ConditionDefinition:
    def __init__(
        self,
        *,
        age: typing.Optional[jsii.Number] = None,
        created_before: typing.Optional[builtins.str] = None,
        custom_time_before: typing.Optional[builtins.str] = None,
        days_since_custom_time: typing.Optional[jsii.Number] = None,
        days_since_noncurrent_time: typing.Optional[jsii.Number] = None,
        matches_storage_class: typing.Optional[typing.Sequence[builtins.str]] = None,
        noncurrent_time_before: typing.Optional[builtins.str] = None,
        num_newer_versions: typing.Optional[jsii.Number] = None,
        with_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param age: Minimum age of an object in days to satisfy this condition.
        :param created_before: A date in the RFC 3339 format YYYY-MM-DD. This condition is satisfied when an object is created before midnight of the specified date in UTC.
        :param custom_time_before: A date in the RFC 3339 format YYYY-MM-DD. This condition is satisfied when the customTime metadata for the object is set to an earlier date than the date used in this lifecycle condition.
        :param days_since_custom_time: Days since the date set in the ``customTime`` metadata for the object. This condition is satisfied when the current date and time is at least the specified number of days after the ``customTime``.
        :param days_since_noncurrent_time: Relevant only for versioned objects. Number of days elapsed since the noncurrent timestamp of an object.
        :param matches_storage_class: `Storage Class <https://cloud.google.com/storage/docs/storage-classes>`_ of objects to satisfy this condition. Supported values include: ``STANDARD``, ``MULTI_REGIONAL``, ``REGIONAL``, ``NEARLINE``, ``COLDLINE``, ``ARCHIVE``, ``DURABLE_REDUCED_AVAILABILITY``.
        :param noncurrent_time_before: Relevant only for versioned objects. The date in RFC 3339 (e.g. ``2017-06-13``) when the object became nonconcurrent.
        :param num_newer_versions: Relevant only for versioned objects. The number of newer versions of an object to satisfy this condition.
        :param with_state: Match to live and/or archived objects. Unversioned buckets have only live objects. Supported values include: ``"LIVE"``, ``"ARCHIVED"``, ``"ANY"``.

        :schema: ConditionDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7af42c6f7cc98e264ae5917e3d4d59f2b8b87dc3b488a3088b9af8dda313f13a)
            check_type(argname="argument age", value=age, expected_type=type_hints["age"])
            check_type(argname="argument created_before", value=created_before, expected_type=type_hints["created_before"])
            check_type(argname="argument custom_time_before", value=custom_time_before, expected_type=type_hints["custom_time_before"])
            check_type(argname="argument days_since_custom_time", value=days_since_custom_time, expected_type=type_hints["days_since_custom_time"])
            check_type(argname="argument days_since_noncurrent_time", value=days_since_noncurrent_time, expected_type=type_hints["days_since_noncurrent_time"])
            check_type(argname="argument matches_storage_class", value=matches_storage_class, expected_type=type_hints["matches_storage_class"])
            check_type(argname="argument noncurrent_time_before", value=noncurrent_time_before, expected_type=type_hints["noncurrent_time_before"])
            check_type(argname="argument num_newer_versions", value=num_newer_versions, expected_type=type_hints["num_newer_versions"])
            check_type(argname="argument with_state", value=with_state, expected_type=type_hints["with_state"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if age is not None:
            self._values["age"] = age
        if created_before is not None:
            self._values["created_before"] = created_before
        if custom_time_before is not None:
            self._values["custom_time_before"] = custom_time_before
        if days_since_custom_time is not None:
            self._values["days_since_custom_time"] = days_since_custom_time
        if days_since_noncurrent_time is not None:
            self._values["days_since_noncurrent_time"] = days_since_noncurrent_time
        if matches_storage_class is not None:
            self._values["matches_storage_class"] = matches_storage_class
        if noncurrent_time_before is not None:
            self._values["noncurrent_time_before"] = noncurrent_time_before
        if num_newer_versions is not None:
            self._values["num_newer_versions"] = num_newer_versions
        if with_state is not None:
            self._values["with_state"] = with_state

    @builtins.property
    def age(self) -> typing.Optional[jsii.Number]:
        '''Minimum age of an object in days to satisfy this condition.

        :schema: ConditionDefinition#Age
        '''
        result = self._values.get("age")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def created_before(self) -> typing.Optional[builtins.str]:
        '''A date in the RFC 3339 format YYYY-MM-DD.

        This condition is satisfied when an object is created before midnight of the specified date in UTC.

        :schema: ConditionDefinition#CreatedBefore
        '''
        result = self._values.get("created_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_time_before(self) -> typing.Optional[builtins.str]:
        '''A date in the RFC 3339 format YYYY-MM-DD.

        This condition is satisfied when the customTime metadata for the object is set to an earlier date than the date used in this lifecycle condition.

        :schema: ConditionDefinition#CustomTimeBefore
        '''
        result = self._values.get("custom_time_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days_since_custom_time(self) -> typing.Optional[jsii.Number]:
        '''Days since the date set in the ``customTime`` metadata for the object.

        This condition is satisfied when the current date and time is at least the specified number of days after the ``customTime``.

        :schema: ConditionDefinition#DaysSinceCustomTime
        '''
        result = self._values.get("days_since_custom_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def days_since_noncurrent_time(self) -> typing.Optional[jsii.Number]:
        '''Relevant only for versioned objects.

        Number of days elapsed since the noncurrent timestamp of an object.

        :schema: ConditionDefinition#DaysSinceNoncurrentTime
        '''
        result = self._values.get("days_since_noncurrent_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matches_storage_class(self) -> typing.Optional[typing.List[builtins.str]]:
        '''`Storage Class <https://cloud.google.com/storage/docs/storage-classes>`_ of objects to satisfy this condition. Supported values include: ``STANDARD``, ``MULTI_REGIONAL``, ``REGIONAL``, ``NEARLINE``, ``COLDLINE``, ``ARCHIVE``, ``DURABLE_REDUCED_AVAILABILITY``.

        :schema: ConditionDefinition#MatchesStorageClass
        '''
        result = self._values.get("matches_storage_class")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def noncurrent_time_before(self) -> typing.Optional[builtins.str]:
        '''Relevant only for versioned objects.

        The date in RFC 3339 (e.g. ``2017-06-13``) when the object became nonconcurrent.

        :schema: ConditionDefinition#NoncurrentTimeBefore
        '''
        result = self._values.get("noncurrent_time_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_newer_versions(self) -> typing.Optional[jsii.Number]:
        '''Relevant only for versioned objects.

        The number of newer versions of an object to satisfy this condition.

        :schema: ConditionDefinition#NumNewerVersions
        '''
        result = self._values.get("num_newer_versions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def with_state(self) -> typing.Optional[builtins.str]:
        '''Match to live and/or archived objects.

        Unversioned buckets have only live objects. Supported values include: ``"LIVE"``, ``"ARCHIVED"``, ``"ANY"``.

        :schema: ConditionDefinition#WithState
        '''
        result = self._values.get("with_state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConditionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.CorsDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "max_age_seconds": "maxAgeSeconds",
        "method": "method",
        "origin": "origin",
        "response_header": "responseHeader",
    },
)
class CorsDefinition:
    def __init__(
        self,
        *,
        max_age_seconds: typing.Optional[jsii.Number] = None,
        method: typing.Optional[typing.Sequence[builtins.str]] = None,
        origin: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_header: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param max_age_seconds: The value, in seconds, to return in the `Access-Control-Max-Age header <https://www.w3.org/TR/cors/#access-control-max-age-response-header>`_ used in preflight responses.
        :param method: The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method".
        :param origin: The list of `Origins <https://tools.ietf.org/html/rfc6454>`_ eligible to receive CORS response headers. Note: "*" is permitted in the list of origins, and means "any Origin".
        :param response_header: The list of HTTP headers other than the `simple response headers <https://www.w3.org/TR/cors/#simple-response-header>`_ to give permission for the user-agent to share across domains.

        :schema: CorsDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a5f4c3a49fbb922936d61dd3a1ff9211754955ab7453290b857f92f8dac84ce)
            check_type(argname="argument max_age_seconds", value=max_age_seconds, expected_type=type_hints["max_age_seconds"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument response_header", value=response_header, expected_type=type_hints["response_header"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_age_seconds is not None:
            self._values["max_age_seconds"] = max_age_seconds
        if method is not None:
            self._values["method"] = method
        if origin is not None:
            self._values["origin"] = origin
        if response_header is not None:
            self._values["response_header"] = response_header

    @builtins.property
    def max_age_seconds(self) -> typing.Optional[jsii.Number]:
        '''The value, in seconds, to return in the `Access-Control-Max-Age header <https://www.w3.org/TR/cors/#access-control-max-age-response-header>`_ used in preflight responses.

        :schema: CorsDefinition#MaxAgeSeconds
        '''
        result = self._values.get("max_age_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method".

        :schema: CorsDefinition#Method
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def origin(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of `Origins <https://tools.ietf.org/html/rfc6454>`_ eligible to receive CORS response headers. Note: "*" is permitted in the list of origins, and means "any Origin".

        :schema: CorsDefinition#Origin
        '''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def response_header(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of HTTP headers other than the `simple response headers <https://www.w3.org/TR/cors/#simple-response-header>`_ to give permission for the user-agent to share across domains.

        :schema: CorsDefinition#ResponseHeader
        '''
        result = self._values.get("response_header")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CorsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.EncryptionDefinition",
    jsii_struct_bases=[],
    name_mapping={"default_kms_key_name": "defaultKmsKeyName"},
)
class EncryptionDefinition:
    def __init__(self, *, default_kms_key_name: builtins.str) -> None:
        '''
        :param default_kms_key_name: 

        :schema: EncryptionDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94596a0221dbdd4d4f37dc566bc502e64a4cd28bf26da834c642ac51017fcbf3)
            check_type(argname="argument default_kms_key_name", value=default_kms_key_name, expected_type=type_hints["default_kms_key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_kms_key_name": default_kms_key_name,
        }

    @builtins.property
    def default_kms_key_name(self) -> builtins.str:
        '''
        :schema: EncryptionDefinition#DefaultKmsKeyName
        '''
        result = self._values.get("default_kms_key_name")
        assert result is not None, "Required property 'default_kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncryptionDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.LabelsDefinition",
    jsii_struct_bases=[],
    name_mapping={"map_key": "mapKey", "map_value": "mapValue"},
)
class LabelsDefinition:
    def __init__(self, *, map_key: builtins.str, map_value: builtins.str) -> None:
        '''
        :param map_key: 
        :param map_value: 

        :schema: LabelsDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ceedfb8d4c62ee6cfa8b20fdb1c0ed294d900392b24a2619a07ff6f33daeb1)
            check_type(argname="argument map_key", value=map_key, expected_type=type_hints["map_key"])
            check_type(argname="argument map_value", value=map_value, expected_type=type_hints["map_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "map_key": map_key,
            "map_value": map_value,
        }

    @builtins.property
    def map_key(self) -> builtins.str:
        '''
        :schema: LabelsDefinition#MapKey
        '''
        result = self._values.get("map_key")
        assert result is not None, "Required property 'map_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_value(self) -> builtins.str:
        '''
        :schema: LabelsDefinition#MapValue
        '''
        result = self._values.get("map_value")
        assert result is not None, "Required property 'map_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LabelsDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.LifecycleRuleDefinition",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "condition": "condition"},
)
class LifecycleRuleDefinition:
    def __init__(
        self,
        *,
        action: typing.Optional[typing.Sequence[typing.Union[ActionDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
        condition: typing.Optional[typing.Sequence[typing.Union[ConditionDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param action: 
        :param condition: 

        :schema: LifecycleRuleDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__937265e2716bf56ed0a2586a6b8a15f84877364b7e18c9758fcf1b31947ad224)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if condition is not None:
            self._values["condition"] = condition

    @builtins.property
    def action(self) -> typing.Optional[typing.List[ActionDefinition]]:
        '''
        :schema: LifecycleRuleDefinition#Action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[typing.List[ActionDefinition]], result)

    @builtins.property
    def condition(self) -> typing.Optional[typing.List[ConditionDefinition]]:
        '''
        :schema: LifecycleRuleDefinition#Condition
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[typing.List[ConditionDefinition]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LifecycleRuleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.LoggingDefinition",
    jsii_struct_bases=[],
    name_mapping={"log_bucket": "logBucket", "log_object_prefix": "logObjectPrefix"},
)
class LoggingDefinition:
    def __init__(
        self,
        *,
        log_bucket: builtins.str,
        log_object_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_bucket: The bucket that will receive log objects.
        :param log_object_prefix: The object prefix for log objects. If it's not provided, by default GCS sets this to this bucket's name.

        :schema: LoggingDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db03dbc088eca7a6da3852696584d546d206ee14bd3b7954388e7b57701137e)
            check_type(argname="argument log_bucket", value=log_bucket, expected_type=type_hints["log_bucket"])
            check_type(argname="argument log_object_prefix", value=log_object_prefix, expected_type=type_hints["log_object_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_bucket": log_bucket,
        }
        if log_object_prefix is not None:
            self._values["log_object_prefix"] = log_object_prefix

    @builtins.property
    def log_bucket(self) -> builtins.str:
        '''The bucket that will receive log objects.

        :schema: LoggingDefinition#LogBucket
        '''
        result = self._values.get("log_bucket")
        assert result is not None, "Required property 'log_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_object_prefix(self) -> typing.Optional[builtins.str]:
        '''The object prefix for log objects.

        If it's not provided,
        by default GCS sets this to this bucket's name.

        :schema: LoggingDefinition#LogObjectPrefix
        '''
        result = self._values.get("log_object_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.RetentionPolicyDefinition",
    jsii_struct_bases=[],
    name_mapping={"retention_period": "retentionPeriod", "is_locked": "isLocked"},
)
class RetentionPolicyDefinition:
    def __init__(
        self,
        *,
        retention_period: jsii.Number,
        is_locked: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param retention_period: The period of time, in seconds, that objects in the bucket must be retained and cannot be deleted, overwritten, or archived. The value must be less than 2,147,483,647 seconds.
        :param is_locked: If set to ``true``, the bucket will be `locked <https://cloud.google.com/storage/docs/using-bucket-lock#lock-bucket>`_ and permanently restrict edits to the bucket's retention policy. Caution: Locking a bucket is an irreversible action.

        :schema: RetentionPolicyDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a09188897d7c23d67cf09732c97e72bed8bbcd49ab37a31b5c3da0d57a8c2e5)
            check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
            check_type(argname="argument is_locked", value=is_locked, expected_type=type_hints["is_locked"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "retention_period": retention_period,
        }
        if is_locked is not None:
            self._values["is_locked"] = is_locked

    @builtins.property
    def retention_period(self) -> jsii.Number:
        '''The period of time, in seconds, that objects in the bucket must be retained and cannot be deleted, overwritten, or archived.

        The value must be less than 2,147,483,647 seconds.

        :schema: RetentionPolicyDefinition#RetentionPeriod
        '''
        result = self._values.get("retention_period")
        assert result is not None, "Required property 'retention_period' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def is_locked(self) -> typing.Optional[builtins.bool]:
        '''If set to ``true``, the bucket will be `locked <https://cloud.google.com/storage/docs/using-bucket-lock#lock-bucket>`_ and permanently restrict edits to the bucket's retention policy.  Caution: Locking a bucket is an irreversible action.

        :schema: RetentionPolicyDefinition#IsLocked
        '''
        result = self._values.get("is_locked")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RetentionPolicyDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.VersioningDefinition",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class VersioningDefinition:
    def __init__(self, *, enabled: builtins.bool) -> None:
        '''
        :param enabled: While set to ``true``, versioning is fully enabled for this bucket.

        :schema: VersioningDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c87f8d8da9a295b023a8fe9a8d2d961b018af1b5eeba4f6e0c9bb50f5735e671)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> builtins.bool:
        '''While set to ``true``, versioning is fully enabled for this bucket.

        :schema: VersioningDefinition#Enabled
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VersioningDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/tf-google-storagebucket.WebsiteDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "main_page_suffix": "mainPageSuffix",
        "not_found_page": "notFoundPage",
    },
)
class WebsiteDefinition:
    def __init__(
        self,
        *,
        main_page_suffix: typing.Optional[builtins.str] = None,
        not_found_page: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param main_page_suffix: Behaves as the bucket's directory index where missing objects are treated as potential directories.
        :param not_found_page: The custom object to return when a requested resource is not found.

        :schema: WebsiteDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__823464e3f89e6603b75fdfd3909bbc4fcf0aaad8a114c46f20f625add4ac6b6b)
            check_type(argname="argument main_page_suffix", value=main_page_suffix, expected_type=type_hints["main_page_suffix"])
            check_type(argname="argument not_found_page", value=not_found_page, expected_type=type_hints["not_found_page"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if main_page_suffix is not None:
            self._values["main_page_suffix"] = main_page_suffix
        if not_found_page is not None:
            self._values["not_found_page"] = not_found_page

    @builtins.property
    def main_page_suffix(self) -> typing.Optional[builtins.str]:
        '''Behaves as the bucket's directory index where missing objects are treated as potential directories.

        :schema: WebsiteDefinition#MainPageSuffix
        '''
        result = self._values.get("main_page_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_found_page(self) -> typing.Optional[builtins.str]:
        '''The custom object to return when a requested resource is not found.

        :schema: WebsiteDefinition#NotFoundPage
        '''
        result = self._values.get("not_found_page")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebsiteDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ActionDefinition",
    "CfnStorageBucket",
    "CfnStorageBucketProps",
    "ConditionDefinition",
    "CorsDefinition",
    "EncryptionDefinition",
    "LabelsDefinition",
    "LifecycleRuleDefinition",
    "LoggingDefinition",
    "RetentionPolicyDefinition",
    "VersioningDefinition",
    "WebsiteDefinition",
]

publication.publish()

def _typecheckingstub__aa6d59e9c697b677e5e31f9b7eb7e9dd7232347089b25ee242c9d75c0e117987(
    *,
    type: builtins.str,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955975cb17a5edf68d3a4886331581e9e8e161ab156a95f548463e9ad1374bf5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    bucket_policy_only: typing.Optional[builtins.bool] = None,
    cors: typing.Optional[typing.Sequence[typing.Union[CorsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_event_based_hold: typing.Optional[builtins.bool] = None,
    encryption: typing.Optional[typing.Sequence[typing.Union[EncryptionDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    force_destroy: typing.Optional[builtins.bool] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[LabelsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    lifecycle_rule: typing.Optional[typing.Sequence[typing.Union[LifecycleRuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    location: typing.Optional[builtins.str] = None,
    logging: typing.Optional[typing.Sequence[typing.Union[LoggingDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    project: typing.Optional[builtins.str] = None,
    requester_pays: typing.Optional[builtins.bool] = None,
    retention_policy: typing.Optional[typing.Sequence[typing.Union[RetentionPolicyDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    storage_class: typing.Optional[builtins.str] = None,
    uniform_bucket_level_access: typing.Optional[builtins.bool] = None,
    versioning: typing.Optional[typing.Sequence[typing.Union[VersioningDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    website: typing.Optional[typing.Sequence[typing.Union[WebsiteDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5466a6cce4e0d2cccc6056e2456f7ec990ef1baffa4c19e5eeeaa1a289c75ab5(
    *,
    name: builtins.str,
    bucket_policy_only: typing.Optional[builtins.bool] = None,
    cors: typing.Optional[typing.Sequence[typing.Union[CorsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_event_based_hold: typing.Optional[builtins.bool] = None,
    encryption: typing.Optional[typing.Sequence[typing.Union[EncryptionDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    force_destroy: typing.Optional[builtins.bool] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[LabelsDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    lifecycle_rule: typing.Optional[typing.Sequence[typing.Union[LifecycleRuleDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    location: typing.Optional[builtins.str] = None,
    logging: typing.Optional[typing.Sequence[typing.Union[LoggingDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    project: typing.Optional[builtins.str] = None,
    requester_pays: typing.Optional[builtins.bool] = None,
    retention_policy: typing.Optional[typing.Sequence[typing.Union[RetentionPolicyDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    storage_class: typing.Optional[builtins.str] = None,
    uniform_bucket_level_access: typing.Optional[builtins.bool] = None,
    versioning: typing.Optional[typing.Sequence[typing.Union[VersioningDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    website: typing.Optional[typing.Sequence[typing.Union[WebsiteDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7af42c6f7cc98e264ae5917e3d4d59f2b8b87dc3b488a3088b9af8dda313f13a(
    *,
    age: typing.Optional[jsii.Number] = None,
    created_before: typing.Optional[builtins.str] = None,
    custom_time_before: typing.Optional[builtins.str] = None,
    days_since_custom_time: typing.Optional[jsii.Number] = None,
    days_since_noncurrent_time: typing.Optional[jsii.Number] = None,
    matches_storage_class: typing.Optional[typing.Sequence[builtins.str]] = None,
    noncurrent_time_before: typing.Optional[builtins.str] = None,
    num_newer_versions: typing.Optional[jsii.Number] = None,
    with_state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a5f4c3a49fbb922936d61dd3a1ff9211754955ab7453290b857f92f8dac84ce(
    *,
    max_age_seconds: typing.Optional[jsii.Number] = None,
    method: typing.Optional[typing.Sequence[builtins.str]] = None,
    origin: typing.Optional[typing.Sequence[builtins.str]] = None,
    response_header: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94596a0221dbdd4d4f37dc566bc502e64a4cd28bf26da834c642ac51017fcbf3(
    *,
    default_kms_key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ceedfb8d4c62ee6cfa8b20fdb1c0ed294d900392b24a2619a07ff6f33daeb1(
    *,
    map_key: builtins.str,
    map_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__937265e2716bf56ed0a2586a6b8a15f84877364b7e18c9758fcf1b31947ad224(
    *,
    action: typing.Optional[typing.Sequence[typing.Union[ActionDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
    condition: typing.Optional[typing.Sequence[typing.Union[ConditionDefinition, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db03dbc088eca7a6da3852696584d546d206ee14bd3b7954388e7b57701137e(
    *,
    log_bucket: builtins.str,
    log_object_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a09188897d7c23d67cf09732c97e72bed8bbcd49ab37a31b5c3da0d57a8c2e5(
    *,
    retention_period: jsii.Number,
    is_locked: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c87f8d8da9a295b023a8fe9a8d2d961b018af1b5eeba4f6e0c9bb50f5735e671(
    *,
    enabled: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__823464e3f89e6603b75fdfd3909bbc4fcf0aaad8a114c46f20f625add4ac6b6b(
    *,
    main_page_suffix: typing.Optional[builtins.str] = None,
    not_found_page: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
