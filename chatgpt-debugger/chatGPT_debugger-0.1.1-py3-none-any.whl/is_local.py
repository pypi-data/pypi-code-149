import inspect
import sys

def is_local(func_name):
    # Get the function from the locals or globals
    try:
        func = eval(func_name, sys._getframe(1).f_locals)
    except NameError:
        try:
            func = eval(func_name, sys._getframe(1).f_globals)
        except NameError:
            return False
    
    # Check if the function is local
    module = inspect.getmodule(func)
    return module.__name__ == "__main__"
