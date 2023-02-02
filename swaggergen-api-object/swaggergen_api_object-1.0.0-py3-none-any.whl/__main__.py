from __future__ import absolute_import
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

from swaggergen_api.swagger_generate import generate

generate()
