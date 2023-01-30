# -*- coding: utf-8 -*-
"""Functions that use iterators for efficient loops."""
import collections
import functools
import itertools
import operator
import statistics

empty = object()
consume_all = collections.deque(maxlen=0).extend  # Consume given iterator entirely.


def replacer(iterable, matcher, new_value, count=-1):
    """
    Make a generator that yields all occurrences of the old "iterable"
    replaced by "new_value".

    :param iterable:
    :param matcher: Callable to find occurrences. It is an occurrence if the matcher returns True.
    :param new_value: Any value to replace found occurrences.
    :param int count:
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.
    :rtype: Generator

    Examples:
        from pymince.iterator import replacer

        is_one = lambda n: n == 1
        replacer([1,2,3,1,2,3], is_one, None) # --> None 2 3 None 2 3
        replacer([1,2,3,1,2,3], is_one, None, count=1) # --> None 2 3 1 2 3
    """
    changed = 0
    for obj in iterable:
        if matcher(obj) and (count == -1 or changed < count):
            changed += 1
            yield new_value
        else:
            yield obj


def uniques(iterable, key=None):
    """
    Check if all the elements of a key-based iterable are unique.

    :param iterable:
    :param key: None or "Callable" to compare if iterable items.
    :rtype: bool

    Examples:
        from pymince.iterator import uniques

        uniques([1,2]) # --> True
        uniques([1,1]) # --> False
    """

    bag = set()
    add = bag.add

    values = map(key, iter(iterable)) if key else iter(iterable)
    result = (val for val in values if val in bag or add(val))
    return next(result, empty) is empty


def uniquer(iterable, key=None):
    """
    Make a generator that returns each element from iterable only once
    respecting the input order.

    Examples:
        from pymince.iterator import uniquer

        uniquer([1, 2, 3, 2]) # --> 1 2 3
    """

    get = key or (lambda x: x)
    bag = set()
    add = bag.add

    yield from (add(check) or v for v in iter(iterable) if (check := get(v)) not in bag)


def grouper(iterable, size):
    """
    Make a generator that returns each element being iterable
    with "size" as the maximum number of elements.

    :param iterable:
    :param int size: maximum size of element groups.
    :rtype: Generator

    Examples:
        from pymince.iterator import grouper

        groups = grouper([1, 2, 3, 4, 5], 2)
        list(list(g) for g in groups) # --> [[1, 2], [3, 4], [5]]
    """

    slicer = itertools.islice
    values = iter(iterable)
    while True:
        sliced = slicer(values, size)
        if it := ibool(sliced):
            yield it
        else:
            break


def consume(iterator, n=None):
    """
    Advance *iterator* by *n* steps. If *n* is ``None``, consume it
    entirely.

    Examples:
        from pymince.iterator import consume
        it = iter([1, 2])
        consume(it)
        next(it) # --> StopIteration
    """

    if n is None:
        consume_all(iterator)
    else:
        next(itertools.islice(iterator, n, n), None)


def all_equals(*iterables, key=None):
    """
    Check if the iterables are equal.
    If the "iterables" are empty, it returns True.

    :param iterables:
    :param key: None or "Callable" to compare if iterable items.
    :rtype: bool

    Examples:
        from pymince.iterator import all_equals

        all_equals() # --> True
        all_equals(range(1, 4), (1, 2, 3), {1, 2, 3}) # --> True
        all_equals((1, 2), (1, 2, 3)) # --> False
    """

    zipped = itertools.zip_longest(*iterables, fillvalue=empty)
    equals = functools.partial(all_equal, key=key)
    return all(map(equals, zipped))


def all_identical(left, right):
    """
    Check that the items of `left` are the same objects
    as those in `right`.

    :param Iterable[Any] left:
    :param Iterable[Any] right:
    :rtype: bool

    Examples:
        from pymince.iterator import all_identical

        a, b = object(), object()
        all_identical([a, b, a], [a, b, a]) # --> True
        all_identical([a, b, [a]], [a, b, [a]])  # --> False *new list object, while "equal" is not "identical"*
    """

    zipped = itertools.zip_longest(left, right, fillvalue=empty)
    return all(itertools.starmap(operator.is_, zipped))


def all_equal(iterable, key=None):
    """
    Check if all the elements of a key-based iterable are equals.

    :param iterable:
    :param key: None or "Callable" to compare if iterable items.
    :rtype: bool

    Examples:
        from pymince.iterator import all_equal

        all_equal([1, 1]) # --> True
        all_equal([1, 2]) # --> False
    """

    grouped = itertools.groupby(iterable, key=key)
    return has_only_one(grouped)


def all_distinct(iterable, key=None):
    """
    Check if all the elements of a key-based iterable are distinct.

    :param iterable:
    :param key: None or "Callable" to compare if iterable items.
    :rtype: bool

    Examples:
        from pymince.iterator import all_distinct

        all_distinct([1, 1]) # --> False
        all_distinct([1, 2]) # --> True
    """

    grouped = itertools.groupby(iterable, key=key)
    return all(has_only_one(group) for _, group in grouped)


def has_only_one(iterable):
    """
    Check if given iterable has only one element.

    :param iterable:
    :rtype: bool

    Examples:
        from pymince.iterator import has_only_one

        has_only_one([1]) # --> True
        has_only_one([1, 2]) # --> False
        has_only_one([]) # --> False
    """

    it = iter(iterable)
    return next(it, empty) is not empty and next(it, empty) is empty


