#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   payload.py
# @Function     :   ChainMaker生成Payload


import time
from typing import Union, Dict

from chainmaker.protos.common.request_pb2 import Payload, TxType, Limit
from chainmaker.sdk_config import DefaultConfig
from chainmaker.utils import common


class PayloadBuilder:
    """Payload构建者"""

    def __init__(self, chain_id):
        self.chain_id = chain_id

    def create_invoke_payload(self, contract_name: str, method: str, params: Dict[str, Union[str, int, bool]] = None,
                              tx_id="", seq=0,
                              gas_limit: int = None) -> Payload:
        return self._create_payload(TxType.INVOKE_CONTRACT, contract_name, method, params, tx_id, seq, gas_limit)

    def create_query_payload(self, contract_name: str, method: str, params: Dict[str, Union[str, int, bool]] = None,
                             tx_id="", seq=0) -> Payload:
        return self._create_payload(TxType.QUERY_CONTRACT, contract_name, method, params, tx_id, seq)

    def create_subscribe_payload(self, contract_name: str, method: str, params: Dict[str, Union[str, int, bool]] = None,
                                 tx_id="", seq=0) -> Payload:
        return self._create_payload(TxType.SUBSCRIBE, contract_name, method, params, tx_id, seq)

    def create_archive_payload(self, contract_name: str, method: str, params: Dict[str, Union[str, int, bool]] = None,
                               tx_id: str = "", seq: int = 0) -> Payload:
        return self._create_payload(TxType.ARCHIVE, contract_name, method, params, tx_id, seq)

    # def create_contract_manage_payload(self, method: str, contract_name: str = None, version: str = None,
    #                                    byte_code: bytes = None, runtime_type: RuntimeType = None, kvs: list = None,
    #                                    seq: int = 0, gas_limit: int = None):
    #     warnings.warn('use cc._create_contract_manage_payload instead', DeprecationWarning)
    #     kvs = kvs or []
    #     if contract_name is not None:
    #         kvs.append(KeyValuePair(key=ParamKey.CONTRACT_NAME.name, value=contract_name.encode()))
    #     if version is not None:
    #         kvs.append(KeyValuePair(key=ParamKey.CONTRACT_VERSION.name, value=version.encode()))
    #     if runtime_type is not None:
    #         kvs.append(KeyValuePair(key=ParamKey.CONTRACT_RUNTIME_TYPE.name, value=runtime_type.encode()))
    #     if byte_code is not None:
    #         if runtime_type == RuntimeType.EVM:
    #             byte_code = bytes.fromhex(byte_code.decode())  # EMV byte_code需要转为hex
    #         kvs.append(KeyValuePair(key=ParamKey.CONTRACT_BYTECODE, value=byte_code))
    #     return self.create_invoke_payload(SystemContractName.CONTRACT_MANAGE.name, method, kvs, seq=seq,
    #                                       gas_limit=gas_limit)

    def _create_payload(self, tx_type: TxType, contract_name: str, method: str, params: Union[dict, list] = None,
                        tx_id="", seq=0, gas_limit: int = None) -> Payload:
        tx_id = tx_id or common.gen_rand_tx_id()
        kv_pairs = common.params_map_kv_pairs(params)
        if gas_limit is None:
            gas_limit = DefaultConfig.gas_limit
        return Payload(chain_id=self.chain_id, tx_type=tx_type, tx_id=tx_id, timestamp=int(time.time()),
                       contract_name=contract_name, method=method, parameters=kv_pairs, sequence=seq,
                       limit=Limit(gas_limit=gas_limit))
