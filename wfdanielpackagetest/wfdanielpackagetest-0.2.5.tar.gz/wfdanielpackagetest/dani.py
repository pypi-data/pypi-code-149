import logging

class Dani:

    def __init__(self, name=None):
        self.name = name
        if name is None:
            print("Why you dont want to tell me your name?")
        else:
            print(f"Hi dumb {self.name}")

    def use_loggin(self):
        if self.name is None:
            logging.warning(f"Youre logged but i dont know you")
        else:
            logging.warning(f"Youre logged {self.name}")

    def speak(self):
        if self.name is None:
            print("I dont know you dude, forget about")
        else:
            print(f"Hey {self.name} you are really cool")
