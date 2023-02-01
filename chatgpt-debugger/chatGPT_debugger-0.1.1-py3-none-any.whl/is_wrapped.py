import sys
import inspect


def is_wrapped(func_name, wrapper_func):
    # Get the function object from the name
    func = sys.modules[func_name]
    
    # Get the source code of the function
    src = inspect.getsource(func)

    # Check if the source code contains the wrapper function
    return wrapper_func.__name__ in src,func
