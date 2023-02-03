# -*- coding: utf-8

"""Utility functions."""

import os
from pathlib import Path
from typing import Union

import numpy as np
from jpype import getDefaultJVMPath
import jdk


def parse_numeric(value: str) -> Union[int, float]:
    """Parse a string representation of a number."""
    if not len(value):
        return np.nan
    return int(value) if value.lstrip(" -+").isdigit() else float(value)


def parse_numeric_to_null(value: str) -> Union[int, float]:
    """Parse a string representation of a number and return NaN."""
    return np.nan


def jre_available():
    """Detects if a Java Runtime Environment exists."""
    try:
        # Full installation of the JRE
        getDefaultJVMPath()
        return True
    except:
        other_path = list(Path(jdk._JRE_DIR).rglob('server/jvm.dll'))
        if len(other_path) > 0:
            # JRE installed with jdk
            return True
        return False


def install_jre(version: str = '11'):
    """Ensures the JVM is available and has started."""
    if not jre_available():
        jdk.install(version, jre=True)
    jdk_path = list(Path(jdk._JRE_DIR).rglob('server/jvm.dll'))
    if len(jdk_path) > 0:
        return str(jdk_path[0])
    else:
        return getDefaultJVMPath()
