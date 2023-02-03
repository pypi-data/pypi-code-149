from typing import Optional
from enum import Enum
from dataclasses import dataclass


class EnvType(Enum):

    DOTENV = 1
    DOCKERFILE = 2
    DOCKER_COMPOSE = 3
    NONE = 4


@dataclass(frozen=False, order=True)
class EnvPaths:
    docker_compose_path: Optional[str]
    dotenv_path: Optional[str]
    dockerfile_path: Optional[str]
    python_env_path: Optional[str]
