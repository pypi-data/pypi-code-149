#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   chain_manager.py
# @Function     :   ChainMaker管理操作接口(带背书客户端)
import functools
import json
import os
import uuid
from pathlib import Path
from typing import List, Union, Dict

from hostz import Host

from chainmaker.chain_client import ChainClientWithEndorsers
from chainmaker.client_user import ClientUser
from chainmaker.keys import (ChainConfigMethod, ParamKey, Role, AddrType, RuntimeType,
                             ContractManageMethod, SystemContractName, ResourceName, Rule, RechargeGasItem)
from chainmaker.protos import (Payload, TxResponse, BlockHeader, BlockInfo, Contract, CertInfos, Result,
                               TransactionInfo, ChainConfig,
                               ResourcePolicy, MultiSignInfo, ChainList, ChainInfo, BlockWithRWSet, ValidatorVector,
                               Delegation, DelegationInfo, Epoch)
from chainmaker.sdk_config import DefaultConfig
from chainmaker.utils import file_utils, crypto_utils, result_utils
from chainmaker.utils.common import gen_rand_contract_name, gen_rand_tx_id
from chainmaker.utils.crypto_config_utils import CryptoConfig
from chainmaker.utils.result_utils import msg_to_dict, parse_result
from chainmaker.utils.server_utils import ChainMakerCluster


def with_user_endorsers(method):
    @functools.wraps(method)
    def _method(self, *args, **kwargs):
        user = kwargs.pop('user') if 'user' in kwargs else None
        endorsers = kwargs.pop('endorsers') if 'endorsers' in kwargs else None
        conn_node = kwargs.pop('conn_node') if 'conn_node' in kwargs else None
        alias = kwargs.pop('alias') if 'alias' in kwargs else None
        enable_cert_hash = kwargs.pop('enable_cert_hash') if 'enable_cert_hash' in kwargs else None

        if user:
            cc = self._crypto_config.new_chain_client(user, endorsers=endorsers, conn_node=conn_node, alias=alias,
                                                      enable_cert_hash=enable_cert_hash)
            self._origin_cc, self._cc = self._cc, cc
            try:
                return msg_to_dict(method(self, *args, **kwargs))
            except Exception as ex:
                return str(ex)
            finally:
                self._cc = self._origin_cc
                cc.stop()
                delattr(self, '_origin_cc')
        else:
            try:
                return method(self, *args, **kwargs)
            except Exception as ex:
                return str(ex)

    return _method


class BaseOps:
    def __init__(self, cc: ChainClientWithEndorsers, crypto_config: CryptoConfig = None):
        self._crypto_config = crypto_config
        self._cc = cc or self._crypto_config.new_chain_client()

    def _get_client(self, user: str = None, endorsers: List[str] = None, endorsers_cnt: int = None,
                    conn_node: Union[str, int] = None, alias: str = None, enable_cert_hash: bool = False,
                    chain_id=DefaultConfig.chain_id):
        if user:
            return self._crypto_config.new_chain_client(user, endorsers, endorsers_cnt, conn_node, alias,
                                                        enable_cert_hash, chain_id)
        return self._cc


