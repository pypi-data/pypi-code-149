#!/usr/bin/env python
# coding: utf-8

# Copyright (c) nicolvisser.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget, ValueWidget
from traitlets import Unicode, List, Float, Int
from ._frontend import module_name, module_version


class Slider2D(ValueWidget, DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('Slider2DModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('Slider2DView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    # Your widget state goes here. Make sure to update the corresponding
    # JavaScript widget state (defaultModelProperties) in widget.ts
    value = List(Float, [0., 0.]).tag(sync=True)
    xlim = List(Float, [0., 1.]).tag(sync=True)
    ylim = List(Float, [0., 1.]).tag(sync=True)
    width = Int(100).tag(sync=True)
    height = Int(100).tag(sync=True)
