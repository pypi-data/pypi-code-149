"""An empty python package."""

__version__ = "0.9.0"


def add(a: int, b: int) -> int:
    """Compute the sum of two integers.

    >>> add(1, 2)
    3

    Args:
        a (int): 1st integer
        b (int): 2nd integer

    Returns:
        The sum of `a` and `b`.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Compute the difference between two integers.

    >>> subtract(5, 3)
    2

    Args:
        a (int): 1st integer
        b (int): 2nd integer

    Returns:
        The difference between `a` and `b`.
    """
    return a - b


def fib(n: int) -> int:
    """Compute an element in the fibonacci sequence.

    >>> fib(0)
    0

    Args:
        n (int): the position in the sequence.

    Returns:
        The nth element in the fibonacci sequence.
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)
