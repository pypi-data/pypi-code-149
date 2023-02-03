'''
# awsqs-vpc-vpcqs-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `AWSQS::VPC::VPCQS::MODULE` v1.1.0.

## Description

Schema for Module Fragment of type AWSQS::VPC::VPCQS::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name AWSQS::VPC::VPCQS::MODULE \
  --publisher-id 408988dff9e863704bcc72e7e13f8d645cee8311 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-VPC-VPCQS-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `AWSQS::VPC::VPCQS::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fawsqs-vpc-vpcqs-module+v1.1.0).
* Issues related to `AWSQS::VPC::VPCQS::MODULE` should be reported to the [publisher](undefined).

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


class CfnVpcqsModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModule",
):
    '''A CloudFormation ``AWSQS::VPC::VPCQS::MODULE``.

    :cloudformationResource: AWSQS::VPC::VPCQS::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnVpcqsModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnVpcqsModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``AWSQS::VPC::VPCQS::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f05101874bba4ad0920312d5b89bfc57cca070aba09083455f2e291d0f1e191)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcqsModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnVpcqsModuleProps":
        '''Resource props.'''
        return typing.cast("CfnVpcqsModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnVpcqsModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnVpcqsModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnVpcqsModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type AWSQS::VPC::VPCQS::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnVpcqsModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnVpcqsModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnVpcqsModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0ef4b61bbc09d83ec63cf115c24ede713e40463a3339848f93a0212b9cf0b07)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnVpcqsModulePropsParameters"]:
        '''
        :schema: CfnVpcqsModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnVpcqsModulePropsResources"]:
        '''
        :schema: CfnVpcqsModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zones": "availabilityZones",
        "create_additional_private_subnets": "createAdditionalPrivateSubnets",
        "create_nat_gateways": "createNatGateways",
        "create_private_subnets": "createPrivateSubnets",
        "create_public_subnets": "createPublicSubnets",
        "create_vpc_flow_logs_to_cloud_watch": "createVpcFlowLogsToCloudWatch",
        "number_of_a_zs": "numberOfAZs",
        "private_subnet1_acidr": "privateSubnet1Acidr",
        "private_subnet1_bcidr": "privateSubnet1Bcidr",
        "private_subnet2_acidr": "privateSubnet2Acidr",
        "private_subnet2_bcidr": "privateSubnet2Bcidr",
        "private_subnet3_acidr": "privateSubnet3Acidr",
        "private_subnet3_bcidr": "privateSubnet3Bcidr",
        "private_subnet4_acidr": "privateSubnet4Acidr",
        "private_subnet4_bcidr": "privateSubnet4Bcidr",
        "private_subnet_a_tag1": "privateSubnetATag1",
        "private_subnet_a_tag2": "privateSubnetATag2",
        "private_subnet_a_tag3": "privateSubnetATag3",
        "private_subnet_b_tag1": "privateSubnetBTag1",
        "private_subnet_b_tag2": "privateSubnetBTag2",
        "private_subnet_b_tag3": "privateSubnetBTag3",
        "public_subnet1_cidr": "publicSubnet1Cidr",
        "public_subnet2_cidr": "publicSubnet2Cidr",
        "public_subnet3_cidr": "publicSubnet3Cidr",
        "public_subnet4_cidr": "publicSubnet4Cidr",
        "public_subnet_tag1": "publicSubnetTag1",
        "public_subnet_tag2": "publicSubnetTag2",
        "public_subnet_tag3": "publicSubnetTag3",
        "vpccidr": "vpccidr",
        "vpc_flow_logs_cloud_watch_kms_key": "vpcFlowLogsCloudWatchKmsKey",
        "vpc_flow_logs_log_format": "vpcFlowLogsLogFormat",
        "vpc_flow_logs_log_group_retention": "vpcFlowLogsLogGroupRetention",
        "vpc_flow_logs_max_aggregation_interval": "vpcFlowLogsMaxAggregationInterval",
        "vpc_flow_logs_traffic_type": "vpcFlowLogsTrafficType",
        "vpc_tenancy": "vpcTenancy",
    },
)
class CfnVpcqsModulePropsParameters:
    def __init__(
        self,
        *,
        availability_zones: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersAvailabilityZones", typing.Dict[builtins.str, typing.Any]]] = None,
        create_additional_private_subnets: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets", typing.Dict[builtins.str, typing.Any]]] = None,
        create_nat_gateways: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersCreateNatGateways", typing.Dict[builtins.str, typing.Any]]] = None,
        create_private_subnets: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersCreatePrivateSubnets", typing.Dict[builtins.str, typing.Any]]] = None,
        create_public_subnets: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersCreatePublicSubnets", typing.Dict[builtins.str, typing.Any]]] = None,
        create_vpc_flow_logs_to_cloud_watch: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch", typing.Dict[builtins.str, typing.Any]]] = None,
        number_of_a_zs: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersNumberOfAZs", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_acidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnet1Acidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_bcidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_acidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnet2Acidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_bcidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_acidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnet3Acidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_bcidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_acidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnet4Acidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_bcidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet_a_tag1: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnetATag1", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet_a_tag2: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnetATag2", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet_a_tag3: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnetATag3", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet_b_tag1: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnetBTag1", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet_b_tag2: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnetBTag2", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet_b_tag3: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPrivateSubnetBTag3", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1_cidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPublicSubnet1Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2_cidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPublicSubnet2Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet3_cidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPublicSubnet3Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet4_cidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPublicSubnet4Cidr", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet_tag1: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPublicSubnetTag1", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet_tag2: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPublicSubnetTag2", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet_tag3: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersPublicSubnetTag3", typing.Dict[builtins.str, typing.Any]]] = None,
        vpccidr: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersVpccidr", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_flow_logs_cloud_watch_kms_key: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_flow_logs_log_format: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_flow_logs_log_group_retention: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_flow_logs_max_aggregation_interval: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_flow_logs_traffic_type: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_tenancy: typing.Optional[typing.Union["CfnVpcqsModulePropsParametersVpcTenancy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param availability_zones: List of Availability Zones to use for the subnets in the VPC. Note: The logical order is preserved.
        :param create_additional_private_subnets: Set to true to create a network ACL protected subnet in each Availability Zone. If false, the CIDR parameters for those subnets will be ignored. If true, it also requires that the 'Create private subnets' parameter is also true to have any effect.
        :param create_nat_gateways: Set to false when creating only private subnets. If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.
        :param create_private_subnets: Set to false to create only public subnets. If false, the CIDR parameters for ALL private subnets will be ignored.
        :param create_public_subnets: Set to false to create only private subnets. If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored
        :param create_vpc_flow_logs_to_cloud_watch: Set to true to create VPC flow logs for the VPC and publish them to CloudWatch. If false, VPC flow logs will not be created.
        :param number_of_a_zs: Number of Availability Zones to use in the VPC. This must match your selections in the list of Availability Zones parameter.
        :param private_subnet1_acidr: CIDR block for private subnet 1A located in Availability Zone 1.
        :param private_subnet1_bcidr: CIDR block for private subnet 1B with dedicated network ACL located in Availability Zone 1.
        :param private_subnet2_acidr: CIDR block for private subnet 2A located in Availability Zone 2.
        :param private_subnet2_bcidr: CIDR block for private subnet 2B with dedicated network ACL located in Availability Zone 2.
        :param private_subnet3_acidr: CIDR block for private subnet 3A located in Availability Zone 3.
        :param private_subnet3_bcidr: CIDR block for private subnet 3B with dedicated network ACL located in Availability Zone 3.
        :param private_subnet4_acidr: CIDR block for private subnet 4A located in Availability Zone 4.
        :param private_subnet4_bcidr: CIDR block for private subnet 4B with dedicated network ACL located in Availability Zone 4.
        :param private_subnet_a_tag1: tag to add to private subnets A, in format Key=Value (Optional).
        :param private_subnet_a_tag2: tag to add to private subnets A, in format Key=Value (Optional).
        :param private_subnet_a_tag3: tag to add to private subnets A, in format Key=Value (Optional).
        :param private_subnet_b_tag1: tag to add to private subnets B, in format Key=Value (Optional).
        :param private_subnet_b_tag2: tag to add to private subnets B, in format Key=Value (Optional).
        :param private_subnet_b_tag3: tag to add to private subnets B, in format Key=Value (Optional).
        :param public_subnet1_cidr: CIDR block for the public DMZ subnet 1 located in Availability Zone 1.
        :param public_subnet2_cidr: CIDR block for the public DMZ subnet 2 located in Availability Zone 2.
        :param public_subnet3_cidr: CIDR block for the public DMZ subnet 3 located in Availability Zone 3.
        :param public_subnet4_cidr: CIDR block for the public DMZ subnet 4 located in Availability Zone 4.
        :param public_subnet_tag1: tag to add to public subnets, in format Key=Value (Optional).
        :param public_subnet_tag2: tag to add to public subnets, in format Key=Value (Optional).
        :param public_subnet_tag3: tag to add to public subnets, in format Key=Value (Optional).
        :param vpccidr: CIDR block for the VPC.
        :param vpc_flow_logs_cloud_watch_kms_key: (Optional) KMS Key ARN to use for encrypting the VPC flow logs data. If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.
        :param vpc_flow_logs_log_format: The fields to include in the flow log record, in the order in which they should appear. Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.
        :param vpc_flow_logs_log_group_retention: Number of days to retain the VPC Flow Logs in CloudWatch.
        :param vpc_flow_logs_max_aggregation_interval: The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).
        :param vpc_flow_logs_traffic_type: The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
        :param vpc_tenancy: The allowed tenancy of instances launched into the VPC.

        :schema: CfnVpcqsModulePropsParameters
        '''
        if isinstance(availability_zones, dict):
            availability_zones = CfnVpcqsModulePropsParametersAvailabilityZones(**availability_zones)
        if isinstance(create_additional_private_subnets, dict):
            create_additional_private_subnets = CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets(**create_additional_private_subnets)
        if isinstance(create_nat_gateways, dict):
            create_nat_gateways = CfnVpcqsModulePropsParametersCreateNatGateways(**create_nat_gateways)
        if isinstance(create_private_subnets, dict):
            create_private_subnets = CfnVpcqsModulePropsParametersCreatePrivateSubnets(**create_private_subnets)
        if isinstance(create_public_subnets, dict):
            create_public_subnets = CfnVpcqsModulePropsParametersCreatePublicSubnets(**create_public_subnets)
        if isinstance(create_vpc_flow_logs_to_cloud_watch, dict):
            create_vpc_flow_logs_to_cloud_watch = CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch(**create_vpc_flow_logs_to_cloud_watch)
        if isinstance(number_of_a_zs, dict):
            number_of_a_zs = CfnVpcqsModulePropsParametersNumberOfAZs(**number_of_a_zs)
        if isinstance(private_subnet1_acidr, dict):
            private_subnet1_acidr = CfnVpcqsModulePropsParametersPrivateSubnet1Acidr(**private_subnet1_acidr)
        if isinstance(private_subnet1_bcidr, dict):
            private_subnet1_bcidr = CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr(**private_subnet1_bcidr)
        if isinstance(private_subnet2_acidr, dict):
            private_subnet2_acidr = CfnVpcqsModulePropsParametersPrivateSubnet2Acidr(**private_subnet2_acidr)
        if isinstance(private_subnet2_bcidr, dict):
            private_subnet2_bcidr = CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr(**private_subnet2_bcidr)
        if isinstance(private_subnet3_acidr, dict):
            private_subnet3_acidr = CfnVpcqsModulePropsParametersPrivateSubnet3Acidr(**private_subnet3_acidr)
        if isinstance(private_subnet3_bcidr, dict):
            private_subnet3_bcidr = CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr(**private_subnet3_bcidr)
        if isinstance(private_subnet4_acidr, dict):
            private_subnet4_acidr = CfnVpcqsModulePropsParametersPrivateSubnet4Acidr(**private_subnet4_acidr)
        if isinstance(private_subnet4_bcidr, dict):
            private_subnet4_bcidr = CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr(**private_subnet4_bcidr)
        if isinstance(private_subnet_a_tag1, dict):
            private_subnet_a_tag1 = CfnVpcqsModulePropsParametersPrivateSubnetATag1(**private_subnet_a_tag1)
        if isinstance(private_subnet_a_tag2, dict):
            private_subnet_a_tag2 = CfnVpcqsModulePropsParametersPrivateSubnetATag2(**private_subnet_a_tag2)
        if isinstance(private_subnet_a_tag3, dict):
            private_subnet_a_tag3 = CfnVpcqsModulePropsParametersPrivateSubnetATag3(**private_subnet_a_tag3)
        if isinstance(private_subnet_b_tag1, dict):
            private_subnet_b_tag1 = CfnVpcqsModulePropsParametersPrivateSubnetBTag1(**private_subnet_b_tag1)
        if isinstance(private_subnet_b_tag2, dict):
            private_subnet_b_tag2 = CfnVpcqsModulePropsParametersPrivateSubnetBTag2(**private_subnet_b_tag2)
        if isinstance(private_subnet_b_tag3, dict):
            private_subnet_b_tag3 = CfnVpcqsModulePropsParametersPrivateSubnetBTag3(**private_subnet_b_tag3)
        if isinstance(public_subnet1_cidr, dict):
            public_subnet1_cidr = CfnVpcqsModulePropsParametersPublicSubnet1Cidr(**public_subnet1_cidr)
        if isinstance(public_subnet2_cidr, dict):
            public_subnet2_cidr = CfnVpcqsModulePropsParametersPublicSubnet2Cidr(**public_subnet2_cidr)
        if isinstance(public_subnet3_cidr, dict):
            public_subnet3_cidr = CfnVpcqsModulePropsParametersPublicSubnet3Cidr(**public_subnet3_cidr)
        if isinstance(public_subnet4_cidr, dict):
            public_subnet4_cidr = CfnVpcqsModulePropsParametersPublicSubnet4Cidr(**public_subnet4_cidr)
        if isinstance(public_subnet_tag1, dict):
            public_subnet_tag1 = CfnVpcqsModulePropsParametersPublicSubnetTag1(**public_subnet_tag1)
        if isinstance(public_subnet_tag2, dict):
            public_subnet_tag2 = CfnVpcqsModulePropsParametersPublicSubnetTag2(**public_subnet_tag2)
        if isinstance(public_subnet_tag3, dict):
            public_subnet_tag3 = CfnVpcqsModulePropsParametersPublicSubnetTag3(**public_subnet_tag3)
        if isinstance(vpccidr, dict):
            vpccidr = CfnVpcqsModulePropsParametersVpccidr(**vpccidr)
        if isinstance(vpc_flow_logs_cloud_watch_kms_key, dict):
            vpc_flow_logs_cloud_watch_kms_key = CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey(**vpc_flow_logs_cloud_watch_kms_key)
        if isinstance(vpc_flow_logs_log_format, dict):
            vpc_flow_logs_log_format = CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat(**vpc_flow_logs_log_format)
        if isinstance(vpc_flow_logs_log_group_retention, dict):
            vpc_flow_logs_log_group_retention = CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention(**vpc_flow_logs_log_group_retention)
        if isinstance(vpc_flow_logs_max_aggregation_interval, dict):
            vpc_flow_logs_max_aggregation_interval = CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval(**vpc_flow_logs_max_aggregation_interval)
        if isinstance(vpc_flow_logs_traffic_type, dict):
            vpc_flow_logs_traffic_type = CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType(**vpc_flow_logs_traffic_type)
        if isinstance(vpc_tenancy, dict):
            vpc_tenancy = CfnVpcqsModulePropsParametersVpcTenancy(**vpc_tenancy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b24fb7876b2d6f328c3a04afb85864a5e64a1d432057cd8eeee0d71b636ac595)
            check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
            check_type(argname="argument create_additional_private_subnets", value=create_additional_private_subnets, expected_type=type_hints["create_additional_private_subnets"])
            check_type(argname="argument create_nat_gateways", value=create_nat_gateways, expected_type=type_hints["create_nat_gateways"])
            check_type(argname="argument create_private_subnets", value=create_private_subnets, expected_type=type_hints["create_private_subnets"])
            check_type(argname="argument create_public_subnets", value=create_public_subnets, expected_type=type_hints["create_public_subnets"])
            check_type(argname="argument create_vpc_flow_logs_to_cloud_watch", value=create_vpc_flow_logs_to_cloud_watch, expected_type=type_hints["create_vpc_flow_logs_to_cloud_watch"])
            check_type(argname="argument number_of_a_zs", value=number_of_a_zs, expected_type=type_hints["number_of_a_zs"])
            check_type(argname="argument private_subnet1_acidr", value=private_subnet1_acidr, expected_type=type_hints["private_subnet1_acidr"])
            check_type(argname="argument private_subnet1_bcidr", value=private_subnet1_bcidr, expected_type=type_hints["private_subnet1_bcidr"])
            check_type(argname="argument private_subnet2_acidr", value=private_subnet2_acidr, expected_type=type_hints["private_subnet2_acidr"])
            check_type(argname="argument private_subnet2_bcidr", value=private_subnet2_bcidr, expected_type=type_hints["private_subnet2_bcidr"])
            check_type(argname="argument private_subnet3_acidr", value=private_subnet3_acidr, expected_type=type_hints["private_subnet3_acidr"])
            check_type(argname="argument private_subnet3_bcidr", value=private_subnet3_bcidr, expected_type=type_hints["private_subnet3_bcidr"])
            check_type(argname="argument private_subnet4_acidr", value=private_subnet4_acidr, expected_type=type_hints["private_subnet4_acidr"])
            check_type(argname="argument private_subnet4_bcidr", value=private_subnet4_bcidr, expected_type=type_hints["private_subnet4_bcidr"])
            check_type(argname="argument private_subnet_a_tag1", value=private_subnet_a_tag1, expected_type=type_hints["private_subnet_a_tag1"])
            check_type(argname="argument private_subnet_a_tag2", value=private_subnet_a_tag2, expected_type=type_hints["private_subnet_a_tag2"])
            check_type(argname="argument private_subnet_a_tag3", value=private_subnet_a_tag3, expected_type=type_hints["private_subnet_a_tag3"])
            check_type(argname="argument private_subnet_b_tag1", value=private_subnet_b_tag1, expected_type=type_hints["private_subnet_b_tag1"])
            check_type(argname="argument private_subnet_b_tag2", value=private_subnet_b_tag2, expected_type=type_hints["private_subnet_b_tag2"])
            check_type(argname="argument private_subnet_b_tag3", value=private_subnet_b_tag3, expected_type=type_hints["private_subnet_b_tag3"])
            check_type(argname="argument public_subnet1_cidr", value=public_subnet1_cidr, expected_type=type_hints["public_subnet1_cidr"])
            check_type(argname="argument public_subnet2_cidr", value=public_subnet2_cidr, expected_type=type_hints["public_subnet2_cidr"])
            check_type(argname="argument public_subnet3_cidr", value=public_subnet3_cidr, expected_type=type_hints["public_subnet3_cidr"])
            check_type(argname="argument public_subnet4_cidr", value=public_subnet4_cidr, expected_type=type_hints["public_subnet4_cidr"])
            check_type(argname="argument public_subnet_tag1", value=public_subnet_tag1, expected_type=type_hints["public_subnet_tag1"])
            check_type(argname="argument public_subnet_tag2", value=public_subnet_tag2, expected_type=type_hints["public_subnet_tag2"])
            check_type(argname="argument public_subnet_tag3", value=public_subnet_tag3, expected_type=type_hints["public_subnet_tag3"])
            check_type(argname="argument vpccidr", value=vpccidr, expected_type=type_hints["vpccidr"])
            check_type(argname="argument vpc_flow_logs_cloud_watch_kms_key", value=vpc_flow_logs_cloud_watch_kms_key, expected_type=type_hints["vpc_flow_logs_cloud_watch_kms_key"])
            check_type(argname="argument vpc_flow_logs_log_format", value=vpc_flow_logs_log_format, expected_type=type_hints["vpc_flow_logs_log_format"])
            check_type(argname="argument vpc_flow_logs_log_group_retention", value=vpc_flow_logs_log_group_retention, expected_type=type_hints["vpc_flow_logs_log_group_retention"])
            check_type(argname="argument vpc_flow_logs_max_aggregation_interval", value=vpc_flow_logs_max_aggregation_interval, expected_type=type_hints["vpc_flow_logs_max_aggregation_interval"])
            check_type(argname="argument vpc_flow_logs_traffic_type", value=vpc_flow_logs_traffic_type, expected_type=type_hints["vpc_flow_logs_traffic_type"])
            check_type(argname="argument vpc_tenancy", value=vpc_tenancy, expected_type=type_hints["vpc_tenancy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zones is not None:
            self._values["availability_zones"] = availability_zones
        if create_additional_private_subnets is not None:
            self._values["create_additional_private_subnets"] = create_additional_private_subnets
        if create_nat_gateways is not None:
            self._values["create_nat_gateways"] = create_nat_gateways
        if create_private_subnets is not None:
            self._values["create_private_subnets"] = create_private_subnets
        if create_public_subnets is not None:
            self._values["create_public_subnets"] = create_public_subnets
        if create_vpc_flow_logs_to_cloud_watch is not None:
            self._values["create_vpc_flow_logs_to_cloud_watch"] = create_vpc_flow_logs_to_cloud_watch
        if number_of_a_zs is not None:
            self._values["number_of_a_zs"] = number_of_a_zs
        if private_subnet1_acidr is not None:
            self._values["private_subnet1_acidr"] = private_subnet1_acidr
        if private_subnet1_bcidr is not None:
            self._values["private_subnet1_bcidr"] = private_subnet1_bcidr
        if private_subnet2_acidr is not None:
            self._values["private_subnet2_acidr"] = private_subnet2_acidr
        if private_subnet2_bcidr is not None:
            self._values["private_subnet2_bcidr"] = private_subnet2_bcidr
        if private_subnet3_acidr is not None:
            self._values["private_subnet3_acidr"] = private_subnet3_acidr
        if private_subnet3_bcidr is not None:
            self._values["private_subnet3_bcidr"] = private_subnet3_bcidr
        if private_subnet4_acidr is not None:
            self._values["private_subnet4_acidr"] = private_subnet4_acidr
        if private_subnet4_bcidr is not None:
            self._values["private_subnet4_bcidr"] = private_subnet4_bcidr
        if private_subnet_a_tag1 is not None:
            self._values["private_subnet_a_tag1"] = private_subnet_a_tag1
        if private_subnet_a_tag2 is not None:
            self._values["private_subnet_a_tag2"] = private_subnet_a_tag2
        if private_subnet_a_tag3 is not None:
            self._values["private_subnet_a_tag3"] = private_subnet_a_tag3
        if private_subnet_b_tag1 is not None:
            self._values["private_subnet_b_tag1"] = private_subnet_b_tag1
        if private_subnet_b_tag2 is not None:
            self._values["private_subnet_b_tag2"] = private_subnet_b_tag2
        if private_subnet_b_tag3 is not None:
            self._values["private_subnet_b_tag3"] = private_subnet_b_tag3
        if public_subnet1_cidr is not None:
            self._values["public_subnet1_cidr"] = public_subnet1_cidr
        if public_subnet2_cidr is not None:
            self._values["public_subnet2_cidr"] = public_subnet2_cidr
        if public_subnet3_cidr is not None:
            self._values["public_subnet3_cidr"] = public_subnet3_cidr
        if public_subnet4_cidr is not None:
            self._values["public_subnet4_cidr"] = public_subnet4_cidr
        if public_subnet_tag1 is not None:
            self._values["public_subnet_tag1"] = public_subnet_tag1
        if public_subnet_tag2 is not None:
            self._values["public_subnet_tag2"] = public_subnet_tag2
        if public_subnet_tag3 is not None:
            self._values["public_subnet_tag3"] = public_subnet_tag3
        if vpccidr is not None:
            self._values["vpccidr"] = vpccidr
        if vpc_flow_logs_cloud_watch_kms_key is not None:
            self._values["vpc_flow_logs_cloud_watch_kms_key"] = vpc_flow_logs_cloud_watch_kms_key
        if vpc_flow_logs_log_format is not None:
            self._values["vpc_flow_logs_log_format"] = vpc_flow_logs_log_format
        if vpc_flow_logs_log_group_retention is not None:
            self._values["vpc_flow_logs_log_group_retention"] = vpc_flow_logs_log_group_retention
        if vpc_flow_logs_max_aggregation_interval is not None:
            self._values["vpc_flow_logs_max_aggregation_interval"] = vpc_flow_logs_max_aggregation_interval
        if vpc_flow_logs_traffic_type is not None:
            self._values["vpc_flow_logs_traffic_type"] = vpc_flow_logs_traffic_type
        if vpc_tenancy is not None:
            self._values["vpc_tenancy"] = vpc_tenancy

    @builtins.property
    def availability_zones(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersAvailabilityZones"]:
        '''List of Availability Zones to use for the subnets in the VPC.

        Note: The logical order is preserved.

        :schema: CfnVpcqsModulePropsParameters#AvailabilityZones
        '''
        result = self._values.get("availability_zones")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersAvailabilityZones"], result)

    @builtins.property
    def create_additional_private_subnets(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets"]:
        '''Set to true to create a network ACL protected subnet in each Availability Zone.

        If false, the CIDR parameters for those subnets will be ignored. If true, it also requires that the 'Create private subnets' parameter is also true to have any effect.

        :schema: CfnVpcqsModulePropsParameters#CreateAdditionalPrivateSubnets
        '''
        result = self._values.get("create_additional_private_subnets")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets"], result)

    @builtins.property
    def create_nat_gateways(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersCreateNatGateways"]:
        '''Set to false when creating only private subnets.

        If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.

        :schema: CfnVpcqsModulePropsParameters#CreateNATGateways
        '''
        result = self._values.get("create_nat_gateways")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersCreateNatGateways"], result)

    @builtins.property
    def create_private_subnets(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersCreatePrivateSubnets"]:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored.

        :schema: CfnVpcqsModulePropsParameters#CreatePrivateSubnets
        '''
        result = self._values.get("create_private_subnets")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersCreatePrivateSubnets"], result)

    @builtins.property
    def create_public_subnets(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersCreatePublicSubnets"]:
        '''Set to false to create only private subnets.

        If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored

        :schema: CfnVpcqsModulePropsParameters#CreatePublicSubnets
        '''
        result = self._values.get("create_public_subnets")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersCreatePublicSubnets"], result)

    @builtins.property
    def create_vpc_flow_logs_to_cloud_watch(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch"]:
        '''Set to true to create VPC flow logs for the VPC and publish them to CloudWatch.

        If false, VPC flow logs will not be created.

        :schema: CfnVpcqsModulePropsParameters#CreateVPCFlowLogsToCloudWatch
        '''
        result = self._values.get("create_vpc_flow_logs_to_cloud_watch")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch"], result)

    @builtins.property
    def number_of_a_zs(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersNumberOfAZs"]:
        '''Number of Availability Zones to use in the VPC.

        This must match your selections in the list of Availability Zones parameter.

        :schema: CfnVpcqsModulePropsParameters#NumberOfAZs
        '''
        result = self._values.get("number_of_a_zs")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersNumberOfAZs"], result)

    @builtins.property
    def private_subnet1_acidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet1Acidr"]:
        '''CIDR block for private subnet 1A located in Availability Zone 1.

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnet1ACIDR
        '''
        result = self._values.get("private_subnet1_acidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet1Acidr"], result)

    @builtins.property
    def private_subnet1_bcidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr"]:
        '''CIDR block for private subnet 1B with dedicated network ACL located in Availability Zone 1.

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnet1BCIDR
        '''
        result = self._values.get("private_subnet1_bcidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr"], result)

    @builtins.property
    def private_subnet2_acidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet2Acidr"]:
        '''CIDR block for private subnet 2A located in Availability Zone 2.

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnet2ACIDR
        '''
        result = self._values.get("private_subnet2_acidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet2Acidr"], result)

    @builtins.property
    def private_subnet2_bcidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr"]:
        '''CIDR block for private subnet 2B with dedicated network ACL located in Availability Zone 2.

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnet2BCIDR
        '''
        result = self._values.get("private_subnet2_bcidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr"], result)

    @builtins.property
    def private_subnet3_acidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet3Acidr"]:
        '''CIDR block for private subnet 3A located in Availability Zone 3.

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnet3ACIDR
        '''
        result = self._values.get("private_subnet3_acidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet3Acidr"], result)

    @builtins.property
    def private_subnet3_bcidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr"]:
        '''CIDR block for private subnet 3B with dedicated network ACL located in Availability Zone 3.

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnet3BCIDR
        '''
        result = self._values.get("private_subnet3_bcidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr"], result)

    @builtins.property
    def private_subnet4_acidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet4Acidr"]:
        '''CIDR block for private subnet 4A located in Availability Zone 4.

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnet4ACIDR
        '''
        result = self._values.get("private_subnet4_acidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet4Acidr"], result)

    @builtins.property
    def private_subnet4_bcidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr"]:
        '''CIDR block for private subnet 4B with dedicated network ACL located in Availability Zone 4.

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnet4BCIDR
        '''
        result = self._values.get("private_subnet4_bcidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr"], result)

    @builtins.property
    def private_subnet_a_tag1(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetATag1"]:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnetATag1
        '''
        result = self._values.get("private_subnet_a_tag1")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetATag1"], result)

    @builtins.property
    def private_subnet_a_tag2(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetATag2"]:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnetATag2
        '''
        result = self._values.get("private_subnet_a_tag2")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetATag2"], result)

    @builtins.property
    def private_subnet_a_tag3(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetATag3"]:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnetATag3
        '''
        result = self._values.get("private_subnet_a_tag3")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetATag3"], result)

    @builtins.property
    def private_subnet_b_tag1(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetBTag1"]:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnetBTag1
        '''
        result = self._values.get("private_subnet_b_tag1")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetBTag1"], result)

    @builtins.property
    def private_subnet_b_tag2(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetBTag2"]:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnetBTag2
        '''
        result = self._values.get("private_subnet_b_tag2")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetBTag2"], result)

    @builtins.property
    def private_subnet_b_tag3(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetBTag3"]:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PrivateSubnetBTag3
        '''
        result = self._values.get("private_subnet_b_tag3")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPrivateSubnetBTag3"], result)

    @builtins.property
    def public_subnet1_cidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPublicSubnet1Cidr"]:
        '''CIDR block for the public DMZ subnet 1 located in Availability Zone 1.

        :schema: CfnVpcqsModulePropsParameters#PublicSubnet1CIDR
        '''
        result = self._values.get("public_subnet1_cidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPublicSubnet1Cidr"], result)

    @builtins.property
    def public_subnet2_cidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPublicSubnet2Cidr"]:
        '''CIDR block for the public DMZ subnet 2 located in Availability Zone 2.

        :schema: CfnVpcqsModulePropsParameters#PublicSubnet2CIDR
        '''
        result = self._values.get("public_subnet2_cidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPublicSubnet2Cidr"], result)

    @builtins.property
    def public_subnet3_cidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPublicSubnet3Cidr"]:
        '''CIDR block for the public DMZ subnet 3 located in Availability Zone 3.

        :schema: CfnVpcqsModulePropsParameters#PublicSubnet3CIDR
        '''
        result = self._values.get("public_subnet3_cidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPublicSubnet3Cidr"], result)

    @builtins.property
    def public_subnet4_cidr(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPublicSubnet4Cidr"]:
        '''CIDR block for the public DMZ subnet 4 located in Availability Zone 4.

        :schema: CfnVpcqsModulePropsParameters#PublicSubnet4CIDR
        '''
        result = self._values.get("public_subnet4_cidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPublicSubnet4Cidr"], result)

    @builtins.property
    def public_subnet_tag1(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPublicSubnetTag1"]:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PublicSubnetTag1
        '''
        result = self._values.get("public_subnet_tag1")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPublicSubnetTag1"], result)

    @builtins.property
    def public_subnet_tag2(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPublicSubnetTag2"]:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PublicSubnetTag2
        '''
        result = self._values.get("public_subnet_tag2")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPublicSubnetTag2"], result)

    @builtins.property
    def public_subnet_tag3(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersPublicSubnetTag3"]:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :schema: CfnVpcqsModulePropsParameters#PublicSubnetTag3
        '''
        result = self._values.get("public_subnet_tag3")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersPublicSubnetTag3"], result)

    @builtins.property
    def vpccidr(self) -> typing.Optional["CfnVpcqsModulePropsParametersVpccidr"]:
        '''CIDR block for the VPC.

        :schema: CfnVpcqsModulePropsParameters#VPCCIDR
        '''
        result = self._values.get("vpccidr")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersVpccidr"], result)

    @builtins.property
    def vpc_flow_logs_cloud_watch_kms_key(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey"]:
        '''(Optional) KMS Key ARN to use for encrypting the VPC flow logs data.

        If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.

        :schema: CfnVpcqsModulePropsParameters#VPCFlowLogsCloudWatchKMSKey
        '''
        result = self._values.get("vpc_flow_logs_cloud_watch_kms_key")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey"], result)

    @builtins.property
    def vpc_flow_logs_log_format(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat"]:
        '''The fields to include in the flow log record, in the order in which they should appear.

        Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.

        :schema: CfnVpcqsModulePropsParameters#VPCFlowLogsLogFormat
        '''
        result = self._values.get("vpc_flow_logs_log_format")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat"], result)

    @builtins.property
    def vpc_flow_logs_log_group_retention(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention"]:
        '''Number of days to retain the VPC Flow Logs in CloudWatch.

        :schema: CfnVpcqsModulePropsParameters#VPCFlowLogsLogGroupRetention
        '''
        result = self._values.get("vpc_flow_logs_log_group_retention")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention"], result)

    @builtins.property
    def vpc_flow_logs_max_aggregation_interval(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval"]:
        '''The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record.

        You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).

        :schema: CfnVpcqsModulePropsParameters#VPCFlowLogsMaxAggregationInterval
        '''
        result = self._values.get("vpc_flow_logs_max_aggregation_interval")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval"], result)

    @builtins.property
    def vpc_flow_logs_traffic_type(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType"]:
        '''The type of traffic to log.

        You can log traffic that the resource accepts or rejects, or all traffic.

        :schema: CfnVpcqsModulePropsParameters#VPCFlowLogsTrafficType
        '''
        result = self._values.get("vpc_flow_logs_traffic_type")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType"], result)

    @builtins.property
    def vpc_tenancy(self) -> typing.Optional["CfnVpcqsModulePropsParametersVpcTenancy"]:
        '''The allowed tenancy of instances launched into the VPC.

        :schema: CfnVpcqsModulePropsParameters#VPCTenancy
        '''
        result = self._values.get("vpc_tenancy")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsParametersVpcTenancy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersAvailabilityZones",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersAvailabilityZones:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''List of Availability Zones to use for the subnets in the VPC.

        Note: The logical order is preserved.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersAvailabilityZones
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f082b85af10f31a18949321188ee85f9236c9300b5084b359211dcc8ea5b339c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersAvailabilityZones#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersAvailabilityZones#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersAvailabilityZones(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to true to create a network ACL protected subnet in each Availability Zone.

        If false, the CIDR parameters for those subnets will be ignored. If true, it also requires that the 'Create private subnets' parameter is also true to have any effect.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97765f8002b03d68af17bccf49441db59f4cd66a1985d59d677af9e6666727d5)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersCreateNatGateways",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersCreateNatGateways:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false when creating only private subnets.

        If True, both CreatePublicSubnets and CreatePrivateSubnets must also be true.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersCreateNatGateways
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ad85d44a2129bc3149e96f914532c31859ecbf542b860ff60c9df980b7d7229)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreateNatGateways#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreateNatGateways#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersCreateNatGateways(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersCreatePrivateSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersCreatePrivateSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false to create only public subnets.

        If false, the CIDR parameters for ALL private subnets will be ignored.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersCreatePrivateSubnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc4a57a934049bb1265b77849a8b573984812628d6889cfd45ea21b3d3e89117)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreatePrivateSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreatePrivateSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersCreatePrivateSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersCreatePublicSubnets",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersCreatePublicSubnets:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to false to create only private subnets.

        If false, CreatePrivateSubnets must be True and the CIDR parameters for ALL public subnets will be ignored

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersCreatePublicSubnets
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56c95c3cf3af5dc7401b7f5cd65d8196d8293795da7b0010a03683560acc4a0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreatePublicSubnets#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreatePublicSubnets#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersCreatePublicSubnets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Set to true to create VPC flow logs for the VPC and publish them to CloudWatch.

        If false, VPC flow logs will not be created.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa882eca6624ab6943fc543ae4942e09cf7b94c964af02ef779546df2f1c635)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersNumberOfAZs",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersNumberOfAZs:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of Availability Zones to use in the VPC.

        This must match your selections in the list of Availability Zones parameter.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersNumberOfAZs
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa3fdc936049706a5c5e2333cd269b4efbaf701170b9296bb4bc7db4e577bcc6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersNumberOfAZs#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersNumberOfAZs#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersNumberOfAZs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnet1Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnet1Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1A located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnet1Acidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18e0bee1aec3bbdb5989349bcb7ec4a0bba23d154e9096c5dd30b39b5ce88a25)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet1Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet1Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnet1Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 1B with dedicated network ACL located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b40018af05c15b850b79c56750e2b97f9e7b7f3be84075d480bf24079bfecc0d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnet2Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnet2Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2A located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnet2Acidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9255afbe163f1abedd5b3ef0cd0bfcb7ce7405785e5830f0ff0fda8bd1d8f61)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet2Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet2Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnet2Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 2B with dedicated network ACL located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c04a7e1692e0259ec0b58f752e3d08fdace8798f3ee696b7c827faf23adcfc6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnet3Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnet3Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 3A located in Availability Zone 3.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnet3Acidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b63166c5420d97215472df8755b1bb4d05b139d29c7a5d01ee2e7238c898757)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet3Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet3Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnet3Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 3B with dedicated network ACL located in Availability Zone 3.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec24b47b2d6b2d8050be9b946a866747d6c780a30dde2ea1c58fd2a3a94df19a)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnet4Acidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnet4Acidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 4A located in Availability Zone 4.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnet4Acidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddc81a4eec33fbb648f89257e51586d352c99a1248ac8f606b3ac7f1ede17d8b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet4Acidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet4Acidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnet4Acidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for private subnet 4B with dedicated network ACL located in Availability Zone 4.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbd5a48a6c37602431b565b655d8c0e554116d4c4b6127206607857547215c56)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnetATag1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnetATag1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41c8e54c4cbb9d904cb03bc766c1561b976902e126fd8f709ce52daba8069ef9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnetATag1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnetATag2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnetATag2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a745cdfddac18d69f34408b13ef49ebdbbee94414a2cfe2d2f97939fc2328bd)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnetATag2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnetATag3",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnetATag3:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets A, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde13280d77abf574778f8a197f71e93c1145409c274de468812291880c86636)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag3#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetATag3#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnetATag3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnetBTag1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnetBTag1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c30ae04531b2c93d633d818c388918c713c7ed0bdc8d3d92dd442e23eb0d1bc)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnetBTag1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnetBTag2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnetBTag2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2604cbed2eab9d83d2d5f736304d8789e7ec00c6eb5aee42c300858f3c05d2a2)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnetBTag2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPrivateSubnetBTag3",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPrivateSubnetBTag3:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to private subnets B, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22abb2930df6166815cd76a0b90c397fc7e27225fc4f4cbb707bf371d6808940)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag3#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPrivateSubnetBTag3#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPrivateSubnetBTag3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPublicSubnet1Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPublicSubnet1Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 1 located in Availability Zone 1.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPublicSubnet1Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d1cb697dfd4ce654a49876d7a7103464dec037649058f3e314e5ccd995933d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnet1Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnet1Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPublicSubnet1Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPublicSubnet2Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPublicSubnet2Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 2 located in Availability Zone 2.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPublicSubnet2Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3814651dfd3ba07a9e2af44806e955ccc3a76a7e518db1f4d510ab584c2505c5)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnet2Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnet2Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPublicSubnet2Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPublicSubnet3Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPublicSubnet3Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 3 located in Availability Zone 3.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPublicSubnet3Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8672a2462068a5289486f8a1546cd7cdd05c1c4c43cd838276cddc0448116256)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnet3Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnet3Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPublicSubnet3Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPublicSubnet4Cidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPublicSubnet4Cidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the public DMZ subnet 4 located in Availability Zone 4.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPublicSubnet4Cidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__414a379960ecd7a2a6b5fc096a4c78212a4f203497014274a6608c28aa59c5aa)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnet4Cidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnet4Cidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPublicSubnet4Cidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPublicSubnetTag1",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPublicSubnetTag1:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95e5b7a0c6586178b00642867ef18710e84f6382f2f649f42d88b0f85ca01bf)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag1#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag1#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPublicSubnetTag1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPublicSubnetTag2",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPublicSubnetTag2:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0813f711557a854c8796812505683ac6d8b663690b8ec3247d6129042b6a2456)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag2#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag2#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPublicSubnetTag2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersPublicSubnetTag3",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersPublicSubnetTag3:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''tag to add to public subnets, in format Key=Value (Optional).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61e1a0b5a5a13185e7c283065e1f755fe73d1ba0a84a5003541b5bb3fd31d28c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag3#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersPublicSubnetTag3#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersPublicSubnetTag3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''(Optional) KMS Key ARN to use for encrypting the VPC flow logs data.

        If empty, encryption is enabled with CloudWatch Logs managing the server-side encryption keys.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5db2ba8a7da950abe46dede641ec4d3f1a1789e9c099d2c461d35e1df0e3d41e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The fields to include in the flow log record, in the order in which they should appear.

        Specify the fields using the ${field-id} format, separated by spaces. Using the Default Format as the default value.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57f887b7e120684547a9a6aaf9bf1f7a5cf7fff92d5840a8328b1b174d276783)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Number of days to retain the VPC Flow Logs in CloudWatch.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c39600e1b80938f22edbb7bade615ed829633938eb9d9ca7c5eb3c6d8a546a17)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record.

        You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__388d244207ffa5383ebb43e50b1d3251ed518bf52e7d0aa027e52da44855b85c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The type of traffic to log.

        You can log traffic that the resource accepts or rejects, or all traffic.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4e777720237b0ee4704c2f21a04c8481d4a2e1d6b54ac935dbaedfc59083fb)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersVpcTenancy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersVpcTenancy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The allowed tenancy of instances launched into the VPC.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersVpcTenancy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97408e9c24cac272c1c330b3559c95a56796305285d802fea223c2290a33844f)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcTenancy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpcTenancy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersVpcTenancy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsParametersVpccidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnVpcqsModulePropsParametersVpccidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''CIDR block for the VPC.

        :param description: 
        :param type: 

        :schema: CfnVpcqsModulePropsParametersVpccidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d727fdf94d6dca09fb6901982df419cb2298afd1cb56d554f1223945ac662b8d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpccidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnVpcqsModulePropsParametersVpccidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsParametersVpccidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "dhcp_options": "dhcpOptions",
        "internet_gateway": "internetGateway",
        "nat1_eip": "nat1Eip",
        "nat2_eip": "nat2Eip",
        "nat3_eip": "nat3Eip",
        "nat4_eip": "nat4Eip",
        "nat_gateway1": "natGateway1",
        "nat_gateway2": "natGateway2",
        "nat_gateway3": "natGateway3",
        "nat_gateway4": "natGateway4",
        "private_subnet1_a": "privateSubnet1A",
        "private_subnet1_a_route": "privateSubnet1ARoute",
        "private_subnet1_a_route_table": "privateSubnet1ARouteTable",
        "private_subnet1_a_route_table_association": "privateSubnet1ARouteTableAssociation",
        "private_subnet1_b": "privateSubnet1B",
        "private_subnet1_b_network_acl": "privateSubnet1BNetworkAcl",
        "private_subnet1_b_network_acl_association": "privateSubnet1BNetworkAclAssociation",
        "private_subnet1_b_network_acl_entry_inbound": "privateSubnet1BNetworkAclEntryInbound",
        "private_subnet1_b_network_acl_entry_outbound": "privateSubnet1BNetworkAclEntryOutbound",
        "private_subnet1_b_route": "privateSubnet1BRoute",
        "private_subnet1_b_route_table": "privateSubnet1BRouteTable",
        "private_subnet1_b_route_table_association": "privateSubnet1BRouteTableAssociation",
        "private_subnet2_a": "privateSubnet2A",
        "private_subnet2_a_route": "privateSubnet2ARoute",
        "private_subnet2_a_route_table": "privateSubnet2ARouteTable",
        "private_subnet2_a_route_table_association": "privateSubnet2ARouteTableAssociation",
        "private_subnet2_b": "privateSubnet2B",
        "private_subnet2_b_network_acl": "privateSubnet2BNetworkAcl",
        "private_subnet2_b_network_acl_association": "privateSubnet2BNetworkAclAssociation",
        "private_subnet2_b_network_acl_entry_inbound": "privateSubnet2BNetworkAclEntryInbound",
        "private_subnet2_b_network_acl_entry_outbound": "privateSubnet2BNetworkAclEntryOutbound",
        "private_subnet2_b_route": "privateSubnet2BRoute",
        "private_subnet2_b_route_table": "privateSubnet2BRouteTable",
        "private_subnet2_b_route_table_association": "privateSubnet2BRouteTableAssociation",
        "private_subnet3_a": "privateSubnet3A",
        "private_subnet3_a_route": "privateSubnet3ARoute",
        "private_subnet3_a_route_table": "privateSubnet3ARouteTable",
        "private_subnet3_a_route_table_association": "privateSubnet3ARouteTableAssociation",
        "private_subnet3_b": "privateSubnet3B",
        "private_subnet3_b_network_acl": "privateSubnet3BNetworkAcl",
        "private_subnet3_b_network_acl_association": "privateSubnet3BNetworkAclAssociation",
        "private_subnet3_b_network_acl_entry_inbound": "privateSubnet3BNetworkAclEntryInbound",
        "private_subnet3_b_network_acl_entry_outbound": "privateSubnet3BNetworkAclEntryOutbound",
        "private_subnet3_b_route": "privateSubnet3BRoute",
        "private_subnet3_b_route_table": "privateSubnet3BRouteTable",
        "private_subnet3_b_route_table_association": "privateSubnet3BRouteTableAssociation",
        "private_subnet4_a": "privateSubnet4A",
        "private_subnet4_a_route": "privateSubnet4ARoute",
        "private_subnet4_a_route_table": "privateSubnet4ARouteTable",
        "private_subnet4_a_route_table_association": "privateSubnet4ARouteTableAssociation",
        "private_subnet4_b": "privateSubnet4B",
        "private_subnet4_b_network_acl": "privateSubnet4BNetworkAcl",
        "private_subnet4_b_network_acl_association": "privateSubnet4BNetworkAclAssociation",
        "private_subnet4_b_network_acl_entry_inbound": "privateSubnet4BNetworkAclEntryInbound",
        "private_subnet4_b_network_acl_entry_outbound": "privateSubnet4BNetworkAclEntryOutbound",
        "private_subnet4_b_route": "privateSubnet4BRoute",
        "private_subnet4_b_route_table": "privateSubnet4BRouteTable",
        "private_subnet4_b_route_table_association": "privateSubnet4BRouteTableAssociation",
        "public_subnet1": "publicSubnet1",
        "public_subnet1_route_table_association": "publicSubnet1RouteTableAssociation",
        "public_subnet2": "publicSubnet2",
        "public_subnet2_route_table_association": "publicSubnet2RouteTableAssociation",
        "public_subnet3": "publicSubnet3",
        "public_subnet3_route_table_association": "publicSubnet3RouteTableAssociation",
        "public_subnet4": "publicSubnet4",
        "public_subnet4_route_table_association": "publicSubnet4RouteTableAssociation",
        "public_subnet_route": "publicSubnetRoute",
        "public_subnet_route_table": "publicSubnetRouteTable",
        "s3_vpc_endpoint": "s3VpcEndpoint",
        "vpc": "vpc",
        "vpcdhcp_options_association": "vpcdhcpOptionsAssociation",
        "vpc_flow_logs_log_group": "vpcFlowLogsLogGroup",
        "vpc_flow_logs_role": "vpcFlowLogsRole",
        "vpc_flow_logs_to_cloud_watch": "vpcFlowLogsToCloudWatch",
        "vpc_gateway_attachment": "vpcGatewayAttachment",
    },
)
class CfnVpcqsModulePropsResources:
    def __init__(
        self,
        *,
        dhcp_options: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesDhcpOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        internet_gateway: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesInternetGateway", typing.Dict[builtins.str, typing.Any]]] = None,
        nat1_eip: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesNat1Eip", typing.Dict[builtins.str, typing.Any]]] = None,
        nat2_eip: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesNat2Eip", typing.Dict[builtins.str, typing.Any]]] = None,
        nat3_eip: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesNat3Eip", typing.Dict[builtins.str, typing.Any]]] = None,
        nat4_eip: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesNat4Eip", typing.Dict[builtins.str, typing.Any]]] = None,
        nat_gateway1: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesNatGateway1", typing.Dict[builtins.str, typing.Any]]] = None,
        nat_gateway2: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesNatGateway2", typing.Dict[builtins.str, typing.Any]]] = None,
        nat_gateway3: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesNatGateway3", typing.Dict[builtins.str, typing.Any]]] = None,
        nat_gateway4: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesNatGateway4", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_a: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1A", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_a_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_a_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_a_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_b: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1B", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_b_network_acl: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_b_network_acl_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_b_network_acl_entry_inbound: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_b_network_acl_entry_outbound: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_b_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_b_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet1_b_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_a: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2A", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_a_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_a_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_a_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_b: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2B", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_b_network_acl: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_b_network_acl_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_b_network_acl_entry_inbound: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_b_network_acl_entry_outbound: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_b_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_b_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet2_b_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_a: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3A", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_a_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_a_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_a_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_b: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3B", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_b_network_acl: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_b_network_acl_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_b_network_acl_entry_inbound: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_b_network_acl_entry_outbound: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_b_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_b_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet3_b_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_a: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4A", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_a_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_a_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_a_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_b: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4B", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_b_network_acl: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_b_network_acl_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_b_network_acl_entry_inbound: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_b_network_acl_entry_outbound: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_b_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_b_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        private_subnet4_b_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnet1", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnet2", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet3: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnet3", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet3_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet4: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnet4", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet4_route_table_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet_route: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnetRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet_route_table: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesPublicSubnetRouteTable", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_vpc_endpoint: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesS3VpcEndpoint", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesVpc", typing.Dict[builtins.str, typing.Any]]] = None,
        vpcdhcp_options_association: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_flow_logs_log_group: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_flow_logs_role: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesVpcFlowLogsRole", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_flow_logs_to_cloud_watch: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_gateway_attachment: typing.Optional[typing.Union["CfnVpcqsModulePropsResourcesVpcGatewayAttachment", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dhcp_options: 
        :param internet_gateway: 
        :param nat1_eip: 
        :param nat2_eip: 
        :param nat3_eip: 
        :param nat4_eip: 
        :param nat_gateway1: 
        :param nat_gateway2: 
        :param nat_gateway3: 
        :param nat_gateway4: 
        :param private_subnet1_a: 
        :param private_subnet1_a_route: 
        :param private_subnet1_a_route_table: 
        :param private_subnet1_a_route_table_association: 
        :param private_subnet1_b: 
        :param private_subnet1_b_network_acl: 
        :param private_subnet1_b_network_acl_association: 
        :param private_subnet1_b_network_acl_entry_inbound: 
        :param private_subnet1_b_network_acl_entry_outbound: 
        :param private_subnet1_b_route: 
        :param private_subnet1_b_route_table: 
        :param private_subnet1_b_route_table_association: 
        :param private_subnet2_a: 
        :param private_subnet2_a_route: 
        :param private_subnet2_a_route_table: 
        :param private_subnet2_a_route_table_association: 
        :param private_subnet2_b: 
        :param private_subnet2_b_network_acl: 
        :param private_subnet2_b_network_acl_association: 
        :param private_subnet2_b_network_acl_entry_inbound: 
        :param private_subnet2_b_network_acl_entry_outbound: 
        :param private_subnet2_b_route: 
        :param private_subnet2_b_route_table: 
        :param private_subnet2_b_route_table_association: 
        :param private_subnet3_a: 
        :param private_subnet3_a_route: 
        :param private_subnet3_a_route_table: 
        :param private_subnet3_a_route_table_association: 
        :param private_subnet3_b: 
        :param private_subnet3_b_network_acl: 
        :param private_subnet3_b_network_acl_association: 
        :param private_subnet3_b_network_acl_entry_inbound: 
        :param private_subnet3_b_network_acl_entry_outbound: 
        :param private_subnet3_b_route: 
        :param private_subnet3_b_route_table: 
        :param private_subnet3_b_route_table_association: 
        :param private_subnet4_a: 
        :param private_subnet4_a_route: 
        :param private_subnet4_a_route_table: 
        :param private_subnet4_a_route_table_association: 
        :param private_subnet4_b: 
        :param private_subnet4_b_network_acl: 
        :param private_subnet4_b_network_acl_association: 
        :param private_subnet4_b_network_acl_entry_inbound: 
        :param private_subnet4_b_network_acl_entry_outbound: 
        :param private_subnet4_b_route: 
        :param private_subnet4_b_route_table: 
        :param private_subnet4_b_route_table_association: 
        :param public_subnet1: 
        :param public_subnet1_route_table_association: 
        :param public_subnet2: 
        :param public_subnet2_route_table_association: 
        :param public_subnet3: 
        :param public_subnet3_route_table_association: 
        :param public_subnet4: 
        :param public_subnet4_route_table_association: 
        :param public_subnet_route: 
        :param public_subnet_route_table: 
        :param s3_vpc_endpoint: 
        :param vpc: 
        :param vpcdhcp_options_association: 
        :param vpc_flow_logs_log_group: 
        :param vpc_flow_logs_role: 
        :param vpc_flow_logs_to_cloud_watch: 
        :param vpc_gateway_attachment: 

        :schema: CfnVpcqsModulePropsResources
        '''
        if isinstance(dhcp_options, dict):
            dhcp_options = CfnVpcqsModulePropsResourcesDhcpOptions(**dhcp_options)
        if isinstance(internet_gateway, dict):
            internet_gateway = CfnVpcqsModulePropsResourcesInternetGateway(**internet_gateway)
        if isinstance(nat1_eip, dict):
            nat1_eip = CfnVpcqsModulePropsResourcesNat1Eip(**nat1_eip)
        if isinstance(nat2_eip, dict):
            nat2_eip = CfnVpcqsModulePropsResourcesNat2Eip(**nat2_eip)
        if isinstance(nat3_eip, dict):
            nat3_eip = CfnVpcqsModulePropsResourcesNat3Eip(**nat3_eip)
        if isinstance(nat4_eip, dict):
            nat4_eip = CfnVpcqsModulePropsResourcesNat4Eip(**nat4_eip)
        if isinstance(nat_gateway1, dict):
            nat_gateway1 = CfnVpcqsModulePropsResourcesNatGateway1(**nat_gateway1)
        if isinstance(nat_gateway2, dict):
            nat_gateway2 = CfnVpcqsModulePropsResourcesNatGateway2(**nat_gateway2)
        if isinstance(nat_gateway3, dict):
            nat_gateway3 = CfnVpcqsModulePropsResourcesNatGateway3(**nat_gateway3)
        if isinstance(nat_gateway4, dict):
            nat_gateway4 = CfnVpcqsModulePropsResourcesNatGateway4(**nat_gateway4)
        if isinstance(private_subnet1_a, dict):
            private_subnet1_a = CfnVpcqsModulePropsResourcesPrivateSubnet1A(**private_subnet1_a)
        if isinstance(private_subnet1_a_route, dict):
            private_subnet1_a_route = CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute(**private_subnet1_a_route)
        if isinstance(private_subnet1_a_route_table, dict):
            private_subnet1_a_route_table = CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable(**private_subnet1_a_route_table)
        if isinstance(private_subnet1_a_route_table_association, dict):
            private_subnet1_a_route_table_association = CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation(**private_subnet1_a_route_table_association)
        if isinstance(private_subnet1_b, dict):
            private_subnet1_b = CfnVpcqsModulePropsResourcesPrivateSubnet1B(**private_subnet1_b)
        if isinstance(private_subnet1_b_network_acl, dict):
            private_subnet1_b_network_acl = CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl(**private_subnet1_b_network_acl)
        if isinstance(private_subnet1_b_network_acl_association, dict):
            private_subnet1_b_network_acl_association = CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation(**private_subnet1_b_network_acl_association)
        if isinstance(private_subnet1_b_network_acl_entry_inbound, dict):
            private_subnet1_b_network_acl_entry_inbound = CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound(**private_subnet1_b_network_acl_entry_inbound)
        if isinstance(private_subnet1_b_network_acl_entry_outbound, dict):
            private_subnet1_b_network_acl_entry_outbound = CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound(**private_subnet1_b_network_acl_entry_outbound)
        if isinstance(private_subnet1_b_route, dict):
            private_subnet1_b_route = CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute(**private_subnet1_b_route)
        if isinstance(private_subnet1_b_route_table, dict):
            private_subnet1_b_route_table = CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable(**private_subnet1_b_route_table)
        if isinstance(private_subnet1_b_route_table_association, dict):
            private_subnet1_b_route_table_association = CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation(**private_subnet1_b_route_table_association)
        if isinstance(private_subnet2_a, dict):
            private_subnet2_a = CfnVpcqsModulePropsResourcesPrivateSubnet2A(**private_subnet2_a)
        if isinstance(private_subnet2_a_route, dict):
            private_subnet2_a_route = CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute(**private_subnet2_a_route)
        if isinstance(private_subnet2_a_route_table, dict):
            private_subnet2_a_route_table = CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable(**private_subnet2_a_route_table)
        if isinstance(private_subnet2_a_route_table_association, dict):
            private_subnet2_a_route_table_association = CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation(**private_subnet2_a_route_table_association)
        if isinstance(private_subnet2_b, dict):
            private_subnet2_b = CfnVpcqsModulePropsResourcesPrivateSubnet2B(**private_subnet2_b)
        if isinstance(private_subnet2_b_network_acl, dict):
            private_subnet2_b_network_acl = CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl(**private_subnet2_b_network_acl)
        if isinstance(private_subnet2_b_network_acl_association, dict):
            private_subnet2_b_network_acl_association = CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation(**private_subnet2_b_network_acl_association)
        if isinstance(private_subnet2_b_network_acl_entry_inbound, dict):
            private_subnet2_b_network_acl_entry_inbound = CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound(**private_subnet2_b_network_acl_entry_inbound)
        if isinstance(private_subnet2_b_network_acl_entry_outbound, dict):
            private_subnet2_b_network_acl_entry_outbound = CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound(**private_subnet2_b_network_acl_entry_outbound)
        if isinstance(private_subnet2_b_route, dict):
            private_subnet2_b_route = CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute(**private_subnet2_b_route)
        if isinstance(private_subnet2_b_route_table, dict):
            private_subnet2_b_route_table = CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable(**private_subnet2_b_route_table)
        if isinstance(private_subnet2_b_route_table_association, dict):
            private_subnet2_b_route_table_association = CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation(**private_subnet2_b_route_table_association)
        if isinstance(private_subnet3_a, dict):
            private_subnet3_a = CfnVpcqsModulePropsResourcesPrivateSubnet3A(**private_subnet3_a)
        if isinstance(private_subnet3_a_route, dict):
            private_subnet3_a_route = CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute(**private_subnet3_a_route)
        if isinstance(private_subnet3_a_route_table, dict):
            private_subnet3_a_route_table = CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable(**private_subnet3_a_route_table)
        if isinstance(private_subnet3_a_route_table_association, dict):
            private_subnet3_a_route_table_association = CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation(**private_subnet3_a_route_table_association)
        if isinstance(private_subnet3_b, dict):
            private_subnet3_b = CfnVpcqsModulePropsResourcesPrivateSubnet3B(**private_subnet3_b)
        if isinstance(private_subnet3_b_network_acl, dict):
            private_subnet3_b_network_acl = CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl(**private_subnet3_b_network_acl)
        if isinstance(private_subnet3_b_network_acl_association, dict):
            private_subnet3_b_network_acl_association = CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation(**private_subnet3_b_network_acl_association)
        if isinstance(private_subnet3_b_network_acl_entry_inbound, dict):
            private_subnet3_b_network_acl_entry_inbound = CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound(**private_subnet3_b_network_acl_entry_inbound)
        if isinstance(private_subnet3_b_network_acl_entry_outbound, dict):
            private_subnet3_b_network_acl_entry_outbound = CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound(**private_subnet3_b_network_acl_entry_outbound)
        if isinstance(private_subnet3_b_route, dict):
            private_subnet3_b_route = CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute(**private_subnet3_b_route)
        if isinstance(private_subnet3_b_route_table, dict):
            private_subnet3_b_route_table = CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable(**private_subnet3_b_route_table)
        if isinstance(private_subnet3_b_route_table_association, dict):
            private_subnet3_b_route_table_association = CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation(**private_subnet3_b_route_table_association)
        if isinstance(private_subnet4_a, dict):
            private_subnet4_a = CfnVpcqsModulePropsResourcesPrivateSubnet4A(**private_subnet4_a)
        if isinstance(private_subnet4_a_route, dict):
            private_subnet4_a_route = CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute(**private_subnet4_a_route)
        if isinstance(private_subnet4_a_route_table, dict):
            private_subnet4_a_route_table = CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable(**private_subnet4_a_route_table)
        if isinstance(private_subnet4_a_route_table_association, dict):
            private_subnet4_a_route_table_association = CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation(**private_subnet4_a_route_table_association)
        if isinstance(private_subnet4_b, dict):
            private_subnet4_b = CfnVpcqsModulePropsResourcesPrivateSubnet4B(**private_subnet4_b)
        if isinstance(private_subnet4_b_network_acl, dict):
            private_subnet4_b_network_acl = CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl(**private_subnet4_b_network_acl)
        if isinstance(private_subnet4_b_network_acl_association, dict):
            private_subnet4_b_network_acl_association = CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation(**private_subnet4_b_network_acl_association)
        if isinstance(private_subnet4_b_network_acl_entry_inbound, dict):
            private_subnet4_b_network_acl_entry_inbound = CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound(**private_subnet4_b_network_acl_entry_inbound)
        if isinstance(private_subnet4_b_network_acl_entry_outbound, dict):
            private_subnet4_b_network_acl_entry_outbound = CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound(**private_subnet4_b_network_acl_entry_outbound)
        if isinstance(private_subnet4_b_route, dict):
            private_subnet4_b_route = CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute(**private_subnet4_b_route)
        if isinstance(private_subnet4_b_route_table, dict):
            private_subnet4_b_route_table = CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable(**private_subnet4_b_route_table)
        if isinstance(private_subnet4_b_route_table_association, dict):
            private_subnet4_b_route_table_association = CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation(**private_subnet4_b_route_table_association)
        if isinstance(public_subnet1, dict):
            public_subnet1 = CfnVpcqsModulePropsResourcesPublicSubnet1(**public_subnet1)
        if isinstance(public_subnet1_route_table_association, dict):
            public_subnet1_route_table_association = CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation(**public_subnet1_route_table_association)
        if isinstance(public_subnet2, dict):
            public_subnet2 = CfnVpcqsModulePropsResourcesPublicSubnet2(**public_subnet2)
        if isinstance(public_subnet2_route_table_association, dict):
            public_subnet2_route_table_association = CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation(**public_subnet2_route_table_association)
        if isinstance(public_subnet3, dict):
            public_subnet3 = CfnVpcqsModulePropsResourcesPublicSubnet3(**public_subnet3)
        if isinstance(public_subnet3_route_table_association, dict):
            public_subnet3_route_table_association = CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation(**public_subnet3_route_table_association)
        if isinstance(public_subnet4, dict):
            public_subnet4 = CfnVpcqsModulePropsResourcesPublicSubnet4(**public_subnet4)
        if isinstance(public_subnet4_route_table_association, dict):
            public_subnet4_route_table_association = CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation(**public_subnet4_route_table_association)
        if isinstance(public_subnet_route, dict):
            public_subnet_route = CfnVpcqsModulePropsResourcesPublicSubnetRoute(**public_subnet_route)
        if isinstance(public_subnet_route_table, dict):
            public_subnet_route_table = CfnVpcqsModulePropsResourcesPublicSubnetRouteTable(**public_subnet_route_table)
        if isinstance(s3_vpc_endpoint, dict):
            s3_vpc_endpoint = CfnVpcqsModulePropsResourcesS3VpcEndpoint(**s3_vpc_endpoint)
        if isinstance(vpc, dict):
            vpc = CfnVpcqsModulePropsResourcesVpc(**vpc)
        if isinstance(vpcdhcp_options_association, dict):
            vpcdhcp_options_association = CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation(**vpcdhcp_options_association)
        if isinstance(vpc_flow_logs_log_group, dict):
            vpc_flow_logs_log_group = CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup(**vpc_flow_logs_log_group)
        if isinstance(vpc_flow_logs_role, dict):
            vpc_flow_logs_role = CfnVpcqsModulePropsResourcesVpcFlowLogsRole(**vpc_flow_logs_role)
        if isinstance(vpc_flow_logs_to_cloud_watch, dict):
            vpc_flow_logs_to_cloud_watch = CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch(**vpc_flow_logs_to_cloud_watch)
        if isinstance(vpc_gateway_attachment, dict):
            vpc_gateway_attachment = CfnVpcqsModulePropsResourcesVpcGatewayAttachment(**vpc_gateway_attachment)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40bc2466d9903edb953edc8386d5d642d73d1bd38baddbdc76590b9b09a4a8d3)
            check_type(argname="argument dhcp_options", value=dhcp_options, expected_type=type_hints["dhcp_options"])
            check_type(argname="argument internet_gateway", value=internet_gateway, expected_type=type_hints["internet_gateway"])
            check_type(argname="argument nat1_eip", value=nat1_eip, expected_type=type_hints["nat1_eip"])
            check_type(argname="argument nat2_eip", value=nat2_eip, expected_type=type_hints["nat2_eip"])
            check_type(argname="argument nat3_eip", value=nat3_eip, expected_type=type_hints["nat3_eip"])
            check_type(argname="argument nat4_eip", value=nat4_eip, expected_type=type_hints["nat4_eip"])
            check_type(argname="argument nat_gateway1", value=nat_gateway1, expected_type=type_hints["nat_gateway1"])
            check_type(argname="argument nat_gateway2", value=nat_gateway2, expected_type=type_hints["nat_gateway2"])
            check_type(argname="argument nat_gateway3", value=nat_gateway3, expected_type=type_hints["nat_gateway3"])
            check_type(argname="argument nat_gateway4", value=nat_gateway4, expected_type=type_hints["nat_gateway4"])
            check_type(argname="argument private_subnet1_a", value=private_subnet1_a, expected_type=type_hints["private_subnet1_a"])
            check_type(argname="argument private_subnet1_a_route", value=private_subnet1_a_route, expected_type=type_hints["private_subnet1_a_route"])
            check_type(argname="argument private_subnet1_a_route_table", value=private_subnet1_a_route_table, expected_type=type_hints["private_subnet1_a_route_table"])
            check_type(argname="argument private_subnet1_a_route_table_association", value=private_subnet1_a_route_table_association, expected_type=type_hints["private_subnet1_a_route_table_association"])
            check_type(argname="argument private_subnet1_b", value=private_subnet1_b, expected_type=type_hints["private_subnet1_b"])
            check_type(argname="argument private_subnet1_b_network_acl", value=private_subnet1_b_network_acl, expected_type=type_hints["private_subnet1_b_network_acl"])
            check_type(argname="argument private_subnet1_b_network_acl_association", value=private_subnet1_b_network_acl_association, expected_type=type_hints["private_subnet1_b_network_acl_association"])
            check_type(argname="argument private_subnet1_b_network_acl_entry_inbound", value=private_subnet1_b_network_acl_entry_inbound, expected_type=type_hints["private_subnet1_b_network_acl_entry_inbound"])
            check_type(argname="argument private_subnet1_b_network_acl_entry_outbound", value=private_subnet1_b_network_acl_entry_outbound, expected_type=type_hints["private_subnet1_b_network_acl_entry_outbound"])
            check_type(argname="argument private_subnet1_b_route", value=private_subnet1_b_route, expected_type=type_hints["private_subnet1_b_route"])
            check_type(argname="argument private_subnet1_b_route_table", value=private_subnet1_b_route_table, expected_type=type_hints["private_subnet1_b_route_table"])
            check_type(argname="argument private_subnet1_b_route_table_association", value=private_subnet1_b_route_table_association, expected_type=type_hints["private_subnet1_b_route_table_association"])
            check_type(argname="argument private_subnet2_a", value=private_subnet2_a, expected_type=type_hints["private_subnet2_a"])
            check_type(argname="argument private_subnet2_a_route", value=private_subnet2_a_route, expected_type=type_hints["private_subnet2_a_route"])
            check_type(argname="argument private_subnet2_a_route_table", value=private_subnet2_a_route_table, expected_type=type_hints["private_subnet2_a_route_table"])
            check_type(argname="argument private_subnet2_a_route_table_association", value=private_subnet2_a_route_table_association, expected_type=type_hints["private_subnet2_a_route_table_association"])
            check_type(argname="argument private_subnet2_b", value=private_subnet2_b, expected_type=type_hints["private_subnet2_b"])
            check_type(argname="argument private_subnet2_b_network_acl", value=private_subnet2_b_network_acl, expected_type=type_hints["private_subnet2_b_network_acl"])
            check_type(argname="argument private_subnet2_b_network_acl_association", value=private_subnet2_b_network_acl_association, expected_type=type_hints["private_subnet2_b_network_acl_association"])
            check_type(argname="argument private_subnet2_b_network_acl_entry_inbound", value=private_subnet2_b_network_acl_entry_inbound, expected_type=type_hints["private_subnet2_b_network_acl_entry_inbound"])
            check_type(argname="argument private_subnet2_b_network_acl_entry_outbound", value=private_subnet2_b_network_acl_entry_outbound, expected_type=type_hints["private_subnet2_b_network_acl_entry_outbound"])
            check_type(argname="argument private_subnet2_b_route", value=private_subnet2_b_route, expected_type=type_hints["private_subnet2_b_route"])
            check_type(argname="argument private_subnet2_b_route_table", value=private_subnet2_b_route_table, expected_type=type_hints["private_subnet2_b_route_table"])
            check_type(argname="argument private_subnet2_b_route_table_association", value=private_subnet2_b_route_table_association, expected_type=type_hints["private_subnet2_b_route_table_association"])
            check_type(argname="argument private_subnet3_a", value=private_subnet3_a, expected_type=type_hints["private_subnet3_a"])
            check_type(argname="argument private_subnet3_a_route", value=private_subnet3_a_route, expected_type=type_hints["private_subnet3_a_route"])
            check_type(argname="argument private_subnet3_a_route_table", value=private_subnet3_a_route_table, expected_type=type_hints["private_subnet3_a_route_table"])
            check_type(argname="argument private_subnet3_a_route_table_association", value=private_subnet3_a_route_table_association, expected_type=type_hints["private_subnet3_a_route_table_association"])
            check_type(argname="argument private_subnet3_b", value=private_subnet3_b, expected_type=type_hints["private_subnet3_b"])
            check_type(argname="argument private_subnet3_b_network_acl", value=private_subnet3_b_network_acl, expected_type=type_hints["private_subnet3_b_network_acl"])
            check_type(argname="argument private_subnet3_b_network_acl_association", value=private_subnet3_b_network_acl_association, expected_type=type_hints["private_subnet3_b_network_acl_association"])
            check_type(argname="argument private_subnet3_b_network_acl_entry_inbound", value=private_subnet3_b_network_acl_entry_inbound, expected_type=type_hints["private_subnet3_b_network_acl_entry_inbound"])
            check_type(argname="argument private_subnet3_b_network_acl_entry_outbound", value=private_subnet3_b_network_acl_entry_outbound, expected_type=type_hints["private_subnet3_b_network_acl_entry_outbound"])
            check_type(argname="argument private_subnet3_b_route", value=private_subnet3_b_route, expected_type=type_hints["private_subnet3_b_route"])
            check_type(argname="argument private_subnet3_b_route_table", value=private_subnet3_b_route_table, expected_type=type_hints["private_subnet3_b_route_table"])
            check_type(argname="argument private_subnet3_b_route_table_association", value=private_subnet3_b_route_table_association, expected_type=type_hints["private_subnet3_b_route_table_association"])
            check_type(argname="argument private_subnet4_a", value=private_subnet4_a, expected_type=type_hints["private_subnet4_a"])
            check_type(argname="argument private_subnet4_a_route", value=private_subnet4_a_route, expected_type=type_hints["private_subnet4_a_route"])
            check_type(argname="argument private_subnet4_a_route_table", value=private_subnet4_a_route_table, expected_type=type_hints["private_subnet4_a_route_table"])
            check_type(argname="argument private_subnet4_a_route_table_association", value=private_subnet4_a_route_table_association, expected_type=type_hints["private_subnet4_a_route_table_association"])
            check_type(argname="argument private_subnet4_b", value=private_subnet4_b, expected_type=type_hints["private_subnet4_b"])
            check_type(argname="argument private_subnet4_b_network_acl", value=private_subnet4_b_network_acl, expected_type=type_hints["private_subnet4_b_network_acl"])
            check_type(argname="argument private_subnet4_b_network_acl_association", value=private_subnet4_b_network_acl_association, expected_type=type_hints["private_subnet4_b_network_acl_association"])
            check_type(argname="argument private_subnet4_b_network_acl_entry_inbound", value=private_subnet4_b_network_acl_entry_inbound, expected_type=type_hints["private_subnet4_b_network_acl_entry_inbound"])
            check_type(argname="argument private_subnet4_b_network_acl_entry_outbound", value=private_subnet4_b_network_acl_entry_outbound, expected_type=type_hints["private_subnet4_b_network_acl_entry_outbound"])
            check_type(argname="argument private_subnet4_b_route", value=private_subnet4_b_route, expected_type=type_hints["private_subnet4_b_route"])
            check_type(argname="argument private_subnet4_b_route_table", value=private_subnet4_b_route_table, expected_type=type_hints["private_subnet4_b_route_table"])
            check_type(argname="argument private_subnet4_b_route_table_association", value=private_subnet4_b_route_table_association, expected_type=type_hints["private_subnet4_b_route_table_association"])
            check_type(argname="argument public_subnet1", value=public_subnet1, expected_type=type_hints["public_subnet1"])
            check_type(argname="argument public_subnet1_route_table_association", value=public_subnet1_route_table_association, expected_type=type_hints["public_subnet1_route_table_association"])
            check_type(argname="argument public_subnet2", value=public_subnet2, expected_type=type_hints["public_subnet2"])
            check_type(argname="argument public_subnet2_route_table_association", value=public_subnet2_route_table_association, expected_type=type_hints["public_subnet2_route_table_association"])
            check_type(argname="argument public_subnet3", value=public_subnet3, expected_type=type_hints["public_subnet3"])
            check_type(argname="argument public_subnet3_route_table_association", value=public_subnet3_route_table_association, expected_type=type_hints["public_subnet3_route_table_association"])
            check_type(argname="argument public_subnet4", value=public_subnet4, expected_type=type_hints["public_subnet4"])
            check_type(argname="argument public_subnet4_route_table_association", value=public_subnet4_route_table_association, expected_type=type_hints["public_subnet4_route_table_association"])
            check_type(argname="argument public_subnet_route", value=public_subnet_route, expected_type=type_hints["public_subnet_route"])
            check_type(argname="argument public_subnet_route_table", value=public_subnet_route_table, expected_type=type_hints["public_subnet_route_table"])
            check_type(argname="argument s3_vpc_endpoint", value=s3_vpc_endpoint, expected_type=type_hints["s3_vpc_endpoint"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpcdhcp_options_association", value=vpcdhcp_options_association, expected_type=type_hints["vpcdhcp_options_association"])
            check_type(argname="argument vpc_flow_logs_log_group", value=vpc_flow_logs_log_group, expected_type=type_hints["vpc_flow_logs_log_group"])
            check_type(argname="argument vpc_flow_logs_role", value=vpc_flow_logs_role, expected_type=type_hints["vpc_flow_logs_role"])
            check_type(argname="argument vpc_flow_logs_to_cloud_watch", value=vpc_flow_logs_to_cloud_watch, expected_type=type_hints["vpc_flow_logs_to_cloud_watch"])
            check_type(argname="argument vpc_gateway_attachment", value=vpc_gateway_attachment, expected_type=type_hints["vpc_gateway_attachment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dhcp_options is not None:
            self._values["dhcp_options"] = dhcp_options
        if internet_gateway is not None:
            self._values["internet_gateway"] = internet_gateway
        if nat1_eip is not None:
            self._values["nat1_eip"] = nat1_eip
        if nat2_eip is not None:
            self._values["nat2_eip"] = nat2_eip
        if nat3_eip is not None:
            self._values["nat3_eip"] = nat3_eip
        if nat4_eip is not None:
            self._values["nat4_eip"] = nat4_eip
        if nat_gateway1 is not None:
            self._values["nat_gateway1"] = nat_gateway1
        if nat_gateway2 is not None:
            self._values["nat_gateway2"] = nat_gateway2
        if nat_gateway3 is not None:
            self._values["nat_gateway3"] = nat_gateway3
        if nat_gateway4 is not None:
            self._values["nat_gateway4"] = nat_gateway4
        if private_subnet1_a is not None:
            self._values["private_subnet1_a"] = private_subnet1_a
        if private_subnet1_a_route is not None:
            self._values["private_subnet1_a_route"] = private_subnet1_a_route
        if private_subnet1_a_route_table is not None:
            self._values["private_subnet1_a_route_table"] = private_subnet1_a_route_table
        if private_subnet1_a_route_table_association is not None:
            self._values["private_subnet1_a_route_table_association"] = private_subnet1_a_route_table_association
        if private_subnet1_b is not None:
            self._values["private_subnet1_b"] = private_subnet1_b
        if private_subnet1_b_network_acl is not None:
            self._values["private_subnet1_b_network_acl"] = private_subnet1_b_network_acl
        if private_subnet1_b_network_acl_association is not None:
            self._values["private_subnet1_b_network_acl_association"] = private_subnet1_b_network_acl_association
        if private_subnet1_b_network_acl_entry_inbound is not None:
            self._values["private_subnet1_b_network_acl_entry_inbound"] = private_subnet1_b_network_acl_entry_inbound
        if private_subnet1_b_network_acl_entry_outbound is not None:
            self._values["private_subnet1_b_network_acl_entry_outbound"] = private_subnet1_b_network_acl_entry_outbound
        if private_subnet1_b_route is not None:
            self._values["private_subnet1_b_route"] = private_subnet1_b_route
        if private_subnet1_b_route_table is not None:
            self._values["private_subnet1_b_route_table"] = private_subnet1_b_route_table
        if private_subnet1_b_route_table_association is not None:
            self._values["private_subnet1_b_route_table_association"] = private_subnet1_b_route_table_association
        if private_subnet2_a is not None:
            self._values["private_subnet2_a"] = private_subnet2_a
        if private_subnet2_a_route is not None:
            self._values["private_subnet2_a_route"] = private_subnet2_a_route
        if private_subnet2_a_route_table is not None:
            self._values["private_subnet2_a_route_table"] = private_subnet2_a_route_table
        if private_subnet2_a_route_table_association is not None:
            self._values["private_subnet2_a_route_table_association"] = private_subnet2_a_route_table_association
        if private_subnet2_b is not None:
            self._values["private_subnet2_b"] = private_subnet2_b
        if private_subnet2_b_network_acl is not None:
            self._values["private_subnet2_b_network_acl"] = private_subnet2_b_network_acl
        if private_subnet2_b_network_acl_association is not None:
            self._values["private_subnet2_b_network_acl_association"] = private_subnet2_b_network_acl_association
        if private_subnet2_b_network_acl_entry_inbound is not None:
            self._values["private_subnet2_b_network_acl_entry_inbound"] = private_subnet2_b_network_acl_entry_inbound
        if private_subnet2_b_network_acl_entry_outbound is not None:
            self._values["private_subnet2_b_network_acl_entry_outbound"] = private_subnet2_b_network_acl_entry_outbound
        if private_subnet2_b_route is not None:
            self._values["private_subnet2_b_route"] = private_subnet2_b_route
        if private_subnet2_b_route_table is not None:
            self._values["private_subnet2_b_route_table"] = private_subnet2_b_route_table
        if private_subnet2_b_route_table_association is not None:
            self._values["private_subnet2_b_route_table_association"] = private_subnet2_b_route_table_association
        if private_subnet3_a is not None:
            self._values["private_subnet3_a"] = private_subnet3_a
        if private_subnet3_a_route is not None:
            self._values["private_subnet3_a_route"] = private_subnet3_a_route
        if private_subnet3_a_route_table is not None:
            self._values["private_subnet3_a_route_table"] = private_subnet3_a_route_table
        if private_subnet3_a_route_table_association is not None:
            self._values["private_subnet3_a_route_table_association"] = private_subnet3_a_route_table_association
        if private_subnet3_b is not None:
            self._values["private_subnet3_b"] = private_subnet3_b
        if private_subnet3_b_network_acl is not None:
            self._values["private_subnet3_b_network_acl"] = private_subnet3_b_network_acl
        if private_subnet3_b_network_acl_association is not None:
            self._values["private_subnet3_b_network_acl_association"] = private_subnet3_b_network_acl_association
        if private_subnet3_b_network_acl_entry_inbound is not None:
            self._values["private_subnet3_b_network_acl_entry_inbound"] = private_subnet3_b_network_acl_entry_inbound
        if private_subnet3_b_network_acl_entry_outbound is not None:
            self._values["private_subnet3_b_network_acl_entry_outbound"] = private_subnet3_b_network_acl_entry_outbound
        if private_subnet3_b_route is not None:
            self._values["private_subnet3_b_route"] = private_subnet3_b_route
        if private_subnet3_b_route_table is not None:
            self._values["private_subnet3_b_route_table"] = private_subnet3_b_route_table
        if private_subnet3_b_route_table_association is not None:
            self._values["private_subnet3_b_route_table_association"] = private_subnet3_b_route_table_association
        if private_subnet4_a is not None:
            self._values["private_subnet4_a"] = private_subnet4_a
        if private_subnet4_a_route is not None:
            self._values["private_subnet4_a_route"] = private_subnet4_a_route
        if private_subnet4_a_route_table is not None:
            self._values["private_subnet4_a_route_table"] = private_subnet4_a_route_table
        if private_subnet4_a_route_table_association is not None:
            self._values["private_subnet4_a_route_table_association"] = private_subnet4_a_route_table_association
        if private_subnet4_b is not None:
            self._values["private_subnet4_b"] = private_subnet4_b
        if private_subnet4_b_network_acl is not None:
            self._values["private_subnet4_b_network_acl"] = private_subnet4_b_network_acl
        if private_subnet4_b_network_acl_association is not None:
            self._values["private_subnet4_b_network_acl_association"] = private_subnet4_b_network_acl_association
        if private_subnet4_b_network_acl_entry_inbound is not None:
            self._values["private_subnet4_b_network_acl_entry_inbound"] = private_subnet4_b_network_acl_entry_inbound
        if private_subnet4_b_network_acl_entry_outbound is not None:
            self._values["private_subnet4_b_network_acl_entry_outbound"] = private_subnet4_b_network_acl_entry_outbound
        if private_subnet4_b_route is not None:
            self._values["private_subnet4_b_route"] = private_subnet4_b_route
        if private_subnet4_b_route_table is not None:
            self._values["private_subnet4_b_route_table"] = private_subnet4_b_route_table
        if private_subnet4_b_route_table_association is not None:
            self._values["private_subnet4_b_route_table_association"] = private_subnet4_b_route_table_association
        if public_subnet1 is not None:
            self._values["public_subnet1"] = public_subnet1
        if public_subnet1_route_table_association is not None:
            self._values["public_subnet1_route_table_association"] = public_subnet1_route_table_association
        if public_subnet2 is not None:
            self._values["public_subnet2"] = public_subnet2
        if public_subnet2_route_table_association is not None:
            self._values["public_subnet2_route_table_association"] = public_subnet2_route_table_association
        if public_subnet3 is not None:
            self._values["public_subnet3"] = public_subnet3
        if public_subnet3_route_table_association is not None:
            self._values["public_subnet3_route_table_association"] = public_subnet3_route_table_association
        if public_subnet4 is not None:
            self._values["public_subnet4"] = public_subnet4
        if public_subnet4_route_table_association is not None:
            self._values["public_subnet4_route_table_association"] = public_subnet4_route_table_association
        if public_subnet_route is not None:
            self._values["public_subnet_route"] = public_subnet_route
        if public_subnet_route_table is not None:
            self._values["public_subnet_route_table"] = public_subnet_route_table
        if s3_vpc_endpoint is not None:
            self._values["s3_vpc_endpoint"] = s3_vpc_endpoint
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpcdhcp_options_association is not None:
            self._values["vpcdhcp_options_association"] = vpcdhcp_options_association
        if vpc_flow_logs_log_group is not None:
            self._values["vpc_flow_logs_log_group"] = vpc_flow_logs_log_group
        if vpc_flow_logs_role is not None:
            self._values["vpc_flow_logs_role"] = vpc_flow_logs_role
        if vpc_flow_logs_to_cloud_watch is not None:
            self._values["vpc_flow_logs_to_cloud_watch"] = vpc_flow_logs_to_cloud_watch
        if vpc_gateway_attachment is not None:
            self._values["vpc_gateway_attachment"] = vpc_gateway_attachment

    @builtins.property
    def dhcp_options(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesDhcpOptions"]:
        '''
        :schema: CfnVpcqsModulePropsResources#DHCPOptions
        '''
        result = self._values.get("dhcp_options")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesDhcpOptions"], result)

    @builtins.property
    def internet_gateway(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesInternetGateway"]:
        '''
        :schema: CfnVpcqsModulePropsResources#InternetGateway
        '''
        result = self._values.get("internet_gateway")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesInternetGateway"], result)

    @builtins.property
    def nat1_eip(self) -> typing.Optional["CfnVpcqsModulePropsResourcesNat1Eip"]:
        '''
        :schema: CfnVpcqsModulePropsResources#NAT1EIP
        '''
        result = self._values.get("nat1_eip")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesNat1Eip"], result)

    @builtins.property
    def nat2_eip(self) -> typing.Optional["CfnVpcqsModulePropsResourcesNat2Eip"]:
        '''
        :schema: CfnVpcqsModulePropsResources#NAT2EIP
        '''
        result = self._values.get("nat2_eip")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesNat2Eip"], result)

    @builtins.property
    def nat3_eip(self) -> typing.Optional["CfnVpcqsModulePropsResourcesNat3Eip"]:
        '''
        :schema: CfnVpcqsModulePropsResources#NAT3EIP
        '''
        result = self._values.get("nat3_eip")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesNat3Eip"], result)

    @builtins.property
    def nat4_eip(self) -> typing.Optional["CfnVpcqsModulePropsResourcesNat4Eip"]:
        '''
        :schema: CfnVpcqsModulePropsResources#NAT4EIP
        '''
        result = self._values.get("nat4_eip")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesNat4Eip"], result)

    @builtins.property
    def nat_gateway1(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesNatGateway1"]:
        '''
        :schema: CfnVpcqsModulePropsResources#NATGateway1
        '''
        result = self._values.get("nat_gateway1")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesNatGateway1"], result)

    @builtins.property
    def nat_gateway2(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesNatGateway2"]:
        '''
        :schema: CfnVpcqsModulePropsResources#NATGateway2
        '''
        result = self._values.get("nat_gateway2")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesNatGateway2"], result)

    @builtins.property
    def nat_gateway3(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesNatGateway3"]:
        '''
        :schema: CfnVpcqsModulePropsResources#NATGateway3
        '''
        result = self._values.get("nat_gateway3")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesNatGateway3"], result)

    @builtins.property
    def nat_gateway4(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesNatGateway4"]:
        '''
        :schema: CfnVpcqsModulePropsResources#NATGateway4
        '''
        result = self._values.get("nat_gateway4")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesNatGateway4"], result)

    @builtins.property
    def private_subnet1_a(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1A"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1A
        '''
        result = self._values.get("private_subnet1_a")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1A"], result)

    @builtins.property
    def private_subnet1_a_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1ARoute
        '''
        result = self._values.get("private_subnet1_a_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute"], result)

    @builtins.property
    def private_subnet1_a_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1ARouteTable
        '''
        result = self._values.get("private_subnet1_a_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable"], result)

    @builtins.property
    def private_subnet1_a_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1ARouteTableAssociation
        '''
        result = self._values.get("private_subnet1_a_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation"], result)

    @builtins.property
    def private_subnet1_b(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1B"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1B
        '''
        result = self._values.get("private_subnet1_b")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1B"], result)

    @builtins.property
    def private_subnet1_b_network_acl(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1BNetworkAcl
        '''
        result = self._values.get("private_subnet1_b_network_acl")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl"], result)

    @builtins.property
    def private_subnet1_b_network_acl_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1BNetworkAclAssociation
        '''
        result = self._values.get("private_subnet1_b_network_acl_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation"], result)

    @builtins.property
    def private_subnet1_b_network_acl_entry_inbound(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1BNetworkAclEntryInbound
        '''
        result = self._values.get("private_subnet1_b_network_acl_entry_inbound")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound"], result)

    @builtins.property
    def private_subnet1_b_network_acl_entry_outbound(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1BNetworkAclEntryOutbound
        '''
        result = self._values.get("private_subnet1_b_network_acl_entry_outbound")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound"], result)

    @builtins.property
    def private_subnet1_b_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1BRoute
        '''
        result = self._values.get("private_subnet1_b_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute"], result)

    @builtins.property
    def private_subnet1_b_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1BRouteTable
        '''
        result = self._values.get("private_subnet1_b_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable"], result)

    @builtins.property
    def private_subnet1_b_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet1BRouteTableAssociation
        '''
        result = self._values.get("private_subnet1_b_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation"], result)

    @builtins.property
    def private_subnet2_a(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2A"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2A
        '''
        result = self._values.get("private_subnet2_a")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2A"], result)

    @builtins.property
    def private_subnet2_a_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2ARoute
        '''
        result = self._values.get("private_subnet2_a_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute"], result)

    @builtins.property
    def private_subnet2_a_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2ARouteTable
        '''
        result = self._values.get("private_subnet2_a_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable"], result)

    @builtins.property
    def private_subnet2_a_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2ARouteTableAssociation
        '''
        result = self._values.get("private_subnet2_a_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation"], result)

    @builtins.property
    def private_subnet2_b(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2B"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2B
        '''
        result = self._values.get("private_subnet2_b")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2B"], result)

    @builtins.property
    def private_subnet2_b_network_acl(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2BNetworkAcl
        '''
        result = self._values.get("private_subnet2_b_network_acl")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl"], result)

    @builtins.property
    def private_subnet2_b_network_acl_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2BNetworkAclAssociation
        '''
        result = self._values.get("private_subnet2_b_network_acl_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation"], result)

    @builtins.property
    def private_subnet2_b_network_acl_entry_inbound(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2BNetworkAclEntryInbound
        '''
        result = self._values.get("private_subnet2_b_network_acl_entry_inbound")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound"], result)

    @builtins.property
    def private_subnet2_b_network_acl_entry_outbound(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2BNetworkAclEntryOutbound
        '''
        result = self._values.get("private_subnet2_b_network_acl_entry_outbound")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound"], result)

    @builtins.property
    def private_subnet2_b_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2BRoute
        '''
        result = self._values.get("private_subnet2_b_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute"], result)

    @builtins.property
    def private_subnet2_b_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2BRouteTable
        '''
        result = self._values.get("private_subnet2_b_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable"], result)

    @builtins.property
    def private_subnet2_b_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet2BRouteTableAssociation
        '''
        result = self._values.get("private_subnet2_b_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation"], result)

    @builtins.property
    def private_subnet3_a(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3A"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3A
        '''
        result = self._values.get("private_subnet3_a")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3A"], result)

    @builtins.property
    def private_subnet3_a_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3ARoute
        '''
        result = self._values.get("private_subnet3_a_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute"], result)

    @builtins.property
    def private_subnet3_a_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3ARouteTable
        '''
        result = self._values.get("private_subnet3_a_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable"], result)

    @builtins.property
    def private_subnet3_a_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3ARouteTableAssociation
        '''
        result = self._values.get("private_subnet3_a_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation"], result)

    @builtins.property
    def private_subnet3_b(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3B"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3B
        '''
        result = self._values.get("private_subnet3_b")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3B"], result)

    @builtins.property
    def private_subnet3_b_network_acl(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3BNetworkAcl
        '''
        result = self._values.get("private_subnet3_b_network_acl")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl"], result)

    @builtins.property
    def private_subnet3_b_network_acl_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3BNetworkAclAssociation
        '''
        result = self._values.get("private_subnet3_b_network_acl_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation"], result)

    @builtins.property
    def private_subnet3_b_network_acl_entry_inbound(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3BNetworkAclEntryInbound
        '''
        result = self._values.get("private_subnet3_b_network_acl_entry_inbound")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound"], result)

    @builtins.property
    def private_subnet3_b_network_acl_entry_outbound(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3BNetworkAclEntryOutbound
        '''
        result = self._values.get("private_subnet3_b_network_acl_entry_outbound")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound"], result)

    @builtins.property
    def private_subnet3_b_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3BRoute
        '''
        result = self._values.get("private_subnet3_b_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute"], result)

    @builtins.property
    def private_subnet3_b_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3BRouteTable
        '''
        result = self._values.get("private_subnet3_b_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable"], result)

    @builtins.property
    def private_subnet3_b_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet3BRouteTableAssociation
        '''
        result = self._values.get("private_subnet3_b_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation"], result)

    @builtins.property
    def private_subnet4_a(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4A"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4A
        '''
        result = self._values.get("private_subnet4_a")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4A"], result)

    @builtins.property
    def private_subnet4_a_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4ARoute
        '''
        result = self._values.get("private_subnet4_a_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute"], result)

    @builtins.property
    def private_subnet4_a_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4ARouteTable
        '''
        result = self._values.get("private_subnet4_a_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable"], result)

    @builtins.property
    def private_subnet4_a_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4ARouteTableAssociation
        '''
        result = self._values.get("private_subnet4_a_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation"], result)

    @builtins.property
    def private_subnet4_b(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4B"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4B
        '''
        result = self._values.get("private_subnet4_b")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4B"], result)

    @builtins.property
    def private_subnet4_b_network_acl(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4BNetworkAcl
        '''
        result = self._values.get("private_subnet4_b_network_acl")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl"], result)

    @builtins.property
    def private_subnet4_b_network_acl_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4BNetworkAclAssociation
        '''
        result = self._values.get("private_subnet4_b_network_acl_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation"], result)

    @builtins.property
    def private_subnet4_b_network_acl_entry_inbound(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4BNetworkAclEntryInbound
        '''
        result = self._values.get("private_subnet4_b_network_acl_entry_inbound")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound"], result)

    @builtins.property
    def private_subnet4_b_network_acl_entry_outbound(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4BNetworkAclEntryOutbound
        '''
        result = self._values.get("private_subnet4_b_network_acl_entry_outbound")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound"], result)

    @builtins.property
    def private_subnet4_b_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4BRoute
        '''
        result = self._values.get("private_subnet4_b_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute"], result)

    @builtins.property
    def private_subnet4_b_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4BRouteTable
        '''
        result = self._values.get("private_subnet4_b_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable"], result)

    @builtins.property
    def private_subnet4_b_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PrivateSubnet4BRouteTableAssociation
        '''
        result = self._values.get("private_subnet4_b_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation"], result)

    @builtins.property
    def public_subnet1(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet1"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnet1
        '''
        result = self._values.get("public_subnet1")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet1"], result)

    @builtins.property
    def public_subnet1_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnet1RouteTableAssociation
        '''
        result = self._values.get("public_subnet1_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation"], result)

    @builtins.property
    def public_subnet2(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet2"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnet2
        '''
        result = self._values.get("public_subnet2")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet2"], result)

    @builtins.property
    def public_subnet2_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnet2RouteTableAssociation
        '''
        result = self._values.get("public_subnet2_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation"], result)

    @builtins.property
    def public_subnet3(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet3"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnet3
        '''
        result = self._values.get("public_subnet3")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet3"], result)

    @builtins.property
    def public_subnet3_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnet3RouteTableAssociation
        '''
        result = self._values.get("public_subnet3_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation"], result)

    @builtins.property
    def public_subnet4(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet4"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnet4
        '''
        result = self._values.get("public_subnet4")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet4"], result)

    @builtins.property
    def public_subnet4_route_table_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnet4RouteTableAssociation
        '''
        result = self._values.get("public_subnet4_route_table_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation"], result)

    @builtins.property
    def public_subnet_route(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnetRoute"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnetRoute
        '''
        result = self._values.get("public_subnet_route")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnetRoute"], result)

    @builtins.property
    def public_subnet_route_table(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnetRouteTable"]:
        '''
        :schema: CfnVpcqsModulePropsResources#PublicSubnetRouteTable
        '''
        result = self._values.get("public_subnet_route_table")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesPublicSubnetRouteTable"], result)

    @builtins.property
    def s3_vpc_endpoint(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesS3VpcEndpoint"]:
        '''
        :schema: CfnVpcqsModulePropsResources#S3VPCEndpoint
        '''
        result = self._values.get("s3_vpc_endpoint")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesS3VpcEndpoint"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CfnVpcqsModulePropsResourcesVpc"]:
        '''
        :schema: CfnVpcqsModulePropsResources#VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesVpc"], result)

    @builtins.property
    def vpcdhcp_options_association(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation"]:
        '''
        :schema: CfnVpcqsModulePropsResources#VPCDHCPOptionsAssociation
        '''
        result = self._values.get("vpcdhcp_options_association")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation"], result)

    @builtins.property
    def vpc_flow_logs_log_group(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup"]:
        '''
        :schema: CfnVpcqsModulePropsResources#VPCFlowLogsLogGroup
        '''
        result = self._values.get("vpc_flow_logs_log_group")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup"], result)

    @builtins.property
    def vpc_flow_logs_role(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesVpcFlowLogsRole"]:
        '''
        :schema: CfnVpcqsModulePropsResources#VPCFlowLogsRole
        '''
        result = self._values.get("vpc_flow_logs_role")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesVpcFlowLogsRole"], result)

    @builtins.property
    def vpc_flow_logs_to_cloud_watch(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch"]:
        '''
        :schema: CfnVpcqsModulePropsResources#VPCFlowLogsToCloudWatch
        '''
        result = self._values.get("vpc_flow_logs_to_cloud_watch")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch"], result)

    @builtins.property
    def vpc_gateway_attachment(
        self,
    ) -> typing.Optional["CfnVpcqsModulePropsResourcesVpcGatewayAttachment"]:
        '''
        :schema: CfnVpcqsModulePropsResources#VPCGatewayAttachment
        '''
        result = self._values.get("vpc_gateway_attachment")
        return typing.cast(typing.Optional["CfnVpcqsModulePropsResourcesVpcGatewayAttachment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesDhcpOptions",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesDhcpOptions:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesDhcpOptions
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d88d41da485a42116c06df99aa7f632625bf7ce1b91d2a1b53face018d548062)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesDhcpOptions#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesDhcpOptions#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesDhcpOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesInternetGateway",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesInternetGateway:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesInternetGateway
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5409f848b38209f7b51ddc47a1439997ced5ca7e5b9ac0bb0d94fbbfc57859ae)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesInternetGateway#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesInternetGateway#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesInternetGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesNat1Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesNat1Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesNat1Eip
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1e77950025280b6f44d5fdf7bc3c60b9aec76ba369a04e3707eb1eb88c61da7)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesNat1Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesNat1Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesNat1Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesNat2Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesNat2Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesNat2Eip
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a53dcc33eb4048f6c7c8bb70b0789a499bcd6269830b6ddc40859229f861e60)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesNat2Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesNat2Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesNat2Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesNat3Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesNat3Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesNat3Eip
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50dd5f3b82351afd89929a9aa844658a72389067ff05da404d0b621bebc6517c)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesNat3Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesNat3Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesNat3Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesNat4Eip",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesNat4Eip:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesNat4Eip
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab7037985985c8963826c1a6e122678c365221c92a3e256470de07e7d435ef4e)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesNat4Eip#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesNat4Eip#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesNat4Eip(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesNatGateway1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesNatGateway1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesNatGateway1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57ce35b24ea54dfd8263a54152689d38fc72ca09406140073de3250f01c9d159)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesNatGateway1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesNatGateway1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesNatGateway1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesNatGateway2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesNatGateway2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesNatGateway2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__705962d56d068cdacfb6a5a2f27e93eee6625f1cdcd24b5532f400408cde8d59)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesNatGateway2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesNatGateway2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesNatGateway2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesNatGateway3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesNatGateway3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesNatGateway3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77c49e0b3b3f027e0268b880d2eaf8548412537f6fa4651a172813841ca8b25)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesNatGateway3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesNatGateway3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesNatGateway3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesNatGateway4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesNatGateway4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesNatGateway4
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c49d5e04f3eae74374ad37bb11f7939e55c6dc2655d3a079d5386bbd1e9a4a20)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesNatGateway4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesNatGateway4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesNatGateway4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1A
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f57f08fd9795ad7942bed4231e290bb0b2d79fadbed5a17a3f39939958ddddf)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbbc2ecaf7d22133de11804f87e85b8a2bc56b9490a4919cd50d5c561b9484a3)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3fbbd04460c9c8ee9e3ea0242f085f7bddb81821c3a5a6e74fdcd8b6d0c42ea)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7592252706ac737a3983ffc2f4793beb706f091ad4a0e18ba1aed55298fbe57)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1B",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1B:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1B
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324d88254b7b8a01f16f1136b8c20f7fb2981712fcfe71cd1a3f5cdae345e8c4)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1B#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1B#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1B(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a69c6cecba04f62b6322b5c5c2feed6583bf3dbc3b0548a2cc4a76a0f8899059)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97c123836a2e443bef3cfbe2c7075d78b2d1c7e93ebad7bc685bae99bbfdbd03)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b51993558939e14aa6cadb306bba08624cbde67be1f3da740616fa607aab961c)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41c9478401467e194c93680798ec8bcfc949653b40d7846523269cb1fa36f2e5)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13656d22226544d772c89a67e9b29131a5e607ca087bebe8ae09fe00c13f07ed)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a6e11bc8e4f5e2e3ab0326d482b42a40b87ec57949e3481db96b17a99720732)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e96bcceafdfe4b95d0e1338f35556170f09af71417e185e9fe28a248b1aa8ffb)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2A
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53fb809ec729a2accd4b2b112dd90953a8c9f8a94db8ad57072bbf66585969e7)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80eb84b4e9207de1582ce0da421282194e6ddb6820bae40418bab9667b57cb09)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f39daa2e6391004e1d2b0123ecb12676ef4ea8916bd9ab5526365f8d738712)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ad8fd441114ed8ac3b6d616180ea8897eff10a634609a51dbc4c3d8e7be386c)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2B",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2B:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2B
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34294df860fba3546087c3247801e267ee7e11d6ba6337fb08a7975a74dcee7)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2B#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2B#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2B(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdc025ba5c9ef20e82356ed06e1866d2ccca1d076737569421e9649d8a6e7944)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bec56366565e84e3074860cc6db120695eb407a094891fa2716b8a234283476)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47330d568d719b5230b620f3e4e7ae168cb13cfbabace741aaeb2990e3323b05)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43f38e993ff731e0b72ec48f970b99b2f3b14b4a1a3140a2e072de21590d311b)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab1e8921a32a1429504a81b041e8d150e1e7080ca8c2458e0f05b0b964a45849)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f584cfb359e6c5aa3192a1c201b5581b3d6222601f1e276a18878368dba916)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea51049bbbbe9e3a13710a47292796d26a5460ed4514e34bce2dbe672b6eed83)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3A
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8f85a21021d7111e6bf94d1f8be1eed28070946ad5ed911d6af604f451dd3f7)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10acd7f7a647ceaaf3acf02e84728a9fb83ccc6d02ceda0edfd172d1d6ea53bc)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8b2543debdece7efaf0953bfb43ea17001bf85c0d394f6f7c88ba0eeb7a4329)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a836cda74929dd09577fd492478f415049d947fcbd48a4c8d2a6b9bfab1d985e)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3B",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3B:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3B
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2026490ff53b5ea05ca63113f2c4b5dc8f0d10e8fc159b30ea23521ddf44132c)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3B#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3B#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3B(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e1d864dc7528a9b4bc367b6e96297c9d8a71d3c2335a5b8b9339e269b070805)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb088af92649c7da0d8f5fff2f5bbaa9f8e472be32f29dafe8065fb4a0b6f72)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7011c73d5ee019cba42b71566f5bd9a45ac30d34cd2bc907b93696313e272dbd)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e314120ce84adfce677d069b2059c3a2b09ea8990f09218414f44b9e27f47e9c)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0eb6bd8d19aea91bac0adca1fc7cb0e388e9eaa06c56c5c124cfcbcf6614ab2)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0c3991b8242e824ae4808a2bf22a97d1271c88df9a4f76d243fa4ba0f3500d4)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5c00a74f8d86349567a8bcd4ac3c8fdff9821a884235295acf1a22488e27013)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4A",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4A:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4A
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15a24e7da9bbd42555c085216f568ff99bcd2d32cdd8337a87dd76193af1fdf3)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4A#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4A#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4A(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02dbcaa15d82eca8af543564d1e2b161f53b2c09b489822debfaba83506464d4)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6dc6884c19cda93da2233c2f2e68358518128ac35b290b996dc12e441725b3)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92cb2882a38aa1bc4fa1da78ed1fdb0aaf561c07dc423b46ba60dcc1382c7631)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4B",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4B:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4B
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54d7ea93d56783eb09e9962c9bd30085e02b1a51c7722439c743e2de4e419643)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4B#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4B#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4B(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__934fb8b87ed2b336599e59c0373055f6cb27dad972114dd16f5815694041fb36)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76eb74d13f9de3f47f8e58c2f25ee7e4f02926006ac69b736f6beb0c3c4fadd)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999fb0192f7f5a494460158d516647182407f3fc12dff4166eec919d71e36990)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55501d90c1605f13c7af616bebfe243a3a7edcd5ab5262abda92672e1c092a45)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c1934d0cb1228844f56480ba2ba7564b8711a9a97945e3a4431f95775aa0976)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9646e20ad3cab6e19a66e666a70fb38c1c86d55b67a0d752882b74fcb8e1a5cc)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ced312a85f5516c19c55f343df750dfb489ab6dbcb998130c79f34d2ee31e663)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnet1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnet1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnet1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c7df6cb04e63b0b07fb2659592a9322ceb99cd8146a5b758baef24b1e9a4f0b)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnet1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7765e8f635813ba84c7fa0b5317933079f0e85f66c572ede6c0bed61c6ad2a25)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnet2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnet2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnet2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed4c91b942c36a5bc5b47e128ad0455399cdd9ddb81865e39a37e194d8a796a5)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnet2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd7b78260493357acfab390adc9dd9a43eeccf7c187fd6818229301e9980eece)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnet3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnet3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnet3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092799ed490f6d71867cd653e712517e73ff23431bc9667bda00427da87d5527)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnet3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17da3bfcd568fa6e296171906455bafd11141ea268914bc4519e24c3caf8647)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnet4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnet4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnet4
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0bca9f5ce4c74ed36f35ad2f672a8660592a6c3bad1b23cb2e17f8cbdc938c4)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnet4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37b216f96f21e22e66060e741c25af0d46ac0a6342fbdd8a204acdb681f84b87)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnetRoute",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnetRoute:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnetRoute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d5f6f264243d699aa9ea34949e5648f107833fd44dd6ab01565ff326714871a)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnetRoute#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnetRoute#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnetRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesPublicSubnetRouteTable",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesPublicSubnetRouteTable:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesPublicSubnetRouteTable
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b029fe8a946434a2873383e35f1fbd464dd5dabc6c589558c8d75b7f3d1c86d)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnetRouteTable#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesPublicSubnetRouteTable#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesPublicSubnetRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesS3VpcEndpoint",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesS3VpcEndpoint:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesS3VpcEndpoint
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb193a97f7f7d5402f0087310624de012d02a8f6dff5fbe5d080aa518884c388)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesS3VpcEndpoint#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesS3VpcEndpoint#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesS3VpcEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesVpc",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesVpc:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesVpc
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a747271fee3a00087f642f384081b66024c10a5080dfc4d033dd4ce70181f404)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpc#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpc#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9660d3ef4d4c085fdf9ef8aa258529ae4927f0ffb8ee51834740572ebeb6b5a)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesVpcFlowLogsRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesVpcFlowLogsRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d2570a10c54813eda272981657dd0485a2ede943dd9173556ba5e082a81a16)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesVpcFlowLogsRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2539581fc1370c6f52b9037237dbc45e7d7789f54ccf0922b7c8a9aed3cd53d)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesVpcGatewayAttachment",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesVpcGatewayAttachment:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesVpcGatewayAttachment
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a5c8c0766a5105792c2208acefd355195edee7c1567c55d01526fa2684a5fe6)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcGatewayAttachment#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcGatewayAttachment#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesVpcGatewayAttachment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-vpc-vpcqs-module.CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae1b03b2f03caff0bd5eb9b9a6d6e932d645d4765a21e013074be5b9127cc534)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def properties(self) -> typing.Any:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnVpcqsModule",
    "CfnVpcqsModuleProps",
    "CfnVpcqsModulePropsParameters",
    "CfnVpcqsModulePropsParametersAvailabilityZones",
    "CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets",
    "CfnVpcqsModulePropsParametersCreateNatGateways",
    "CfnVpcqsModulePropsParametersCreatePrivateSubnets",
    "CfnVpcqsModulePropsParametersCreatePublicSubnets",
    "CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch",
    "CfnVpcqsModulePropsParametersNumberOfAZs",
    "CfnVpcqsModulePropsParametersPrivateSubnet1Acidr",
    "CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr",
    "CfnVpcqsModulePropsParametersPrivateSubnet2Acidr",
    "CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr",
    "CfnVpcqsModulePropsParametersPrivateSubnet3Acidr",
    "CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr",
    "CfnVpcqsModulePropsParametersPrivateSubnet4Acidr",
    "CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr",
    "CfnVpcqsModulePropsParametersPrivateSubnetATag1",
    "CfnVpcqsModulePropsParametersPrivateSubnetATag2",
    "CfnVpcqsModulePropsParametersPrivateSubnetATag3",
    "CfnVpcqsModulePropsParametersPrivateSubnetBTag1",
    "CfnVpcqsModulePropsParametersPrivateSubnetBTag2",
    "CfnVpcqsModulePropsParametersPrivateSubnetBTag3",
    "CfnVpcqsModulePropsParametersPublicSubnet1Cidr",
    "CfnVpcqsModulePropsParametersPublicSubnet2Cidr",
    "CfnVpcqsModulePropsParametersPublicSubnet3Cidr",
    "CfnVpcqsModulePropsParametersPublicSubnet4Cidr",
    "CfnVpcqsModulePropsParametersPublicSubnetTag1",
    "CfnVpcqsModulePropsParametersPublicSubnetTag2",
    "CfnVpcqsModulePropsParametersPublicSubnetTag3",
    "CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey",
    "CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat",
    "CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention",
    "CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval",
    "CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType",
    "CfnVpcqsModulePropsParametersVpcTenancy",
    "CfnVpcqsModulePropsParametersVpccidr",
    "CfnVpcqsModulePropsResources",
    "CfnVpcqsModulePropsResourcesDhcpOptions",
    "CfnVpcqsModulePropsResourcesInternetGateway",
    "CfnVpcqsModulePropsResourcesNat1Eip",
    "CfnVpcqsModulePropsResourcesNat2Eip",
    "CfnVpcqsModulePropsResourcesNat3Eip",
    "CfnVpcqsModulePropsResourcesNat4Eip",
    "CfnVpcqsModulePropsResourcesNatGateway1",
    "CfnVpcqsModulePropsResourcesNatGateway2",
    "CfnVpcqsModulePropsResourcesNatGateway3",
    "CfnVpcqsModulePropsResourcesNatGateway4",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1A",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1B",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable",
    "CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2A",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2B",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable",
    "CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3A",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3B",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable",
    "CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4A",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4B",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable",
    "CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPublicSubnet1",
    "CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPublicSubnet2",
    "CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPublicSubnet3",
    "CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPublicSubnet4",
    "CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation",
    "CfnVpcqsModulePropsResourcesPublicSubnetRoute",
    "CfnVpcqsModulePropsResourcesPublicSubnetRouteTable",
    "CfnVpcqsModulePropsResourcesS3VpcEndpoint",
    "CfnVpcqsModulePropsResourcesVpc",
    "CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup",
    "CfnVpcqsModulePropsResourcesVpcFlowLogsRole",
    "CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch",
    "CfnVpcqsModulePropsResourcesVpcGatewayAttachment",
    "CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation",
]

