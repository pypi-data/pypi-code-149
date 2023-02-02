__version__ = "0.1.2-rc"

from .backend import JSONBackend
from .exceptions import FakeItException, RecordNotFound
from .fakeit import FakeIt
from .models import Mode, Record
