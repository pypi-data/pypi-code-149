from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'JWT token authentication decorator'

# Setting up
setup(
    name="timauthdecpkg",
    version=VERSION,
    author="KE",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['flask'],
    keywords=['python', 'flask', 'JWT', 'decorator','token'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ]
)
