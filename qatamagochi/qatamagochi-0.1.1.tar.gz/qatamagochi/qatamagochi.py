from .tamagochiowner import Tamagochiowner

class Qatamagochi(Tamagochiowner):
    def __init__(self, name=None, tamagochi_name=None):
        super().__init__(name)
        # super().show()
        self.owner = name
        self.name = tamagochi_name

    def speak(self):
        if self.owner is None and self.name is None:
            print(f"Hi i dont know my name and my owner name's too")
        elif self.owner != None and self.name is None:
            print(f"Hi i dont know my name but my owner is {self.owner}")
        elif self.owner is None and self.name != None:
            print(f"Hi my name is {self.name} and i dont know my owner :(")
        else:
            print(f"Hi my name is {self.name} and my owner is {self.owner}")
            