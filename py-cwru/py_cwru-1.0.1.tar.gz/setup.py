#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='py_cwru',
    version='1.0.1',
    author='Xu Fangzheng',
    author_email='fonderxu@163.com',
    url='',
    description=u'README.md',
    packages=['py-cwru'],
    install_requires=[],
    entry_points={
        'console_scripts': []
    },
    readme="README.md",
    long_description=long_description,
    long_description_content_type='text/markdown'
)

