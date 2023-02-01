from __future__ import annotations
from django.http import JsonResponse
from django.utils.translation import gettext as _
from .jsons import ObjectEncoder
from typing import Optional
from enum import Enum


class BaseErrorEnum(Enum):
    """
    error code is negative number
    """
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg

    @classmethod
    def get_by_code(cls, code) -> Optional[BaseErrorEnum]:
        return next(filter(lambda x: x.code == code, cls.__members__.values()), None)


class ApiResult:
    def __init__(self, code, *, msg=None, msg_detail=None, data=None):
        self.code = code
        self.succ = (code == 200)
        self.msg = msg
        self.msg_detail = msg_detail
        self.data = data

    @classmethod
    def fail(cls, msg, code=400, msg_detail=None):
        return ApiResult(code, msg=msg, msg_detail=msg_detail)

    @classmethod
    def succ(cls, data=None):
        return ApiResult(200, data=data)

    @classmethod
    def succ_response(cls, data=None):
        return JsonResponse(cls.succ(data), encoder=ObjectEncoder, safe=False)

    @classmethod
    def fail_response(cls, msg, code=400, msg_detail=None):
        return JsonResponse(cls.fail(msg, code=code, msg_detail=msg_detail), encoder=ObjectEncoder, safe=False)

    @classmethod
    def error_response(cls, error_enum: BaseErrorEnum, msg_detail=None):
        return JsonResponse(cls.fail(error_enum.msg, code=error_enum.code, msg_detail=msg_detail), encoder=ObjectEncoder, safe=False)

    @classmethod
    def token_invalid(cls, msg=_('请先登录')):
        return cls.fail_response(msg, code=300)

    @classmethod
    def missing_param(cls, msg=_('缺少参数')):
        return cls.fail_response(msg)
