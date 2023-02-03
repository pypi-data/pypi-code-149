from typing import Optional
from .objects import EnvPaths, EnvType
from .core import env_dict
from .core import env_src
from .utils import dict_utils
from .utils import path_utils


def docker_compose_dict(path: str):
    return env_dict.env_dict(path=path, env=EnvType.DOCKER_COMPOSE)


def dotenv_dict(path: str):
    return env_dict.env_dict(path=path, env=EnvType.DOTENV)


def dockerfile_dict(path: str):
    return env_dict.env_dict(path=path, env=EnvType.DOCKERFILE)


def unified_environment(paths: EnvPaths):
    result = {}
    path = paths.docker_compose_path
    if path_utils.path_exists(path):
        docker_compose_env = docker_compose_dict(path=path)
        result = dict_utils.safe_merge(result, docker_compose_env)
    path = paths.dockerfile_path
    if path_utils.path_exists(path):
        dockerfile_env = dockerfile_dict(path)
        result = dict_utils.safe_merge(result, dockerfile_env)
    path = paths.dotenv_path
    if path_utils.path_exists(path):
        dotenv_env = dotenv_dict(path)
        result = dict_utils.safe_merge(result, dotenv_env)
    return result


def update_envs(
    docker_compose_path: Optional[str] = None,
    dotenv_path: Optional[str] = None,
    dockerfile_path: Optional[str] = None,
    python_env_path: Optional[str] = "env.py",
):

    env_paths = EnvPaths(
        **dict(
            docker_compose_path=docker_compose_path,
            dotenv_path=dotenv_path,
            dockerfile_path=dockerfile_path,
            python_env_path=python_env_path,
        )
    )

    env = unified_environment(paths=env_paths)

    if env:

        if path_utils.path_exists(dotenv_path):
            dotenv_src = env_src.form_dotenv_src(env)
            path_utils.write_text(dotenv_path, dotenv_src)
        if path_utils.path_exists(python_env_path):
            if path_utils.path_exists(dotenv_path):
                python_src = env_src.form_python_env_src(
                    env=env, dotenv_path=dotenv_path, python_env_path=python_env_path
                )
                path_utils.write_text(python_env_path, python_src)
        if path_utils.path_exists(dockerfile_path):
            dockerfile_src = env_src.form_dockerfile_env_src(env, dockerfile_path)
            path_utils.write_text(dockerfile_path, dockerfile_src)
