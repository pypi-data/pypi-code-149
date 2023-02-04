import pathlib
from setuptools import setup, find_packages


setup(
    name="o2m",
    version="0.0.0",
    author="Chivier Humber",
    long_description_content_type="text/markdown",
    # url="https://github.com/Chivier/H2O2H",
    long_description="# README\n",
    entry_points={
        "console_scripts": ["obs2medium=o2m.o2m:o2m"],
    },
    license="MIT",
    keywords="translator",
    packages=find_packages(),
)

