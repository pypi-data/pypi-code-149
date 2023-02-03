from functools import wraps

def estimated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Estimate: {result}")
        return result
    return wrapper