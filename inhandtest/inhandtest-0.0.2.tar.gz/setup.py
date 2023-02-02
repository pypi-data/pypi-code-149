# -*- coding: utf-8 -*-
# @Time    : 2023/1/31 16:47:12
# @Author  : Pane Li
# @File    : setup.py
"""

setup

"""
from distutils.core import setup

setup(
    name='inhandtest',
    version='0.0.2',
    author='liwei',
    author_email='liwei@inhand.com.cn',
    description='inhand test tools, so easy',
    maintainer='liwei',
    maintainer_email='liwei@inhand.com.cn',
    py_modules=['inhandtest.tools'],
    long_description=open('README.md', 'r').read(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.7',
)
