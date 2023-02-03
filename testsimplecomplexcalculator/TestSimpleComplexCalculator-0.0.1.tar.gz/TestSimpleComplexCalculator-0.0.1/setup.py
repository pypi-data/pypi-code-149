from setuptools import setup
import setuptools

setup(
    name='TestSimpleComplexCalculator',
    version='0.0.1',
    author="Perrichet Théotime",
    description="TestSimpleComplexCalculator est un package \
    permmetant de faire des tests sur les principe de packaging en Python",
    license='GNU GPLv3',
    python_requires ='>=3.4',
    package_dir={"": "Package_Calculator"},
    packages=setuptools.find_namespace_packages(where="Calculator"),
)

