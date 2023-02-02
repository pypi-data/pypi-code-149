from setuptools import setup, find_packages
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

setup (
    name = 'mlkits',
    version = '0.0.1',
    keywords = ["mlkits", "xgboost", "lightgbm"],  
    description = "MLkits",
    long_description = "MLkits",
    license = "MIT Licence",

    url = "https://gitee.com/winter1991/mlkits", 
    author = "WangSihong",
    author_email = "wangsihong@live.com",

    packages=find_packages(where='.'),
    zip_safe = False
)


