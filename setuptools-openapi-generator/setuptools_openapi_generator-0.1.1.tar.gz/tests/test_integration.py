from os import chdir

from setuptools_openapi_generator.config import Configuration
from setuptools_openapi_generator.integration import _generate_clients


def test_clinets_are_generated():
    chdir("tests/sample_project/")
    configuration = Configuration.from_toml()
    _generate_clients(configuration)
