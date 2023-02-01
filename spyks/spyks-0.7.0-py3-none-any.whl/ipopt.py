# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Generates equations.txt and parameters.txt for makecode (not implemented)"""
# python 3 compatibility
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

from spyks.codegen import simplify_equations
from spyks.core import n_forcing, n_params, n_state

log = logging.getLogger("spyks")  # root logger


def discretize(model):
    pass