publication.publish()

def _typecheckingstub__1f05101874bba4ad0920312d5b89bfc57cca070aba09083455f2e291d0f1e191(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnVpcqsModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnVpcqsModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ef4b61bbc09d83ec63cf115c24ede713e40463a3339848f93a0212b9cf0b07(
    *,
    parameters: typing.Optional[typing.Union[CfnVpcqsModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnVpcqsModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b24fb7876b2d6f328c3a04afb85864a5e64a1d432057cd8eeee0d71b636ac595(
    *,
    availability_zones: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersAvailabilityZones, typing.Dict[builtins.str, typing.Any]]] = None,
    create_additional_private_subnets: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersCreateAdditionalPrivateSubnets, typing.Dict[builtins.str, typing.Any]]] = None,
    create_nat_gateways: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersCreateNatGateways, typing.Dict[builtins.str, typing.Any]]] = None,
    create_private_subnets: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersCreatePrivateSubnets, typing.Dict[builtins.str, typing.Any]]] = None,
    create_public_subnets: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersCreatePublicSubnets, typing.Dict[builtins.str, typing.Any]]] = None,
    create_vpc_flow_logs_to_cloud_watch: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersCreateVpcFlowLogsToCloudWatch, typing.Dict[builtins.str, typing.Any]]] = None,
    number_of_a_zs: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersNumberOfAZs, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_acidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnet1Acidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_bcidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnet1Bcidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_acidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnet2Acidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_bcidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnet2Bcidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_acidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnet3Acidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_bcidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnet3Bcidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_acidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnet4Acidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_bcidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnet4Bcidr, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet_a_tag1: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnetATag1, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet_a_tag2: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnetATag2, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet_a_tag3: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnetATag3, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet_b_tag1: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnetBTag1, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet_b_tag2: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnetBTag2, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet_b_tag3: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPrivateSubnetBTag3, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1_cidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPublicSubnet1Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2_cidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPublicSubnet2Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet3_cidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPublicSubnet3Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet4_cidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPublicSubnet4Cidr, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet_tag1: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPublicSubnetTag1, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet_tag2: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPublicSubnetTag2, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet_tag3: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersPublicSubnetTag3, typing.Dict[builtins.str, typing.Any]]] = None,
    vpccidr: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersVpccidr, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_flow_logs_cloud_watch_kms_key: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersVpcFlowLogsCloudWatchKmsKey, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_flow_logs_log_format: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersVpcFlowLogsLogFormat, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_flow_logs_log_group_retention: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersVpcFlowLogsLogGroupRetention, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_flow_logs_max_aggregation_interval: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersVpcFlowLogsMaxAggregationInterval, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_flow_logs_traffic_type: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersVpcFlowLogsTrafficType, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_tenancy: typing.Optional[typing.Union[CfnVpcqsModulePropsParametersVpcTenancy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f082b85af10f31a18949321188ee85f9236c9300b5084b359211dcc8ea5b339c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97765f8002b03d68af17bccf49441db59f4cd66a1985d59d677af9e6666727d5(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad85d44a2129bc3149e96f914532c31859ecbf542b860ff60c9df980b7d7229(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc4a57a934049bb1265b77849a8b573984812628d6889cfd45ea21b3d3e89117(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56c95c3cf3af5dc7401b7f5cd65d8196d8293795da7b0010a03683560acc4a0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa882eca6624ab6943fc543ae4942e09cf7b94c964af02ef779546df2f1c635(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa3fdc936049706a5c5e2333cd269b4efbaf701170b9296bb4bc7db4e577bcc6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18e0bee1aec3bbdb5989349bcb7ec4a0bba23d154e9096c5dd30b39b5ce88a25(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b40018af05c15b850b79c56750e2b97f9e7b7f3be84075d480bf24079bfecc0d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9255afbe163f1abedd5b3ef0cd0bfcb7ce7405785e5830f0ff0fda8bd1d8f61(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c04a7e1692e0259ec0b58f752e3d08fdace8798f3ee696b7c827faf23adcfc6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b63166c5420d97215472df8755b1bb4d05b139d29c7a5d01ee2e7238c898757(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec24b47b2d6b2d8050be9b946a866747d6c780a30dde2ea1c58fd2a3a94df19a(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc81a4eec33fbb648f89257e51586d352c99a1248ac8f606b3ac7f1ede17d8b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd5a48a6c37602431b565b655d8c0e554116d4c4b6127206607857547215c56(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41c8e54c4cbb9d904cb03bc766c1561b976902e126fd8f709ce52daba8069ef9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a745cdfddac18d69f34408b13ef49ebdbbee94414a2cfe2d2f97939fc2328bd(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde13280d77abf574778f8a197f71e93c1145409c274de468812291880c86636(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c30ae04531b2c93d633d818c388918c713c7ed0bdc8d3d92dd442e23eb0d1bc(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2604cbed2eab9d83d2d5f736304d8789e7ec00c6eb5aee42c300858f3c05d2a2(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22abb2930df6166815cd76a0b90c397fc7e27225fc4f4cbb707bf371d6808940(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d1cb697dfd4ce654a49876d7a7103464dec037649058f3e314e5ccd995933d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3814651dfd3ba07a9e2af44806e955ccc3a76a7e518db1f4d510ab584c2505c5(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8672a2462068a5289486f8a1546cd7cdd05c1c4c43cd838276cddc0448116256(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414a379960ecd7a2a6b5fc096a4c78212a4f203497014274a6608c28aa59c5aa(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f95e5b7a0c6586178b00642867ef18710e84f6382f2f649f42d88b0f85ca01bf(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0813f711557a854c8796812505683ac6d8b663690b8ec3247d6129042b6a2456(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e1a0b5a5a13185e7c283065e1f755fe73d1ba0a84a5003541b5bb3fd31d28c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5db2ba8a7da950abe46dede641ec4d3f1a1789e9c099d2c461d35e1df0e3d41e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f887b7e120684547a9a6aaf9bf1f7a5cf7fff92d5840a8328b1b174d276783(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c39600e1b80938f22edbb7bade615ed829633938eb9d9ca7c5eb3c6d8a546a17(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__388d244207ffa5383ebb43e50b1d3251ed518bf52e7d0aa027e52da44855b85c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4e777720237b0ee4704c2f21a04c8481d4a2e1d6b54ac935dbaedfc59083fb(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97408e9c24cac272c1c330b3559c95a56796305285d802fea223c2290a33844f(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d727fdf94d6dca09fb6901982df419cb2298afd1cb56d554f1223945ac662b8d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40bc2466d9903edb953edc8386d5d642d73d1bd38baddbdc76590b9b09a4a8d3(
    *,
    dhcp_options: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesDhcpOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    internet_gateway: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesInternetGateway, typing.Dict[builtins.str, typing.Any]]] = None,
    nat1_eip: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesNat1Eip, typing.Dict[builtins.str, typing.Any]]] = None,
    nat2_eip: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesNat2Eip, typing.Dict[builtins.str, typing.Any]]] = None,
    nat3_eip: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesNat3Eip, typing.Dict[builtins.str, typing.Any]]] = None,
    nat4_eip: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesNat4Eip, typing.Dict[builtins.str, typing.Any]]] = None,
    nat_gateway1: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesNatGateway1, typing.Dict[builtins.str, typing.Any]]] = None,
    nat_gateway2: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesNatGateway2, typing.Dict[builtins.str, typing.Any]]] = None,
    nat_gateway3: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesNatGateway3, typing.Dict[builtins.str, typing.Any]]] = None,
    nat_gateway4: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesNatGateway4, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_a: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1A, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_a_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1ARoute, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_a_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_a_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1ARouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_b: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1B, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_b_network_acl: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAcl, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_b_network_acl_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_b_network_acl_entry_inbound: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryInbound, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_b_network_acl_entry_outbound: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1BNetworkAclEntryOutbound, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_b_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1BRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_b_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet1_b_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet1BRouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_a: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2A, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_a_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2ARoute, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_a_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_a_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2ARouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_b: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2B, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_b_network_acl: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAcl, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_b_network_acl_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_b_network_acl_entry_inbound: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryInbound, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_b_network_acl_entry_outbound: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2BNetworkAclEntryOutbound, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_b_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2BRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_b_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet2_b_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet2BRouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_a: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3A, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_a_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3ARoute, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_a_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_a_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3ARouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_b: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3B, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_b_network_acl: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAcl, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_b_network_acl_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_b_network_acl_entry_inbound: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryInbound, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_b_network_acl_entry_outbound: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3BNetworkAclEntryOutbound, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_b_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3BRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_b_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet3_b_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet3BRouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_a: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4A, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_a_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4ARoute, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_a_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_a_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4ARouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_b: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4B, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_b_network_acl: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAcl, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_b_network_acl_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_b_network_acl_entry_inbound: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryInbound, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_b_network_acl_entry_outbound: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4BNetworkAclEntryOutbound, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_b_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4BRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_b_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    private_subnet4_b_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPrivateSubnet4BRouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnet1, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnet1RouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnet2, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnet2RouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet3: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnet3, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet3_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnet3RouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet4: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnet4, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet4_route_table_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnet4RouteTableAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet_route: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnetRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet_route_table: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesPublicSubnetRouteTable, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_vpc_endpoint: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesS3VpcEndpoint, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesVpc, typing.Dict[builtins.str, typing.Any]]] = None,
    vpcdhcp_options_association: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesVpcdhcpOptionsAssociation, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_flow_logs_log_group: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesVpcFlowLogsLogGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_flow_logs_role: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesVpcFlowLogsRole, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_flow_logs_to_cloud_watch: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesVpcFlowLogsToCloudWatch, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_gateway_attachment: typing.Optional[typing.Union[CfnVpcqsModulePropsResourcesVpcGatewayAttachment, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88d41da485a42116c06df99aa7f632625bf7ce1b91d2a1b53face018d548062(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5409f848b38209f7b51ddc47a1439997ced5ca7e5b9ac0bb0d94fbbfc57859ae(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1e77950025280b6f44d5fdf7bc3c60b9aec76ba369a04e3707eb1eb88c61da7(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a53dcc33eb4048f6c7c8bb70b0789a499bcd6269830b6ddc40859229f861e60(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50dd5f3b82351afd89929a9aa844658a72389067ff05da404d0b621bebc6517c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7037985985c8963826c1a6e122678c365221c92a3e256470de07e7d435ef4e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ce35b24ea54dfd8263a54152689d38fc72ca09406140073de3250f01c9d159(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__705962d56d068cdacfb6a5a2f27e93eee6625f1cdcd24b5532f400408cde8d59(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77c49e0b3b3f027e0268b880d2eaf8548412537f6fa4651a172813841ca8b25(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c49d5e04f3eae74374ad37bb11f7939e55c6dc2655d3a079d5386bbd1e9a4a20(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f57f08fd9795ad7942bed4231e290bb0b2d79fadbed5a17a3f39939958ddddf(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbbc2ecaf7d22133de11804f87e85b8a2bc56b9490a4919cd50d5c561b9484a3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3fbbd04460c9c8ee9e3ea0242f085f7bddb81821c3a5a6e74fdcd8b6d0c42ea(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7592252706ac737a3983ffc2f4793beb706f091ad4a0e18ba1aed55298fbe57(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324d88254b7b8a01f16f1136b8c20f7fb2981712fcfe71cd1a3f5cdae345e8c4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a69c6cecba04f62b6322b5c5c2feed6583bf3dbc3b0548a2cc4a76a0f8899059(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c123836a2e443bef3cfbe2c7075d78b2d1c7e93ebad7bc685bae99bbfdbd03(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51993558939e14aa6cadb306bba08624cbde67be1f3da740616fa607aab961c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41c9478401467e194c93680798ec8bcfc949653b40d7846523269cb1fa36f2e5(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13656d22226544d772c89a67e9b29131a5e607ca087bebe8ae09fe00c13f07ed(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a6e11bc8e4f5e2e3ab0326d482b42a40b87ec57949e3481db96b17a99720732(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e96bcceafdfe4b95d0e1338f35556170f09af71417e185e9fe28a248b1aa8ffb(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53fb809ec729a2accd4b2b112dd90953a8c9f8a94db8ad57072bbf66585969e7(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80eb84b4e9207de1582ce0da421282194e6ddb6820bae40418bab9667b57cb09(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f39daa2e6391004e1d2b0123ecb12676ef4ea8916bd9ab5526365f8d738712(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad8fd441114ed8ac3b6d616180ea8897eff10a634609a51dbc4c3d8e7be386c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34294df860fba3546087c3247801e267ee7e11d6ba6337fb08a7975a74dcee7(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdc025ba5c9ef20e82356ed06e1866d2ccca1d076737569421e9649d8a6e7944(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bec56366565e84e3074860cc6db120695eb407a094891fa2716b8a234283476(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47330d568d719b5230b620f3e4e7ae168cb13cfbabace741aaeb2990e3323b05(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43f38e993ff731e0b72ec48f970b99b2f3b14b4a1a3140a2e072de21590d311b(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab1e8921a32a1429504a81b041e8d150e1e7080ca8c2458e0f05b0b964a45849(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f584cfb359e6c5aa3192a1c201b5581b3d6222601f1e276a18878368dba916(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea51049bbbbe9e3a13710a47292796d26a5460ed4514e34bce2dbe672b6eed83(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8f85a21021d7111e6bf94d1f8be1eed28070946ad5ed911d6af604f451dd3f7(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10acd7f7a647ceaaf3acf02e84728a9fb83ccc6d02ceda0edfd172d1d6ea53bc(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8b2543debdece7efaf0953bfb43ea17001bf85c0d394f6f7c88ba0eeb7a4329(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a836cda74929dd09577fd492478f415049d947fcbd48a4c8d2a6b9bfab1d985e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2026490ff53b5ea05ca63113f2c4b5dc8f0d10e8fc159b30ea23521ddf44132c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e1d864dc7528a9b4bc367b6e96297c9d8a71d3c2335a5b8b9339e269b070805(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb088af92649c7da0d8f5fff2f5bbaa9f8e472be32f29dafe8065fb4a0b6f72(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7011c73d5ee019cba42b71566f5bd9a45ac30d34cd2bc907b93696313e272dbd(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e314120ce84adfce677d069b2059c3a2b09ea8990f09218414f44b9e27f47e9c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0eb6bd8d19aea91bac0adca1fc7cb0e388e9eaa06c56c5c124cfcbcf6614ab2(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c3991b8242e824ae4808a2bf22a97d1271c88df9a4f76d243fa4ba0f3500d4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c00a74f8d86349567a8bcd4ac3c8fdff9821a884235295acf1a22488e27013(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a24e7da9bbd42555c085216f568ff99bcd2d32cdd8337a87dd76193af1fdf3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02dbcaa15d82eca8af543564d1e2b161f53b2c09b489822debfaba83506464d4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6dc6884c19cda93da2233c2f2e68358518128ac35b290b996dc12e441725b3(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92cb2882a38aa1bc4fa1da78ed1fdb0aaf561c07dc423b46ba60dcc1382c7631(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54d7ea93d56783eb09e9962c9bd30085e02b1a51c7722439c743e2de4e419643(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__934fb8b87ed2b336599e59c0373055f6cb27dad972114dd16f5815694041fb36(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76eb74d13f9de3f47f8e58c2f25ee7e4f02926006ac69b736f6beb0c3c4fadd(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999fb0192f7f5a494460158d516647182407f3fc12dff4166eec919d71e36990(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55501d90c1605f13c7af616bebfe243a3a7edcd5ab5262abda92672e1c092a45(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c1934d0cb1228844f56480ba2ba7564b8711a9a97945e3a4431f95775aa0976(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9646e20ad3cab6e19a66e666a70fb38c1c86d55b67a0d752882b74fcb8e1a5cc(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ced312a85f5516c19c55f343df750dfb489ab6dbcb998130c79f34d2ee31e663(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c7df6cb04e63b0b07fb2659592a9322ceb99cd8146a5b758baef24b1e9a4f0b(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7765e8f635813ba84c7fa0b5317933079f0e85f66c572ede6c0bed61c6ad2a25(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4c91b942c36a5bc5b47e128ad0455399cdd9ddb81865e39a37e194d8a796a5(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd7b78260493357acfab390adc9dd9a43eeccf7c187fd6818229301e9980eece(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092799ed490f6d71867cd653e712517e73ff23431bc9667bda00427da87d5527(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17da3bfcd568fa6e296171906455bafd11141ea268914bc4519e24c3caf8647(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0bca9f5ce4c74ed36f35ad2f672a8660592a6c3bad1b23cb2e17f8cbdc938c4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b216f96f21e22e66060e741c25af0d46ac0a6342fbdd8a204acdb681f84b87(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d5f6f264243d699aa9ea34949e5648f107833fd44dd6ab01565ff326714871a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b029fe8a946434a2873383e35f1fbd464dd5dabc6c589558c8d75b7f3d1c86d(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb193a97f7f7d5402f0087310624de012d02a8f6dff5fbe5d080aa518884c388(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a747271fee3a00087f642f384081b66024c10a5080dfc4d033dd4ce70181f404(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9660d3ef4d4c085fdf9ef8aa258529ae4927f0ffb8ee51834740572ebeb6b5a(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d2570a10c54813eda272981657dd0485a2ede943dd9173556ba5e082a81a16(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2539581fc1370c6f52b9037237dbc45e7d7789f54ccf0922b7c8a9aed3cd53d(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a5c8c0766a5105792c2208acefd355195edee7c1567c55d01526fa2684a5fe6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae1b03b2f03caff0bd5eb9b9a6d6e932d645d4765a21e013074be5b9127cc534(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
