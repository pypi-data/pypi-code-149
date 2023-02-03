from wfdanielpackagetest.dani import Dani

class Twinpackage:

    def __init__(self, name):
        self.name = name

    def package(self):
        model = Dani(self.name)
        model.tell()