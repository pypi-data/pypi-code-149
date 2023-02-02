from pathlib import Path

from setuptools_openapi_generator.config import Configuration


def test_load_config_from_toml():
    assert Configuration(
        basedir=Path("src/sample_project/apis/"),
        sources={
            "https://raw.githubusercontent.com"
            "/OAI/OpenAPI-Specification/main/examples/v3.0/link-example.json",
            "api_definitions/petstore.json",
        },
    ) == Configuration.from_toml(toml_path="tests/sample_project/pyproject.toml")
