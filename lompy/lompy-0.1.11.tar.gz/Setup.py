#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:39:53 2023

@author: J. Lengyel, January 2023, janka.lengyel@ens-lyon.fr
"""

from setuptools import setup, find_packages

setup(
   name='lompy',
   version='0.1.11',
   author=['Stéphane G. Roux, Janka Lengyel'],
   author_email='jankalengyel@gmail.com',
   #package_dir={'': 'lompy'},
   packages=find_packages(),
   #py_modules=['lompy'],
   url='https://gitlab.com/sroux67/LomPy',
   license='GNU AGPLv3',
   description='Local Multiscale Analysis of Marked Point Processes',
   entry_points={"console_scripts": ["lompy = lompy.lompy:main"]},
   #long_description=open('README.txt').read(),
   #install_requires=[],
)