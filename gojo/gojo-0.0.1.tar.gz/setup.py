from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = ''

# Setting up
setup(
    name="gojo",
    version=VERSION,
    author="Binod Expert",
    author_email="binodexpert@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description="",
    packages=find_packages(),
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)