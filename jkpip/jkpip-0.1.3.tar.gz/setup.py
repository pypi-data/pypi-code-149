#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: jackief
# Mail: jackief@foxmail.com
# Created Time: 2022-09-28 21:47:33
#############################################


from asyncio import subprocess
from setuptools import setup, find_packages

setup(
  name = "jkpip",
  version = "0.1.3",
  keywords = ("pip", "source","tool"),
  description = "pip source tool",
  long_description = "A tool for people change pip source easily",
  license = "MIT Licence",

  url = "https://github.com/a5225662/jkpipsource",
  author = "jackief",
  author_email = "jackief@foxmail.com",

  packages = find_packages(),
  include_package_data = True,
  platforms = "any",
  install_requires = []
)