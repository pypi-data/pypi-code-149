#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdout
from os import environ
from logging import getLogger, StreamHandler, DEBUG
from argparse import ArgumentParser

logger = getLogger()
logger.setLevel(DEBUG)
handler = StreamHandler(stdout)
handler.setLevel(DEBUG)
logger.addHandler(handler)

PARSER = ArgumentParser()
PARSER.add_argument('--branch', type=str, default=environ.get('BRANCH', None), choices=[None, 'master', 'develop'])
PARSER.add_argument('--version', type=str, default=environ.get('VERSION', None))
PARSER.add_argument('--ip', type=str, default=environ.get('IP', '192.168.1.200'))
PARSER.add_argument('--password', type=str, default=environ.get('PASSWORD', 'elite2014'))

from .main import distcrab
distcrab(**vars(PARSER.parse_args()))
