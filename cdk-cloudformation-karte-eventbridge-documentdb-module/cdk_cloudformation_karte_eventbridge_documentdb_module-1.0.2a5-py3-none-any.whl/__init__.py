'''
# karte-eventbridge-documentdb-module

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `KARTE::EventBridge::DocumentDB::MODULE` v1.0.2.

## Description

Schema for Module Fragment of type KARTE::EventBridge::DocumentDB::MODULE

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name KARTE::EventBridge::DocumentDB::MODULE \
  --publisher-id a2fa3829e2ccf0bb9ce593c2684ad795962eb804 \
  --type MODULE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/module/a2fa3829e2ccf0bb9ce593c2684ad795962eb804/KARTE-EventBridge-DocumentDB-MODULE \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `KARTE::EventBridge::DocumentDB::MODULE`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fkarte-eventbridge-documentdb-module+v1.0.2).
* Issues related to `KARTE::EventBridge::DocumentDB::MODULE` should be reported to the [publisher](undefined).

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


class CfnDocumentDbModule(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModule",
):
    '''A CloudFormation ``KARTE::EventBridge::DocumentDB::MODULE``.

    :cloudformationResource: KARTE::EventBridge::DocumentDB::MODULE
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Optional[typing.Union["CfnDocumentDbModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnDocumentDbModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Create a new ``KARTE::EventBridge::DocumentDB::MODULE``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param parameters: 
        :param resources: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e34b65c33da739a29e8e430f9bdf33bc0266feef68e1925f1ec7f27d74699faf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDocumentDbModuleProps(parameters=parameters, resources=resources)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDocumentDbModuleProps":
        '''Resource props.'''
        return typing.cast("CfnDocumentDbModuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModuleProps",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters", "resources": "resources"},
)
class CfnDocumentDbModuleProps:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union["CfnDocumentDbModulePropsParameters", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["CfnDocumentDbModulePropsResources", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Schema for Module Fragment of type KARTE::EventBridge::DocumentDB::MODULE.

        :param parameters: 
        :param resources: 

        :schema: CfnDocumentDbModuleProps
        '''
        if isinstance(parameters, dict):
            parameters = CfnDocumentDbModulePropsParameters(**parameters)
        if isinstance(resources, dict):
            resources = CfnDocumentDbModulePropsResources(**resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fdac04980662aa8e42140a24e2d6531e153dfbb325e563e182cb5263bbe4931)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def parameters(self) -> typing.Optional["CfnDocumentDbModulePropsParameters"]:
        '''
        :schema: CfnDocumentDbModuleProps#Parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParameters"], result)

    @builtins.property
    def resources(self) -> typing.Optional["CfnDocumentDbModulePropsResources"]:
        '''
        :schema: CfnDocumentDbModuleProps#Resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResources"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParameters",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "collection_name": "collectionName",
        "db_instance_class": "dbInstanceClass",
        "db_name": "dbName",
        "event_source_name": "eventSourceName",
        "master_username": "masterUsername",
        "master_user_password": "masterUserPassword",
        "security_group_ids": "securityGroupIds",
        "subnet_group_name": "subnetGroupName",
        "subnet_ids": "subnetIds",
    },
)
class CfnDocumentDbModulePropsParameters:
    def __init__(
        self,
        *,
        cluster_name: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersClusterName", typing.Dict[builtins.str, typing.Any]]] = None,
        collection_name: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersCollectionName", typing.Dict[builtins.str, typing.Any]]] = None,
        db_instance_class: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersDbInstanceClass", typing.Dict[builtins.str, typing.Any]]] = None,
        db_name: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersDbName", typing.Dict[builtins.str, typing.Any]]] = None,
        event_source_name: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersEventSourceName", typing.Dict[builtins.str, typing.Any]]] = None,
        master_username: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersMasterUsername", typing.Dict[builtins.str, typing.Any]]] = None,
        master_user_password: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersMasterUserPassword", typing.Dict[builtins.str, typing.Any]]] = None,
        security_group_ids: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersSecurityGroupIds", typing.Dict[builtins.str, typing.Any]]] = None,
        subnet_group_name: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersSubnetGroupName", typing.Dict[builtins.str, typing.Any]]] = None,
        subnet_ids: typing.Optional[typing.Union["CfnDocumentDbModulePropsParametersSubnetIds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cluster_name: Cluster Name.
        :param collection_name: Collection name of DocumentDB.
        :param db_instance_class: The compute and memory capacity of the DB instance.
        :param db_name: Database name of DocumentDB.
        :param event_source_name: Name of the Amazon EventBridge KARTE Event Source to associate with an Event Bus. For example, aws.partner/karte.io/{AWSAccountID}/{KARTEProjectId}/{AppName}
        :param master_username: Master Username.
        :param master_user_password: Master Password.
        :param security_group_ids: Amazon MemoryDB Security Group Ids.
        :param subnet_group_name: Amazon MemoryDB DB Subnet Group Name.
        :param subnet_ids: Amazon MemoryDB Subnet Ids.

        :schema: CfnDocumentDbModulePropsParameters
        '''
        if isinstance(cluster_name, dict):
            cluster_name = CfnDocumentDbModulePropsParametersClusterName(**cluster_name)
        if isinstance(collection_name, dict):
            collection_name = CfnDocumentDbModulePropsParametersCollectionName(**collection_name)
        if isinstance(db_instance_class, dict):
            db_instance_class = CfnDocumentDbModulePropsParametersDbInstanceClass(**db_instance_class)
        if isinstance(db_name, dict):
            db_name = CfnDocumentDbModulePropsParametersDbName(**db_name)
        if isinstance(event_source_name, dict):
            event_source_name = CfnDocumentDbModulePropsParametersEventSourceName(**event_source_name)
        if isinstance(master_username, dict):
            master_username = CfnDocumentDbModulePropsParametersMasterUsername(**master_username)
        if isinstance(master_user_password, dict):
            master_user_password = CfnDocumentDbModulePropsParametersMasterUserPassword(**master_user_password)
        if isinstance(security_group_ids, dict):
            security_group_ids = CfnDocumentDbModulePropsParametersSecurityGroupIds(**security_group_ids)
        if isinstance(subnet_group_name, dict):
            subnet_group_name = CfnDocumentDbModulePropsParametersSubnetGroupName(**subnet_group_name)
        if isinstance(subnet_ids, dict):
            subnet_ids = CfnDocumentDbModulePropsParametersSubnetIds(**subnet_ids)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58773cb58d5e814e84f339e5efe3c4e87cbb2f681e556ae7ae8d127fea661316)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument collection_name", value=collection_name, expected_type=type_hints["collection_name"])
            check_type(argname="argument db_instance_class", value=db_instance_class, expected_type=type_hints["db_instance_class"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument event_source_name", value=event_source_name, expected_type=type_hints["event_source_name"])
            check_type(argname="argument master_username", value=master_username, expected_type=type_hints["master_username"])
            check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if collection_name is not None:
            self._values["collection_name"] = collection_name
        if db_instance_class is not None:
            self._values["db_instance_class"] = db_instance_class
        if db_name is not None:
            self._values["db_name"] = db_name
        if event_source_name is not None:
            self._values["event_source_name"] = event_source_name
        if master_username is not None:
            self._values["master_username"] = master_username
        if master_user_password is not None:
            self._values["master_user_password"] = master_user_password
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_group_name is not None:
            self._values["subnet_group_name"] = subnet_group_name
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def cluster_name(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersClusterName"]:
        '''Cluster Name.

        :schema: CfnDocumentDbModulePropsParameters#ClusterName
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersClusterName"], result)

    @builtins.property
    def collection_name(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersCollectionName"]:
        '''Collection name of DocumentDB.

        :schema: CfnDocumentDbModulePropsParameters#CollectionName
        '''
        result = self._values.get("collection_name")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersCollectionName"], result)

    @builtins.property
    def db_instance_class(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersDbInstanceClass"]:
        '''The compute and memory capacity of the DB instance.

        :schema: CfnDocumentDbModulePropsParameters#DBInstanceClass
        '''
        result = self._values.get("db_instance_class")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersDbInstanceClass"], result)

    @builtins.property
    def db_name(self) -> typing.Optional["CfnDocumentDbModulePropsParametersDbName"]:
        '''Database name of DocumentDB.

        :schema: CfnDocumentDbModulePropsParameters#DBName
        '''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersDbName"], result)

    @builtins.property
    def event_source_name(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersEventSourceName"]:
        '''Name of the Amazon EventBridge KARTE Event Source to associate with an Event Bus.

        For example, aws.partner/karte.io/{AWSAccountID}/{KARTEProjectId}/{AppName}

        :schema: CfnDocumentDbModulePropsParameters#EventSourceName
        '''
        result = self._values.get("event_source_name")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersEventSourceName"], result)

    @builtins.property
    def master_username(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersMasterUsername"]:
        '''Master Username.

        :schema: CfnDocumentDbModulePropsParameters#MasterUsername
        '''
        result = self._values.get("master_username")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersMasterUsername"], result)

    @builtins.property
    def master_user_password(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersMasterUserPassword"]:
        '''Master Password.

        :schema: CfnDocumentDbModulePropsParameters#MasterUserPassword
        '''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersMasterUserPassword"], result)

    @builtins.property
    def security_group_ids(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersSecurityGroupIds"]:
        '''Amazon MemoryDB Security Group Ids.

        :schema: CfnDocumentDbModulePropsParameters#SecurityGroupIds
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersSecurityGroupIds"], result)

    @builtins.property
    def subnet_group_name(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersSubnetGroupName"]:
        '''Amazon MemoryDB DB Subnet Group Name.

        :schema: CfnDocumentDbModulePropsParameters#SubnetGroupName
        '''
        result = self._values.get("subnet_group_name")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersSubnetGroupName"], result)

    @builtins.property
    def subnet_ids(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsParametersSubnetIds"]:
        '''Amazon MemoryDB Subnet Ids.

        :schema: CfnDocumentDbModulePropsParameters#SubnetIds
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsParametersSubnetIds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersClusterName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersClusterName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Cluster Name.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersClusterName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0062822c480e13ad1c8a61ca558f926fba798f46d9b31a9a5995557326520d1d)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersClusterName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersClusterName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersClusterName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersCollectionName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersCollectionName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Collection name of DocumentDB.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersCollectionName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c4ea55b45468c55a7600964ead29d295c476e012e70f951578e262a325b354)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersCollectionName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersCollectionName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersCollectionName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersDbInstanceClass",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersDbInstanceClass:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''The compute and memory capacity of the DB instance.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersDbInstanceClass
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79788c7fdf3592b9f619aad285a4bb447fcc78149001de6a9015e97df0d407ec)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersDbInstanceClass#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersDbInstanceClass#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersDbInstanceClass(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersDbName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersDbName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Database name of DocumentDB.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersDbName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4608ed4663766b5d840f3e4210933df35eae7eeef6ee80c166383262c5c6217e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersDbName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersDbName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersDbName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersEventSourceName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersEventSourceName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Name of the Amazon EventBridge KARTE Event Source to associate with an Event Bus.

        For example, aws.partner/karte.io/{AWSAccountID}/{KARTEProjectId}/{AppName}

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersEventSourceName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aecdf9c2055fc3201725941408403bad5747ce4bdc3be08569db8718cabb21d6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersEventSourceName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersEventSourceName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersEventSourceName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersMasterUserPassword",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersMasterUserPassword:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Master Password.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersMasterUserPassword
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb07e6bfb90db8539eb3beb6d86dc0531c35d48dab841c882017247fff5a04a6)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersMasterUserPassword#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersMasterUserPassword#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersMasterUserPassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersMasterUsername",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersMasterUsername:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Master Username.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersMasterUsername
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a39e78f2fad577ac2c09f850e84a98a11e450944d647f15e9772d8efeebf6c2)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersMasterUsername#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersMasterUsername#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersMasterUsername(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersSecurityGroupIds",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersSecurityGroupIds:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon MemoryDB Security Group Ids.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersSecurityGroupIds
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__563f84b1e936b94cc6d290247435f34463737aaec95a353caf98f98e0fe8653e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersSecurityGroupIds#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersSecurityGroupIds#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersSecurityGroupIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersSubnetGroupName",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersSubnetGroupName:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon MemoryDB DB Subnet Group Name.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersSubnetGroupName
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be5202abfb0b2533498401002bdf4843bce28c8b601b9e24589de468f76f7fa)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersSubnetGroupName#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersSubnetGroupName#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersSubnetGroupName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsParametersSubnetIds",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "type": "type"},
)
class CfnDocumentDbModulePropsParametersSubnetIds:
    def __init__(self, *, description: builtins.str, type: builtins.str) -> None:
        '''Amazon MemoryDB Subnet Ids.

        :param description: 
        :param type: 

        :schema: CfnDocumentDbModulePropsParametersSubnetIds
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481f5b859e390aa91dade1936872698b3de92ce1561316ad21c12b96af6b105c)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "type": type,
        }

    @builtins.property
    def description(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersSubnetIds#Description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :schema: CfnDocumentDbModulePropsParametersSubnetIds#Type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsParametersSubnetIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResources",
    jsii_struct_bases=[],
    name_mapping={
        "document_db_cluster": "documentDbCluster",
        "document_db_instance": "documentDbInstance",
        "event_bridge_event_bus": "eventBridgeEventBus",
        "event_bridge_rule": "eventBridgeRule",
        "event_topic_policy": "eventTopicPolicy",
        "lambda_execution_role": "lambdaExecutionRole",
        "sns_topic": "snsTopic",
        "write_to_db_lambda_function": "writeToDbLambdaFunction",
    },
)
class CfnDocumentDbModulePropsResources:
    def __init__(
        self,
        *,
        document_db_cluster: typing.Optional[typing.Union["CfnDocumentDbModulePropsResourcesDocumentDbCluster", typing.Dict[builtins.str, typing.Any]]] = None,
        document_db_instance: typing.Optional[typing.Union["CfnDocumentDbModulePropsResourcesDocumentDbInstance", typing.Dict[builtins.str, typing.Any]]] = None,
        event_bridge_event_bus: typing.Optional[typing.Union["CfnDocumentDbModulePropsResourcesEventBridgeEventBus", typing.Dict[builtins.str, typing.Any]]] = None,
        event_bridge_rule: typing.Optional[typing.Union["CfnDocumentDbModulePropsResourcesEventBridgeRule", typing.Dict[builtins.str, typing.Any]]] = None,
        event_topic_policy: typing.Optional[typing.Union["CfnDocumentDbModulePropsResourcesEventTopicPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_execution_role: typing.Optional[typing.Union["CfnDocumentDbModulePropsResourcesLambdaExecutionRole", typing.Dict[builtins.str, typing.Any]]] = None,
        sns_topic: typing.Optional[typing.Union["CfnDocumentDbModulePropsResourcesSnsTopic", typing.Dict[builtins.str, typing.Any]]] = None,
        write_to_db_lambda_function: typing.Optional[typing.Union["CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param document_db_cluster: 
        :param document_db_instance: 
        :param event_bridge_event_bus: 
        :param event_bridge_rule: 
        :param event_topic_policy: 
        :param lambda_execution_role: 
        :param sns_topic: 
        :param write_to_db_lambda_function: 

        :schema: CfnDocumentDbModulePropsResources
        '''
        if isinstance(document_db_cluster, dict):
            document_db_cluster = CfnDocumentDbModulePropsResourcesDocumentDbCluster(**document_db_cluster)
        if isinstance(document_db_instance, dict):
            document_db_instance = CfnDocumentDbModulePropsResourcesDocumentDbInstance(**document_db_instance)
        if isinstance(event_bridge_event_bus, dict):
            event_bridge_event_bus = CfnDocumentDbModulePropsResourcesEventBridgeEventBus(**event_bridge_event_bus)
        if isinstance(event_bridge_rule, dict):
            event_bridge_rule = CfnDocumentDbModulePropsResourcesEventBridgeRule(**event_bridge_rule)
        if isinstance(event_topic_policy, dict):
            event_topic_policy = CfnDocumentDbModulePropsResourcesEventTopicPolicy(**event_topic_policy)
        if isinstance(lambda_execution_role, dict):
            lambda_execution_role = CfnDocumentDbModulePropsResourcesLambdaExecutionRole(**lambda_execution_role)
        if isinstance(sns_topic, dict):
            sns_topic = CfnDocumentDbModulePropsResourcesSnsTopic(**sns_topic)
        if isinstance(write_to_db_lambda_function, dict):
            write_to_db_lambda_function = CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction(**write_to_db_lambda_function)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f216a6d6630e9116c28ae6242741992ac040042cddd710d6f086e4d9f241425f)
            check_type(argname="argument document_db_cluster", value=document_db_cluster, expected_type=type_hints["document_db_cluster"])
            check_type(argname="argument document_db_instance", value=document_db_instance, expected_type=type_hints["document_db_instance"])
            check_type(argname="argument event_bridge_event_bus", value=event_bridge_event_bus, expected_type=type_hints["event_bridge_event_bus"])
            check_type(argname="argument event_bridge_rule", value=event_bridge_rule, expected_type=type_hints["event_bridge_rule"])
            check_type(argname="argument event_topic_policy", value=event_topic_policy, expected_type=type_hints["event_topic_policy"])
            check_type(argname="argument lambda_execution_role", value=lambda_execution_role, expected_type=type_hints["lambda_execution_role"])
            check_type(argname="argument sns_topic", value=sns_topic, expected_type=type_hints["sns_topic"])
            check_type(argname="argument write_to_db_lambda_function", value=write_to_db_lambda_function, expected_type=type_hints["write_to_db_lambda_function"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if document_db_cluster is not None:
            self._values["document_db_cluster"] = document_db_cluster
        if document_db_instance is not None:
            self._values["document_db_instance"] = document_db_instance
        if event_bridge_event_bus is not None:
            self._values["event_bridge_event_bus"] = event_bridge_event_bus
        if event_bridge_rule is not None:
            self._values["event_bridge_rule"] = event_bridge_rule
        if event_topic_policy is not None:
            self._values["event_topic_policy"] = event_topic_policy
        if lambda_execution_role is not None:
            self._values["lambda_execution_role"] = lambda_execution_role
        if sns_topic is not None:
            self._values["sns_topic"] = sns_topic
        if write_to_db_lambda_function is not None:
            self._values["write_to_db_lambda_function"] = write_to_db_lambda_function

    @builtins.property
    def document_db_cluster(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsResourcesDocumentDbCluster"]:
        '''
        :schema: CfnDocumentDbModulePropsResources#DocumentDBCluster
        '''
        result = self._values.get("document_db_cluster")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResourcesDocumentDbCluster"], result)

    @builtins.property
    def document_db_instance(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsResourcesDocumentDbInstance"]:
        '''
        :schema: CfnDocumentDbModulePropsResources#DocumentDBInstance
        '''
        result = self._values.get("document_db_instance")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResourcesDocumentDbInstance"], result)

    @builtins.property
    def event_bridge_event_bus(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsResourcesEventBridgeEventBus"]:
        '''
        :schema: CfnDocumentDbModulePropsResources#EventBridgeEventBus
        '''
        result = self._values.get("event_bridge_event_bus")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResourcesEventBridgeEventBus"], result)

    @builtins.property
    def event_bridge_rule(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsResourcesEventBridgeRule"]:
        '''
        :schema: CfnDocumentDbModulePropsResources#EventBridgeRule
        '''
        result = self._values.get("event_bridge_rule")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResourcesEventBridgeRule"], result)

    @builtins.property
    def event_topic_policy(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsResourcesEventTopicPolicy"]:
        '''
        :schema: CfnDocumentDbModulePropsResources#EventTopicPolicy
        '''
        result = self._values.get("event_topic_policy")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResourcesEventTopicPolicy"], result)

    @builtins.property
    def lambda_execution_role(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsResourcesLambdaExecutionRole"]:
        '''
        :schema: CfnDocumentDbModulePropsResources#LambdaExecutionRole
        '''
        result = self._values.get("lambda_execution_role")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResourcesLambdaExecutionRole"], result)

    @builtins.property
    def sns_topic(self) -> typing.Optional["CfnDocumentDbModulePropsResourcesSnsTopic"]:
        '''
        :schema: CfnDocumentDbModulePropsResources#SNSTopic
        '''
        result = self._values.get("sns_topic")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResourcesSnsTopic"], result)

    @builtins.property
    def write_to_db_lambda_function(
        self,
    ) -> typing.Optional["CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction"]:
        '''
        :schema: CfnDocumentDbModulePropsResources#WriteToDBLambdaFunction
        '''
        result = self._values.get("write_to_db_lambda_function")
        return typing.cast(typing.Optional["CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResourcesDocumentDbCluster",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDocumentDbModulePropsResourcesDocumentDbCluster:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDocumentDbModulePropsResourcesDocumentDbCluster
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f376c8371834088e9d472bffdeea695a65b470f3775fda417855ee911502106b)
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
        :schema: CfnDocumentDbModulePropsResourcesDocumentDbCluster#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDocumentDbModulePropsResourcesDocumentDbCluster#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResourcesDocumentDbCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResourcesDocumentDbInstance",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDocumentDbModulePropsResourcesDocumentDbInstance:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDocumentDbModulePropsResourcesDocumentDbInstance
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c23e9d8d931ddc04374acb2181b3a0a1c539982d50618663e3831fd32d1a9a52)
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
        :schema: CfnDocumentDbModulePropsResourcesDocumentDbInstance#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDocumentDbModulePropsResourcesDocumentDbInstance#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResourcesDocumentDbInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResourcesEventBridgeEventBus",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDocumentDbModulePropsResourcesEventBridgeEventBus:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDocumentDbModulePropsResourcesEventBridgeEventBus
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f79358ec3cf82e3afe4aab001eb4f9e97d693b5ad6372712204c617f4046bae)
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
        :schema: CfnDocumentDbModulePropsResourcesEventBridgeEventBus#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDocumentDbModulePropsResourcesEventBridgeEventBus#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResourcesEventBridgeEventBus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResourcesEventBridgeRule",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDocumentDbModulePropsResourcesEventBridgeRule:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDocumentDbModulePropsResourcesEventBridgeRule
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534e2cf4b46a7f7bef8507f85d6c45298b058cc277df215bbb33045220e6366f)
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
        :schema: CfnDocumentDbModulePropsResourcesEventBridgeRule#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDocumentDbModulePropsResourcesEventBridgeRule#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResourcesEventBridgeRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResourcesEventTopicPolicy",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDocumentDbModulePropsResourcesEventTopicPolicy:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDocumentDbModulePropsResourcesEventTopicPolicy
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa8288d33992c6c17a7522656b396bc8ad6f969d59a1ed3aa757866970faeab)
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
        :schema: CfnDocumentDbModulePropsResourcesEventTopicPolicy#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDocumentDbModulePropsResourcesEventTopicPolicy#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResourcesEventTopicPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResourcesLambdaExecutionRole",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDocumentDbModulePropsResourcesLambdaExecutionRole:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDocumentDbModulePropsResourcesLambdaExecutionRole
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bac59bf7f3b3c9f98c1129cde72c6b507915c6a9664a21b21d314a40f1bcdea2)
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
        :schema: CfnDocumentDbModulePropsResourcesLambdaExecutionRole#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDocumentDbModulePropsResourcesLambdaExecutionRole#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResourcesLambdaExecutionRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResourcesSnsTopic",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDocumentDbModulePropsResourcesSnsTopic:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDocumentDbModulePropsResourcesSnsTopic
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c66207e7ef63561651f2a32e23a8eb2e324f1d4d1069045dbb01da03471936ac)
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
        :schema: CfnDocumentDbModulePropsResourcesSnsTopic#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDocumentDbModulePropsResourcesSnsTopic#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResourcesSnsTopic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/karte-eventbridge-documentdb-module.CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties", "type": "type"},
)
class CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction:
    def __init__(
        self,
        *,
        properties: typing.Any = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param properties: 
        :param type: 

        :schema: CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f4e52aae5348d04ef60537da30802da99435eb6af7ae2456d7dcbef26795a5b)
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
        :schema: CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction#Properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Any, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDocumentDbModule",
    "CfnDocumentDbModuleProps",
    "CfnDocumentDbModulePropsParameters",
    "CfnDocumentDbModulePropsParametersClusterName",
    "CfnDocumentDbModulePropsParametersCollectionName",
    "CfnDocumentDbModulePropsParametersDbInstanceClass",
    "CfnDocumentDbModulePropsParametersDbName",
    "CfnDocumentDbModulePropsParametersEventSourceName",
    "CfnDocumentDbModulePropsParametersMasterUserPassword",
    "CfnDocumentDbModulePropsParametersMasterUsername",
    "CfnDocumentDbModulePropsParametersSecurityGroupIds",
    "CfnDocumentDbModulePropsParametersSubnetGroupName",
    "CfnDocumentDbModulePropsParametersSubnetIds",
    "CfnDocumentDbModulePropsResources",
    "CfnDocumentDbModulePropsResourcesDocumentDbCluster",
    "CfnDocumentDbModulePropsResourcesDocumentDbInstance",
    "CfnDocumentDbModulePropsResourcesEventBridgeEventBus",
    "CfnDocumentDbModulePropsResourcesEventBridgeRule",
    "CfnDocumentDbModulePropsResourcesEventTopicPolicy",
    "CfnDocumentDbModulePropsResourcesLambdaExecutionRole",
    "CfnDocumentDbModulePropsResourcesSnsTopic",
    "CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction",
]

publication.publish()

def _typecheckingstub__e34b65c33da739a29e8e430f9bdf33bc0266feef68e1925f1ec7f27d74699faf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Optional[typing.Union[CfnDocumentDbModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnDocumentDbModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fdac04980662aa8e42140a24e2d6531e153dfbb325e563e182cb5263bbe4931(
    *,
    parameters: typing.Optional[typing.Union[CfnDocumentDbModulePropsParameters, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[CfnDocumentDbModulePropsResources, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58773cb58d5e814e84f339e5efe3c4e87cbb2f681e556ae7ae8d127fea661316(
    *,
    cluster_name: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersClusterName, typing.Dict[builtins.str, typing.Any]]] = None,
    collection_name: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersCollectionName, typing.Dict[builtins.str, typing.Any]]] = None,
    db_instance_class: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersDbInstanceClass, typing.Dict[builtins.str, typing.Any]]] = None,
    db_name: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersDbName, typing.Dict[builtins.str, typing.Any]]] = None,
    event_source_name: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersEventSourceName, typing.Dict[builtins.str, typing.Any]]] = None,
    master_username: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersMasterUsername, typing.Dict[builtins.str, typing.Any]]] = None,
    master_user_password: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersMasterUserPassword, typing.Dict[builtins.str, typing.Any]]] = None,
    security_group_ids: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersSecurityGroupIds, typing.Dict[builtins.str, typing.Any]]] = None,
    subnet_group_name: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersSubnetGroupName, typing.Dict[builtins.str, typing.Any]]] = None,
    subnet_ids: typing.Optional[typing.Union[CfnDocumentDbModulePropsParametersSubnetIds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0062822c480e13ad1c8a61ca558f926fba798f46d9b31a9a5995557326520d1d(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c4ea55b45468c55a7600964ead29d295c476e012e70f951578e262a325b354(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79788c7fdf3592b9f619aad285a4bb447fcc78149001de6a9015e97df0d407ec(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4608ed4663766b5d840f3e4210933df35eae7eeef6ee80c166383262c5c6217e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aecdf9c2055fc3201725941408403bad5747ce4bdc3be08569db8718cabb21d6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb07e6bfb90db8539eb3beb6d86dc0531c35d48dab841c882017247fff5a04a6(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a39e78f2fad577ac2c09f850e84a98a11e450944d647f15e9772d8efeebf6c2(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__563f84b1e936b94cc6d290247435f34463737aaec95a353caf98f98e0fe8653e(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be5202abfb0b2533498401002bdf4843bce28c8b601b9e24589de468f76f7fa(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481f5b859e390aa91dade1936872698b3de92ce1561316ad21c12b96af6b105c(
    *,
    description: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f216a6d6630e9116c28ae6242741992ac040042cddd710d6f086e4d9f241425f(
    *,
    document_db_cluster: typing.Optional[typing.Union[CfnDocumentDbModulePropsResourcesDocumentDbCluster, typing.Dict[builtins.str, typing.Any]]] = None,
    document_db_instance: typing.Optional[typing.Union[CfnDocumentDbModulePropsResourcesDocumentDbInstance, typing.Dict[builtins.str, typing.Any]]] = None,
    event_bridge_event_bus: typing.Optional[typing.Union[CfnDocumentDbModulePropsResourcesEventBridgeEventBus, typing.Dict[builtins.str, typing.Any]]] = None,
    event_bridge_rule: typing.Optional[typing.Union[CfnDocumentDbModulePropsResourcesEventBridgeRule, typing.Dict[builtins.str, typing.Any]]] = None,
    event_topic_policy: typing.Optional[typing.Union[CfnDocumentDbModulePropsResourcesEventTopicPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_execution_role: typing.Optional[typing.Union[CfnDocumentDbModulePropsResourcesLambdaExecutionRole, typing.Dict[builtins.str, typing.Any]]] = None,
    sns_topic: typing.Optional[typing.Union[CfnDocumentDbModulePropsResourcesSnsTopic, typing.Dict[builtins.str, typing.Any]]] = None,
    write_to_db_lambda_function: typing.Optional[typing.Union[CfnDocumentDbModulePropsResourcesWriteToDbLambdaFunction, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f376c8371834088e9d472bffdeea695a65b470f3775fda417855ee911502106b(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23e9d8d931ddc04374acb2181b3a0a1c539982d50618663e3831fd32d1a9a52(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f79358ec3cf82e3afe4aab001eb4f9e97d693b5ad6372712204c617f4046bae(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534e2cf4b46a7f7bef8507f85d6c45298b058cc277df215bbb33045220e6366f(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa8288d33992c6c17a7522656b396bc8ad6f969d59a1ed3aa757866970faeab(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac59bf7f3b3c9f98c1129cde72c6b507915c6a9664a21b21d314a40f1bcdea2(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c66207e7ef63561651f2a32e23a8eb2e324f1d4d1069045dbb01da03471936ac(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f4e52aae5348d04ef60537da30802da99435eb6af7ae2456d7dcbef26795a5b(
    *,
    properties: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
