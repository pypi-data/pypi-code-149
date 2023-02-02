def iter_alphabetic_sort(array: list | tuple | set) -> list:
    l = list(array)
    l.sort()
    return type(array)(l)

def bisect(list: list | tuple | set, query):
    """
    Searches through a list or other iterable using an iterative binary-search algorithm. \n
    Returns the index of the query if found, otherwise returns -1. \n
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == query:
            return mid
        elif list[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return -1
