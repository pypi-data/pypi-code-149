#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2023/2/3 23:41
# @Author : Rongrui Zhan
# @desc : 本代码未经授权禁止商用
import sys
from bonecommand import SingleCommand, MultiCommand
from bonecommand.utils import user_path


def install():
    if sys.platform == "darwin":
        pm = "brew"
    elif sys.platform == "linux":
        pm = "apt-get"
    else:
        pm = ""
    cmd = SingleCommand("apt-get")



"brew"
