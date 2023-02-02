from os import makedirs
from pathlib import Path
from shutil import rmtree
from typing import List, Sequence

from openapi_python_client.parser.errors import GeneratorError
from setuptools import Distribution

from setuptools_openapi_generator.config import Configuration
from setuptools_openapi_generator.generator import Generator


def _generate_clients(configuration: Configuration):
    generated_apis: List[str] = list()
    if configuration.basedir.is_dir():
        rmtree(configuration.basedir)
    makedirs(configuration.basedir)
    for source in sorted(configuration.sources):
        generator = Generator.from_source_and_dir(source, configuration.basedir)
        if isinstance(generator, GeneratorError):
            continue
        name_or_errors = generator.build()
        if isinstance(name_or_errors, Sequence):
            continue
        generated_apis.append(name_or_errors)
    with open(configuration.basedir.joinpath("__init__.py"), "w+") as init_file:
        init_file.writelines(f"import {api}\n" for api in generated_apis)


def generate_clients(distribution: Distribution):
    TOML_PATH = Path("pyproject.toml")
    configuration = Configuration.from_toml(TOML_PATH)
    _generate_clients(configuration)
