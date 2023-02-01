



from huble.error.exceptions import FunctionRuntimeException


def function_error_handling(name: str, *args, **kwargs):
  
      """
      Decorator for handling errors while calling functions in Huble.
      """
      def decorator(func):
        try:
          func(*args, **kwargs)
        except Exception as e:
          raise FunctionRuntimeException(f"{name} failed to execute. Error: {e}")
      return decorator