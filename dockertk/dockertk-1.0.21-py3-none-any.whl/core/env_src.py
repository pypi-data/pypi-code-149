from typing import Dict
from ..utils import path_utils


def form_dotenv_src(__dict: Dict[str, str]):
    env_lines = [f"{key}={value}" for key, value in __dict.items()]
    env_lines.sort()
    return "\n".join(env_lines) if env_lines else ""


def infer_type(__obj):
    base = str(__obj).strip().lower()
    base_len = len(base)
    digits = "".join(c for c in base if c.isdigit())
    dots = "".join(c for c in base if c == ".")

    digits_len = len(digits)
    dots_len = len(dots)
    if digits_len == base_len:
        result = "int"
    elif dots_len + digits_len == base_len:
        result = "float"
    elif base in ("true", "false"):
        result = "bool"
    else:
        result = "str"
    return result


def form_python_env_src(env: Dict[str, str], dotenv_path: str, python_env_path: str):
    keys = list(env.keys())
    keys.sort()
    value_types = [infer_type(env[key]) for key in keys]

    env_fields_src = "\n".join(
        f"    {key}:Optional[{value_type}] = Field(default=None)"
        for (key, value_type) in zip(keys, value_types)
    )
    env_init_src = "env = Env(**{" + "key:os.environ.get(key) for key in Env.keys()})\n"

    result = f"""
import os
from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv('{dotenv_path}')

class Env(BaseModel):

    @classmethod
    def keys(cls):
        return cls.__fields__.keys()

{env_fields_src}

{env_init_src}

    """

    if path_utils.path_exists(python_env_path):
        env_src = path_utils.read_text(python_env_path)
        if "env = " in env_src:
            env_src = env_src.split("env = ", 1)[1]
            env_src = "\n".join(
                line for line in env_src.splitlines(keepends=False)[1:] if line
            )
            while result.endswith("\n\n"):
                result = result.removesuffix("\n")
            while env_src.startswith("\n"):
                env_src = env_src.removeprefix("\n")
            result += f"\n{env_src}"
    return result


def form_dockerfile_env_src(
    __dict: Dict[str, str], dockerfile_path: str = "Dockerfile"
):
    dockerfile_lines = []
    if path_utils.path_exists(dockerfile_path):
        dockerfile_env_src = path_utils.read_text(dockerfile_path)
        dockerfile_lines = dockerfile_env_src.splitlines(keepends=False)
    dockerfile_lines = [line for line in dockerfile_lines if not line.startswith("ENV")]
    endline = ""
    if dockerfile_lines:
        endline = dockerfile_lines[-1]
        dockerfile_lines = dockerfile_lines[:-1]
    env_lines = [f"ENV {key}={value}" for key, value in __dict.items()]
    result = dockerfile_lines + env_lines + [endline]
    return "\n".join(result)
