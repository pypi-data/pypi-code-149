from pathlib import Path
import subprocess
from typing import Union


def open_process(cmd, cwd: Union[str, Path] = "."):
    return subprocess.Popen(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf8")


def check_error(p: subprocess.Popen, raise_error: bool = False):
    p.wait()
    if p.returncode > 0:
        msg = p.stderr.read().strip()
        print(msg)
        if raise_error:
            raise ValueError(msg)


def get_current_git_branch(cwd: Union[str, Path] = "."):
    """Get current branch infos
    Used command is "git branch --show-current"

    Args:
        cwd (str, optional): Location of git project. Defaults to the current location (i.e '.').

    Returns:
        str: resulting output
    """

    cmd = "git branch --show-current"
    p = open_process(cmd, cwd)
    check_error(p)
    return p.stdout.read().strip()


def get_full_commit(cwd: Union[str, Path] = "."):
    """Get full commit infos
    Used command is "git log -n 1"

    Args:
        cwd (str, optional): Location of git project. Defaults to the current location (i.e '.').

    Returns:
        str: resulting output
    """

    cmd = "git log -n 1"
    p = open_process(cmd, cwd)
    check_error(p)
    return p.stdout.read().strip()


def get_tag(cwd: Union[str, Path] = "."):
    """Get current tag infos
    Used command is "git describe --tags --abbrev=0"

    Args:
        cwd (str, optional): Location of git project. Defaults to the current location (i.e '.').

    Returns:
        str: resulting output
    """

    cmd = "git describe --tags --abbrev=0"
    p = open_process(cmd, cwd)
    check_error(p)
    return p.stdout.read().strip()


def get_short_commit_id(cwd: Union[str, Path] = "."):
    """Get infos
    Used command is "git rev-parse --short HEAD"

    Args:
        cwd (str, optional): Location of git project. Defaults to the current location (i.e '.').

    Returns:
        str: resulting output
    """

    cmd = "git rev-parse --short HEAD"
    p = open_process(cmd, cwd)
    check_error(p)
    return p.stdout.read().strip()
