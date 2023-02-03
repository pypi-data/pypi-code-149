from setuptools import setup, find_packages
from os.path import join, dirname

import src.uniqchars

with open("requirements.txt") as dependency:
    requirements = dependency.read()

setup(
    name='uniqchars',
    version=src.uniqchars.__version__,
    author="Dihtiar Vadym",
    description="Count of uniq chars in string package",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={'console_scripts': ['main = src.uniqchars.app.app:main']},
)
