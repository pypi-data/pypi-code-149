"""Run upon call of pip install cri-diagnose."""

from pathlib import Path

from setuptools import setup

here = Path(__file__).parent
name = "cri-diagnose"

setup(name=name, version="0.0.0.dev0")
