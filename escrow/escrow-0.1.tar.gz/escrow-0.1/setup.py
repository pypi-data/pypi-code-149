from setuptools import setup, find_packages

setup(
    name='escrow',
    version='0.1',
    description='This script is a import and wrapper for all my variables and workflows',
    author='var',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
)