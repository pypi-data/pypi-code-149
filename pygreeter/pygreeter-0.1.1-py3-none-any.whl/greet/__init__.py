from pygreeter.greet._utils import greet_with_urwid

class greet_client():
    def __init__(self, greet_number : int = 1) -> None:
        self.greet_number = greet_number

    def greet(self):
        print("Greetings Universe\n"*self.greet_number)

    def greet_using_urwid(self):
        greet_with_urwid()