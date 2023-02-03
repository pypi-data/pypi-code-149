import sys
import time
from enum import Enum

from PColorLogging.error import InvalidProcessRange


class TypeProcess(Enum):
    BAR = "bar"
    PERCENT = "percent"
    NUMBER = "number"


class ProcessConsole:
    def __init__(self, minimum: int, maximum: int, _type: TypeProcess = TypeProcess.NUMBER):
        if minimum > maximum:
            raise InvalidProcessRange(self.minimum, self.maximum)
        self.minimum = minimum
        self.maximum = maximum
        self.type = _type

    def set_minimum(self, minimum: int):
        if self.maximum < minimum:
            raise InvalidProcessRange(minimum, self.maximum)
        self.minimum = minimum

    def set_maximum(self, maximum: int):
        if self.minimum > maximum:
            raise InvalidProcessRange(self.minimum, maximum)
        self.maximum = maximum

    def set_process_type(self, _type: TypeProcess):
        self.type = _type

    def loading(self):
        print("Loading...")
        for i in range(self.minimum, self.maximum):
            time.sleep(0.1)
            sys.stdout.write("\u001b[1000D" + str(i + 1) + "%")
            sys.stdout.flush()
