from pathlib import Path

__version__ = "0.0.1"
__version__bak = __version__  # This version is backup for MLKitsConfig.reset_qlib_version
import os
from typing import Union
import yaml
import logging
import platform
import subprocess
from .log import get_module_logger


# init mlkits
def init(**kwargs):
    from .config import C

    C.set(**kwargs)
    get_module_logger.setLevel(C.logging_level)


