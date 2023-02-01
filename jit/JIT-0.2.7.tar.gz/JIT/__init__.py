__version__ = '0.2.7'
"""this python package is for running python profile faster."""

__metaclass__ = type
import time
import os
import subprocess
import sys
sys_path = os.path.abspath(".")
sys.path.append(sys_path)
# import _classes
# from _jit_internal import *
# from _namedtensor_internals import *
# from _ops import *
# from _overrides import *
# from _six import *
# from hub import *
import platform
if platform.system() == 'Windows':
    from JIT.tools.__short_time import *
else:
    from JIT.linux.__short_time import *
    from JIT.tools.__cpu_memory import *

__all__ = [
    'hub', '_six', '_tensor_docs', '_storage_docs', '_utils', '_utils_internal', 'serialization', '_overrides',
    '_jit_internal', '_classes', 'version', '__future__', '__config__'
]
