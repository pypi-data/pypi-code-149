import datetime


name = "allan_tool"


def p(strings, *a):
    print(strings)


def t(*b) -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
