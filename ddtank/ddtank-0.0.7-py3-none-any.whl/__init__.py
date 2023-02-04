__version__ = '0.0.7'


import win32api
import win32con
import win32gui
import win32ui
import time
import string
import cv2
import numpy as np
import re
import os
import onnxruntime

from ctypes import windll
from threading import Thread

from .dl_script import load_onnx, build_preprocess, build_postprocess

VkKeyScanA = windll.user32.VkKeyScanA
