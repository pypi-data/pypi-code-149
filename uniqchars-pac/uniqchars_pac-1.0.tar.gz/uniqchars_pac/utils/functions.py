from collections import Counter
from functools import wraps
from typing import Callable, List

# from exceptions import CustomTypeErrorException
from uniqchars_pac.utils import CustomTypeErrorException

cached_storage = {}


def cached_dict_decorator(func: Callable) -> Callable[[str], int]:
    """
    Decorator for work with cached dict
    Get value from cache if value in cached dict
    Add value to cache if value not in cached dict
    """
    storage = cached_storage

    @wraps(func)
    def check_if_str_in_cache(string: str) -> int:
        if not isinstance(string, str):
            raise CustomTypeErrorException(
                f"Wrong data type {type(string)}, must be a {str}"
            )
        if cached_value := storage.get(string):
            return cached_value
        else:
            count_uniq_chars = func(string)
            storage[string] = count_uniq_chars
            return count_uniq_chars

    return check_if_str_in_cache


@cached_dict_decorator
def count_uniq_chars_in_string(string: str) -> int:
    """Receive "str" and return count of uniq chars in string"""
    count_for_all_chars_in_string = Counter(string).values()
    count_uniq_chars = len(
        [number for number in count_for_all_chars_in_string if number == 1]
    )
    return count_uniq_chars


def count_uniq_chars_in_list(string_data: List[str]) -> List[int]:
    """Receive list["st1", "str2"] and return count of uniq chars list[count1, count2]"""
    if not isinstance(string_data, list):
        raise CustomTypeErrorException(
            f"Wrong data type {type(string_data)}, must be a {list}"
        )
    return list(map(count_uniq_chars_in_string, string_data))
