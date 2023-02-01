#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   system_contract.py
# @Function     :   ChainMaker系统合约(链获取相关)接口
from typing import Dict, Union, List

from chainmaker.apis.base_client import BaseClient
from chainmaker.keys import (ParamKey, SystemContractName, ChainQueryMethod)
from chainmaker.protos import (Payload, TxResponse, BlockHeader, BlockInfo, BlockWithRWSet,
                               TransactionInfo, TransactionWithRWSet,
                               ChainList, ChainInfo, Contract)


class ChainQueryMixIn(BaseClient):
    """链查询操作"""
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
        self._debug("begin to GetBlockByTxId, [tx_id:%s]/[with_rw_set:%s]" % (tx_id, with_rw_set))

        params = {ParamKey.txId.name: tx_id,
                  ParamKey.withRWSet.name: with_rw_set}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_BLOCK_BY_TX_ID.name, params)

        response = self.send_request(payload)
        self._parse_block_info(response)

    # 01-01 通过交易Id获取交易信息
    def get_tx_by_tx_id(self, tx_id: str) -> TransactionInfo:
        """
        通过交易Id获取交易信息
        <01-01-CHAIN_QUERY-GET_TX_BY_TX_ID>
        :param tx_id: 交易Id，类型为字符串
        :return: Result
        :raises RequestError: 请求失败
        """
        self._debug("begin to GetTxByTxId, [tx_id:%s]" % tx_id)

        params = {ParamKey.txId.name: tx_id}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_TX_BY_TX_ID.name, params)

        tx_response = self.send_request(payload)
        data = tx_response.contract_result.result

        transaction_info = TransactionInfo()
        transaction_info.ParseFromString(data)
        return transaction_info

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
        self._debug("begin to GetBlockByHeight, [block_height:%s]/[with_rw_set:%s]" % (block_height, with_rw_set))
        params = {
            ParamKey.blockHeight.name: block_height,
            ParamKey.withRWSet.name: with_rw_set
        }
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_BLOCK_BY_HEIGHT.name, params)
        response = self.send_request(payload)
        return self._parse_block_info(response)

    # 01-03 获取链信息
    def get_chain_info(self) -> ChainInfo:
        """
        获取链信息
        <01-03-CHAIN_QUERY-GET_CHAIN_INFO>
        :return: ChainInfo
        :raises RequestError: 请求失败
        """
        self._debug('begin to GetChainInfo')
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_CHAIN_INFO.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        chain_info = ChainInfo()
        chain_info.ParseFromString(data)
        return chain_info

    def get_tx_with_rwset_by_tx_id(self, tx_id: str) -> TransactionWithRWSet:
        """
        通过交易Id获取带读写集交易信息
        :param tx_id: 交易Id，类型为字符串
        :return: Result
        :raises RequestError: 请求失败
        """
        self._debug("begin to GetTxWithRWSetByTxId, [tx_id:%s]" % tx_id)
        params = {ParamKey.txId.name: tx_id,
                  ParamKey.withRWSet.name: True}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_TX_BY_TX_ID.name, params)

        response = self.send_request(payload)

        data = response.contract_result.result
        transaction_info = TransactionWithRWSet()
        transaction_info.ParseFromString(data)

        return transaction_info

    # 01-04 获取最新的配置块
    def get_last_config_block(self, with_rw_set: bool = False) -> BlockInfo:
        """
        获取最新的配置块
        <01-04-CHAIN_QUERY-GET_LAST_CONFIG_BLOCK>
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """
        self._debug("begin to GetLastConfigBlock, [with_rw_set:%s]" % with_rw_set)

        params = {ParamKey.withRWSet.name: with_rw_set}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_LAST_CONFIG_BLOCK.name, params)
        response = self.send_request(payload)
        return self._parse_block_info(response)

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
        self._debug("begin to GetBlockByHash, [block_hash:%s]/[with_rw_set:%s]" % (block_hash, with_rw_set))

        params = {ParamKey.blockHash.name: block_hash,
                  ParamKey.withRWSet.name: with_rw_set}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_BLOCK_BY_HASH.name,
                                                   params)

        response = self.send_request(payload)
        return self._parse_block_info(response)

    # 01-06 获取节点加入的链列表
    def get_node_chain_list(self) -> ChainList:
        """
        获取节点加入的链列表
        <01-06-CHAIN_QUERY-GET_NODE_CHAIN_LIST>
        :return: 链Id列表
        :raises RequestError: 请求失败
        """
        self._debug("begin to GetNodeChainList")

        payload = self._create_chain_query_payload(ChainQueryMethod.GET_NODE_CHAIN_LIST.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        chain_list = ChainList()
        chain_list.ParseFromString(data)
        return chain_list

    # 01-07 获取统治合约
    def get_governance_contract(self):
        """
        获取统治合约
        <01-07-CHAIN_QUERY-GET_GOVERNANCE_CONTRACT>
        :return:
        """
        raise NotImplementedError('the method does not found')
        # self._debug("begin to GetGovernanceContract")
        #
        # payload = self._create_chain_query_payload(ChainQueryMethod.GET_GOVERNANCE_CONTRACT.name)
        # response = self.send_request(payload)
        #
        # data = response.contract_result.result
        # contract_data = json.loads(data)
        # return self._parse_contract(contract_data)

    # 01-08 通过区块高度获取带读写集区块信息
    def get_block_with_tx_rw_sets_by_height(self, block_height: int) -> BlockWithRWSet:
        """
        通过区块高度获取带读写集区块信息
        <01-08-CHAIN_QUERY-GET_BLOCK_WITH_TXRWSETS_BY_HEIGHT>
        :param block_height: 区块高度
        :return: 带读写集区块信息
        """
        self._debug("begin to GetBlockWithRWSetsByHeight, [block_height:%s]" % block_height)
        params = {ParamKey.blockHeight.name: block_height}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_BLOCK_WITH_TXRWSETS_BY_HEIGHT.name, params)
        response = self.send_request(payload)
        data = response.contract_result.result
        block_info_with_rw_set = BlockWithRWSet()
        block_info_with_rw_set.ParseFromString(data)
        return block_info_with_rw_set

    # 01-09 通过区块哈希获取带读写集区块信息
    def get_block_with_tx_rw_sets_by_hash(self, block_hash: str) -> BlockWithRWSet:
        """
        通过区块哈希获取带读写集区块信息
         <01-09-CHAIN_QUERY-GET_BLOCK_WITH_TXRWSETS_BY_HASH>
        :param block_hash: 区块哈希
        :return: 带读写集区块信息
        """
        self._debug("begin to GetBlockByHash, [block_hash:%s]" % block_hash)

        params = {ParamKey.blockHash.name: block_hash}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_BLOCK_WITH_TXRWSETS_BY_HASH.name, params)

        response = self.send_request(payload)
        data = response.contract_result.result
        block_info_with_rw_set = BlockWithRWSet()
        block_info_with_rw_set.ParseFromString(data)
        return block_info_with_rw_set

    # 01-10 获取最新区块信息
    def get_last_block(self, with_rw_set: bool = False) -> BlockInfo:
        """
        获取最新区块信息
        <01-10-CHAIN_QUERY-GET_LAST_BLOCK>
        :param with_rw_set: 是否返回读写集数据
        :return: BlockInfo
        :raises RequestError: 请求失败
        """
        self._debug("begin to GetLastBlock, [with_rw_set:%s]" % with_rw_set)

        params = {ParamKey.withRWSet.name: with_rw_set}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_LAST_BLOCK.name, params)
        response = self.send_request(payload)
        return self._parse_block_info(response)

    # 01-11 通过区块高度获取完整区块信息
    def get_full_block_by_height(self, block_height: int) -> BlockWithRWSet:
        """
        通过区块高度获取完整区块信息
        <01-11-CHAIN_QUERY-GET_FULL_BLOCK_BY_HEIGHT>
        :param block_height: 区块高度
        :return: BlockInfo
        :raises RequestError: 请求失败
        """
        self._debug("begin to GetFullBlockHeight, [block_height:%s]" % block_height)

        params = {ParamKey.blockHeight.name: str(block_height)}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_FULL_BLOCK_BY_HEIGHT.name, params)
        response = self.send_request(payload)

        block_with_rw_set = BlockWithRWSet()
        block_with_rw_set.ParseFromString(response.contract_result.result)
        return block_with_rw_set

    # 01-12 通过交易Id获取区块高度
    def get_block_height_by_tx_id(self, tx_id: str) -> int:
        """
        通过交易Id获取区块高度
        <01-12-CHAIN_QUERY-GET_BLOCK_HEIGHT_BY_TX_ID>
        :param tx_id: 交易Id
        :return: 区块高度
        :raises RequestError: 请求失败
        """
        self._debug("begin to GetBlockHeightByTxId, [tx_id:%s]" % tx_id)

        params = {ParamKey.txId.name: tx_id}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_BLOCK_HEIGHT_BY_TX_ID.name, params)
        response = self.send_request(payload)

        block_height = response.contract_result.result

        return int(block_height)

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
        self._debug("begin to GetBlockHeightByHash, [block_hash:%s]" % block_hash)

        params = {ParamKey.blockHash.name: block_hash}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_BLOCK_HEIGHT_BY_HASH.name, params)
        response = self.send_request(payload)
        block_height = response.contract_result.result
        return int(block_height)

    # 01-14 通过高度获取区块头
    def get_block_header_by_height(self, block_height: int) -> BlockHeader:
        """
        通过高度获取区块头
        <01-14-CHAIN_QUERY-GET_BLOCK_HEADER_BY_HEIGHT>
        :param block_height: 区块高度
        :return: 区块头
        """
        params = {ParamKey.blockHeight.name: block_height}
        self._debug("begin to GetBlockHeaderByHeight, [block_height:%s]" % block_height)

        payload = self._create_chain_query_payload(ChainQueryMethod.GET_BLOCK_HEADER_BY_HEIGHT.name, params)
        response = self.send_request(payload)
        data = response.contract_result.result
        block_header = BlockHeader()
        block_header.ParseFromString(data)
        return block_header

    # 01-15 获取已归档的区块高度
    def get_archived_block_height(self) -> int:
        """
        获取已归档的区块高度
         <01-15-CHAIN_QUERY-GET_ARCHIVED_BLOCK_HEIGHT>
        :return: 区块高度
        :raises RequestError: 请求失败
        """
        self._debug("begin to GetArchiveBlockHeight")
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_ARCHIVED_BLOCK_HEIGHT.name)
        response = self.send_request(payload)
        block_height = response.contract_result.result
        return int(block_height)

    # 01-16 获取全部合约信息
    def get_all_contracts(self) -> List[Contract]:
        """
        获取全部合约信息
        <01-16-CHAIN_QUERY-GET_ALL_CONTRACTS>
        :return: 合约Contract对象列表
        :raise: RequestError: 请求出错
        :raise: AssertionError: 响应code不为0,检查响应时抛出断言失败
        :raise: 当数据不是JSON格式时，抛出json.decoder.JSONDecodeError
        """
        raise NotImplementedError('the method does not found')
        # self._debug("begin to GetAllContracts")
        # payload = self._create_chain_query_payload(ChainQueryMethod.GET_ALL_CONTRACTS.name)
        #
        # response = self.send_request(payload)
        # contract_list = json.loads(response.contract_result.result)
        # contracts = [self._parse_contract(contract_data) for contract_data in contract_list]
        # return contracts

    # 01-17 通过交易Id获取Merkle树路径
    def get_merkle_path_by_tx_id(self, tx_id: str) -> bytes:
        """
        通过交易Id获取Merkle树路径
        <01-17-CHAIN_QUERY-GET_MERKLE_PATH_BY_TX_ID>
        :param tx_id: 交易Id
        :return: Merkle树路径
        """
        self._debug("begin to GetMerklePathByTxId, [tx_id:%s]" % tx_id)

        params = {ParamKey.txId.name: tx_id}
        payload = self._create_chain_query_payload(ChainQueryMethod.GET_MERKLE_PATH_BY_TX_ID.name, params)
        response = self.send_request(payload)
        return response.contract_result.result

    def get_block_height(self, tx_id: str = None, block_hash: str = None) -> int:  # todo
        """
        通过交易Id或区块hash获取区块高度
        :param tx_id: 交易Id
        :param block_hash: 区块hash
        :return: 区块高度
        """
        if tx_id is None and block_hash is None:
            raise ValueError('tx_id和block_hash最少需要其中一个')
        return self.get_block_height_by_tx_id(tx_id) if tx_id else self.get_block_height_by_hash(block_hash)

    def get_current_block_height(self) -> int:
        """
        获取当前区块高度
        :return: 区块高度
        """
        self._debug("begin to GetCurrentBlockHeight")
        return self.get_last_block(with_rw_set=False).block.header.block_height

    def _create_chain_query_payload(self, method: str, params: Dict[str, Union[str, int, bool]] = None) -> Payload:
        """
        创建链获取待签名请求
        :param method: 链获取方法
        :param params: 获取参数
        :return: 待签名Payload
        """
        return self._payload_builder.create_query_payload(SystemContractName.CHAIN_QUERY.name, method, params)

    @staticmethod
    def _parse_block_info(response: TxResponse) -> BlockInfo:
        data = response.contract_result.result
        block_info = BlockInfo()
        block_info.ParseFromString(data)
        return block_info
