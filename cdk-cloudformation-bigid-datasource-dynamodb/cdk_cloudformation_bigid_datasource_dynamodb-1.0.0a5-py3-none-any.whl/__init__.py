'''
# bigid-datasource-dynamodb

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `BigID::DataSource::DynamoDB` v1.0.0.

## Description

Manage a BigID DynamoDB data source.

## References

* [Source](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git)

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name BigID::DataSource::DynamoDB \
  --publisher-id a3e6db75fd40c541561fdfc70d9f3764a9c3a000 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/a3e6db75fd40c541561fdfc70d9f3764a9c3a000/BigID-DataSource-DynamoDB \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `BigID::DataSource::DynamoDB`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fbigid-datasource-dynamodb+v1.0.0).
* Issues related to `BigID::DataSource::DynamoDB` should be reported to the [publisher](https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git).

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


@jsii.enum(
    jsii_type="@cdk-cloudformation/bigid-datasource-dynamodb.AuthenticationMethod"
)
class AuthenticationMethod(enum.Enum):
    '''Authentication Method.

    :schema: AuthenticationMethod
    '''

    DEFAULT = "DEFAULT"
    '''Default.'''
    BIG_ID = "BIG_ID"
    '''BigID.'''
    IAM_ROLE = "IAM_ROLE"
    '''IAMRole.'''


class CfnDynamoDb(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/bigid-datasource-dynamodb.CfnDynamoDb",
):
    '''A CloudFormation ``BigID::DataSource::DynamoDB``.

    :cloudformationResource: BigID::DataSource::DynamoDB
    :link: https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git
    '''

    def __init__(
        self,
        scope_: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        authentication_method: typing.Optional[AuthenticationMethod] = None,
        aws_access_key: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
        aws_secret_key: typing.Optional[builtins.str] = None,
        aws_session_token: typing.Optional[builtins.str] = None,
        business_owners: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
        comments: typing.Optional[builtins.str] = None,
        credential_id: typing.Optional[builtins.str] = None,
        custom_fields: typing.Optional[typing.Sequence[typing.Union["CustomField", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamodb_table_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_advance_classifiers: typing.Optional[builtins.bool] = None,
        enable_classifiers: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_structured_clustering: typing.Optional[builtins.bool] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        is_correlation_set_supported: typing.Optional[builtins.bool] = None,
        it_owners: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
        location: typing.Optional[builtins.str] = None,
        number_of_parsing_threads: typing.Optional[builtins.str] = None,
        rdb_sample_data_max_size: typing.Optional[builtins.str] = None,
        sample_scan_only: typing.Optional[builtins.bool] = None,
        scanner_group: typing.Optional[builtins.str] = None,
        scan_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        scan_window_name: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        security_tier: typing.Optional["SecurityTier"] = None,
        test_connection_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``BigID::DataSource::DynamoDB``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: 
        :param authentication_method: 
        :param aws_access_key: 
        :param aws_region: 
        :param aws_secret_key: 
        :param aws_session_token: 
        :param business_owners: 
        :param comments: 
        :param credential_id: 
        :param custom_fields: 
        :param description: 
        :param dynamodb_table_names: 
        :param enable_advance_classifiers: 
        :param enable_classifiers: 
        :param enabled: 
        :param enable_structured_clustering: 
        :param friendly_name: 
        :param is_correlation_set_supported: 
        :param it_owners: 
        :param location: 
        :param number_of_parsing_threads: 
        :param rdb_sample_data_max_size: 
        :param sample_scan_only: 
        :param scanner_group: 
        :param scan_timeout_in_seconds: 
        :param scan_window_name: 
        :param scope: 
        :param security_tier: 
        :param test_connection_timeout_in_seconds: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2a408778b8ecf7bdac6f4885419bf8cfeabc1052ae7329ce119ed124cc12cc7)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDynamoDbProps(
            name=name,
            authentication_method=authentication_method,
            aws_access_key=aws_access_key,
            aws_region=aws_region,
            aws_secret_key=aws_secret_key,
            aws_session_token=aws_session_token,
            business_owners=business_owners,
            comments=comments,
            credential_id=credential_id,
            custom_fields=custom_fields,
            description=description,
            dynamodb_table_names=dynamodb_table_names,
            enable_advance_classifiers=enable_advance_classifiers,
            enable_classifiers=enable_classifiers,
            enabled=enabled,
            enable_structured_clustering=enable_structured_clustering,
            friendly_name=friendly_name,
            is_correlation_set_supported=is_correlation_set_supported,
            it_owners=it_owners,
            location=location,
            number_of_parsing_threads=number_of_parsing_threads,
            rdb_sample_data_max_size=rdb_sample_data_max_size,
            sample_scan_only=sample_scan_only,
            scanner_group=scanner_group,
            scan_timeout_in_seconds=scan_timeout_in_seconds,
            scan_window_name=scan_window_name,
            scope=scope,
            security_tier=security_tier,
            test_connection_timeout_in_seconds=test_connection_timeout_in_seconds,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDynamoDbProps":
        '''Resource props.'''
        return typing.cast("CfnDynamoDbProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/bigid-datasource-dynamodb.CfnDynamoDbProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "authentication_method": "authenticationMethod",
        "aws_access_key": "awsAccessKey",
        "aws_region": "awsRegion",
        "aws_secret_key": "awsSecretKey",
        "aws_session_token": "awsSessionToken",
        "business_owners": "businessOwners",
        "comments": "comments",
        "credential_id": "credentialId",
        "custom_fields": "customFields",
        "description": "description",
        "dynamodb_table_names": "dynamodbTableNames",
        "enable_advance_classifiers": "enableAdvanceClassifiers",
        "enable_classifiers": "enableClassifiers",
        "enabled": "enabled",
        "enable_structured_clustering": "enableStructuredClustering",
        "friendly_name": "friendlyName",
        "is_correlation_set_supported": "isCorrelationSetSupported",
        "it_owners": "itOwners",
        "location": "location",
        "number_of_parsing_threads": "numberOfParsingThreads",
        "rdb_sample_data_max_size": "rdbSampleDataMaxSize",
        "sample_scan_only": "sampleScanOnly",
        "scanner_group": "scannerGroup",
        "scan_timeout_in_seconds": "scanTimeoutInSeconds",
        "scan_window_name": "scanWindowName",
        "scope": "scope",
        "security_tier": "securityTier",
        "test_connection_timeout_in_seconds": "testConnectionTimeoutInSeconds",
    },
)
class CfnDynamoDbProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        authentication_method: typing.Optional[AuthenticationMethod] = None,
        aws_access_key: typing.Optional[builtins.str] = None,
        aws_region: typing.Optional[builtins.str] = None,
        aws_secret_key: typing.Optional[builtins.str] = None,
        aws_session_token: typing.Optional[builtins.str] = None,
        business_owners: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
        comments: typing.Optional[builtins.str] = None,
        credential_id: typing.Optional[builtins.str] = None,
        custom_fields: typing.Optional[typing.Sequence[typing.Union["CustomField", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamodb_table_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_advance_classifiers: typing.Optional[builtins.bool] = None,
        enable_classifiers: typing.Optional[builtins.bool] = None,
        enabled: typing.Optional[builtins.bool] = None,
        enable_structured_clustering: typing.Optional[builtins.bool] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        is_correlation_set_supported: typing.Optional[builtins.bool] = None,
        it_owners: typing.Optional[typing.Sequence[typing.Union["User", typing.Dict[builtins.str, typing.Any]]]] = None,
        location: typing.Optional[builtins.str] = None,
        number_of_parsing_threads: typing.Optional[builtins.str] = None,
        rdb_sample_data_max_size: typing.Optional[builtins.str] = None,
        sample_scan_only: typing.Optional[builtins.bool] = None,
        scanner_group: typing.Optional[builtins.str] = None,
        scan_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        scan_window_name: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        security_tier: typing.Optional["SecurityTier"] = None,
        test_connection_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Manage a BigID DynamoDB data source.

        :param name: 
        :param authentication_method: 
        :param aws_access_key: 
        :param aws_region: 
        :param aws_secret_key: 
        :param aws_session_token: 
        :param business_owners: 
        :param comments: 
        :param credential_id: 
        :param custom_fields: 
        :param description: 
        :param dynamodb_table_names: 
        :param enable_advance_classifiers: 
        :param enable_classifiers: 
        :param enabled: 
        :param enable_structured_clustering: 
        :param friendly_name: 
        :param is_correlation_set_supported: 
        :param it_owners: 
        :param location: 
        :param number_of_parsing_threads: 
        :param rdb_sample_data_max_size: 
        :param sample_scan_only: 
        :param scanner_group: 
        :param scan_timeout_in_seconds: 
        :param scan_window_name: 
        :param scope: 
        :param security_tier: 
        :param test_connection_timeout_in_seconds: 

        :schema: CfnDynamoDbProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__386617c31d7bd1937e1e4f330f64bffbc681f15b1084a76563344e51839c2872)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument authentication_method", value=authentication_method, expected_type=type_hints["authentication_method"])
            check_type(argname="argument aws_access_key", value=aws_access_key, expected_type=type_hints["aws_access_key"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            check_type(argname="argument aws_secret_key", value=aws_secret_key, expected_type=type_hints["aws_secret_key"])
            check_type(argname="argument aws_session_token", value=aws_session_token, expected_type=type_hints["aws_session_token"])
            check_type(argname="argument business_owners", value=business_owners, expected_type=type_hints["business_owners"])
            check_type(argname="argument comments", value=comments, expected_type=type_hints["comments"])
            check_type(argname="argument credential_id", value=credential_id, expected_type=type_hints["credential_id"])
            check_type(argname="argument custom_fields", value=custom_fields, expected_type=type_hints["custom_fields"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamodb_table_names", value=dynamodb_table_names, expected_type=type_hints["dynamodb_table_names"])
            check_type(argname="argument enable_advance_classifiers", value=enable_advance_classifiers, expected_type=type_hints["enable_advance_classifiers"])
            check_type(argname="argument enable_classifiers", value=enable_classifiers, expected_type=type_hints["enable_classifiers"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enable_structured_clustering", value=enable_structured_clustering, expected_type=type_hints["enable_structured_clustering"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument is_correlation_set_supported", value=is_correlation_set_supported, expected_type=type_hints["is_correlation_set_supported"])
            check_type(argname="argument it_owners", value=it_owners, expected_type=type_hints["it_owners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument number_of_parsing_threads", value=number_of_parsing_threads, expected_type=type_hints["number_of_parsing_threads"])
            check_type(argname="argument rdb_sample_data_max_size", value=rdb_sample_data_max_size, expected_type=type_hints["rdb_sample_data_max_size"])
            check_type(argname="argument sample_scan_only", value=sample_scan_only, expected_type=type_hints["sample_scan_only"])
            check_type(argname="argument scanner_group", value=scanner_group, expected_type=type_hints["scanner_group"])
            check_type(argname="argument scan_timeout_in_seconds", value=scan_timeout_in_seconds, expected_type=type_hints["scan_timeout_in_seconds"])
            check_type(argname="argument scan_window_name", value=scan_window_name, expected_type=type_hints["scan_window_name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument security_tier", value=security_tier, expected_type=type_hints["security_tier"])
            check_type(argname="argument test_connection_timeout_in_seconds", value=test_connection_timeout_in_seconds, expected_type=type_hints["test_connection_timeout_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if authentication_method is not None:
            self._values["authentication_method"] = authentication_method
        if aws_access_key is not None:
            self._values["aws_access_key"] = aws_access_key
        if aws_region is not None:
            self._values["aws_region"] = aws_region
        if aws_secret_key is not None:
            self._values["aws_secret_key"] = aws_secret_key
        if aws_session_token is not None:
            self._values["aws_session_token"] = aws_session_token
        if business_owners is not None:
            self._values["business_owners"] = business_owners
        if comments is not None:
            self._values["comments"] = comments
        if credential_id is not None:
            self._values["credential_id"] = credential_id
        if custom_fields is not None:
            self._values["custom_fields"] = custom_fields
        if description is not None:
            self._values["description"] = description
        if dynamodb_table_names is not None:
            self._values["dynamodb_table_names"] = dynamodb_table_names
        if enable_advance_classifiers is not None:
            self._values["enable_advance_classifiers"] = enable_advance_classifiers
        if enable_classifiers is not None:
            self._values["enable_classifiers"] = enable_classifiers
        if enabled is not None:
            self._values["enabled"] = enabled
        if enable_structured_clustering is not None:
            self._values["enable_structured_clustering"] = enable_structured_clustering
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if is_correlation_set_supported is not None:
            self._values["is_correlation_set_supported"] = is_correlation_set_supported
        if it_owners is not None:
            self._values["it_owners"] = it_owners
        if location is not None:
            self._values["location"] = location
        if number_of_parsing_threads is not None:
            self._values["number_of_parsing_threads"] = number_of_parsing_threads
        if rdb_sample_data_max_size is not None:
            self._values["rdb_sample_data_max_size"] = rdb_sample_data_max_size
        if sample_scan_only is not None:
            self._values["sample_scan_only"] = sample_scan_only
        if scanner_group is not None:
            self._values["scanner_group"] = scanner_group
        if scan_timeout_in_seconds is not None:
            self._values["scan_timeout_in_seconds"] = scan_timeout_in_seconds
        if scan_window_name is not None:
            self._values["scan_window_name"] = scan_window_name
        if scope is not None:
            self._values["scope"] = scope
        if security_tier is not None:
            self._values["security_tier"] = security_tier
        if test_connection_timeout_in_seconds is not None:
            self._values["test_connection_timeout_in_seconds"] = test_connection_timeout_in_seconds

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :schema: CfnDynamoDbProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_method(self) -> typing.Optional[AuthenticationMethod]:
        '''
        :schema: CfnDynamoDbProps#AuthenticationMethod
        '''
        result = self._values.get("authentication_method")
        return typing.cast(typing.Optional[AuthenticationMethod], result)

    @builtins.property
    def aws_access_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#AwsAccessKey
        '''
        result = self._values.get("aws_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#AwsRegion
        '''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_secret_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#AwsSecretKey
        '''
        result = self._values.get("aws_secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_session_token(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#AwsSessionToken
        '''
        result = self._values.get("aws_session_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def business_owners(self) -> typing.Optional[typing.List["User"]]:
        '''
        :schema: CfnDynamoDbProps#BusinessOwners
        '''
        result = self._values.get("business_owners")
        return typing.cast(typing.Optional[typing.List["User"]], result)

    @builtins.property
    def comments(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#Comments
        '''
        result = self._values.get("comments")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credential_id(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#CredentialId
        '''
        result = self._values.get("credential_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_fields(self) -> typing.Optional[typing.List["CustomField"]]:
        '''
        :schema: CfnDynamoDbProps#CustomFields
        '''
        result = self._values.get("custom_fields")
        return typing.cast(typing.Optional[typing.List["CustomField"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#Description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb_table_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: CfnDynamoDbProps#DynamodbTableNames
        '''
        result = self._values.get("dynamodb_table_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_advance_classifiers(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnDynamoDbProps#EnableAdvanceClassifiers
        '''
        result = self._values.get("enable_advance_classifiers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_classifiers(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnDynamoDbProps#EnableClassifiers
        '''
        result = self._values.get("enable_classifiers")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnDynamoDbProps#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_structured_clustering(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnDynamoDbProps#EnableStructuredClustering
        '''
        result = self._values.get("enable_structured_clustering")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#FriendlyName
        '''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_correlation_set_supported(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnDynamoDbProps#IsCorrelationSetSupported
        '''
        result = self._values.get("is_correlation_set_supported")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def it_owners(self) -> typing.Optional[typing.List["User"]]:
        '''
        :schema: CfnDynamoDbProps#ItOwners
        '''
        result = self._values.get("it_owners")
        return typing.cast(typing.Optional[typing.List["User"]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#Location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number_of_parsing_threads(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#NumberOfParsingThreads
        '''
        result = self._values.get("number_of_parsing_threads")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rdb_sample_data_max_size(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#RdbSampleDataMaxSize
        '''
        result = self._values.get("rdb_sample_data_max_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_scan_only(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: CfnDynamoDbProps#SampleScanOnly
        '''
        result = self._values.get("sample_scan_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def scanner_group(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#ScannerGroup
        '''
        result = self._values.get("scanner_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scan_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnDynamoDbProps#ScanTimeoutInSeconds
        '''
        result = self._values.get("scan_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scan_window_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#ScanWindowName
        '''
        result = self._values.get("scan_window_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDynamoDbProps#Scope
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_tier(self) -> typing.Optional["SecurityTier"]:
        '''
        :schema: CfnDynamoDbProps#SecurityTier
        '''
        result = self._values.get("security_tier")
        return typing.cast(typing.Optional["SecurityTier"], result)

    @builtins.property
    def test_connection_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CfnDynamoDbProps#TestConnectionTimeoutInSeconds
        '''
        result = self._values.get("test_connection_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDynamoDbProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/bigid-datasource-dynamodb.CustomField",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type", "value": "value"},
)
class CustomField:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["CustomFieldType"] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: 
        :param type: 
        :param value: 

        :schema: CustomField
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7363edd5492d68ceba5769d09446f49a0436672aa8e97b08fbf189991e3016fd)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

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


@jsii.enum(jsii_type="@cdk-cloudformation/bigid-datasource-dynamodb.CustomFieldType")
class CustomFieldType(enum.Enum):
    '''
    :schema: CustomFieldType
    '''

    CLEAR = "CLEAR"
    '''clear.'''
    ENCRYPTED = "ENCRYPTED"
    '''encrypted.'''


@jsii.enum(jsii_type="@cdk-cloudformation/bigid-datasource-dynamodb.SecurityTier")
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
    jsii_type="@cdk-cloudformation/bigid-datasource-dynamodb.User",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2944dc942da34de4ca53894a3dcfa55fbae58e2641d385d598165fae6dcaed1b)
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
    "AuthenticationMethod",
    "CfnDynamoDb",
    "CfnDynamoDbProps",
    "CustomField",
    "CustomFieldType",
    "SecurityTier",
    "User",
]

publication.publish()

def _typecheckingstub__f2a408778b8ecf7bdac6f4885419bf8cfeabc1052ae7329ce119ed124cc12cc7(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    authentication_method: typing.Optional[AuthenticationMethod] = None,
    aws_access_key: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    aws_secret_key: typing.Optional[builtins.str] = None,
    aws_session_token: typing.Optional[builtins.str] = None,
    business_owners: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
    comments: typing.Optional[builtins.str] = None,
    credential_id: typing.Optional[builtins.str] = None,
    custom_fields: typing.Optional[typing.Sequence[typing.Union[CustomField, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    dynamodb_table_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_advance_classifiers: typing.Optional[builtins.bool] = None,
    enable_classifiers: typing.Optional[builtins.bool] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_structured_clustering: typing.Optional[builtins.bool] = None,
    friendly_name: typing.Optional[builtins.str] = None,
    is_correlation_set_supported: typing.Optional[builtins.bool] = None,
    it_owners: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
    location: typing.Optional[builtins.str] = None,
    number_of_parsing_threads: typing.Optional[builtins.str] = None,
    rdb_sample_data_max_size: typing.Optional[builtins.str] = None,
    sample_scan_only: typing.Optional[builtins.bool] = None,
    scanner_group: typing.Optional[builtins.str] = None,
    scan_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    scan_window_name: typing.Optional[builtins.str] = None,
    scope: typing.Optional[builtins.str] = None,
    security_tier: typing.Optional[SecurityTier] = None,
    test_connection_timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__386617c31d7bd1937e1e4f330f64bffbc681f15b1084a76563344e51839c2872(
    *,
    name: builtins.str,
    authentication_method: typing.Optional[AuthenticationMethod] = None,
    aws_access_key: typing.Optional[builtins.str] = None,
    aws_region: typing.Optional[builtins.str] = None,
    aws_secret_key: typing.Optional[builtins.str] = None,
    aws_session_token: typing.Optional[builtins.str] = None,
    business_owners: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
    comments: typing.Optional[builtins.str] = None,
    credential_id: typing.Optional[builtins.str] = None,
    custom_fields: typing.Optional[typing.Sequence[typing.Union[CustomField, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    dynamodb_table_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_advance_classifiers: typing.Optional[builtins.bool] = None,
    enable_classifiers: typing.Optional[builtins.bool] = None,
    enabled: typing.Optional[builtins.bool] = None,
    enable_structured_clustering: typing.Optional[builtins.bool] = None,
    friendly_name: typing.Optional[builtins.str] = None,
    is_correlation_set_supported: typing.Optional[builtins.bool] = None,
    it_owners: typing.Optional[typing.Sequence[typing.Union[User, typing.Dict[builtins.str, typing.Any]]]] = None,
    location: typing.Optional[builtins.str] = None,
    number_of_parsing_threads: typing.Optional[builtins.str] = None,
    rdb_sample_data_max_size: typing.Optional[builtins.str] = None,
    sample_scan_only: typing.Optional[builtins.bool] = None,
    scanner_group: typing.Optional[builtins.str] = None,
    scan_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    scan_window_name: typing.Optional[builtins.str] = None,
    scope: typing.Optional[builtins.str] = None,
    security_tier: typing.Optional[SecurityTier] = None,
    test_connection_timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7363edd5492d68ceba5769d09446f49a0436672aa8e97b08fbf189991e3016fd(
    *,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[CustomFieldType] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2944dc942da34de4ca53894a3dcfa55fbae58e2641d385d598165fae6dcaed1b(
    *,
    email: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    origin: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
