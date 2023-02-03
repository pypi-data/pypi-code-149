class NotFoundLevel(Exception):
    def __init__(self, _level):
        self.level = _level

    def __str__(self):
        if self.level is None:
            return "Not found level"
        else:
            return f"Not found level: {self.level}"


class InvalidProcessRange(Exception):
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def __str__(self):
        return f"({self.minimum, self.maximum}) is invalid"
