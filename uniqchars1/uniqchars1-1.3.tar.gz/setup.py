from setuptools import setup, find_packages
from os.path import join, dirname

import src.uniqchars1

with open("requirements.txt") as dependency:
    requirements = dependency.read()

setup(
    name='uniqchars1',
    version=src.uniqchars1.__version__,
    author="Dihtiar Vadym",
    description="Count of uniq chars in string package",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={'console_scripts': ['main = src.uniqchars1.app.app:main']},
)
