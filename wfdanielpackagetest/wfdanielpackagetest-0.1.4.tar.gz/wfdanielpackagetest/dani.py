import logging

class Dani():

    def __init__(self, message=None):
        self.message = message
        print(f"Hi dumb {self.message}")

    def use_loggin(self):
        if self.message is None:
            print("Youre logged foreing")
        else:
            print(f"Youre logged {self.message}")
