#!/usr/bin/env python3
import os
import random
import json
import re
import sys
from collections import defaultdict
from functools import reduce

import codefast as cf
from rich import print
from typing import List, Union, Callable, Set, Dict, Tuple, Optional


def get_texts_from_dir(dirname:str)->List[str]:
    """ Get all texts from a directory. """
    return cf.l(cf.io.walk(dirname)).map(cf.js).flatten().map(lambda x: x['content']).data