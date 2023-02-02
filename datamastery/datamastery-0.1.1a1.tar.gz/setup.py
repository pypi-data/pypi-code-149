from setuptools import setup, find_packages

setup(
    name="datamastery",
    author="Baran Kutluay",
    author_email="barankutluay19@gmail.com",
    description="Datamastery is a Python package for data preprocessing and visualisation.",
    long_description="Datamastery is a Python package for data preprocessing and visualisation. It provides a set of functions to make it easier to work with data.",
    version="0.1.1a1",
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=[
        "setuptools>=65.5.0",
        "matplotlib>=3.6.3",
        "numpy>=1.24.1",
        "seaborn>=0.12.2",
        "pandas>=1.5.3",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
