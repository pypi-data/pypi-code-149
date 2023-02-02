#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 08:56:34 2023

@author: benoit.jomain
"""

from setuptools import setup

setup(
      name = 'Simple_Complex_Calulator',
      version = '0.1',
      packages = ["Package_Calculator"],
      install_requires = [],
      include_package_data = True,
      author = 'Benoit-Jomain',
      author_email = 'benoit.jomain@cpe.fr',
      description = 'Réaliser les différentes opérations élémentaires entre 2 nombres complexes : addition,différence,multiplication,division',
      classifiers = [
              'Programming Language :: Python :: 3',
              ],
      )