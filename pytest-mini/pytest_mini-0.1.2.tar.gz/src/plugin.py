#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : tingbai
# @Time     : 2023/2/3 23:49
# @File     : plugin.py
# @Project  : PyCharm
import inspect
import os
import time

from src.allureoperator import attach_png
from src.constant import TEST_PIC
from src.logoperator import LogOperator

logger = LogOperator(__name__)


class Plugin:

    @staticmethod
    def pytest_assume_fail(lineno, entry):
        """
        assume 断言报错截图
        """
        print(entry)
        for i in inspect.stack():
            if os.path.split(i.filename)[1].startswith('test_'):
                try:
                    for k, v in i.frame.f_locals.items():
                        if hasattr(v, 'native'):
                            attach_png(f'{TEST_PIC}/{int(time.time())}.png', f"失败截图_{int(time.time())}", v)
                            break
                except Exception as e:
                    logger.error(f"失败截图异常:{e}")

    @staticmethod
    def pytest_collection_modifyitems(session, items):
        """
        修改用例执行顺序
        :param session: 会话信息
        :param items: 用例列表
        :return:
        """
        for item in items:
            item.name = item.name.encode("utf-8").decode("unicode_escape")
            item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        logger.info(f"收集到的测试用例:{items}")
