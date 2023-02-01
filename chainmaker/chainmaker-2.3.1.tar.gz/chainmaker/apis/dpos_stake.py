#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   dpos.py
# @Function     :   ChainMaker DPOS ERC20 / DPOS Stake 等操作接口

from chainmaker.apis.base_client import BaseClient
from chainmaker.keys import (SystemContractName, DposStakeMethod, ParamKey, DposSlashingMethod)
from chainmaker.protos import (ValidatorVector, Epoch, Delegation, DelegationInfo, Validator)
from chainmaker.protos.common.result_pb2 import TxResponse


class DPosStakeMixIn(BaseClient):
    """DPos权益操作"""

    # 08-00 查询所有的候选人
    def get_all_candidates(self) -> ValidatorVector:  # ✅
        """
        查询所有的候选人
        <08-00-DPOS_STAKE-GET_ALL_CANDIDATES>
        :return: 候选人列表
        """
        self._debug('begin to get all candidates')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.GET_ALL_CANDIDATES.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        vectors = ValidatorVector()
        vectors.ParseFromString(data)
        return vectors

    # 08-01 通过地址获取验证人的信息
    def get_validator_by_address(self, address: str):  # ✅
        """
        通过地址获取验证人的信息
        <08-01-DPOS_STAKE-GET_VALIDATOR_BY_ADDRESS>
        :param address:
        :return:
        """
        self._debug('begin to get validator by address %s' % address)
        params = {
            ParamKey.address.name: address
        }
        payload = self._payload_builder.create_query_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.GET_VALIDATOR_BY_ADDRESS.name,
            params)

        response = self.send_request(payload)
        data = response.contract_result.result
        validator = Validator()
        validator.ParseFromString(data)
        return validator

    # 08-02 抵押权益到验证人
    def delegate(self, address: str, amount: int) -> Delegation:  # fixme 无结果
        """
        抵押权益到验证人
        <08-02-DPOS_STAKE-DELEGATE>
        :param address:
        :param amount:
        :return:
        """
        self._debug('begin to delegate %s %s' % (address, amount))
        params = {
            ParamKey.to.name: address,
            ParamKey.amount.name: str(amount)
        }
        payload = self._payload_builder.create_invoke_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.DELEGATE.name,
            params)

        response = self.send_request(payload)
        data = response.contract_result.result
        delegation = Delegation()
        delegation.ParseFromString(data)
        return delegation

    # 08-03 查询指定地址的抵押信息
    def get_delegations_by_address(self, address: str) -> DelegationInfo:  # ✅
        """
        查询指定地址的抵押信息
        <08-03-DPOS_STAKE-GET_DELEGATIONS_BY_ADDRESS>
        :param address:
        :return:
        """
        self._debug('begin to get delegation by address %s' % address)
        params = {
            ParamKey.address.name: address
        }
        payload = self._payload_builder.create_query_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.GET_DELEGATIONS_BY_ADDRESS.name,
            params)
        response = self.send_request(payload)
        data = response.contract_result.result
        delegate_info = DelegationInfo()
        delegate_info.ParseFromString(data)
        return delegate_info

    # 08-04 查询指定地址的抵押信息
    def get_user_delegation_by_validator(self, delegator: str, validator: str) -> Delegation:  # ✅
        """
        查询指定地址的抵押信息
        <08-04-DPOS_STAKE-GET_USER_DELEGATION_BY_VALIDATOR>
        :param delegator:
        :param validator:
        :return:
        """
        self._debug('begin to get delegation by address %s %s' % (delegator, validator))
        params = {
            ParamKey.delegator_address.name: delegator,
            ParamKey.validator_address.name: validator,
        }
        payload = self._payload_builder.create_query_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.GET_USER_DELEGATION_BY_VALIDATOR.name,
            params)
        response = self.send_request(payload)
        data = response.contract_result.result
        delegation = Delegation()
        delegation.ParseFromString(data)
        return delegation

    # 08-04 从验证人解除抵押的权益
    def undelegate(self, address: str, amount: int) -> Delegation:  # fixme 无结果
        """
        从验证人解除抵押的权益
        <08-05-DPOS_STAKE-UNDELEGATE>
        :param address:
        :param amount:
        :return:
        """
        self._debug('begin to undelegate %s %s' % (address, amount))
        params = {
            ParamKey._from.name: address,
            ParamKey.amount.name: str(amount)
        }
        payload = self._payload_builder.create_invoke_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.UNDELEGATE.name,
            params)

        response = self.send_request(payload)
        data = response.contract_result.result
        delegation = Delegation()
        delegation.ParseFromString(data)
        return delegation

    # 08-06 查询指定世代信息
    def get_epoch_by_id(self, epoch_id: int) -> Epoch:  # ✅
        """
        查询指定世代信息
        <08-06-DPOS_STAKE-READ_EPOCH_BY_ID>
        :param epoch_id: 世代Id eg. 0
        :return:
        """
        self._debug('begin to get epoch by id %s' % epoch_id)
        params = {
            ParamKey.epoch_id.name: epoch_id
        }
        payload = self._payload_builder.create_query_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.READ_EPOCH_BY_ID.name,
            params)
        response = self.send_request(payload)
        data = response.contract_result.result
        epoch = Epoch()
        epoch.ParseFromString(data)
        return epoch

    # 08-07 查询当前世代信息
    def get_last_epoch(self) -> Epoch:  # ✅
        """
        查询当前世代信息
        <08-07-DPOS_STAKE-READ_LATEST_EPOCH>
        :return:
        """
        self._debug('begin to get last epoch')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_LATEST_EPOCH.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        epoch = Epoch()
        epoch.ParseFromString(data)
        return epoch

    # 08-08 Stake合约中设置验证人的NodeID
    def set_node_id(self, node_id: str, with_sync_result: bool = True) -> TxResponse:  # ✅
        """
        Stake合约中设置验证人的NodeId
        <08-08-DPOS_STAKE-SET_NODE_ID>
        :param node_id: 节点Id
        :param with_sync_result: 是否同步轮询交易结果
        :return: 交易响应
        """
        self._debug('begin to set node id')
        params = {
            ParamKey.node_id.name: node_id
        }
        payload = self._payload_builder.create_invoke_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.SET_NODE_ID.name,
            params)
        response = self.send_request_with_sync_result(payload) if with_sync_result else self.send_request(payload)
        return response

    # 08-09 Stake合约中查询验证人的NodeId
    def get_node_id(self, address: str) -> str:  # ✅
        """
        Stake合约中查询验证人的NodeID
        <08-09-DPOS_STAKE-GET_NODE_ID>
        :param address:
        :return:
        """
        self._debug('begin to get node id')
        params = {
            ParamKey.address.name: address
        }
        payload = self._payload_builder.create_query_payload(
            SystemContractName.DPOS_STAKE.name,
            DposStakeMethod.GET_NODE_ID.name,
            params)

        response = self.send_request(payload)
        data = response.contract_result.result
        return data.decode()

    # 08-10 更新验证人节点的最少自我抵押数量
    def update_min_self_delegation(self):  # todo
        """
        更新验证人节点的最少自我抵押数量
        <08-10-DPOS_STAKE-UPDATE_MIN_SELF_DELEGATION>
        :return:
        """
        pass

    # 08-11 查询验证人节点的最少自我抵押数量
    def get_min_self_delegation(self) -> int:  # ✅
        """
        查询验证人节点的最少自我抵押数量
        <08-11-DPOS_STAKE-READ_MIN_SELF_DELEGATION>
        :return:
        """
        self._debug('begin to get min self delegation')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_EPOCH_VALIDATOR_NUMBER.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return int(data)

    # 08-12 更新世代中的验证人数
    def update_epoch_validator_number(self):  # todo
        """
        更新世代中的验证人数
        <08-12-DPOS_STAKE-UPDATE_EPOCH_VALIDATOR_NUMBER>
        :return:
        """
        pass

    # 08-13 查询世代中的验证人数
    def get_epoch_validator_number(self) -> int:  # ✅
        """
        查询世代中的验证人数
        <08-13-DPOS_STAKE-READ_EPOCH_VALIDATOR_NUMBER>
        :return:
        """
        self._debug('begin to get epoch validator number')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_EPOCH_VALIDATOR_NUMBER.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return int(data.decode())

    # 08-14 更新世代中的区块数量
    def update_epoch_block_number(self):  # todo
        """
        更新世代中的区块数量
        <08-14-DPOS_STAKE-UPDATE_EPOCH_BLOCK_NUMBER>
        :return:
        """
        pass

    # 08-15 查询世代中的区块数量
    def get_epoch_block_number(self) -> int:  # ✅
        """
        查询世代中的区块数量
        <08-15-DPOS_STAKE-READ_EPOCH_BLOCK_NUMBER>
        :return:
        """
        self._debug('begin to get epoch block number')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_EPOCH_BLOCK_NUMBER.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return int(data.decode())

    # 08-16 查询收到解质押退款间隔的世代数
    def get_unbounding_interval_epoch_number(self) -> int:  # ✅
        """
        查询收到解质押退款间隔的世代数
        <08-16-DPOS_STAKE-READ_COMPLETE_UNBOUNDING_EPOCH_NUMBER>
        :return:
        """
        self._debug('begin to get unbounding interval epoch number')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_COMPLETE_UNBOUNDING_EPOCH_NUMBER.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return int(data.decode())

    # 08-17 查询Stake合约的系统地址
    def get_stake_contract_address(self) -> str:  # ✅
        """
        查询Stake合约的系统地址
        <08-18-DPOS_STAKE-READ_SYSTEM_CONTRACT_ADDR>
        :return:
        """
        self._debug('begin to get state contract address')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_STAKE.name,
                                                             DposStakeMethod.READ_SYSTEM_CONTRACT_ADDR.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return data.decode()

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


