#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:39:53 2023

@author: J. Lengyel, January 2023, janka.lengyel@ens-lyon.fr
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
   name='lompy',
   version='0.1.12',
   author='S.G. Roux, J. Lengyel',
   author_email='jankalengyel@gmail.com',
   packages=find_packages(),
   url='https://gitlab.com/sroux67/LomPy',
   license='GNU AGPLv3',
   description='Local Multiscale Analysis of Marked Point Processes',
   long_description = readme,
   install_requires=['pyfftw','numpy','geopandas','matplotlib'],
   platforms=['any'],
   entry_points={"console_scripts": ["lompy = lompy.lompy:main"]},
   #long_description=open('README.txt').read(),
   #install_requires=[],
)