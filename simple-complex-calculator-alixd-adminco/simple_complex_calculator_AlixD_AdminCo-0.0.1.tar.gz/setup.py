import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "simple_complex_calculator_AlixD_AdminCo",
    version = "0.0.1",
    author = "Alix Deleule",
    author_email = "alixdeleule@cpe.fr",
    description = ("A calculator that can make simple operations with complexs."),
    keywords = "complex calculator",
    url = "",
    packages=['calculator'],
    long_description=read('README.md'),
)
