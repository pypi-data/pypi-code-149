import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='rickquests',
    version='3.1.0',
    description='Typosquatting talk example, do not use.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/psf/requests',
    author='Not. A. RealPackage',
    author_email='fake.package@dont.use',
    license='Apache',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)                                                  