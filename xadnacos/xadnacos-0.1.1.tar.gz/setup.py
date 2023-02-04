#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', 'r', encoding='utf-8') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'requests>=2.20.0']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="KONE-XAD",
    author_email='1793360097@qq.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="python sdk for nacos",
    entry_points={
        'console_scripts': [
            'xadnacos=xadnacos.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='xadnacos',
    name='xadnacos',
    packages=find_packages(include=['xadnacos', 'xadnacos.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/KONE-XAD/xadnacos',
    version='0.1.1',
    zip_safe=False,
)