def splitter(iterable, sep, key=None, maxsplit=-1, container=None):
    """
    Splits an iterable based on a separator.
    A separator will never appear in the output.

    :param iterable:
    :param sep: The delimiter to split the iterable.
    :param key
        A function to compare the equality of each element with the given delimiter.
        If the key function is not specified or is None, the element itself is used for compare.
    :param maxsplit:
        Maximum number of splits to do.
        -1 (the default value) means no limit.
    :param container: Callable to save the splits. By default tuple is used.

    :return: Generator with consecutive splits of "iterable" without the delimiter item.

    Examples:
        from pymince.iterator import splitter

        data = ("a", "b", "c", "d", "b", "e")
        split_n = splitter(data, "b")  # --> ("a",) ("c", "d") ("e",)
        split_1 = splitter(data, "b", maxsplit=1)  # --> ("a",) ("c", "d", "b", "e")
    """

    def is_not_sep(obj):
        return key(obj) != sep if key else obj != sep

    data = ibool(iterable)
    numb = 0
    wrap = container or tuple
    while data and (maxsplit == -1 or numb < maxsplit):
        taken = itertools.takewhile(is_not_sep, data)
        yield wrap(taken)
        numb += 1
    if data:
        yield wrap(data)


def pad_start(iterable, length, fill_value=None):
    """
    The function adds "fill_value" at the beginning of the iterable,
    until it reaches the specified length.
    If the value of the "length" param is less than the length of
    the given "iterable", no filling is done.

    :param iterable:
    :param int length: A number specifying the desired length of the resulting iterable.
    :param Any fill_value: Any value to fill the given iterable.
    :rtype: Generator

     Examples:
        from pymince.iterator import pad_start

        pad_start(("a", "b"), 3, fill_value="1") # --> "1" "a" "b"
        pad_start(("a", "b"), 3) # --> None "a" "b"
        pad_start(("a", "b", "c"), 3) # --> "a" "b" "c"
    """

    pool = tuple(iter(iterable))
    diff = length - len(pool)
    if diff:
        yield from itertools.repeat(fill_value, diff)
    yield from pool


def pad_end(iterable, length, fill_value=None):
    """
    The function adds "fill_value" at the finishing of the iterable,
    until it reaches the specified length.
    If the value of the "length" param is less than the length of
    the given "iterable", no filling is done.

    :param iterable:
    :param int length: A number specifying the desired length of the resulting iterable.
    :param Any fill_value: Any value to fill the given iterable.
    :rtype: Generator

     Examples:
        from pymince.iterator import pad_end

        pad_end(("a", "b"), 3, fill_value="1") # --> "a" "b" "1"
        pad_end(("a", "b"), 3) # --> "a" "b" None
        pad_end(("a", "b", "c"), 3) # --> "a" "b" "c"
    """

    fill = length
    for obj in iter(iterable):
        fill -= 1
        yield obj
    if fill > 0:
        yield from itertools.repeat(fill_value, fill)


def in_all(obj, iterables):
    """
    Check if the object is contained in all the given iterables.
    If the "iterables" are empty, return True.

    :param Any obj:
    :param iterables: iterable of iterables
    :rtype: bool

    Examples:
        from pymince.iterator import in_all

        in_all("a", (("a", "b"), "bcd")) # --> False
        in_all("a", (("a", "b"), "abc")) # --> True
        in_all("a", ()) # --> True
    """

    return all(obj in it for it in iter(iterables))


def in_any(obj, iterables):
    """
    Check if the object is contained in any of the given iterables.

    :param Any obj:
    :param iterables: iterable of iterables
    :rtype: bool

    Examples:
        from pymince.iterator import in_any

        in_any("a", (("a", "b"), "bcd")) # --> True
        in_any("a", (("b", "b"), "def")) # --> False
        in_any("a", ()) # --> False
    """

    return any(obj in it for it in iter(iterables))


class ibool:
    """
    Iterator class supporting __bool__.

    Examples:
        from pymince.iterator import ibool

        it = ibool((1, 2, 3))
        bool(it) # --> True
        list(it) # --> [1, 2, 3]
    """

    __slots__ = ("_it", "_queue")

    def __init__(self, iterable):
        self._it = iter(iterable)
        self._queue = collections.deque(maxlen=1)

    def __iter__(self):
        return self

    def __next__(self):
        return self._queue.popleft() if self._queue else next(self._it)

    def __bool__(self):
        """Returns True if the iterator is not consumed, False otherwise."""

        if self._queue:
            return True
        else:
            obj = next(self._it, empty)
            if obj is empty:  # Consumed
                return False
            else:
                self._queue.append(obj)
                return True


def centroid(coordinates):
    """
    Calculate the centroid of a set of n-dimensional coordinates.
    In Cartesian coordinates, the centroid is
    just the mean of the components.

    :param Iterable[Iterable[int]] coordinates: Iterable of n-dimensional coordinates.
    :rtype: Generator[int]

     Examples:
        from pymince.iterator import centroid

        coord = (((2, 2), (4, 4)))
        tuple(centroid(coord))  # --> (3, 3)
    """

    yield from map(statistics.mean, itertools.zip_longest(*coordinates))


def sub(iterable):
    """Return the subtraction of a non-empty iterable of numbers and sets."""

    return functools.reduce(operator.sub, iter(iterable))


def truediv(iterable):
    """Return the division of an non-empty iterable of numbers."""

    return functools.reduce(operator.truediv, iter(iterable))


def mul(iterable, start=1):
    """
    Return the multiplication of a 'start' value (default: 1)
    plus an iterable of numbers.

    When the iterable is empty, return the start value.
    """

    return functools.reduce(operator.mul, iter(iterable), start)
