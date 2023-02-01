#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) THL A29 Limited, a Tencent company. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# @FileName     :   result_utils.py
# @Function     :   ChainMaker 结果处理实用方法
import base64
import functools
import json
import re
from typing import Union, Iterable

from google.protobuf import json_format
from google.protobuf.message import Message

from chainmaker.keys import ResultMessageType, ResultType, ContractResultType
from chainmaker.protos import TxResponse, Result, TransactionInfo

# from google.protobuf.pyext._message import RepeatedCompositeContainer

SUCCESS_CODE = 0


def version_to_num(version: str) -> int:
    """版本转数字 eg. v2.3.0 -> 2300"""
    version, *_ = re.findall(r'v(\d+\.\d+\.\d+)', version)
    versions = version.split('.')
    version_num = int(versions[0]) * 1000 + int(versions[1]) * 100 + int(versions[2])
    return version_num


def result_is_ok(response: Union[TxResponse, Result]) -> bool:
    """
    检查合约是否成功
    :param Union[TxResponse, Transaction] resp: 响应信息
    :param need_contract_result: 是否需要交易合约结果
    :return: 成功返回True, 否则返回False
    """
    if response is None:
        return True

    if hasattr(response, 'code') and SUCCESS_CODE != response.code:
        return False

    if isinstance(response, TxResponse):
        if hasattr(response, 'result') and hasattr(response.result, 'code') and SUCCESS_CODE != response.result.code:
            return False
        if hasattr(response, 'contract_result') and SUCCESS_CODE != response.contract_result.code:
            return False

    if isinstance(response, Result):
        result = response
        if SUCCESS_CODE != result.code:
            return False
        if hasattr(result, 'contract_result') and SUCCESS_CODE != result.contract_result.code:
            return False

    if isinstance(response, TransactionInfo):
        result = response.transaction.result
        if SUCCESS_CODE != result.code:
            return False
        if hasattr(result, 'contract_result') and SUCCESS_CODE != result.contract_result.code:
            return False

    return True


def check_response(response: Union[TxResponse, Result]):
    """
    检查合约是否成功
    :param Union[TxResponse, Transaction] resp: 响应信息
    :param need_contract_result: 是否需要交易合约结果
    :return: None
    """
    assert result_is_ok(response), f'响应失败: {response}'


def assert_success(response: Union[TxResponse, Result]):
    """
    检查合约是否成功
    :param Union[TxResponse, Transaction] resp: 响应信息
    :param need_contract_result: 是否需要交易合约结果
    :return: None
    """
    assert result_is_ok(response), f'响应失败: {response}'


def assert_is_forbidden(ex):
    assert 'is forbidden to access' in str(ex)


def assert_contract_fail(response: Union[TxResponse, Result]):
    """
    检查合约是否成功
    :param Union[TxResponse, Transaction] resp: 响应信息
    :param need_contract_result: 是否需要交易合约结果
    :return: None
    """
    assert response.code == 4


def msg_to_dict(msg: Union[Message, str, int, list]) -> Union[dict, str, int, list]:
    """
    proto消息体转字典
    :param msg: 消息体，如TxResponse, Result, BlockInfo等
    :return: 字典，bytes类型会转为base64字符串
    """
    if isinstance(msg, Message):
        return json_format.MessageToDict(msg)
    if isinstance(msg, Iterable):
        return [msg_to_dict(item) for item in msg]
    return msg


def msg_to_json(msg: Union[Message, str, int, list]) -> Union[str, int]:
    """
    proto消息体转JSON字符串
    :param msg: 消息体，如TxResponse, Result, BlockInfo等
    :return: JSON字符串，bytes类型会转为base64字符串
    """
    if isinstance(msg, Message):
        return json_format.MessageToJson(msg)
    if isinstance(msg, list):
        return json.dumps([msg_to_dict(item) for item in msg])
    return msg


def ensure_message_type(msg: Union[Message, str, int, list], message_type: ResultMessageType):
    """
    转换msg类型
    :param msg: 消息体
    :param message_type:
    :return:
    """
    if message_type == ResultMessageType.MESSAGE:
        return msg
    if message_type == ResultMessageType.DICT:
        return msg_to_dict(msg)
    if message_type == ResultMessageType.JSON:
        return msg_to_json(msg)
    return msg


