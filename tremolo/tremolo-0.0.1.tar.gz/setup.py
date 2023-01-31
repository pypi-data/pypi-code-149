#!/usr/bin/env python

from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='tremolo',
    packages=['tremolo'],
    version='0.0.1',
    license='MIT',
    author='nggit',
    author_email='contact@anggit.com',
    description='Tremolo',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nggit/tremolo',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
