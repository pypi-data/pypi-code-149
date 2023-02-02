import logging
import qafunnypet

class Dani():

    def __init__(self, message=None):
        self.message = message
        print(f"Hi dumb {self.message}")

    def use_loggin(self):
        if self.message is None:
            print("Youre logged foreing")
        else:
            logging.warning(f"Youre logged {self.message}")

    # def new_tamagochi(self, name, tamagochi_name):
    #     tamagochi = qatamagochi.Qatamagochi(name, tamagochi_name)
    #     tamagochi.speak()

    def new_pet(self, name, age):
        pet = qafunnypet.Qafunnypet(name, age)
        pet.present()
