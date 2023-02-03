from setuptools import setup, find_packages
from os.path import join, dirname

import src.uniqcharstest8

with open("requirements.txt") as dependency:
    requirements = dependency.read()

setup(
    name='uniqcharstest8',
    version=src.uniqcharstest8.__version__,
    author="Dihtiar Vadym",
    description="Count of uniq chars in string package",
    test_suite='tests',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={'console_scripts': ['main = src.uniqcharstest8.app.app:main']},
)
