import sys
from pathlib import Path
from typing import Any, Dict, Set

from pydantic import BaseModel


def read_pyproject(name: str = "pyproject.toml") -> Dict[str, Any]:
    with open(name, encoding="UTF-8") as file:
        contents = file.read()
    return lazy_toml_load(contents)


def lazy_toml_load(data: str) -> Dict[str, Any]:
    if sys.version_info >= (3, 11):
        from tomllib import loads
    else:
        from tomli import loads

    return loads(data)


class Configuration(BaseModel):
    basedir: Path
    sources: Set[str]

    @classmethod
    def from_toml(
        cls,
        toml_path: Path = Path("pyproject.toml"),
        tool_name: str = "setuptools_openapi_generator",
    ) -> "Configuration":
        pyproject_data = read_pyproject(str(toml_path))
        tool_section: Dict[str, Any] = pyproject_data["tool"][tool_name]
        return cls.parse_obj(tool_section)
