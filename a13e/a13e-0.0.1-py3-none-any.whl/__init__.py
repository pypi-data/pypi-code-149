import sys

# In my test environment, the pypi module will not be found without adding this.
for i in filter(
        lambda path: path.endswith(r'\\Lib\\site-packages'),
        sys.path
):
    sys.path.append(i.removesuffix(r'\\Lib\\site-packages') + r'\\lib\\site-packages')

from importlib.metadata import version

from a13e.tag import set_tag
from a13e.api import recognize, random_recognize

try:
    __version__ = version("a13e")
except Exception:
    __version__ = None

__all__ = ['recognize', 'random_recognize', 'set_tag']
