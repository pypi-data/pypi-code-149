"""Install packages as defined in this file into the Python environment."""

from setuptools import setup, find_namespace_packages

setup(
    name="datamastery",
    author="Baran Kutluay",
    author_email="barankutluay19@gmail.com",
    # url="xxx",
    description="Datamastery is a Python package for data preprocessing and visualisation.",
    long_description="Datamastery is a Python package for data preprocessing and visualisation. It provides a set of functions to make it easier to work with data.",
    version="0.1.1a",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", exclude=["tests"]),
    install_requires=[
        "setuptools>=65.5.0",
        "matplotlib>=3.6.3",
        "numpy>=1.24.1",
        "seaborn>=0.12.2",
        "pandas>=1.5.3",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
    ],
)