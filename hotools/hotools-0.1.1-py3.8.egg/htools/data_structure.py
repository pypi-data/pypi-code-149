"""Functions about data structure
"""


class DictionaryCounter:
    """Count numbers for each key.
    """
    def __init__(self):
        self.dictionary = {}

    def count(self, key: str, number=1):
        if key not in self.dictionary:
            self.dictionary[key] = number
        else:
            self.dictionary[key] += number

    def get_count(self, key) -> int:
        if key in self.dictionary:
            return self.dictionary[key]
        return 0

    def get_total_count(self) -> int:
        """Get a sum of all keys.
        """
        total = 0

        for v in self.dictionary.values():
            total += v

        return total
