from .Typecheck import Typecheck


def typecheck(func: callable) -> None:
    _type = "FUNCTION"
    if "." in func.__qualname__: # Includes parent class, if any.
        _type = "METHOD"

    """Decorator used to enforce type-hints."""
    def decorated_function(*args, **kwargs) -> callable:
        Typecheck(_type, func, *args, **kwargs)
        result = func(*args, **kwargs)
        return result

    return decorated_function
