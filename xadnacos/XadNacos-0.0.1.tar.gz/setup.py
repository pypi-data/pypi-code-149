#!/usr/bin/env python
import setuptools
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
setuptools.setup(
    name='XadNacos',
    version='0.0.1',
    description='a package for nacos',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='xadocker',
    author_email='1793360097@qq.com',
    license='Apache License 2.0',
    url='',
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.20.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
