from setuptools import setup, find_packages
from os.path import join, dirname

import src.uniqcharstest2

with open("requirements.txt") as dependency:
    requirements = dependency.read()

setup(
    name='uniqcharstest2',
    version=src.uniqcharstest2.__version__,
    author="Dihtiar Vadym",
    description="Count of uniq chars in string package",
    test_suite='tests',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={'console_scripts': ['main = src.uniqcharstest2.app.app:main']},
)
