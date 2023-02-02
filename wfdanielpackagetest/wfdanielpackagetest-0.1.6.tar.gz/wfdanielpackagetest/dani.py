import logging
from qatamagochi import Qatamagochi
from qafunnypet import Qafunnypet

class Dani():

    def __init__(self, message=None):
        self.message = message
        print(f"Hi dumb {self.message}")

    def use_loggin(self):
        if self.message is None:
            print("Youre logged foreing")
        else:
            logging.warning(f"Youre logged {self.message}")

    def new_tamagochi(self, name, tamagochi_name):
        tamagochi = Qatamagochi(name, tamagochi_name)
        tamagochi.speak()

    def new_pet(self, name, age):
        pet = Qafunnypet(name, age)
        pet.present()
