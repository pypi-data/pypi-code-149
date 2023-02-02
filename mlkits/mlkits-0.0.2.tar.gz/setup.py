from setuptools import setup, find_packages
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

setup (
    name = 'mlkits',
    version = '0.0.2',
    keywords = ["mlkits", "xgboost", "lightgbm"],  
    description = "MLkits",
    long_description = "MLkits",
    license = "MIT Licence",

    url = "https://gitee.com/winter1991/mlkits", 
    author = "WangSihong",
    author_email = "wangsihong@live.com",

    entry_points={
        'console_scripts': [
            'mlkits-train = mlkits.cli.train:main',
            'mlkits-predict = mlkits.cli.predict:main',
        ],
    },

    packages=find_packages(where='.'),
    zip_safe = False
)


