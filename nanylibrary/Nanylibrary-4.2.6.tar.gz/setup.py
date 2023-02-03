import os
import re
from setuptools import setup

_long_description = open('README.md').read()

setup(
    name = "Nanylibrary",
    version = "4.2.6",
    author = "Mohammad _GeNeRal_",
    author_email = "nanylibrary@gmail.com",
    description = (" library robot Rubika"),
    license = "MIT",
    keywords = ["rubika","bot","robot","library","rubikalib","rubikalib.ml","rubikalib.ir","rubika.ir","Nanylibrary","nanylibrary","Nany","nany","Rubika","Python"],
    url = "https://github.com/Nanymous/Nany_library.git",
    packages=['Nanylibrary'],
    long_description=_long_description,
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: Implementation :: PyPy",
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    ],
)