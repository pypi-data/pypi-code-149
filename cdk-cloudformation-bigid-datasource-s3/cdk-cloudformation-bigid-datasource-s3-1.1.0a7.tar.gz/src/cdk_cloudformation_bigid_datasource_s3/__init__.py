'''
# bigid-datasource-s3

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `BigID::DataSource::S3` v1.1.0.

## Description

Manage a BigID S3 data source

## References

* [Source](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name BigID::DataSource::S3 \
  --publisher-id a3e6db75fd40c541561fdfc70d9f3764a9c3a000 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/a3e6db75fd40c541561fdfc70d9f3764a9c3a000/BigID-DataSource-S3 \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `BigID::DataSource::S3`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fbigid-datasource-s3+v1.1.0).
* Issues related to `BigID::DataSource::S3` should be reported to the [publisher](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git).

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


@jsii.enum(jsii_type="@cdk-cloudformation/bigid-datasource-s3.AwsAuthenticationType")
class AwsAuthenticationType(enum.Enum):
    '''AWS Authentication Type.

    :schema: AwsAuthenticationType
    '''

    IS_CREDENTIALS_AUTH = "IS_CREDENTIALS_AUTH"
    '''isCredentialsAuth.'''
    IS_IAM_ROLE_AUTH = "IS_IAM_ROLE_AUTH"
    '''isIamRoleAuth.'''
    IS_ANONYMOUS_AUTH = "IS_ANONYMOUS_AUTH"
    '''isAnonymousAuth.'''
    IS_CROSS_ACCOUNT_AUTH = "IS_CROSS_ACCOUNT_AUTH"
    '''isCrossAccountAuth.'''
    IS_STS_AUTH = "IS_STS_AUTH"
    '''isSTSAuth.'''


class CfnS3(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/bigid-datasource-s3.CfnS3",
):
    '''A CloudFormation ``BigID::DataSource::S3``.

    :cloudformationResource: BigID::DataSource::S3
    :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
    '''

    def __init__(
        self,
        scope_: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        aws_access_key: typing.Optional[builtins.str] = None,
        aws_authentication_type: typing.Optional[AwsAuthenticationType] = None,
        aws_region: typing.Optional[builtins.str] = None,
        aws_role_arn: typing.Optional[builtins.str] = None,
        aws_role_session_name: typing.Optional[builtins.str] = None,
        aws_secret_key: typing.Optional[builtins.str] = None,
        aws_session_token: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        business_owners: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
        comments: typing.Optional[builtins.str] = None,
        custom_fields: typing.Optional[typing.Sequence[typing.Union["CustomField", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        differential_scan: typing.Optional[builtins.bool] = None,
        ds_acl_scan_enabled: typing.Optional[builtins.bool] = None,
        enable_advance_classifiers: typing.Optional[builtins.bool] = None,
        enable_classifiers: typing.Optional[builtins.bool] = None,
        enable_clustering: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enabled_ocr: typing.Optional[builtins.bool] = None,
        file_types_to_exclude: typing.Optional[builtins.str] = None,
        folder_to_scan: typing.Optional[builtins.str] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        include_exclude_files: typing.Optional[builtins.bool] = None,
        is_modified_in_x_days: typing.Optional[builtins.bool] = None,
        it_owners: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
        location: typing.Optional[builtins.str] = None,
        metadata_acl_scan_enabled: typing.Optional[builtins.bool] = None,
        number_of_parsing_threads: typing.Optional[builtins.str] = None,
        ocr_languages: typing.Optional["OcrLanguages"] = None,
        ocr_timeout: typing.Optional[jsii.Number] = None,
        parquet_file_regex: typing.Optional[builtins.str] = None,
        sample_file_content: typing.Optional[builtins.bool] = None,
        sample_folders: typing.Optional[builtins.bool] = None,
        sample_percentage: typing.Optional[builtins.str] = None,
        scanner_group: typing.Optional[builtins.str] = None,
        scan_window_name: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        security_tier: typing.Optional["SecurityTier"] = None,
        test_connection_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        x_last_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``BigID::DataSource::S3``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: 
        :param aws_access_key: 
        :param aws_authentication_type: 
        :param aws_region: 
        :param aws_role_arn: 
        :param aws_role_session_name: 
        :param aws_secret_key: 
        :param aws_session_token: 
        :param bucket_name: 
        :param business_owners: 
        :param comments: 
        :param custom_fields: 
        :param description: 
        :param differential_scan: 
        :param ds_acl_scan_enabled: 
        :param enable_advance_classifiers: 
        :param enable_classifiers: 
        :param enable_clustering: 
        :param enabled: 
        :param enabled_ocr: 
        :param file_types_to_exclude: 
        :param folder_to_scan: 
        :param friendly_name: 
        :param include_exclude_files: 
        :param is_modified_in_x_days: 
        :param it_owners: 
        :param location: 
        :param metadata_acl_scan_enabled: 
        :param number_of_parsing_threads: 
        :param ocr_languages: 
        :param ocr_timeout: 
        :param parquet_file_regex: 
        :param sample_file_content: 
        :param sample_folders: 
        :param sample_percentage: 
        :param scanner_group: 
        :param scan_window_name: 
        :param scope: 
        :param security_tier: 
        :param test_connection_timeout_in_seconds: 
        :param x_last_days: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceee09d99a2c32ebf38d5ba7e59c4168decaffe1142c8cb0d8146f60764724a3)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnS3Props(
            name=name,
            aws_access_key=aws_access_key,
            aws_authentication_type=aws_authentication_type,
            aws_region=aws_region,
            aws_role_arn=aws_role_arn,
            aws_role_session_name=aws_role_session_name,
            aws_secret_key=aws_secret_key,
            aws_session_token=aws_session_token,
            bucket_name=bucket_name,
            business_owners=business_owners,
            comments=comments,
            custom_fields=custom_fields,
            description=description,
            differential_scan=differential_scan,
            ds_acl_scan_enabled=ds_acl_scan_enabled,
            enable_advance_classifiers=enable_advance_classifiers,
            enable_classifiers=enable_classifiers,
            enable_clustering=enable_clustering,
            enabled=enabled,
            enabled_ocr=enabled_ocr,
            file_types_to_exclude=file_types_to_exclude,
            folder_to_scan=folder_to_scan,
            friendly_name=friendly_name,
            include_exclude_files=include_exclude_files,
            is_modified_in_x_days=is_modified_in_x_days,
            it_owners=it_owners,
            location=location,
            metadata_acl_scan_enabled=metadata_acl_scan_enabled,
            number_of_parsing_threads=number_of_parsing_threads,
            ocr_languages=ocr_languages,
            ocr_timeout=ocr_timeout,
            parquet_file_regex=parquet_file_regex,
            sample_file_content=sample_file_content,
            sample_folders=sample_folders,
            sample_percentage=sample_percentage,
            scanner_group=scanner_group,
            scan_window_name=scan_window_name,
            scope=scope,
            security_tier=security_tier,
            test_connection_timeout_in_seconds=test_connection_timeout_in_seconds,
            x_last_days=x_last_days,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnS3Props":
        '''Resource props.'''
        return typing.cast("CfnS3Props", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/bigid-datasource-s3.CfnS3Props",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "aws_access_key": "awsAccessKey",
        "aws_authentication_type": "awsAuthenticationType",
        "aws_region": "awsRegion",
        "aws_role_arn": "awsRoleArn",
        "aws_role_session_name": "awsRoleSessionName",
        "aws_secret_key": "awsSecretKey",
        "aws_session_token": "awsSessionToken",
        "bucket_name": "bucketName",
        "business_owners": "businessOwners",
        "comments": "comments",
        "custom_fields": "customFields",
        "description": "description",
        "differential_scan": "differentialScan",
        "ds_acl_scan_enabled": "dsAclScanEnabled",
        "enable_advance_classifiers": "enableAdvanceClassifiers",
        "enable_classifiers": "enableClassifiers",
        "enable_clustering": "enableClustering",
        "enabled": "enabled",
        "enabled_ocr": "enabledOcr",
        "file_types_to_exclude": "fileTypesToExclude",
        "folder_to_scan": "folderToScan",
        "friendly_name": "friendlyName",
        "include_exclude_files": "includeExcludeFiles",
        "is_modified_in_x_days": "isModifiedInXDays",
        "it_owners": "itOwners",
        "location": "location",
        "metadata_acl_scan_enabled": "metadataAclScanEnabled",
        "number_of_parsing_threads": "numberOfParsingThreads",
        "ocr_languages": "ocrLanguages",
        "ocr_timeout": "ocrTimeout",
        "parquet_file_regex": "parquetFileRegex",
        "sample_file_content": "sampleFileContent",
        "sample_folders": "sampleFolders",
        "sample_percentage": "samplePercentage",
        "scanner_group": "scannerGroup",
        "scan_window_name": "scanWindowName",
        "scope": "scope",
        "security_tier": "securityTier",
        "test_connection_timeout_in_seconds": "testConnectionTimeoutInSeconds",
        "x_last_days": "xLastDays",
    },
)
class CfnS3Props:
    def __init__(
        self,
        *,
        name: builtins.str,
        aws_access_key: typing.Optional[builtins.str] = None,
        aws_authentication_type: typing.Optional[AwsAuthenticationType] = None,
        aws_region: typing.Optional[builtins.str] = None,
        aws_role_arn: typing.Optional[builtins.str] = None,
        aws_role_session_name: typing.Optional[builtins.str] = None,
        aws_secret_key: typing.Optional[builtins.str] = None,
        aws_session_token: typing.Optional[builtins.str] = None,
        bucket_name: typing.Optional[builtins.str] = None,
        business_owners: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
        comments: typing.Optional[builtins.str] = None,
        custom_fields: typing.Optional[typing.Sequence[typing.Union["CustomField", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        differential_scan: typing.Optional[builtins.bool] = None,
        ds_acl_scan_enabled: typing.Optional[builtins.bool] = None,
        enable_advance_classifiers: typing.Optional[builtins.bool] = None,
        enable_classifiers: typing.Optional[builtins.bool] = None,
        enable_clustering: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enabled_ocr: typing.Optional[builtins.bool] = None,
        file_types_to_exclude: typing.Optional[builtins.str] = None,
        folder_to_scan: typing.Optional[builtins.str] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        include_exclude_files: typing.Optional[builtins.bool] = None,
        is_modified_in_x_days: typing.Optional[builtins.bool] = None,
        it_owners: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
        location: typing.Optional[builtins.str] = None,
        metadata_acl_scan_enabled: typing.Optional[builtins.bool] = None,
        number_of_parsing_threads: typing.Optional[builtins.str] = None,
        ocr_languages: typing.Optional["OcrLanguages"] = None,
        ocr_timeout: typing.Optional[jsii.Number] = None,
        parquet_file_regex: typing.Optional[builtins.str] = None,
        sample_file_content: typing.Optional[builtins.bool] = None,
        sample_folders: typing.Optional[builtins.bool] = None,
        sample_percentage: typing.Optional[builtins.str] = None,
        scanner_group: typing.Optional[builtins.str] = None,
        scan_window_name: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        security_tier: typing.Optional["SecurityTier"] = None,
        test_connection_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        x_last_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Manage a BigID S3 data source.

        :param name: 
        :param aws_access_key: 
        :param aws_authentication_type: 
        :param aws_region: 
        :param aws_role_arn: 
        :param aws_role_session_name: 
        :param aws_secret_key: 
        :param aws_session_token: 
        :param bucket_name: 
        :param business_owners: 
        :param comments: 
        :param custom_fields: 
        :param description: 
        :param differential_scan: 
        :param ds_acl_scan_enabled: 
        :param enable_advance_classifiers: 
        :param enable_classifiers: 
        :param enable_clustering: 
        :param enabled: 
        :param enabled_ocr: 
        :param file_types_to_exclude: 
        :param folder_to_scan: 
        :param friendly_name: 
        :param include_exclude_files: 
        :param is_modified_in_x_days: 
        :param it_owners: 
        :param location: 
        :param metadata_acl_scan_enabled: 
        :param number_of_parsing_threads: 
        :param ocr_languages: 
        :param ocr_timeout: 
        :param parquet_file_regex: 
        :param sample_file_content: 
        :param sample_folders: 
        :param sample_percentage: 
        :param scanner_group: 
        :param scan_window_name: 
        :param scope: 
        :param security_tier: 
        :param test_connection_timeout_in_seconds: 
        :param x_last_days: 

        :schema: CfnS3Props
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5e8f662edceb4a59509bbf717b04b6203a1b79c7115590e8ec378c5ed7c5fb3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aws_access_key", value=aws_access_key, expected_type=type_hints["aws_access_key"])
            check_type(argname="argument aws_authentication_type", value=aws_authentication_type, expected_type=type_hints["aws_authentication_type"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            check_type(argname="argument aws_role_arn", value=aws_role_arn, expected_type=type_hints["aws_role_arn"])
            check_type(argname="argument aws_role_session_name", value=aws_role_session_name, expected_type=type_hints["aws_role_session_name"])
            check_type(argname="argument aws_secret_key", value=aws_secret_key, expected_type=type_hints["aws_secret_key"])
            check_type(argname="argument aws_session_token", value=aws_session_token, expected_type=type_hints["aws_session_token"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument business_owners", value=business_owners, expected_type=type_hints["business_owners"])
            check_type(argname="argument comments", value=comments, expected_type=type_hints["comments"])
            check_type(argname="argument custom_fields", value=custom_fields, expected_type=type_hints["custom_fields"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument differential_scan", value=differential_scan, expected_type=type_hints["differential_scan"])
            check_type(argname="argument ds_acl_scan_enabled", value=ds_acl_scan_enabled, expected_type=type_hints["ds_acl_scan_enabled"])
            check_type(argname="argument enable_advance_classifiers", value=enable_advance_classifiers, expected_type=type_hints["enable_advance_classifiers"])
            check_type(argname="argument enable_classifiers", value=enable_classifiers, expected_type=type_hints["enable_classifiers"])
            check_type(argname="argument enable_clustering", value=enable_clustering, expected_type=type_hints["enable_clustering"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enabled_ocr", value=enabled_ocr, expected_type=type_hints["enabled_ocr"])
            check_type(argname="argument file_types_to_exclude", value=file_types_to_exclude, expected_type=type_hints["file_types_to_exclude"])
            check_type(argname="argument folder_to_scan", value=folder_to_scan, expected_type=type_hints["folder_to_scan"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument include_exclude_files", value=include_exclude_files, expected_type=type_hints["include_exclude_files"])
            check_type(argname="argument is_modified_in_x_days", value=is_modified_in_x_days, expected_type=type_hints["is_modified_in_x_days"])
            check_type(argname="argument it_owners", value=it_owners, expected_type=type_hints["it_owners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument metadata_acl_scan_enabled", value=metadata_acl_scan_enabled, expected_type=type_hints["metadata_acl_scan_enabled"])
            check_type(argname="argument number_of_parsing_threads", value=number_of_parsing_threads, expected_type=type_hints["number_of_parsing_threads"])
            check_type(argname="argument ocr_languages", value=ocr_languages, expected_type=type_hints["ocr_languages"])
            check_type(argname="argument ocr_timeout", value=ocr_timeout, expected_type=type_hints["ocr_timeout"])
            check_type(argname="argument parquet_file_regex", value=parquet_file_regex, expected_type=type_hints["parquet_file_regex"])
            check_type(argname="argument sample_file_content", value=sample_file_content, expected_type=type_hints["sample_file_content"])
            check_type(argname="argument sample_folders", value=sample_folders, expected_type=type_hints["sample_folders"])
            check_type(argname="argument sample_percentage", value=sample_percentage, expected_type=type_hints["sample_percentage"])
            check_type(argname="argument scanner_group", value=scanner_group, expected_type=type_hints["scanner_group"])
            check_type(argname="argument scan_window_name", value=scan_window_name, expected_type=type_hints["scan_window_name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument security_tier", value=security_tier, expected_type=type_hints["security_tier"])
            check_type(argname="argument test_connection_timeout_in_seconds", value=test_connection_timeout_in_seconds, expected_type=type_hints["test_connection_timeout_in_seconds"])
            check_type(argname="argument x_last_days", value=x_last_days, expected_type=type_hints["x_last_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if aws_access_key is not None:
            self._values["aws_access_key"] = aws_access_key
        if aws_authentication_type is not None:
            self._values["aws_authentication_type"] = aws_authentication_type
        if aws_region is not None:
            self._values["aws_region"] = aws_region
        if aws_role_arn is not None:
            self._values["aws_role_arn"] = aws_role_arn
        if aws_role_session_name is not None:
            self._values["aws_role_session_name"] = aws_role_session_name
        if aws_secret_key is not None:
            self._values["aws_secret_key"] = aws_secret_key
        if aws_session_token is not None:
            self._values["aws_session_token"] = aws_session_token
        if bucket_name is not None:
            self._values["bucket_name"] = bucket_name
        if business_owners is not None:
            self._values["business_owners"] = business_owners
        if comments is not None:
            self._values["comments"] = comments
        if custom_fields is not None:
            self._values["custom_fields"] = custom_fields
        if description is not None:
            self._values["description"] = description
        if differential_scan is not None:
            self._values["differential_scan"] = differential_scan
        if ds_acl_scan_enabled is not None:
            self._values["ds_acl_scan_enabled"] = ds_acl_scan_enabled
        if enable_advance_classifiers is not None:
            self._values["enable_advance_classifiers"] = enable_advance_classifiers
        if enable_classifiers is not None:
            self._values["enable_classifiers"] = enable_classifiers
        if enable_clustering is not None:
            self._values["enable_clustering"] = enable_clustering
        if enabled is not None:
            self._values["enabled"] = enabled
        if enabled_ocr is not None:
            self._values["enabled_ocr"] = enabled_ocr
        if file_types_to_exclude is not None:
            self._values["file_types_to_exclude"] = file_types_to_exclude
        if folder_to_scan is not None:
            self._values["folder_to_scan"] = folder_to_scan
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if include_exclude_files is not None:
            self._values["include_exclude_files"] = include_exclude_files
        if is_modified_in_x_days is not None:
            self._values["is_modified_in_x_days"] = is_modified_in_x_days
        if it_owners is not None:
            self._values["it_owners"] = it_owners
        if location is not None:
            self._values["location"] = location
        if metadata_acl_scan_enabled is not None:
            self._values["metadata_acl_scan_enabled"] = metadata_acl_scan_enabled
        if number_of_parsing_threads is not None:
            self._values["number_of_parsing_threads"] = number_of_parsing_threads
        if ocr_languages is not None:
            self._values["ocr_languages"] = ocr_languages
        if ocr_timeout is not None:
            self._values["ocr_timeout"] = ocr_timeout
        if parquet_file_regex is not None:
            self._values["parquet_file_regex"] = parquet_file_regex
        if sample_file_content is not None:
            self._values["sample_file_content"] = sample_file_content
        if sample_folders is not None:
            self._values["sample_folders"] = sample_folders
        if sample_percentage is not None:
            self._values["sample_percentage"] = sample_percentage
        if scanner_group is not None:
            self._values["scanner_group"] = scanner_group
        if scan_window_name is not None:
            self._values["scan_window_name"] = scan_window_name
        if scope is not None:
            self._values["scope"] = scope
        if security_tier is not None:
            self._values["security_tier"] = security_tier
        if test_connection_timeout_in_seconds is not None:
            self._values["test_connection_timeout_in_seconds"] = test_connection_timeout_in_seconds
        if x_last_days is not None:
            self._values["x_last_days"] = x_last_days

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: CfnS3Props#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_access_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#AwsAccessKey
        '''
        result = self._values.get("aws_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_authentication_type(self) -> typing.Optional[AwsAuthenticationType]:
        '''
        :schema: CfnS3Props#AwsAuthenticationType
        '''
        result = self._values.get("aws_authentication_type")
        return typing.cast(typing.Optional[AwsAuthenticationType], result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#AwsRegion
        '''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_role_arn(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#AwsRoleArn
        '''
        result = self._values.get("aws_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_role_session_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#AwsRoleSessionName
        '''
        result = self._values.get("aws_role_session_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#AwsSecretKey
        '''
        result = self._values.get("aws_secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_session_token(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#AwsSessionToken
        '''
        result = self._values.get("aws_session_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#BucketName
        '''
        result = self._values.get("bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def business_owners(self) -> typing.Optional[typing.List["User"]]:
        '''
        :schema: CfnS3Props#BusinessOwners
        '''
        result = self._values.get("business_owners")
        return typing.cast(typing.Optional[typing.List["User"]], result)

    @builtins.property
    def comments(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#Comments
        '''
        result = self._values.get("comments")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_fields(self) -> typing.Optional[typing.List["CustomField"]]:
        '''
        :schema: CfnS3Props#CustomFields
        '''
        result = self._values.get("custom_fields")
        return typing.cast(typing.Optional[typing.List["CustomField"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def differential_scan(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#DifferentialScan
        '''
        result = self._values.get("differential_scan")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ds_acl_scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#DsAclScanEnabled
        '''
        result = self._values.get("ds_acl_scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_advance_classifiers(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#EnableAdvanceClassifiers
        '''
        result = self._values.get("enable_advance_classifiers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_classifiers(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#EnableClassifiers
        '''
        result = self._values.get("enable_classifiers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_clustering(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#EnableClustering
        '''
        result = self._values.get("enable_clustering")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enabled_ocr(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#EnabledOcr
        '''
        result = self._values.get("enabled_ocr")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def file_types_to_exclude(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#FileTypesToExclude
        '''
        result = self._values.get("file_types_to_exclude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def folder_to_scan(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#FolderToScan
        '''
        result = self._values.get("folder_to_scan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#FriendlyName
        '''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_exclude_files(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#IncludeExcludeFiles
        '''
        result = self._values.get("include_exclude_files")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_modified_in_x_days(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#IsModifiedInXDays
        '''
        result = self._values.get("is_modified_in_x_days")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def it_owners(self) -> typing.Optional[typing.List["User"]]:
        '''
        :schema: CfnS3Props#ItOwners
        '''
        result = self._values.get("it_owners")
        return typing.cast(typing.Optional[typing.List["User"]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#Location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_acl_scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#MetadataAclScanEnabled
        '''
        result = self._values.get("metadata_acl_scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def number_of_parsing_threads(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#NumberOfParsingThreads
        '''
        result = self._values.get("number_of_parsing_threads")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ocr_languages(self) -> typing.Optional["OcrLanguages"]:
        '''
        :schema: CfnS3Props#OcrLanguages
        '''
        result = self._values.get("ocr_languages")
        return typing.cast(typing.Optional["OcrLanguages"], result)

    @builtins.property
    def ocr_timeout(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnS3Props#OcrTimeout
        '''
        result = self._values.get("ocr_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parquet_file_regex(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#ParquetFileRegex
        '''
        result = self._values.get("parquet_file_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_file_content(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#SampleFileContent
        '''
        result = self._values.get("sample_file_content")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sample_folders(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnS3Props#SampleFolders
        '''
        result = self._values.get("sample_folders")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sample_percentage(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#SamplePercentage
        '''
        result = self._values.get("sample_percentage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scanner_group(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#ScannerGroup
        '''
        result = self._values.get("scanner_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scan_window_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#ScanWindowName
        '''
        result = self._values.get("scan_window_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnS3Props#Scope
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_tier(self) -> typing.Optional["SecurityTier"]:
        '''
        :schema: CfnS3Props#SecurityTier
        '''
        result = self._values.get("security_tier")
        return typing.cast(typing.Optional["SecurityTier"], result)

    @builtins.property
    def test_connection_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnS3Props#TestConnectionTimeoutInSeconds
        '''
        result = self._values.get("test_connection_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def x_last_days(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnS3Props#XLastDays
        '''
        result = self._values.get("x_last_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/bigid-datasource-s3.CustomField",
    jsii_struct_bases=[],
    name_mapping={
        "encoded": "encoded",
        "name": "name",
        "type": "type",
        "value": "value",
    },
)
class CustomField:
    def __init__(
        self,
        *,
        encoded: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["CustomFieldType"] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encoded: 
        :param name: 
        :param type: 
        :param value: 

        :schema: CustomField
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8da085f051a7e9da4a6dde4ff42bf2e67f92f1c453451e38631cd5d65f35348)
            check_type(argname="argument encoded", value=encoded, expected_type=type_hints["encoded"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encoded is not None:
            self._values["encoded"] = encoded
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def encoded(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CustomField#Encoded
        '''
        result = self._values.get("encoded")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CustomField#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["CustomFieldType"]:
        '''
        :schema: CustomField#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["CustomFieldType"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CustomField#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@cdk-cloudformation/bigid-datasource-s3.CustomFieldType")
class CustomFieldType(enum.Enum):
    '''
    :schema: CustomFieldType
    '''

    CLEAR = "CLEAR"
    '''clear.'''
    ENCRYPTED = "ENCRYPTED"
    '''encrypted.'''


@jsii.enum(jsii_type="@cdk-cloudformation/bigid-datasource-s3.OcrLanguages")
class OcrLanguages(enum.Enum):
    '''OCR Languages (only used when "EnabledOcr" is set to "true").

    :schema: OcrLanguages
    '''

    ENG = "ENG"
    '''eng.'''
    CHI_SIM_CHI_TRA = "CHI_SIM_CHI_TRA"
    '''chi_sim+chi_tra.'''
    IND = "IND"
    '''ind.'''
    JPN = "JPN"
    '''jpn.'''
    KOR = "KOR"
    '''kor.'''
    THA = "THA"
    '''tha.'''
    VIE = "VIE"
    '''vie.'''
    DEU = "DEU"
    '''deu.'''
    FRA = "FRA"
    '''fra.'''
    BUL = "BUL"
    '''bul.'''


@jsii.enum(jsii_type="@cdk-cloudformation/bigid-datasource-s3.SecurityTier")
class SecurityTier(enum.Enum):
    '''Security Tier.

    :schema: SecurityTier
    '''

    VALUE_1 = "VALUE_1"
    '''1.'''
    VALUE_2 = "VALUE_2"
    '''2.'''
    VALUE_3 = "VALUE_3"
    '''3.'''
    VALUE_4 = "VALUE_4"
    '''4.'''
    VALUE_5 = "VALUE_5"
    '''5.'''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/bigid-datasource-s3.User",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "id": "id", "origin": "origin"},
)
class User:
    def __init__(
        self,
        *,
        email: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        origin: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: 
        :param id: 
        :param origin: 

        :schema: User
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa1f2ecfbf46e2d22545714eba246cd0db5d138f00fa09fa9d6ee04bafb2e29)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if id is not None:
            self._values["id"] = id
        if origin is not None:
            self._values["origin"] = origin

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''
        :schema: User#Email
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: User#Id
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin(self) -> typing.Optional[builtins.str]:
        '''
        :schema: User#Origin
        '''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "User(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsAuthenticationType",
    "CfnS3",
    "CfnS3Props",
    "CustomField",
    "CustomFieldType",
    "OcrLanguages",
    "SecurityTier",
    "User",
]

publication.publish()

def _typecheckingstub__ceee09d99a2c32ebf38d5ba7e59c4168decaffe1142c8cb0d8146f60764724a3(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    aws_access_key: typing.Optional[builtins.str] = None,
    aws_authentication_type: typing.Optional[AwsAuthenticationType] = None,
    aws_region: typing.Optional[builtins.str] = None,
    aws_role_arn: typing.Optional[builtins.str] = None,
    aws_role_session_name: typing.Optional[builtins.str] = None,
    aws_secret_key: typing.Optional[builtins.str] = None,
    aws_session_token: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    business_owners: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
    comments: typing.Optional[builtins.str] = None,
    custom_fields: typing.Optional[typing.Sequence[typing.Union[CustomField, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    differential_scan: typing.Optional[builtins.bool] = None,
    ds_acl_scan_enabled: typing.Optional[builtins.bool] = None,
    enable_advance_classifiers: typing.Optional[builtins.bool] = None,
    enable_classifiers: typing.Optional[builtins.bool] = None,
    enable_clustering: typing.Optional[builtins.bool] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enabled_ocr: typing.Optional[builtins.bool] = None,
    file_types_to_exclude: typing.Optional[builtins.str] = None,
    folder_to_scan: typing.Optional[builtins.str] = None,
    friendly_name: typing.Optional[builtins.str] = None,
    include_exclude_files: typing.Optional[builtins.bool] = None,
    is_modified_in_x_days: typing.Optional[builtins.bool] = None,
    it_owners: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
    location: typing.Optional[builtins.str] = None,
    metadata_acl_scan_enabled: typing.Optional[builtins.bool] = None,
    number_of_parsing_threads: typing.Optional[builtins.str] = None,
    ocr_languages: typing.Optional[OcrLanguages] = None,
    ocr_timeout: typing.Optional[jsii.Number] = None,
    parquet_file_regex: typing.Optional[builtins.str] = None,
    sample_file_content: typing.Optional[builtins.bool] = None,
    sample_folders: typing.Optional[builtins.bool] = None,
    sample_percentage: typing.Optional[builtins.str] = None,
    scanner_group: typing.Optional[builtins.str] = None,
    scan_window_name: typing.Optional[builtins.str] = None,
    scope: typing.Optional[builtins.str] = None,
    security_tier: typing.Optional[SecurityTier] = None,
    test_connection_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    x_last_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e8f662edceb4a59509bbf717b04b6203a1b79c7115590e8ec378c5ed7c5fb3(
    *,
    name: builtins.str,
    aws_access_key: typing.Optional[builtins.str] = None,
    aws_authentication_type: typing.Optional[AwsAuthenticationType] = None,
    aws_region: typing.Optional[builtins.str] = None,
    aws_role_arn: typing.Optional[builtins.str] = None,
    aws_role_session_name: typing.Optional[builtins.str] = None,
    aws_secret_key: typing.Optional[builtins.str] = None,
    aws_session_token: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    business_owners: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
    comments: typing.Optional[builtins.str] = None,
    custom_fields: typing.Optional[typing.Sequence[typing.Union[CustomField, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    differential_scan: typing.Optional[builtins.bool] = None,
    ds_acl_scan_enabled: typing.Optional[builtins.bool] = None,
    enable_advance_classifiers: typing.Optional[builtins.bool] = None,
    enable_classifiers: typing.Optional[builtins.bool] = None,
    enable_clustering: typing.Optional[builtins.bool] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enabled_ocr: typing.Optional[builtins.bool] = None,
    file_types_to_exclude: typing.Optional[builtins.str] = None,
    folder_to_scan: typing.Optional[builtins.str] = None,
    friendly_name: typing.Optional[builtins.str] = None,
    include_exclude_files: typing.Optional[builtins.bool] = None,
    is_modified_in_x_days: typing.Optional[builtins.bool] = None,
    it_owners: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
    location: typing.Optional[builtins.str] = None,
    metadata_acl_scan_enabled: typing.Optional[builtins.bool] = None,
    number_of_parsing_threads: typing.Optional[builtins.str] = None,
    ocr_languages: typing.Optional[OcrLanguages] = None,
    ocr_timeout: typing.Optional[jsii.Number] = None,
    parquet_file_regex: typing.Optional[builtins.str] = None,
    sample_file_content: typing.Optional[builtins.bool] = None,
    sample_folders: typing.Optional[builtins.bool] = None,
    sample_percentage: typing.Optional[builtins.str] = None,
    scanner_group: typing.Optional[builtins.str] = None,
    scan_window_name: typing.Optional[builtins.str] = None,
    scope: typing.Optional[builtins.str] = None,
    security_tier: typing.Optional[SecurityTier] = None,
    test_connection_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    x_last_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8da085f051a7e9da4a6dde4ff42bf2e67f92f1c453451e38631cd5d65f35348(
    *,
    encoded: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[CustomFieldType] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa1f2ecfbf46e2d22545714eba246cd0db5d138f00fa09fa9d6ee04bafb2e29(
    *,
    email: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    origin: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
