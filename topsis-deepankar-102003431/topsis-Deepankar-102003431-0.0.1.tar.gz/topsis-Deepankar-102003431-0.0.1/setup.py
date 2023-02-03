from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Topsis package '
LONG_DESCRIPTION = 'TOPSIS method for multiple-criteria decision making (MCDM) Evaluation of alternatives based on multiple criteria using TOPSIS method.'

# Setting up
setup(
    name="topsis-Deepankar-102003431",
    version=VERSION,
    author="Deepankar Varma",
    author_email="<satwikdpshrit@gmail.com>",
    description=DESCRIPTION,
    
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'os', 'sys'],
    keywords=['python', 'topsis', 'package'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)