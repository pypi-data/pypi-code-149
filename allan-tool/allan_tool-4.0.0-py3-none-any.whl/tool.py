# python 3.7

"""
一个简洁的打印函数由p() 代替 print()
time: 2023-01-30
author: Allan Wang
PS: 想念前任
"""
import datetime


def p(strings, *a):
    print(strings)


def t(*b) -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')