class DPosDistributionMixIn(BaseClient):
    """DPos共识奖励"""

    # 14-00
    def reward(self):
        """
        <14-00-DPOS_DISTRIBUTION-REWARD>
        :return:
        """

    # 14-01
    def get_distribution_detail(self):
        """
        <14-01-DPOS_DISTRIBUTION-GET_DISTRIBUTION_DETAIL>
        :return:
        """

    # 14-02
    def set_distribution_per_block(self):
        """
        <14-02-DPOS_DISTRIBUTION-SET_DISTRIBUTION_PER_BLOCK>
        :return:
        """

    # 14-03
    def get_distribution_per_block(self):
        """
        <14-03-DPOS_DISTRIBUTION-GET_DISTRIBUTION_PER_BLOCK>
        :return:
        """

    # 14-04
    def set_distribution_for_slashing(self):
        """
        <14-04-DPOS_DISTRIBUTION-SET_DISTRIBUTION_FROM_SLASHING>
        :return:
        """

    # 14-05
    def get_distribution_for_slashing(self):
        """
        <14-05-DPOS_DISTRIBUTION-GET_DISTRIBUTION_FROM_SLASHING>
        :return:
        """

    # 14-06
    def set_gas_exchange_rage(self):
        """
        <14-06-DPOS_DISTRIBUTION-SET_GAS_EXCHANGE_RATE>
        :return:
        """

    # 14-07
    def get_gas_exchange_rage(self):
        """
        <14-07-DPOS_DISTRIBUTION-SET_GAS_EXCHANGE_RATE>
        :return:
        """


