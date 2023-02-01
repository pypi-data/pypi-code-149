from setuptools import setup

DESCRIPTION = 'hotools: Tools for Python made by Hosoi.'
NAME = 'hotools'
AUTHOR = 'HOSOI Hiroyuki'
AUTHOR_EMAIL = 'hosoi0410@gmail.com'
URL = 'https://github.com/hosson/hotools'
LICENSE = 'MIT'
DOWNLOAD_URL = URL
VERSION = '0.1.1'
PYTHON_REQUIRES = '>=3.8'
PACKAGES = [
    'hotools'
]
KEYWORDS = 'tool'
CLASSIFIERS=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'
]
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=KEYWORDS,
)
