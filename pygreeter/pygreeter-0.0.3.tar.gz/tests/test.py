import pygreeter
print(pygreeter.__file__)

from pygreeter.greet import greet_client

t = greet_client(5)

t.greet()
t.greet_using_urwid()