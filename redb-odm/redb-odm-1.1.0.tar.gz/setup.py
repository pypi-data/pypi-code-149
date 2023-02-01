from __future__ import annotations

from pathlib import Path

import setuptools


def read_multiline_as_list(file_path: Path | str) -> list[str]:
    with open(file_path) as req_file:
        contents = req_file.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


def get_optional_requirements() -> dict[str, list[str]]:
    """Get dict of suffix -> list of requirements."""
    requirements_files = Path(".").glob(r"requirements-*.txt")
    requirements = {
        p.stem.split("-")[-1]: read_multiline_as_list(p) for p in requirements_files
    }
    return requirements


requirements = read_multiline_as_list("requirements.txt")
opt_requirements = get_optional_requirements()
opt_requirements["mongo"] = ["pymongo"]

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="redb-odm",
    version="1.1.0",
    author="Teia Labs",
    author_email="contato@teialabs.com",
    description="REsearch DataBase. An object-oriented NoSQL database interface.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teialabs/redb",
    packages=setuptools.find_namespace_packages(),
    keywords="database, milvus, mongo, json, interface, object-oriented",
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require=opt_requirements,
)
