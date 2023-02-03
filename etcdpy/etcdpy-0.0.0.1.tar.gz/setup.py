#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from etcd3 import get_author, get_author_email, get_version
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def load_reqs(filename):
    with open(filename) as reqs_file:
        return [
            re.sub('==', '>=', line) for line in reqs_file.readlines()
            if not re.match(r'(\s*#|-r)', line)
        ]


requirements = load_reqs('requirements/base.txt')
test_requirements = load_reqs('requirements/test.txt')

setup(
    name="etcdpy",
    version=get_version(),
    description="Python client for etcd",
    long_description="This is a work in progress",
    author=get_author(),
    author_email=get_author_email(),
    url="https://github.com/candango/etcdpy",
    packages=[
        "etcd3",
        "etcd3.etcdrpc",
    ],
    package_dir={
        'etcd3': "etcd3",
        'etcd3.etcdrpc': "etcd3/etcdrpc",
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="etcd3",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    test_suite="tests",
    tests_require=test_requirements
)
