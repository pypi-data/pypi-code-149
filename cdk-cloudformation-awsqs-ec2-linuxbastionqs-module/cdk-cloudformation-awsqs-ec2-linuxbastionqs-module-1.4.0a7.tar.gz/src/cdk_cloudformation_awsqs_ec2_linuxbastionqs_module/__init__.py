'''
# awsqs-ec2-linuxbastionqs-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `AWSQS::EC2::LinuxBastionQS::MODULE` v1.4.0.

## Description

Schema for Module Fragment of type AWSQS::EC2::LinuxBastionQS::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name AWSQS::EC2::LinuxBastionQS::MODULE \
  --publisher-id 408988dff9e863704bcc72e7e13f8d645cee8311 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-EC2-LinuxBastionQS-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `AWSQS::EC2::LinuxBastionQS::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fawsqs-ec2-linuxbastionqs-module+v1.4.0).
* Issues related to `AWSQS::EC2::LinuxBastionQS::MODULE` should be reported to the [publisher](undefined).

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


class CfnLinuxBastionQsModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModule",
):
    '''A CloudFormation ``AWSQS::EC2::LinuxBastionQS::MODULE``.

    :cloudformationResource: AWSQS::EC2::LinuxBastionQS::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``AWSQS::EC2::LinuxBastionQS::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d587f5f0b1ebd1c7f8619a4a353a8bd5a55b5a247affa7b4d5fc4528cb28a85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLinuxBastionQsModuleProps(
            parameters=parameters, resources=resources
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnLinuxBastionQsModuleProps":
        '''Resource props.'''
        return typing.cast("CfnLinuxBastionQsModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnLinuxBastionQsModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type AWSQS::EC2::LinuxBastionQS::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnLinuxBastionQsModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnLinuxBastionQsModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnLinuxBastionQsModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abdeb3381f8023f5e56914e2a9b6edd7b43fab67f50eeb6fd6b9a7eed257a473)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnLinuxBastionQsModulePropsParameters"]:
        '''
        :schema: CfnLinuxBastionQsModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnLinuxBastionQsModulePropsResources"]:
        '''
        :schema: CfnLinuxBastionQsModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "alternative_iam_role": "alternativeIamRole",
        "alternative_initialization_script": "alternativeInitializationScript",
        "bastion_amios": "bastionAmios",
        "bastion_banner": "bastionBanner",
        "bastion_host_name": "bastionHostName",
        "bastion_instance_type": "bastionInstanceType",
        "bastion_tenancy": "bastionTenancy",
        "enable_banner": "enableBanner",
        "enable_tcp_forwarding": "enableTcpForwarding",
        "enable_x11_forwarding": "enableX11Forwarding",
        "environment_variables": "environmentVariables",
        "key_pair_name": "keyPairName",
        "num_bastion_hosts": "numBastionHosts",
        "os_image_override": "osImageOverride",
        "public_subnet1_id": "publicSubnet1Id",
        "public_subnet2_id": "publicSubnet2Id",
        "qss3_bucket_name": "qss3BucketName",
        "qss3_bucket_region": "qss3BucketRegion",
        "qss3_key_prefix": "qss3KeyPrefix",
        "remote_access_cidr": "remoteAccessCidr",
        "root_volume_size": "rootVolumeSize",
        "vpcid": "vpcid",
    },
)
class CfnLinuxBastionQsModulePropsParameters:
    def __init__(
        self,
        *,
        alternative_iam_role: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersAlternativeIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        alternative_initialization_script: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_amios: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersBastionAmios", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_banner: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersBastionBanner", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_host_name: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersBastionHostName", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_instance_type: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersBastionInstanceType", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_tenancy: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersBastionTenancy", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_banner: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersEnableBanner", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_tcp_forwarding: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_x11_forwarding: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding", typing.Dict[builtins.str, typing.Any]]] = None,
        environment_variables: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersEnvironmentVariables", typing.Dict[builtins.str, typing.Any]]] = None,
        key_pair_name: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersKeyPairName", typing.Dict[builtins.str, typing.Any]]] = None,
        num_bastion_hosts: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersNumBastionHosts", typing.Dict[builtins.str, typing.Any]]] = None,
        os_image_override: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersOsImageOverride", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet1_id: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id", typing.Dict[builtins.str, typing.Any]]] = None,
        public_subnet2_id: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id", typing.Dict[builtins.str, typing.Any]]] = None,
        qss3_bucket_name: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersQss3BucketName", typing.Dict[builtins.str, typing.Any]]] = None,
        qss3_bucket_region: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersQss3BucketRegion", typing.Dict[builtins.str, typing.Any]]] = None,
        qss3_key_prefix: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix", typing.Dict[builtins.str, typing.Any]]] = None,
        remote_access_cidr: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr", typing.Dict[builtins.str, typing.Any]]] = None,
        root_volume_size: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersRootVolumeSize", typing.Dict[builtins.str, typing.Any]]] = None,
        vpcid: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsParametersVpcid", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param alternative_iam_role: An existing IAM role name to attach to the bastion. If left blank, a new role will be created.
        :param alternative_initialization_script: An alternative initialization script to run during setup.
        :param bastion_amios: The Linux distribution for the AMI to be used for the bastion instances.
        :param bastion_banner: Banner text to display upon login.
        :param bastion_host_name: The value used for the name tag of the bastion host.
        :param bastion_instance_type: Amazon EC2 instance type for the bastion instances.
        :param bastion_tenancy: Bastion VPC tenancy (dedicated or default).
        :param enable_banner: Choose *true* to display a banner when connecting via SSH to the bastion.
        :param enable_tcp_forwarding: To enable TCP forwarding, choose *true*.
        :param enable_x11_forwarding: To enable X11 forwarding, choose *true*.
        :param environment_variables: A comma-separated list of environment variables for use in bootstrapping. Variables must be in the format ``key=value``. ``Value`` cannot contain commas.
        :param key_pair_name: Name of an existing public/private key pair. If you do not have one in this AWS Region, please create it before continuing.
        :param num_bastion_hosts: The number of bastion hosts to create. The maximum number is four.
        :param os_image_override: The Region-specific image to use for the instance.
        :param public_subnet1_id: ID of the public subnet 1 that you want to provision the first bastion into (e.g., subnet-a0246dcd).
        :param public_subnet2_id: ID of the public subnet 2 that you want to provision the second bastion into (e.g., subnet-e3246d8e).
        :param qss3_bucket_name: Name of the S3 bucket for your copy of the Quick Start assets. Keep the default name unless you are customizing the template. Changing the name updates code references to point to a new Quick Start location. This name can include numbers, lowercase letters, uppercase letters, and hyphens, but do not start or end with a hyphen (-). See https://aws-quickstart.github.io/option1.html.
        :param qss3_bucket_region: The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted. When using your own bucket, you must specify this value.
        :param qss3_key_prefix: S3 key prefix that is used to simulate a directory for your copy of the Quick Start assets. Keep the default prefix unless you are customizing the template. Changing this prefix updates code references to point to a new Quick Start location. This prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slashes (/). End with a forward slash. See https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html and https://aws-quickstart.github.io/option1.html.
        :param remote_access_cidr: Allowed CIDR block for external SSH access to the bastions.
        :param root_volume_size: The size in GB for the root EBS volume.
        :param vpcid: ID of the VPC (e.g., vpc-0343606e).

        :schema: CfnLinuxBastionQsModulePropsParameters
        '''
        if isinstance(alternative_iam_role, dict):
            alternative_iam_role = CfnLinuxBastionQsModulePropsParametersAlternativeIamRole(**alternative_iam_role)
        if isinstance(alternative_initialization_script, dict):
            alternative_initialization_script = CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript(**alternative_initialization_script)
        if isinstance(bastion_amios, dict):
            bastion_amios = CfnLinuxBastionQsModulePropsParametersBastionAmios(**bastion_amios)
        if isinstance(bastion_banner, dict):
            bastion_banner = CfnLinuxBastionQsModulePropsParametersBastionBanner(**bastion_banner)
        if isinstance(bastion_host_name, dict):
            bastion_host_name = CfnLinuxBastionQsModulePropsParametersBastionHostName(**bastion_host_name)
        if isinstance(bastion_instance_type, dict):
            bastion_instance_type = CfnLinuxBastionQsModulePropsParametersBastionInstanceType(**bastion_instance_type)
        if isinstance(bastion_tenancy, dict):
            bastion_tenancy = CfnLinuxBastionQsModulePropsParametersBastionTenancy(**bastion_tenancy)
        if isinstance(enable_banner, dict):
            enable_banner = CfnLinuxBastionQsModulePropsParametersEnableBanner(**enable_banner)
        if isinstance(enable_tcp_forwarding, dict):
            enable_tcp_forwarding = CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding(**enable_tcp_forwarding)
        if isinstance(enable_x11_forwarding, dict):
            enable_x11_forwarding = CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding(**enable_x11_forwarding)
        if isinstance(environment_variables, dict):
            environment_variables = CfnLinuxBastionQsModulePropsParametersEnvironmentVariables(**environment_variables)
        if isinstance(key_pair_name, dict):
            key_pair_name = CfnLinuxBastionQsModulePropsParametersKeyPairName(**key_pair_name)
        if isinstance(num_bastion_hosts, dict):
            num_bastion_hosts = CfnLinuxBastionQsModulePropsParametersNumBastionHosts(**num_bastion_hosts)
        if isinstance(os_image_override, dict):
            os_image_override = CfnLinuxBastionQsModulePropsParametersOsImageOverride(**os_image_override)
        if isinstance(public_subnet1_id, dict):
            public_subnet1_id = CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id(**public_subnet1_id)
        if isinstance(public_subnet2_id, dict):
            public_subnet2_id = CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id(**public_subnet2_id)
        if isinstance(qss3_bucket_name, dict):
            qss3_bucket_name = CfnLinuxBastionQsModulePropsParametersQss3BucketName(**qss3_bucket_name)
        if isinstance(qss3_bucket_region, dict):
            qss3_bucket_region = CfnLinuxBastionQsModulePropsParametersQss3BucketRegion(**qss3_bucket_region)
        if isinstance(qss3_key_prefix, dict):
            qss3_key_prefix = CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix(**qss3_key_prefix)
        if isinstance(remote_access_cidr, dict):
            remote_access_cidr = CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr(**remote_access_cidr)
        if isinstance(root_volume_size, dict):
            root_volume_size = CfnLinuxBastionQsModulePropsParametersRootVolumeSize(**root_volume_size)
        if isinstance(vpcid, dict):
            vpcid = CfnLinuxBastionQsModulePropsParametersVpcid(**vpcid)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__933a2adc9ab1095e75d1ce90db29a7eec0171b55100f5315d2d115d5b5ea40fe)
            check_type(argname="argument alternative_iam_role", value=alternative_iam_role, expected_type=type_hints["alternative_iam_role"])
            check_type(argname="argument alternative_initialization_script", value=alternative_initialization_script, expected_type=type_hints["alternative_initialization_script"])
            check_type(argname="argument bastion_amios", value=bastion_amios, expected_type=type_hints["bastion_amios"])
            check_type(argname="argument bastion_banner", value=bastion_banner, expected_type=type_hints["bastion_banner"])
            check_type(argname="argument bastion_host_name", value=bastion_host_name, expected_type=type_hints["bastion_host_name"])
            check_type(argname="argument bastion_instance_type", value=bastion_instance_type, expected_type=type_hints["bastion_instance_type"])
            check_type(argname="argument bastion_tenancy", value=bastion_tenancy, expected_type=type_hints["bastion_tenancy"])
            check_type(argname="argument enable_banner", value=enable_banner, expected_type=type_hints["enable_banner"])
            check_type(argname="argument enable_tcp_forwarding", value=enable_tcp_forwarding, expected_type=type_hints["enable_tcp_forwarding"])
            check_type(argname="argument enable_x11_forwarding", value=enable_x11_forwarding, expected_type=type_hints["enable_x11_forwarding"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument key_pair_name", value=key_pair_name, expected_type=type_hints["key_pair_name"])
            check_type(argname="argument num_bastion_hosts", value=num_bastion_hosts, expected_type=type_hints["num_bastion_hosts"])
            check_type(argname="argument os_image_override", value=os_image_override, expected_type=type_hints["os_image_override"])
            check_type(argname="argument public_subnet1_id", value=public_subnet1_id, expected_type=type_hints["public_subnet1_id"])
            check_type(argname="argument public_subnet2_id", value=public_subnet2_id, expected_type=type_hints["public_subnet2_id"])
            check_type(argname="argument qss3_bucket_name", value=qss3_bucket_name, expected_type=type_hints["qss3_bucket_name"])
            check_type(argname="argument qss3_bucket_region", value=qss3_bucket_region, expected_type=type_hints["qss3_bucket_region"])
            check_type(argname="argument qss3_key_prefix", value=qss3_key_prefix, expected_type=type_hints["qss3_key_prefix"])
            check_type(argname="argument remote_access_cidr", value=remote_access_cidr, expected_type=type_hints["remote_access_cidr"])
            check_type(argname="argument root_volume_size", value=root_volume_size, expected_type=type_hints["root_volume_size"])
            check_type(argname="argument vpcid", value=vpcid, expected_type=type_hints["vpcid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alternative_iam_role is not None:
            self._values["alternative_iam_role"] = alternative_iam_role
        if alternative_initialization_script is not None:
            self._values["alternative_initialization_script"] = alternative_initialization_script
        if bastion_amios is not None:
            self._values["bastion_amios"] = bastion_amios
        if bastion_banner is not None:
            self._values["bastion_banner"] = bastion_banner
        if bastion_host_name is not None:
            self._values["bastion_host_name"] = bastion_host_name
        if bastion_instance_type is not None:
            self._values["bastion_instance_type"] = bastion_instance_type
        if bastion_tenancy is not None:
            self._values["bastion_tenancy"] = bastion_tenancy
        if enable_banner is not None:
            self._values["enable_banner"] = enable_banner
        if enable_tcp_forwarding is not None:
            self._values["enable_tcp_forwarding"] = enable_tcp_forwarding
        if enable_x11_forwarding is not None:
            self._values["enable_x11_forwarding"] = enable_x11_forwarding
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if key_pair_name is not None:
            self._values["key_pair_name"] = key_pair_name
        if num_bastion_hosts is not None:
            self._values["num_bastion_hosts"] = num_bastion_hosts
        if os_image_override is not None:
            self._values["os_image_override"] = os_image_override
        if public_subnet1_id is not None:
            self._values["public_subnet1_id"] = public_subnet1_id
        if public_subnet2_id is not None:
            self._values["public_subnet2_id"] = public_subnet2_id
        if qss3_bucket_name is not None:
            self._values["qss3_bucket_name"] = qss3_bucket_name
        if qss3_bucket_region is not None:
            self._values["qss3_bucket_region"] = qss3_bucket_region
        if qss3_key_prefix is not None:
            self._values["qss3_key_prefix"] = qss3_key_prefix
        if remote_access_cidr is not None:
            self._values["remote_access_cidr"] = remote_access_cidr
        if root_volume_size is not None:
            self._values["root_volume_size"] = root_volume_size
        if vpcid is not None:
            self._values["vpcid"] = vpcid

    @builtins.property
    def alternative_iam_role(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersAlternativeIamRole"]:
        '''An existing IAM role name to attach to the bastion.

        If left blank, a new role will be created.

        :schema: CfnLinuxBastionQsModulePropsParameters#AlternativeIAMRole
        '''
        result = self._values.get("alternative_iam_role")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersAlternativeIamRole"], result)

    @builtins.property
    def alternative_initialization_script(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript"]:
        '''An alternative initialization script to run during setup.

        :schema: CfnLinuxBastionQsModulePropsParameters#AlternativeInitializationScript
        '''
        result = self._values.get("alternative_initialization_script")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript"], result)

    @builtins.property
    def bastion_amios(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionAmios"]:
        '''The Linux distribution for the AMI to be used for the bastion instances.

        :schema: CfnLinuxBastionQsModulePropsParameters#BastionAMIOS
        '''
        result = self._values.get("bastion_amios")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionAmios"], result)

    @builtins.property
    def bastion_banner(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionBanner"]:
        '''Banner text to display upon login.

        :schema: CfnLinuxBastionQsModulePropsParameters#BastionBanner
        '''
        result = self._values.get("bastion_banner")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionBanner"], result)

    @builtins.property
    def bastion_host_name(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionHostName"]:
        '''The value used for the name tag of the bastion host.

        :schema: CfnLinuxBastionQsModulePropsParameters#BastionHostName
        '''
        result = self._values.get("bastion_host_name")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionHostName"], result)

    @builtins.property
    def bastion_instance_type(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionInstanceType"]:
        '''Amazon EC2 instance type for the bastion instances.

        :schema: CfnLinuxBastionQsModulePropsParameters#BastionInstanceType
        '''
        result = self._values.get("bastion_instance_type")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionInstanceType"], result)

    @builtins.property
    def bastion_tenancy(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionTenancy"]:
        '''Bastion VPC tenancy (dedicated or default).

        :schema: CfnLinuxBastionQsModulePropsParameters#BastionTenancy
        '''
        result = self._values.get("bastion_tenancy")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersBastionTenancy"], result)

    @builtins.property
    def enable_banner(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersEnableBanner"]:
        '''Choose *true* to display a banner when connecting via SSH to the bastion.

        :schema: CfnLinuxBastionQsModulePropsParameters#EnableBanner
        '''
        result = self._values.get("enable_banner")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersEnableBanner"], result)

    @builtins.property
    def enable_tcp_forwarding(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding"]:
        '''To enable TCP forwarding, choose *true*.

        :schema: CfnLinuxBastionQsModulePropsParameters#EnableTCPForwarding
        '''
        result = self._values.get("enable_tcp_forwarding")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding"], result)

    @builtins.property
    def enable_x11_forwarding(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding"]:
        '''To enable X11 forwarding, choose *true*.

        :schema: CfnLinuxBastionQsModulePropsParameters#EnableX11Forwarding
        '''
        result = self._values.get("enable_x11_forwarding")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding"], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersEnvironmentVariables"]:
        '''A comma-separated list of environment variables for use in bootstrapping.

        Variables must be in the format ``key=value``. ``Value`` cannot contain commas.

        :schema: CfnLinuxBastionQsModulePropsParameters#EnvironmentVariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersEnvironmentVariables"], result)

    @builtins.property
    def key_pair_name(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersKeyPairName"]:
        '''Name of an existing public/private key pair.

        If you do not have one in this AWS Region, please create it before continuing.

        :schema: CfnLinuxBastionQsModulePropsParameters#KeyPairName
        '''
        result = self._values.get("key_pair_name")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersKeyPairName"], result)

    @builtins.property
    def num_bastion_hosts(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersNumBastionHosts"]:
        '''The number of bastion hosts to create.

        The maximum number is four.

        :schema: CfnLinuxBastionQsModulePropsParameters#NumBastionHosts
        '''
        result = self._values.get("num_bastion_hosts")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersNumBastionHosts"], result)

    @builtins.property
    def os_image_override(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersOsImageOverride"]:
        '''The Region-specific image to use for the instance.

        :schema: CfnLinuxBastionQsModulePropsParameters#OSImageOverride
        '''
        result = self._values.get("os_image_override")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersOsImageOverride"], result)

    @builtins.property
    def public_subnet1_id(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id"]:
        '''ID of the public subnet 1 that you want to provision the first bastion into (e.g., subnet-a0246dcd).

        :schema: CfnLinuxBastionQsModulePropsParameters#PublicSubnet1ID
        '''
        result = self._values.get("public_subnet1_id")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id"], result)

    @builtins.property
    def public_subnet2_id(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id"]:
        '''ID of the public subnet 2 that you want to provision the second bastion into (e.g., subnet-e3246d8e).

        :schema: CfnLinuxBastionQsModulePropsParameters#PublicSubnet2ID
        '''
        result = self._values.get("public_subnet2_id")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id"], result)

    @builtins.property
    def qss3_bucket_name(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersQss3BucketName"]:
        '''Name of the S3 bucket for your copy of the Quick Start assets.

        Keep the default name unless you are customizing the template. Changing the name updates code references to point to a new Quick Start location. This name can include numbers, lowercase letters, uppercase letters, and hyphens, but do not start or end with a hyphen (-). See https://aws-quickstart.github.io/option1.html.

        :schema: CfnLinuxBastionQsModulePropsParameters#QSS3BucketName
        '''
        result = self._values.get("qss3_bucket_name")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersQss3BucketName"], result)

    @builtins.property
    def qss3_bucket_region(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersQss3BucketRegion"]:
        '''The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        When using your own bucket, you must specify this value.

        :schema: CfnLinuxBastionQsModulePropsParameters#QSS3BucketRegion
        '''
        result = self._values.get("qss3_bucket_region")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersQss3BucketRegion"], result)

    @builtins.property
    def qss3_key_prefix(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix"]:
        '''S3 key prefix that is used to simulate a directory for your copy of the Quick Start assets.

        Keep the default prefix unless you are customizing the template. Changing this prefix updates code references to point to a new Quick Start location. This prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slashes (/). End with a forward slash. See https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html and https://aws-quickstart.github.io/option1.html.

        :schema: CfnLinuxBastionQsModulePropsParameters#QSS3KeyPrefix
        '''
        result = self._values.get("qss3_key_prefix")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix"], result)

    @builtins.property
    def remote_access_cidr(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr"]:
        '''Allowed CIDR block for external SSH access to the bastions.

        :schema: CfnLinuxBastionQsModulePropsParameters#RemoteAccessCIDR
        '''
        result = self._values.get("remote_access_cidr")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr"], result)

    @builtins.property
    def root_volume_size(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersRootVolumeSize"]:
        '''The size in GB for the root EBS volume.

        :schema: CfnLinuxBastionQsModulePropsParameters#RootVolumeSize
        '''
        result = self._values.get("root_volume_size")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersRootVolumeSize"], result)

    @builtins.property
    def vpcid(self) -> typing.Optional["CfnLinuxBastionQsModulePropsParametersVpcid"]:
        '''ID of the VPC (e.g., vpc-0343606e).

        :schema: CfnLinuxBastionQsModulePropsParameters#VPCID
        '''
        result = self._values.get("vpcid")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsParametersVpcid"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersAlternativeIamRole",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersAlternativeIamRole:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''An existing IAM role name to attach to the bastion.

        If left blank, a new role will be created.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersAlternativeIamRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34d72d9e40f0f26546ed000b05e35efad36d0608a5b2f1a92b1ad30acc8f9933)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersAlternativeIamRole#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersAlternativeIamRole#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersAlternativeIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''An alternative initialization script to run during setup.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17cd64acd6951b6aacf6869996b760502203097c6e5d489440d4ab64ec50e1d1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersBastionAmios",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersBastionAmios:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Linux distribution for the AMI to be used for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersBastionAmios
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66347ace125a163172c91c69296d8cd970d71e23459cf1bed9f73b872f219c21)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionAmios#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionAmios#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersBastionAmios(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersBastionBanner",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersBastionBanner:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Banner text to display upon login.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersBastionBanner
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ee61cb8b1b19aff8fcba8b85e698a3a2a21955e98c88c2125f965e656204dcc)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionBanner#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionBanner#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersBastionBanner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersBastionHostName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersBastionHostName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The value used for the name tag of the bastion host.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersBastionHostName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da5d7a920fb81fe219c4e19baf7907d16e89fe61361e4e9c98b1fc1d3ed6c47)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionHostName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionHostName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersBastionHostName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersBastionInstanceType",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersBastionInstanceType:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon EC2 instance type for the bastion instances.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersBastionInstanceType
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b217425082ef5710f85d0124e0023d75c6110d97610f4c0bb4f168258f682ee3)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionInstanceType#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionInstanceType#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersBastionInstanceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersBastionTenancy",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersBastionTenancy:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Bastion VPC tenancy (dedicated or default).

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersBastionTenancy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62540663e000be05297a9dfb473174842da989432d7e19111359701af23d7cb1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionTenancy#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersBastionTenancy#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersBastionTenancy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersEnableBanner",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersEnableBanner:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Choose *true* to display a banner when connecting via SSH to the bastion.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersEnableBanner
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2b7517605c9a55d494cde02fe1e97ca89a0c092cadc118f7bf5e0dea506d1b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersEnableBanner#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersEnableBanner#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersEnableBanner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''To enable TCP forwarding, choose *true*.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6e50e85ad3b5882a513ea98ef89080a9aa2276b0d5405dcd95bc8bc9768c91)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''To enable X11 forwarding, choose *true*.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03da5501827ce6990d0e3376d0992d6c745bdbbadb1c44caa9cd8a48f062be90)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersEnvironmentVariables",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersEnvironmentVariables:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''A comma-separated list of environment variables for use in bootstrapping.

        Variables must be in the format ``key=value``. ``Value`` cannot contain commas.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersEnvironmentVariables
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3de12a6efafb51725029302fd788a1b453f5946eefd08a134016aa957dccf46)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersEnvironmentVariables#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersEnvironmentVariables#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersEnvironmentVariables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersKeyPairName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersKeyPairName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of an existing public/private key pair.

        If you do not have one in this AWS Region, please create it before continuing.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersKeyPairName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6916dd1283af6839d1f594cdbee2ab7c3dabdba8837a525bac6782d5e5d2f04)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersKeyPairName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersKeyPairName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersKeyPairName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersNumBastionHosts",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersNumBastionHosts:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The number of bastion hosts to create.

        The maximum number is four.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersNumBastionHosts
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70d22abf9094479ef2cb6e5b76be391998f55038215275ae3f9bfb2ee75b654c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersNumBastionHosts#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersNumBastionHosts#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersNumBastionHosts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersOsImageOverride",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersOsImageOverride:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The Region-specific image to use for the instance.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersOsImageOverride
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__062b2442f7b0ab22dd04f81e1377b18dfa9c92f596e6eee8edb754ddd2a0a4bc)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersOsImageOverride#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersOsImageOverride#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersOsImageOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the public subnet 1 that you want to provision the first bastion into (e.g., subnet-a0246dcd).

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6d0d50d66389c9b80cc6687c659dfb3d21bd5d0a22eb3266b0fe6e719fc0cc9)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the public subnet 2 that you want to provision the second bastion into (e.g., subnet-e3246d8e).

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6486568f93ef33ba4bb1b8bf45a796571310863acd28a8affdb2151b84881968)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersQss3BucketName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersQss3BucketName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the S3 bucket for your copy of the Quick Start assets.

        Keep the default name unless you are customizing the template. Changing the name updates code references to point to a new Quick Start location. This name can include numbers, lowercase letters, uppercase letters, and hyphens, but do not start or end with a hyphen (-). See https://aws-quickstart.github.io/option1.html.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersQss3BucketName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30a96ad066ca1b2a4ee3183614bde2c15b362089996514470eea27ea3c003dc1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersQss3BucketName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersQss3BucketName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersQss3BucketName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersQss3BucketRegion",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersQss3BucketRegion:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The AWS Region where the Quick Start S3 bucket (QSS3BucketName) is hosted.

        When using your own bucket, you must specify this value.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersQss3BucketRegion
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca0be709a551222d0ce38d31a9e7fcde0aaecda71de5fbc787200a8448395d4)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersQss3BucketRegion#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersQss3BucketRegion#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersQss3BucketRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''S3 key prefix that is used to simulate a directory for your copy of the Quick Start assets.

        Keep the default prefix unless you are customizing the template. Changing this prefix updates code references to point to a new Quick Start location. This prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slashes (/). End with a forward slash. See https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html and https://aws-quickstart.github.io/option1.html.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9218f94c9da128791443c3e4ed2d0e403a9a3f5293101e08e5fead45fd78cacf)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Allowed CIDR block for external SSH access to the bastions.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6459e8a7ce1ebdcf2868246a6067e758f350723251e64ce506722a47c05ccccc)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersRootVolumeSize",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersRootVolumeSize:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The size in GB for the root EBS volume.

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersRootVolumeSize
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aca7a4dbb5d2563cdcd6bbf5d0acccb47e28e4e30f5a109369735f78756196d0)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersRootVolumeSize#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersRootVolumeSize#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersRootVolumeSize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsParametersVpcid",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnLinuxBastionQsModulePropsParametersVpcid:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''ID of the VPC (e.g., vpc-0343606e).

        :param description: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsParametersVpcid
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1cde6807bb3c9eff508bb1f1d9cd24be8202872a778cbf7f7e813fc445b7b04)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersVpcid#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnLinuxBastionQsModulePropsParametersVpcid#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsParametersVpcid(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "bastion_auto_scaling_group": "bastionAutoScalingGroup",
        "bastion_host_policy": "bastionHostPolicy",
        "bastion_host_profile": "bastionHostProfile",
        "bastion_host_role": "bastionHostRole",
        "bastion_launch_configuration": "bastionLaunchConfiguration",
        "bastion_main_log_group": "bastionMainLogGroup",
        "bastion_security_group": "bastionSecurityGroup",
        "eip1": "eip1",
        "eip2": "eip2",
        "eip3": "eip3",
        "eip4": "eip4",
        "ssh_metric_filter": "sshMetricFilter",
    },
)
class CfnLinuxBastionQsModulePropsResources:
    def __init__(
        self,
        *,
        bastion_auto_scaling_group: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_host_policy: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_host_profile: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesBastionHostProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_host_role: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesBastionHostRole", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_launch_configuration: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_main_log_group: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        bastion_security_group: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        eip1: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesEip1", typing.Dict[builtins.str, typing.Any]]] = None,
        eip2: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesEip2", typing.Dict[builtins.str, typing.Any]]] = None,
        eip3: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesEip3", typing.Dict[builtins.str, typing.Any]]] = None,
        eip4: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesEip4", typing.Dict[builtins.str, typing.Any]]] = None,
        ssh_metric_filter: typing.Optional[typing.Union["CfnLinuxBastionQsModulePropsResourcesSshMetricFilter", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bastion_auto_scaling_group: 
        :param bastion_host_policy: 
        :param bastion_host_profile: 
        :param bastion_host_role: 
        :param bastion_launch_configuration: 
        :param bastion_main_log_group: 
        :param bastion_security_group: 
        :param eip1: 
        :param eip2: 
        :param eip3: 
        :param eip4: 
        :param ssh_metric_filter: 

        :schema: CfnLinuxBastionQsModulePropsResources
        '''
        if isinstance(bastion_auto_scaling_group, dict):
            bastion_auto_scaling_group = CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup(**bastion_auto_scaling_group)
        if isinstance(bastion_host_policy, dict):
            bastion_host_policy = CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy(**bastion_host_policy)
        if isinstance(bastion_host_profile, dict):
            bastion_host_profile = CfnLinuxBastionQsModulePropsResourcesBastionHostProfile(**bastion_host_profile)
        if isinstance(bastion_host_role, dict):
            bastion_host_role = CfnLinuxBastionQsModulePropsResourcesBastionHostRole(**bastion_host_role)
        if isinstance(bastion_launch_configuration, dict):
            bastion_launch_configuration = CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration(**bastion_launch_configuration)
        if isinstance(bastion_main_log_group, dict):
            bastion_main_log_group = CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup(**bastion_main_log_group)
        if isinstance(bastion_security_group, dict):
            bastion_security_group = CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup(**bastion_security_group)
        if isinstance(eip1, dict):
            eip1 = CfnLinuxBastionQsModulePropsResourcesEip1(**eip1)
        if isinstance(eip2, dict):
            eip2 = CfnLinuxBastionQsModulePropsResourcesEip2(**eip2)
        if isinstance(eip3, dict):
            eip3 = CfnLinuxBastionQsModulePropsResourcesEip3(**eip3)
        if isinstance(eip4, dict):
            eip4 = CfnLinuxBastionQsModulePropsResourcesEip4(**eip4)
        if isinstance(ssh_metric_filter, dict):
            ssh_metric_filter = CfnLinuxBastionQsModulePropsResourcesSshMetricFilter(**ssh_metric_filter)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6202dc1e8df3476714fd8381021bec47ea730e3567603ddd6e563586572aad26)
            check_type(argname="argument bastion_auto_scaling_group", value=bastion_auto_scaling_group, expected_type=type_hints["bastion_auto_scaling_group"])
            check_type(argname="argument bastion_host_policy", value=bastion_host_policy, expected_type=type_hints["bastion_host_policy"])
            check_type(argname="argument bastion_host_profile", value=bastion_host_profile, expected_type=type_hints["bastion_host_profile"])
            check_type(argname="argument bastion_host_role", value=bastion_host_role, expected_type=type_hints["bastion_host_role"])
            check_type(argname="argument bastion_launch_configuration", value=bastion_launch_configuration, expected_type=type_hints["bastion_launch_configuration"])
            check_type(argname="argument bastion_main_log_group", value=bastion_main_log_group, expected_type=type_hints["bastion_main_log_group"])
            check_type(argname="argument bastion_security_group", value=bastion_security_group, expected_type=type_hints["bastion_security_group"])
            check_type(argname="argument eip1", value=eip1, expected_type=type_hints["eip1"])
            check_type(argname="argument eip2", value=eip2, expected_type=type_hints["eip2"])
            check_type(argname="argument eip3", value=eip3, expected_type=type_hints["eip3"])
            check_type(argname="argument eip4", value=eip4, expected_type=type_hints["eip4"])
            check_type(argname="argument ssh_metric_filter", value=ssh_metric_filter, expected_type=type_hints["ssh_metric_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bastion_auto_scaling_group is not None:
            self._values["bastion_auto_scaling_group"] = bastion_auto_scaling_group
        if bastion_host_policy is not None:
            self._values["bastion_host_policy"] = bastion_host_policy
        if bastion_host_profile is not None:
            self._values["bastion_host_profile"] = bastion_host_profile
        if bastion_host_role is not None:
            self._values["bastion_host_role"] = bastion_host_role
        if bastion_launch_configuration is not None:
            self._values["bastion_launch_configuration"] = bastion_launch_configuration
        if bastion_main_log_group is not None:
            self._values["bastion_main_log_group"] = bastion_main_log_group
        if bastion_security_group is not None:
            self._values["bastion_security_group"] = bastion_security_group
        if eip1 is not None:
            self._values["eip1"] = eip1
        if eip2 is not None:
            self._values["eip2"] = eip2
        if eip3 is not None:
            self._values["eip3"] = eip3
        if eip4 is not None:
            self._values["eip4"] = eip4
        if ssh_metric_filter is not None:
            self._values["ssh_metric_filter"] = ssh_metric_filter

    @builtins.property
    def bastion_auto_scaling_group(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#BastionAutoScalingGroup
        '''
        result = self._values.get("bastion_auto_scaling_group")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup"], result)

    @builtins.property
    def bastion_host_policy(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#BastionHostPolicy
        '''
        result = self._values.get("bastion_host_policy")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy"], result)

    @builtins.property
    def bastion_host_profile(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionHostProfile"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#BastionHostProfile
        '''
        result = self._values.get("bastion_host_profile")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionHostProfile"], result)

    @builtins.property
    def bastion_host_role(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionHostRole"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#BastionHostRole
        '''
        result = self._values.get("bastion_host_role")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionHostRole"], result)

    @builtins.property
    def bastion_launch_configuration(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#BastionLaunchConfiguration
        '''
        result = self._values.get("bastion_launch_configuration")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration"], result)

    @builtins.property
    def bastion_main_log_group(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#BastionMainLogGroup
        '''
        result = self._values.get("bastion_main_log_group")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup"], result)

    @builtins.property
    def bastion_security_group(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#BastionSecurityGroup
        '''
        result = self._values.get("bastion_security_group")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup"], result)

    @builtins.property
    def eip1(self) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesEip1"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#EIP1
        '''
        result = self._values.get("eip1")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesEip1"], result)

    @builtins.property
    def eip2(self) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesEip2"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#EIP2
        '''
        result = self._values.get("eip2")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesEip2"], result)

    @builtins.property
    def eip3(self) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesEip3"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#EIP3
        '''
        result = self._values.get("eip3")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesEip3"], result)

    @builtins.property
    def eip4(self) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesEip4"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#EIP4
        '''
        result = self._values.get("eip4")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesEip4"], result)

    @builtins.property
    def ssh_metric_filter(
        self,
    ) -> typing.Optional["CfnLinuxBastionQsModulePropsResourcesSshMetricFilter"]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResources#SSHMetricFilter
        '''
        result = self._values.get("ssh_metric_filter")
        return typing.cast(typing.Optional["CfnLinuxBastionQsModulePropsResourcesSshMetricFilter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e058c019399d10574fa333e7b9f05d829266e4651b0cec154e76315f3cf977c4)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__194c488cfee6279622383bd8a36e59b78238128a9b7bc84f922455eff9211e0e)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesBastionHostProfile",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesBastionHostProfile:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostProfile
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c72f6403788861aac189f4d2043c65ac1301d174611211b0bfdb6aa4cd4e1b68)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostProfile#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostProfile#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesBastionHostProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesBastionHostRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesBastionHostRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57bcfa5b65ef61275e15744d9bdb87214d3a697925eb3317adf9a3fe18ff0ba7)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionHostRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesBastionHostRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b4b13d204d46e00130c7f6d5ffe5c722462988c3ff5208767031868568282a6)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd61f57490286755c3b90812ac8fc56b39748bf2d68079f5c2f068707d1bd9a2)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4590afcffd05ec917298f07ab60817e5464dc8f774c1d44f66a3e8c08c519fa5)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesEip1",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesEip1:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesEip1
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c472fdc67cb8f933723c3ab9e3a79129f914c20e0bce350b4fb6b5477d99e73)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesEip1#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesEip1#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesEip1(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesEip2",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesEip2:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesEip2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e64ce1a0ae58dff4c984e382f0859220b9d0a19144f77348ab59d010208fdb4c)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesEip2#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesEip2#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesEip2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesEip3",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesEip3:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesEip3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24121c486fcb5c1f0fb403bc6eb7501fd9efd0372ce0a6afafdbc49753d1ae92)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesEip3#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesEip3#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesEip3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesEip4",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesEip4:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesEip4
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a69a8b2296b194d3d1e6225c10c7251be378fcbedcafa8e1e17b72732433746)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesEip4#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesEip4#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesEip4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/awsqs-ec2-linuxbastionqs-module.CfnLinuxBastionQsModulePropsResourcesSshMetricFilter",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnLinuxBastionQsModulePropsResourcesSshMetricFilter:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnLinuxBastionQsModulePropsResourcesSshMetricFilter
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__528938059b2775bd48ac58b3fdf005cf99302b4706403baf14b566154a46f760)
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
        :schema: CfnLinuxBastionQsModulePropsResourcesSshMetricFilter#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnLinuxBastionQsModulePropsResourcesSshMetricFilter#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinuxBastionQsModulePropsResourcesSshMetricFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLinuxBastionQsModule",
    "CfnLinuxBastionQsModuleProps",
    "CfnLinuxBastionQsModulePropsParameters",
    "CfnLinuxBastionQsModulePropsParametersAlternativeIamRole",
    "CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript",
    "CfnLinuxBastionQsModulePropsParametersBastionAmios",
    "CfnLinuxBastionQsModulePropsParametersBastionBanner",
    "CfnLinuxBastionQsModulePropsParametersBastionHostName",
    "CfnLinuxBastionQsModulePropsParametersBastionInstanceType",
    "CfnLinuxBastionQsModulePropsParametersBastionTenancy",
    "CfnLinuxBastionQsModulePropsParametersEnableBanner",
    "CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding",
    "CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding",
    "CfnLinuxBastionQsModulePropsParametersEnvironmentVariables",
    "CfnLinuxBastionQsModulePropsParametersKeyPairName",
    "CfnLinuxBastionQsModulePropsParametersNumBastionHosts",
    "CfnLinuxBastionQsModulePropsParametersOsImageOverride",
    "CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id",
    "CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id",
    "CfnLinuxBastionQsModulePropsParametersQss3BucketName",
    "CfnLinuxBastionQsModulePropsParametersQss3BucketRegion",
    "CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix",
    "CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr",
    "CfnLinuxBastionQsModulePropsParametersRootVolumeSize",
    "CfnLinuxBastionQsModulePropsParametersVpcid",
    "CfnLinuxBastionQsModulePropsResources",
    "CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup",
    "CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy",
    "CfnLinuxBastionQsModulePropsResourcesBastionHostProfile",
    "CfnLinuxBastionQsModulePropsResourcesBastionHostRole",
    "CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration",
    "CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup",
    "CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup",
    "CfnLinuxBastionQsModulePropsResourcesEip1",
    "CfnLinuxBastionQsModulePropsResourcesEip2",
    "CfnLinuxBastionQsModulePropsResourcesEip3",
    "CfnLinuxBastionQsModulePropsResourcesEip4",
    "CfnLinuxBastionQsModulePropsResourcesSshMetricFilter",
]

publication.publish()

def _typecheckingstub__0d587f5f0b1ebd1c7f8619a4a353a8bd5a55b5a247affa7b4d5fc4528cb28a85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abdeb3381f8023f5e56914e2a9b6edd7b43fab67f50eeb6fd6b9a7eed257a473(
    *,
    parameters: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__933a2adc9ab1095e75d1ce90db29a7eec0171b55100f5315d2d115d5b5ea40fe(
    *,
    alternative_iam_role: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersAlternativeIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    alternative_initialization_script: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersAlternativeInitializationScript, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_amios: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersBastionAmios, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_banner: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersBastionBanner, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_host_name: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersBastionHostName, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_instance_type: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersBastionInstanceType, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_tenancy: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersBastionTenancy, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_banner: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersEnableBanner, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_tcp_forwarding: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersEnableTcpForwarding, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_x11_forwarding: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersEnableX11Forwarding, typing.Dict[builtins.str, typing.Any]]] = None,
    environment_variables: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersEnvironmentVariables, typing.Dict[builtins.str, typing.Any]]] = None,
    key_pair_name: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersKeyPairName, typing.Dict[builtins.str, typing.Any]]] = None,
    num_bastion_hosts: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersNumBastionHosts, typing.Dict[builtins.str, typing.Any]]] = None,
    os_image_override: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersOsImageOverride, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet1_id: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersPublicSubnet1Id, typing.Dict[builtins.str, typing.Any]]] = None,
    public_subnet2_id: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersPublicSubnet2Id, typing.Dict[builtins.str, typing.Any]]] = None,
    qss3_bucket_name: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersQss3BucketName, typing.Dict[builtins.str, typing.Any]]] = None,
    qss3_bucket_region: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersQss3BucketRegion, typing.Dict[builtins.str, typing.Any]]] = None,
    qss3_key_prefix: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersQss3KeyPrefix, typing.Dict[builtins.str, typing.Any]]] = None,
    remote_access_cidr: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersRemoteAccessCidr, typing.Dict[builtins.str, typing.Any]]] = None,
    root_volume_size: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersRootVolumeSize, typing.Dict[builtins.str, typing.Any]]] = None,
    vpcid: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsParametersVpcid, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34d72d9e40f0f26546ed000b05e35efad36d0608a5b2f1a92b1ad30acc8f9933(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17cd64acd6951b6aacf6869996b760502203097c6e5d489440d4ab64ec50e1d1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66347ace125a163172c91c69296d8cd970d71e23459cf1bed9f73b872f219c21(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee61cb8b1b19aff8fcba8b85e698a3a2a21955e98c88c2125f965e656204dcc(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da5d7a920fb81fe219c4e19baf7907d16e89fe61361e4e9c98b1fc1d3ed6c47(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b217425082ef5710f85d0124e0023d75c6110d97610f4c0bb4f168258f682ee3(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62540663e000be05297a9dfb473174842da989432d7e19111359701af23d7cb1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2b7517605c9a55d494cde02fe1e97ca89a0c092cadc118f7bf5e0dea506d1b(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6e50e85ad3b5882a513ea98ef89080a9aa2276b0d5405dcd95bc8bc9768c91(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03da5501827ce6990d0e3376d0992d6c745bdbbadb1c44caa9cd8a48f062be90(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3de12a6efafb51725029302fd788a1b453f5946eefd08a134016aa957dccf46(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6916dd1283af6839d1f594cdbee2ab7c3dabdba8837a525bac6782d5e5d2f04(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d22abf9094479ef2cb6e5b76be391998f55038215275ae3f9bfb2ee75b654c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062b2442f7b0ab22dd04f81e1377b18dfa9c92f596e6eee8edb754ddd2a0a4bc(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6d0d50d66389c9b80cc6687c659dfb3d21bd5d0a22eb3266b0fe6e719fc0cc9(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6486568f93ef33ba4bb1b8bf45a796571310863acd28a8affdb2151b84881968(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a96ad066ca1b2a4ee3183614bde2c15b362089996514470eea27ea3c003dc1(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca0be709a551222d0ce38d31a9e7fcde0aaecda71de5fbc787200a8448395d4(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9218f94c9da128791443c3e4ed2d0e403a9a3f5293101e08e5fead45fd78cacf(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6459e8a7ce1ebdcf2868246a6067e758f350723251e64ce506722a47c05ccccc(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca7a4dbb5d2563cdcd6bbf5d0acccb47e28e4e30f5a109369735f78756196d0(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1cde6807bb3c9eff508bb1f1d9cd24be8202872a778cbf7f7e813fc445b7b04(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6202dc1e8df3476714fd8381021bec47ea730e3567603ddd6e563586572aad26(
    *,
    bastion_auto_scaling_group: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesBastionAutoScalingGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_host_policy: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesBastionHostPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_host_profile: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesBastionHostProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_host_role: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesBastionHostRole, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_launch_configuration: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesBastionLaunchConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_main_log_group: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesBastionMainLogGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    bastion_security_group: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesBastionSecurityGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    eip1: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesEip1, typing.Dict[builtins.str, typing.Any]]] = None,
    eip2: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesEip2, typing.Dict[builtins.str, typing.Any]]] = None,
    eip3: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesEip3, typing.Dict[builtins.str, typing.Any]]] = None,
    eip4: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesEip4, typing.Dict[builtins.str, typing.Any]]] = None,
    ssh_metric_filter: typing.Optional[typing.Union[CfnLinuxBastionQsModulePropsResourcesSshMetricFilter, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e058c019399d10574fa333e7b9f05d829266e4651b0cec154e76315f3cf977c4(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__194c488cfee6279622383bd8a36e59b78238128a9b7bc84f922455eff9211e0e(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c72f6403788861aac189f4d2043c65ac1301d174611211b0bfdb6aa4cd4e1b68(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57bcfa5b65ef61275e15744d9bdb87214d3a697925eb3317adf9a3fe18ff0ba7(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b4b13d204d46e00130c7f6d5ffe5c722462988c3ff5208767031868568282a6(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd61f57490286755c3b90812ac8fc56b39748bf2d68079f5c2f068707d1bd9a2(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4590afcffd05ec917298f07ab60817e5464dc8f774c1d44f66a3e8c08c519fa5(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c472fdc67cb8f933723c3ab9e3a79129f914c20e0bce350b4fb6b5477d99e73(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64ce1a0ae58dff4c984e382f0859220b9d0a19144f77348ab59d010208fdb4c(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24121c486fcb5c1f0fb403bc6eb7501fd9efd0372ce0a6afafdbc49753d1ae92(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a69a8b2296b194d3d1e6225c10c7251be378fcbedcafa8e1e17b72732433746(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__528938059b2775bd48ac58b3fdf005cf99302b4706403baf14b566154a46f760(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
