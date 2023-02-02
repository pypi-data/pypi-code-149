from pathlib import Path
from typing import Optional, Tuple, Union
from urllib.parse import urlparse

from openapi_python_client import MetaType, Project, _get_document
from openapi_python_client.config import Config
from openapi_python_client.parser import GeneratorData
from openapi_python_client.parser.errors import GeneratorError


def _get_path_or_url(source: str) -> Tuple[Optional[Path], Optional[str]]:
    if urlparse(source).scheme == "":
        return (Path(source), None)
    else:
        return (None, source)


class Generator(Project):
    def __init__(
        self,
        *,
        openapi: GeneratorData,
        config: Config,
        base_dir: Path = Path.cwd(),
        custom_template_path: Optional[Path] = None,
    ) -> None:
        super().__init__(
            openapi=openapi,
            meta=MetaType.NONE,
            config=config,
            custom_template_path=custom_template_path,
        )
        self.project_dir = base_dir
        self.package_dir = base_dir.joinpath(self.package_name)

    @classmethod
    def from_source_and_dir(
        cls, source: str, base_dir: Path
    ) -> Union["Generator", GeneratorError]:
        path, url = _get_path_or_url(source)
        config = Config()
        data_dict = _get_document(url=url, path=path, timeout=config.http_timeout)
        if isinstance(data_dict, GeneratorError):
            return data_dict
        openapi = GeneratorData.from_dict(data_dict, config=config)
        if isinstance(openapi, GeneratorError):
            return openapi
        return cls(openapi=openapi, config=config, base_dir=base_dir)
