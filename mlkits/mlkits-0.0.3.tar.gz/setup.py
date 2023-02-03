from setuptools import setup, find_packages
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

setup (
    name = 'mlkits',
    version = '0.0.3',
    keywords = ["mlkits", "xgboost", "lightgbm"],
    description = "Common tools and training models for machine learning.",
    long_description = "Common machine learning tools and training models can be used to solve common regression and classification problems. The model includes the most commonly used XGBoost and LightGBT models, as well as the basic linear model and SVM that will be gradually improved in the future, and the DNN model based on PyTorch will be implemented. At the same time, feature processing and analysis will be gradually added, as well as comprehensive model index evaluation capabilities.",
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

    install_requires=[
        'Cython~=0.29.28',
        'dill~=0.3.5.1',
        'lightgbm~=3.3.2',
        'numpy~=1.22.3',
        'pandas~=1.4.2',
        'PyYAML~=6.0',
        'setuptools~=59.5.0',
        'storage~=0.0.4.3',
        'tqdm~=4.63.0',
        'typing_extensions~=4.4.0',
    ],

    packages=find_packages(where='.'),
    zip_safe = False
)


