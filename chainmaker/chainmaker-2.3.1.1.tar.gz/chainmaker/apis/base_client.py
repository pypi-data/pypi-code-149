#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   base_client.py
# @Function     :   ChainMaker链客户端基类

import logging
from pathlib import Path
from typing import List, Union, Callable, Dict

from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import ec, rsa

from chainmaker.client_node import ClientNode
from chainmaker.client_user import ClientUser
from chainmaker.conn_pool import ConnectionPool
from chainmaker.keys import (AuthType, RuntimeType, AddrType, RechargeGasItem, ConsensusType, ResourceName)
from chainmaker.payload import PayloadBuilder
from chainmaker.protos import (Policy, RpcNodeStub, BlockHeader, BlockInfo, Contract, Payload, TxRequest,
                               EndorsementEntry,
                               TxResponse, Result, TransactionWithRWSet, TransactionInfo, ChainConfig, ChainList,
                               ChainInfo, BlockWithRWSet, MultiSignInfo)
from chainmaker.protos.common.result_pb2 import AliasInfos, PrivateGetContract, CertInfos
from chainmaker.protos.config.chain_config_pb2 import ResourcePolicy
from chainmaker.protos.syscontract.dpos_stake_pb2 import ValidatorVector, Delegation, DelegationInfo, Epoch
from chainmaker.sdk_config import DefaultConfig, ArchiveConfig, RpcClientConfig, Pkcs11Config


