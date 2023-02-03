"""
utils
"""
import re
import base64
from os import makedirs
from os.path import isdir, dirname
from functools import wraps
from collections import Counter



def open_decorator(built_in_open):
    """
    内置函数 open 装饰器
    作用: 写或追加模式下 创建不存在的目录
    """
    @wraps(built_in_open)
    def wrapper(file, mode="r", **kwargs):
        # 判断 mode 是否属于写或追加模
        # collections.Counter 统计可迭代对象 每项出现的次
        # itertools.product 求多个可迭代对象的笛卡尔积
        create_mode = [Counter(i+j) for i in ("w", "a") for j in ("b", "+", "b+", "")]
        # 创建目录
        if isinstance(mode, str) and Counter(mode) in create_mode:
            folder = dirname(file)
            if not isdir(folder):
                makedirs(folder)
        return built_in_open(file, mode, **kwargs)
    return wrapper

make_open = open_decorator(open)


# base64 数据类型 正则表达式判断
B64_RE_PATTERN   = re.compile(r"^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$")
B64_RE_PATTERN_B = re.compile(rb"^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$")


def is_b64data(data: str or bytes) -> bool:
    """
    判断base64数据类型 return: bool
    """
    if isinstance(data, bytes):
        return bool(B64_RE_PATTERN_B.match(data))
    if isinstance(data, str):
        return bool(B64_RE_PATTERN.match(data))
    # str 或 bytes 以外类型返回 False
    return False


def tobytes_from_base64(data: str or bytes, encoding="UTF-8"):
    """
    base64数据类型 转化为bytes
    如果不为base64数据类型 则返回原始数据
    """
    if (
        not isinstance(data, (str, bytes))
        or not is_b64data(data)
    ):
        return False, data
    if isinstance(data, str):
        data = data.encode(encoding)
    return True, base64.b64decode(data)
