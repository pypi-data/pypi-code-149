#!/usr/bin/env python
# coding: utf-8

# Copyright (c) nicolvisser.
# Distributed under the terms of the Modified BSD License.

import pytest

from ..slider2d import Slider2D


def test_example_creation_blank():
    w = Slider2D()
    assert w.value == [0., 0.]
    assert w.xlim == [0., 1.]
    assert w.ylim == [0., 1.]
    assert w.width == 100
    assert w.height == 100
