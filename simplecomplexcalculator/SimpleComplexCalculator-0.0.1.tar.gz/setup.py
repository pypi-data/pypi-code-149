#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 08:28:30 2023

@author: tom.ebermeyer
"""


from setuptools import setup

setup(
    name="SimpleComplexCalculator",
    version="0.0.1",
    author="Tom Ebermeyer",
    author_email="tom.ebermeyer@cpe.fr",
    description="Calculateur simple entre nombres complexes",
    packages=['Package_Calculator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)