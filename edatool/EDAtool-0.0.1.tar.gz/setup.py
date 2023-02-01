from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'EDA_TOOL'
LONG_DESCRIPTION = 'EDA TOOL'

# Setting up
setup(
    name="EDAtool",
    version=VERSION,
    author="Ketto",
    author_email="analytics@ketto.org",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="MIT License",
    packages=find_packages(),
    install_requires=['streamlit'],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
