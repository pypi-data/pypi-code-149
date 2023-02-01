import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.2'
PACKAGE_NAME = 'OwlModelExtractor'
AUTHOR = 'KnowledgeFactory'
AUTHOR_EMAIL = ''
URL = 'https://umane.everis.com/git/KFSEMBU/initiatives/fairify/owlmodelextractor.git'

LICENSE = 'MIT'
DESCRIPTION = 'Librería que nos permite acceder a un fichero OWL tanto local como remoto y modelar la información que contiene'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'importlib-resources==5.10.2',
    'isodate==0.6.1',
    'numpy==1.24.1',
    'Owlready2==0.39',
    'pandas==1.5.3',
    'pyparsing==3.0.9',
    'python-dateutil==2.8.2',
    'pytz==2022.7.1',
    'rdflib==6.2.0',
    'six==1.16.0'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)