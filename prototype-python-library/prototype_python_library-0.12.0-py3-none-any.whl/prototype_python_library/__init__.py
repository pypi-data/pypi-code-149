"""An empty python package."""

__version__ = "0.12.0"


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


def multiply(a: int, b: int) -> int:
    """Compute the multiplication of two integers.

    >>> multiply(2, 2)
    4

    Args:
        a (int): 1st integer
        b (int): 2nd integer

    Returns:
        The multiplication of a and b.

    """
    return a * b


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


def divide(a: int, b: int) -> int:
    """Compute division of two integers.

    >>> divide(4, 2)
    2

    Args:
        a (int): 1st integer
        b (int): 2nd integer

    Returns:
        int: division of a by b
    """
    return a // b


def power(b: int, e: int) -> int:
    """Compute an exponential.

    Args:
        b (int): the base
        e (int): the power

    Returns:
        int: power e of b
    """
    return b**e


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