class DPosSlashingMixIn(BaseClient):
    """DPos共识惩罚操作"""

    # 15-00
    def punish(self):  # todo
        """
        <15-00-DPOS_SLASHING-PUNISH>
        :return:
        """

    # 15-01
    def set_slashing_per_block(self):  # todo
        """
        <15-02-DPOS_SLASHING-SET_SLASHING_PER_BLOCK>
        :return:
        """

    # 15-02
    def get_slashing_per_block(self):  # todo
        """
        <15-03-DPOS_SLASHING-GET_SLASHING_PER_BLOCK>
        :return:
        """
        self._debug('begin to get slashing per block')

    # 15-03
    def get_slashing_balance(self) -> str:
        """
        查询惩罚账户余额
        <15-04-DPOS_SLASHING-GET_SLASHING_ADDRESS_BALANCE>
        :return:
        """
        self._debug('begin to get slashing balance')
        payload = self._payload_builder.create_query_payload(SystemContractName.DPOS_SLASHING.name,
                                                             DposSlashingMethod.GET_SLASHING_ADDRESS_BALANCE.name)
        response = self.send_request(payload)
        data = response.contract_result.result
        return data.decode()

    # 15-04
    def get_slashing_detail(self):  # todo
        """
        <15-05-DPOS_SLASHING-GET_SLASHING_DETAIL>
        :return:
        """
        self._debug('begin to get slashing detail')


class DPosStakeWithEndorsers(BaseClient):

    # 08-02 抵押权益到验证人
    def delegate(self, address: str, amount: int) -> Delegation:  # todo 确认是否需要轮训
        """
        抵押权益到验证人
        <08-02-DPOS_STAKE-DELEGATE>
        :param address:
        :param amount:
        :return:
        """
        return super().delegate(address, amount)

    # 08-04 从验证人解除抵押的权益
    def undelegate(self, address: str, amount: int) -> Delegation:
        """
        从验证人解除抵押的权益
        <08-05-DPOS_STAKE-UNDELEGATE>
        :param address:
        :param amount:
        :return:
        """
        return super().undelegate(address, amount)

    # 08-06 查询指定世代信息
    def get_epoch_by_id(self, epoch_id: str) -> Epoch:
        """
        查询指定世代信息
        <08-06-DPOS_STAKE-READ_EPOCH_BY_ID>
        :param epoch_id:
        :return:
        """
        return super().get_epoch_by_id(epoch_id)

    # 08-07 查询当前世代信息
    def get_last_epoch(self) -> Epoch:
        """
        查询当前世代信息
        <08-07-DPOS_STAKE-READ_LATEST_EPOCH>
        :return:
        """
        return super().get_last_epoch()

    # 08-08 Stake合约中设置验证人的NodeId
    def set_node_id(self, node_id: str) -> str:
        """
        Stake合约中设置验证人的NodeId
        <08-08-DPOS_STAKE-SET_NODE_ID>
        :param node_id:
        :return:
        """
        return super().set_node_id(node_id)

    # 08-10
    def update_min_self_delegation(self):
        """
        <08-10-DPOS_STAKE-UPDATE_MIN_SELF_DELEGATION>
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

    # 08-19
    def unbounding(self):
        """
        <08-19-DPOS_STAKE-UNBOUNDING>
        :return:
        """
