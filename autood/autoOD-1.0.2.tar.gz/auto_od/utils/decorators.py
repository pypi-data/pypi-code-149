from functools import wraps
from typing import Any, Callable

from auto_od.core.logger import logger
from auto_od.utils.info_messages import file_not_ex


def error_handler(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except KeyError:
            raise KeyError
        except FileNotFoundError:
            logger.info(file_not_ex.format('during the execution of function ' + func.__name__))
            return
    return wrapper

