'''
# mongodb-atlas-cluster

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `MongoDB::Atlas::Cluster` v1.0.0.

---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This package is deprecated. Please use the respective `@mongodbatlas-awscdk/*` scoped package instead

---


## Description

The cluster resource provides access to your cluster configurations. The resource lets you create, edit and delete clusters. The resource requires your Project ID.

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name MongoDB::Atlas::Cluster \
  --publisher-id bb989456c78c398a858fef18f2ca1bfc1fbba082 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/bb989456c78c398a858fef18f2ca1bfc1fbba082/MongoDB-Atlas-Cluster \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `MongoDB::Atlas::Cluster`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fmongodb-atlas-cluster+v1.0.0).
* Issues related to `MongoDB::Atlas::Cluster` should be reported to the [publisher](undefined).

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
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.ApiKeyDefinition",
    jsii_struct_bases=[],
    name_mapping={"private_key": "privateKey", "public_key": "publicKey"},
)
class ApiKeyDefinition:
    def __init__(
        self,
        *,
        private_key: typing.Optional[builtins.str] = None,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private_key: 
        :param public_key: 

        :stability: deprecated
        :schema: apiKeyDefinition
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c610eab3e37e1b54bc5c58cc8f3f7f672e3bd33562a644c16288b0da81f83243)
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if private_key is not None:
            self._values["private_key"] = private_key
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: apiKeyDefinition#PrivateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: apiKeyDefinition#PublicKey
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.AutoScaling",
    jsii_struct_bases=[],
    name_mapping={"compute": "compute", "disk_gb_enabled": "diskGbEnabled"},
)
class AutoScaling:
    def __init__(
        self,
        *,
        compute: typing.Optional[typing.Union["Compute", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_gb_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param compute: 
        :param disk_gb_enabled: 

        :stability: deprecated
        :schema: autoScaling
        '''
        if isinstance(compute, dict):
            compute = Compute(**compute)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d08d58e7f17a943d2ae36fe2932bd72f1d98ee746e2912fa5b54f97142dd9a5)
            check_type(argname="argument compute", value=compute, expected_type=type_hints["compute"])
            check_type(argname="argument disk_gb_enabled", value=disk_gb_enabled, expected_type=type_hints["disk_gb_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compute is not None:
            self._values["compute"] = compute
        if disk_gb_enabled is not None:
            self._values["disk_gb_enabled"] = disk_gb_enabled

    @builtins.property
    def compute(self) -> typing.Optional["Compute"]:
        '''
        :stability: deprecated
        :schema: autoScaling#Compute
        '''
        result = self._values.get("compute")
        return typing.cast(typing.Optional["Compute"], result)

    @builtins.property
    def disk_gb_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: deprecated
        :schema: autoScaling#DiskGBEnabled
        '''
        result = self._values.get("disk_gb_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnCluster(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnCluster",
):
    '''A CloudFormation ``MongoDB::Atlas::Cluster``.

    :cloudformationResource: MongoDB::Atlas::Cluster
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_scaling: typing.Optional[typing.Union[AutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
        backup_enabled: typing.Optional[builtins.bool] = None,
        bi_connector: typing.Optional[typing.Union["CfnClusterPropsBiConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_type: typing.Optional[builtins.str] = None,
        connection_strings: typing.Optional[typing.Union["ConnectionStrings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption_at_rest_provider: typing.Optional["CfnClusterPropsEncryptionAtRestProvider"] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["CfnClusterPropsLabels", typing.Dict[builtins.str, typing.Any]]]] = None,
        mongo_db_major_version: typing.Optional[builtins.str] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        pit_enabled: typing.Optional[builtins.bool] = None,
        project_id: typing.Optional[builtins.str] = None,
        provider_backup_enabled: typing.Optional[builtins.bool] = None,
        provider_settings: typing.Optional[typing.Union["CfnClusterPropsProviderSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        replication_factor: typing.Optional[jsii.Number] = None,
        replication_specs: typing.Optional[typing.Sequence[typing.Union["ReplicationSpec", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``MongoDB::Atlas::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: (deprecated) Name of the cluster. Once the cluster is created, its name cannot be changed.
        :param api_keys: 
        :param auto_scaling: 
        :param backup_enabled: (deprecated) Applicable only for M10+ clusters. Set to true to enable Atlas continuous backups for the cluster. Set to false to disable continuous backups for the cluster. Atlas deletes any stored snapshots. See the continuous backup Snapshot Schedule for more information. You cannot enable continuous backups if you have an existing cluster in the project with Cloud Provider Snapshots enabled. The default value is false.
        :param bi_connector: 
        :param cluster_type: (deprecated) Type of the cluster that you want to create.
        :param connection_strings: (deprecated) Set of connection strings that your applications use to connect to this cluster. Use the parameters in this object to connect your applications to this cluster. See the MongoDB `Connection String URI Format <https://docs.mongodb.com/manual/reference/connection-string/>`_ reference for further details.
        :param disk_size_gb: (deprecated) Capacity, in gigabytes, of the hosts root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.
        :param encryption_at_rest_provider: (deprecated) Set the Encryption at Rest parameter.
        :param labels: (deprecated) Array containing key-value pairs that tag and categorize the cluster.
        :param mongo_db_major_version: (deprecated) Major version of the cluster to deploy.
        :param num_shards: (deprecated) Positive integer that specifies the number of shards to deploy for a sharded cluster.
        :param pit_enabled: (deprecated) Flag that indicates if the cluster uses Point-in-Time backups. If set to true, providerBackupEnabled must also be set to true.
        :param project_id: (deprecated) Unique identifier of the project the cluster belongs to.
        :param provider_backup_enabled: (deprecated) Applicable only for M10+ clusters. Set to true to enable Atlas Cloud Provider Snapshots backups for the cluster. Set to false to disable Cloud Provider Snapshots backups for the cluster. You cannot enable Cloud Provider Snapshots if you have an existing cluster in the project with continuous backups enabled. Note that you must set this value to true for NVMe clusters. The default value is false.
        :param provider_settings: 
        :param replication_factor: (deprecated) ReplicationFactor is deprecated. Use replicationSpecs.
        :param replication_specs: (deprecated) Configuration for cluster regions.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97dc4a2e5f9988afb37c42f7f66883b9617709641c4d692f282a7fffcf52d9e0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            name=name,
            api_keys=api_keys,
            auto_scaling=auto_scaling,
            backup_enabled=backup_enabled,
            bi_connector=bi_connector,
            cluster_type=cluster_type,
            connection_strings=connection_strings,
            disk_size_gb=disk_size_gb,
            encryption_at_rest_provider=encryption_at_rest_provider,
            labels=labels,
            mongo_db_major_version=mongo_db_major_version,
            num_shards=num_shards,
            pit_enabled=pit_enabled,
            project_id=project_id,
            provider_backup_enabled=provider_backup_enabled,
            provider_settings=provider_settings,
            replication_factor=replication_factor,
            replication_specs=replication_specs,
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
        '''Attribute ``MongoDB::Atlas::Cluster.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrMongoDBVersion")
    def attr_mongo_db_version(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoDBVersion``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoDBVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrMongoURI")
    def attr_mongo_uri(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoURI``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoURI"))

    @builtins.property
    @jsii.member(jsii_name="attrMongoURIUpdated")
    def attr_mongo_uri_updated(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoURIUpdated``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoURIUpdated"))

    @builtins.property
    @jsii.member(jsii_name="attrMongoURIWithOptions")
    def attr_mongo_uri_with_options(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.MongoURIWithOptions``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMongoURIWithOptions"))

    @builtins.property
    @jsii.member(jsii_name="attrPaused")
    def attr_paused(self) -> _aws_cdk_ceddda9d.IResolvable:
        '''Attribute ``MongoDB::Atlas::Cluster.Paused``.

        :link: http://unknown-url
        '''
        return typing.cast(_aws_cdk_ceddda9d.IResolvable, jsii.get(self, "attrPaused"))

    @builtins.property
    @jsii.member(jsii_name="attrSrvAddress")
    def attr_srv_address(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.SrvAddress``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSrvAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrStateName")
    def attr_state_name(self) -> builtins.str:
        '''Attribute ``MongoDB::Atlas::Cluster.StateName``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateName"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnClusterProps":
        '''Resource props.'''
        return typing.cast("CfnClusterProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "api_keys": "apiKeys",
        "auto_scaling": "autoScaling",
        "backup_enabled": "backupEnabled",
        "bi_connector": "biConnector",
        "cluster_type": "clusterType",
        "connection_strings": "connectionStrings",
        "disk_size_gb": "diskSizeGb",
        "encryption_at_rest_provider": "encryptionAtRestProvider",
        "labels": "labels",
        "mongo_db_major_version": "mongoDbMajorVersion",
        "num_shards": "numShards",
        "pit_enabled": "pitEnabled",
        "project_id": "projectId",
        "provider_backup_enabled": "providerBackupEnabled",
        "provider_settings": "providerSettings",
        "replication_factor": "replicationFactor",
        "replication_specs": "replicationSpecs",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_scaling: typing.Optional[typing.Union[AutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
        backup_enabled: typing.Optional[builtins.bool] = None,
        bi_connector: typing.Optional[typing.Union["CfnClusterPropsBiConnector", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_type: typing.Optional[builtins.str] = None,
        connection_strings: typing.Optional[typing.Union["ConnectionStrings", typing.Dict[builtins.str, typing.Any]]] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption_at_rest_provider: typing.Optional["CfnClusterPropsEncryptionAtRestProvider"] = None,
        labels: typing.Optional[typing.Sequence[typing.Union["CfnClusterPropsLabels", typing.Dict[builtins.str, typing.Any]]]] = None,
        mongo_db_major_version: typing.Optional[builtins.str] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        pit_enabled: typing.Optional[builtins.bool] = None,
        project_id: typing.Optional[builtins.str] = None,
        provider_backup_enabled: typing.Optional[builtins.bool] = None,
        provider_settings: typing.Optional[typing.Union["CfnClusterPropsProviderSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        replication_factor: typing.Optional[jsii.Number] = None,
        replication_specs: typing.Optional[typing.Sequence[typing.Union["ReplicationSpec", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''(deprecated) The cluster resource provides access to your cluster configurations.

        The resource lets you create, edit and delete clusters. The resource requires your Project ID.

        :param name: (deprecated) Name of the cluster. Once the cluster is created, its name cannot be changed.
        :param api_keys: 
        :param auto_scaling: 
        :param backup_enabled: (deprecated) Applicable only for M10+ clusters. Set to true to enable Atlas continuous backups for the cluster. Set to false to disable continuous backups for the cluster. Atlas deletes any stored snapshots. See the continuous backup Snapshot Schedule for more information. You cannot enable continuous backups if you have an existing cluster in the project with Cloud Provider Snapshots enabled. The default value is false.
        :param bi_connector: 
        :param cluster_type: (deprecated) Type of the cluster that you want to create.
        :param connection_strings: (deprecated) Set of connection strings that your applications use to connect to this cluster. Use the parameters in this object to connect your applications to this cluster. See the MongoDB `Connection String URI Format <https://docs.mongodb.com/manual/reference/connection-string/>`_ reference for further details.
        :param disk_size_gb: (deprecated) Capacity, in gigabytes, of the hosts root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.
        :param encryption_at_rest_provider: (deprecated) Set the Encryption at Rest parameter.
        :param labels: (deprecated) Array containing key-value pairs that tag and categorize the cluster.
        :param mongo_db_major_version: (deprecated) Major version of the cluster to deploy.
        :param num_shards: (deprecated) Positive integer that specifies the number of shards to deploy for a sharded cluster.
        :param pit_enabled: (deprecated) Flag that indicates if the cluster uses Point-in-Time backups. If set to true, providerBackupEnabled must also be set to true.
        :param project_id: (deprecated) Unique identifier of the project the cluster belongs to.
        :param provider_backup_enabled: (deprecated) Applicable only for M10+ clusters. Set to true to enable Atlas Cloud Provider Snapshots backups for the cluster. Set to false to disable Cloud Provider Snapshots backups for the cluster. You cannot enable Cloud Provider Snapshots if you have an existing cluster in the project with continuous backups enabled. Note that you must set this value to true for NVMe clusters. The default value is false.
        :param provider_settings: 
        :param replication_factor: (deprecated) ReplicationFactor is deprecated. Use replicationSpecs.
        :param replication_specs: (deprecated) Configuration for cluster regions.

        :stability: deprecated
        :schema: CfnClusterProps
        '''
        if isinstance(api_keys, dict):
            api_keys = ApiKeyDefinition(**api_keys)
        if isinstance(auto_scaling, dict):
            auto_scaling = AutoScaling(**auto_scaling)
        if isinstance(bi_connector, dict):
            bi_connector = CfnClusterPropsBiConnector(**bi_connector)
        if isinstance(connection_strings, dict):
            connection_strings = ConnectionStrings(**connection_strings)
        if isinstance(provider_settings, dict):
            provider_settings = CfnClusterPropsProviderSettings(**provider_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5c94d3cd97aac74155001fe1b47254ebc6c92fbd18fb2481f740ae3decbe0ad)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument api_keys", value=api_keys, expected_type=type_hints["api_keys"])
            check_type(argname="argument auto_scaling", value=auto_scaling, expected_type=type_hints["auto_scaling"])
            check_type(argname="argument backup_enabled", value=backup_enabled, expected_type=type_hints["backup_enabled"])
            check_type(argname="argument bi_connector", value=bi_connector, expected_type=type_hints["bi_connector"])
            check_type(argname="argument cluster_type", value=cluster_type, expected_type=type_hints["cluster_type"])
            check_type(argname="argument connection_strings", value=connection_strings, expected_type=type_hints["connection_strings"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument encryption_at_rest_provider", value=encryption_at_rest_provider, expected_type=type_hints["encryption_at_rest_provider"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mongo_db_major_version", value=mongo_db_major_version, expected_type=type_hints["mongo_db_major_version"])
            check_type(argname="argument num_shards", value=num_shards, expected_type=type_hints["num_shards"])
            check_type(argname="argument pit_enabled", value=pit_enabled, expected_type=type_hints["pit_enabled"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument provider_backup_enabled", value=provider_backup_enabled, expected_type=type_hints["provider_backup_enabled"])
            check_type(argname="argument provider_settings", value=provider_settings, expected_type=type_hints["provider_settings"])
            check_type(argname="argument replication_factor", value=replication_factor, expected_type=type_hints["replication_factor"])
            check_type(argname="argument replication_specs", value=replication_specs, expected_type=type_hints["replication_specs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if api_keys is not None:
            self._values["api_keys"] = api_keys
        if auto_scaling is not None:
            self._values["auto_scaling"] = auto_scaling
        if backup_enabled is not None:
            self._values["backup_enabled"] = backup_enabled
        if bi_connector is not None:
            self._values["bi_connector"] = bi_connector
        if cluster_type is not None:
            self._values["cluster_type"] = cluster_type
        if connection_strings is not None:
            self._values["connection_strings"] = connection_strings
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if encryption_at_rest_provider is not None:
            self._values["encryption_at_rest_provider"] = encryption_at_rest_provider
        if labels is not None:
            self._values["labels"] = labels
        if mongo_db_major_version is not None:
            self._values["mongo_db_major_version"] = mongo_db_major_version
        if num_shards is not None:
            self._values["num_shards"] = num_shards
        if pit_enabled is not None:
            self._values["pit_enabled"] = pit_enabled
        if project_id is not None:
            self._values["project_id"] = project_id
        if provider_backup_enabled is not None:
            self._values["provider_backup_enabled"] = provider_backup_enabled
        if provider_settings is not None:
            self._values["provider_settings"] = provider_settings
        if replication_factor is not None:
            self._values["replication_factor"] = replication_factor
        if replication_specs is not None:
            self._values["replication_specs"] = replication_specs

    @builtins.property
    def name(self) -> builtins.str:
        '''(deprecated) Name of the cluster.

        Once the cluster is created, its name cannot be changed.

        :stability: deprecated
        :schema: CfnClusterProps#Name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_keys(self) -> typing.Optional[ApiKeyDefinition]:
        '''
        :stability: deprecated
        :schema: CfnClusterProps#ApiKeys
        '''
        result = self._values.get("api_keys")
        return typing.cast(typing.Optional[ApiKeyDefinition], result)

    @builtins.property
    def auto_scaling(self) -> typing.Optional[AutoScaling]:
        '''
        :stability: deprecated
        :schema: CfnClusterProps#AutoScaling
        '''
        result = self._values.get("auto_scaling")
        return typing.cast(typing.Optional[AutoScaling], result)

    @builtins.property
    def backup_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Applicable only for M10+ clusters.

        Set to true to enable Atlas continuous backups for the cluster. Set to false to disable continuous backups for the cluster. Atlas deletes any stored snapshots. See the continuous backup Snapshot Schedule for more information. You cannot enable continuous backups if you have an existing cluster in the project with Cloud Provider Snapshots enabled. The default value is false.

        :stability: deprecated
        :schema: CfnClusterProps#BackupEnabled
        '''
        result = self._values.get("backup_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bi_connector(self) -> typing.Optional["CfnClusterPropsBiConnector"]:
        '''
        :stability: deprecated
        :schema: CfnClusterProps#BiConnector
        '''
        result = self._values.get("bi_connector")
        return typing.cast(typing.Optional["CfnClusterPropsBiConnector"], result)

    @builtins.property
    def cluster_type(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Type of the cluster that you want to create.

        :stability: deprecated
        :schema: CfnClusterProps#ClusterType
        '''
        result = self._values.get("cluster_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_strings(self) -> typing.Optional["ConnectionStrings"]:
        '''(deprecated) Set of connection strings that your applications use to connect to this cluster.

        Use the parameters in this object to connect your applications to this cluster. See the MongoDB `Connection String URI Format <https://docs.mongodb.com/manual/reference/connection-string/>`_ reference for further details.

        :stability: deprecated
        :schema: CfnClusterProps#ConnectionStrings
        '''
        result = self._values.get("connection_strings")
        return typing.cast(typing.Optional["ConnectionStrings"], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) Capacity, in gigabytes, of the hosts root volume.

        Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.

        :stability: deprecated
        :schema: CfnClusterProps#DiskSizeGB
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption_at_rest_provider(
        self,
    ) -> typing.Optional["CfnClusterPropsEncryptionAtRestProvider"]:
        '''(deprecated) Set the Encryption at Rest parameter.

        :stability: deprecated
        :schema: CfnClusterProps#EncryptionAtRestProvider
        '''
        result = self._values.get("encryption_at_rest_provider")
        return typing.cast(typing.Optional["CfnClusterPropsEncryptionAtRestProvider"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List["CfnClusterPropsLabels"]]:
        '''(deprecated) Array containing key-value pairs that tag and categorize the cluster.

        :stability: deprecated
        :schema: CfnClusterProps#Labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List["CfnClusterPropsLabels"]], result)

    @builtins.property
    def mongo_db_major_version(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Major version of the cluster to deploy.

        :stability: deprecated
        :schema: CfnClusterProps#MongoDBMajorVersion
        '''
        result = self._values.get("mongo_db_major_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_shards(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) Positive integer that specifies the number of shards to deploy for a sharded cluster.

        :stability: deprecated
        :schema: CfnClusterProps#NumShards
        '''
        result = self._values.get("num_shards")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pit_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Flag that indicates if the cluster uses Point-in-Time backups.

        If set to true, providerBackupEnabled must also be set to true.

        :stability: deprecated
        :schema: CfnClusterProps#PitEnabled
        '''
        result = self._values.get("pit_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Unique identifier of the project the cluster belongs to.

        :stability: deprecated
        :schema: CfnClusterProps#ProjectId
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_backup_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Applicable only for M10+ clusters.

        Set to true to enable Atlas Cloud Provider Snapshots backups for the cluster. Set to false to disable Cloud Provider Snapshots backups for the cluster. You cannot enable Cloud Provider Snapshots if you have an existing cluster in the project with continuous backups enabled. Note that you must set this value to true for NVMe clusters. The default value is false.

        :stability: deprecated
        :schema: CfnClusterProps#ProviderBackupEnabled
        '''
        result = self._values.get("provider_backup_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def provider_settings(self) -> typing.Optional["CfnClusterPropsProviderSettings"]:
        '''
        :stability: deprecated
        :schema: CfnClusterProps#ProviderSettings
        '''
        result = self._values.get("provider_settings")
        return typing.cast(typing.Optional["CfnClusterPropsProviderSettings"], result)

    @builtins.property
    def replication_factor(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) ReplicationFactor is deprecated.

        Use replicationSpecs.

        :stability: deprecated
        :schema: CfnClusterProps#ReplicationFactor
        '''
        result = self._values.get("replication_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replication_specs(self) -> typing.Optional[typing.List["ReplicationSpec"]]:
        '''(deprecated) Configuration for cluster regions.

        :stability: deprecated
        :schema: CfnClusterProps#ReplicationSpecs
        '''
        result = self._values.get("replication_specs")
        return typing.cast(typing.Optional[typing.List["ReplicationSpec"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterPropsBiConnector",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "read_preference": "readPreference"},
)
class CfnClusterPropsBiConnector:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        read_preference: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: 
        :param read_preference: 

        :stability: deprecated
        :schema: CfnClusterPropsBiConnector
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__204a702f272ef0e8ba699cbedf3b81209053d42f8edbe0f25fa6b754c39cc60e)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument read_preference", value=read_preference, expected_type=type_hints["read_preference"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if read_preference is not None:
            self._values["read_preference"] = read_preference

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsBiConnector#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_preference(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsBiConnector#ReadPreference
        '''
        result = self._values.get("read_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsBiConnector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterPropsEncryptionAtRestProvider"
)
class CfnClusterPropsEncryptionAtRestProvider(enum.Enum):
    '''(deprecated) Set the Encryption at Rest parameter.

    :stability: deprecated
    :schema: CfnClusterPropsEncryptionAtRestProvider
    '''

    AWS = "AWS"
    '''(deprecated) AWS.

    :stability: deprecated
    '''
    GCP = "GCP"
    '''(deprecated) GCP.

    :stability: deprecated
    '''
    AZURE = "AZURE"
    '''(deprecated) AZURE.

    :stability: deprecated
    '''
    NONE = "NONE"
    '''(deprecated) NONE.

    :stability: deprecated
    '''


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterPropsLabels",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class CfnClusterPropsLabels:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: 
        :param value: 

        :stability: deprecated
        :schema: CfnClusterPropsLabels
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2855e69cfad720bc80619a3fad984f34f3c234bd0b6ee152a7b593fa934837c0)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsLabels#Key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsLabels#Value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.CfnClusterPropsProviderSettings",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling": "autoScaling",
        "backing_provider_name": "backingProviderName",
        "disk_iops": "diskIops",
        "encrypt_ebs_volume": "encryptEbsVolume",
        "instance_size_name": "instanceSizeName",
        "provider_name": "providerName",
        "region_name": "regionName",
        "volume_type": "volumeType",
    },
)
class CfnClusterPropsProviderSettings:
    def __init__(
        self,
        *,
        auto_scaling: typing.Optional[typing.Union[AutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
        backing_provider_name: typing.Optional[builtins.str] = None,
        disk_iops: typing.Optional[jsii.Number] = None,
        encrypt_ebs_volume: typing.Optional[builtins.bool] = None,
        instance_size_name: typing.Optional[builtins.str] = None,
        provider_name: typing.Optional[builtins.str] = None,
        region_name: typing.Optional[builtins.str] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_scaling: 
        :param backing_provider_name: 
        :param disk_iops: 
        :param encrypt_ebs_volume: 
        :param instance_size_name: 
        :param provider_name: 
        :param region_name: 
        :param volume_type: 

        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings
        '''
        if isinstance(auto_scaling, dict):
            auto_scaling = AutoScaling(**auto_scaling)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__384db7d74549cd4fc5d8f7b385753dc73ed807edb95d7dca85c32330b9b672d6)
            check_type(argname="argument auto_scaling", value=auto_scaling, expected_type=type_hints["auto_scaling"])
            check_type(argname="argument backing_provider_name", value=backing_provider_name, expected_type=type_hints["backing_provider_name"])
            check_type(argname="argument disk_iops", value=disk_iops, expected_type=type_hints["disk_iops"])
            check_type(argname="argument encrypt_ebs_volume", value=encrypt_ebs_volume, expected_type=type_hints["encrypt_ebs_volume"])
            check_type(argname="argument instance_size_name", value=instance_size_name, expected_type=type_hints["instance_size_name"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_scaling is not None:
            self._values["auto_scaling"] = auto_scaling
        if backing_provider_name is not None:
            self._values["backing_provider_name"] = backing_provider_name
        if disk_iops is not None:
            self._values["disk_iops"] = disk_iops
        if encrypt_ebs_volume is not None:
            self._values["encrypt_ebs_volume"] = encrypt_ebs_volume
        if instance_size_name is not None:
            self._values["instance_size_name"] = instance_size_name
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if region_name is not None:
            self._values["region_name"] = region_name
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def auto_scaling(self) -> typing.Optional[AutoScaling]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings#AutoScaling
        '''
        result = self._values.get("auto_scaling")
        return typing.cast(typing.Optional[AutoScaling], result)

    @builtins.property
    def backing_provider_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings#BackingProviderName
        '''
        result = self._values.get("backing_provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_iops(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings#DiskIOPS
        '''
        result = self._values.get("disk_iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encrypt_ebs_volume(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings#EncryptEBSVolume
        '''
        result = self._values.get("encrypt_ebs_volume")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_size_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings#InstanceSizeName
        '''
        result = self._values.get("instance_size_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings#ProviderName
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings#RegionName
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: CfnClusterPropsProviderSettings#VolumeType
        '''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterPropsProviderSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.Compute",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "max_instance_size": "maxInstanceSize",
        "min_instance_size": "minInstanceSize",
        "scale_down_enabled": "scaleDownEnabled",
    },
)
class Compute:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.bool] = None,
        max_instance_size: typing.Optional[builtins.str] = None,
        min_instance_size: typing.Optional[builtins.str] = None,
        scale_down_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param enabled: 
        :param max_instance_size: 
        :param min_instance_size: 
        :param scale_down_enabled: 

        :stability: deprecated
        :schema: compute
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36a9c3b96f232883fd2f5a4b4b7d1c7cbd90961fb4bdc801c5af8b6ae4873216)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument max_instance_size", value=max_instance_size, expected_type=type_hints["max_instance_size"])
            check_type(argname="argument min_instance_size", value=min_instance_size, expected_type=type_hints["min_instance_size"])
            check_type(argname="argument scale_down_enabled", value=scale_down_enabled, expected_type=type_hints["scale_down_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if max_instance_size is not None:
            self._values["max_instance_size"] = max_instance_size
        if min_instance_size is not None:
            self._values["min_instance_size"] = min_instance_size
        if scale_down_enabled is not None:
            self._values["scale_down_enabled"] = scale_down_enabled

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: deprecated
        :schema: compute#Enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_instance_size(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: compute#MaxInstanceSize
        '''
        result = self._values.get("max_instance_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_instance_size(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: compute#MinInstanceSize
        '''
        result = self._values.get("min_instance_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_enabled(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: deprecated
        :schema: compute#ScaleDownEnabled
        '''
        result = self._values.get("scale_down_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Compute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.ConnectionStrings",
    jsii_struct_bases=[],
    name_mapping={
        "private": "private",
        "private_srv": "privateSrv",
        "standard": "standard",
        "standard_srv": "standardSrv",
    },
)
class ConnectionStrings:
    def __init__(
        self,
        *,
        private: typing.Optional[builtins.str] = None,
        private_srv: typing.Optional[builtins.str] = None,
        standard: typing.Optional[builtins.str] = None,
        standard_srv: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param private: 
        :param private_srv: 
        :param standard: 
        :param standard_srv: 

        :stability: deprecated
        :schema: connectionStrings
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65ff19860da47aafff9faa188554a5f58300431b561f1797400a01d3ee0d91d2)
            check_type(argname="argument private", value=private, expected_type=type_hints["private"])
            check_type(argname="argument private_srv", value=private_srv, expected_type=type_hints["private_srv"])
            check_type(argname="argument standard", value=standard, expected_type=type_hints["standard"])
            check_type(argname="argument standard_srv", value=standard_srv, expected_type=type_hints["standard_srv"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if private is not None:
            self._values["private"] = private
        if private_srv is not None:
            self._values["private_srv"] = private_srv
        if standard is not None:
            self._values["standard"] = standard
        if standard_srv is not None:
            self._values["standard_srv"] = standard_srv

    @builtins.property
    def private(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: connectionStrings#Private
        '''
        result = self._values.get("private")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_srv(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: connectionStrings#PrivateSrv
        '''
        result = self._values.get("private_srv")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def standard(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: connectionStrings#Standard
        '''
        result = self._values.get("standard")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def standard_srv(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: connectionStrings#StandardSrv
        '''
        result = self._values.get("standard_srv")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionStrings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.RegionsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "analytics_nodes": "analyticsNodes",
        "electable_nodes": "electableNodes",
        "priority": "priority",
        "read_only_nodes": "readOnlyNodes",
        "region_name": "regionName",
    },
)
class RegionsConfig:
    def __init__(
        self,
        *,
        analytics_nodes: typing.Optional[jsii.Number] = None,
        electable_nodes: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        read_only_nodes: typing.Optional[jsii.Number] = None,
        region_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param analytics_nodes: 
        :param electable_nodes: 
        :param priority: 
        :param read_only_nodes: 
        :param region_name: 

        :stability: deprecated
        :schema: regionsConfig
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f192b891e65d818f455bd795680b4dc06e2f68072b38fe28dae702860676da3)
            check_type(argname="argument analytics_nodes", value=analytics_nodes, expected_type=type_hints["analytics_nodes"])
            check_type(argname="argument electable_nodes", value=electable_nodes, expected_type=type_hints["electable_nodes"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument read_only_nodes", value=read_only_nodes, expected_type=type_hints["read_only_nodes"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if analytics_nodes is not None:
            self._values["analytics_nodes"] = analytics_nodes
        if electable_nodes is not None:
            self._values["electable_nodes"] = electable_nodes
        if priority is not None:
            self._values["priority"] = priority
        if read_only_nodes is not None:
            self._values["read_only_nodes"] = read_only_nodes
        if region_name is not None:
            self._values["region_name"] = region_name

    @builtins.property
    def analytics_nodes(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: deprecated
        :schema: regionsConfig#AnalyticsNodes
        '''
        result = self._values.get("analytics_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def electable_nodes(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: deprecated
        :schema: regionsConfig#ElectableNodes
        '''
        result = self._values.get("electable_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: deprecated
        :schema: regionsConfig#Priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only_nodes(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: deprecated
        :schema: regionsConfig#ReadOnlyNodes
        '''
        result = self._values.get("read_only_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: regionsConfig#RegionName
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdk-cloudformation/mongodb-atlas-cluster.ReplicationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "num_shards": "numShards",
        "regions_config": "regionsConfig",
        "zone_name": "zoneName",
    },
)
class ReplicationSpec:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        num_shards: typing.Optional[jsii.Number] = None,
        regions_config: typing.Optional[typing.Sequence[typing.Union[RegionsConfig, typing.Dict[builtins.str, typing.Any]]]] = None,
        zone_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: 
        :param num_shards: 
        :param regions_config: 
        :param zone_name: 

        :stability: deprecated
        :schema: replicationSpec
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea95b6a6ef3bf011fc511f6108951fa0d0b0b28a959b2fa589cb7a277b7c4ac3)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument num_shards", value=num_shards, expected_type=type_hints["num_shards"])
            check_type(argname="argument regions_config", value=regions_config, expected_type=type_hints["regions_config"])
            check_type(argname="argument zone_name", value=zone_name, expected_type=type_hints["zone_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if num_shards is not None:
            self._values["num_shards"] = num_shards
        if regions_config is not None:
            self._values["regions_config"] = regions_config
        if zone_name is not None:
            self._values["zone_name"] = zone_name

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: replicationSpec#ID
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_shards(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: deprecated
        :schema: replicationSpec#NumShards
        '''
        result = self._values.get("num_shards")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def regions_config(self) -> typing.Optional[typing.List[RegionsConfig]]:
        '''
        :stability: deprecated
        :schema: replicationSpec#RegionsConfig
        '''
        result = self._values.get("regions_config")
        return typing.cast(typing.Optional[typing.List[RegionsConfig]], result)

    @builtins.property
    def zone_name(self) -> typing.Optional[builtins.str]:
        '''
        :stability: deprecated
        :schema: replicationSpec#ZoneName
        '''
        result = self._values.get("zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiKeyDefinition",
    "AutoScaling",
    "CfnCluster",
    "CfnClusterProps",
    "CfnClusterPropsBiConnector",
    "CfnClusterPropsEncryptionAtRestProvider",
    "CfnClusterPropsLabels",
    "CfnClusterPropsProviderSettings",
    "Compute",
    "ConnectionStrings",
    "RegionsConfig",
    "ReplicationSpec",
]

publication.publish()

def _typecheckingstub__c610eab3e37e1b54bc5c58cc8f3f7f672e3bd33562a644c16288b0da81f83243(
    *,
    private_key: typing.Optional[builtins.str] = None,
    public_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d08d58e7f17a943d2ae36fe2932bd72f1d98ee746e2912fa5b54f97142dd9a5(
    *,
    compute: typing.Optional[typing.Union[Compute, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_gb_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97dc4a2e5f9988afb37c42f7f66883b9617709641c4d692f282a7fffcf52d9e0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_scaling: typing.Optional[typing.Union[AutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    backup_enabled: typing.Optional[builtins.bool] = None,
    bi_connector: typing.Optional[typing.Union[CfnClusterPropsBiConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_type: typing.Optional[builtins.str] = None,
    connection_strings: typing.Optional[typing.Union[ConnectionStrings, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    encryption_at_rest_provider: typing.Optional[CfnClusterPropsEncryptionAtRestProvider] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[CfnClusterPropsLabels, typing.Dict[builtins.str, typing.Any]]]] = None,
    mongo_db_major_version: typing.Optional[builtins.str] = None,
    num_shards: typing.Optional[jsii.Number] = None,
    pit_enabled: typing.Optional[builtins.bool] = None,
    project_id: typing.Optional[builtins.str] = None,
    provider_backup_enabled: typing.Optional[builtins.bool] = None,
    provider_settings: typing.Optional[typing.Union[CfnClusterPropsProviderSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    replication_factor: typing.Optional[jsii.Number] = None,
    replication_specs: typing.Optional[typing.Sequence[typing.Union[ReplicationSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c94d3cd97aac74155001fe1b47254ebc6c92fbd18fb2481f740ae3decbe0ad(
    *,
    name: builtins.str,
    api_keys: typing.Optional[typing.Union[ApiKeyDefinition, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_scaling: typing.Optional[typing.Union[AutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    backup_enabled: typing.Optional[builtins.bool] = None,
    bi_connector: typing.Optional[typing.Union[CfnClusterPropsBiConnector, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_type: typing.Optional[builtins.str] = None,
    connection_strings: typing.Optional[typing.Union[ConnectionStrings, typing.Dict[builtins.str, typing.Any]]] = None,
    disk_size_gb: typing.Optional[jsii.Number] = None,
    encryption_at_rest_provider: typing.Optional[CfnClusterPropsEncryptionAtRestProvider] = None,
    labels: typing.Optional[typing.Sequence[typing.Union[CfnClusterPropsLabels, typing.Dict[builtins.str, typing.Any]]]] = None,
    mongo_db_major_version: typing.Optional[builtins.str] = None,
    num_shards: typing.Optional[jsii.Number] = None,
    pit_enabled: typing.Optional[builtins.bool] = None,
    project_id: typing.Optional[builtins.str] = None,
    provider_backup_enabled: typing.Optional[builtins.bool] = None,
    provider_settings: typing.Optional[typing.Union[CfnClusterPropsProviderSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    replication_factor: typing.Optional[jsii.Number] = None,
    replication_specs: typing.Optional[typing.Sequence[typing.Union[ReplicationSpec, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__204a702f272ef0e8ba699cbedf3b81209053d42f8edbe0f25fa6b754c39cc60e(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    read_preference: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2855e69cfad720bc80619a3fad984f34f3c234bd0b6ee152a7b593fa934837c0(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__384db7d74549cd4fc5d8f7b385753dc73ed807edb95d7dca85c32330b9b672d6(
    *,
    auto_scaling: typing.Optional[typing.Union[AutoScaling, typing.Dict[builtins.str, typing.Any]]] = None,
    backing_provider_name: typing.Optional[builtins.str] = None,
    disk_iops: typing.Optional[jsii.Number] = None,
    encrypt_ebs_volume: typing.Optional[builtins.bool] = None,
    instance_size_name: typing.Optional[builtins.str] = None,
    provider_name: typing.Optional[builtins.str] = None,
    region_name: typing.Optional[builtins.str] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a9c3b96f232883fd2f5a4b4b7d1c7cbd90961fb4bdc801c5af8b6ae4873216(
    *,
    enabled: typing.Optional[builtins.bool] = None,
    max_instance_size: typing.Optional[builtins.str] = None,
    min_instance_size: typing.Optional[builtins.str] = None,
    scale_down_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ff19860da47aafff9faa188554a5f58300431b561f1797400a01d3ee0d91d2(
    *,
    private: typing.Optional[builtins.str] = None,
    private_srv: typing.Optional[builtins.str] = None,
    standard: typing.Optional[builtins.str] = None,
    standard_srv: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f192b891e65d818f455bd795680b4dc06e2f68072b38fe28dae702860676da3(
    *,
    analytics_nodes: typing.Optional[jsii.Number] = None,
    electable_nodes: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    read_only_nodes: typing.Optional[jsii.Number] = None,
    region_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea95b6a6ef3bf011fc511f6108951fa0d0b0b28a959b2fa589cb7a277b7c4ac3(
    *,
    id: typing.Optional[builtins.str] = None,
    num_shards: typing.Optional[jsii.Number] = None,
    regions_config: typing.Optional[typing.Sequence[typing.Union[RegionsConfig, typing.Dict[builtins.str, typing.Any]]]] = None,
    zone_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