def bytes_to_hex(data: bytes) -> str:
    """
    用于result中的bytes转16进制字符串
    :param data: 二进制数据，如bytes_to_hex(block_info.block.header.block_hash)可以得到区块哈希
    :return: 16进制字符串
    """
    return data.hex()


def bytes_to_str(data: bytes) -> str:
    """
    用于result中的bytes转字符串
    :param data:bytes字符串
    :return: 对应的字符串
    """
    return data.decode()


def bytes_to_int(data: bytes) -> int:
    """
    用于result中的bytes转整形
    :param data: bytes字符串
    :return: 整形
    :raises ValueError 如果bytes不是纯数字形式
    """
    return int(data.hex(), 16)


def base64_to_hex(data: str) -> str:
    """
    用于将MessageToDict或MessageToJson转换后的结果中的base64还原成bytes并转为16进制字符串
    :param data: 由bytes转为的base64字符串
    :return: 16进制字符串
    """
    return base64.b64decode(data).hex()


def base64_to_block_hash(block_hash_base64: str):
    """base64形式的block_hash转hex形式的block_hash"""
    return base64_to_hex(block_hash_base64)


def base64_to_str(result: str) -> str:
    """
    用于将MessageToDict或MessageToJson转换后的结果中的base64还原成bytes并转为字符串
    :param result: 由bytes转为的base64字符串
    :return: 原字符串
    """
    return base64.b64decode(result).strip(b' \x00\x1e').strip(b'\x03').decode()


def base64_to_int(result: str) -> int:
    """
    用于将MessageToDict或MessageToJson转换后的结果中的base64还原成bytes并转为整形
    :param result: 由bytes转为的base64字符串
    :return: 整数
    """
    return int(base64.b64decode(result).hex(), 16)


def base64_to_dict(result: str) -> dict:
    """
    用于将MessageToDict或MessageToJson转换后的结果中的base64还原成bytes, 转为字符串并按JSON格式转为字典
    :param result: 由bytes转为的base64字符串
    :return: 原字符串
    """
    return json.loads(base64_to_str(result))


def parse_result(response: Union[TxResponse, dict],
                 result_type: Union[ContractResultType, str] = ContractResultType.STRING):
    """
    解析交易响应中的result
    :param response: 交易响应结构体或MessageToDict后的字典
    :param result_type: 'str'/ 'int' / 'json' 转为字符串、整型、字典格式
    :return: 如果响应中不存在result则返回愿响应，否则按指定格式返回转换后的result信息
    """
    if isinstance(result_type, str):
        result_type = ContractResultType(result_type)

    if isinstance(response, TxResponse):
        response = msg_to_dict(response)

    if isinstance(response, dict):
        result = response.get('contractResult', {}).get('result')
        if not result:
            return response
        if result_type == ContractResultType.STRING:
            return base64_to_str(result)
        if result_type == ContractResultType.INT:
            return base64_to_int(result)
        if result_type == ContractResultType.JSON:
            return base64_to_dict(result)
        if result_type == ContractResultType.HEX:
            return base64_to_hex(result)
    return response


def result_or_err_msg(func):
    """装饰器：返回正常结果或错误信息"""

    @functools.wraps(func)
    def _func(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as err:
            return str(err)
        else:
            return res

    return _func


def result_and_err_msg(func):
    """装饰器：返回正常结果及错误信息"""

    @functools.wraps(func)
    def _func(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as err:
            return None, str(err)
        else:
            return res, None

    return _func


def origin_result(func):
    """装饰器：返回原始结果"""
    return func
    # @functools.wraps(func)
    # def _func(*args, **kwargs):
    #     res = func(*args, **kwargs)
    #     return res
    # return _func


def ensure_result(result_type: ResultType):
    """转换结果类型"""
    if result_type == ResultType.RESULT_OR_ERR_MSG:
        return result_or_err_msg
    if result_type == ResultType.RESULT_AND_ERR_MSG:
        return result_and_err_msg
    return origin_result