class BaseClient(object):
    # common config 常规配置
    chain_id: str  # 链id
    user: ClientUser
    nodes: List[ClientNode]
    node_cnt: int

    _conn_node: int

    _logger: logging.Logger  # 日志对象
    _poll: ConnectionPool  # 连接池
    _payload_builder: PayloadBuilder

    # archive config 归档配置
    _archive_config: ArchiveConfig
    # rpc客户端配置
    _rpc_client_config: RpcClientConfig
    _pkcs11_config: Pkcs11Config

    # additional 额外部分(在go-sdk之上增加的部分控制属性)
    _timeout: int  # rpc call 超时时间，请求超时太短会导致Deadline Exceeded
    _with_sync_result: bool  # 是否同步获取交易结果
    _tx_check_interval: int  # 交易轮询间隔
    _tx_check_timeout: int  # 交易轮询超时时间
    # retry config 重试配置
    _retry_limit: int  # rpc重试次数, 默认为5
    _retry_interval: int  # rpc重试间隔, 默认为0.5s
    _default_gas_limit: int  # 默认gas_limit值

    endorsers: List[ClientUser]  # 默认背书用户列表

    # 动态属性
    org_id: str  # 组织id
    hash_type: str  # 用户密钥/证书哈希类型，默认为 SHA256
    auth_type: AuthType  # 权限类型，默认为 AuthType.PermissionedWithCert
    sender_address: str  # 用户账户地址地址

    user_crt_bytes: bytes  # 用户PEM证书二进制内容  # todo remove
    user_crt: x509.Certificate  # 用户证书对象     # todo remove
    private_key: Union[ec.EllipticCurvePrivateKey, rsa.RSAPrivateKey]  # 用户私钥  # todo remove
    public_key: Union[ec.EllipticCurvePublicKey, rsa.RSAPublicKey]  # 用户公钥对象  # todo remove
    public_bytes: bytes  # 用户公钥二进制  # todo remove

    # cert_or_cert_bytes hash config  证书哈希配置
    enabled_cert_hash: bool = DefaultConfig.enable_cert_hash  # 是否以启用证书哈希
    # user_crt_hash: bytes = b''  # 对应的user.sign_cert_hash     # todo remove
    cert_hash: str
    cert_hash_bytes: bytes

    # cert_or_cert_bytes alias config 证书别名配置
    # enabled_alias: bool = DefaultConfig.enable_alias  # 是否已启用证书别名
    alias: str = None  # 用户证书别名  # todo remove

    # default TimestampKey , true NormalKey support
    enable_normal_key: bool

    _create_chain_config_manage_payload: Callable
    _create_cert_manage_payload: Callable

    def _debug(self, msg: str, *args):
        self._logger.debug('[Sdk] %s' % msg, *args)

    def _info(self, msg: str, *args):
        self._logger.info('[Sdk] %s' % msg, *args)

    def _error(self, msg: str, *args):
        self._logger.error('[Sdk] %s' % msg, *args)

    def _get_client(self, conn_node: int = None) -> RpcNodeStub:
        ...

    def _generate_tx_request(self, payload: Payload) -> TxRequest:
        """
        生成交易请求
        :param payload:
        :return:
        """

    def get_sync_result(self, tx_id: str, retry_limit: int = None, retry_timeout: int = None,
                        retry_interval: int = None) -> Result:
        """
        轮询获取交易结果
        :param retry_interval:
        :param retry_limit:
        :param retry_timeout:
        :param tx_id: 交易ID
        :return: 交易结果
        """

    def send_request(self, payload: Payload, endorsers: List[EndorsementEntry] = None,
                     timeout: int = None) -> TxResponse:
        """
        发送请求
        :param payload:
        :param endorsers:
        :param timeout:
        :return:
        """

    def send_request_with_sync_result(self, payload: Payload, endorsers: List[EndorsementEntry] = None,
                                      timeout: int = None,
                                      with_sync_result: bool = True) -> TxResponse:
        """
        发送请求并执行轮询交易结果
        :param payload: 请求数据
        :param timeout: 超时时间
        :param with_sync_result: 是否同步获取交易结果，默认为False
        :param endorsers: 背书配置
        :return: 响应对象
        :raise: RequestError
        :raise: TimeoutError
        """

    def send_manage_request(self, payload, endorsers: List[ClientUser] = None, timeout: int = None,
                            with_sync_result: bool = True) -> TxResponse:
        """
        发送管理(带背书)请求
        :param payload: 待签名payload
        :param endorsers: 背书用户
        :param timeout: 超时时间
        :param with_sync_result: 是否同步查询交易结果
        :return: 交易响应
        """

    # 0-链配置 ----------------------------------------------------------------------------------------------------------
    # 00-00 获取链配置
    def get_chain_config(self) -> ChainConfig:
        """
        获取链配置
        <00-00-CHAIN_CONFIG-GET_CHAIN_CONFIG>
        :return: ChainConfig
        :raises RequestError: 请求失败
        """

    # 00-01 通过指定区块高度查询最近链配置
    def get_chain_config_by_block_height(self, block_height: int) -> ChainConfig:
        """
        通过指定区块高度查询最近链配置
        如果当前区块就是配置块，直接返回当前区块的链配置
        <00-01-CHAIN_CONFIG-GET_CHAIN_CONFIG_AT>
        :param block_height: 块高
        :return: ChainConfig
        :raises RequestError: 请求失败
        """

    # 00-02 创建链配置Core配置更新待签名Payload
    def create_chain_config_core_update_payload(self, tx_scheduler_timeout: int = None,
                                                tx_scheduler_validate_timeout: int = None) -> Payload:
        """
        创建链配置Core配置更新待签名Payload
        <00-02-CHAIN_CONFIG-CORE_UPDATE>
        :param tx_scheduler_timeout: 交易调度器从交易池拿到交易后, 进行调度的时间，其值范围为[0, 60]，若无需修改，请置为-1
        :param tx_scheduler_validate_timeout: 交易调度器从区块中拿到交易后, 进行验证的超时时间，其值范围为[0, 60]，若无需修改，请置为-1
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-03 创建链配置区块配置更新待签名Payload
    def create_chain_config_block_update_payload(self, tx_timestamp_verify: bool = None, tx_timeout: int = None,
                                                 block_tx_capacity: int = None, block_size: int = None,
                                                 block_interval: int = None, tx_parameter_size=None) -> Payload:
        """
        创建链配置区块配置更新待签名Payload
        <00-03-CHAIN_CONFIG-BLOCK_UPDATE>
        :param tx_timestamp_verify: 是否需要开启交易时间戳校验
        :param tx_timeout: 交易时间戳的过期时间(秒)，其值范围为[600, +∞)（若无需修改，请置为-1）
        :param block_tx_capacity: 区块中最大交易数，其值范围为(0, +∞]（若无需修改，请置为-1）
        :param block_size: 区块最大限制，单位MB，其值范围为(0, +∞]（若无需修改，请置为-1）
        :param block_interval: 出块间隔，单位:ms，其值范围为[10, +∞]（若无需修改，请置为-1）
        :param tx_parameter_size: 交易参数大小
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-04 创建信任组织根证书添加待签名Payload
    def create_chain_config_trust_root_add_payload(self, trust_root_org_id: str,
                                                   trust_root_crts: List[str]) -> Payload:
        """
        创建信任组织根证书添加待签名Payload
         <00-04-CHAIN_CONFIG-TRUST_ROOT_ADD>
        :param str trust_root_org_id: 组织Id  eg. 'wx-or5.chainmaker.org'
        :param List[str] trust_root_crts: 根证书文件内容列表
           eg. [open('./testdata/crypto-config/wx-org5.chainmaker.org/ca/ca.crt').read()]
        :return: 待签名Payload
        :raises RequestError: 无效参数
        """

    # 00-05 创建信任组织根证书更新待签名Payload
    def create_chain_config_trust_root_update_payload(self, trust_root_org_id: str,
                                                      trust_root_crts: List[str]) -> Payload:
        """
        创建信任组织根证书更新待签名Payload
         <00-05-CHAIN_CONFIG-TRUST_ROOT_UPDATE>
        :param str trust_root_org_id: 组织Id
        :param List[str] trust_root_crts: 根证书内容列表
        :return: 待签名Payload
        :raises RequestError: 无效参数
        """

    # 00-06 创建信任组织根证书删除待签名Payload
    def create_chain_config_trust_root_delete_payload(self, org_id: str) -> Payload:
        """
        创建信任组织根证书删除待签名Payload
        <00-06-CHAIN_CONFIG-TRUST_ROOT_DELETE>
        :param org_id: 组织Id
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-07 创建链配置节点地址添加待签名Payload
    def create_chain_config_node_addr_add_payload(self, org_id: str, node_addrs: List[str]) -> Payload:
        """
        创建链配置节点地址添加待签名Payload
        <00-07-CHAIN_CONFIG-NODE_ADDR_ADD>
        :param org_id: 节点组织Id
        :param node_addrs: 节点地址列表
        :return: 待签名Payload
        """

    # 00-08 创建链配置节点地址更新待签名Payload
    def create_chain_config_node_addr_update_payload(self, org_id: str, node_old_addr: str,
                                                     node_new_addr: str) -> Payload:  # todo
        """
        创建链配置节点地址更新待签名Payload
        <00-08-CHAIN_CONFIG-NODE_ADDR_UPDATE>
        :param org_id: 节点组织Id
        :param node_old_addr: 原节点地址
        :param node_new_addr: 新节点地址
        :return: 待签名Payload
        """

    # 00-09 创建链配置节点地址删除待签名Payload
    def create_chain_config_node_addr_delete_payload(self, org_id: str, node_addr: str) -> Payload:  # todo
        """
        创建链配置节点地址删除待签名Payload
        <00-09-CHAIN_CONFIG-NODE_ADDR_DELETE>
        :param org_id: 节点组织Id
        :param node_addr: 节点地址
        :return: 待签名Payload
        """

    # 00-10 创建链配置共识组织添加待签名Payload
    def create_chain_config_consensus_node_org_add_payload(self, node_org_id: str,
                                                           node_ids: List[str]) -> Payload:
        """
        创建链配置共识组织添加待签名Payload
        <00-10-CHAIN_CONFIG-NODE_ORG_ADD>
        :param node_org_id: 节点组织Id
        :param node_ids: 节点Id
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-11 创建链配置共识节点更新待签名Payload
    def create_chain_config_consensus_node_org_update_payload(self, node_org_id: str,
                                                              node_ids: List[str]) -> Payload:
        """
        创建链配置共识节点更新待签名Payload
        <00-11-CHAIN_CONFIG-NODE_ORG_UPDATE>
        :param node_org_id: 节点组织Id
        :param node_ids: 节点Id
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-12 创建链配置共识节点删除待签名Payload
    def create_chain_config_consensus_node_org_delete_payload(self, node_org_id: str) -> Payload:
        """
        创建链配置共识节点删除待签名Payload
        <00-12-CHAIN_CONFIG-NODE_ORG_DELETE>
        :param node_org_id: 节点组织Id
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-13 创建链配置共识扩展参数添加待签名Payload
    def create_chain_config_consensus_ext_add_payload(self, params: dict) -> Payload:
        """
        创建链配置共识扩展参数添加待签名Payload
        <00-13-CHAIN_CONFIG-CONSENSUS_EXT_ADD>
        :param params: 字段key、value对
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-14 创建链配置共识扩展参数更新待签名Payload
    def create_chain_config_consensus_ext_update_payload(self, params: dict) -> Payload:
        """
        创建链配置共识扩展参数更新待签名Payload
        <00-14-CHAIN_CONFIG-CONSENSUS_EXT_UPDATE>
        :param params: 字段key、value对
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-15 创建链配置删除共识扩展参数删除待签名Payload
    def create_chain_config_consensus_ext_delete_payload(self, keys: List[str]) -> Payload:
        """
        创建链配置删除共识扩展参数删除待签名Payload
        <00-15-CHAIN_CONFIG-CONSENSUS_EXT_DELETE>
        :param keys: 待删除字段
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-16 创建链配置权限配置添加待签名Payload
    def create_chain_config_permission_add_payload(self, permission_resource_name: Union[ResourceName, str],
                                                   policy: Policy) -> Payload:
        """
        创建链配置权限配置添加待签名Payload
        <00-16-CHAIN_CONFIG-PERMISSION_ADD>
        :param permission_resource_name: 权限名
        :param policy: 权限规则
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-17 创建链配置权限配置更新待签名Payload
    def create_chain_config_permission_update_payload(self, permission_resource_name: Union[ResourceName, str],
                                                      policy: Policy) -> Payload:  # todo policy->dict
        """
        创建链配置权限配置更新待签名Payload
        <00-17-CHAIN_CONFIG-PERMISSION_UPDATE>
        :param permission_resource_name: 权限名
        :param policy: 权限规则
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-18 创建权限配置删除待签名Payload
    def create_chain_config_permission_delete_payload(self,
                                                      permission_resource_name: Union[ResourceName, str]) -> Payload:
        """
        创建权限配置删除待签名Payload
        <00-18-CHAIN_CONFIG-PERMISSION_DELETE>
        :param permission_resource_name: 权限名
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-19 创建链配置共识节点Id添加待签名Payload
    def create_chain_config_consensus_node_id_add_payload(self, org_id: str, node_ids: List[str]) -> Payload:
        """
        创建链配置共识节点Id添加待签名Payload
        <00-19-CHAIN_CONFIG-NODE_ID_ADD>
        :param org_id: 节点组织Id eg. 'wx-org5.chainmaker.org'
        :param node_ids: 节点Id列表 eg. ['QmcQHCuAXaFkbcsPUj7e37hXXfZ9DdN7bozseo5oX4qiC4']
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-20 创建链配置共识节点Id更新待签名Payload
    def create_chain_config_consensus_node_id_update_payload(self, org_id: str, node_old_id: str,
                                                             node_new_id: str) -> Payload:
        """
        创建链配置共识节点Id更新待签名Payload
        <00-20-CHAIN_CONFIG-NODE_ID_UPDATE>
        :param org_id: 节点组织Id
        :param node_old_id: 节点原Id
        :param node_new_id: 节点新Id
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-22 创建链配置信任三方添加待签名Payload
    def create_chain_config_trust_member_add_payload(self, trust_member_org_id: str, trust_member_node_id: str,
                                                     trust_member_info: str, trust_member_role: str,
                                                     ) -> Payload:
        """
        创建链配置信任三方添加待签名Payload
         <00-22-CHAIN_CONFIG-TRUST_MEMBER_ADD>
        :param trust_member_org_id: 组织Id
        :param trust_member_node_id: 节点ID
        :param trust_member_info: 节点信息
        :param trust_member_role: 节点角色
        :return: 待签名Payload
        :raises InvalidParametersError: 无效参数
        """

    # 00-21 创建链配置共识节点Id删除待签名Payload
    def create_chain_config_consensus_node_id_delete_payload(self, node_org_id: str,
                                                             node_id: str) -> Payload:
        """
        创建链配置共识节点Id删除待签名Payload
         <00-21-CHAIN_CONFIG-NODE_ID_DELETE>
        :param node_org_id: 节点组织Id
        :param node_id: 节点Id
        :return: request_pb2.SystemContractPayload
        :raises InvalidParametersError: 无效参数
        """

    # 00-23 创建链配置信任三方更新待签名Payload
    def create_chain_config_trust_member_update_payload(self, trust_member_org_id: str, trust_member_node_id: str,
                                                        trust_member_info: str, trust_member_role: str,
                                                        ) -> Payload:
        """
        创建链配置信任三方更新待签名Payload
         <00-23-CHAIN_CONFIG-TRUST_MEMBER_UPDATE>
        :param trust_member_org_id: 组织Id
        :param trust_member_node_id: 节点ID
        :param trust_member_info: 节点信息
        :param trust_member_role: 节点角色
        :return: 待签名Payload
        :raises InvalidParametersError: 无效参数
        """

    # 00-24 创建链配置创建信任三方删除待签名Payload
    def create_chain_config_trust_member_delete_payload(self, trust_member_info: str) -> Payload:
        """
        创建链配置创建信任三方删除待签名Payload
         <00-24-CHAIN_CONFIG-TRUST_MEMBER_DELETE>
        :param trust_member_info: 节点证书信息
        :return: 待签名Payload
        :raises InvalidParametersError: 无效参数
        """

    # 00-25 创建链配置变更地址类型待签名Payload
    def create_chain_config_alter_addr_type_payload(self, addr_type: Union[AddrType, str, int]) -> Payload:
        """
        创建链配置变更地址类型待签名Payload
        <00-25-CHAIN_CONFIG-ALTER_ADDR_TYPE>
        :param addr_type: 地址类型
        :return: 待签名Payload
        """

    # 00-26 创建链配置切换启用禁用Gas待签名Payload
    def create_chain_config_enable_or_disable_gas_payload(self) -> Payload:
        """
        创建链配置切换启用禁用Gas待签名Payload
        <0026 CHAIN_CONFIG-ENABLE_OR_DISABLE_GAS>
        :return: 待签名Payload
        """

    # 00-27 创建链配置设置合约调用基础Gas消耗待签名Payload
    def create_chain_config_set_invoke_base_gas_payload(self, amount: int) -> Payload:
        """
        创建链配置设置合约调用基础Gas消耗待签名Payload
        <00-27 CHAIN_CONFIG-SET_INVOKE_BASE_GAS>
        :param amount: 设置待基础Gas消耗数量
        :return: 待签名Payload
        """

    # 00-28 创建链配置设置账户管理员Payload
    def create_chain_config_set_account_manager_admin_payload(self, address) -> Payload:
        """
        创建链配置设置账户管理员Payload
        <00-28 CHAIN_CONFIG-SET_ACCOUNT_MANAGER_ADMIN>
        :return: 待签名Payload
        """

    # 00-29 获取链配置权限列表
    def get_chain_config_permission_list(self) -> ResourcePolicy:
        """
        获取链配置权限列表
        <00-29-CHAIN_CONFIG-PERMISSION_LIST>
        :return: 权限列表
        """

    # 00-30 创建链配置版本更新待签名Payload
    def create_chain_config_update_version_payload(self, block_version: str) -> Payload:
        """
        创建链配置版本更新待签名Payload
        <00-30-CHAIN_CONFIG-UPDATE_VERSION>
        :return: 待签名Payload
        """

    # 00-31 创建链配置版本更新待签名Payload
    def create_chain_config_consensus_switch_payload(self, origin_consensus: Union[ConsensusType, str, int],
                                                     target_consensus: Union[ConsensusType, str, int],
                                                     ext_config: dict) -> Payload:
        """
        创建链配置版本更新待签名Payload
        <00-31-CHAIN_CONFIG-CONSENSUS_SWITCH>
        :param origin_consensus:
        :param target_consensus:
        :param ext_config:
        :return: 待签名Payload
        """

    # 00-32 创建链配置DPOS共识节点Id更新待签名Payload
    def create_chain_config_dpos_node_id_update_payload(self, node_ids: List[str]) -> Payload:
        """
        创建链配置DPOS共识节点Id更新待签名Payload
        <00-32-CHAIN_CONFIG-DPOS_NODE_ID_UPDATE>
        :param node_ids: 节点Id列表
        :return: 待签名Payload
        """

    def create_tbft_to_raft_payload(self, ext_config: dict) -> Payload:
        """
        生成链配置更新链配置版本Payload
        :return: 待签名Payload
        """

    def create_raft_to_tbft_payload(self, ext_config: dict) -> Payload:
        """
        生成链配置更新链配置版本Payload
        :return: 待签名Payload
        """

    def sign_chain_config_payload(self, payload_bytes: bytes) -> Payload:
        """
        对链配置的Payload进行签名
        如果当前区块就是配置块，直接返回当前区块的链配置
        :param payload_bytes: payload.SerializeToString() 序列化后的payload bytes数据
        :return: 签名的背书
        :raises
        """

    def send_chain_config_update_request(self, payload: Payload, endorsers: List[EndorsementEntry], timeout: int = None,
                                         with_sync_result: bool = None) -> TxResponse:
        """
        发送链配置更新请求
        :param payload: 待签名链配置更新请求Payload
        :param endorsers: 背书列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮交易结果
        :return: 交易响应信息
        """

    # 链查询 ------------------------------------------------------------------------------------------------------------

    # 01-00 通过交易Id获取交易所在区块信息
    def get_block_by_tx_id(self, tx_id: str, with_rw_set: bool = False) -> BlockInfo:
        """
        通过交易Id获取交易所在区块信息
        <01-00-CHAIN_QUERY-GET_BLOCK_BY_TX_ID>
        :param tx_id: 交易Id
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """

    # 01-01 通过交易Id获取交易信息
    def get_tx_by_tx_id(self, tx_id: str) -> TransactionInfo:
        """
        通过交易Id获取交易信息
        <01-01-CHAIN_QUERY-GET_TX_BY_TX_ID>
        :param tx_id: 交易Id，类型为字符串
        :return: Result
        :raises RequestError: 请求失败
        """

    # 01-02 通过区块高度获取区块信息
    def get_block_by_height(self, block_height: int, with_rw_set: bool = False) -> BlockInfo:
        """
        通过区块高度获取区块信息
        <01-02-CHAIN_QUERY-GET_BLOCK_BY_HEIGHT>
        :param block_height: 区块高度
        :param with_rw_set: 是否返回读写集数据, 默认不返回。
        :return: 区块信息BlockInfo对象
        :raises RequestError: 请求失败，块已归档是抛出ContractFile
        """

    # 01-03 获取链信息
    def get_chain_info(self) -> ChainInfo:
        """
        获取链信息
        <01-03-CHAIN_QUERY-GET_CHAIN_INFO>
        :return: ChainInfo
        :raises RequestError: 请求失败
        """

    def get_tx_with_rwset_by_tx_id(self, tx_id: str) -> TransactionWithRWSet:
        """
        通过交易Id获取带读写集交易信息
        :param tx_id: 交易Id，类型为字符串
        :return: Result
        :raises RequestError: 请求失败
        """

    # 01-04 获取最新的配置块
    def get_last_config_block(self, with_rw_set: bool = False) -> BlockInfo:
        """
        获取最新的配置块
        <01-04-CHAIN_QUERY-GET_LAST_CONFIG_BLOCK>
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """

    # 01-05 通过区块哈希获取区块信息
    def get_block_by_hash(self, block_hash: str, with_rw_set: bool = False) -> BlockInfo:
        """
        通过区块哈希获取区块信息
        <01-05-CHAIN_QUERY-GET_BLOCK_BY_HASH>
        :param block_hash: 区块Hash, 二进制hash.hex()值，
                           如果拿到的block_hash字符串是base64值, 需要用 base64.b64decode(block_hash).hex()
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """

    # 01-06 获取节点加入的链列表
    def get_node_chain_list(self) -> ChainList:
        """
        获取节点加入的链列表
        <01-06-CHAIN_QUERY-GET_NODE_CHAIN_LIST>
        :return: 链Id列表
        :raises RequestError: 请求失败
        """

    # 01-07 获取统治合约 不开放
    def get_governance_contract(self):
        """
        获取统治合约
        <01-07-CHAIN_QUERY-GET_GOVERNANCE_CONTRACT>
        :return:
        """

    # 01-08 通过区块高度获取带读写集区块信息
    def get_block_with_tx_rw_sets_by_height(self, block_height: int) -> BlockWithRWSet:
        """
        通过区块高度获取带读写集区块信息
        <01-08-CHAIN_QUERY-GET_BLOCK_WITH_TXRWSETS_BY_HEIGHT>
        :param block_height: 区块高度
        :return: 带读写集区块信息
        """

    # 01-09 通过区块哈希获取带读写集区块信息
    def get_block_with_tx_rw_sets_by_hash(self, block_hash: str) -> BlockWithRWSet:
        """
        通过区块哈希获取带读写集区块信息
         <01-09-CHAIN_QUERY-GET_BLOCK_WITH_TXRWSETS_BY_HASH>
        :param block_hash: 区块哈希
        :return: 带读写集区块信息
        """

    # 01-10 获取最新区块信息
    def get_last_block(self, with_rw_set: bool = False) -> BlockInfo:
        """
        获取最新区块信息
        <01-10-CHAIN_QUERY-GET_LAST_BLOCK>
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """

    # 01-11 通过区块高度获取完整区块信息
    def get_full_block_by_height(self, block_height: int) -> BlockWithRWSet:
        """
        通过区块高度获取完整区块信息
        <01-11-CHAIN_QUERY-GET_FULL_BLOCK_BY_HEIGHT>
        :param block_height: 区块高度
        :return: BlockInfo
        :raises RequestError: 请求失败
        """

    # 01-12 通过交易Id获取区块高度
    def get_block_height_by_tx_id(self, tx_id: str) -> int:
        """
        通过交易Id获取区块高度
        <01-12-CHAIN_QUERY-GET_BLOCK_HEIGHT_BY_TX_ID>
        :param tx_id: 交易Id
        :return: 区块高度
        :raises RequestError: 请求失败
        """

    # 01-13 通过区块哈希获取区块高度
    def get_block_height_by_hash(self, block_hash: str) -> int:
        """
        通过区块哈希获取区块高度
        <01-13-CHAIN_QUERY-GET_BLOCK_HEIGHT_BY_HASH>
        :param block_hash: 区块Hash 二进制hash.hex()值,
               如果拿到的block_hash字符串是base64值, 需要用 base64.b64decode(block_hash).hex()
        :return: 区块高度
        :raises RequestError: 请求失败
        """

    # 01-14 通过高度获取区块头
    def get_block_header_by_height(self, block_height: int) -> BlockHeader:
        """
        通过高度获取区块头
        <01-14-CHAIN_QUERY-GET_BLOCK_HEADER_BY_HEIGHT>
        :param block_height: 区块高度
        :return: 区块头
        """

    # 01-15 获取已归档的区块高度
    def get_archived_block_height(self) -> int:
        """
        获取已归档的区块高度
         <01-15-CHAIN_QUERY-GET_ARCHIVED_BLOCK_HEIGHT>
        :return: 区块高度
        :raises RequestError: 请求失败
        """

    # 01-16 获取全部合约信息 不开放
    def get_all_contracts(self) -> List[Contract]:
        """
        获取全部合约信息
        <01-16-CHAIN_QUERY-GET_ALL_CONTRACTS>
        :return: 合约Contract对象列表
        :raise: RequestError: 请求出错
        :raise: AssertionError: 响应code不为0,检查响应时抛出断言失败
        :raise: 当数据不是JSON格式时，抛出json.decoder.JSONDecodeError
        """

    # 01-17 通过交易Id获取Merkle树路径
    def get_merkle_path_by_tx_id(self, tx_id: str) -> bytes:
        """
        通过交易Id获取Merkle树路径
        <01-17-CHAIN_QUERY-GET_MERKLE_PATH_BY_TX_ID>
        :param tx_id: 交易Id
        :return: Merkle树路径
        """

    def get_block_height(self, tx_id: str = None, block_hash: str = None) -> int:  # todo
        """
        通过交易Id或区块hash获取区块高度
        :param tx_id: 交易Id
        :param block_hash: 区块hash
        :return: 区块高度
        """

    def get_current_block_height(self) -> int:
        """
        获取当前区块高度
        :return: 区块高度
        """

    # 2-证书管理 --------------------------------------------------------------------------------------------------------
    def enable_cert_hash(self):
        """启用证书hash，会修改实例的enabled_crt_hash值。默认为不启用。
        :raises OnChainFailedError: 证书上链失败
        :raises EndorsementInvalidError: 证书已删除
        """

    def disable_cert_hash(self):
        """
        关闭证书哈希(短证书)
        """

    def get_cert_hash_bytes(self) -> bytes:
        """
        返回用户的签名证书哈希
        :return: 证书hash-bytes值
        """

    def get_cert_hash(self, cert_bytes_or_file_path: Union[Path, str, bytes] = None) -> str:
        """
        返回用户的签名证书哈希
        :return: 证书hash-hex值
        """

    # 02-00 添加证书
    def add_cert(self, cert_hashes: List[str] = None, timeout: int = None,
                 with_sync_result: bool = None) -> TxResponse:
        """
        添加证书
        <02-00-CERT_MANAGE-CERT_ADD>
        :param cert_hashes: 证书哈希列表，为None时添加当前用户证书
        :param timeout: 设置请求超时时间
        :param with_sync_result: 同步返回请求结果
        :return: Response
        :raises RequestError: 请求失败
        """

    # 02-01 创建证书管理证书删除待签名Payload
    def create_cert_delete_payload(self, cert_hashes: Union[list, str] = None) -> TxResponse:
        """
        创建证书管理证书删除待签名Payload
         <02-01-CERT_MANAGE-CERTS_DELETE>
        :param cert_hashes: 证书hash列表, 每个证书hash应转为hex字符串, 为None时使用当前用户证书哈希
        :return: Payload
        """

    # 02-02 根据证书哈希查询证书
    def query_cert(self, cert_hashes: Union[list, str] = None, timeout: int = None) -> CertInfos:
        """
        根据证书哈希查询证书
        <02-02-CERT_MANAGE-CERTS_QUERY>
        :param cert_hashes: 证书hash列表(List)，每个证书hash应转为hex字符串, 为None时查询当前用户证书
        :param timeout: 请求超时时间
        :return: result_pb2.CertInfos
        :raises 查询不到证书抛出 RequestError
        """

    # 02-03 创建证书管理证书冻结待签名Payload
    def create_cert_freeze_payload(self, certs: List[str]) -> Payload:
        """
        创建证书管理证书冻结待签名Payload
        <02-03-CERT_MANAGE-CERTS_FREEZE>
        :param certs: 证书列表(List)，证书为证书文件读取后的字符串格式
        :return: Payload
        """

    # 02-04 创建证书管理证书解冻待签名Payload
    def create_cert_unfreeze_payload(self, certs: List[str]) -> Payload:
        """
        创建证书管理证书解冻待签名Payload
        <02-04-CERT_MANAGE-CERTS_UNFREEZE>
        :param certs: 证书列表，证书为证书文件读取后的字符串格式
        :return: Payload
        """

    # 02-05 创建证书管理证书吊销待签名Payload
    def create_cert_revoke_payload(self, cert_crl: str) -> Payload:
        """
        创建证书管理证书吊销待签名Payload
        <02-05-CERT_MANAGE-CERTS_REVOKE>
        :param cert_crl: 证书吊销列表 文件内容，字符串形式
        :return: Payload
        """

    @staticmethod
    def create_cert_crl(cert_bytes_or_file_path: Union[Path, str, bytes],
                        ca_key_bytes_or_file_path: Union[Path, str, bytes],
                        ca_crt_bytes_or_file_path: Union[Path, str, bytes]) -> str:
        """ 创建吊销证书列表文件二进制数据
        :param cert_bytes_or_file_path: 原客户端证书文件
               eg ./crypto-config/wx-org2.chainmaker.org/user_full_name/client1/client1.tls.crt'
        :param ca_key_bytes_or_file_path: 同组织根证书私钥文件
               eg. ./crypto-config/wx-org2.chainmaker.org/ca/ca.key
        :param ca_crt_bytes_or_file_path: 同组织跟证书文件
               eg. ./crypto-config/wx-org2.chainmaker.org/ca/ca.crt
        :return: 生成的crl文件二进制内容
        """

    def enable_alias(self, alias: str = None):
        """
        启用证书别名
        :return:
        """

    def check_alias(self, alias: str = None):  # 对应sdk-go getCheckAlias  
        """
        检查证书别名是否上链
        :return:
        """

    # 02-06 添加证书别名
    def add_alias(self, alias: str = None) -> Result:  # MemberType must be MemberType_CERT
        """
        添加证书别名
        <02-06-CERT_MANAGE-CERT_ALIAS_ADD>
        :return: 响应信息
        """

    # 02-07 创建通过别名更新证书待签名Payload
    def create_update_cert_by_alias_payload(self, alias: str, new_cert_pem: str) -> Payload:
        """
        创建通过别名更新证书待签名Payload
        <02-07-CERT_MANAGE-CERT_ALIAS_UPDATE>
        :param alias: 用户别名
        :param new_cert_pem: 新证书文件内容
        :return: 签名Payload
        """

    # 02-08 创建删除证书别名待签名Payload
    def create_delete_cert_alias_payload(self, aliases: List[str]) -> Payload:
        """
        创建删除证书别名待签名Payload
        <02-08-CERT_MANAGE-CERTS_ALIAS_DELETE>
        :param aliases: 证书别名列表
        :return: 待签名Payload
        """

    # 02-09 查询证书别名
    def query_cert_alias(self, aliases: List[str] = None) -> AliasInfos:
        """
        查询证书别名
        <02-09-CERT_MANAGE-CERTS_ALIAS_QUERY>
        :param aliases: 证书别名列表
        :return: 仅当所有别名存在时返回别名信息列表，否则返回None，建议单个别名查询
        """

    def sign_cert_manage_payload(self, payload_bytes: bytes) -> EndorsementEntry:
        """
        对证书管理的payload进行签名
        :param: 待签名payload
        :return: 背书条目
        """

    def send_cert_manage_request(self, payload: Payload, endorsers: List[EndorsementEntry] = None,
                                 timeout: int = None) -> TxResponse:
        """
        发送证书管理请求
        :param payload: 交易payload
        :param endorsers: 背书列表
        :param timeout: 超时时间
        :param with_sync_result: 是否同步交易执行结果。如果不同步，返回tx_id，供异步查询; 同步则循环等待，返回交易的执行结果。
        :return: Response
        :raises RequestError: 请求失败
            """

    # 4-多签 ------------------------------------------------------------------------------------------------------------
    def multi_sign_req(self, payload: Payload, timeout: int = None, with_sync_result: bool = False):
        """
        发起多签请求
        :param payload: 待签名payload
        :param timeout: 请求超时时间
        :param with_sync_result: 是否同步获取交易结果
        :return: 交易响应或交易信息
        """

    def multi_sign_contract_vote(self, multi_sign_req_payload, endorser: ClientUser, is_agree: bool = True,
                                 timeout: int = None, with_sync_result: bool = False) -> TxResponse:
        """
        对请求payload发起多签投票
        :param multi_sign_req_payload: 待签名payload
        :param endorser: 投票用户对象
        :param is_agree: 是否同意，true为同意，false则反对
        :param timeout: 请求超时时间
        :param with_sync_result: 是否同步获取交易结果
        :return: 交易响应或交易信息
        """

    def multi_sign_contract_vote_tx_id(self, tx_id, endorser: ClientUser, is_agree: bool,
                                       timeout: int = None, with_sync_result: bool = False) -> TxResponse:
        """
        对交易ID发起多签投票
        :param tx_id: 交易ID
        :param endorser: 投票用户对象
        :param is_agree: 是否同意，true为同意，false则反对
        :param timeout: 请求超时时间
        :param with_sync_result: 是否同步获取交易结果
        :return: 交易响应或交易信息
        """

    def multi_sign_contract_query(self, tx_id: str) -> MultiSignInfo:
        """
        根据交易ID查询多签状态
        :param tx_id: 交易ID
        :return: 多签信息
        """

    def create_multi_sign_req_payload(self, params: Union[list, dict]) -> Payload:
        """
        根据发起多签请求所需的参数构建payload
        :param params: 发起多签请求所需的参数
        :return: 待签名Payload
        """

    # 5-用户合约 --------------------------------------------------------------------------------------------------------
    # 05-00 创建创建用户合约待签名Payload
    def create_contract_create_payload(self, contract_name: str, version: str, byte_code_or_file_path: str,
                                       runtime_type: Union[RuntimeType, str],
                                       params: Dict[str, Union[str, int, bool]] = None,
                                       gas_limit: int = None, tx_id: str = None) -> Payload:
        """
        创建创建用户合约待签名Payload
        <05-00-CONTRACT_MANAGE-INIT_CONTRACT>
        :param contract_name: 合约名
        :param version: 合约版本
        :param byte_code_or_file_path: 合约字节码：可以是字节码；合约文件路径；或者 hex编码字符串；或者 base64编码字符串。
        :param runtime_type: contract_pb2.RuntimeType.WASMER
        :param params: 合约参数，dict类型，key 和 value 尽量为字符串
        :param gas_limit: Gas交易限制
        :param tx_id: 指定交易Id
        :return: 待签名Payload
        :raises ValueError: 如果 byte_code 不能转成合约字节码
        """

    # 05-01 创建升级用户合约待签名Payload
    def create_contract_upgrade_payload(self, contract_name: str, version: str, byte_code_or_file_path: str,
                                        runtime_type: Union[RuntimeType, str],
                                        params: dict = None, gas_limit: int = None, tx_id: str = None) -> Payload:
        """
        创建升级用户合约待签名Payload
        <05-01-CONTRACT_MANAGE-UPGRADE_CONTRACT>
        :param contract_name: 合约名
        :param version: 合约版本
        :param byte_code_or_file_path: 合约字节码：可以是字节码；合约文件路径；或者 hex编码字符串；或者 base64编码字符串。
        :param runtime_type: contract_pb2.RuntimeType.WASMER
            eg. 'INVALID', 'NATIVE', 'WASMER', 'WXVM', 'GASM', 'EVM', 'DOCKER_GO', 'DOCKER_JAVA'
        :param params: 合约参数，dict类型，key 和 value 尽量为字符串
        :param gas_limit: Gas交易限制
        :param tx_id: 指定交易Id
        :return: 待签名Payload
        :raises ValueError: 如果 byte_code 不能转成合约字节码
        """

    # 05-02 创建冻结合约待签名Payload
    def create_contract_freeze_payload(self, contract_name: str, tx_id: str = None) -> Payload:
        """
        创建冻结合约待签名Payload
        <05-02-CONTRACT_MANAGE-FREEZE_CONTRACT>
        :param contract_name: 合约名
        :param tx_id: 指定交易Id
        :return: 待签名Payload
        """

    # 05-03 创建解冻合约待签名Payload
    def create_contract_unfreeze_payload(self, contract_name: str, tx_id: str = None) -> Payload:
        """
        创建解冻合约待签名Payload
        <05-03-CONTRACT_MANAGE-UNFREEZE_CONTRACT>
        :param contract_name: 合约名
        :param tx_id: 指定交易Id
        :return: 待签名Payload
        """

    # 05-04 创建吊销合约待签名Payload
    def create_contract_revoke_payload(self, contract_name: str, tx_id: str = None) -> Payload:
        """
        创建吊销合约待签名Payload
        <05-04-CONTRACT_MANAGE-REVOKE_CONTRACT>
        :param contract_name: 合约名
        :param tx_id: 指定交易Id
        :return: 待签名Payload
        """

    def invoke_contract(self, contract_name: str, method: str, params: dict = None, tx_id: str = None,
                        gas_limit: int = None, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        调用合约
        :param contract_name: 合约名
        :param method: 调用合约方法名
        :param params: 调用参数，参数类型为dict
        :param tx_id: 交易id，如果交易id为空/空字符串，则创建新的tx_id
        :param gas_limit: 交易Gas限制
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步交易执行结果。如果不同步，返回tx_id，供异步查询; 同步则循环等待，返回交易的执行结果。
        :return: TxResponse
        :raises RequestError: 请求失败
        """

    def invoke_contract_with_limit(self, contract_name: str, method: str, params: dict = None, tx_id: str = None,
                                   timeout: int = None,
                                   with_sync_result: bool = None,
                                   gas_limit: int = None) -> TxResponse:  # todo remove
        """
        带Gas限制调用合约
        :param contract_name: 合约名
        :param method: 调用合约方法名
        :param params: 调用参数，参数类型为dict
        :param tx_id: 交易id，如果交易id为空/空字符串，则创建新的tx_id
        :param timeout: 超时时间，默认为 3s
        :param with_sync_result: 是否同步交易执行结果。如果不同步，返回tx_id，供异步查询; 同步则循环等待，返回交易的执行结果。
        :param gas_limit: Gas交易限制
        :return: TxResponse
        :raises RequestError: 请求失败
        """

    def query_contract(self, contract_name: str, method: str, params: Union[dict, list] = None,
                       timeout: int = None) -> TxResponse:
        """
        查询用户合约
        :param contract_name: 合约名
        :param method: 调用合约方法名
        :param params: 调用参数，参数类型为dict
        :param timeout: 超时时间，默认为 3s
        :return: TxResponse, 结果不存在时返回None
        :raises RequestError: 请求失败
        """

    def sign_contract_manage_payload(self, payload: Payload) -> bytes:
        """对 合约管理的 payload 字节数组进行签名，返回签名后待签名Payload字节数组
        :param payload: 交易 payload
        :return: 待签名Payload 的字节数组
        :raises DecodeError: 如果 byte_code 解码失败
        """

    def send_contract_manage_request(self, payload: Payload, endorsers: List[EndorsementEntry], timeout: int = None,
                                     with_sync_result: bool = None) -> TxResponse:
        """发送合约管理的请求
        :param endorsers: 背书列表
        :param payload: 请求的 payload
        :param timeout: 超时时间
        :param with_sync_result: 是否同步交易执行结果。如果不同步，返回tx_id，供异步查询; 同步则循环等待，返回交易的执行结果。
        :return: TxResponse
        :raises RequestError: 请求失败
        """

    def get_tx_request(self, contract_name: str, method: str, params: Union[dict, list] = None,
                       tx_id: str = None) -> TxRequest:
        """
        获取交易请求体
        :param contract_name: 合约名
        :param method: 调用合约方法名
        :param params: 调用参数，参数类型为dict
        :param tx_id: 交易id，如果交易id为空/空字符串，则创建新的tx_id
        :return: Request
        """

    def send_tx_request(self, tx_request, timeout=None, with_sync_result=None) -> TxResponse:
        """发送请求
        :param tx_request: 请求体
        :param timeout: 超时时间
        :param with_sync_result: 是否同步交易执行结果。如果不同步，返回tx_id，供异步查询; 同步则循环等待，返回交易的执行结果。
        :return: Response
        :raises RequestError: 请求失败
        """

    def invoke_system_contract(self, contract_name: str, method: str,
                               params: Dict[str, Union[str, int, bool]] = None,
                               tx_id: str = None, gas_limit: int = None,
                               timeout: int = None, with_sync_result: bool = False) -> TxResponse:
        """
        调用系统合约
        :param contract_name: 系统合约名称
        :param method: 系统合约方法
        :param params: 系统合约方法所需的参数
        :param tx_id: 指定交易Id，默认为空是生成随机交易Id
        :param gas_limit: Gas交易限制
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应信息
        """

    def query_system_contract(self, contract_name: str, method: str,
                              params: Dict[str, Union[str, int, bool]] = None,
                              tx_id: str = None, timeout: int = None) -> TxResponse:
        """
        查询系统合约
        :param contract_name: 系统合约名称
        :param method: 系统合约方法
        :param params: 系统合约方法所需的参数
        :param tx_id: 指定交易Id，默认为空是生成随机交易Id
        :param timeout: RPC请求超时时间
        :return: 交易响应信息
        """

    # 05-05 生成系统合约授权访问待签名Payload
    def create_native_contract_access_grant_payload(self, grant_contract_list: List[str]) -> Payload:
        """
        生成系统合约授权访问待签名Payload
        <05-05-CONTRACT_MANAGE-GRANT_CONTRACT_ACCESS>
        :param List[str] grant_contract_list: 授予权限的访问系统合约名称列表 # TODO 确认 合约状态必须是FROZEN
        :return: 待签名Payload
        """

    # 05-06 生成原生合约吊销授权访问待签名Payload
    def create_native_contract_access_revoke_payload(self, revoke_contract_list: List[str]) -> Payload:
        """
        生成原生合约吊销授权访问待签名Payload
        <05-06-CONTRACT_MANAGE-REVOKE_CONTRACT_ACCESS>
        :param revoke_contract_list: 吊销授予权限的访问合约列表
        :return: 待签名Payload
        """

    # 05-07 生成原生合约验证授权访问待签名Payload
    def create_native_contract_access_verify_payload(self, contract_list: List[str]) -> Payload:
        """
        生成原生合约验证授权访问待签名Payload
        <05-07-CONTRACT_MANAGE-VERIFY_CONTRACT_ACCESS>
        :param contract_list: 验证授予权限的访问合约列表
        :return: 待签名Payload
        """

    # 05-08 创建创建新系统合约待签名Payload
    def create_init_new_native_contract_payload(self, contract_name: str, version: str,
                                                byte_code_or_file_path: str,
                                                runtime_type: Union[RuntimeType, str],
                                                params: Dict[str, Union[str, int, bool]] = None,
                                                gas_limit: int = None, tx_id: str = None) -> Payload:  # todo
        """
        创建创建新系统合约待签名Payload
        <05-08-CONTRACT_MANAGE-INIT_NEW_NATIVE_CONTRACT>
        :param contract_name: 合约名
        :param version: 合约版本
        :param byte_code_or_file_path: 合约字节码：可以是字节码；合约文件路径；或者 hex编码字符串；或者 base64编码字符串。
        :param runtime_type: contract_pb2.RuntimeType.WASMER
        :param params: 合约参数，dict类型，key 和 value 尽量为字符串
        :param gas_limit: Gas交易限制
        :return: 待签名Payload
        :raises ValueError: 如果 byte_code 不能转成合约字节码
        """

    # 06-00 获取合约代码
    def get_contract(self, contract_name: str, code_hash: str) -> PrivateGetContract:
        """
        获取合约代码
        :param contract_name: 合约名称
        :param code_hash: 代码哈希
        :return: 隐私合约
        """

    # 06-01 获取隐私数据
    def get_data(self, contract_name: str, key: str) -> bytes:
        """
        获取隐私数据
        :param contract_name: 合约名称
        :param key: 键名
        :return: 键对应的数据
        """

    # 06-02 保存可信执行环境证书
    def save_enclave_ca_cert(self, enclave_ca_cert: str,
                             tx_id: str = None, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        保存可信执行环境根证书
        :param enclave_ca_cert: 可信执行环境根证书
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 交易响应
        """

    # 06-03 保存隐私数据目录
    def save_dir(self, order_id: str, private_dir: list,
                 tx_id: str = None, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        保存隐私数据目录
        :param order_id: 序号
        :param private_dir: 隐私数据目录
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 交易响应
        """

    # 06-04 保存隐私计算结果数据
    def save_data(self, contract_name: str, contract_version: str, is_deployment: bool, code_hash: bytes,
                  report_hash: bytes, result: dict,
                  code_header: bytes, rwset: dict, sign: bytes, events: list, private_req: bytes,
                  tx_id: str = None, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        保存隐私计算结果数据
        :param contract_name: 合约名称
        :param contract_version: 合约版本
        :param is_deployment: 是否部署
        :param code_hash:
        :param code_header:
        :param report_hash:
        :param result:
        :param events: 事件列表
        :param rwset: 读写集
        :param sign: 签名数据
        :param private_req:
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 交易响应
        """

    # 06-05 获取可信执行环境报告
    def save_enclave_report(self, enclave_id: str, report: str,
                            tx_id: str = None, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        获取可信执行环境报告
        :param enclave_id: 可信执行环境Id
        :param report: 报告数据
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 交易响应
        """

    # 06-06 获取可信执行环境证明
    def get_enclave_proof(self, enclave_id: str) -> bytes:
        """
        获取可信执行环境证明
        :param enclave_id: 可信执行环境Id
        :return:
        """

    # 06-07 获取可信执行环境证书
    def get_enclave_ca_cert(self) -> bytes:
        """
        获取可信执行环境证书
        :return: 证书二进制数据
        """

    # 06-08 获取隐私数据目录
    def get_dir(self, order_id: str) -> bytes:
        """
        获取隐私数据目录
        :param order_id: 序号
        :return: 数据目录二进制内容
        """

    # 06-09 检查调用者证书授权
    def check_caller_cert_auth(self, payload: str, org_ids: List[str], sign_pairs: dict) -> TxResponse:
        """
        检查调用者证书授权
        :param payload: 待签名Payload
        :param org_ids: 序号列表
        :param sign_pairs: 签名对
        :return: 交易响应
        """

    # 06-10 获取可信执行环境加密公钥
    def get_enclave_encrypt_pubkey(self, enclave_id: str) -> bytes:
        """
        获取可信执行环境加密公钥
        :param enclave_id: 可信执行环境Id
        :return: 公钥二进制数据
        """

    # 06-11 获取可信执行环境验证公钥
    def get_enclave_verification_pubkey(self, enclave_id: str) -> bytes:
        """
        获取可信执行环境验证公钥
        :param enclave_id: 可信执行环境Id
        :return: 公钥二进制数据
        """

    # 06-12 获取可信执行环境报告
    def get_enclave_report(self, enclave_id: str) -> bytes:
        """
        获取可信执行环境报告
        :param enclave_id: 可信执行环境Id
        :return: 报告二进制数据
        """

    # 06-13 获取可信执行环境挑战
    def get_enclave_challenge(self, enclave_id: str) -> bytes:
        """
        获取可信执行环境挑战
        :param enclave_id: 可信执行环境Id
        :return: 挑战二进制数据
        """

    # 06-14 获取可信执行环境签名
    def get_enclave_signature(self, enclave_id: str) -> bytes:
        """
        获取可信执行环境签名
        :param enclave_id: 可信执行环境Id
        :return: 签名二进制数据
        """

    # 06-15 保存远端认证证明
    def save_remote_attestation_proof(self, proof: str,
                                      tx_id: str = None, timeout: int = None,
                                      with_sync_result: bool = None) -> TxResponse:
        """
        保存远端认证证明
        :param proof: 证明数据
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 交易响应
        """

    # 创建保存可信执行环境根证书待签名Payload
    def create_save_enclave_ca_cert_payload(self, enclave_ca_cert: str, tx_id: str = None) -> Payload:
        """
        创建保存可信执行环境根证书待签名Payload
        :param enclave_ca_cert: 可信执行环境根证书
        :param tx_id: 指定交易Id
        :return: 待签名Payload
        """

    # 06-创建可信执行环境报告待签名Payload
    def create_save_enclave_report_payload(self, enclave_id: str, report: str, tx_id: str = None) -> Payload:
        """
        创建可信执行环境报告待签名Payload
        :param enclave_id: 可信执行环境Id
        :param report: 报告数据
        :param tx_id: 指定交易Id
        :return: 待签名Payload
        """

    def send_multi_signing_request(self, payload: Payload, endorsers: List[ClientUser] = None,
                                   timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        发送多签请求
        :param payload: 待签名Payload
        :param endorsers: 背书用户列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 交易响应
        """

    # 7-DPOS ERC20 -----------------------------------------------------------------------------------------------------
    # 07-00 查询归属人
    def owner(self) -> str:  # todo get_owner
        """
        查询归属人
        <07-00-DPOS_ERC20-GET_OWNER>
        """

    # 07-01 查询ERC20合约的精度
    def decimals(self) -> str:
        """
        查询ERC20合约的精度
        <07-01-DPOS_ERC20-GET_DECIMALS>
        :return: 合约精度
        """

    # 07-02 创建转账待签名Payload
    def create_transfer_payload(self, address: str, amount: int) -> Payload:
        """
        创建转账待签名Payload
        <07-02-DPOS_ERC20-TRANSFER>
        :param address: 接收Token的地址
        :param amount: 转账数量
        :return: 待签名Payload
        """

    # 07-03 创建从某个地址转账待签名Payload
    def create_transfer_from_payload(self, _from: str, to: str, amount: int) -> Payload:
        """
        创建从某个地址转账待签名Payload
        <07-03-DPOS_ERC20-TRANSFER_FROM>
        :param _from: 转出Token的地址
        :param to: 转入Token的地址
        :param amount: 转账数量
        :return: 待签名Payload
        """

    # 07-04 查询账户余额
    def balance_of(self, address: str) -> int:
        """
        查询账户余额
        <07-04-DPOS_ERC20-GET_BALANCEOF>
        :param address: 账户地址
        :return: 账户余额
        """

    # 07-05 创建转账证明待签名Payload
    def create_approve_payload(self, _from: str, to: str, amount: int) -> Payload:  # todo
        """
        创建转账证明待签名Payload
        <07-05-DPOS_ERC20-APPROVE>
        :param _from: 转出Token的地址
        :param to: 转入Token的地址
        :param amount: 转账数量
        :return: 待签名Payload
        """

    # 07-07 创建消耗Token待签名Payload
    def create_burn_payload(self, address: str, amount: int) -> Payload:  # todo
        """
        创建消耗Token待签名Payload
        <07-07-DPOS_ERC20-BURN>
        :param address: 接收Token的地址
        :param amount: 发行数量
        :return: 待签名Payload
        """

    # 07-08 创建发行Token待签名Payload
    def create_mint_payload(self, address: str, amount: int) -> Payload:
        """
        创建发行Token待签名Payload
        <07-08-DPOS_ERC20-MINT>
        :param address: 接收Token的地址
        :param amount: 发行数量
        :return: 待签名Payload
        """

    # 07-09 创建转移归属权待签名Payload
    def create_transfer_ownership_payload(self, address: str):
        """
        创建转移归属权待签名Payload
        <07-09-DPOS_ERC20-TRANSFER_OWNERSHIP>
        :param address: 接收资产地址
        :return: 待签名Payload
        """

    # 07-10 查询Token总供应量
    def total(self) -> str:
        """
        查询Token总供应量
        <07-10-DPOS_ERC20-GET_TOTAL_SUPPLY>
        :return:
        """

    # 8-DPOS STAKE操作 -
    # 08-00 查询所有的候选人
    def get_all_candidates(self) -> ValidatorVector:
        """
        查询所有的候选人
        <08-00-DPOS_STAKE-GET_ALL_CANDIDATES>
        :return: 候选人列表
        """

    # 08-01 通过地址获取验证人的信息
    def get_validator_by_address(self, address: str):
        """
        通过地址获取验证人的信息
        <08-01-DPOS_STAKE-GET_VALIDATOR_BY_ADDRESS>
        :param address:
        :return:
        """

    # 08-02 抵押权益到验证人
    def delegate(self, address: str, amount: int) -> Delegation:  # todo 确认是否需要轮训
        """
        抵押权益到验证人
        <08-02-DPOS_STAKE-DELEGATE>
        :param address:
        :param amount:
        :return:
        """

    # 08-03 查询指定地址的抵押信息
    def get_delegations_by_address(self, address: str) -> DelegationInfo:
        """
        查询指定地址的抵押信息
        <08-03-DPOS_STAKE-GET_DELEGATIONS_BY_ADDRESS>
        :param address:
        :return:
        """

    # 08-04 查询指定地址的抵押信息
    def get_user_delegation_by_validator(self, delegator: str, validator: str) -> Delegation:
        """
        查询指定地址的抵押信息
        <08-04-DPOS_STAKE-GET_USER_DELEGATION_BY_VALIDATOR>
        :param delegator:
        :param validator:
        :return:
        """

    # 08-04 从验证人解除抵押的权益
    def undelegate(self, address: str, amount: int) -> Delegation:
        """
        从验证人解除抵押的权益
        <08-05-DPOS_STAKE-UNDELEGATE>
        :param address:
        :param amount:
        :return:
        """

    # 08-06 查询指定世代信息
    def get_epoch_by_id(self, epoch_id: str) -> Epoch:
        """
        查询指定世代信息
        <08-06-DPOS_STAKE-READ_EPOCH_BY_ID>
        :param epoch_id:
        :return:
        """

    # 08-07 查询当前世代信息
    def get_last_epoch(self) -> Epoch:
        """
        查询当前世代信息
        <08-07-DPOS_STAKE-READ_LATEST_EPOCH>
        :return:
        """

    # 08-08 Stake合约中设置验证人的NodeID
    def set_node_id(self, node_id: str) -> str:
        """
        Stake合约中设置验证人的NodeID
        <08-08-DPOS_STAKE-SET_NODE_ID>
        :param node_id:
        :return:
        """

    # 08-09 Stake合约中查询验证人的NodeID
    def get_node_id(self, address: str) -> str:
        """
        Stake合约中查询验证人的NodeID
        <08-09-DPOS_STAKE-GET_NODE_ID>
        :param address:
        :return:
        """

    # 08-10
    def update_min_self_delegation(self):
        """
        <08-10-DPOS_STAKE-UPDATE_MIN_SELF_DELEGATION>
        :return:
        """
        pass

    # 08-11
    def get_min_self_delegation(self):
        """
        <08-11-DPOS_STAKE-READ_MIN_SELF_DELEGATION>
        :return:
        """
        pass

    # 08-12
    def update_epoch_validator_number(self):
        """
        <08-12-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER>
        :return:
        """
        pass

    # 08-13
    def get_epoch_validator_number(self):
        """
        <08-13-DPOS_STAKE-READ_EPOCH_VALIDATOR_NUMBER>
        :return:
        """
        pass

    # 08-14
    def update_epoch_block_number(self):
        """
        <08-14-DPOS_STAKE-UPDATE_EPOCH_BLOCK_NUMBER>
        :return:
        """
        pass

    # 08-15
    def get_epoch_block_number(self):
        """
        <08-15-DPOS_STAKE-READ_EPOCH_BLOCK_NUMBER>
        :return:
        """
        pass

    # 08-16 查询收到解质押退款间隔的世代数
    def get_unbounding_interval_epoch_number(self) -> str:
        """
        查询收到解质押退款间隔的世代数
         <08-16-DPOS_STAKE-READ_COMPLETE_UNBOUNDING_EPOCH_NUMBER>
        :return:
        """

    # 08-17 查询Stake合约的系统地址
    def get_stake_contract_address(self) -> str:
        """
        查询Stake合约的系统地址
        <08-18-DPOS_STAKE-READ_SYSTEM_CONTRACT_ADDR>
        :return:
        """

    # 08-19
    def unbounding(self):
        """
        <08-19-DPOS_STAKE-UNBOUNDING>
        :return:
        """

    # 08-20
    def create_create_epoch_payload(self):
        """
        <08-20-DPOS_STAKE-CREATE_EPOCH>
        :return:
        """

    # 08-21
    def update_epoch_validator_number_and_epoch_block_number(self):
        """
        <08-21-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER_AND_EPOCH_BLOCK_NUMBER>
        :return:
        """
        pass

    # 9-订阅 ------------------------------------------------------------------------------------------------------------
    # 09-00 订阅区块
    def subscribe_block(self, start_block: int, end_block: int, with_rw_set=False, only_header=False,
                        timeout: int = None, callback: Callable = None):
        """
        订阅区块
        :param start_block: 订阅的起始区块
        :param end_block: 订阅的结束区块
        :param with_rw_set: 是否包含读写集
        :param only_header: 是否只订阅区块头
        :param timeout: 订阅尚未产生区块的等待超时时间, 默认60s
        :param callback: 回调函数
        :return: 回调函数返回值
        """

    # 09-01 订阅交易
    def subscribe_tx(self, start_block: int, end_block: int, contract_name: str = None, tx_ids: List[str] = None,
                     timeout: int = None, callback: Callable = None):
        """
        订阅交易
        :param start_block: 订阅的起始区块
        :param end_block: 订阅的结束区块
        :param contract_name: 交易所属合约名称
        :param tx_ids: 指定交易Id列表进行订阅
        :param timeout: RPC请求超时时间
        :param callback: 回调函数
        :return: 回调函数返回值
        """

    # 09-02 订阅合约事件
    def subscribe_contract_event(self, start_block, end_block, topic: str, contract_name: str,
                                 timeout: int = None, callback: Callable = None) -> None:
        """
        订阅合约事件
        :param start_block: 订阅的起始区块
        :param end_block: 订阅的结束区块
        :param topic: 订阅待事件主题
        :param contract_name: 事件所属合约名称
        :param timeout: RPC请求超时时间
        :param callback: 回调函数
        :return: 回调函数返回值
        """

    def subscribe(self, payload: Payload, timeout: int = None,
                  callback: Callable = None) -> None:
        """
        订阅区块、交易、合约事件
        :param payload: 订阅Payload
        :param timeout: 订阅待产生区块等待超时时间
        :param callback: 回调函数，默认为self._callback
        :return: 回调函数返回值
        """

    # Hibe -------------------------------------------------------------------------------------------------------------
    def create_hibe_init_params_tx_payload_params(self, order_id: str, hibe_params: list):
        """

        :param order_id:
        :param hibe_params:
        :return:
        """

    def create_hibe_tx_payload_param_with_hibe_params(self, plaintext: list, receiver_ids: list,
                                                      params_bytes_list: list, tx_id: str, key_type: str):
        """
        
        :param plaintext:
        :param receiver_ids:
        :param params_bytes_list:
        :param tx_id:
        :param key_type:
        :return:
        """

    def create_hibe_tx_payload_param_without_hibe_params(self, contract_name: str, query_params_method: str,
                                                         plaintext: list, receiver_ids: list, receiver_oreg_ids: list,
                                                         tx_id: str, key_type: str, timeout: int):
        """

        :param contract_name:
        :param query_params_method:
        :param plaintext:
        :param receiver_ids:
        :param receiver_oreg_ids:
        :param tx_id:
        :param key_type:
        :param timeout:
        :return:
        """

    def query_hibe_params_with_org_id(self, contract_name: str, method: str, org_id: str, timeout: int):
        """

        :param contract_name:
        :param method:
        :param org_id:
        :param timeout:
        :return:
        """

    def decrypt_hibe_tx_by_tx_id(self, local_id: str, hibe_params: list, hibe_prv_key: list, tx_id: str,
                                 key_type) -> bytes:
        """

        :param local_id:
        :param hibe_params:
        :param hibe_prv_key:
        :param tx_id:
        :param key_type:
        :return:
        """

    # 10-归档 -----------------------------------------------------------------------------------------------------------
    def create_archive_block_payload(self, target_block_height):
        """

        :param target_block_height:
        :return:
        """

    def create_restore_block_payload(self, full_block: bytes):
        """

        :param full_block:
        :return:
        """

    def sign_archive_payload(self, payload):
        """

        :param payload:
        :return:
        """

    def send_archive_block_request(self, merge_signed_payload_bytes, timeout: int = None):
        """

        :param merge_signed_payload_bytes:
        :param timeout:
        :return:
        """

    def send_restore_block_request(self, merge_signed_payload_bytes):
        """

        :param merge_signed_payload_bytes:
        :return:
        """

    # 连接 -------------------------------------------------------------------------------------------------------------
    def stop(self):
        """

        :return:
        """

    # 版本信息 ----------------------------------------------------------------------------------------------------------
    def get_chainmaker_server_version(self):
        """

        :return:
        """

    # 12-公钥管理 -------------------------------------------------------------------------------------------------------
    # 12-00 创建公钥添加待签名Payload
    def create_pubkey_add_payload(self, pubkey: str, org_id: str, role: str):
        """
        创建公钥添加Payload
        :param pubkey: 公钥
        :param org_id: 组织id
        :param role: 角色
        :return: 生成的payload
        """

    # 12-01 创建公钥删除待签名Payload
    def create_pubkey_delete_payload(self, pubkey: str, org_id: str):
        """
        创建公钥删除Payload
        :param pubkey: 公钥
        :param org_id: 组织id
        :return: 生成的payload
        """

    # 12-02 查询公钥
    def query_pubkey(self, pubkey: str):
        """
        查询公钥
        <12-02-PUBKEY_MANAGE-PUBKEY_QUERY>
        :param pubkey:公钥文件内容
        :param timeout: RPC请求超时时间
        :return: 交易响应
        :raises: RequestError: 请求出错
        """

    def send_pubkey_manage_request(self, payload, endorsers: List[EndorsementEntry],
                                   timeout: int, with_sync_result: bool) -> TxResponse:
        """
        发送公钥管理请求
        :param payload: 公钥管理payload
        :param endorsers: 背书列表
        :param timeout: 超时时间
        :param with_sync_result: 是否同步结果
        :return: 交易响应或事务交易信息
        """

    # 13-Gas管理 --------------------------------------------------------------------------------------------------------
    # 13-00 创建设置Gas管理员待签名Payload
    def create_set_gas_admin_payload(self, address: str) -> Payload:
        """
        创建设置Gas管理员待签名Payload
        <13-00-ACCOUNT_MANAGER-SET_ADMIN>
        :param address: 管理员账户地址
        :return: 待签名Payload
        """

    # 13-01 查询Gas管理员地址
    def get_gas_admin(self) -> str:
        """
        查询Gas管理员地址
        <13-01-ACCOUNT_MANAGER-GET_ADMIN>
        :return: Gas管理员账户地址
        """

    # 13-02 创建Gas充值待签名Payload
    def create_recharge_gas_payload(self, recharge_gas_list: List[RechargeGasItem]) -> Payload:
        """
        创建Gas充值待签名Payload
        <13-02-ACCOUNT_MANAGER-RECHARGE_GAS>
        :param recharge_gas_list: 充值列表
        :return: 待签名Payload
        """

    # 13-03 获取Gas账户余额
    def get_gas_balance(self, address: str = None) -> int:
        """
        获取Gas账户余额
        <13-03-ACCOUNT_MANAGER-GET_BALANCE>
        :param str address: 账户地址
        :return: 账户余额
        """

    # 13-04 创建Gas收费待签名Payload
    def create_charge_gas_payload(self, recharge_gas_list: List[RechargeGasItem]) -> Payload:  # todo
        """
        创建Gas收费待签名Payload
        <13-04-ACCOUNT_MANAGER-CHARGE_GAS>
        :param recharge_gas_list: 充值列表
        :return: 待签名Payload
        """

    # 13-05 创建冻结账户待签名Payload
    def create_frozen_gas_account_payload(self, address: str) -> Payload:
        """
        创建冻结账户待签名Payload
        <13-05-ACCOUNT_MANAGER-FROZEN_ACCOUNT>
        :param address: 账户地址
        :return: 待签名Payload
        """

    # 13-06 创建解冻账户待签名Payload
    def create_unfrozen_gas_account_payload(self, address: str) -> Payload:
        """
        创建解冻账户待签名Payload
        <13-06-ACCOUNT_MANAGER-UNFROZEN_ACCOUNT>
        :param address: 账户地址
        :return: 待签名Payload
        """

    # 13-07 查询Gas账户状态
    def get_gas_account_status(self, address: str = None) -> bool:
        """
        查询Gas账户状态
        <13-07-ACCOUNT_MANAGER-ACCOUNT_STATUS>
        :param str address: 账户地址
        :return: 正常是返回True, 冻结返回False
        """

    # 13-08 创建Gas退款待签名Payload
    def create_refund_gas_payload(self, address: str, amount: int) -> Payload:
        """
        创建Gas退款待签名Payload
        <13-08-ACCOUNT_MANAGER-REFUND_GAS>
        :param address: 账户地址
        :param amount: 退款额度
        :return: 待签名Payload
        """

    # 13-09 创建Gas VM退款待签名Payload
    def create_refund_gas_vm_payload(self, address: str, amount: int) -> Payload:  # todo
        """
        创建Gas退款待签名Payload
        <13-09-ACCOUNT_MANAGER-REFUND_GAS_VM>
        :param address: 账户地址
        :param amount: 退款额度
        :return: 待签名Payload
        """

    # 13-10 创建Gas退款待签名Payload
    def create_charge_gas_for_multi_account_payload(self, address: str, amount: int) -> Payload:  # todo
        """
        创建Gas多账户收费待签名Payload
        <13-10-ACCOUNT_MANAGER-CHARGE_GAS_FOR_MULTI_ACCOUNT>
        :param address: 账户地址
        :param amount: 退款额度
        :return: 待签名Payload
        """

    @staticmethod
    def attach_gas_limit(payload: Payload, gas_limit: int) -> Payload:
        """
        设置Gas转账限制
        :param payload: Payload
        :param gas_limit: Gas交易限制
        :return: Payload
        """

    def estimate_gas(self, payload: Payload) -> int:
        """
        估计请求Gas消耗
        :param payload: 待发送请求payload
        :return: Gas数量
        """

    def send_gas_manage_request(self, payload: Payload, endorsers: list, timeout: int = None,
                                with_sync_result: bool = True) -> Union[TxResponse, Result]:
        """
        发送Gas管理请求
        :param payload: Payload
        :param endorsers: 背书列表
        :param timeout: 超时时间
        :param with_sync_result: 是否同步轮询结果
        :return: 响应信息
        """
