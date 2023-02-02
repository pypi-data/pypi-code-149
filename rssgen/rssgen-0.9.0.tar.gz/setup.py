#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import rssgen.version

packages = ['rssgen']

setup(name='rssgen',
      packages=packages,
      version=rssgen.version.version_full_str,
      description='RSS Generator',
      author='Mustafa Gezen',
      author_email='mustafa@gezen.no',
      url='https://github.com/mstg/rssgen',
      keywords=['RSS'],
      license='FreeBSD and LGPLv3+',
      install_requires=['python-dateutil'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: GNU Lesser General Public License v3 ' +
        'or later (LGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: XML'
        ],
      test_suite="tests",
      long_description='''\
Rssgenerator
=============

This module can be used to generate web feeds in both ATOM and RSS format. It
has support for extensions. Included is for example an extension to produce
Podcasts.

It is licensed under the terms of both, the FreeBSD license and the LGPLv3+.
Choose the one which is more convenient for you. For more details have a look
at license.bsd and license.lgpl.
''')
