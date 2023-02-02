"""
utils
"""

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