# 00
class ChainConfigOps(BaseOps):
    """带背书链客户端"""

    # =========================  带背书链配置信任组织根证书操作 =========================
    # 00-00 获取链配置
    @with_user_endorsers
    def get_chain_config(self) -> ChainConfig:
        """
        获取链配置
        <00-00-CHAIN_CONFIG-GET_CHAIN_CONFIG>
        :return: ChainConfig
        :raises RequestError: 请求失败
        """
        self._cc._info('获取链配置')
        return self._cc.get_chain_config()

    # 00-01 通过指定区块高度查询最近链配置
    @with_user_endorsers
    def get_chain_config_by_block_height(self, block_height: int) -> ChainConfig:
        """
        通过指定区块高度查询最近链配置
        如果当前区块就是配置块，直接返回当前区块的链配置
        <00-01-CHAIN_CONFIG-GET_CHAIN_CONFIG_AT>
        :param block_height: 块高
        :return: ChainConfig
        :raises RequestError: 请求失败
        """
        self._cc._info('通过指定区块高度查询最近链配置 block_height:%s' % block_height)
        return self._cc.get_chain_config_by_block_height(block_height)

    # 00-02 更新链配置Core配置
    @with_user_endorsers
    def core_update(self, tx_scheduler_timeout: int = None, tx_scheduler_validate_timeout: int = None,
                    timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新链配置Core配置
        <00-02-CHAIN_CONFIG-CORE_UPDATE>
        :param tx_scheduler_timeout: 交易调度器从交易池拿到交易后, 进行调度的时间，其值范围为[0, 60]，若无需修改，请置为-1
        :param tx_scheduler_validate_timeout: 交易调度器从区块中拿到交易后, 进行验证的超时时间，其值范围为[0, 60]，若无需修改，请置为-1
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错

        默认配置为：
        tx_scheduler_timeout: 10
        tx_scheduler_validate_timeout: 10
        consensus_turbo_config {}
        enable_conflicts_bit_window: true
        """
        self._cc._info('更新链配置Core配置')
        payload = self._cc.create_chain_config_core_update_payload(tx_scheduler_timeout, tx_scheduler_validate_timeout)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-03 更新链配置区块配置
    @with_user_endorsers
    def block_update(self, tx_timestamp_verify: bool = None, tx_timeout: int = None,
                     block_tx_capacity: int = None,
                     block_size: int = None, block_interval: int = None, tx_parameter_size: int = None,
                     timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新链配置区块配置
        <00-03-CHAIN_CONFIG-BLOCK_UPDATE>
        :param tx_timestamp_verify: 是否需要开启交易时间戳校验
        :param tx_timeout: 交易时间戳的过期时间(秒)，其值范围为[600, +∞)（若无需修改，请置为-1）
        :param block_tx_capacity: 区块中最大交易数，其值范围为(0, +∞]（若无需修改，请置为-1）
        :param block_size: 区块最大限制，单位MB，其值范围为(0, +∞]（若无需修改，请置为-1）
        :param block_interval: 出块间隔，单位:ms，其值范围为[10, +∞]（若无需修改，请置为-1）
        :param tx_parameter_size: 交易参数大小
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错

        默认配置为：
        tx_timestamp_verify: true
        tx_timeout: 600
        block_tx_capacity: 100
        block_size: 10
        block_interval: 10
        """
        self._cc._info('更新链配置区块配置')
        payload = self._cc.create_chain_config_block_update_payload(tx_timestamp_verify, tx_timeout, block_tx_capacity,
                                                                    block_size, block_interval, tx_parameter_size)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def trust_root_check(self, org_id: str, trust_root_crts: List[str] = None):
        """
        检查信任组织根证书是否上链
        :param org_id: 组织Id
        :param trust_root_crts: 信任根证书列表
        :return:
        """
        self._cc._info('检查信任组织根证书是否上链')
        trust_roots = self._cc.chain_config.trust_roots

        trust_root_orgs = [item.org_id for item in trust_roots]
        if org_id in trust_root_orgs:
            trust_root_certs = []
            for item in trust_roots:
                trust_root_certs.extend(item.root)
            if trust_root_crts in trust_root_certs:
                return True
        return False

    # 00-04 添加信任组织根证书
    @with_user_endorsers
    def trust_root_add(self, org_id: str, trust_root_crts: List[str],
                       timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        添加信任组织根证书
        <00-04-CHAIN_CONFIG-TRUST_ROOT_ADD>
        :param str org_id: 组织Id
        :param trust_root_crts: 根证书列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("添加信任组织根证书")
        payload = self._cc.create_chain_config_trust_root_add_payload(org_id, trust_root_crts)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-05 更新信任组织根证书
    @with_user_endorsers
    def trust_root_update(self, org_id: str, trust_root_crts: List[str],
                          timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新信任组织根证书
        <00-05-CHAIN_CONFIG-TRUST_ROOT_UPDATE>
        :param str org_id: 组织Id
        :param trust_root_crts: 根证书列表
        :param auto_remove_consensus_org: 是否检查并自动移除共识组织
        :param auto_add_trust_root: 是否检查并自动添加trust_root
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("更新信任组织根证书")
        payload = self._cc.create_chain_config_trust_root_update_payload(org_id, trust_root_crts)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-06 删除信任组织根证书
    @with_user_endorsers
    def trust_root_delete(self, org_id: str,
                          timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        删除信任组织根证书
        <00-06-CHAIN_CONFIG-TRUST_ROOT_DELETE>
        :param str org_id: 组织Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("删除信任组织根证书 org_id: %s" % org_id)
        payload = self._cc.create_chain_config_trust_root_delete_payload(org_id)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-07 添加共识节点地址
    @with_user_endorsers
    def node_addr_add(self, org_id: str, node_addrs: List[str], timeout: int = None,
                      with_sync_result: bool = None) -> TxResponse:
        """
        添加节点地址
        <00-07-CHAIN_CONFIG-NODE_ADDR_ADD>
        :param org_id: 节点组织Id
        :param node_addrs: 节点地址列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("添加共识节点地址 org_id: %s")
        payload = self._cc.create_chain_config_node_addr_add_payload(org_id, node_addrs)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-08 更新共识节点地址
    @with_user_endorsers
    def node_addr_update(self, org_id: str, node_old_addr: str, node_new_addr: str,
                         timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新节点地址
        <00-08-CHAIN_CONFIG-NODE_ADDR_UPDATE>
        :param org_id: 节点组织Id
        :param node_old_addr: 原节点地址
        :param node_new_addr: 新节点地址
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("更新共识节点地址 org_id: %s" % org_id)
        payload = self._cc.create_chain_config_node_addr_update_payload(org_id, node_old_addr, node_new_addr)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-09 删除共识节点地址
    @with_user_endorsers
    def node_addr_delete(self, org_id: str, node_addr: str,
                         timeout: int = None, with_sync_result: bool = None):
        """
        删除节点地址
        <00-09-CHAIN_CONFIG-NODE_ADDR_DELETE>
        :param org_id: 节点组织Id
        :param node_addr: 节点地址
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("删除共识节点地址 org_id: %s" % org_id)
        payload = self._cc.create_chain_config_node_addr_delete_payload(org_id, node_addr)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def node_org_check(self, org_id: str) -> bool:
        self._cc._info("检查共识节点组织 org_id: %s" % org_id)
        consensus_nodes = self._cc.chain_config.consensus.nodes
        consensus_orgs = [item.org_id for item in consensus_nodes]
        return org_id in consensus_orgs

    ## 00-10 添加共识节点组织
    @with_user_endorsers
    def node_org_add(self, org_id: str, node_ids: List[str],
                     timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        添加共识节点组织
        :param org_id: 节点组织Id
        :param node_ids: 节点Id
        :param auto_add_trust_root: 自动添加trust_root
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("添加共识节点组织 org_id: %s" % org_id)
        payload = self._cc.create_chain_config_consensus_node_org_add_payload(org_id, node_ids)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    ## 00-11 更新共识节点组织
    @with_user_endorsers
    def node_org_update(self, org_id: str, node_ids: List[str],
                        timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新共识节点组织
        :param org_id: 节点组织Id
        :param node_ids: 节点Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :param auto_add_consensus_org: 不存在该共识组织时是否自动添加
        :return: 添加共识、更新共识组织的交易响应或None
        :raises RequestError: 请求出错
        """
        self._cc._info("更新共识节点组织 org_id: %s" % org_id)
        self._cc._info('begin to update consensus org')
        payload = self._cc.create_chain_config_consensus_node_org_update_payload(org_id, node_ids)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    ## 00-12 删除共识节点组织
    @with_user_endorsers
    def node_org_delete(self, org_id: str,
                        timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        删除共识节点组织
        :param org_id: 节点组织Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("删除共识节点组织 org_id: %s" % org_id)
        payload = self._cc.create_chain_config_consensus_node_org_delete_payload(org_id)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def consensus_ext_check(self, key: str, value: str = None) -> bool:
        """检查共识扩展key是否存在及key-value是否相同"""
        self._cc._info("检查共识扩展参数")
        consensus_ext = msg_to_dict(self._cc.chain_config.consensus.ext_config)
        if key in self._cc.consensus_ext.keys():
            if value is None:
                return True
            else:
                return value == self._cc.consensus_ext.get(key)
        return False

    ## 00-13 添加共识扩展参数
    @with_user_endorsers
    def consensus_ext_add(self, params: dict,
                          timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        添加共识扩展参数
        :param params: 字段key、value对
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("添加共识扩展参数")
        payload = self._cc.create_chain_config_consensus_ext_add_payload(params)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    ## 00-14 更新共识扩展参数
    @with_user_endorsers
    def consensus_ext_update(self, params: dict, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新共识扩展参数
        :param dict params: 字段key、value对
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("更新共识扩展参数")
        payload = self._cc.create_chain_config_consensus_ext_update_payload(params)

        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    ## 00-15 删除共识扩展参数
    @with_user_endorsers
    def consensus_ext_delete(self, keys: List[str], timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        删除共识扩展参数
        :param keys: 待删除字段
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("删除共识扩展参数")
        payload = self._cc.create_chain_config_consensus_ext_delete_payload(keys)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def permission_check(self, permission_resource_name: Union[ResourceName, str]) -> bool:
        """
        检查权限是否存在
        :param permission_resource_name:
        :return:
        """
        self._cc._info("检查权限是否存在")
        permission_resource_names = [item.resource_name for item in self._cc.chain_config.resource_policies]
        return permission_resource_name in permission_resource_names

    # 00-16 添加权限配置
    @with_user_endorsers
    def permission_add(self, permission_resource_name: Union[ResourceName, str], rule: Union[Rule, str],
                       role_list: List[Role] = None, org_list: List[str] = None,
                       timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        添加权限配置
        :param permission_resource_name: 权限名
        :param rule: 权限规则
        :param org_list: 权限适用组织列表
        :param role_list: 权限适用角色列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("添加权限配置")
        policy = self._cc.create_policy(rule, role_list=role_list, org_list=org_list)
        payload = self._cc.create_chain_config_permission_add_payload(permission_resource_name, policy)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-17 更新权限配置
    @with_user_endorsers
    def permission_update(self, permission_resource_name: Union[ResourceName, str], rule: Union[Rule, str],
                          role_list: List[Role] = None, org_list: List[str] = None,
                          timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新权限配置
        :param str permission_resource_name: 权限名
        :param rule: 权限规则
        :param org_list: 权限适用组织列表
        :param role_list: 权限适用角色列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("更新权限配置")
        policy = self._cc.create_policy(rule, role_list=role_list, org_list=org_list)
        payload = self._cc.create_chain_config_permission_update_payload(permission_resource_name, policy)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-18 删除权限配置
    @with_user_endorsers
    def permission_delete(self, permission_resource_name: Union[ResourceName, str],
                          timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        删除权限配置
        :param str permission_resource_name: 权限名
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("删除权限配置")
        payload = self._cc.create_chain_config_permission_delete_payload(permission_resource_name)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def node_id_check(self, org_id: str, node_id: str) -> bool:
        """
        检查共识节点Id
        :param org_id:
        :param node_id:
        :return:
        """
        self._cc._info("检查共识节点Id")
        consensus_nodes = self._cc.chain_config.consensus.nodes
        consensus_orgs = [item.org_id for item in consensus_nodes]
        if org_id in consensus_orgs:
            node_ids = []
            for item in consensus_nodes:
                if org_id is None:
                    node_ids.extend(item.node_id)
            if node_id in node_ids:
                return True
        return False

    # 00-19 添加共识节点Id
    @with_user_endorsers
    def node_id_add(self, org_id: str, node_ids: List[str],
                    timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        添加共识节点Id
        :param str org_id: 节点组织Id
        :param node_ids: 节点Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :param auto_add_consensus_node_org: 是否自动添加共识组织
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("添加共识节点Id")
        payload = self._cc.create_chain_config_consensus_node_id_add_payload(org_id, node_ids)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-20 更新共识节点Id
    @with_user_endorsers
    def node_id_update(self, org_id: str, node_old_id: str, node_new_id: str,
                       timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新共识节点Id
        :param str org_id: 节点组织Id
        :param node_old_id: 节点原Id
        :param node_new_id: 节点新Id
        :param auto_add: 不存在时是否自动添加该节点组织及节点Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("更新共识节点Id")
        payload = self._cc.create_chain_config_consensus_node_id_update_payload(org_id, node_old_id, node_new_id)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-21 删除共识节点Id
    @with_user_endorsers
    def node_id_delete(self, org_id: str, node_id: str,
                       timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        删除共识节点Id
        :param str org_id: 节点组织Id
        :param node_id: 节点Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("删除共识节点Id")
        payload = self._cc.create_chain_config_consensus_node_id_delete_payload(org_id, node_id)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def trust_member_check(self, org_id: str, trust_member_info: str = None) -> bool:
        """
        检查信任第三方组织是否上链
        :param org_id: 组织Id
        :param trust_member_info: 信任第三方根证书
        :return: 已上链返回True，否则返回False
        """
        self._cc._info("检查信任第三方组织")
        trust_members = self._cc.chain_config.trust_members
        trust_member_org_ids = [item.org_id for item in trust_members]
        if org_id in trust_member_org_ids:
            trust_member_infos = [item.member_info for item in trust_members]
            if trust_member_info in trust_member_infos:
                return True
        return False

    # 00-22 添加信任第三方组织
    @with_user_endorsers
    def trust_member_add(self, org_id: str, trust_member_node_id: str, trust_member_info: str,
                         trust_member_role: Union[Role, str],
                         timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        添加信任第三方组织
        :param org_id: 组织Id
        :param trust_member_node_id: 节点ID
        :param trust_member_info: 节点信息
        :param trust_member_role: 节点角色
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("添加信任第三方组织")
        payload = self._cc.create_chain_config_trust_member_add_payload(org_id, trust_member_node_id, trust_member_info,
                                                                        trust_member_role)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    ## 00-23 更新信任第三方组织
    @with_user_endorsers
    def trust_member_update(self, trust_member_org_id: str, trust_member_node_id: str, trust_member_info: str,
                            trust_member_role: Union[Role, str],
                            timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新信任第三方组织
        :param trust_member_org_id: 组织Id
        :param trust_member_node_id: 节点ID
        :param trust_member_info: 节点信息
        :param trust_member_role: 节点角色
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("更新信任第三方组织")
        payload = self._cc.create_chain_config_trust_member_update_payload(trust_member_org_id, trust_member_node_id,
                                                                           trust_member_info, trust_member_role)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-24 删除信任第三方组织
    @with_user_endorsers
    def trust_member_deleate(self, trust_member_info: str,
                             timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        删除信任第三方组织
        :param trust_member_info: 节点证书信息
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        self._cc._info("删除信任第三方组织")
        payload = self._cc.create_chain_config_trust_member_delete_payload(trust_member_info)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-25 变更地址类型
    @with_user_endorsers
    def alter_addr_type(self, addr_type: Union[AddrType, str, int],
                        timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        创建链配置变更地址类型待签名Payload
        <00-25-CHAIN_CONFIG-ALTER_ADDR_TYPE>
        :param addr_type: 地址类型
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        self._cc._info("变更地址类型")
        payload = self._cc.create_chain_config_alter_addr_type_payload(addr_type)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout,
                                                          with_sync_result=with_sync_result)

    # 00-26 启用或禁用Gas
    @with_user_endorsers
    def enable_or_disable_gas(self, enable_gas: bool = None,
                              timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        启用或禁用Gas
        :param enable_gas: 是否启用Gas, 为None时直接切换
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        if enable_gas is None or (enable_gas is not self._cc.enabled_gas):
            self._cc._info("启用或禁用Gas")
            payload = self._cc.create_chain_config_enable_or_disable_gas_payload()
            return self._cc._send_chain_config_update_request(payload, timeout=timeout,
                                                              with_sync_result=with_sync_result)

    # 00-27 设置合约调用基础Gas消耗
    @with_user_endorsers
    def set_invoke_base_gas(self, amount: int, timeout: int = None, with_sync_result: bool = None):
        """
        设置合约调用基础Gas消耗
        :param amount: 设置待基础Gas消耗数量
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :param auto_set_gas_admin: 是否自动设置当前用户为Gas管理员
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        self._cc._info("设置合约调用基础Gas消耗")
        params = {ParamKey.set_invoke_base_gas.name: amount}
        payload = self._cc._create_chain_config_manage_payload(ChainConfigMethod.SET_INVOKE_BASE_GAS.name,
                                                               params)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-28 设置Gas管理员地址
    @with_user_endorsers
    def set_account_manager_admin(self, address: str, timeout: int = None,
                                  with_sync_result: bool = None) -> TxResponse:
        """
        设置Gas管理员地址
        :param address: 用户地址-为None时为当前用户地址
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        self._cc._info("设置Gas管理员地址")
        payload = self._cc.create_chain_config_set_account_manager_admin_payload(address)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 00-29 获取链配置权限列表
    @with_user_endorsers
    def get_permission_list(self) -> ResourcePolicy:
        """
        获取链配置权限列表
        <00-29-CHAIN_CONFIG-PERMISSION_LIST>
        :return: 权限列表
        """
        self._cc._info("获取链配置权限列表")
        return self._cc.get_chain_config_permission_list()

    # 00-32 更新DPos共识节点Id
    @with_user_endorsers
    def dpos_node_id_update(self, node_ids: List[str],
                            timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        更新DPos共识节点Id
        :param node_ids: 节点Id列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises RequestError: 请求出错
        """
        self._cc._info("更新DPos共识节点Id")
        payload = self._cc.create_chain_config_dpos_node_id_update_payload(node_ids)
        return self._cc._send_chain_config_update_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def _send_chain_config_update_request(self, payload: Payload,
                                          timeout: int = None,
                                          with_sync_result: bool = None) -> TxResponse:
        """
        发送链配置更新请求
        :param payload: 待签名链配置更新请求Payload
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮交易结果
        :return: 交易响应信息
        """
        response = self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)
        # 更新缓存的chain_config
        setattr(self, '_cached_chain_config', None)
        return response


# 01
class ChainQueryOps(BaseOps):
    # ========================== 链查询操作 ==================================

    # 01-00 通过交易Id获取交易所在区块信息
    @with_user_endorsers
    def get_block_by_tx_id(self, tx_id: str) -> BlockInfo:
        """
        通过交易Id获取交易所在区块信息
        <01-00-CHAIN_QUERY-GET_BLOCK_BY_TX_ID>
        :param tx_id: 交易Id
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """
        self._cc._info("通过交易Id获取交易所在区块信息")
        return self._cc.get_block_by_tx_id(tx_id)

    # 01-01 通过交易Id获取交易信息
    @with_user_endorsers
    def get_tx_by_tx_id(self, tx_id: str) -> TransactionInfo:
        """
        通过交易Id获取交易信息
        <01-01-CHAIN_QUERY-GET_TX_BY_TX_ID>
        :param tx_id: 交易Id，类型为字符串
        :return: Result
        :raises RequestError: 请求失败
        """
        self._cc._info("通过交易Id获取交易信息")
        return self._cc.get_tx_by_tx_id(tx_id)

    # 01-02 通过区块高度获取区块信息
    @with_user_endorsers
    def get_block_by_height(self, block_height: int, with_rw_set: bool = False) -> Union[BlockInfo, BlockWithRWSet]:
        """
        通过区块高度获取区块信息
        <01-02-CHAIN_QUERY-GET_BLOCK_BY_HEIGHT>
        :param block_height: 区块高度
        :param with_rw_set: 是否返回读写集数据, 默认不返回。
        :return: 区块信息BlockInfo对象
        :raises RequestError: 请求失败，块已归档是抛出ContractFile
        """
        self._cc._info("通过区块高度获取区块信息")
        if with_rw_set:
            return self._cc.get_block_with_tx_rw_sets_by_height(block_height)
        return self._cc.get_block_by_height(block_height)

    # 01-03 获取链信息
    @with_user_endorsers
    def get_chain_info(self) -> ChainInfo:
        """
        获取链信息
        <01-03-CHAIN_QUERY-GET_CHAIN_INFO>
        :return: ChainInfo
        :raises RequestError: 请求失败
        """
        self._cc._info("获取链信息")
        return self._cc.get_chain_info()

    # 01-04 获取最新的配置块
    @with_user_endorsers
    def get_last_config_block(self, with_rw_set: bool = False) -> BlockInfo:
        """
        获取最新的配置块
        <01-04-CHAIN_QUERY-GET_LAST_CONFIG_BLOCK>
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """
        self._cc._info("获取最新的配置块")
        return self._cc.get_last_config_block(with_rw_set)

    # 01-05 通过区块哈希获取区块信息
    @with_user_endorsers
    def get_block_by_hash(self, block_hash: str, with_rw_set: bool = False) -> Union[BlockInfo, BlockWithRWSet]:
        """
        通过区块哈希获取区块信息
        <01-05-CHAIN_QUERY-GET_BLOCK_BY_HASH>
        :param block_hash: 区块Hash, 二进制hash.hex()值，
                           如果拿到的block_hash字符串是base64值, 需要用 base64.b64decode(block_hash).hex()
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """
        self._cc._info("通过区块哈希获取区块信息")
        if with_rw_set:
            return self._cc.get_block_with_tx_rw_sets_by_hash(block_hash)
        return self._cc.get_block_by_hash(block_hash)

    # 01-06 获取节点加入的链列表
    @with_user_endorsers
    def get_node_chain_list(self) -> ChainList:
        """
        获取节点加入的链列表
        <01-06-CHAIN_QUERY-GET_NODE_CHAIN_LIST>
        :return: 链Id列表
        :raises RequestError: 请求失败
        """
        self._cc._info("获取节点加入的链列表")
        return self._cc.get_node_chain_list()

    # 01-07 获取统治合约
    @with_user_endorsers
    def get_governance_contract(self):
        """
        获取统治合约
        <01-07-CHAIN_QUERY-GET_GOVERNANCE_CONTRACT>
        :return:
        """
        self._cc._info("获取统治合约")
        return self._cc.get_governance_contract()

    # 01-08 通过区块高度获取带读写集区块信息
    @with_user_endorsers
    def get_block_with_tx_rw_sets_by_height(self, block_height: int) -> BlockWithRWSet:
        """
        通过区块高度获取带读写集区块信息
        <01-08-CHAIN_QUERY-GET_BLOCK_WITH_TXRWSETS_BY_HEIGHT>
        :param block_height: 区块高度
        :return: 带读写集区块信息
        """
        self._cc._info("通过区块高度获取带读写集区块信息")
        return self._cc.get_block_with_tx_rw_sets_by_height(block_height)

    # 01-09 通过区块哈希获取带读写集区块信息
    @with_user_endorsers
    def get_block_with_tx_rw_sets_by_hash(self, block_hash: str) -> BlockWithRWSet:
        """
        通过区块哈希获取带读写集区块信息
         <01-09-CHAIN_QUERY-GET_BLOCK_WITH_TXRWSETS_BY_HASH>
        :param block_hash: 区块哈希
        :return: 带读写集区块信息
        """
        self._cc._info("通过区块哈希获取带读写集区块信息")
        return self._cc.get_block_with_tx_rw_sets_by_hash(block_hash)

    # 01-10 获取最新区块信息
    @with_user_endorsers
    def get_last_block(self, with_rw_set: bool = False) -> BlockInfo:
        """
        获取最新区块信息
        <01-10-CHAIN_QUERY-GET_LAST_BLOCK>
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """
        self._cc._info("获取最新区块信息")
        return self._cc.get_last_block(with_rw_set)

    # 01-11 通过区块高度获取完整区块信息
    @with_user_endorsers
    def get_full_block_by_height(self, block_height: int) -> BlockWithRWSet:
        """
        通过区块高度获取完整区块信息
        <01-11-CHAIN_QUERY-GET_FULL_BLOCK_BY_HEIGHT>
        :param block_height: 区块高度
        :return: BlockInfo
        :raises RequestError: 请求失败
        """
        self._cc._info("通过区块高度获取完整区块信息")
        return self._cc.get_full_block_by_height(block_height)

    # 01-12 通过交易Id获取区块高度
    @with_user_endorsers
    def get_block_height_by_tx_id(self, tx_id: str) -> int:
        """
        通过交易Id获取区块高度
        <01-12-CHAIN_QUERY-GET_BLOCK_HEIGHT_BY_TX_ID>
        :param tx_id: 交易Id
        :return: 区块高度
        :raises RequestError: 请求失败
        """
        self._cc._info("通过交易Id获取区块高度")
        return self._cc.get_block_height_by_tx_id(tx_id)

    # 01-13 通过区块哈希获取区块高度
    @with_user_endorsers
    def get_block_height_by_hash(self, block_hash: str) -> int:
        """
        通过区块哈希获取区块高度
        <01-13-CHAIN_QUERY-GET_BLOCK_HEIGHT_BY_HASH>
        :param block_hash: 区块Hash 二进制hash.hex()值,
               如果拿到的block_hash字符串是base64值, 需要用 base64.b64decode(block_hash).hex()
        :return: 区块高度
        :raises RequestError: 请求失败
        """
        self._cc._info("通过区块哈希获取区块高度")
        return self._cc.get_block_height_by_hash(block_hash)

    # 01-14 通过高度获取区块头
    @with_user_endorsers
    def get_block_header_by_height(self, block_height: int) -> BlockHeader:
        """
        通过高度获取区块头
        <01-14-CHAIN_QUERY-GET_BLOCK_HEADER_BY_HEIGHT>
        :param block_height: 区块高度
        :return: 区块头
        """
        self._cc._info("通过高度获取区块头")
        return self._cc.get_block_header_by_height(block_height)

    # 01-15 获取已归档的区块高度
    @with_user_endorsers
    def get_archived_block_height(self) -> int:
        """
        获取已归档的区块高度
         <01-15-CHAIN_QUERY-GET_ARCHIVED_BLOCK_HEIGHT>
        :return: 区块高度
        :raises RequestError: 请求失败
        """
        self._cc._info("获取已归档的区块高度")
        return self._cc.get_archived_block_height()

    # 01-16 获取全部合约信息
    @with_user_endorsers
    def get_all_contracts(self) -> List[Contract]:
        """
        获取全部合约信息
        <01-16-CHAIN_QUERY-GET_ALL_CONTRACTS>
        :return: 合约Contract对象列表
        :raise: RequestError: 请求出错
        :raise: AssertionError: 响应code不为0,检查响应时抛出断言失败
        :raise: 当数据不是JSON格式时，抛出json.decoder.JSONDecodeError
        """
        self._cc._info("获取全部合约信息")
        return self._cc.get_all_contracts()

    # 01-17 通过交易Id获取Merkle树路径
    @with_user_endorsers
    def get_merkle_path_by_tx_id(self, tx_id: str) -> bytes:
        """
        通过交易Id获取Merkle树路径
        <01-17-CHAIN_QUERY-GET_MERKLE_PATH_BY_TX_ID>
        :param tx_id: 交易Id
        :return: Merkle树路径
        """
        self._cc._info("通过交易Id获取Merkle树路径")
        return self._cc.get_merkle_path_by_tx_id(tx_id)


# 02
class CertManageOps(BaseOps):
    """证书管理"""

    @with_user_endorsers
    def check_cert_hash(self, cert_hash: str = None) -> bool:
        """
        检查证书哈希是否上链
        :param cert_hash: 证书哈希
        :return: 已上链返回True，否则返回False
        """
        self._cc._info("检查证书哈希是否上链")
        cert_hashes = [cert_hash] if cert_hash is not None else None
        return self._cc.query_cert(cert_hashes) is not None

    @with_user_endorsers
    def check_cert(self, cert_bytes_or_file_path: Union[Path, str, bytes] = None):
        """
        检查用户证书是否已上链
        :param cert_bytes_or_file_path: 证书二进制内容或证书文件路径
        :return: 已上链返回True，否则返回False
        """
        self._cc._info("检查用户证书是否已上链")
        if cert_bytes_or_file_path is None:
            return self._cc.check_cert_hash()

        cert_bytes = cert_bytes_or_file_path
        if isinstance(cert_bytes_or_file_path, (Path, str)):
            cert_bytes = file_utils.read_file_bytes(cert_bytes_or_file_path)
        cert = crypto_utils.load_pem_cert(cert_bytes)
        cert_hash = crypto_utils.get_cert_hash_bytes(cert).hex()
        return self._cc.check_cert_hash(cert_hash)

    # 02-00 添加证书
    @with_user_endorsers
    def add_cert(self, cert_hashes: List[str] = None, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        添加证书
        <02-00-CERT_MANAGE-CERT_ADD>
        :param cert_hashes:
        :param timeout: 设置请求超时时间
        :param with_sync_result: 同步返回请求结果
        :return: 交易响应
        :raises RequestError: 请求失败
        """
        self._cc._info("添加证书")
        if cert_hashes is None:
            cert_hashes = [self._cc.user.cert_hash]
        return self._cc.add_cert(cert_hashes, timeout, with_sync_result)

    # 02-01 删除证书
    @with_user_endorsers
    def delete_cert(self, cert_hashes: List[str] = None,
                    timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        删除证书
        <02-01-CERT_MANAGE-CERTS_DELETE>
        :param cert_hashes: 证书hash列表, 每个证书hash应转为hex字符串
        :param timeout: 超时时长
        :param with_sync_result: 是否同步返回请求结果
        :return: Response
        :raises RequestError: 请求失败
        """
        self._cc._info("删除证书")
        payload = self._cc.create_cert_delete_payload(cert_hashes)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 02-02 根据证书哈希查询证书
    @with_user_endorsers
    def query_cert(self, cert_hashes: Union[list, str] = None, timeout: int = None) -> CertInfos:
        """
        查询证书的hash是否已经上链
        <02-02-CERT_MANAGE-CERTS_QUERY>
        :param cert_hashes: 证书hash列表(List)，每个证书hash应转为hex字符串, 为None时查询当前用户证书
        :param timeout: 请求超时时间
        :return: CertInfos
        :raises 查询不到证书抛出 RequestError
        """
        self._cc._info("根据证书哈希查询证书")
        return self._cc.query_cert(cert_hashes, timeout)

    # 02-03 冻结证书
    @with_user_endorsers
    def freeze_cert(self, certs: List[str], timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        冻结证书
        <02-03-CERT_MANAGE-CERTS_FREEZE>
        :param certs: 证书内容列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        self._cc._info("冻结证书")
        payload = self._cc.create_cert_freeze_payload(certs)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 02-04 解冻证书
    @with_user_endorsers
    def unfreeze_cert(self, certs: List[str], timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        解冻证书
        <02-04-CERT_MANAGE-CERTS_UNFREEZE>
        :param certs: 证书内容
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        self._cc._info("解冻证书")
        payload = self._cc.create_cert_unfreeze_payload(certs)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 02-05 吊销证书
    @with_user_endorsers
    def revoke_cert(self, cert_bytes_or_file_path: Union[Path, str, bytes],
                    ca_key_bytes_or_file_path: Union[Path, str, bytes],
                    ca_cert_bytes_or_file_path: Union[Path, str, bytes],
                    timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        吊销证书
         <02-05-CERT_MANAGE-CERTS_REVOKE>
        :param cert_bytes_or_file_path: 证书文件路径
        :param ca_key_bytes_or_file_path: 所属组织ca证书文件路径
        :param ca_cert_bytes_or_file_path: 所属组织ca私钥文件路径
        :param timeout: RCP请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        self._cc._info("吊销证书")
        cert_crl = crypto_utils.create_crl_bytes(cert_bytes_or_file_path, ca_key_bytes_or_file_path,
                                                 ca_cert_bytes_or_file_path)

        payload = self._cc.create_cert_revoke_payload(cert_crl.decode())
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 02-06 添加证书别名
    @with_user_endorsers
    def add_cert_alias(self, alias: str = None) -> Result:  # MemberType must be MemberType_CERT
        """
        添加证书别名
        <02-06-CERT_MANAGE-CERT_ALIAS_ADD>
        :return: 响应信息
        """
        self._cc._info("添加证书别名")
        return self._cc.add_alias(alias)

    # 02-07 通过别名更新证书
    @with_user_endorsers
    def update_cert_by_alias(self, alias: str, new_cert_pem: str,
                             timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        通过别名更新证书
        :param alias: 用户别名
        :param new_cert_pem: 新证书文件内容
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        self._cc._info("通过别名更新证书")
        payload = self._cc.create_update_cert_by_alias_payload(alias, new_cert_pem)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 02-08 删除证书别名
    @with_user_endorsers
    def delete_cert_alias(self, aliases: List[str], timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        删除证书别名
        :param aliases: 别名列表
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        self._cc._info("删除证书别名")
        payload = self._cc.create_delete_cert_alias_payload(aliases)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @staticmethod
    @with_user_endorsers
    def gen_random_alias(prefix='alias_') -> str:
        """
        生成随机别名
        :param prefix: 别名前缀
        :return: 别名字符串
        """
        return '%s%s' % (prefix, str(uuid.uuid4()).replace('-', '_'))


# 04
class MultiSignOps(BaseOps):
    """多签管理"""

    # 04-00 发起多签请求
    @with_user_endorsers
    def multi_sign_req(self, params: Union[list, dict], tx_id: str = None, timeout: int = None,
                       with_sync_result: bool = None) -> Payload:
        """
        发起多签请求
        <04-00-MULTI_SIGN-REQ>
        :param payload: 待签名payload
        :param timeout: 请求超时时间
        :param with_sync_result: 是否同步获取交易结果
        :return: 交易响应或交易信息
        """
        self._cc._info("发起多签请求")
        payload = self._cc.create_multi_sign_req_payload(params, tx_id)
        self._cc.multi_sign_req(payload, timeout=timeout, with_sync_result=with_sync_result)
        return payload

    # 04-01 对多签请求Payload进行投票
    @with_user_endorsers
    def multi_sign_vote(self, multi_sign_req_payload, endorser: ClientUser = None, is_agree: bool = True,
                        timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        对多签请求Payload进行投票
        <04-01-MULTI_SIGN-VOTE>
        :param multi_sign_req_payload: 待签名payload
        :param endorser: 投票用户对象
        :param is_agree: 是否同意，true为同意，false则反对
        :param timeout: 请求超时时间
        :param with_sync_result: 是否同步获取交易结果
        :return: 交易响应或交易信息
        """
        self._cc._info("对多签请求Payload进行投票")
        return self._cc.multi_sign_vote_by_tx_id(multi_sign_req_payload, endorser, is_agree, timeout, with_sync_result)

    @with_user_endorsers
    def multi_sign_vote_by_tx_id(self, tx_id: str, endorser: ClientUser = None, is_agree: bool = True,
                                 timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        根据交易Id对多签请求进行投票
        :param tx_id: 交易Id
        :param endorser: 投票用户对象
        :param is_agree: 是否同意，true为同意，false则反对
        :param timeout: 请求超时时间
        :param with_sync_result: 是否同步获取交易结果
        :return: 交易响应或交易信息
        """
        self._cc._info("根据交易Id对多签请求进行投票")
        return self._cc.multi_sign_vote_by_tx_id(tx_id, endorser, is_agree, timeout, with_sync_result)

    # 04-02 查询多签状态
    @with_user_endorsers
    def multi_sign_query(self, tx_id: str, timeout: int = None) -> MultiSignInfo:
        """
        查询多签状态
        <04-02-MULTI_SIGN-QUERY>
        :param tx_id: 交易ID
        :param timeout: RPC请求超时时间
        :return: 多签信息
        """
        self._cc._info("查询多签状态")
        return self._cc.multi_sign_query(tx_id, timeout=timeout)

    @with_user_endorsers
    def multi_sign_trig(self, multi_sign_req_payload: Payload) -> TxResponse:
        """
        发送线上多签触发请求到节点 v2.3.1新增
        :param multi_sign_req_payload: 多签请求
        :return: 交易相应
        """
        self._cc._info("发送线上多签触发请求到节点")
        return self._cc.multi_sign_trig(multi_sign_req_payload)


# 05
class ContractManageOps(BaseOps):
    # ================================ 合约管理 ===============================================
    # 05-00 获取合约信息
    @with_user_endorsers
    def get_contract_info(self, contract_name: str) -> Union[Contract, None]:
        """
        获取合约信息
        <05-00-CONTRACT_MANAGE-GET_CONTRACT_INFO> # todo
        :param contract_name: 用户合约名称
        :return: 合约存在则返回合约信息Contract对象，合约不存在抛出ContractFail
        :raise: RequestError: 请求出错
        :raise: AssertionError: 响应code不为0,检查响应时抛出断言失败
        :raise: 当数据不是JSON格式时，抛出json.decoder.JSONDecodeError
        """
        return self._cc.get_contract_info(contract_name)

    # 05-01 获取合约ByteCode
    @with_user_endorsers
    def get_contract_byte_code(self, contract_name: str) -> bytes:  # todo
        """
        获取合约ByteCode
        <05-01-CONTRACT_MANAGE-GET_CONTRACT_BYTECODE> # todo
        :param contract_name: 用户合约名称
        :return: 合约存在则返回合约信息Contract对象，合约不存在抛出ContractFail
        :raise: RequestError: 请求出错
        :raise: AssertionError: 响应code不为0,检查响应时抛出断言失败
        :raise: 当数据不是JSON格式时，抛出json.decoder.JSONDecodeError
        """
        return self._cc.get_contract_byte_code(contract_name)

    # 05-02 获取合约列表
    @with_user_endorsers
    def get_contract_list(self) -> List[Contract]:
        """
        获取合约列表(包括系统合约和用户合约)
        <05-02-CONTRACT_MANAGE-GET_CONTRACT_LIST> # todo
        :return: 合约Contract对象列表
        :raise: RequestError: 请求出错
        :raise: AssertionError: 响应code不为0,检查响应时抛出断言失败
        :raise: 当数据不是JSON格式时，抛出json.decoder.JSONDecodeError
        """
        return self._cc.get_contract_list()

    # 05-03 获取禁用系统合约名称列表
    @with_user_endorsers
    def get_disabled_native_contract_list(self) -> List[str]:
        """
        获取禁用系统合约名称列表
        <05-03-CONTRACT_MANAGE-GET_DISABLED_CONTRACT_LIST> # todo
        :return: 禁用合约名称列表
        """
        return self._cc.get_disabled_native_contract_list()

    @with_user_endorsers
    def check_contract(self, contract_name: str) -> bool:
        """
        检查合约是否存在
        :param contract_name: 合约名称
        :return: 合约存在返回True, 否则返回False
        """
        contract = self._cc.get_contract_info(contract_name)
        return contract is not None

    # 05-00 创建合约
    @with_user_endorsers
    def create_contract(self, contract_name: str, byte_code_path: str, runtime_type: Union[RuntimeType, str],
                        params: dict = None, version: str = None, gas_limit: int = None, tx_id: str = None,
                        timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        创建合约
        :param contract_name: 合约名
        :param version: 合约版本
        :param byte_code_path: 合约字节码：可以是字节码；合约文件路径；或者 hex编码字符串；或者 base64编码字符串。
        :param runtime_type: contract_pb2.RuntimeType.WASMER
        :param params: 合约参数，dict类型，key 和 value 尽量为字符串
        :param gas_limit: Gas限制
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises ValueError: 如果 byte_code 不能转成合约字节码
        :raises: RequestError: 请求失败
        """
        payload = self._cc.create_contract_create_payload(contract_name, version, byte_code_path, runtime_type,
                                                          params, gas_limit, tx_id)

        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def invoke_contract(self, contract_name: str, method: str, params: dict = None,
                        gas_limit: int = None, tx_id: str = None, result_type: str = None,
                        timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        调用合约
        :param contract_name: 合约名
        :param method: 合约方法名
        :param params: 合约方法参数
        :param gas_limit: 交易Gas限制
        :param tx_id: 指定交易Id
        :param result_type: 结果类型, 用于解析响应中的result
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步交易执行结果。如果不同步，返回tx_id，供异步查询; 同步则循环等待，返回交易的执行结果。
        :return: TxResponse
        :raises RequestError: 请求失败
        """
        response = self._cc.invoke_contract(contract_name, method, params, tx_id, gas_limit, timeout, with_sync_result)
        return response if result_type is None else parse_result(response, result_type)

    @with_user_endorsers
    def query_contract(self, contract_name: str, method: str, params: Union[dict, list] = None, result_type: str = None,
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
        response = self._cc.query_contract(contract_name, method, params)
        return response if result_type is None else parse_result(response, result_type)

    # 05-01 升级合约
    @with_user_endorsers
    def upgrade_contract(self, contract_name: str, byte_code_path: str, runtime_type: Union[RuntimeType, str],
                         params: dict = None, version: str = None, gas_limit: int = None, tx_id: str = None,
                         timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        升级合约
        :param contract_name: 合约名
        :param version: 合约版本
        :param byte_code_path: 合约字节码：可以是字节码；合约文件路径；或者 hex编码字符串；或者 base64编码字符串。
        :param runtime_type: contract_pb2.RuntimeType.WASMER
        :param params: 合约参数，dict类型，key 和 value 尽量为字符串
        :param gas_limit: 交易Gas限制
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises ValueError: 如果 byte_code 不能转成合约字节码
        :raises: RequestError: 请求失败
        """
        payload = self._cc.create_contract_upgrade_payload(contract_name, version, byte_code_path, runtime_type,
                                                           params, gas_limit, tx_id)

        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 05-02 冻结合约
    @with_user_endorsers
    def freeze_contract(self, contract_name: str, tx_id: str = None, timeout: int = None,
                        with_sync_result: bool = None) -> TxResponse:
        """
        冻结合约
        :param contract_name: 合约名称
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求失败
        """
        payload = self._cc._create_contract_manage_payload(ContractManageMethod.FREEZE_CONTRACT.name, contract_name,
                                                           tx_id=tx_id)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 05-03 解冻合约
    @with_user_endorsers
    def unfreeze_contract(self, contract_name: str, tx_id: str = None, timeout: int = None,
                          with_sync_result: bool = None) -> TxResponse:
        """
        解冻合约
        :param contract_name: 合约名称
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求失败
        """
        payload = self._cc._create_contract_manage_payload(ContractManageMethod.UNFREEZE_CONTRACT.name, contract_name,
                                                           tx_id=tx_id)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 05-04 吊销合约
    @with_user_endorsers
    def revoke_contract(self, contract_name: str, tx_id=None, timeout: int = None,
                        with_sync_result: bool = None) -> TxResponse:
        """
        吊销合约
        :param contract_name: 合约名称
        :param tx_id: 指定交易Id
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求失败
        """
        payload = self._cc._create_contract_manage_payload(ContractManageMethod.REVOKE_CONTRACT.name, contract_name,
                                                           tx_id=tx_id)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    @with_user_endorsers
    def _gen_new_contract_version(self, contract_name: str, increase: float = 1.0) -> str:
        """
        查询合约当前版本，并生成合约新版本号
        :param contract_name: 合约名称
        :param increase: 在原版本基础上增加值，默认原版本+1
        :return: 合约版本
        """
        version = self._cc.get_contract_info(contract_name).version
        return str(float(version) + increase)

    @staticmethod
    @with_user_endorsers
    def gen_random_tx_id():
        """生成随机交易Id"""
        return gen_rand_tx_id()

    @staticmethod
    @with_user_endorsers
    def gen_random_contract_name(prefix='contract_'):
        """生成随机合约名称"""
        return gen_rand_contract_name(prefix)

    @with_user_endorsers
    def invoke_system_contract(self, contract_name: str, method: str, params: Dict[str, Union[str, int, bool]] = None,
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
        if timeout is None:
            timeout = DefaultConfig.rpc_send_tx_timeout
        if gas_limit is None:
            gas_limit = self._cc._default_gas_limit

        payload = self._cc._payload_builder.create_invoke_payload(contract_name, method, params, tx_id,
                                                                  gas_limit=gas_limit)
        response = self._cc.send_request_with_sync_result(payload, timeout=timeout, with_sync_result=with_sync_result)
        return response

    # 05-06 授权访问系统合约
    @with_user_endorsers
    def grant_native_contract_access(self, contract_list: List[str],
                                     timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        授权访问系统合约
        :param contract_list: 待授权访问的系统合约列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        params = {ParamKey.NATIVE_CONTRACT_NAME.name: json.dumps(contract_list)}
        payload = self._cc._payload_builder.create_invoke_payload(SystemContractName.CONTRACT_MANAGE.name,
                                                                  ContractManageMethod.GRANT_CONTRACT_ACCESS.name,
                                                                  params)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 05-06 吊销系统合约访问授权
    @with_user_endorsers
    def revoke_native_contract_access(self, contract_list: List[str],
                                      timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        吊销系统合约访问授权
        :param contract_list: 待吊销访问带系统合约列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        params = {ParamKey.NATIVE_CONTRACT_NAME.name: json.dumps(contract_list)}
        payload = self._cc._payload_builder.create_invoke_payload(SystemContractName.CONTRACT_MANAGE.name,
                                                                  ContractManageMethod.REVOKE_CONTRACT_ACCESS.name,
                                                                  params)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 05-07 验证系统合约访问授权
    @with_user_endorsers
    def verify_native_contract_access(self, contract_list: List[Union[SystemContractName, str]],
                                      timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        验证系统合约是否可访问
        :param contract_list: 待验证合约列表
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        params = {ParamKey.NATIVE_CONTRACT_NAME.name: json.dumps(contract_list)}
        payload = self._cc._payload_builder.create_invoke_payload(SystemContractName.CONTRACT_MANAGE.name,
                                                                  ContractManageMethod.VERIFY_CONTRACT_ACCESS.name,
                                                                  params)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 05-08 创建新的系统合约
    @with_user_endorsers
    def init_new_native_contract(self, contract_name: str, version: str,
                                 byte_code_path: str,
                                 runtime_type: Union[RuntimeType, str],
                                 params: Dict[str, Union[str, int, bool]] = None,
                                 gas_limit: int = None) -> Payload:
        """
        创建新的系统合约
        :param contract_name: 合约名
        :param version: 合约版本
        :param byte_code_path: 合约字节码：可以是字节码；合约文件路径；或者 hex编码字符串；或者 base64编码字符串。
        :param runtime_type: contract_pb2.RuntimeType.WASMER
        :param params: 合约参数，dict类型，key 和 value 尽量为字符串
        :param gas_limit: Gas交易限制
        :return: Payload
        :raises ValueError: 如果 byte_code 不能转成合约字节码
        """
        raise NotImplementedError('待实现')


# 06
class PrivateComputeOps(BaseOps):
    """隐私计算操作"""


# 07
class DposErc20Ops(BaseOps):
    """DPOS共识下ERC20操作"""

    # 07-00 查询归属人
    @with_user_endorsers
    def owner(self) -> str:  # todo get_owner
        """
        查询归属人
        <07-00-DPOS_ERC20-GET_OWNER>
        """
        return self._cc.owner()

    # 07-01 查询ERC20合约的精度
    @with_user_endorsers
    def decimals(self) -> str:
        """
        查询ERC20合约的精度
        <07-01-DPOS_ERC20-GET_DECIMALS>
        :return: 合约精度
        """
        return self._cc.decimals()

    # 07-02 转账
    @with_user_endorsers
    def transfer(self, address: str, amount: int, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        转账
        :param address: 接收Token的地址
        :param amount: 转账数量
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 请求响应
        """

        payload = self._cc.create_transfer_payload(address, amount)
        response = self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)
        return response

    # 07-03 从某个地址转账
    @with_user_endorsers
    def transfer_from(self, _from: str, to: str, amount: int, timeout: int = None,
                      with_sync_result: bool = None) -> TxResponse:
        """
        从某个地址转账
        :param address: 接收Token的地址
        :param amount: 转账数量
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 请求响应
        """

        payload = self._cc.create_transfer_from_payload(_from, to, amount)
        response = self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)
        return response
        # 07-04 查询账户余额

    # 07-04 查询账户余额
    @with_user_endorsers
    def balance_of(self, address: str) -> int:
        """
        查询账户余额
        <07-04-DPOS_ERC20-GET_BALANCEOF>
        :param address: 账户地址
        :return: 账户余额
        """
        return self._cc.balance_of(address)

    # 07-05 转账证明
    @with_user_endorsers
    def approve(self, _from: str, to: str, amount: int,
                timeout: int = None, with_sync_result: bool = None):
        payload = self._cc.create_approve_payload(_from, to, amount)
        response = self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)
        return response

    # 07-07 消耗Token
    @with_user_endorsers
    def burn(self, address: str, amount: int,
             timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        Burn Token
        :param address: 接收Token的地址
        :param amount: 发行数量
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 请求响应
        """
        payload = self._cc.create_burn_payload(address, amount)
        response = self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)
        return response

    # 07-08 发行Token
    @with_user_endorsers
    def mint(self, address: str, amount: int,
             timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        发行Token
        :param address: 接收Token的地址
        :param amount: 发行数量
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 请求响应
        """
        payload = self._cc.create_mint_payload(address, amount)
        response = self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)
        return response

    # 07-09 转移管理员权限
    @with_user_endorsers
    def transfer_ownership(self, address: str, timeout: int = None, with_sync_result: bool = None):
        """
        转移管理员权限
        :param address: 接收资产地址
        :param timeout: RPC请求超时时间
        :param with_sync_result: 是否同步轮训交易结果
        :return: 请求响应
        """
        payload = self._cc.create_transfer_ownership_payload(address)
        response = self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)
        return response

    # 07-10 查询Token总供应量
    @with_user_endorsers
    def total(self) -> str:
        """
        查询Token总供应量
        <07-10-DPOS_ERC20-GET_TOTAL_SUPPLY>
        :return:
        """
        return self._cc.total()


# 08
class DposStakeOps(BaseOps):
    """DPOS共识权益操作"""

    # 08-00 查询所有的候选人
    @with_user_endorsers
    def get_all_candidates(self) -> ValidatorVector:
        """
        查询所有的候选人
        <08-00-DPOS_STAKE-GET_ALL_CANDIDATES>
        :return: 候选人列表
        """
        return self._cc.get_all_candidates()

    # 08-01 通过地址获取验证人的信息
    @with_user_endorsers
    def get_validator_by_address(self, address: str):
        """
        通过地址获取验证人的信息
        <08-01-DPOS_STAKE-GET_VALIDATOR_BY_ADDRESS>
        :param address:
        :return:
        """
        return self._cc.get_validator_by_address(address)

    # 08-02 抵押权益到验证人
    @with_user_endorsers
    def delegate(self, address: str, amount: int) -> Delegation:  # todo 确认是否需要轮训
        """
        抵押权益到验证人
        <08-02-DPOS_STAKE-DELEGATE>
        :param address:
        :param amount:
        :return:
        """
        return self._cc.delegate(address, amount)

    # 08-03 查询指定地址的抵押信息
    @with_user_endorsers
    def get_delegations_by_address(self, address: str) -> DelegationInfo:
        """
        查询指定地址的抵押信息
        <08-03-DPOS_STAKE-GET_DELEGATIONS_BY_ADDRESS>
        :param address:
        :return:
        """
        return self._cc.get_delegations_by_address(address)

    # 08-04 查询指定地址的抵押信息
    @with_user_endorsers
    def get_user_delegation_by_validator(self, delegator: str, validator: str) -> Delegation:
        """
        查询指定地址的抵押信息
        <08-04-DPOS_STAKE-GET_USER_DELEGATION_BY_VALIDATOR>
        :param delegator:
        :param validator:
        :return:
        """
        return self._cc.get_user_delegation_by_validator(delegator, validator)

    # 08-04 从验证人解除抵押的权益
    @with_user_endorsers
    def undelegate(self, address: str, amount: int) -> Delegation:
        """
        从验证人解除抵押的权益
        <08-05-DPOS_STAKE-UNDELEGATE>
        :param address:
        :param amount:
        :return:
        """
        return self._cc.undelegate(address, amount)

    # 08-06 查询指定世代信息
    @with_user_endorsers
    def get_epoch_by_id(self, epoch_id: int) -> Epoch:
        """
        查询指定世代信息
        <08-06-DPOS_STAKE-READ_EPOCH_BY_ID>
        :param epoch_id:
        :return:
        """
        return self._cc.get_epoch_by_id(epoch_id)

    # 08-07 查询当前世代信息
    @with_user_endorsers
    def get_last_epoch(self) -> Epoch:
        """
        查询当前世代信息
        <08-07-DPOS_STAKE-READ_LATEST_EPOCH>
        :return:
        """
        return self._cc.get_last_epoch()

    # 08-08 Stake合约中设置验证人的NodeID
    @with_user_endorsers
    def set_node_id(self, node_id: str) -> str:
        """
        Stake合约中设置验证人的NodeID
        <08-08-DPOS_STAKE-SET_NODE_ID>
        :param node_id:
        :return:
        """
        return self._cc.set_node_id(node_id)

    # 08-09 Stake合约中查询验证人的NodeID
    @with_user_endorsers
    def get_node_id(self, address: str) -> str:
        """
        Stake合约中查询验证人的NodeID
        <08-09-DPOS_STAKE-GET_NODE_ID>
        :param address:
        :return:
        """
        return self._cc.get_node_id(address)

    # 08-10
    @with_user_endorsers
    def update_min_self_delegation(self):
        """
        <08-10-DPOS_STAKE-UPDATE_MIN_SELF_DELEGATION>
        :return:
        """
        pass

    # 08-11
    @with_user_endorsers
    def get_min_self_delegation(self):
        """
        <08-11-DPOS_STAKE-READ_MIN_SELF_DELEGATION>
        :return:
        """
        pass

    # 08-12
    @with_user_endorsers
    def update_epoch_validator_number(self):
        """
        <08-12-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER>
        :return:
        """
        pass

    # 08-13
    @with_user_endorsers
    def get_epoch_validator_number(self):
        """
        <08-13-DPOS_STAKE-READ_EPOCH_VALIDATOR_NUMBER>
        :return:
        """
        pass

    # 08-14
    @with_user_endorsers
    def update_epoch_block_number(self):
        """
        <08-14-DPOS_STAKE-UPDATE_EPOCH_BLOCK_NUMBER>
        :return:
        """
        pass

    # 08-15
    @with_user_endorsers
    def get_epoch_block_number(self):
        """
        <08-15-DPOS_STAKE-READ_EPOCH_BLOCK_NUMBER>
        :return:
        """
        pass

    # 08-16 查询收到解质押退款间隔的世代数
    @with_user_endorsers
    def get_unbounding_interval_epoch_number(self) -> str:
        """
        查询收到解质押退款间隔的世代数
         <08-16-DPOS_STAKE-READ_COMPLETE_UNBOUNDING_EPOCH_NUMBER>
        :return:
        """
        return self._cc.get_unbounding_interval_epoch_number()

    # 08-17 查询Stake合约的系统地址
    @with_user_endorsers
    def get_stake_contract_address(self) -> str:
        """
        查询Stake合约的系统地址
        <08-18-DPOS_STAKE-READ_SYSTEM_CONTRACT_ADDR>
        :return:
        """
        return self._cc.get_stake_contract_address()

    # 08-19
    @with_user_endorsers
    def unbounding(self):
        """
        <08-19-DPOS_STAKE-UNBOUNDING>
        :return:
        """

    # 08-20
    @with_user_endorsers
    def create_create_epoch_payload(self):
        """
        <08-20-DPOS_STAKE-CREATE_EPOCH>
        :return:
        """

    # 08-21
    @with_user_endorsers
    def update_epoch_validator_number_and_epoch_block_number(self):
        """
        <08-21-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER_AND_EPOCH_BLOCK_NUMBER>
        :return:
        """
        pass

    # todo


# 09
class SubscribeManageOps(BaseOps):
    """订阅管理操作"""


# 10
class ArchiveManageOps(BaseOps):
    """归档管理"""

    # 10-00 归档区块
    @with_user_endorsers
    def archive_block(self, target_block_height: int, timeout: int = None) -> TxResponse:
        """
        归档区块
        :param target_block_height: 目标区块高度
        :param timeout: RPC请求超时时间
        :return: 请求响应
        """
        payload = self._cc.create_archive_block_payload(target_block_height)
        return self._cc.send_archive_block_request(payload, timeout=timeout)

    # 10-01 恢复区块
    @with_user_endorsers
    def restore_block(self, full_block: bytes, timeout: int = None) -> TxResponse:
        """
        恢复区块
        :param full_block: 完整区块数据
        :param timeout: RPC请求超时时间
        :return: 请求响应
        """
        payload = self._cc.create_restore_block_payload(full_block)
        return self._cc.send_archive_block_request(payload, timeout=timeout)


# 12
class PubkeyManageOps(BaseOps):
    """公钥管理"""

    @with_user_endorsers
    def check_pubkey(self):  # todo
        pass

    # 12-00 添加公钥
    @with_user_endorsers
    def add_pubkey(self, pubkey: str, org_id: str, role: Union[Role, str], timeout: int = None,
                   with_sync_result: bool = True) -> TxResponse:
        """
        添加公钥
        :param pubkey: 公钥文件内容
        :param org_id: 组织ID
        :param role: 角色
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        payload = self._cc.create_pubkey_add_payload(pubkey, org_id, role)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 12-01 删除公钥
    @with_user_endorsers
    def delete_pubkey(self, pubkey: str, org_id: str, timeout: int = None, with_sync_result: bool = True):
        """
        删除公钥
        :param pubkey: 公钥文件内容
        :param org_id: 组织ID
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        payload = self._cc.create_pubkey_delete_payload(pubkey, org_id)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 12-02 查询公钥
    @with_user_endorsers
    def query_pubkey(self, pubkey: str, timeout: int = None) -> TxResponse:
        """
        查询公钥
        <12-02-PUBKEY_MANAGE-PUBKEY_QUERY>
        :param pubkey:公钥文件内容
        :param timeout: RPC请求超时时间
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        return self._cc.query_pubkey(pubkey, timeout)


# 13
class AccountManagerOps(BaseOps):
    """Gas管理"""

    @with_user_endorsers
    def check_gas_admin(self) -> bool:
        """
        检查当前客户端用户是否Gas管理员
        :return: 当前客户端用户是Gas管理员返回True, 否则返回False
        """
        return self._cc.user.address == self._cc.get_gas_admin()

    # 13-00
    @with_user_endorsers
    def set_gas_admin(self, address: str = None, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        设置Gas管理员地址
        :param address: 用户地址-为None时为当前用户地址
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        if address is None:
            address = self._cc.sender_address
        payload = self._cc.create_set_gas_admin_payload(address)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

        # 13-01 查询Gas管理员地址

    # 12-01 查询Gas管理员地址
    @with_user_endorsers
    def get_gas_admin(self) -> str:
        """
        查询Gas管理员地址
        <13-01-ACCOUNT_MANAGER-GET_ADMIN>
        :return: Gas管理员账户地址
        """
        return self._cc.get_gas_admin()

    # 13-02 Gas充值
    @with_user_endorsers
    def recharge_gas(self, recharge_gas_list: List[RechargeGasItem],
                     timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        Gas充值
        :param recharge_gas_list: 充值列表 [(address, amount)] 格式
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        payload = self._cc.create_recharge_gas_payload(recharge_gas_list)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 13-03 获取Gas账户余额
    @with_user_endorsers
    def get_gas_balance(self, address: str = None) -> int:
        """
        获取Gas账户余额
        <13-03-ACCOUNT_MANAGER-GET_BALANCE>
        :param str address: 账户地址
        :return: 账户余额
        """
        return self._cc.get_gas_balance()

    # 13-04 Gas收费
    @with_user_endorsers
    def charge_gas(self, recharge_gas_list: List[RechargeGasItem],
                   timeout: int = None, with_sync_result: bool = None):  # todo 待验证
        """
        Gas收费
        :param recharge_gas_list:
        :param timeout:
        :param with_sync_result:
        :return:
        """
        payload = self._cc.create_charge_gas_payload(recharge_gas_list)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 13-05 冻结Gas账户
    @with_user_endorsers
    def freeze_gas_account(self, address: str, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        冻结Gas账户
        :param address: 待冻结账户地址
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :param auto_set_gas_admin: 是否自动设置当前用户为Gas管理员
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        payload = self._cc.create_frozen_gas_account_payload(address)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 13-06 解冻Gas账户
    @with_user_endorsers
    def unfreeze_gas_account(self, address: str, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        解冻Gas账户
        :param address: 待冻结账户地址
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        payload = self._cc.create_unfrozen_gas_account_payload(address)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 13-07 查询Gas账户状态
    @with_user_endorsers
    def get_gas_account_status(self, address: str = None) -> bool:
        """
        查询Gas账户状态
        <13-07-ACCOUNT_MANAGER-ACCOUNT_STATUS>
        :param str address: 账户地址
        :return: 正常是返回True, 冻结返回False
        """
        return self._cc.get_gas_account_status(address)

    # 13-08 Gas退款
    @with_user_endorsers
    def refund_gas(self, address: str, amount: int, timeout: int = None, with_sync_result: bool = None) -> TxResponse:
        """
        Gas退款
        :param address: 退款账户地址
        :param amount: 退款金额
        :param timeout: RPC请求超时实际
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        :raises: RequestError: 请求出错
        """
        payload = self._cc.create_refund_gas_payload(address, amount)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 12-09 Gas VM 退款
    @with_user_endorsers
    def refund_gas_vm(self, address: str, amount: int, timeout: int = None,
                      with_sync_result: bool = None) -> TxResponse:  # todo 待验证
        """

        :param address:
        :param amount:
        :param timeout:
        :param with_sync_result:
        :return:
        """
        payload = self._cc.create_refund_gas_vm_payload(address, amount)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)

    # 13-10 Gas多账户收费
    @with_user_endorsers
    def charge_gas_for_multi_account(self, charge_gas_list: List[tuple],
                                     timeout: int = None, with_sync_result: bool = None):  # todo 待验证
        """

        :param charge_gas_list:
        :param timeout:
        :param with_sync_result:
        :return:
        """
        payload = self._cc.create_charge_gas_for_multi_account_payload(charge_gas_list)
        return self._cc.send_manage_request(payload, timeout=timeout, with_sync_result=with_sync_result)


# 15
class DposSlashingOps(BaseOps):
    """DPOS共识惩罚操作"""


class DposDistributionOps(BaseOps):
    """DPOS共识奖励操作"""


class ChainManager:
    """链管理客户端"""

    def __init__(self, crypto_config: CryptoConfig, server_config: dict = None):
        self.crypto_config = crypto_config
        self.server_config = server_config

        self._cc = crypto_config.new_chain_client('client1', endorsers=['admin1', 'admin2', 'admin3'])

        self.chain_config = ChainConfigOps(self._cc, self.crypto_config)  # 00
        self.chain_query = ChainQueryOps(self._cc, self.crypto_config)  # 01
        self.cert_manage = CertManageOps(self._cc, self.crypto_config)  # 02
        self.multi_sign = MultiSignOps(self._cc, self.crypto_config)  # 04
        self.contract_manage = ContractManageOps(self._cc, self.crypto_config)  # 05
        self.private_compute = PrivateComputeOps(self._cc, self.crypto_config)  # 06
        self.dpos_erc20 = DposErc20Ops(self._cc, self.crypto_config)  # 07
        self.dpos_stake = DposStakeOps(self._cc, self.crypto_config)  # 08
        self.subscribe_manage = SubscribeManageOps(self._cc, self.crypto_config)  # 09
        self.archive_manage = ArchiveManageOps(self._cc, self.crypto_config)  # 10
        self.pubkey_manage = PubkeyManageOps(self._cc, self.crypto_config)  # 12
        self.account_manager = AccountManagerOps(self._cc, self.crypto_config)  # 13
        self.dpos_slashing = DposSlashingOps(self._cc, self.crypto_config)  # 15

        self._cluster = None

    @property
    def cluster(self) -> Union[ChainMakerCluster, None]:
        if self._cluster is None and self.server_config:
            self._cluster = ChainMakerCluster.from_conf(self.server_config)
        return self._cluster

    @classmethod
    def from_host_conf(cls, host_config: dict, crypto_config_path: str = './crypto-config',
                       rpc_start_port: int = 12301):
        host = Host(**host_config)  # todo local
        chainmaker_go_path = f'{host.workspace}/chainmaker-go'
        if not os.path.exists(crypto_config_path):
            host.get_dir(f'{chainmaker_go_path}/build/crypto-config', crypto_config_path)
        return cls.from_crypto_config(crypto_config_path, host=host_config['host'],
                                      rpc_start_port=rpc_start_port, server_config=dict(host=host_config))

    @classmethod
    def from_crypto_config(cls, crypto_config_path: Union[Path, str], host: str, rpc_start_port: int = 12301,
                           server_config: dict = None):
        crypto_config = CryptoConfig(crypto_config_path, host=host, rpc_start_port=rpc_start_port)
        return cls(crypto_config=crypto_config, server_config=server_config)

    @staticmethod
    def check_response(response: TxResponse) -> bool:
        return result_utils.result_is_ok(response)
