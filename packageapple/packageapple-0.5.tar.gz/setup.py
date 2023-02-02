from setuptools import setup, find_packages
import os, pathlib
HERE  = pathlib.Path(__file__).parent 
setup(
    name='packageapple',
    packages=find_packages(),
    version = 0.5,
    package = ['math']
)